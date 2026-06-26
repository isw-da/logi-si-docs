---
title: "Tracking Scheduled Alert Status"
id: 4402955432215
section: "Composer v6 Developer Tools"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955432215-Tracking-Scheduled-Alert-Status
updated_at: 2021-08-07T17:29:16Z
---

# Tracking Scheduled Alert Status

# Tracking Scheduled Alert Status

The [Console of Refreshing Jobs](https://devnet.logianalytics.com/hc/en-us/articles/4402955651863-Review-Refresh-Jobs) in the UI does not show scheduled alert jobs. However, you can use the `/api/jobs` API endpoint to list all jobs, including the alert-related jobs. For example:

```
http://<host:port>/composer/api/jobs?limit=1000&sort=-lastExecutionEndTime
```

API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.
