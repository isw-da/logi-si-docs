---
title: "Manage Activity Logs"
id: 34933069110925
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933069110925-Manage-Activity-Logs
updated_at: 2026-05-26T22:07:43Z
---

# Manage Activity Logs

# Manage Activity Logs

The Composer server records user- and server-based activities in log files. These files can be used by Composer administrators to troubleshoot issues that may occur with the Composer server, for example, activities related to setting up data sources or creating visuals and dashboards. When Composer is installed in your network environment, a log file is created.

By default, activity logging is enabled, but some activities are not logged by default. For details, see the [Activities Log Reference Sheet](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933133494797-Activities-Log-Reference-Sheet).

**Important:** 
Activity logging in `zoomdata-activity.log` is deprecated and will be removed in a future release.
Information previously captured in `zoomdata-activity.log` can be found in other log files such as `access.log`, `service.log`, and by using Composer's [User Auditing](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933076803085-User-Auditing) feature.

You can enable or disable activity logging by calling REST API endpoints.
See [Activity Logging](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933086348813-Activity-Logging). A list of the types of activities that are logged can be found in the [Activities Log Reference Sheet](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933133494797-Activities-Log-Reference-Sheet).

For more information about other Composer log files, see [Composer Log Files Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933097277069-Composer-Log-Files-Reference).
