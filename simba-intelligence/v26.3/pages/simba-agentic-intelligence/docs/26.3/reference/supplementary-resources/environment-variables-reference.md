> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Environment variables reference

# Environment Variables Reference

This reference documents all environment variables available for configuring Simba Intelligence. Variables are grouped by function and include defaults and descriptions.

> **📝 Note:** LLM provider credentials are not configured via environment variables. They are managed per-tenant through the web interface at `/llm-configuration`. See the [LLM Provider Configuration](/simba-agentic-intelligence/docs/26.3/guides/admin-guides/llm-provider-configuration) guide.

***

## Application Mode

### APP\_MODE Values

| Mode | Process | Description |
| - | - | - |
| `web` | Flask/Gunicorn | Main web application and API server |
| `worker` | Celery worker | Background task processor for AI queries and data operations |
| `beat` | Celery beat | Periodic task scheduler (suggestions generation, cleanup jobs) |
| `migrate` | Alembic | Runs database migrations (upgrade, downgrade, or stamp) |
| `validate-schema` | Alembic | Validates current database schema against migration state |
| `mcp` | Uvicorn/FastMCP | MCP server with OAuth2 PKCE authentication |
| `full` | All of the above | Single-container mode that runs migrations, then web + worker + beat + MCP as child processes. Intended for Docker and local development, **not** Kubernetes |

> **⚠️ Important:** `full` mode starts a beat scheduler, so exactly one container may run it. Do not scale a `full`-mode deployment.

### Full Mode Options

These apply only when `APP_MODE=full`.

| Variable | Default | Description |
| - | - | - |
| `FULL_MODE_INCLUDE_MCP` | `true` | Set to `false` to start without the MCP server |
| `FULL_MODE_INCLUDE_BEAT` | `true` | Set to `false` to start without the beat scheduler |

***

## Core Infrastructure

| Variable | Default | Description |
| - | - | - |
| `MAIN_DB_URL` | — | **Required** unless the `POSTGRES_*` variables below are set. PostgreSQL connection URL (e.g., `postgresql://user:pass@host:5432/dbname`) |
| `REDIS_URL` | `redis://localhost:6379/0` | Redis connection URL for Celery broker and semantic cache |
| `COMPOSER_HOST` | — | **Required.** Cluster-internal Logi Composer API base URL used for server-to-server calls (e.g., `http://composer:8080/discovery`) |
| `COMPOSER_PUBLIC_URL` | — | **Required.** Browser-reachable Composer base URL *including its context path* (e.g., `https://analytics.example.com/composer`). Used for embedded visualizations and browser redirects, which cannot resolve `COMPOSER_HOST`. Must be an absolute `http`/`https` URL with no query string or fragment |
| `BASE_PATH` | `""` (empty) | URL subpath prefix for non-root deployments (e.g., `/intelligence`). Trailing slashes are stripped automatically |
| `PORT` | `5050` | Web server listen port |

> **📝 Note:** `COMPOSER_HOST` and `COMPOSER_PUBLIC_URL` are distinct and both required. The first is the in-cluster service address; the second is what a user's browser can reach. Simba Intelligence is always served directly below Composer's context path (`<context-path>/intelligence`) — that location is derived from `COMPOSER_PUBLIC_URL` and is not configurable, because Composer scopes its session cookie to its own context path.

### Database Connection via Components

When `MAIN_DB_URL` is not set, the connection URL is constructed from these variables instead. This is how the Helm chart wires the database, since it handles URL-encoding of passwords containing special characters (`@`, `:`, `/`).

| Variable | Default | Description |
| - | - | - |
| `POSTGRES_USER` | — | **Required** (when `MAIN_DB_URL` is unset). Database username |
| `POSTGRES_PASSWORD` | — | **Required** (when `MAIN_DB_URL` is unset). Database password. URL-encoded automatically |
| `POSTGRES_HOST` | — | **Required** (when `MAIN_DB_URL` is unset). Database hostname |
| `POSTGRES_PORT` | `5432` | Database port |
| `POSTGRES_DATABASE` | — | **Required** (when `MAIN_DB_URL` is unset). Database name |
| `POSTGRES_EXTRA_ARGS` | `""` (empty) | Extra query string appended to the constructed URL (e.g., `?sslmode=require`) |

