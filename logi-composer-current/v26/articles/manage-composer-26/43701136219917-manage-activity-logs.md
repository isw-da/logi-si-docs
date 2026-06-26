---
title: "Manage Activity Logs"
id: 43701136219917
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136219917-Manage-Activity-Logs
updated_at: 2026-05-29T14:08:55Z
---

# Manage Activity Logs

# Manage Activity Logs

The Composer server records user- and server-based activities in log files. These files can be used by administrators to troubleshoot issues that may occur with the Composer server, for example, activities related to setting up data sources or creating visuals and dashboards. When Composer is installed in your network environment, a log file is created.

By default, activity logging is enabled, but some activities are not logged by default. For details, see the [Activities Log Reference Sheet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113237773-Activities-Log-Reference-Sheet).

**Important:** 
Activity logging in `zoomdata-activity.log` is deprecated and will be removed in a future release.
Information previously captured in `zoomdata-activity.log` can be found in other log files such as `access.log`, `service.log`, and by using Composer's [User Auditing](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701124523021-User-Auditing) feature.

You can enable or disable activity logging by calling REST API endpoints.
See [Activity Logging](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701106334605-Activity-Logging). A list of the types of activities that are logged can be found in the [Activities Log Reference Sheet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113237773-Activities-Log-Reference-Sheet).

For more information about other Composer log files, see [Composer Log Files Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701143687181-Composer-Log-Files-Reference).
