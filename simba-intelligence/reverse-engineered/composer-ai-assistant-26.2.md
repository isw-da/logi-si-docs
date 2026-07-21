# Simba Intelligence assistant inside Composer (26.2) — verified behaviour

Field-verified 2026-07-21 on a live SI 26.2.0 rig (kind, chart install), driving the
Composer dashboard UI. Grounds the 22 Jul webinar use case 2. Companion:
`composer-visual-api-26.2.md` (programmatic dashboard build).

## What exists in 26.2

Two distinct in-Composer AI capabilities, gated by Composer feature flags
(Confluence ZD/17328046108 "Composer Feature flags"):

| Capability | Flag | Default | State on our rig |
|---|---|---|---|
| SI chat assistant on dashboards ("Open Simba Intelligence Chat", sparkle icon) | `symphony-chat` | false | ENABLED (works) |
| Inline "Create visual with AI" (+ menu, BETA) generating a rendered governed visual | `symphony-ai-visuals-flow` | none | DISABLED (needs a visual-generation chatflow id) |
| AI SQL generation in source creation | `symphony-ai-sql-flow` | none | — |

## The SI chat assistant (verified working)

- Toolbar sparkle button. In headless DOM the button is
  `button[aria-label="Open Simba Intelligence Chat"]` (the `title` attr only attaches
  with a live pointer; the green `bp3-intent-success` class only appears when LLM-active).
- Answers governed NL questions against the same sources the dashboard uses — so the
  numbers match the dashboard tiles and any Claude/MCP answer on the same source
  (verified: identical golden numbers across all three surfaces).
- DESCRIBE: asked "total value of alerted transactions by alert typology…" it returns a
  clean per-group table with correct values AND a plain-English conclusion. NOTE: the
  LLM's prose VARIES run to run (sometimes states the overall total, sometimes only the
  comparison) — the deterministic guarantee is the numbers, not the wording. Read totals
  off the tiles, not the assistant's sentence.
- GENERATE: asked "create a bar chart of …" it returns a STRUCTURED TEXT bar-chart
  breakdown with correct values (ASCII bars + offer to format as table/CSV/JSON). It does
  NOT render a Composer visual inline here — inline visual rendering is the opt-in "Visual"
  capability (Confluence CB/17745838107) and is off in this embed.
- Backend: `/api/v1/chat*` (26.2 apispec, flagged EXPERIMENTAL); `/api/v1/config/llm/status`
  must return `{"is_configured":true}` (precondition).
- UX: paste then click the SEND arrow; Return alone does not submit in the panel.

## "Create visual with AI" (BETA, disabled here)

- Present in the dashboard "+ / Add" menu as "Create visual with AI [BETA]", but
  `bp3-disabled` on our instance because `symphony-ai-visuals-flow` = none. Enabling needs
  a valid visual-generation chatflow id set on that flag (feature-toggle/DB change). Treat
  as roadmap for a demo; do not enable on a live demo rig without testing.

## Capture harness note

Headless CDP screenshots of the assistant flow need: the aria-label selector above, a
WS-recv timeout (a dropped SSH tunnel otherwise hangs the capture), and the proven
"fully render the dashboard before touching the toolbar" wait. A plain HTTP auth proxy
must pass the WebSocket upgrade for dashboard data to load.
