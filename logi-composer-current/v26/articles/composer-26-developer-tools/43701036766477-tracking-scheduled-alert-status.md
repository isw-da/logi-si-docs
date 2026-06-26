---
title: "Tracking Scheduled Alert Status"
id: 43701036766477
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036766477-Tracking-Scheduled-Alert-Status
updated_at: 2026-05-29T14:07:12Z
---

# Tracking Scheduled Alert Status

# Tracking Scheduled Alert Status

Use the [Console of Refreshing Jobs](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701140188173-Review-Refresh-Jobs) to view scheduled alert jobs. Optionally, use the `/api/jobs` endpoint to list all jobs, including alert related jobs. For example:

http://<host:port>/composer/api/jobs?limit=1000&sort=-lastExecutionEndTime

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.
