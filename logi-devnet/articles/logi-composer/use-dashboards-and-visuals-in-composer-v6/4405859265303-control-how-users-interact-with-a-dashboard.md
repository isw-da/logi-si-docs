---
title: "Control How Users Interact With a Dashboard"
id: 4405859265303
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859265303-Control-How-Users-Interact-With-a-Dashboard
updated_at: 2022-08-25T13:55:43Z
---

# Control How Users Interact With a Dashboard

# Control How Users Interact With a Dashboard

You can control how users can interact with a dashboard. You can control their ability to:

* Resize or move visuals in a dashboard
* Add visuals to a dashboard
* Refresh, save or delete a dashboard
* Filter a dashboard
* Rename a dashboard
* Mark the dashboard as a favorite
* Link a dashboard or set up cross-source links in the dashboard
* Export a dashboard

You can also apply a global set of visual interactivity settings to all of the visuals on the dashboard that overrides the interactivity settings for the individual visuals on the dashboard.

Dashboard interactivity settings are useful in embedded use cases where the analytic on the parent application page needs to behave in a consistent manner with the rest of the application. These controls are managed on the interactivity panel for the dashboard.

To control user interactions with a dashboard and its visuals:

1. Select the visual on the dashboard or in the Visual Gallery.
2. Select the interactivity option (![](https://devnet.logianalytics.com/hc/article_attachments/4406743714071/sidebar-interactive.png)) to the left of the dashboard title.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747440535/dash-interactive-icon_768x83.png)

   The dashboard interactivity panel appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747440791/dash-interactivity_384x673.png)

   By default, all interactivity settings are activated (on) for a dashboard. Each setting is controlled by a toggle switch. Slide the switch to the right to turn an interactivity setting on; slide them to the left to turn a setting off.

   There are two tabs on the dashboard interactivity panel: **Dashboard** and **Visuals**. The settings on each tab are described at the end of these instructions.

   In addition, you can use the **Preview Interactivity Settings** option to test the dashboard and visual interactivity settings. When this switch is turned on, the dashboard and visuals behave as they will when the dashboard is embedded, based on the interactivity settings for the dashboard and its visuals. The **Preview Interactivity Settings** switch is a temporary switch: by default it is off each time you access the dashboard. It is not saved with the dashboard; so if you turn it on and save the dashboard, it will still be off the next time you edit the dashboard.
3. Slide the switch on or off for the interactivity settings you want to change on the **Dashboard** tab. See [*Dashboard Interactivity Settings (Dashboard Tab)*](#Dashboar).
4. Slide the switch on or off for the interactivity settings you want to change on the **Visuals** tab. See [*Visual Interactivity Settings (Visuals Tab)*](#Visual).
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743715607/save-blue2-btn.png) to save the interactivity settings.
6. Optionally, preview the behavior with the interactivity settings applied. Slide the **Preview Interactivity Settings** switch on (to the right).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Custom attributes are not evaluated in Preview mode. If custom attributes are used, Composer uses defaults to preview the interactivity settings. Customer attributes will be applied correctly in an embedded workflow.
7. [Save](https://devnet.logianalytics.com/hc/en-us/articles/4405850986647-Save-a-Dashboard) the dashboard. When you save a dashboard (Save option), the dashboard interactivity settings are also saved (if there are any). If there are no dashboard interactivity settings or if they have not been changed, they are not saved. When you save a dashboard with a new name (Save As option), the dashboard interactivity settings are saved to the new dashboard, but the interactivity settings for the original dashboard remain unchanged.

## Dashboard Interactivity Settings (Dashboard Tab)

Each dashboard interactivity setting is described in the following table.

| Dashboard Feature Group | Setting | Controls the ability to... |
| --- | --- | --- |
| **Editing** | Change Layout | Resize or move visuals in the dashboard. |
| Add Visuals | Add visuals to the dashboard. When this setting is turned off, the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available. |
| Delete | Delete the dashboard. When this setting is turned off, the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available. |
| Save | Save the dashboard. When this setting is turned off, the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available. |
| Filter | Apply filters to the dashboard. When this setting is turned off, the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available. You can still apply filters to the visuals, however. |
| Rename | Rename the dashboard. |
| Add to Favorites | Mark the dashboard as a favorite. When this setting is turned off, the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available. |
| Share Filter Sets | Share saved filter sets with other users. When this setting is turned off, other users cannot view or use the filter sets for the dashboard. |
| **Data** | Set Up Dashboard Links | Link dashboards. When this setting is turned off, the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available. |
| Refresh | Refresh the dashboard data. When this setting is turned off, the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available. |
| Change Dashboard Interactions | Link fields between disparate data sources to create cross-source links. When this setting is turned off, the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available. |
| **Exporting** | Export to PNG/PDF | Export the dashboard as a PNG or PDF file. When this setting is turned off, the [Export dialog](https://devnet.logianalytics.com/hc/en-us/articles/4405850982935-Export-a-Dashboard) no longer provides an option to export an image. If this setting and the **Export Configuration** setting are both turned off, the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available. |
| Export Configuration | Export the JSON configuration for the dashboard. When this setting is turned off, the [Export dialog](https://devnet.logianalytics.com/hc/en-us/articles/4405850982935-Export-a-Dashboard) no longer provides an option to export the configuration. If this setting and the **Export to PNG/PDF** setting are both turned off, the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available. |

## Visual Interactivity Settings (Visuals Tab)

The Visuals tab allows you to override the interactivity settings for the individual visuals in the dashboard. When the **Override Visual Interactivity** switch is turned on, the individual visual interactivity settings for each visual on the dashboard are overridden and ignored and the visual interactivity settings set for the dashboard are used for all of the visuals in the dashboard.

These settings are only applied to the visuals while they are used in this dashboard and not universally. The interactivity settings for the visuals themselves are not affected when used elsewhere. In other words, if a visual is used in one dashboard (Dashboard A) with **Override Visual Interactivity** turned on and is also used in a second dashboard (Dashboard B) with **Override Visual Interactivity** turned off, the individual visual interactivity settings are not honored in Dashboard A, but are honored in Dashboard B.

Each visual interactivity setting is described in the following table.

| Visual Feature Group | UI Setting | JavaScript Setting | Controls the ability to... |
| --- | --- | --- | --- |
| **Data Interactivity** | Metrics | `METRICS` | Change metric fields (other than a metric that might be in the **Group** field) on the axes for the visual. This setting also controls whether a user can control the aggregation method (SUM, AVG, MIN, MAX, etc.) used for [metrics](https://devnet.logianalytics.com/hc/en-us/articles/4405859309975-Metrics) in a table. |
| Group | `GROUPING` | Change the **Group** field on the x-axis of the visual. This setting also controls whether a user can group tables. |
| Filter | `FILTER` | Filter data using the **Filter** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) and to the left of the visual title. (To fully remove filtering functionality for a visual, be sure to turn off the **Filter** switch in the Radial Menu settings on the interactivity sidebar too.) |
| Sort | `SORT` | Sort and limit the data in a visual. The sort and limit () [visual sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the Sort & Limit sidebar. |
| **Radial Menu** | Zoom | `ZOOM_ACTION` | Zoom into a selected data point on a visual using the **Zoom** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). |
| Filter | `FILTER_ACTION` | Filter data using the **Filter** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). (To fully remove filtering functionality for a visual, be sure to turn off the **Filter** switch in the Data Interactivity settings on the interactivity sidebar too.) |
| Details | `DETAILS_ACTION` | Display additional information about a specific visual data element using the **Details** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). |
| Trend | `TREND_ACTION` | View trends for a selected data point using the **Trend** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). |
| Keyset | `KEYSET_ACTION` | Create a keyset from a selected data point using the **Keyset** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). (To fully remove keyset functionality for a visual, be sure to turn off the **Create Keyset** switch in the Visualization settings on the interactivity sidebar too.) |
| Actions | `ACTIONS_ACTION` | Invoke an action using the **Actions** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). (To fully remove actions functionality for a visual, be sure to turn off the **Actions** switch in the Visualization settings on the interactivity sidebar too.) |
| Link | `LINK_ACTION` | Link to another dashboard using the **Link** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). |
| **Visualization** | Settings | `SETTINGS` | Specify settings for the visual. The visual settings () [visual sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the visual settings sidebar. |
| Rulers | `RULERS` | Add visual reference lines and customize the markers used on the metric axis. The ruler settings () [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the ruler sidebar. |
| Colors | `COLORS` | Change the color palette used by the visual. The color settings () [visual sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the color sidebar. |
| Create Keyset | `KEYSET` | Create a keyset from the visual data using the **Create Keyset** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). (To fully remove keyset functionality for a visual, be sure to turn off the **Keyset** switch in the Radial Menu settings on the interactivity sidebar too.) |
| Copy | `COPY` | Copy a visual using the **Copy Visual** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). |
| Export | `EXPORT` | Export a visual using the **Export** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). |
| Actions | `ACTIONS` | Invoke an action using the **Actions** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). (To fully remove actions functionality for a visual, be sure to turn off the **Actions** switch in the Radial Menu settings on the interactivity sidebar too.) |
| Remove | `REMOVE` | Remove a visual using the **Remove Visual** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). |
| Visual Style | `VISUAL_STYLE` | Change the style of a visual. The visual style settings () [visual sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the visual type sidebar. |
| Select Time Bar Field | `TIMEBAR_FIELD` | Change the time field on the [time bar](https://devnet.logianalytics.com/hc/en-us/articles/4405851196695-Use-the-Time-Bar). |
| Maximize | `MAXIMIZE` | Maximize a visual for optimal viewing. |
| Rename | `RENAME` | Rename a visual. |
| Show Time Bar Panel | `TIMEBAR_PANEL` | Show the [time bar](https://devnet.logianalytics.com/hc/en-us/articles/4405851196695-Use-the-Time-Bar) for the visual. |
