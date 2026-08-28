# insightsoftware product docs, made machine-readable for AI assistants

> **New here?** [`TOOLKIT.md`](TOOLKIT.md) lists every repo in this set, what each
> covers, and how to consume them.


A clean, searchable mirror of insightsoftware's product documentation, organised so an AI assistant can look up the right page and answer from it.

## The problem this solves

End users want to ask an AI assistant how to do something in the product rather than raise a ticket or wait on support. For that to work the assistant needs the product documentation in a form it can read and search. The docs live on help-centre and documentation sites built for people reading them in a browser. A model needs them in a different shape.

Worth being clear on one thing up front: an AI assistant does not memorise documentation. It looks it up each time. So the job is to give it a complete, clean, searchable copy of the docs plus a way to fetch the relevant page for each question. That is what this repo is.

## What's in it

Five trees. Only two of them refresh themselves; see [Refreshing](#refreshing)
before trusting a date.

`simba-intelligence/` is the Simba Intelligence documentation, pulled from the official Mintlify site, which already publishes an LLM-friendly format.
- `llms-full.txt`, the entire SI doc set in one file, made to be read in a single pass.
- `llms.txt`, an index of every SI page.
- `pages/`, the 27 SI pages as individual markdown files.
- `openapi.json`, present but a placeholder only (it is the docs template's sample, and its only two paths are `/plants` and `/plants/{id}`, under the title "OpenAPI Plant Store"). It is not the real SI API. Kept and labelled so its state is obvious.
- `reverse-engineered/`, notes taken against running SI instances where the published docs are silent or lag the release, each one stating how and when it was checked. It includes `apispec_1-26.2.0.json`, the specification the product itself generates at `/apispec_1.json`: Swagger 2.0, titled "Simba Intelligence API", 32 paths, all under `/api/v1/`. That is the real SI API, and the docs site does not publish it.

`logi-devnet/` is the insightsoftware devnet help centre as it stood on 26 June 2026, 15,712 articles. By the `product` field in `manifest.json`: Logi Report 9,344, Logi Info 3,700, Logi Composer 1,306, Izenda 870, Exago 457, General 33, and one article each tagged Logi Symphony and Dundas BI. So it is mostly a Logi Report and Logi Info archive, and anyone hoping for Dundas coverage should look elsewhere. The Composer content here is the older v5/v6 (Zoomdata-era) documentation. Current Composer docs are in `logi-composer-current/` below.
- `articles/<product>/<section>/<id>-<title>.md`, every article as markdown, each with frontmatter (title, id, section, product, source URL, last-updated date).
- `manifest.json`, one machine-readable index of all 15,712 articles (id, title, product, section, path, URL, date). Point a script or an agent at this to enumerate everything.
- `llms.txt`, the same index in the llms.txt convention, grouped by product.
- `meta/` (categories and sections) and `cbp/` (the 158 raw cursor-paged API responses the pull came from), kept so the mirror can be audited against what upstream actually returned.

`composer-api/` is the real Logi Composer REST API, the structured endpoint list rather than the prose. Three specs, because two instances disagree.
- `composer-openapi-26.2.1-bundled.json`, OpenAPI 3.1, pulled live from the SI-bundled Composer 26.2.1 on 27 August 2026: 223 paths, 344 operations.
- `composer-openapi-simba-logisymphony.json`, the same shape from the hosted `simba.logisymphony.com` instance on 26 June 2026: 220 paths, 338 operations.
- `composer-openapi.json`, a stable filename for existing tooling, currently a copy of the bundled 26.2.1 pull.
- `ENDPOINTS.md`, a readable index of the union, 346 operations across 76 tags, with every row marked for the instance it was seen on. 336 operations are on both, 8 only on the bundled instance, 2 only on the hosted one. `verify-endpoints.py` is the gate that keeps the index honest against both files.

`logi-composer-current/` is the current Logi Composer product documentation, pulled from the v25 and v26 help-centre sites, which the devnet help centre does not carry.
- `v25/` and `v26/`, each with `articles/<section>/<id>-<title>.md`, plus a `manifest.json` and `llms.txt` index per version. 877 v25 articles and 883 v26 articles, matching upstream when the refresh last ran.
- Count the manifest, not the files on disk. There are more `.md` files than manifest entries (934 in v25, 1,190 in v26) because the refresh writes a new file when upstream retitles an article and never deletes the old slug. The manifest is regenerated from upstream every run, so it is the list to ingest; the orphans are older copies of articles that are still present under their current names.
- This is where the current how-to lives. Use it over the legacy Composer content in `logi-devnet/` for anyone on Composer 25 or 26.

`logi-report-api/` is the Logi Report Server Web API, which is a different product with a different spec format. `logireport-openapi.json` and `.yaml` are Swagger 2.0, 124 paths and 225 operations across 11 tags, copied out of a running Logi Report Server 26.2 SP1 rather than reconstructed from prose. `ENDPOINTS.md` indexes it and `PROVENANCE.md` says where it came from. The fuller Logi Report corpus lives in [`logi-report-kb`](https://github.com/isw-da/logi-report-kb), which also holds the checksum and the gate that re-checks this spec against a running container.

## How to use it

Pick whichever fits the customer's stack.

1. ChatGPT Custom GPT. Create a GPT, add the markdown as its knowledge, and it answers product how-to questions from the docs.
2. Claude Project. Add the files as project knowledge and ask in the same way.
3. Your own app, by retrieval or MCP. Index the markdown into a vector store and fetch the matching pages per question, or wrap the repo as an MCP server so a governed assistant can pull docs on demand. `manifest.json` gives you the full file list to ingest.

## Honest limits

- The assistant retrieves, it does not know. Answer quality depends on what got indexed and how the question is phrased; it can still miss or fetch the wrong page.
- Only `logi-composer-current/v25` and `v26` refresh themselves weekly. Those are the only two entries in `SOURCES` in `scripts/refresh.py`. Everything else is a dated snapshot: `logi-devnet/` and the Mintlify part of `simba-intelligence/` (26 June 2026), `simba-intelligence/reverse-engineered/` (July 2026, each file dated in its own header), `composer-api/` (26 June and 27 August 2026, one date per spec) and `logi-report-api/` (copied here 28 August 2026 from a 26.2 SP1 install).
- `logi-devnet/` is frozen rather than retired. The upstream Zendesk API still answers: on 28 August 2026 `https://devnet.logianalytics.com/api/v2/help_center/en-us/articles.json` reported 15,713 articles against the 15,712 mirrored here. Adding it back to `SOURCES` is a small change, and nobody has needed it enough to make it.
- The SI documentation site publishes no usable OpenAPI document: the `openapi.json` it ships is the template's plant-store sample. The product itself does generate one, and a live copy is kept at `simba-intelligence/reverse-engineered/apispec_1-26.2.0.json` (32 paths, all `/api/v1/`). Treat it as a capture from one version of one instance rather than a published contract, because insightsoftware does not publish it. The Composer and discovery API in `composer-api/`, which is the backend SI queries, is the spec that is served from a documented endpoint. See `simba-intelligence/API-NOTES.md`.

## Refreshing

**The two Composer help-centre trees refresh themselves. Nothing else does.**
`.github/workflows/refresh-mirror.yml` runs `scripts/refresh.py` at 06:00 UTC every Monday
and commits anything that moved, for `logi-composer-current/v25` and `v26` only. It needs
no secrets, because both sources are public unauthenticated Help Centre APIs, and it costs
nothing, because Actions minutes are free on a public repository. Run it on demand from the
Actions tab with **Run workflow**, or locally:

```bash
pip install -r requirements-refresh.txt
python scripts/refresh.py --dry-run   # report the delta, write nothing
python scripts/refresh.py             # write it
```

The refresh is additive: a file is rewritten only when it is new or upstream's `updated_at`
has moved, so a routine run produces a small diff rather than rewriting the corpus. Additive
also means it never deletes, which is where the orphan slug files above come from.

`logi-devnet/` and `simba-intelligence/` are not in `SOURCES` and are not touched by the
weekly job. `python3 scripts/refresh.py --dry-run` prints exactly what it covers, and on
28 August 2026 it reported v25 877 upstream against 877 mirrored, v26 883 against 883.

**`composer-api/` is NOT automated and cannot be.** Those OpenAPI specs come from a running
Composer instance, not a documentation site, and CI cannot reach one. They are pulled by
hand, and each is named for the instance that served it, because two instances demonstrably
disagree. See `composer-api/ENDPOINTS.md`.

**A note on the converter.** `scripts/refresh.py` uses `markdownify` rather than a hand-rolled
regex converter. The regex version was tried first and lost cross-reference links and broke
headings onto two lines, which would have degraded the whole Composer corpus while looking
like a routine refresh. The one dependency in `requirements-refresh.txt` buys that away.
Note what a `--dry-run` does and does not tell you: it compares upstream's `updated_at`
against the stamp in each mirrored file, so zero to write means nothing moved upstream, not
that the converter would reproduce the committed bytes.

## How it was built, and how to refresh

Simba Intelligence: pulled from `https://insightsoftware.mintlify.app` (`llms-full.txt`, `llms.txt`, and each page as `.md`).

devnet: pulled through the public Zendesk Help Center API (no token needed; the token route in the Zendesk guides is for admin actions and does not apply to reading published articles). Page-number paging caps at 10,000 articles, so the pull uses cursor paging to get all 15,712, then converts each article to markdown.

Composer API: pulled from a running Composer instance at `/composer/api-docs` or `/discovery/api-docs`, which serves the live OpenAPI spec. The bundled 26.2.1 spec came from a local SI deployment, the hosted one from `simba.logisymphony.com`, and each file records its own origin in `servers[0].url`.

Composer v25 and v26: pulled by `scripts/refresh.py` through the two version-specific Help Centre APIs, and re-pulled weekly.

Logi Report Server API: copied out of a running Logi Report Server 26.2 SP1 install at `/opt/LogiReport/Server/help/webapi/logireportserver.yaml`. See `logi-report-api/PROVENANCE.md`.

Dates per tree are in [Honest limits](#honest-limits) above. For `logi-composer-current/` the date that matters is the last weekly run, which the `updated_at` fields in each `manifest.json` record.

## Gates

Three. Run them from a fresh clone; none needs network or credentials, and `verify_toolkit.py`
asks GitHub only if `gh` is authenticated, naming the skip when it is not.

```bash
python3 composer-api/verify-endpoints.py   # ENDPOINTS.md against both Composer specs
python3 scripts/verify_toolkit.py          # the repo table against toolkit.json and GitHub
python3 scripts/verify_claims.py           # the counts in this README against the files
echo $?                                    # on its own line; a pipe reports the pipe's status
```

`.github/workflows/release.yml` runs every `verify-*` script in the repository and refuses to
cut a release from a red tree. `verify_claims.py` exists because four numbers in this README
were wrong at once: the Composer spec had been re-pulled and grown, v26 had gained twelve
articles, a whole tree had arrived undocumented, and one file pointed at paths that live in a
different repository. Prose about a corpus goes stale silently unless something recomputes it.

## A note on what this is

This is a documentation mirror for building and demonstrating AI assistants over insightsoftware products. The source content is insightsoftware's, and mirroring it here does not relicense it; see [`NOTICE`](NOTICE). Treat it as a working asset, refresh it against the live docs before relying on it, and check the dates above.
