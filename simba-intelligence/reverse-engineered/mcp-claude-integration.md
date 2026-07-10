# SI 26.2 — native MCP server and Claude integration assessment

Empirical assessment on a live 26.2.0 instance (azuretest, 2026-07-10). The full
OAuth2 PKCE flow and all tool calls below were executed headlessly and verified.

## Verdict

SI 26.2's MCP server is a **genuinely native, standards-correct remote MCP
implementation** — the best AI-integration surface the product has. Claude
Desktop, claude.ai custom connectors and Claude Code can connect with zero
custom code: discovery, dynamic client registration, PKCE, token rotation and
consent all behave per spec.

## What was proven (all live)

1. `/.well-known/oauth-authorization-server` → full metadata (S256 PKCE,
   authorization_code + refresh_token, client_secret_post/basic, revocation).
2. `POST /mcp/register` → dynamic client registration (201). Strict: it
   *requires* `grant_types` to be exactly authorization_code + refresh_token.
3. `GET /mcp/authorize` with an SI session → 302 to the consent screen;
   `POST /mcp/consent` (form params + session cookie) → auth code. The consent
   screen is served by the main app SPA; **the user must already have an SI web
   session in the same browser**.
4. `POST /mcp/token` with PKCE verifier → access token (1 day) + rotating
   refresh token (30 days).
5. MCP protocol 2025-03-26 over streamable HTTP (FastMCP): initialize,
   tools/list, tools/call all worked.
6. `get_data("How many alerts are there in total?")` → structured result
   (`count: 1719`), correct vs SQL ground truth. Note: get_data returns the
   **raw query result JSON** (groups/metrics), not prose — ideal for agents.

## Live tool surface (26.2.0)

| Tool | Purpose |
|---|---|
| `get_data` | NLQ against sources (optional source_id) |
| `search_data_sources` | find sources (docs call it `get_data_sources` — **docs drift**) |
| `get_suggested_questions` | AI follow-up suggestions |
| `get_field_statistics` | per-field stats for exploration |

`prompts/list` and `resources/list` are advertised but empty — tools-only today.

## Architecture change 26.1.1 → 26.2.0

The nginx sidecar is gone; FastMCP itself now serves the well-known endpoints
and the MCP service exposes port **8001** directly (was 8000 via nginx). Helm:
`simba.intelligence.mcp.baseUrl` default moved to `http://localhost:8001` and
MUST be set to the externally reachable URL in any real deployment — every URL
in the OAuth discovery metadata is derived from it.

## Connecting Claude (recipes)

Local/tunnelled (works today, used on the sandbox):
```bash
# metadata self-references localhost:8001, so map that exact port
ssh -f -N -L 8001:localhost:<box-mcp-port> user@box
# log into the SI web UI first (same browser), then:
claude mcp add --transport http si-sandbox http://localhost:8001/mcp
```
Claude Desktop / claude.ai: add a custom connector with the same URL
(claude.ai requires public HTTPS + mcp.baseUrl set to that URL).

## Observations for product

1. **Docs drift**: MCP guide documents `get_data_sources`; server ships
   `search_data_sources`. Release notes (public) still stop at 25.4.
2. **Scope inflation**: requesting `scope=read:data` returned a token granted
   `read:data write:data admin:users` (for a supervisor user). Granted scope
   should not exceed the request.
3. **No write tools**: `write:data`/`admin:users` scopes exist but no tools use
   them — presumably roadmap.
4. **No published OpenAPI**: the docs' `openapi.json` is the Mintlify Plant
   Store placeholder. The REST surface (session auth `/api/v1/*`, API-key
   bearer on `/api/v1/chat/stream`, SSE task streams, Composer `/discovery/api`
   v3) is real and workable but reverse-engineered, not contracted.
5. The main-app REST API accepts API-key bearers for chat, while MCP insists on
   OAuth per user — two parallel auth models for the same capability.
