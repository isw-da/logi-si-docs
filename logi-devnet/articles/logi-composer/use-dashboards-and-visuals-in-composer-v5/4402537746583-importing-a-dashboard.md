---
title: "Importing a Dashboard"
id: 4402537746583
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537746583-Importing-a-Dashboard
updated_at: 2021-09-15T02:20:56Z
---

# Importing a Dashboard

# Importing a Dashboard

If you are logged into Composer as a user who can maintain data source configurations but cannot maintain connection definitions (your [group privileges](https://devnet.logianalytics.com/hc/en-us/articles/4402537668503-Group-Privilege-Reference) include **Can Create new Data Sources**, but **not****Can Manage Connections**), the following dashboard import behavior occurs:

* If the data store connections used by the data sources in the dashboard visuals have already been defined to the Composer instance, the dashboard is successfully imported.
* If the data store connections used by the data sources in the dashboard visuals have not previously been to defined to the Composer instance, the dashboard is **not** imported and an error message displays because your user account does not have authorization to create data store connections.

If you are logged in as a Composer administrator or as a user who can maintain both data source configurations and connection definitions (your [group privileges](https://devnet.logianalytics.com/hc/en-us/articles/4402537668503-Group-Privilege-Reference) include **Can Create new Data Sources** and **Can Manage Connections**), dashboard imports should work every time.

To import a dashboard configuration:

1. Log into Composer as an administrator or as a user with the **Can Create new Data Sources**[group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402537668503-Group-Privilege-Reference).
2. Select **Library** on the [top-level navigation banner](https://devnet.logianalytics.com/hc/en-us/articles/4402552863383-The-Top-Level-Navigation-Banner) or the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537848215-The-Composer-UI-Menu), or select the **Dashboards** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4402552851095-Home-Page). The dashboard library displays.
3. On the left menu of the dashboard library, select **Import Dashboard**.
4. Browse to and select the `json` file for the dashboard, then select
   **Open**. The dashboard is imported.

When you import a dashboard, the data source connections and configurations used for the dashboard visuals are also imported.
