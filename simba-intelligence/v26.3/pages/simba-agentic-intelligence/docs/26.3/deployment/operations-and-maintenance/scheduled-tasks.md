> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Scheduled tasks

# Scheduled Tasks

This guide documents the background tasks that Simba Intelligence runs automatically on a recurring schedule. These tasks are managed by the Celery Beat scheduler and executed by Celery workers.

## Overview

Simba Intelligence uses a task queue architecture with two key components:

* **Celery Beat** — A scheduler process (`APP_MODE=beat`) that triggers tasks at configured intervals. Runs as a single-replica Kubernetes StatefulSet with a small persistent volume for the `celerybeat-schedule` file. The replica count is fixed by the chart and is not configurable: more than one beat instance would schedule every periodic task multiple times.
* **Celery Workers** — Background processors (`APP_MODE=worker`) that execute the scheduled tasks. Can be scaled horizontally based on workload.

Both are deployed by the Self-Service Analytics (formerly Logi Composer) Helm chart under `simbaIntelligence.celery.beat.*` and `simbaIntelligence.celery.worker.*`.

***

## Task Schedule

### 📋 Build Attribute Cache

| Property | Value |
| - | - |
| **Task name** | `build_attribute_cache_task` |
| **Schedule** | Daily at 3:00 AM (server time) |
| **Purpose** | Pre-populate the field-value cache with the distinct values of each data source's attribute fields |

**What it does:**

1. Retrieves all data sources from Composer using administrative credentials
2. For each data source, fetches the distinct values of its attribute fields
3. Stores them in the Redis field-value cache so the Query Agent can match user text against real values without re-fetching from Composer on every query

**Configuration:**
`FIELD_VALUE_CACHE_BUDGET_MB` sizes this cache. See the [Environment Variables Reference](/simba-agentic-intelligence/docs/26.3/reference/supplementary-resources/environment-variables-reference#caching).

***

### 🧹 Purge and Sync Question Records

| Property | Value |
| - | - |
| **Task name** | `purge_and_sync_question_records_task` |
| **Schedule** | Daily at 3:00 AM (server time) |
| **Purpose** | Clean up old query history records based on the configured retention policy, then re-sync the remaining records into the semantic cache |

**What it does:**

1. Queries the database for question records older than the retention period
2. Deletes expired records to manage database size
3. Syncs the surviving records so the semantic cache reflects what remains

**Configuration:**
The retention period is set with `simbaIntelligence.celery.worker.questionRecordRetentionDays` (`QUESTION_RECORD_RETENTION_DAYS`, default **90 days**). Left empty (the chart default), the value is omitted entirely and the application's internal default applies. Only the worker reads it — beat just publishes the job on its schedule.

***

### 🗑️ Purge Task Results

| Property | Value |
| - | - |
| **Task name** | `purge_task_results_task` |
| **Schedule** | Daily at 3:00 AM (server time) |
| **Purpose** | Delete task result records past their retention window so the task history table does not grow without bound |

**What it does:**

1. Deletes task results whose `finished_at` timestamp is older than the retention window
2. Deletes tasks that never finished whose `created_at` timestamp is older than the retention window

**Configuration:**
Set with `simbaIntelligence.celery.worker.purgeTaskResultsDays` (`PURGE_TASK_RESULTS_DAYS`, default **90 days**). It behaves the same way as `questionRecordRetentionDays` above: empty means the application default applies, and only the worker reads it.

> **📝 Note:** The retention window is a *minimum*, not an exact expiry. Because the purge runs only once a day, a task's results remain accessible for at least the configured number of days and may survive up to roughly 24 hours longer — until the next purge run passes the deadline.

***

### 🔑 Cleanup Expired OAuth Tokens

| Property | Value |
| - | - |
| **Task name** | `cleanup_expired_oauth_tokens_task` |
| **Schedule** | Every 7 days |
| **Purpose** | Remove expired OAuth tokens and authorization codes from the database |

**What it does:**

1. Scans for expired OAuth access tokens, refresh tokens, and authorization codes
2. Deletes expired entries to prevent unbounded database growth

> **📝 Note:** This task is relevant only when the [MCP Server](/simba-agentic-intelligence/docs/26.3/guides/admin-guides/mcp-server-guide) is deployed, as OAuth tokens are used exclusively for MCP client authentication.

***

### 🕸️ Rebuild Schema Graphs

| Property | Value |
| - | - |
| **Task name** | `rebuild_all_schema_graphs_task` |
| **Schedule** | Weekly, Mondays at midnight (server time) |
| **Purpose** | Refresh the cached schema graph for every connection so the Data Source Agent sees current schema |

**What it does:**

1. Iterates over connections and rebuilds each one's schema graph from Composer
2. Stores the rebuilt graph for use by the Data Source Agent

> **📝 Note:** A missing schema graph is built on demand by whoever needs it, so this job exists purely to catch schema drift on connections nobody has touched. It runs at midnight rather than 3:00 AM to stagger its Composer and LLM load away from the other overnight jobs.

***

## Monitoring Scheduled Tasks

### Verifying Beat is Running

```bash theme={null}
# Check the Celery beat pod status
kubectl get pods -l app.kubernetes.io/component=composer-simba-intelligence-beat

# View beat scheduler logs to confirm task triggers
kubectl logs -l app.kubernetes.io/component=composer-simba-intelligence-beat
```

The beat pod logs will show entries like:

```
Scheduler: Sending due task run-purge-task-results (purge_task_results_task)
```

### Verifying Worker Execution

```bash theme={null}
# Check worker pod status
kubectl get pods -l app.kubernetes.io/component=composer-simba-intelligence-worker

# View worker logs for task execution
kubectl logs -l app.kubernetes.io/component=composer-simba-intelligence-worker
```

> **🏷️ Label note:** These labels assume the default chart name. Confirm them for your release with `kubectl get pods -l app.kubernetes.io/instance=<release-name> --show-labels`.

***

## Troubleshooting

### Tasks Not Running

* **Beat pod not healthy** — Verify the beat StatefulSet has a running pod and its persistent volume is attached. The schedule state is stored on disk.
* **Workers not processing** — Check that at least one worker pod is running and connected to Redis. Workers use Redis as the message broker.
* **Redis connectivity** — Confirm `REDIS_URL` is correct and Redis is accessible from both beat and worker pods.

### Task Failures

* **Attribute cache build fails** — Usually caused by Composer connectivity issues or missing LLM configuration. Check worker logs for error details.
* **OAuth cleanup fails** — Typically a database connectivity issue. Verify `POSTGRES_HOST`, `POSTGRES_PORT`, and `POSTGRES_DATABASE` are correct and PostgreSQL is accessible.

> **📝 Note:** All scheduled tasks are idempotent — if a task fails, it will be retried on the next scheduled run without causing data inconsistency.
