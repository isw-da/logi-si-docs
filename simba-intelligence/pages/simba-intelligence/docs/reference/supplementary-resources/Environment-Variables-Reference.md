> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.app/llms.txt
> Use this file to discover all available pages before exploring further.

# Environment Variables Reference

# Environment Variables Reference

This reference documents all environment variables available for configuring Simba Intelligence. Variables are grouped by function and include defaults and descriptions.

> **📝 Note:** LLM provider credentials are not configured via environment variables. They are managed per-tenant through the web interface at `/llm-configuration`. See the [LLM Provider Configuration](/simba-intelligence/docs/guides/admin-guides/LLM-Provider-Configuration) guide.

***

## Application Mode

### APP\_MODE Values

| Mode              | Process         | Description                                                    |
| ----------------- | --------------- | -------------------------------------------------------------- |
| `web`             | Flask/Gunicorn  | Main web application and API server                            |
| `worker`          | Celery worker   | Background task processor for AI queries and data operations   |
| `beat`            | Celery beat     | Periodic task scheduler (suggestions generation, cleanup jobs) |
| `migrate`         | Alembic         | Runs database migrations (upgrade, downgrade, or stamp)        |
| `validate-schema` | Alembic         | Validates current database schema against migration state      |
| `mcp`             | Uvicorn/FastMCP | MCP server with OAuth2 PKCE authentication                     |

***

## Core Infrastructure

| Variable        | Default                    | Description                                                                                                      |
| --------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `MAIN_DB_URL`   | —                          | **Required.** PostgreSQL connection URL (e.g., `postgresql://user:pass@host:5432/dbname`)                        |
| `REDIS_URL`     | `redis://localhost:6379/0` | Redis connection URL for Celery broker and semantic cache                                                        |
| `COMPOSER_HOST` | —                          | **Required.** Logi Composer API base URL (e.g., `http://composer:8080/discovery`)                                |
| `BASE_PATH`     | `""` (empty)               | URL subpath prefix for non-root deployments (e.g., `/intelligence`). Trailing slashes are stripped automatically |
| `PORT`          | `5050`                     | Web server listen port                                                                                           |

***

## Web Server (Gunicorn)

These variables tune the Gunicorn web server that runs the main application (`APP_MODE=web`).

| Variable                | Default | Description                                                               |
| ----------------------- | ------- | ------------------------------------------------------------------------- |
| `GUNICORN_WORKERS`      | `4`     | Number of Gunicorn worker processes                                       |
| `GUNICORN_THREADS`      | `4`     | Number of threads per worker                                              |
| `GUNICORN_TIMEOUT`      | `1200`  | Request timeout in seconds (20 minutes)                                   |
| `GUNICORN_MAX_REQUESTS` | `1000`  | Maximum requests per worker before automatic restart. Helps manage memory |
| `GUNICORN_LOG_LEVEL`    | `info`  | Log level (`debug`, `info`, `warning`, `error`, `critical`)               |
| `GUNICORN_ACCESS_LOG`   | `true`  | Enable access logging (`true` / `false`)                                  |

> **💡 Pro Tip:** For memory-constrained environments, reduce `GUNICORN_WORKERS` and `GUNICORN_MAX_REQUESTS`. For high-throughput deployments, increase workers and threads proportionally to available CPU cores.

***

## MCP Server

These variables configure the MCP server container (`APP_MODE=mcp`).

| Variable              | Default | Description                                                                                               |
| --------------------- | ------- | --------------------------------------------------------------------------------------------------------- |
| `MCP_BASE_URL`        | —       | **Required for MCP.** External-facing URL for OAuth2 PKCE redirect URIs (e.g., `https://your-domain.com`) |
| `MCP_UVICORN_WORKERS` | `4`     | Number of Uvicorn worker processes                                                                        |
| `UVICORN_LOG_LEVEL`   | `info`  | Log level for the MCP Uvicorn server                                                                      |

See the [MCP Server Guide](/simba-intelligence/docs/guides/admin-guides/MCP-Server-Guide) for full deployment details.

***

## Database Migrations

| Variable                | Default   | Description                                                                                                                   |
| ----------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `DISABLE_DB_MIGRATIONS` | `false`   | When `true`, skips Alembic migrations on web startup. Use this when running migrations via a dedicated Kubernetes Job instead |
| `MIGRATIONS_ACTION`     | `upgrade` | Migration action for `APP_MODE=migrate`. Values: `upgrade`, `downgrade`, `stamp`                                              |
| `MIGRATIONS_REVISION`   | —         | Target revision for `downgrade` actions. The `stamp` action always stamps to `head` regardless of this value                  |

