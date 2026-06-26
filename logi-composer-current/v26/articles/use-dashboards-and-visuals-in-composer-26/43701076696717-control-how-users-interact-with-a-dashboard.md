---
title: "Control How Users Interact With a  Dashboard"
id: 43701076696717
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076696717-Control-How-Users-Interact-With-a-Dashboard
updated_at: 2026-05-29T14:11:18Z
---

# Control How Users Interact With a  Dashboard

# Control How Users Interact With a Dashboard

You can control how users can interact with a dashboard. Control their ability to:

* Resize or move visuals in a dashboard
* Add visuals, text snippets, and filter snippets to a dashboard
* Refresh, save or delete a dashboard
* Filter a dashboard
* Rename a dashboard
* Mark the dashboard as a favorite
* Link a dashboard or set up cross-source links in the dashboard
* Export a dashboard

You can also apply a global set of visual interactivity settings to all of the visuals on the dashboard that overrides the interactivity settings for the individual visuals on the dashboard.

**Important:** 
User attributes are not resolved when previewing interactivity settings, and default fallbacks will be used in the Preview mode.

**Control user interactions with a dashboard and its visuals**

1. Select the visual on the dashboard or in the Visual Gallery.
2. Select the interactivity option button to the left of the dashboard title.

   ![select the interactivity icon to adjust dashboard interactivty settings](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242683067149 "The dashboard interactivity icon")

   The dashboard interactivity panel appears.

   ![Adjust interactivity settings for a dashboard and its visuals here](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242678151949 "Dashboard Interactivity settings work area")

   By default, all interactivity settings are activated (enabled) for a dashboard. Each setting is controlled by a toggle switch. Slide the switch to the right to turn an interactivity setting on; slide them to the left to turn a setting off.

   There are two tabs on the dashboard interactivity panel: **Dashboard** and **Visuals**. The settings on each tab are described at the end of these instructions.

   In addition, you can use the **Preview Interactivity Settings** option to test the dashboard and visual interactivity settings. When this switch is turned on, the dashboard and visuals behave as they will when the dashboard is embedded, based on the interactivity settings for the dashboard and its visuals. The **Preview Interactivity Settings** switch is a temporary switch: by default it is off each time you access the dashboard. It is not saved with the dashboard; so if you turn it on and save the dashboard, it will still be off the next time you edit the dashboard.
