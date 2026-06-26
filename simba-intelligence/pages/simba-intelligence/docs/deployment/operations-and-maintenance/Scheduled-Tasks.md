> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.app/llms.txt
> Use this file to discover all available pages before exploring further.

# Scheduled Tasks

# Scheduled Tasks

This guide documents the background tasks that Simba Intelligence runs automatically on a recurring schedule. These tasks are managed by the Celery Beat scheduler and executed by Celery workers.

## Overview

Simba Intelligence uses a task queue architecture with two key components:

* **Celery Beat** — A scheduler process (`APP_MODE=beat`) that triggers tasks at configured intervals. Runs as a Kubernetes StatefulSet with persistent storage to maintain schedule state across restarts.
* **Celery Workers** — Background processors (`APP_MODE=worker`) that execute the scheduled tasks. Can be scaled horizontally based on workload.

***

## Task Schedule

### 📋 Generate Query Suggestions

| Property      | Value                                                          |
| ------------- | -------------------------------------------------------------- |
| **Task name** | `generate_suggestions_scheduled_task`                          |
| **Schedule**  | Daily at 3:00 AM (server time)                                 |
| **Purpose**   | Pre-generate AI-powered query suggestions for all data sources |

**What it does:**

1. Retrieves all data sources from Composer using administrative credentials
2. For each data source, fetches field-level attribute values and statistics
3. Generates natural language question suggestions based on available data
4. Caches the suggestions so they are immediately available when users open the Playground

> **💡 Pro Tip:** Pre-generated suggestions improve the user experience by showing relevant questions instantly when a user selects a data source, rather than generating them on demand.

***

### 🧹 Purge Question Records

| Property      | Value                                                                       |
| ------------- | --------------------------------------------------------------------------- |
| **Task name** | `purge_question_records_task`                                               |
| **Schedule**  | Every 24 hours                                                              |
| **Purpose**   | Clean up old query history records based on the configured retention policy |

**What it does:**

1. Queries the database for question records older than the retention period
2. Deletes expired records to manage database size

**Configuration:**
The retention period is configurable via the Helm chart value `questionRecordRetentionDays` (default: **90 days**).

***

### 🔑 Cleanup Expired OAuth Tokens

| Property      | Value                                                                 |
| ------------- | --------------------------------------------------------------------- |
| **Task name** | `cleanup_expired_oauth_tokens_task`                                   |
| **Schedule**  | Every 7 days                                                          |
| **Purpose**   | Remove expired OAuth tokens and authorization codes from the database |

**What it does:**

1. Scans for expired OAuth access tokens, refresh tokens, and authorization codes
2. Deletes expired entries to prevent unbounded database growth

> **📝 Note:** This task is relevant only when the [MCP Server](/simba-intelligence/docs/guides/admin-guides/MCP-Server-Guide) is deployed, as OAuth tokens are used exclusively for MCP client authentication.

***

## Monitoring Scheduled Tasks

### Verifying Beat is Running

```bash theme={null}
# Check the Celery beat pod status
kubectl get pods -n simba-intelligence | grep beat

# View beat scheduler logs to confirm task triggers
kubectl logs <beat-pod-name> -n simba-intelligence
```

The beat pod logs will show entries like:

```
Scheduler: Sending due task run-generate-suggestions (generate_suggestions_scheduled_task)
```

### Verifying Worker Execution

```bash theme={null}
# Check worker pod status
kubectl get pods -n simba-intelligence | grep worker

# View worker logs for task execution
kubectl logs <worker-pod-name> -n simba-intelligence
```

***

## Troubleshooting

### Tasks Not Running

* **Beat pod not healthy** — Verify the beat StatefulSet has a running pod and its persistent volume is attached. The schedule state is stored on disk.
* **Workers not processing** — Check that at least one worker pod is running and connected to Redis. Workers use Redis as the message broker.
* **Redis connectivity** — Confirm `REDIS_URL` is correct and Redis is accessible from both beat and worker pods.

### Task Failures

* **Suggestion generation fails** — Usually caused by Composer connectivity issues or missing LLM configuration. Check worker logs for error details.
* **OAuth cleanup fails** — Typically a database connectivity issue. Verify `MAIN_DB_URL` is correct and PostgreSQL is accessible.

> **📝 Note:** All scheduled tasks are idempotent — if a task fails, it will be retried on the next scheduled run without causing data inconsistency.
