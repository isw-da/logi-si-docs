# The insightsoftware product knowledge toolkit

One place to find out what exists, what it covers, and how current it is. Maintained by
Amin Hasan. Anyone on the team is welcome to clone, pin, fork or raise an issue.

## What exists

<!-- toolkit-table: generated from toolkit.json, do not edit by hand -->

| Repo | Covers | Visibility | Refresh |
|---|---|---|---|
| [`logi-si-docs`](https://github.com/isw-da/logi-si-docs) | Documentation mirror: SI, Composer v25 and v26, the legacy devnet archive, the Composer OpenAPI specs | Public | **Weekly, automatic** |
| [`composer-mcp`](https://github.com/isw-da/composer-mcp) | Composer REST API as MCP tools, with guards. Reference docs for embedding, theming, chatbot, calculations, limitations, safety | Public | Manual |
| [`simba-intelligence-skill`](https://github.com/isw-da/simba-intelligence-skill) | SI install, configuration, troubleshooting, NLQ testing, EDC connector testing, demo environments | Public | Manual |
| [`symphony-dashboard-builder-skill`](https://github.com/isw-da/symphony-dashboard-builder-skill) | Composer dashboards: server-side creation and the client-side application around them | Public | Manual |
| [`simba-intelligence-mcp`](https://github.com/isw-da/simba-intelligence-mcp) | SI API as MCP tools | Private | Manual |
| [`logi-report-kb`](https://github.com/isw-da/logi-report-kb) | Logi Report and JReport: 13,235 documents plus the Server Web API surface | Public | **Weekly**, current docs only |

<!-- /toolkit-table -->

That table is generated from `toolkit.json` by `scripts/render_toolkit.py`, and it is the
only place the repository set is written down. It used to be hand-maintained in six files,
which meant it went stale in all six at once: `logi-report-kb` was described as private and
manually refreshed for some time after it had become public and gained a weekly job.

`scripts/verify_toolkit.py` runs as part of the release gate and fails on three things: a
rendered copy that has drifted from the source, a visibility this file claims that GitHub
disagrees with, and a repository described as refreshing weekly that has no scheduled
workflow. Checks it cannot run, usually because a sibling repository is not checked out on
this machine, are named and counted rather than passed over.

To change the set, edit `toolkit.json`, run `python3 scripts/render_toolkit.py`, and commit
the repositories it touches.

## Which one answers your question

- **"What does this Composer endpoint do?"** → `logi-si-docs/composer-api/ENDPOINTS.md`. Two
  specs from two instances, because they disagree by ten operations, and each endpoint is
  marked with where it was actually seen.
- **"How do I drive Composer from code?"** → `composer-mcp`. Read `SAFETY.md` and
  `LIMITATIONS.md` before anything else; they are the ones written after something went wrong.
- **"How do I embed a dashboard in an application?"** → `symphony-dashboard-builder-skill`,
  Client-Side Assembly.
- **"How do I stand SI up?"** → `simba-intelligence-skill/simba-intelligence-setup`.
- **"What changed between Composer versions?"** → `logi-si-docs/logi-composer-current/`, which
  holds v25 and v26 side by side.
- **"Anything about Logi Report or JReport"** → `logi-report-kb`. Note the product has three
  naming eras and the answer usually depends which one the customer is on.

## Two things to know before you rely on any of it

**Pin a tag.** Every repo cuts releases. `main` moves, often because something turned out to
be wrong, and the release notes say what. Tracking a branch means inheriting corrections you
did not ask for at a time you did not choose.

**Run the gate.** Most repos carry a `verify-*` script that is proven to fail before it is
trusted. If it is red, the documentation is wrong, not the gate.

```bash
python3 verify-*.py     # or bash verify-*.sh
echo $?                 # on its own line; a pipe reports the pipe's status
```

Some checks report NOT APPLICABLE. That means the thing is real but not visible from your
checkout, usually internal material that is never published, or a provenance path that only
resolves on the machine that wrote it. Skips are always named and counted.

## What is deliberately not published

Customer names, deployed customer artefacts, NDA-tagged source material, and anything derived
from unreleased internal roadmap. Where a real customer artefact is used as evidence it
appears as "deployed theme A" and the identifying copy stays in a private tree.

If you find something that should not be public, say so and it comes out the same day.

## Contributing

Issues and pull requests welcome on any of them. Two asks: run the gates first, and say how
you know. A file and line, a command and its output, a Confluence page id or a Jira key.
"I think" is fine as long as it says so. Several confident claims in this corpus turned out
to be wrong and each one cost somebody a day.
