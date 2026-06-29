# logi-si-docs — coding rules

This repo is the canonical documentation mirror for Simba Intelligence and
Logi Composer. It is the source of truth that other tooling reads from. Treat
the content as authoritative and keep it faithful to upstream.

## What lives here

- `simba-intelligence/` — SI Mintlify corpus: `llms-full.txt` (whole corpus),
  `llms.txt` (index), and per-page markdown under `pages/simba-intelligence/docs/`.
  This is the definitive reference for SI product behaviour (NLQ, LLM config,
  EDCs, RLS, deployment).
- `logi-composer-current/v25/` and `v26/` — current Composer product docs
  (articles, raw, meta). The live v25/v26 reference.
- `composer-api/` — the canonical Composer OpenAPI spec
  (`composer-openapi.json`, 220 paths / 338 ops) plus `ENDPOINTS.md`. This spec
  also covers the SI Discovery backend (`/discovery/api/*`), which is
  byte-identical to the Composer backend.
- `logi-devnet/` — full legacy devnet Zendesk archive (15,712 articles).
  Covers legacy Composer v5/v6 and the wider Logi product family. Use the
  `logi-composer-current/` docs, not devnet, for anything v25/v26.

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
- Composer APIs are available to SI callers at the `/discovery` context. There
  is one OpenAPI spec for both backends; it is the one in `composer-api/`.
- SI's own NLQ endpoints (`/api/v1/*`) use session/SSO auth and publish no
  OpenAPI, so the Composer/Discovery spec is the only machine-readable API
  reference.

## Editing rules

- British English in prose and commit messages.
- Keep the top-level directory names stable (see consumers above).
- When refreshing from upstream, replace whole directories rather than editing
  individual generated files, so the mirror stays faithful.
- Do not commit credentials. Probing creds used to capture the OpenAPI spec
  were never committed and must stay out.