> **⚠️ Important:** In production Kubernetes deployments, it is recommended to set `DISABLE_DB_MIGRATIONS=true` on the web container and run migrations via the dedicated `simba-intelligence-db-migrate-job` Helm job instead. This prevents migration race conditions when running multiple web replicas.

***

## CORS Configuration

Cross-Origin Resource Sharing settings for the web application.

| Variable                    | Default                                       | Description                                                                                         |
| --------------------------- | --------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `CORS_ENABLED`              | `false`                                       | Enable CORS headers (`true` / `false`). Disabled by default for same-origin deployments             |
| `CORS_ORIGINS`              | `'self'`                                      | Comma-separated list of allowed origins (e.g., `https://app.example.com,https://admin.example.com`) |
| `CORS_METHODS`              | `GET,POST,PUT,DELETE,OPTIONS`                 | Allowed HTTP methods                                                                                |
| `CORS_ALLOW_HEADERS`        | `Content-Type,Authorization,X-Requested-With` | Allowed request headers                                                                             |
| `CORS_SUPPORTS_CREDENTIALS` | `true`                                        | Allow credentials (cookies, authorization headers) in cross-origin requests                         |
| `CORS_MAX_AGE`              | `86400`                                       | Preflight response cache duration in seconds (24 hours)                                             |

> **📝 Note:** CORS is disabled by default, which is the most secure configuration for same-origin deployments. Only enable CORS if your frontend is hosted on a different domain than the Simba Intelligence API.

***

## Content Security Policy (CSP)

These variables control the Content-Security-Policy response headers.

| Variable                   | Default                  | Description                                              |
| -------------------------- | ------------------------ | -------------------------------------------------------- |
| `SECURITY_HEADERS_ENABLED` | `true`                   | Enable CSP and other security headers (`true` / `false`) |
| `CSP_DEFAULT_SRC`          | `'self'`                 | Default content source policy                            |
| `CSP_SCRIPT_SRC`           | `'self' 'unsafe-inline'` | Allowed JavaScript sources                               |
| `CSP_STYLE_SRC`            | `'self' 'unsafe-inline'` | Allowed CSS sources                                      |
| `CSP_IMG_SRC`              | `'self' data:`           | Allowed image sources                                    |
| `CSP_FONT_SRC`             | `'self' data:`           | Allowed font sources                                     |
| `CSP_CONNECT_SRC`          | `'self'`                 | Allowed AJAX, WebSocket, and EventSource sources         |
| `CSP_FRAME_ANCESTORS`      | `'self'`                 | Controls which origins can embed the page in an iframe   |

> **⚠️ Important:** If you embed Simba Intelligence in an iframe or load external resources (e.g., custom fonts from a CDN), you must adjust the relevant CSP directives. Overly restrictive CSP values can break frontend functionality.

***

## Logging

| Variable     | Default | Description                                                                                                                                                               |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `LOG_FORMAT` | `text`  | Log output format. Values: `text` (human-readable), `json` (structured, suitable for log aggregation)                                                                     |
| `LOG_LEVELS` | `[]`    | JSON array for per-module log level overrides. See the [Logging Configuration Guide](/simba-intelligence/docs/guides/user-guides/Logging-Configuration-Guide) for details |

**Example `LOG_LEVELS` configuration:**

```json theme={null}
[
  {"module": "simba_intelligence.api", "logLevel": "DEBUG"},
  {"module": "simba_intelligence.ai", "logLevel": "INFO"}
]
```

***

## Celery (Background Tasks)

| Variable                    | Default | Description                                                                                                                 |
| --------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------- |
| `CELERY_BEAT_SCHEDULE_FILE` | —       | Custom filesystem path for the Celery beat schedule database. Required when using persistent storage for beat (StatefulSet) |

> **📝 Note:** `REDIS_URL` (listed under Core Infrastructure) is also used as the Celery broker and result backend.

***

## Composer Integration

| Variable                   | Default | Description                                                                                                           |
| -------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------- |
| `DB_HOST`                  | —       | Hostname used in development and test environments when constructing JDBC URLs for Composer data connectors           |
| `COMPOSER_DEFAULT_TIMEOUT` | `60`    | Default timeout in seconds for HTTP requests to Composer. The Helm chart sets this to `30` by default via `extraEnvs` |
