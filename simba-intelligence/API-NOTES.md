# Simba Intelligence API, notes from a live instance

Checked against a running SI deployment on 2026-06-26.

SI's own application API lives under `/api/v1/*` (for example `/api/v1/chat/stream`, `/api/v1/config/llm`, `/api/v1/auth/login`, `/api/v1/apikeys`). These use session or SSO auth, not basic auth. The how-to for them is the prose `pages/.../guides/user-guides/API-Usage-Guide.md` in this folder.

The `openapi.json` mirrored from the SI docs site is a template placeholder (its only paths are `/plants` and `/plants/{id}`, under the title "OpenAPI Plant Store"), not the real SI API.

**Correction, 11 July 2026.** This note originally said SI publishes no OpenAPI or Swagger document for `/api/v1/*`. insightsoftware does not publish one, but the running product generates one: `/apispec_1.json` serves a Swagger 2.0 document titled "Simba Intelligence API", version 26.2.0, with 32 paths, all under `/api/v1/`. A live copy is at `reverse-engineered/apispec_1-26.2.0.json`. It is a capture from one version of one instance, so treat it as a description of what that build served rather than as a contract.

The discovery and Composer backend that SI queries also publishes a full OpenAPI 3.1 spec, captured in `../composer-api/`. On this instance in June 2026 it was served at both `/composer/api-docs` and `/discovery/api-docs` and reported 220 paths, 338 operations, 73 tags. The August 2026 pull from an SI-bundled 26.2.1 at `/discovery/api-docs` reported 223 paths and 344 operations, so the two do not agree and neither number should be quoted without its instance. `../composer-api/ENDPOINTS.md` holds the union and the per-instance marks.

So on a live deployment the genuine machine-readable API is the Composer and discovery one. SI's own endpoints are real but documented only in prose.
