---
title: "Server-Level Variables"
id: 43701053868173
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables
updated_at: 2026-08-26T07:11:40Z
---

# Server-Level Variables

# Server-Level Variables

Server-level variables can be viewed by Composer administrators or members of the Supervisors group in the Server-Level Variables work area.

**Important:** 
Server-level variables are set during installation and must not be changed without understanding how the change affects or compromises your environment. If you must change a variable here, contact [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support).
Do not add or delete server-level variables.

Select the **Advanced** menu option to access the Server-Level Variables work area.

Server-level variables are defined as key-value pairs. You can enable or disable the listed variables below if needed. Select **Save** to save and apply any changes you make in this work area.

**Caution:** Changing toggles or editing content other than as instructed in this work area or as directed by Technical Support may prevent your users from using various components of Logi Composer.

| Key (Server-Level Variable) | Value | Description |
| --- | --- | --- |
| allow-dashboard-and-report-sharing-within-tenant | false (default) | Enable or disable dashboard and self service report sharing options for sharing content with users, established groups, and everyone within your tenants or environment.  See [Share a Dashboard or Self Service Report with Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701077162637-Share-a-Dashboard-or-Self-Service-Report-with-Users). |
| allow-sending-reports-to-external-emails | true (default) | Enabled by default, allows users with appropriate privileges to send reports to external email addresses (user@example.com).  Disable to prevent users from sending reports to users external to your data analytics environment. Any user included in a report send in your environment will get the report sent to the email address associated with their user account. |
| enable-dundas-connector | false (default) | Disabled by default, enable to allow users with appropriate privileges [to register the connector server](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042690957-Register-a-New-Connector-Server), define a connector, and create or [update sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054605453-Modify-Data-Store-Connections#Reconnec) to access data hosted in a Dundas BI environment for use in this analytics environment. |
| enhanced-experience | The default setting is determined by your installation or transition path. See [Transitioning for Symphony and Composer Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968228172557-Transitioning-for-Symphony-and-Composer-Users). | Enable or disable the enhanced user experience layout and theme (`d+a_light`) for your environment.  For environments transitioning from Symphony, this is `true` (enabled) by default.  For fresh installations of Composer v26.2 or later releases, this is `false` (disabled) by default.  For environments transitioning from earlier releases of Composer, this is `false` (disabled) by default.  See [User Interface Themes: v26.2 and Later](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163831053-Manage-User-Interface-Themes#User2) and [Themes and UI Updates](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077251302669-Themes-and-UI-Updates).  **Caution:** Update your custom theme and enable the `enhanced-experience` toggle before upgrading past version 26.2. The enhanced homepage and navigation will become the standard experience for all users in the near future. We recommend making these updates now to ensure a smooth transition. |
| scheduled-report-file-drop | false (default) | Enable or disable users' ability to deliver a scheduled dashboard report or self service report to an SFTP location.  When set to `true`, users can select an SFTP file location you have defined to accept the scheduled report.  When set to `false`, users do not see an SFTP option for scheduled reports.  Define the settings for your environment at the instance level in `zoomdata.properties`or by passing along tenant or user attributes to `zoomdata.properties`. See  [Scheduled Report Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701077034381--Scheduled-Report-Properties). |
| self-service-reports | false (default) | Enable or disable self service reports in your environment.  When set to `true`, users with appropriate permissions can create self service reports in the Reports Library.  When set to `false`, users do not see self service report options or a Reports Library.  For more information about configuring your environment and planning for self service reporting, see [Self Service Report Microservice](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice). |
| timebar-snap-to-interval | false (default) | Enable or disable to control the granularity to which the time bar slider snaps.  When set to `true`, moving the time bar slider adjusts to the closest interval of the defined granularity available in the data set.  When set to `false`, moving the time bar slider adjusts to the nearest smallest granularity available in the data set. |