> **⚠️ Important:** If neither `MAIN_DB_URL` nor the full set of `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, and `POSTGRES_DATABASE` is provided, startup fails immediately.

***

## Web Server (Gunicorn)

These variables tune the Gunicorn web server that runs the main application (`APP_MODE=web`).

| Variable | Default | Description |
| - | - | - |
| `GUNICORN_WORKERS` | `4` | Number of Gunicorn worker processes |
| `GUNICORN_THREADS` | `4` | Number of threads per worker |
| `GUNICORN_TIMEOUT` | `1200` | Request timeout in seconds (20 minutes) |
| `GUNICORN_MAX_REQUESTS` | `1000` | Maximum requests per worker before automatic restart. Helps manage memory |
| `GUNICORN_LOG_LEVEL` | `info` | Log level (`debug`, `info`, `warning`, `error`, `critical`) |
| `GUNICORN_ACCESS_LOG` | `true` | Enable access logging (`true` / `false`) |

> **💡 Pro Tip:** For memory-constrained environments, reduce `GUNICORN_WORKERS` and `GUNICORN_MAX_REQUESTS`. For high-throughput deployments, increase workers and threads proportionally to available CPU cores.

***

## MCP Server

These variables configure the MCP server container (`APP_MODE=mcp`).

| Variable | Default | Description |
| - | - | - |
| `MCP_BASE_URL` | — | **Required for MCP.** External-facing URL for OAuth2 PKCE redirect URIs (e.g., `https://your-domain.com`) |
| `MCP_UVICORN_WORKERS` | `4` | Number of Uvicorn worker processes |
| `UVICORN_LOG_LEVEL` | `info` | Log level for the MCP Uvicorn server |

See the [MCP Server Guide](/simba-agentic-intelligence/docs/26.3/guides/admin-guides/mcp-server-guide) for full deployment details.

***

## Database Migrations

| Variable | Default | Description |
| - | - | - |
| `DISABLE_DB_MIGRATIONS` | `false` | When `true`, skips Alembic migrations on web startup. Use this when running migrations via a dedicated Kubernetes Job instead |
| `MIGRATIONS_ACTION` | `upgrade` | Migration action for `APP_MODE=migrate`. Values: `upgrade`, `downgrade`, `stamp` |
| `MIGRATIONS_REVISION` | — | Target revision for `downgrade` actions. The `stamp` action always stamps to `head` regardless of this value |

> **⚠️ Important:** In production Kubernetes deployments, it is recommended to set `DISABLE_DB_MIGRATIONS=true` on the web container and run migrations via the dedicated `simba-intelligence-db-migrate-job` Helm job instead. This prevents migration race conditions when running multiple web replicas.

***

## CORS Configuration

Cross-Origin Resource Sharing settings for the web application.

| Variable | Default | Description |
| - | - | - |
| `CORS_ENABLED` | `false` | Enable CORS headers (`true` / `false`). Disabled by default for same-origin deployments |
| `CORS_ORIGINS` | `'self'` | Comma-separated list of allowed origins (e.g., `https://app.example.com,https://admin.example.com`) |
| `CORS_METHODS` | `GET,POST,PUT,DELETE,OPTIONS` | Allowed HTTP methods |
| `CORS_ALLOW_HEADERS` | `Content-Type,Authorization,X-Requested-With` | Allowed request headers |
| `CORS_SUPPORTS_CREDENTIALS` | `true` | Allow credentials (cookies, authorization headers) in cross-origin requests |
| `CORS_MAX_AGE` | `86400` | Preflight response cache duration in seconds (24 hours) |

> **📝 Note:** CORS is disabled by default, which is the most secure configuration for same-origin deployments. Only enable CORS if your frontend is hosted on a different domain than the Simba Intelligence API.

***

## Content Security Policy (CSP)

These variables control the Content-Security-Policy response headers.

| Variable | Default | Description |
| - | - | - |
| `SECURITY_HEADERS_ENABLED` | `true` | Enable CSP and other security headers (`true` / `false`) |
| `CSP_DEFAULT_SRC` | `'self'` | Default content source policy |
| `CSP_SCRIPT_SRC` | `'self' 'unsafe-inline'` | Allowed JavaScript sources |
| `CSP_STYLE_SRC` | `'self' 'unsafe-inline'` | Allowed CSS sources |
| `CSP_IMG_SRC` | `'self' data:` | Allowed image sources |
| `CSP_FONT_SRC` | `'self' data:` | Allowed font sources |
| `CSP_CONNECT_SRC` | `'self'` | Allowed AJAX, WebSocket, and EventSource sources |
| `CSP_FRAME_ANCESTORS` | `'self'` | Controls which origins can embed the page in an iframe |

> **⚠️ Important:** If you embed Simba Intelligence in an iframe or load external resources (e.g., custom fonts from a CDN), you must adjust the relevant CSP directives. Overly restrictive CSP values can break frontend functionality.

