---
title: "Import a Dashboard"
id: 4405850983831
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850983831-Import-a-Dashboard
updated_at: 2021-09-21T01:27:46Z
---

# Import a Dashboard

# Import a Dashboard

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) The ability to import dashboard definitions was deprecated in Composer 6.9 and will be removed in a future release.

When imported using the API, dashboards can be imported using an overwrite strategy that is applied to the dashboard itself, the visuals included in the dashboard, and the data sources associated with the visuals in the dashboard. See [*Overwrite Policy Behavior*](#overwrite).

To import a dashboard configuration:

1. Log into Composer as an administrator or as a user with the **Can Create new Data Sources**, **Can Create Visuals** (or **Can Administer Visuals**), and **Can Create Dashboards**[group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).

   If you are logged into Composer as a user who can maintain data source configurations but cannot maintain connection definitions (your [group privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) include **Can Create new Data Sources**, but **not****Can Manage Connections**), the following dashboard import behavior occurs:

   * If the data store connections used by the data sources in the dashboard visuals have already been defined to the Composer instance, the dashboard is successfully imported.
   * If the data store connections used by the data sources in the dashboard visuals have not previously been to defined to the Composer instance, the dashboard is **not** imported and an error message displays because your user account does not have authorization to create data store connections.
2. Select **Library** on the [top-level navigation banner](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner) or the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu), or select the **Dashboards** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The dashboard library displays.
3. At the top of the page, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743882903/dash-import_123x28.png).
4. Browse to and select the `json` file for the dashboard, then select
   **Open**. The dashboard is imported.

When you import a dashboard, the visuals, data store connections and data source configurations used by the dashboard visuals are also imported.

By default, if a dashboard with the same name already exists, the imported dashboard is imported with the same name, but with the date and time appended. If the two dashboards contain any visuals with the same name, the import will fail. However, if you use the API to perform the import, you can request that an imported dashboard and its visuals and data sources overwrite the existing ones. See [*Overwrite Policy Behavior*](#overwrite)

## Overwrite Policy Behavior

The overwrite policy can be used only for dashboard imports requested using the API. Specify the query parameter, `strategy` with the `POST /api/dashboards/import` endpoint. Valid values for strategy are `OVERWRITE` or `USE_EXISTING_OR_CREATE`.

* Specify `OVERWRITE` to implement the new overwrite policy.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) To import (using the OVERWRITE strategy) a dashboard that uses a Fusion data source with custom metrics or derived fields, users with the necessary write permissions and the **Can Manage Connections**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) must also have read permissions for the Fusion data source and its parent sources.
* Specify `USE_EXISTING_OR_CREATE` to continue to use the existing import policy (importing the dashboard with a slightly altered name). This is the default value and will be used if `strategy` is not specified.

To use the overwrite policy, your Composer user account must meet all of the authorization criteria described below.

* Your Composer user account must be an Administrator account or be assigned to a group with the **Can Administer Visuals**, **Can Administer Dashboards**, and **Can Administer Sources**[group privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference). (Your Composer must also be assigned to a group with the **Can Create Visual**, **Can Create Dashboards**, and **Can Create new Data Sources**[group privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference), but these privileges are automatically assigned with the **Can Administer Visuals**, **Can Administer Dashboards**, and **Can Administer Sources**[group privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).)
* Your user account must have both Read and Write permissions for the [data source](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions), [dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4405859259159-About-Dashboard-Permissions), and [visuals](https://devnet.logianalytics.com/hc/en-us/articles/4405851253271-About-Visual-Permissions) included in the dashboard import attempt.

Assuming the authorization criteria are met, importing a dashboard using the overwrite policy will overwrite any dashboards with the same name using the following workflow:

| Imported Item | Condition | What Happens |
| --- | --- | --- |
| **Dashboard** | Imported dashboard name matches an existing dashboard | The existing dashboard is updated with the settings and specifications from the imported dashboard. |
| Imported dashboard name does not match an existing dashboard | A new dashboard is created. |
| **Visuals Imported With the Dashboard** | Imported visual name matches an existing visual | The existing visual is updated with the settings and specifications from the imported visual. |
| Imported visual name does not match an existing visual | A new visual is created. |
| Imported dashboard does not include a visual that is in the existing dashboard | The existing dashboard is updated with the settings and specifications from the imported dashboard. The existing dashboard is no longer associated with the missing visual, but the visual remains in the system. |
| **Sources Imported With the Dashboard** | Imported data source name matches an existing data source | The existing data source definition is updated with the settings and specifications from the imported data source. |
| Imported data source name does not match an existing data source | A new data source is created. |
| **Connections** | Connections validate with the data source. Import behavior for connection definitions is not affected by the import policy. | |
