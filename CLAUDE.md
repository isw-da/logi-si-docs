# logi-si-docs — coding rules

This repo is the canonical documentation mirror for Simba Intelligence and
Logi Composer. It is the source of truth that other tooling reads from. Keep it
faithful to upstream, and read it as authoritative for what upstream said on the
date each tree was pulled; only the two Composer help-centre trees track
upstream week by week. Dates are in `README.md`.

## What lives here

- `simba-intelligence/` — SI Mintlify corpus: `llms-full.txt` (whole corpus),
  `llms.txt` (index), and per-page markdown under `pages/simba-intelligence/docs/`.
  This is the definitive reference for SI product behaviour (NLQ, LLM config,
  EDCs, RLS, deployment).
- `logi-composer-current/v25/` and `v26/` — current Composer product docs
  (`articles/`, `raw/`, `meta/`, plus `manifest.json` and `llms.txt`). The live
  v25/v26 reference, and the only trees the weekly refresh updates. Count the
  manifest rather than the files: the refresh never deletes, so an article that
  upstream retitles leaves its old slug behind.
- `composer-api/`: three Composer OpenAPI specs plus `ENDPOINTS.md`.
  `composer-openapi.json` is a stable filename for existing tooling and is
  byte-identical to `composer-openapi-26.2.1-bundled.json` (same SHA-256),
  which is 223 paths / 344 ops, pulled from an SI-bundled 26.2.1 at the
  `/discovery` context. `composer-openapi-simba-logisymphony.json` is 220 / 338
  from the hosted instance at the `/composer` context. The two disagree by ten
  operations, so do not assume the two contexts serve the same document; check
  `ENDPOINTS.md`, which indexes the union of 346 and marks every row with the
  instance it was seen on.
- `logi-devnet/`: legacy devnet Zendesk archive as at 26 June 2026 (15,712
  articles), covering legacy Composer v5/v6 and the wider Logi product family.
  Use the `logi-composer-current/` docs, not devnet, for anything v25/v26.
  Frozen: it is not in `SOURCES` in `scripts/refresh.py`, so the weekly job
  never touches it, even though the upstream host still answers.
- `logi-report-api/`: the Logi Report Server Web API definition (Swagger 2.0,
  124 paths / 225 ops), copied here from `logi-report-kb/api/`. That repo is
  the canonical home and holds the checksum and the gate for it; this copy is
  for tooling that only clones this repo.

## Who consumes this repo

Two repos pull from here and expect the layout above to stay stable. Renaming
or moving these directories breaks both consumers, so coordinate any structural
change with them:

- [`isw-da/simba-intelligence-mcp`](https://github.com/isw-da/simba-intelligence-mcp)
  — its `scripts/refresh-docs.sh` copies `simba-intelligence/`,
  `logi-composer-current/`, and `composer-api/` into `docs/logi-si-docs/`, then
  serves them through the `search_si_mintlify`, `search_composer_current_docs`,
  and `get_composer_openapi_spec` tools. Its doc-search tools recurse with
  `rglob('*.md')`, so nested article paths are fine; renamed top-level dirs are
  not.
- [`isw-da/simba-intelligence-skill`](https://github.com/isw-da/simba-intelligence-skill)
  — points operators and agents at this repo as the doc-first source before
  answering any SI or Composer question.

## Architecture facts

- SI is built on Logi Composer. The SI Helm chart aliases the Composer subchart
  as `discovery`. EDC connectors live in Composer.
- Composer APIs are available to SI callers at the `/discovery` context. The
  specs in `composer-api/` cover both backends, and the bundled one was pulled
  from the `/discovery` context itself.
- SI's own NLQ endpoints (`/api/v1/*`) use session/SSO auth. insightsoftware
  publishes no OpenAPI document for them and the docs site ships a placeholder,
  but the running product generates one at `/apispec_1.json`; a live capture is
  at `simba-intelligence/reverse-engineered/apispec_1-26.2.0.json` (Swagger 2.0,
  32 paths). Use it as a version-specific capture, not a published contract.

## Editing rules

- British English in prose and commit messages.
- Keep the top-level directory names stable (see consumers above).
- When refreshing from upstream, replace whole directories rather than editing
  individual generated files, so the mirror stays faithful.
- Do not commit credentials. Probing creds used to capture the OpenAPI spec
  were never committed and must stay out.
