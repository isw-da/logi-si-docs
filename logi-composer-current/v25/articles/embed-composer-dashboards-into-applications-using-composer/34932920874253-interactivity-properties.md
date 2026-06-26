---
title: "Interactivity Properties"
id: 34932920874253
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932920874253-Interactivity-Properties
updated_at: 2026-05-26T22:09:47Z
---

# Interactivity Properties

# Interactivity Properties

You can add interactivity override settings to your embed script to provide granular control over what your users can do with an embedded Composer component. Properties can be passed with parameters in the [`interactivityOverrides` object](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932936668301-Embedded-Dashboard-Properties-and-Objects) of the [`createComponent` method](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932928903565-EmbedManager-Methods) when embedding Composer components.

The `interactivityProfileName` property must be specified before the interactivity overrides (`interactivityOverrides` object) can work. See [Embedded Dashboard Properties and Objects](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932936668301-Embedded-Dashboard-Properties-and-Objects).

The `interactivityOverrides` object includes several property settings: `visualSettings`, `InteractivityValue`and `editorUserSettings`.

* The parameters of the `settings` property affect the current embedded dashboard interactivity. See [Dashboard Interactivity Parameters (settings Property)](#Dashboar).
* The parameters of the `visualSettings` object property affect the current embedded visual interactivity. See [Visual Interactivity Parameters (visualSettings Property)](#Visual).
* The parameters of the `InteractivityValue` property define the source inventory dashboard. See [Sources Inventory Interactivity Parameters (InteractivityValue Property)](#Sources) .
* The parameters of the `editorUserSettings` property define the editor configuration dashboard. See [Editor Configuration (editorUserSettings Property)](#Editor).

The following example depicts the use and placement of dashboard and visual interactivity parameters.

<script>
src="<server>:8443/composer/embed/embed.js",
{
"type": "dashboard",
"dashboardId": "<dashboard-ID>",
"theme": "modern",
"interactivityProfileName": "interactive",
"interactivityOverrides": {
"settings":{
"CHANGE\_LAYOUT": true
},
"visualSettings":{
"FILTER": false
},
}
}
</script>

Custom user attributes can be used as variables in these property value settings. For example, the following property setting is valid and will insert the value of the `var2` custom user attribute in the property setting. If a `var2` custom user attribute is not found for a user, a value of `true` is assumed.

While it is possible to save a dashboard profile using custom user attributes, you cannot pass the dashboard profile with custom user attributes in the JavaScript.

"CHANGE\_LAYOUT": "${User.var2|true}"

## Dashboard Interactivity Parameters (`settings` Property)

Use the `settings` property to specify interactivity parameters for the dashboard. The default for all dashboard interactivity parameters is `true`.

| Parameter | Description |
| --- | --- |
| `"ADD_TO_FAVORITES": false` | When set to `true`, users can mark the dashboard as a favorite. When set to `false`, they cannot mark dashboard favorites and the [dashboard icon](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932842163469-Use-the-Dashboard-Icon-Bars) is not available in the UI.  Type: boolean |
| `"ADD_VISUALS": false` | When set to `true`, these options are accessible in the dashboard UI:   * Select the dashboard icon  to add existing visuals to the dashboard (**Add Existing Visual**). * Select **Add to Visual Gallery** from the  menu to replace local visuals with Visual Gallery visuals. See [Create and Add Visuals to the Visual Gallery](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933273224589-Create-and-Add-Visuals-to-the-Visual-Gallery).   When set to `false`, users cannot add existing visuals or replace visuals in the dashboard.  Type: boolean  **Note:**  If all menu item parameters are `false`, the dashboard icon is not shown in the UI. If any menu item parameters are `true`, the dashboard icon is shown in the UI, and includes any items set to `true`. |
| `"CHANGE_LAYOUT": true` | When set to `true`, users can resize or move visuals in the dashboard. When set to `false`, they cannot resize or move visuals in the dashboard.  Type: boolean |
| `"COMMENTS": true` | When set to `true`, users with appropriate permissions can access comments (read, write, edit their own, and delete comments, depending on their access level). When set to `false`, comments are not available in the UI.  Type: boolean |
| `"CREATE_FILTER_SNIPPETS": false` | When set to `true`, users can add new filter snippets () to the dashboard using the dashboard icons. When set to `false`, they cannot create new snippets to add to the dashboard.  Type: boolean  **Note:**  If all menu item parameters are `false`, the dashboard icon is not shown in the UI. If any menu item parameters are `true`, the dashboard icon is shown in the UI, and includes any items set to `true`. |
| `"CREATE_TEXT_SNIPPETS": false` | When set to `true`, users can add new text snippets () to the dashboard using the dashboard icons. When set to `false`, they cannot create new snippets to add to the dashboard.  Type: boolean  **Note:**  If all menu item parameters are `false`, the dashboard icon is not shown in the UI. If any menu item parameters are `true`, the dashboard icon is shown in the UI, and includes any items set to `true`. |
| `"CREATE_VISUALS": false` | When set to `true`, users with **Owner** and **Editor** access levels or the **Administer Visuals**[privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), these options are accessible in the dashboard UI:   * Select the dashboard icon  to add new local visuals to the dashboard (**Add New Visual**). * Select **Convert to Local** from the  menu to convert Visual Gallery visuals to local visuals. See [Convert Visual Gallery Visuals and Local Visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290437005-Convert-Visual-Gallery-Visuals-and-Local-Visuals).   When set to `false`, they cannot create new local visuals or convert Visual Gallery visuals in the dashboard.  Type: boolean  **Note:**  If all menu item parameters are `false`, the dashboard icon is not shown in the UI. If any menu item parameters are `true`, the dashboard icon is shown in the UI, and includes any items set to `true`. |
| `"DASHBOARD_ALERTS": false` | When set to `true`, users with appropriate [privileges](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) can create and edit dashboard alerts using the dashboard icon . When set to `false`,the dashboard icon is hidden and users cannot create or edit dashboard alerts. |
| `"DASHBOARD_INTERACTIONS": true` | When set to `true`, users can link fields between disparate data sources to create cross-source links. When set to `false`, they cannot create cross-source links and the [dashboard icon](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932842163469-Use-the-Dashboard-Icon-Bars) is not available in the UI. |
| `"DASHBOARD_LINKS": true` | When set to `true`, users can link dashboards. When set to `false`, they cannot link dashboards and the [dashboard icon](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932842163469-Use-the-Dashboard-Icon-Bars) is not available in the UI.  Type: boolean |
| `"DELETE": true` | When set to `true`, users can delete the dashboard. When set to `false`, they cannot delete the dashboard and the [dashboard icon](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932842163469-Use-the-Dashboard-Icon-Bars) is not available in the UI.  Type: boolean |
| `"EXPORT_CONFIGURATION": true` | When set to `true`, users can export the JSON configuration for the dashboard. When set to `false`, the [Export dialog](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932788789645-Export-Dashboards) in the UI no longer provides an option to export the configuration. If this setting and the `EXPORT_PNG_PDF` setting are both turned off, the [dashboard icon](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932842163469-Use-the-Dashboard-Icon-Bars) is not available in the UI.  Type: boolean |
| `"EXPORT_CSV": true` | When set to `true`, users can Export the dashboard as a CSV file. When set to `false`, they cannot export the dashboard as a CSV file and the [Export dialog](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932788789645-Export-Dashboards) in the UI no longer provides this export option. If all export settings and the `EXPORT_CONFIGURATION` setting are both turned off, the [dashboard icon](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932842163469-Use-the-Dashboard-Icon-Bars) is not available in the UI.  Type: boolean |
| `"EXPORT_PNG_PDF": true` | When set to `true`, users can Export the dashboard as a PNG or PDF file. When set to `false`, they cannot export the dashboard as a PNG or PDF file and the [Export dialog](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932788789645-Export-Dashboards) in the UI no longer provides this export option. If all export settings and the `EXPORT_CONFIGURATION` setting are both turned off, the [dashboard icon](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932842163469-Use-the-Dashboard-Icon-Bars) is not available in the UI.  Type: boolean |
| `"EXPORT_XLSX": true` | When set to `true`, users can Export the dashboard as an Excel (.xlsx) file. When set to `false`, they cannot export the dashboard as an Excel (.xlsx) file and the [Export dialog](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932788789645-Export-Dashboards) in the UI no longer provides this export option. If all export settings and the `EXPORT_CONFIGURATION` setting are both turned off, the [dashboard icon](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932842163469-Use-the-Dashboard-Icon-Bars) is not available in the UI.  Type: boolean |
| `"FILTER": true` | When set to `true`, users can apply filters to the dashboard. When set to `false`, they cannot apply dashboard filters and the [dashboard icon](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932842163469-Use-the-Dashboard-Icon-Bars) is not available in the UI.  Type: boolean |
| `"REFRESH": true` | When set to `true`, users can refresh the dashboard data. When set to `false`, they cannot refresh dashboard data and the [dashboard icon](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932842163469-Use-the-Dashboard-Icon-Bars) is not available in the UI.  Type: boolean |
| `"RENAME": true` | When set to `true`, users can rename the dashboard. When set to `false`, they cannot rename the dashboard.  Type: boolean |
| `"SAVE_AS": true` | When set to `true`, users can save the dashboard (make a copy) using a new name. When set to `false`, they cannot save the dashboard with a new name and the  [dashboard icon](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932842163469-Use-the-Dashboard-Icon-Bars) is not available in the UI.  Type: boolean |
| `"SAVE": true` | When set to `true`, users can save the dashboard. When set to `false`, they cannot save the dashboard and the  [dashboard icon](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932842163469-Use-the-Dashboard-Icon-Bars) is not available in the UI.  Type: boolean |
| `"SCHEDULE_REPORTS": true` | When set to `true`, users with appropriate [privileges](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) can schedule dashboard reports using the dashboard icon . When set to `false`, the dashboard icon is hidden and they cannot schedule dashboard reports.  Type: boolean |
| `"SHARE_DASHBOARD": true` | When set to `true`, users can share dashboards using the dashboard icon . When set to `false`, the dashboard icon is hidden and they cannot share dashboards.  Type: boolean |
| `"SHARE_FILTER_SETS": true` | When set to `true`, users can share saved filter sets with other users. When set to `false`, users cannot view or use filter sets for the dashboard.  Type: boolean |
| `"WIDGETS": true` | When set to `true`, users can share saved filter sets with other users. When set to `false`, users cannot view or use the widget settings sidebar menu.  Type: boolean |

## Visual Interactivity Parameters (`visualSettings` Property)

Use the `visualSettings` property to specify visual interactivity parameters for the embedded visuals. If the `overrideVisualInteractivity` property is set to `true` within these settings, the visual interactivity parameters will override any interactivity properties specified for the individual visuals.

The defaults for these parameters are determined by the interactivity profile.

* If the interactivity profile is `readonly`, then the `overrideVisualInteractivity` property is `true` and all `visualSettings` parameters are `false`. If the interactivity profile is `interactive`, then the `overrideVisualInteractivity` property is set to `false`, all `visualSettings` parameters are empty, and the visual interactivity settings for the individual visuals are used.
* When a custom interactivity profile is saved for a dashboard and `overrideVisualInteractivity` is set to `false`, then all `visualSettings` parameters are empty and the visual interactivity settings for the individual visuals are used. If `overrideVisualInteractivity` is set to `true`, then the `visualSettings` for the dashboard are used.

| Parameter | Description |
| --- | --- |
| `"ACTIONS": false` | When set to `true`, users can invoke an action using the **Actions** option from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). When set to `false`, they cannot invoke actions.  Type: boolean |
| `"ACTIONS_ACTION": false` | When set to `true`, users can invoke an action using the **Actions** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu). When set to `false`, they cannot invoke actions.  Type: boolean |
| `"COLORS": false` | When set to `true`, users can change the color palette used by the visual.  When set to `false`, they cannot change the color palette . The color settings () [visual sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) option is disabled and they cannot access the color sidebar.  Type: boolean |
| `"CONDITIONAL_FORMATTING": false` | When set to `true`, users define conditional formatting for the visual.  When set to `false`, they cannot define conditional formatting. The conditional formatting [visual sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) option is disabled and can't be accessed.  Type: boolean |
| `"COPY": false` | When set to `true`, users can copy a visual using the **Copy Visual** option from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). When set to `false`, they cannot copy visuals. Type: boolean |
| `"DETAILS_ACTION": false` | When set to `true`, users can display additional information about a specific visual data element using the **Details** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu). When set to `false`, users cannot display additional information about a specific visual data element using the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu).  Type: boolean |
| `"EXPORT_CSV": false` | When set to `true`, users can Export the visual as a CSV file. When set to `false`, they cannot export the visual this way, and the UI no longer provides this export option. If all export settings are turned off, the export menu is removed.  Type: boolean |
| `"EXPORT_PNG_PDF": false` | When set to `true`, users can Export the visual as a PNG or PDF file. When set to `false`, they cannot export the visual this way, and the UI no longer provides this export option. If all export settings are turned off, the export menu is removed.  Type: boolean |
| `"EXPORT_XLSX": false` | When set to `true`, users can Export the visual as an Excle (.xlsx) file. When set to `false`, they cannot export the visual this way, and the UI no longer provides this export option. If all export settings are turned off, the export menu is removed.  Type: boolean |
| `"FILTER": false` | When set to `true`, users can filter visual data using the **Filter** option from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu) and to the left of the visual name on a visual, or display name if viewed in a dashboard. When set to `false`, they cannot filter visual data.  Type: boolean |
| `"FILTER_ACTION": false` | When set to `true`, users can filter data using the **Filter** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu). When set to false, users cannot filter data using the **Filter** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu).  Type: boolean |
| `"FORMAT": false` | When set to `true`, users can [Format specific data](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933268999949-Format-Numeric-Table-Data-Using-the-Table-Context-Menu) in a visual. When set to `false`, they cannot format visual data.  Type: boolean |
| `"GROUPING": false` | When set to `true`, users can change the **Group** field on the x-axis of the visual. When set to `false`, they cannot change the **Group** field.  Type: boolean |
| `"INFO": false` | When set to `true`, users can see visual details in the Info sidebar menu. When set to `false`, they cannot see those details.  Type: boolean |
| `"KEYSET": false` | When set to `true`, users can create a keyset from the visual data using the **Create Keyset** option from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). When set to `false`, users cannot create keysets.  Type: boolean |
| `"KEYSET_ACTION": false` | When set to `true`, users can create a keyset from a selected data point using the **Keyset** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu). When set to `false`, users cannot create a keyset using the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu). |
| `"LINK_ACTION": false` | When set to `true`, users can link to another dashboard using the **Link** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu). When set to `false`, users cannot link to another dashboard using the **Link** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu).  Type: boolean |
| `"MAXIMIZE": false` | When set to `true`, users can maximize a visual for optimal viewing. When set to `false`, they cannot maximize a visual.  Type: boolean |
| `"METRICS": false` | When set to `true`, users can change metric fields (other than a metric that might be in the **Group** field) on the axes for the visual. This setting also controls whether a user can control the aggregation method (SUM, AVG, MIN, MAX, etc.) used for [metrics](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932886385037-Metrics) in a table. When set to `false`, users cannot change metric fields or control the aggregation method used for metrics on a visual.  Type: boolean |
| `"overrideVisualInteractivity": false` | When set to `true`, the individual visual interactivity settings for each visual on the dashboard are overridden and ignored. Instead, the visual interactivity settings set for the dashboard are used for all of the visuals in the dashboard. These settings are only applied to the visuals when they are used in this dashboard and not universally.  When set to `false`, the individual visual interactivity settings for each visual are honored.  Type: boolean |
| `"REMOVE": false` | When set to `true`, users can remove a visual using the **Remove Visual** option from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). When set to `false`, users cannot remove visuals.  Type: boolean |
| `"RENAME": false` | When set to `true`, users can change the display name of a visual. When set to `false`, they cannot change the display name of visual.  Type: boolean |
| `"RULERS": false` | When set to `true`, users can add visual reference lines and customize the markers used on the metric axis.  When set to `false`, users cannot add reference lines and markers. The ruler settings () [visual sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the ruler sidebar.  Type: boolean |
| `"SAVE_AS": false` | When set to `true`, users can save a shared visual (make a copy) using a new name. When set to `false`, they cannot save the shared visual with a new name and the option is not available in the UI.  Type: boolean |
| `"SAVE": false` | When set to `true`, users can save the shared visual. When set to `false`, they cannot save the shared visual and the option is not available in the UI.  Type: boolean |
| `"SETTINGS": false` | When set to `true`, users can specify settings for the visual using the visual settings option on the [visual sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu).  When set to `false`, users cannot specify visual settings. The visual settings () [visual sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) option is disabled and users cannot access the visual settings sidebar.  Type: boolean |
| `"SORT": false` | When set to `true`, users can sort and limit the data in a visual.  When set to `false`, users cannot sort and limit visual data. The sort and limit () [visual sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the Sort & Limit sidebar.  Type: boolean |
| `"TIMEBAR_FIELD": false` | When set to `true`, users can change the time field on the [time bar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933204115725-Use-the-Time-Bar). When set to `false`, users cannot change the time field.  Type: boolean |
| `"TIMEBAR_PANEL": false` | When set to `true`, users can show and hide the time bar on a visual. When set to `false`, the time bar is hidden for this visual.  Type: boolean |
| `"TREND_ACTION": false` | When set to `true`, users can view trends for a selected data point using the **Trend** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu). When set to `false`, users cannot view trends for a selected data point using the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu).  Type: boolean |
| `"VISUAL_STYLE": false` | When set to `true`, users can change the style of a visual.  When set to `false`, users cannot change the visual style. The visual style settings () [visual sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and users cannot access the visual type sidebar.  Type: boolean |
| `"ZOOM_ACTION": false` | When set to `true`, users can drill down in a selected data point on a visual using the **Zoom** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu). When set to `false`, users cannot drill down in a selected data point on a visual using the **Zoom** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu).  Type: boolean |

