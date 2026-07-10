# Simba Intelligence — reverse-engineered notes (not from official docs)

Field-verified findings captured against live SI instances where the official
Mintlify docs are silent, wrong, or lag the release. Each page states how it was
verified and when. Treat as KB source-of-truth for "what does 26.2 actually do"
until the official docs catch up.

- `26.2-undocumented-features.md` — full undocumented API surface, env vars,
  feature flags, chart deltas (26.2.0, verified 2026-07-11).
- `apispec_1-26.2.0.json` — the product's OWN generated OpenAPI spec, pulled live
  from `/apispec_1.json` (the public docs ship a placeholder instead).
- `mcp-claude-integration.md` — native MCP server + Claude integration assessment
  (live-proven OAuth PKCE flow, tool surface, two-identity governance).
- `llm-provider-compatibility.md` — Grok/OpenAI-direct via LiteLLM bridge; the
  GPT-5.6 chat-completions incompatibility; prospect-parity model choice (5.4).
