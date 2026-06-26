# Simba Intelligence API, notes from a live instance

Checked against a running SI deployment on 2026-06-26.

SI's own application API lives under `/api/v1/*` (for example `/api/v1/chat/stream`, `/api/v1/config/llm`, `/api/v1/auth/login`, `/api/v1/apikeys`). These use session or SSO auth, not basic auth, and SI does not publish an OpenAPI or Swagger document for them. The how-to for these is the prose `pages/.../guides/user-guides/API-Usage-Guide.md` in this folder.

The `openapi.json` mirrored from the SI docs site is a template placeholder (its only paths are `/plants`), not the real SI API.

The discovery and Composer backend that SI queries does publish a full OpenAPI 3.1 spec. It is served identically at `/composer/api-docs` and `/discovery/api-docs` (220 paths, 338 operations, 73 tags) and is captured in `../composer-api/`.

So on a live deployment the genuine machine-readable API is the Composer and discovery one. SI's own endpoints are real but documented only in prose.
