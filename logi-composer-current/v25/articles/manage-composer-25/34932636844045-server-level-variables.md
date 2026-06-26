---
title: "Server-Level Variables"
id: 34932636844045
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932636844045-Server-Level-Variables
updated_at: 2026-05-26T22:10:31Z
---

# Server-Level Variables

# Server-Level Variables

Server-level variables can be viewed by Composer administrators or members of the Supervisors group in the Server-Level Variables work area.

**Important:** 
Server-level variables are set during installation and must not be changed without understanding how the change affects or compromises your environment. If you must change a variable here, contact [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support).
Do not add or delete server-level variables.

Select the **Advanced** menu option to access the Server-Level Variables work area.

Server-level variables are defined as key-value pairs. You can enable or disable the listed variables below if needed. Select **Save** to save and apply any changes you make in this work area.

**Caution:** Changing toggles or editing content other than as instructed in this work area may prevent your users from using various components of Logi Composer.

| Key (Server-Level Variable) | Value | Description |
| --- | --- | --- |
| allow-dashboard-and report sharing-within-tenant | false (default) | Enable or disable dashboard sharing options for sharing content with users, established groups, and everyone within your tenants or environment.  See [Share a Dashboard with Users](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932824740749-Share-a-Dashboard-with-Users). |
| scheduled-report-file-drop | false (default) | Enable or disable users' ability to deliver a scheduled dashboard report to an SFTP location.  When set to `true`, users can select an SFTP file location you have defined to accept the scheduled report.  When set to `false`, users do not see an SFTP option for scheduled reports.  Define the settings for your environment at the instance level in `zoomdata.properties`or by passing along tenant or user attributes to `zoomdata.properties`. See  [Scheduled Dashboard Report Properties](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932831429389--Scheduled-Dashboard-Report-Properties). |
| timebar-snap-to-interval | false (default) | Enable or disable to control the granularity to which the time bar slider snaps.  When set to `true`, moving the time bar slider adjusts to the closest interval of the defined granularity available in the data set.  When set to `false`, moving the time bar slider adjusts to the nearest smallest granularity available in the data set. |