***

## Logging

| Variable | Default | Description |
| - | - | - |
| `LOG_FORMAT` | `text` | Log output format. Values: `text` (human-readable), `json` (structured, suitable for log aggregation) |
| `LOG_LEVELS` | `[]` | JSON array for per-module log level overrides. See the [Logging Configuration Guide](/simba-agentic-intelligence/docs/26.3/guides/user-guides/logging-configuration-guide) for details |

**Example `LOG_LEVELS` configuration:**

```json theme={null}
[
  {"module": "simba_intelligence.api", "logLevel": "DEBUG"},
  {"module": "simba_intelligence.ai", "logLevel": "INFO"}
]
```

***

## Celery (Background Tasks)

| Variable | Default | Description |
| - | - | - |
| `CELERY_BEAT_SCHEDULE_FILE` | — | Custom filesystem path for the Celery beat schedule database. Required when using persistent storage for beat (StatefulSet) |

> **📝 Note:** `REDIS_URL` (listed under Core Infrastructure) is also used as the Celery broker and result backend.

***

## Data Retention

These control how long Simba Intelligence keeps historical records. Both are read by the **worker** process from inside the purge task body, so they only need to be set on worker pods — beat merely publishes the job on its schedule and never reads them.

| Variable | Default | Description |
| - | - | - |
| `PURGE_TASK_RESULTS_DAYS` | `90` | Minimum number of days a task's results stay accessible to users. Task results older than this are deleted by the `purge_task_results_task` job |
| `QUESTION_RECORD_RETENTION_DAYS` | `90` | Minimum number of days question (query history) records are retained before the `purge_and_sync_question_records_task` job deletes them |

> **📝 Note:** These are *minimums*, not exact expiries. The purge jobs run once a day (3:00 AM server time), so a record can survive up to roughly 24 hours past its retention deadline — until the next purge run. See [Scheduled Tasks](/simba-agentic-intelligence/docs/26.3/deployment/operations-and-maintenance/scheduled-tasks).

In the Helm chart these map to `simbaIntelligence.celery.worker.purgeTaskResultsDays` and `simbaIntelligence.celery.worker.questionRecordRetentionDays`. Both default to `""`, which omits the environment variable entirely and leaves the application defaults above in effect — only set a number to override.

***

## Composer Integration

| Variable | Default | Description |
| - | - | - |
| `COMPOSER_ADMIN_USERNAME` | `admin` | Composer supervisor account used for administrative API calls and scheduled tasks that run without a user session |
| `COMPOSER_ADMIN_PASSWORD` | — | Password for `COMPOSER_ADMIN_USERNAME` |
| `COMPOSER_DEFAULT_TIMEOUT` | `60` | Default timeout in seconds for HTTP requests to Composer. The Helm chart sets this to `30` by default via `extraEnvs` |

> **⚠️ Important:** In Helm deployments you do not set the admin credentials directly — the chart injects both from the same admin-credentials Secret that Composer itself uses, driven by `zoomdataWeb.adminPassword` (or `zoomdataWeb.existingSecret`). Composer leaves that password unset by default, so the chart fails the install or upgrade when `simbaIntelligence.enabled` is true and no admin password is configured. Without it, Simba Intelligence pods start healthy but cannot call Composer's API.

***

## Caching

The **field-value cache** stores the distinct values seen for each data-source attribute field (e.g., the list of values in a "Region" or "Status" column), so the Query Agent can match user text against real values without re-fetching them from Composer on every query.

| Variable | Default | Description |
| - | - | - |
| `FIELD_VALUE_CACHE_BUDGET_MB` | `450` | Estimated memory budget in MB for the Redis field-value (attribute-value) cache. Currently only used for attribute fields. Approximate — not a hard cap. Scale with pod memory |

> **📝 Note:** `FIELD_VALUE_CACHE_BUDGET_MB` sizes only this one cache — it is **not** a limit on Redis's total memory usage. Redis also holds the semantic/question-record cache, suggestions cache, and Celery broker data, none of which count against this budget. It is set via `extraEnvs` on both the `web` and `worker` deployments (see `APP_MODE` above) in the Helm chart's `values.yaml`. Keep the value identical across both — the cache is shared/tenant-scoped in Redis, not tuned per pod type.

***

## LLM Transport

LLM provider credentials are configured per tenant in the UI, not via environment variables. The one exception is the transport timeout for the experimental Ollama provider.

| Variable | Default | Description |
| - | - | - |
| `OLLAMA_TIMEOUT` | `300` | Connection timeout in seconds for the experimental Ollama provider |
