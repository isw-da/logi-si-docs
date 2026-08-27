#!/usr/bin/env python3
"""Gate: ENDPOINTS.md must match the specs it claims to index.

An index generated once and then hand-edited drifts silently, and a drifted
index is worse than none: it reads as authoritative. This regenerates the
expected operation set from the specs and diffs it against what the file says,
including the per-instance provenance marks.
"""
import json, re, sys, pathlib

D = pathlib.Path(__file__).parent
SRC = [("composer-openapi-26.2.1-bundled.json", "B"),
       ("composer-openapi-simba-logisymphony.json", "H")]

fails = []
specs = {}
for f, key in SRC:
    p = D / f
    if not p.is_file():
        fails.append(f"spec missing: {f}")
        continue
    try:
        d = json.load(open(p))
    except Exception as e:
        fails.append(f"spec unparseable: {f} ({e})")
        continue
    specs[key] = {(m.upper(), path)
                  for path, item in d.get("paths", {}).items()
                  for m in item if m.lower() in ("get","post","put","delete","patch")}

if len(specs) != 2:
    print("\n".join("  FAIL: " + x for x in fails))
    print("ENDPOINTS VERIFY FAILED: cannot load both specs")
    sys.exit(1)

expected = {}
for key, ops in specs.items():
    for op in ops:
        expected.setdefault(op, set()).add(key)

idx = (D / "ENDPOINTS.md").read_text()
listed = {}
for m in re.finditer(r'^- `(GET|POST|PUT|DELETE|PATCH) (\S+)`(.*)$', idx, re.M):
    verb, path, rest = m.group(1), m.group(2), m.group(3)
    if "[B only]" in rest:   srcs = {"B"}
    elif "[H only]" in rest: srcs = {"H"}
    else:                    srcs = {"B","H"}
    listed[(verb, path)] = srcs

missing = set(expected) - set(listed)
extra   = set(listed) - set(expected)
wrong   = {k for k in set(expected) & set(listed) if expected[k] != listed[k]}

for k in sorted(missing)[:10]: fails.append(f"in a spec but not indexed: {k[0]} {k[1]}")
for k in sorted(extra)[:10]:   fails.append(f"indexed but in no spec: {k[0]} {k[1]}")
for k in sorted(wrong)[:10]:
    fails.append(f"wrong provenance for {k[0]} {k[1]}: index says {sorted(listed[k])}, specs say {sorted(expected[k])}")

print(f"specs: bundled {len(specs['B'])} ops, hosted {len(specs['H'])} ops")
print(f"union expected: {len(expected)}   indexed: {len(listed)}")
print(f"both={sum(1 for v in expected.values() if len(v)==2)} "
      f"bundled-only={sum(1 for v in expected.values() if v=={'B'})} "
      f"hosted-only={sum(1 for v in expected.values() if v=={'H'})}")
print()
if fails:
    for f in fails[:20]: print("  FAIL:", f)
    print(f"\nENDPOINTS VERIFY FAILED: {len(missing)} missing, {len(extra)} extra, {len(wrong)} mis-marked")
    sys.exit(1)
print("ENDPOINTS VERIFY OK: index matches both specs, provenance marks correct")
sys.exit(0)