## Sources Inventory Interactivity Parameters (`InteractivityValue` Property)

Use the `InteractivityValue` property to specify interactivity parameters for the sources inventory.

| Parameter | Description |
| --- | --- |
| `"ADD_NEW": true` | When set to `true`, users can create a new data source configuration. When set to `false`, the button to create a new data source is hidden.  Type: boolean |
| `"FILTER": true` | When set to `true`, users can filter sources using the quick filter icons to the left of the **Search** field on the sources page. When set to `false`, they cannot filter sources.  Type: boolean |
| `"DELETE": true` | When set to `true`, users can delete data source configurations not currently in use by a visual.  When set to `false`, they cannot delete data source configurations, and the delete icon is not visible in the UI.  Type: boolean |
| `"DESCRIPTION": true` | When set to `true`, users can view and search for items (sources, visual gallery visuals, dashboard in the library) by the contents of an item's description.  When set to `false`, description options are not available to users.  Type: boolean |
| `"EXPORT": true` | When set to `true`, users can export data source configurations.  When set to `false`, users cannot export data source configurations, and the option is not visible in the UI.  Type: boolean |
| `"PERMISSIONS": false` | When set to `true`, users can manage user and group permissions for data sources. When set to `false`, they cannot manage permissions for data sources, and the related icons are not visible in the UI.  Type: boolean |
| `"FAVORITES": true` | When set to `true`, users can mark the data source as a favorite. When set to `false`, they cannot mark data source favorites and the favorites icons are not visible in the UI.  Type: boolean |
| `"ROW_SECURITY": false` | When set to `true`, users can define row security for data sources. When set to `false`, they cannot define row security for data sources, and the related icons are not visible in the UI.  Type: boolean |
| `"COLUMN_SECURITY": false` | When set to `true`, users can define column security for data sources. When set to `false`, they cannot define column security for data sources, and the related icons are not visible in the UI.  Type: boolean |
| `"CLEAR_CACHE": true` | When set to `true`, users can clear the cache for a data source. When set to `false`, users cannot clear the cache for a data source and the related icons are not visible in the UI.  Type: boolean |
| `"AVAILABLE_VISUAL_TYPES": true` | When set to `true`, users invoke the **Available Visual Types** work area to enable and disable available visual types for a source. When set to `false`, they cannot affect available visual types, or see related icons are not visible in the UI.  Type: boolean |

## Editor Configuration (`editorUserSettings` Property)

Use the `editorUserSettings` property to configure the interactivity parameters for the dashboard.

{
"type": "dashboard",
editorUserSettings: {
isViewMode: true,
canSwitchMode: false,
allowInteractivityConfiguration: false,
}
}

| Parameter | Description |
| --- | --- |
| `isViewMode` | When set to `true`, the dashboard opens for editors and creators in View mode. When set to `false`, the dashboard opens for editors and creators in Edit mode.  Type: boolean  Default: `false` |
| `canSwitchMode` | When set to `true`, editors can toggle between View and Edit modes. When set to `false`, editors can't toggle between View and Edit modes.  Type: boolean  Default: `true` |
| `allowInteractivityConfiguration` | When set to `true`, editors can change interactivity settings for the dashboard and visuals. When set to `false`, editors can't change interactivity settings for the dashboard and visuals.  Type: boolean  Default: `false` |
