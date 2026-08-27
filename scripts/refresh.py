#!/usr/bin/env python3
"""Refresh the documentation mirror from its upstream Zendesk sources.

Runs unattended. Every source below is a public, unauthenticated Zendesk Help
Center API, so this needs no secrets and can run anywhere, including GitHub
Actions on a schedule.

What it deliberately does NOT do: touch `composer-api/`. Those specs come from
a running Composer instance, not from a docs site, and an instance is not
reachable from CI. They are refreshed by hand and each is named for the box it
came from. See composer-api/ENDPOINTS.md.

Exit codes: 0 nothing changed, 0 changes written, 1 a source failed. A source
failing must be loud rather than silently leaving the mirror stale, which is
the whole failure mode this script exists to end.
"""
from __future__ import annotations
import json, os, re, sys, time, urllib.request, urllib.error, pathlib, argparse

ROOT = pathlib.Path(__file__).resolve().parent.parent

SOURCES = [
    {"key": "logi-composer-current/v25", "host": "logi-composer-v25.insightsoftware.com",
     "product": "Logi Composer v25"},
    {"key": "logi-composer-current/v26", "host": "logi-composer-v26.insightsoftware.com",
     "product": "Logi Composer v26"},
]

UA = "logi-si-docs-mirror/1.0 (+https://github.com/isw-da/logi-si-docs)"


def fetch(url: str, tries: int = 4) -> dict:
    """GET JSON with backoff. Zendesk rate-limits, and a 429 mid-run would
    otherwise look like a source that has lost half its articles."""
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            last = e
            if e.code == 429:
                wait = int(e.headers.get("Retry-After", 30))
                print(f"    rate limited, waiting {wait}s", flush=True)
                time.sleep(wait)
                continue
            raise
        except Exception as e:  # transient network
            last = e
            time.sleep(2 ** attempt)
    raise RuntimeError(f"giving up on {url}: {last}")


def slug(s: str, maxlen: int = 80) -> str:
    s = re.sub(r"[^\w\s-]", "", (s or "").lower()).strip()
    s = re.sub(r"[\s_]+", "-", s)
    return (s[:maxlen].rstrip("-") or "untitled")


def html_to_text(html: str) -> str:
    """Convert Zendesk article HTML to markdown.

    Uses markdownify, which reproduces the existing corpus byte for byte on the
    articles checked. A hand-rolled regex converter was tried first and silently
    dropped every cross-reference link and broke headings onto two lines, which
    would have degraded 1,388 files while appearing to be a routine refresh.
    """
    if not html:
        return ""
    from markdownify import markdownify as _md
    return re.sub(r"\n{3,}", "\n\n", _md(html, heading_style="ATX", bullets="*")).strip()


def pull_source(src: dict, dry: bool) -> dict:
    host, key, product = src["host"], src["key"], src["product"]
    base = ROOT / key
    print(f"  {key}  <-  {host}", flush=True)

    sections = {}
    url = f"https://{host}/api/v2/help_center/en-us/sections.json?per_page=100"
    while url:
        d = fetch(url)
        for s in d.get("sections", []):
            sections[s["id"]] = s.get("name", "")
        url = d.get("next_page")

    articles, url = [], f"https://{host}/api/v2/help_center/en-us/articles.json?per_page=100"
    while url:
        d = fetch(url)
        articles.extend(d.get("articles", []))
        url = d.get("next_page")

    upstream = len(articles)
    before = 0
    mpath = base / "manifest.json"
    if mpath.is_file():
        try:
            m = json.load(open(mpath))
            before = len(m if isinstance(m, list) else m.get("documents") or m.get("articles") or [])
        except Exception:
            pass

    if dry:
        print(f"    upstream {upstream}, mirrored {before}, delta {upstream - before}", flush=True)
        return {"key": key, "upstream": upstream, "before": before, "written": 0, "dry": True}

    written, manifest = 0, []
    for a in articles:
        sec = sections.get(a.get("section_id"), "uncategorised")
        rel = f"articles/{slug(sec)}/{a['id']}-{slug(a.get('title',''))}.md"
        p = base / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        body = (
            "---\n"
            f'title: "{(a.get("title") or "").replace(chr(34), chr(39))}"\n'
            f"id: {a['id']}\n"
            f'section: "{sec.replace(chr(34), chr(39))}"\n'
            f'product: "{product}"\n'
            f"url: {a.get('html_url','')}\n"
            f"updated_at: {a.get('updated_at','')}\n"
            "---\n\n"
            f"# {a.get('title','')}\n\n"
            f"{html_to_text(a.get('body') or '')}\n"
        )
        # Rewrite only when the article is new or upstream says it changed.
        # Comparing rendered text instead would rewrite the whole corpus every
        # time this converter differs by a space from whatever wrote it first,
        # which buries the twelve real changes in 1,388 lines of churn and
        # risks replacing a better conversion with a worse one.
        old = p.read_text(encoding="utf-8") if p.is_file() else None
        upstream_stamp = a.get("updated_at", "")
        mirrored_stamp = ""
        if old:
            m_stamp = re.search(r"^updated_at:\s*(.+)$", old, re.M)
            mirrored_stamp = m_stamp.group(1).strip() if m_stamp else ""
        if old is None or (upstream_stamp and upstream_stamp != mirrored_stamp):
            p.write_text(body, encoding="utf-8")
            written += 1
        manifest.append({"id": a["id"], "title": a.get("title", ""), "section": sec,
                         "url": a.get("html_url", ""), "path": rel,
                         "updated_at": a.get("updated_at", "")})

    mpath.write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    (base / "llms.txt").write_text(
        "\n".join(f"{r['id']}\t{r['section']}\t{r['title']}\t{r['url']}" for r in manifest),
        encoding="utf-8")
    print(f"    upstream {upstream}, was {before}, files written {written}", flush=True)
    return {"key": key, "upstream": upstream, "before": before, "written": written, "dry": False}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="report the upstream/mirrored delta and write nothing")
    ap.add_argument("--only", help="refresh one source key only")
    args = ap.parse_args()

    results, failures = [], []
    for src in SOURCES:
        if args.only and args.only != src["key"]:
            continue
        try:
            results.append(pull_source(src, args.dry_run))
        except Exception as e:
            print(f"    FAILED: {e}", file=sys.stderr, flush=True)
            failures.append((src["key"], str(e)))

    print()
    for r in results:
        print(f"  {r['key']}: upstream {r['upstream']}, mirrored {r['before']}, "
              f"{'would write' if r['dry'] else 'wrote'} {r['written']}")
    if failures:
        print(f"\nREFRESH FAILED: {len(failures)} source(s) unreachable", file=sys.stderr)
        for k, e in failures:
            print(f"  {k}: {e}", file=sys.stderr)
        return 1
    print("\nREFRESH OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
