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
- `26.3-authoritative.md`: what release 26.3 changes, written 2026-09-29 **before 26.3 is
  released** and sourced from Jira (PY, SCP, CMP), Confluence page ids and the public
  Composer documentation site. It also lists, by path, the fifteen mirrored
  `simba-intelligence/pages/` lines that 26.3 makes wrong.
- `26.3-public-availability.md`: what of 26.3 is publicly documented and what is not, checked
  2026-09-29. Read it before treating a missing 26.3 page as a capture failure: the Simba
  Agentic Intelligence 26.3 docs return HTTP 404 upstream, so there is nothing to mirror yet.

## Why corrections live here and not in the mirror

`simba-intelligence/pages/` is a faithful copy of upstream Mintlify. Editing a mirrored page
to correct it destroys the property that makes the mirror worth keeping, and the next refresh
overwrites the edit anyway. Every correction goes in this directory instead. The two 26.3
files above were written that way: **no mirrored page was edited.**

## On publishing Confluence-derived material in a public repository

`26.2-release-notes-official.md` mirrors an internal Confluence page into a public repository.
That is deliberate and it is this repository's precedent, but it is not a blanket permission,
and a sibling repository (`isw-da/composer-mcp`) declares the opposite rule in its
`.gitignore`. The two policies disagree, so this repository states which one it follows.

The line is **released versus unreleased**, not internal versus external. Confluence-derived
detail for a **released** version is published here, which is what
`26.2-release-notes-official.md` is. For an **unreleased** version, the 26.3 files carry only
what a reader needs in order not to run a command or write code that breaks, each statement
marked as pertaining to an unreleased version and cited to a ticket key or a public URL. No
verbatim internal prose, no roadmap, no commercial or entitlement detail, and no equivalent of
`26.2-release-notes-official.md` for 26.3 until 26.3 ships.
