#!/usr/bin/env python3
"""Gate: the rendered repository tables match toolkit.json, and toolkit.json is true.

Three checks, one per failure that has actually happened here.

1. DRIFT. The table was hand-maintained in six files and went stale in all six.
   Every rendered copy must match what toolkit.json renders.

2. VISIBILITY. logi-report-kb was described as private for some time after it
   was made public. Checked against GitHub, because the repository is the
   authority on its own visibility and this file is not.

3. REFRESH. A repo claiming a weekly refresh must actually have a scheduled
   workflow. A claim in a table is not a running job, and the table said
   "Manual" for a repo that had one and "Automatic" for one that did not.

Checks that cannot run here (no checkout, no gh, no network) report
NOT APPLICABLE by name and are counted. A skip is never silent, because a gate
that quietly checks nothing reports the same green as one that checked
everything.
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SIBLINGS = os.path.dirname(ROOT)
DATA = json.load(open(os.path.join(ROOT, "toolkit.json"), encoding="utf-8"))

fails, skips, ran = [], [], 0


def sh(cmd):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        return p.returncode, p.stdout.strip()
    except (OSError, subprocess.TimeoutExpired):
        return 1, ""


# 1. drift
rc, out = sh([sys.executable, os.path.join(HERE, "render_toolkit.py"), "--check"])
ran += 1
if rc != 0:
    fails.append("rendered tables differ from toolkit.json; run scripts/render_toolkit.py")
for line in out.splitlines():
    if "SKIP" in line:
        skips.append(line.strip().replace("SKIP (not applicable here): ", "drift, "))

# 2. visibility, against GitHub
rc, _ = sh(["gh", "auth", "status"])
if rc != 0:
    skips.append("visibility, gh is unavailable or not authenticated, so GitHub was not asked")
else:
    for r in DATA["repos"]:
        slug = f"{DATA['org']}/{r['name']}"
        rc, out = sh(["gh", "repo", "view", slug, "--json", "visibility", "-q", ".visibility"])
        if rc != 0:
            skips.append(f"visibility, {slug} could not be read from GitHub")
            continue
        ran += 1
        if out.title() != r["visibility"]:
            fails.append(f"{slug} is {out.title()} on GitHub, toolkit.json says {r['visibility']}")

# 3. a weekly claim needs a scheduled workflow in that repo's checkout
for r in DATA["repos"]:
    if r["refresh"] != "weekly":
        continue
    repo_dir = ROOT if r["name"] == "logi-si-docs" else os.path.join(SIBLINGS, r["name"])
    wf_dir = os.path.join(repo_dir, ".github", "workflows")
    if not os.path.isdir(wf_dir):
        skips.append(f"refresh, {r['name']} is not checked out, so its schedule was not verified")
        continue
    ran += 1
    text = ""
    for fn in os.listdir(wf_dir):
        if fn.endswith((".yml", ".yaml")):
            text += open(os.path.join(wf_dir, fn), encoding="utf-8").read()
    if not re.search(r"^\s*schedule:", text, re.M) or "cron:" not in text:
        fails.append(f"{r['name']} is described as refreshing weekly but has no scheduled "
                     f"workflow in .github/workflows/")

print(f"ran {ran} check(s), {len(skips)} not applicable, {len(fails)} failed")
print()
for s in skips:
    print(f"  NOT APPLICABLE: {s}")
if fails:
    print()
    for f in fails:
        print(f"  FAIL: {f}")
    print("\nGATE: RED")
    sys.exit(1)
print("\nGATE: GREEN")
sys.exit(0)
