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
- `26.2-authoritative.md` — official release notes + Jira traceability + live findings, reconciled (2026-07-11).
- `26.2-release-notes-official.md` — the official v26.2.0 notes mirrored from Confluence PJX (never published to Mintlify).
- `composer-ai-assistant-26.2.md`: the SI assistant inside the Composer dashboard UI, verified behaviour (2026-07-21).
- `composer-theming-branding-26.2.md`: reskinning a live 26.2 Composer to a purple SI theme with the SI logo (2026-07-21).
- `composer-visual-api-26.2.md`: building a four-widget dashboard programmatically, end to end (2026-07-20).
