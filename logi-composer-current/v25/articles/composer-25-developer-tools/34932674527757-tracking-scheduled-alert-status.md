---
title: "Tracking Scheduled Alert Status"
id: 34932674527757
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932674527757-Tracking-Scheduled-Alert-Status
updated_at: 2026-05-26T22:06:10Z
---

# Tracking Scheduled Alert Status

# Tracking Scheduled Alert Status

Use the [Console of Refreshing Jobs](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933114199309-Review-Refresh-Jobs) to view scheduled alert jobs. Optionally, use the `/api/jobs` endpoint to list all jobs, including alert related jobs. For example:

http://<host:port>/composer/api/jobs?limit=1000&sort=-lastExecutionEndTime

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.
