#!/usr/bin/env python3
"""Render the repository-set tables from toolkit.json into every place they appear.

The table used to be hand-written in six files. It went stale in all six at
once, describing logi-report-kb as private and manually refreshed after it had
become public and gained a weekly job. Nobody noticed, because six copies means
no copy is authoritative.

So the list lives in toolkit.json and is rendered here, between markers:

    <!-- toolkit-table: generated from toolkit.json, do not edit by hand -->
    ...
    <!-- /toolkit-table -->

Rendered output stays COMMITTED rather than built on demand, so a fresh clone
with no network and no Python still reads a correct table.

Run with --check to compare without writing; that is what verify_toolkit.py
uses. Sibling repos that are not checked out are reported by name and skipped,
never silently passed over.
"""
import argparse, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = os.path.join(ROOT, "toolkit.json")
SIBLINGS = os.path.dirname(ROOT)

OPEN = "<!-- toolkit-table: generated from toolkit.json, do not edit by hand -->"
CLOSE = "<!-- /toolkit-table -->"


def refresh_cell(r, style):
    if r["refresh"] == "manual":
        return "Manual"
    if style == "toolkit":
        base = "**Weekly, automatic**" if not r["refresh_note"] else "**Weekly**, current docs only"
        return base
    base = "**Automatic**, weekly"
    return f"{base}, {r['refresh_note']}" if r["refresh_note"] else base


def render(data, style):
    org = data["org"]
    if style == "toolkit":
        rows = ["| Repo | Covers | Visibility | Refresh |", "|---|---|---|---|"]
        for r in data["repos"]:
            rows.append(f"| [`{r['name']}`](https://github.com/{org}/{r['name']}) | "
                        f"{r['covers']} | {r['visibility']} | {refresh_cell(r,style)} |")
    else:
        rows = ["| Repo | What it holds | Refresh |", "|---|---|---|"]
        for r in data["repos"]:
            vis = "" if r["visibility"] == "Public" else " (private)"
            rows.append(f"| [`{org}/{r['name']}`](https://github.com/{org}/{r['name']}) | "
                        f"{r['holds']}{vis} | {refresh_cell(r,style)} |")
    return "\n".join(rows)


def splice(path, block):
    """Replace between markers. Insert markers around the existing table on first run."""
    with open(path, encoding="utf-8") as fh:
        s = fh.read()
    new_block = f"{OPEN}\n\n{block}\n\n{CLOSE}"
    if OPEN in s and CLOSE in s:
        out = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), lambda _: new_block, s, flags=re.S)
    else:
        # first run: find the existing hand-written table and wrap it
        m = re.search(r"^\| Repo \|.*?(?=\n\n)", s, flags=re.S | re.M)
        if not m:
            return None, "no table found and no markers present"
        out = s[:m.start()] + new_block + s[m.end():]
    return out, None


def targets():
    """(path, style) for every file that carries the table, that exists on disk."""
    yield os.path.join(ROOT, "TOOLKIT.md"), "toolkit", "si-docs-mirror"
    for r in json.load(open(SRC, encoding="utf-8"))["repos"]:
        if r["name"] == "logi-si-docs":
            continue
        p = os.path.join(SIBLINGS, r["name"], "CONSUMING.md")
        yield p, "consuming", r["name"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="compare only, write nothing")
    a = ap.parse_args()

    data = json.load(open(SRC, encoding="utf-8"))
    stale, wrote, skipped, errors = [], [], [], []

    for path, style, label in targets():
        if not os.path.exists(path):
            skipped.append(f"{label}: not checked out at {path}")
            continue
        out, err = splice(path, render(data, style))
        if err:
            errors.append(f"{label}: {err}")
            continue
        current = open(path, encoding="utf-8").read()
        if out == current:
            continue
        if a.check:
            stale.append(label)
        else:
            open(path, "w", encoding="utf-8").write(out)
            wrote.append(label)

    for s in skipped:
        print(f"  SKIP (not applicable here): {s}")
    for e in errors:
        print(f"  ERROR: {e}")

    if a.check:
        if stale:
            for s in stale:
                print(f"  STALE: {s} does not match toolkit.json")
        print(f"\nchecked {len(list(targets())) - len(skipped)} file(s), "
              f"{len(stale)} stale, {len(skipped)} not checked out")
        sys.exit(1 if (stale or errors) else 0)

    for w in wrote:
        print(f"  wrote {w}")
    print(f"\nrendered into {len(wrote)} file(s), {len(skipped)} not checked out")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
