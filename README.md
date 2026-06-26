# insightsoftware product docs, made machine-readable for AI assistants

A clean, searchable mirror of insightsoftware's product documentation, organised so an AI assistant can look up the right page and answer from it.

## The problem this solves

End users want to ask an AI assistant how to do something in the product rather than raise a ticket or wait on support. For that to work the assistant needs the product documentation in a form it can read and search. The docs live on help-centre and documentation sites built for people reading them in a browser. A model needs them in a different shape.

Worth being clear on one thing up front: an AI assistant does not memorise documentation. It looks it up each time. So the job is to give it a complete, clean, searchable copy of the docs plus a way to fetch the relevant page for each question. That is what this repo is.

## What's in it

Two sources.

`simba-intelligence/` is the Simba Intelligence documentation, pulled from the official Mintlify site, which already publishes an LLM-friendly format.
- `llms-full.txt`, the entire SI doc set in one file, made to be read in a single pass.
- `llms.txt`, an index of every SI page.
- `pages/`, the 27 SI pages as individual markdown files.
- `openapi.json`, present but a placeholder only (it is the docs template's sample, with paths like `/plants`). It is not the real SI API. Kept and labelled so its state is obvious.

`logi-devnet/` is the full insightsoftware devnet help centre, all 15,712 articles, covering Logi Report, Logi Info, Dundas, the embedded products (Izenda, Exago), and the legacy v5/v6 era of Logi Composer, plus general entries. Note: the Composer content here is the older v5/v6 (Zoomdata-era) documentation. Current Composer docs are in `logi-composer-current/` below.
- `articles/<product>/<section>/<id>-<title>.md`, every article as markdown, each with frontmatter (title, id, section, product, source URL, last-updated date).
- `manifest.json`, one machine-readable index of all 15,712 articles (id, title, product, section, path, URL, date). Point a script or an agent at this to enumerate everything.
- `llms.txt`, the same index in the llms.txt convention, grouped by product.

`composer-api/` is the real Logi Composer REST API, the structured endpoint list rather than the prose.
- `composer-openapi.json`, the live OpenAPI 3.1 spec pulled from a running Composer instance: 220 paths, 338 operations across 73 tags. This is the genuine API, feed it to any tool that reads OpenAPI.
- `ENDPOINTS.md`, a readable index of every endpoint grouped by tag, for humans and for retrieval.

`logi-composer-current/` is the current Logi Composer product documentation, pulled from the v25 and v26 help-centre sites, which the devnet help centre does not carry.
- `v25/` and `v26/`, each with `articles/<section>/<id>-<title>.md` (877 and 871 articles), plus a `manifest.json` and `llms.txt` index per version.
- This is where the current how-to lives, including the v26.1 feature enhancements. Use this over the legacy Composer content in `logi-devnet/` for anyone on Composer 25 or 26.

## How to use it

Pick whichever fits the customer's stack.

1. ChatGPT Custom GPT. Create a GPT, add the markdown as its knowledge, and it answers product how-to questions from the docs.
2. Claude Project. Add the files as project knowledge and ask in the same way.
3. Your own app, by retrieval or MCP. Index the markdown into a vector store and fetch the matching pages per question, or wrap the repo as an MCP server so a governed assistant can pull docs on demand. `manifest.json` gives you the full file list to ingest.

## Honest limits

- The assistant retrieves, it does not know. Answer quality depends on what got indexed and how the question is phrased; it can still miss or fetch the wrong page.
- This is a snapshot, dated below. Docs change. Re-run the pull to refresh.
- Simba Intelligence publishes no OpenAPI spec for its own NLQ endpoints (`/api/v1/*`, session-authenticated), checked against a live instance. Those are documented in prose in `simba-intelligence/` (the API Usage Guide). The machine-readable spec that does exist is the Composer and discovery API in `composer-api/`, which is the backend SI queries. See `simba-intelligence/API-NOTES.md`.

## How it was built, and how to refresh

Simba Intelligence: pulled from `https://insightsoftware.mintlify.app` (`llms-full.txt`, `llms.txt`, and each page as `.md`).

devnet: pulled through the public Zendesk Help Center API (no token needed; the token route in the Zendesk guides is for admin actions and does not apply to reading published articles). Page-number paging caps at 10,000 articles, so the pull uses cursor paging to get all 15,712, then converts each article to markdown.

Composer API: pulled from a running Composer instance at `/composer/api-docs`, which serves the live OpenAPI spec.

Snapshot taken 2026-06-26.

## A note on what this is

This is a documentation mirror for building and demonstrating AI assistants over insightsoftware products. The source content is insightsoftware's. Treat it as a working asset, refresh it against the live docs before relying on it, and check the snapshot date.
