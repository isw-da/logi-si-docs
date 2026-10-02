#!/usr/bin/env python3
"""Mirror versioned trees of the public Mintlify docs site.

The Mintlify site publishes an index at https://insightsoftware.mintlify.app/llms.txt
and every page as plain markdown at its own URL plus `.md`, so mirroring a tree
is: read the index, keep the URLs under one prefix, fetch each page as is.

Run by hand, not by the weekly job. `scripts/refresh.py` covers the two Zendesk
help centres only, and README.md says so; these trees are dated snapshots.

Layout follows `simba-intelligence/pages/`: each page is written byte for byte
at `<dest>/pages/<URL path>`. Provenance goes in `<dest>/manifest.json` (title,
section, url, path, fetched_at, sha256) and `<dest>/llms.txt`, as the Zendesk
trees do. Each run replaces the whole `<dest>/pages/` tree, so a page upstream
drops does not linger.

Exit codes: 0 written (or dry run), 1 the index or a page failed to fetch.
"""
from __future__ import annotations
import argparse, datetime, hashlib, json, pathlib, re, shutil, sys, time, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = "https://insightsoftware.mintlify.app/llms.txt"
UA = "logi-si-docs-mirror/1.0 (+https://github.com/isw-da/logi-si-docs)"

TREES = [
    {"dest": "simba-intelligence/v26.3",
     "prefix": "https://insightsoftware.mintlify.app/simba-agentic-intelligence/docs/26.3/",
     "product": "Simba Agentic Intelligence 26.3"},
    {"dest": "logi-composer-current/ssa-26.3",
     "prefix": "https://insightsoftware.mintlify.app/simba-embedded-analytics/docs/self-service-analytics/26.3/",
     "product": "Self-Service Analytics 26.3"},
]


def get(url: str, tries: int = 4) -> bytes:
    last = None
    for attempt in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:
            last = e
            time.sleep(2 ** attempt)
    raise RuntimeError(f"giving up on {url}: {last}")


def index_entries(text: str, prefix: str) -> list[tuple[str, str]]:
    """(title, url) under `prefix`, first occurrence wins. The upstream index
    lists some pages twice, and a duplicate must not inflate the count."""
    seen, out = set(), []
    for title, url in re.findall(r"\[([^\]]*)\]\((https://[^)\s]+)\)", text):
        if url.startswith(prefix) and url not in seen:
            seen.add(url)
            out.append((title, url))
    return out


def mirror(tree: dict, index: str, dry: bool, stamp: str) -> int:
    dest = ROOT / tree["dest"]
    entries = index_entries(index, tree["prefix"])
    if not entries:
        raise RuntimeError(f"no pages under {tree['prefix']} in {INDEX}")
    before = 0
    if (dest / "manifest.json").is_file():
        before = len(json.loads((dest / "manifest.json").read_text(encoding="utf-8")))
    print(f"  {tree['dest']}: upstream {len(entries)}, mirrored {before}", flush=True)
    if dry:
        return len(entries)

    pages = dest / "pages"
    if pages.exists():
        shutil.rmtree(pages)
    manifest = []
    for title, url in entries:
        rel = "pages/" + url.split("://", 1)[1].split("/", 1)[1]
        body = get(url)
        p = dest / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(body)
        section = url[len(tree["prefix"]):].rsplit("/", 1)[0] if "/" in url[len(tree["prefix"]):] else ""
        manifest.append({"title": title, "section": section, "product": tree["product"],
                         "url": url, "path": rel, "fetched_at": stamp,
                         "sha256": hashlib.sha256(body).hexdigest()})
    (dest / "manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    (dest / "llms.txt").write_text(
        "\n".join(f"{r['section']}\t{r['title']}\t{r['url']}" for r in manifest) + "\n",
        encoding="utf-8")
    print(f"    wrote {len(manifest)} page(s)", flush=True)
    return len(manifest)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="report counts, write nothing")
    args = ap.parse_args()
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        index = get(INDEX).decode("utf-8")
        for tree in TREES:
            mirror(tree, index, args.dry_run, stamp)
    except Exception as e:
        print(f"MINTLIFY REFRESH FAILED: {e}", file=sys.stderr)
        return 1
    print("\nMINTLIFY REFRESH OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