3. Slide the switch on or off for the interactivity settings you want to change on the **Dashboard** tab. See [Dashboard Interactivity Settings (Dashboard Tab)](#Dashboar).
4. Slide the switch on or off for the interactivity settings you want to change on the **Visuals** tab. See [Visual Interactivity Settings (Visuals Tab)](#Visual).
5. Select **Save** to save the interactivity settings.
6. Optionally, preview the behavior with the interactivity settings applied. Slide the **Preview Interactivity Settings** switch on (to the right).

   **Note:** 
   Custom attributes are not evaluated in Preview mode. If custom attributes are used, Composer uses defaults to preview the interactivity settings. Customer attributes will be applied correctly in an embedded workflow.
7. [Save](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047225613-Save-a-Dashboard) the dashboard. When you save a dashboard (Save option), the dashboard interactivity settings are also saved (if there are any). If there are no dashboard interactivity settings or if they have not been changed, they are not saved. When you save a dashboard with a new name (Save As option), the dashboard interactivity settings are saved to the new dashboard, but the interactivity settings for the original dashboard remain unchanged.

## Dashboard Interactivity Settings (Dashboard Tab)

Each dashboard interactivity setting is described in the following table.

| Dashboard Feature Group | Setting | Controls the ability to... |
| --- | --- | --- |
| **Editing** | Change Layout | Resize or move visuals and rich text snippet widgets in the dashboard. |
| Add Existing Visuals | Add existing visuals to the dashboard. |
| Add New Visuals | Add new visuals to the dashboard. |
| Add Text Snippets | Add text snippets to the dashboard. |
| Add Filter Snippets | Add filter snippets to the dashboard. |
| Delete | Delete the dashboard. When this setting is turned off, the  [dashboard icon](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047597837-Use-the-Dashboard-Icon-Bars) is not available. |
| Save | Save the dashboard. When this setting is turned off, the  [dashboard icon](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047597837-Use-the-Dashboard-Icon-Bars) is not available. |
| Save As | Save the dashboard and unsaved changes as a dashboard using a different name. When this setting is turned off, the  [dashboard icon](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047597837-Use-the-Dashboard-Icon-Bars) is not available. |
| Filter | Apply filters to the dashboard. When this setting is turned off, the [dashboard icon](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047597837-Use-the-Dashboard-Icon-Bars) is not available. You can still apply filters to the visuals, however. |
| Rename | Rename the dashboard. |
| Change Description | Allow users to change the description on the Info sidebar menu if one exists. |
| Add to Favorites | Mark the dashboard as a favorite. When this setting is turned off, the  [dashboard icon](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047597837-Use-the-Dashboard-Icon-Bars) is not available. |
| Share Filter Sets | Share saved filter sets with other users. When this setting is turned off, other users cannot view or use the filter sets for the dashboard. |
| Schedule Reports | Schedule reports for the dashboard. |
| Share Dashboard | Share the dashboard with specific users. |
| Comments | Allow users with Commenter access or higher to create, view, and manage their own comments. See [Manage Widget Comments](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215559693-Manage-Widget-Comments). |
| **Data** | Set Up Dashboard Link | Link dashboards. When this setting is turned off, the  [dashboard icon](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047597837-Use-the-Dashboard-Icon-Bars) is not available. |
| Refresh | Refresh the dashboard data. When this setting is turned off, the  [dashboard icon](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047597837-Use-the-Dashboard-Icon-Bars) is not available. |
| Change Dashboard Interactions | Link fields between disparate data sources to create cross-source links. When this setting is turned off, the  [dashboard icon](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047597837-Use-the-Dashboard-Icon-Bars) is not available. |
| Set Up Dashboard Alerts | Define alerts for the dashboard. |
| **Exporting** | Export to PNG/PDF | Export the dashboard as a PNG or PDF file. When this setting is turned off, the [Export dialog](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076601229-Export-Dashboards) no longer provides an option to export an image. If all settings for **Exporting** are turned off, the  [dashboard icon](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047597837-Use-the-Dashboard-Icon-Bars) is not available. |
| Export Configuration | Export the JSON configuration for the dashboard. When this setting is turned off, the [Export dialog](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076601229-Export-Dashboards) no longer provides an option to export the configuration. If all settings for **Exporting** are turned off, the  [dashboard icon](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047597837-Use-the-Dashboard-Icon-Bars) is not available. |
| Export Data | Export the dashboard in Excel (XLSX) format as raw data or visual data. When this setting is turned off, the [Export dialog](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076601229-Export-Dashboards) no longer provides an option to export the dashboard in this format. If all settings for **Exporting** are turned off, the  [dashboard icon](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047597837-Use-the-Dashboard-Icon-Bars) is not available. |

## Visual Interactivity Settings (Visuals Tab)

The Visuals tab allows you to override the interactivity settings for the individual visuals in the dashboard. When the **Override Visual Interactivity** switch is turned on, the individual visual interactivity settings for each visual on the dashboard are overridden and ignored and the visual interactivity settings set for the dashboard are used for all of the visuals in the dashboard.

These settings are only applied to the visuals while they are used in this dashboard and not universally. The interactivity settings for the visuals themselves are not affected when used elsewhere. In other words, if a visual is used in one dashboard (Dashboard A) with **Override Visual Interactivity** turned on and is also used in a second dashboard (Dashboard B) with **Override Visual Interactivity** turned off, the individual visual interactivity settings are not honored in Dashboard A, but are honored in Dashboard B.

Each visual interactivity setting is described in the following table.

| Visual Feature Group | UI Setting | JavaScript Setting | Controls the ability to... |
| --- | --- | --- | --- |
| **Data Interactivity** | Metrics | `METRICS` | Change metric fields (other than a metric that might be in the **Group** field) on the axes for the visual. This setting also controls whether a user can control the aggregation method (SUM, AVG, MIN, MAX, etc.) used for [metrics](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701100683021-Metrics) in a table. |
| Group | `GROUPING` | Change the **Group** field on the x-axis of the visual. This setting also controls whether a user can group tables. |
| Filter | `FILTER` | Filter data using the **Filter** option from the [visual drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu) and to the left of the visual name on a visual, or a display name if viewed in a dashboard. (To fully remove filtering functionality for a visual, be sure to turn off the **Filter** switch in the Context Menu settings on the interactivity sidebar too.) |
| Sort | `SORT` | Sort and limit the data in a visual. The sort and limit () [visual sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the Sort & Limit sidebar. |
| Format | `FORMAT` | [Format specific data](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701213266061-Format-Numeric-Table-Data-Using-the-Table-Context-Menu) in a visual. These formatting options are disabled when the switch is off. |
| **Context Menu** | Zoom | `ZOOM_ACTION` | Zoom into a selected data point on a visual using the **Zoom** option on the [context menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701212059021-Use-the-Context-Menu). |
| Filter | `FILTER_ACTION` | Filter data using the **Filter** option on the [context menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701212059021-Use-the-Context-Menu). (To fully remove filtering functionality for a visual, be sure to turn off the **Filter** switch in the Data Interactivity settings on the interactivity sidebar too.) |
| Details | `DETAILS_ACTION` | Display additional information about a specific visual data element using the **Details** option on the [context menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701212059021-Use-the-Context-Menu). |
| Trend | `TREND_ACTION` | View trends for a selected data point using the **Trend** option on the [context menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701212059021-Use-the-Context-Menu). |
| Keyset | `KEYSET_ACTION` | Create a keyset from a selected data point using the **Keyset** option on the [context menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701212059021-Use-the-Context-Menu). (To fully remove keyset functionality for a visual, be sure to turn off the **Create Keyset** switch in the Visualization settings on the interactivity sidebar too.) |
| Actions | `ACTIONS_ACTION` | Invoke an action using the **Actions** option on the [context menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701212059021-Use-the-Context-Menu). (To fully remove actions functionality for a visual, be sure to turn off the **Actions** switch in the Visualization settings on the interactivity sidebar too.) |
| Link | `LINK_ACTION` | Link to another dashboard using the **Link** option on the [context menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701212059021-Use-the-Context-Menu). |
| **Visualization** | Settings | `SETTINGS` | Specify settings for the visual. The visual settings () [visual sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the visual settings sidebar. |
| Rulers | `RULERS` | Add visual reference lines and customize the markers used on the metric axis. The ruler settings () [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the ruler sidebar. |
| Colors | `COLORS` | Change the color palette used by the visual. The color settings () [visual sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the color sidebar. |
| Conditional Formatting | `CONDITIONAL_FORMATTING` | Apply conditional formatting to data in the visual. The conditional formatting () [visual sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) option is disabled when disabled. |
| Create Keyset | `KEYSET` | Create a keyset from the visual data using the **Create Keyset** option from the [visual drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu). (To fully remove keyset functionality for a visual, be sure to turn off the **Keyset** switch in the Context Menu settings on the interactivity sidebar too.) |
| Save | `SAVE` | Save the visual. |
| Save As | `SAVE_AS` | Save the visual using a new name. |
| Copy | `COPY` | Copy a visual using the **Copy Visual** option from the [visual drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu). |
| Actions | `ACTIONS` | Invoke an action using the **Actions** option from the [visual drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu). (To fully remove actions functionality for a visual, be sure to turn off the **Actions** switch in the Context Menu settings on the interactivity sidebar too.) |
| Remove | `REMOVE` | Remove a visual using the **Remove Visual** option from the [visual drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu). |
| Visual Style | `VISUAL_STYLE` | Change the style of a visual. The visual style settings () [visual sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the visual type sidebar. |
| Select Time Bar Field | `TIMEBAR_FIELD` | Change the time field on the [time bar](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210703629-Use-the-Time-Bar). |
| Maximize | `MAXIMIZE` | Maximize a visual for optimal viewing. |
| Rename | `RENAME` | Rename a visual. |
| Show Time Bar Panel | `TIMEBAR_PANEL` | Show the [time bar](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210703629-Use-the-Time-Bar) for the visual. |
| Info | `INFO` | Allow users to edit information in the Info sidebar menu. |
| **Exporting** | Export to PNG/PDF | `EXPORT_PNG_PDF` | Export a visual to PNG/PDF using the **Export** option from the [visual drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu). |
| Export to CSV | `EXPORT_CSV` | Export a visual to a CSV file using the **Export** option from the [visual drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu). |
| Export to XLSX | `EXPORT_XLSX` | Export a visual to an XLSX file using the **Export** option from the [visual drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu). |
