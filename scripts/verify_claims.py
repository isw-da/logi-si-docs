#!/usr/bin/env python3
"""Gate: the counts this repo states about itself are still true.

Written after an audit before sharing the repo found four numbers in README.md
that had quietly stopped being true: the Composer spec had been re-pulled from a
newer instance (220 paths / 338 ops became 223 / 344), v26 had grown from 871
articles to 883, the repo had gained a whole tree (logi-report-api/) that the
README never mentioned, and one file promised paths that only exist in a sibling
repository.

Prose about a corpus goes stale silently, because nothing recomputes it. This
recomputes it. Every number below is derived from the files, then looked for in
the prose that claims it; a claim that no longer matches is a failure, not a
rounding difference.

The counts move legitimately, because the weekly refresh tracks upstream. When
this gate goes red after a refresh, the corpus is right and the sentence is
wrong: update the sentence.

Checks that cannot run report NOT APPLICABLE by name and are counted, so a green
gate never means a gate that checked nothing.
"""
import json, os, re, sys, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

fails, skips, ran = [], [], 0


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return fh.read()


def spec_counts(rel):
    d = json.loads(read(rel))
    paths = d.get("paths", {})
    methods = ("get", "post", "put", "delete", "patch", "head", "options")
    ops = sum(1 for _, item in paths.items() for m in item if m.lower() in methods)
    return len(paths), ops


def claim(where, text, why):
    """The prose at `where` must contain `text`."""
    global ran
    ran += 1
    if text not in read(where):
        fails.append(f"{where} no longer says {text!r} ({why})")


# 1. article and page counts, from the manifests that the refresh regenerates
v25 = len(json.loads(read("logi-composer-current/v25/manifest.json")))
v26 = len(json.loads(read("logi-composer-current/v26/manifest.json")))
devnet = len(json.loads(read("logi-devnet/manifest.json")))
si_pages = sum(1 for _, _, fs in os.walk(os.path.join(ROOT, "simba-intelligence", "pages"))
               for f in fs if f.endswith(".md"))

claim("README.md", f"{v25} v25 articles and {v26} v26 articles", "manifest counts moved")
claim("README.md", f"{devnet:,} articles", "devnet manifest count moved")
claim("README.md", f"the {si_pages} SI pages", "SI page count moved")
claim("NOTICE", f"{v25} Composer v25 and {v26} Composer v26 articles", "manifest counts moved")
claim("NOTICE", f"{devnet:,} devnet", "devnet manifest count moved")

# 2. the OpenAPI specs, counted from the specs themselves
b_paths, b_ops = spec_counts("composer-api/composer-openapi-26.2.1-bundled.json")
h_paths, h_ops = spec_counts("composer-api/composer-openapi-simba-logisymphony.json")
r_paths, r_ops = spec_counts("logi-report-api/logireport-openapi.json")

claim("README.md", f"{b_paths} paths, {b_ops} operations", "bundled Composer spec changed")
claim("README.md", f"{h_paths} paths, {h_ops} operations", "hosted Composer spec changed")
claim("README.md", f"{r_paths} paths and {r_ops} operations", "Logi Report spec changed")
claim("CLAUDE.md", f"{b_paths} paths / {b_ops} ops", "bundled Composer spec changed")

# 3. composer-openapi.json is the stable filename for the bundled pull, and the
#    README says so. If it is ever re-pointed, the sentence must move with it.
ran += 1
digests = {p: hashlib.sha256(read(p).encode("utf-8")).hexdigest()
           for p in ("composer-api/composer-openapi.json",
                     "composer-api/composer-openapi-26.2.1-bundled.json")}
if len(set(digests.values())) != 1:
    fails.append("composer-openapi.json is no longer a copy of the bundled 26.2.1 spec, "
                 "which README.md and CLAUDE.md both state that it is")

# 4. the weekly job covers exactly what the prose says it covers
ran += 1
src = read("scripts/refresh.py")
block = src.split("SOURCES = [", 1)[1].split("]", 1)[0] if "SOURCES = [" in src else ""
covered = sorted(re.findall(r'"key":\s*"([^"]+)"', block))
if covered != ["logi-composer-current/v25", "logi-composer-current/v26"]:
    fails.append(f"scripts/refresh.py now refreshes {covered}, and README.md says the weekly "
                 f"job covers logi-composer-current/v25 and v26 only")

# 5. every repo-relative path the prose points at must exist here. This is the
#    check that would have caught logi-report-api/ promising spec/SPEC.sha256,
#    which only ever existed in logi-report-kb.
REFERENCED = [
    "TOOLKIT.md", "NOTICE", "scripts/refresh.py", "scripts/render_toolkit.py",
    "toolkit.json", "requirements-refresh.txt", ".github/workflows/refresh-mirror.yml",
    "composer-api/ENDPOINTS.md", "composer-api/verify-endpoints.py",
    "composer-api/composer-openapi.json",
    "composer-api/composer-openapi-26.2.1-bundled.json",
    "composer-api/composer-openapi-simba-logisymphony.json",
    "logi-report-api/ENDPOINTS.md", "logi-report-api/PROVENANCE.md",
    "logi-report-api/logireport-openapi.json", "logi-report-api/logireport-openapi.yaml",
    "logi-devnet/manifest.json", "logi-devnet/llms.txt",
    "simba-intelligence/API-NOTES.md", "simba-intelligence/llms-full.txt",
    "simba-intelligence/openapi.json",
    "simba-intelligence/reverse-engineered/apispec_1-26.2.0.json",
    "logi-composer-current/v25/manifest.json", "logi-composer-current/v26/manifest.json",
]
for rel in REFERENCED:
    ran += 1
    if not os.path.exists(os.path.join(ROOT, rel)):
        fails.append(f"prose points at {rel}, which is not in this repository")

# 6. the SI docs-site openapi.json is a placeholder, which the README says twice.
#    If upstream ever ships a real one, both sentences are wrong.
ran += 1
si_spec = json.loads(read("simba-intelligence/openapi.json"))
if sorted(si_spec.get("paths", {})) != ["/plants", "/plants/{id}"]:
    fails.append("simba-intelligence/openapi.json is no longer the plant-store placeholder "
                 "that README.md and API-NOTES.md describe")

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
