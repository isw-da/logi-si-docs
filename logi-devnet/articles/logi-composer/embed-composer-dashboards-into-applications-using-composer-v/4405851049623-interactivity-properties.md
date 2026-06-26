---
title: "Interactivity Properties"
id: 4405851049623
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851049623-Interactivity-Properties
updated_at: 2021-09-21T01:28:29Z
---

# Interactivity Properties

# Interactivity Properties

You can add interactivity override settings to your embed script to provide granular control over what your users can do with an embedded Composer component. Properties can be passed with parameters in the [`interactivityOverrides` object](https://devnet.logianalytics.com/hc/en-us/articles/4405851050647-Supported-Embedded-Dashboard-Properties-and-Objects) of the [`createComponent` method](https://devnet.logianalytics.com/hc/en-us/articles/4405859341847-Supported-EmbedManager-Methods) when embedding Composer components.

The `interactivityProfileName` property must be specified before the interactivity overrides (`interactivityOverrides` object) can work. See [*Embedded Dashboard Properties and Objects*](https://devnet.logianalytics.com/hc/en-us/articles/4405851050647-Supported-Embedded-Dashboard-Properties-and-Objects).

The `interactivityOverrides` object includes two properties, `settings` and `visualSettings`.

* The parameters of the `settings` property affect the current embedded dashboard interactivity. See [*Dashboard Interactivity Parameters (settings Property)*](#Dashboar).
* The parameters of the `visualSettings` object property affect the current embedded visual interactivity. See [*Visual Interactivity Properties (visualSettings Property)*](#Visual).

The following example depicts the use and placement of dashboard and visual interactivity parameters.

```
<script>
   src="<server>:8443/composer/embed/embed.js",
     {
        "type": "dashboard",
        "dashboardId": "<dashboard-ID>",
        "theme": "modern",
        "interactivityProfileName": "interactive",
        "interactivityOverrides": {
          "settings":{
             "CHANGE_LAYOUT": true
          },
          "visualSettings":{
             "FILTER": false
          },
        } 
     }
</script>
```

Custom user attributes can be used as variables in these property value settings. For example, the following property setting is valid and will insert the value of the `var2` custom user attribute in the property setting. If a `var2` custom user attribute is not found for a user, a value of `true` is assumed.

While it is possible to save a dashboard profile using custom user attributes, you cannot pass the dashboard profile with custom user attributes in the JavaScript.

```
"CHANGE_LAYOUT": "${User.var2|true}"
```

## Dashboard Interactivity Parameters (`settings` Property)

Use the `settings` property to specify interactivity parameters for the dashboard. The default for all dashboard interactivity parameters is `true`.

| Parameter | Description |
| --- | --- |
| `"ADD_TO_FAVORITES": false` | When set to `true`, users can mark the dashboard as a favorite. When set to `false`, they cannot mark dashboard favorites and the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available in the UI.  Type: boolean |
| `"ADD_VISUALS": false` | When set to `true`, users can add visuals to the dashboard. When set to `false`, they cannot add visuals to the dashboard and the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available in the UI.  Type: boolean |
| `"CHANGE_LAYOUT": true` | When set to `true`, users can resize or move visuals in the dashboard. When set to `false`, they cannot resize or move visuals in the dashboard.  Type: boolean |
| `"DASHBOARD_INTERACTIONS": true` | When set to `true`, users can link fields between disparate data sources to create cross-source links. When set to `false`, they cannot create cross-source links and the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available in the UI. |
| `"DASHBOARD_LINKS": true` | When set to `true`, users can link dashboards. When set to `false`, they cannot link dashboards and the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available in the UI.  Type: boolean |
| `"DELETE": true` | When set to `true`, users can delete the dashboard. When set to `false`, they cannot delete the dashboard and the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available in the UI.  Type: boolean |
| `"EXPORT_CONFIGURATION": true` | When set to `true`, users can export the JSON configuration for the dashboard. When set to `false`, the [Export dialog](https://devnet.logianalytics.com/hc/en-us/articles/4405850982935-Export-a-Dashboard) in the UI no longer provides an option to export the configuration. If this setting and the `EXPORT_PNG_PDF` setting are both turned off, the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available in the UI.  Type: boolean |
| `"EXPORT_PNG_PDF": true` | When set to `true`, users can Export the dashboard as a PNG or PDF file. When set to `false`, they cannot export the dashboard as a PNG or PDF file and the [Export dialog](https://devnet.logianalytics.com/hc/en-us/articles/4405850982935-Export-a-Dashboard) in the UI no longer provides an option to export an image. If this setting and the `EXPORT_CONFIGURATION` setting are both turned off, the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available in the UI.  Type: boolean |
| `"FILTER": true` | When set to `true`, users can apply filters to the dashboard. When set to `false`, they cannot apply dashboard filters and the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available in the UI.  Type: boolean |
| `"REFRESH": true` | When set to `true`, users can refresh the dashboard data. When set to `false`, they cannot refresh dashboard data and the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available in the UI.  Type: boolean |
| `"RENAME": true` | When set to `true`, users can rename the dashboard. When set to `false`, they cannot rename the dashboard.  Type: boolean |
| `"SAVE": true` | When set to `true`, users can save the dashboard. When set to `false`, they cannot save the dashboard and the [dashboard icon](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) is not available in the UI.  Type: boolean |

## Visual Interactivity Properties (`visualSettings` Property)

Use the `visualSettings` property to specify visual interactivity parameters for the embedded visuals. If the `overrideVisualInteractivity` property is set to `true` within these settings, the visual interactivity parameters will override any interactivity properties specified for the individual visuals.

The defaults for these parameters are determined by the interactivity profile.

* If the interactivity profile is `readonly`, then the `overrideVisualInteractivity` property is `true` and all `visualSettings` parameters are `false`. If the interactivity profile is `interactive`, then the `overrideVisualInteractivity` property is set to `false`, all `visualSettings` parameters are empty, and the visual interactivity settings for the individual visuals are used.
* When a custom interactivity profile is saved for a dashboard and `overrideVisualInteractivity` is set to `false`, then all `visualSettings` parameters are empty and the visual interactivity settings for the individual visuals are used. If `overrideVisualInteractivity` is set to `true`, then the `visualSettings` for the dashboard are used.

| Parameter | Description |
| --- | --- |
| `"ACTIONS": false` | When set to `true`, users can invoke an action using the **Actions** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). When set to `false`, they cannot invoke actions.  Type: boolean |
| `"ACTIONS_ACTION": false` | When set to `true`, users can invoke an action using the **Actions** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). When set to `false`, they cannot invoke actions.  Type: boolean |
| `"COLORS": false` | When set to `true`, users can change the color palette used by the visual.  When set to `false`, they cannot change the color palette . The color settings () [visual sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) option is disabled and they cannot access the color sidebar.  Type: boolean |
| `"COPY": false` | When set to `true`, users can copy a visual using the **Copy Visual** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). When set to `false`, they cannot copy visuals. Type: boolean |
| `"DETAILS_ACTION": false` | When set to `true`, users can display additional information about a specific visual data element using the **Details** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). When set to `false`, users cannot display additional information about a specific visual data element using the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). Type: boolean |
| `"EXPORT": false` | When set to `true`, users can export a visual using the **Export** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). When set to `false`, they cannot export visuals. Type: boolean |
| `"FILTER": false` | When set to `true`, users can filter visual data using the **Filter** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) and to the left of the visual title. When set to `false`, they cannot filter visual data. Type: boolean |
| `"FILTER_ACTION": false` | When set to `true`, users can filter data using the **Filter** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). When set to false, users cannot filter data using the **Filter** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu).  Type: boolean |
| `"GROUPING": false` | When set to `true`, users can change the **Group** field on the x-axis of the visual. When set to `false`, they cannot change the **Group** field. Type: boolean |
| `"KEYSET": false` | When set to `true`, users can create a keyset from the visual data using the **Create Keyset** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). When set to `false`, users cannot create keysets.  Type: boolean |
| `"KEYSET_ACTION": false` | When set to `true`, users can create a keyset from a selected data point using the **Keyset** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). When set to `false`, users cannot create a keyset using the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). |
| `"LINK_ACTION": false` | When set to `true`, users can link to another dashboard using the **Link** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). When set to `false`, users cannot link to another dashboard using the **Link** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). Type: boolean |
| `"METRICS": false` | When set to `true`, users can change metric fields (other than a metric that might be in the **Group** field) on the axes for the visual. This setting also controls whether a user can control the aggregation method (SUM, AVG, MIN, MAX, etc.) used for [metrics](https://devnet.logianalytics.com/hc/en-us/articles/4405859309975-Metrics) in a table. When set to `false`, users cannot change metric fields or control the aggregation method used for metrics on a visual. Type: boolean |
| `"overrideVisualInteractivity": false` | When set to `true`, the individual visual interactivity settings for each visual on the dashboard are overridden and ignored. Instead, the visual interactivity settings set for the dashboard are used for all of the visuals in the dashboard. These settings are only applied to the visuals when they are used in this dashboard and not universally.  When set to `false`, the individual visual interactivity settings for each visual are honored.  Type: boolean |
| `"REMOVE": false` | When set to `true`, users can remove a visual using the **Remove Visual** option from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). When set to `false`, users cannot remove visuals. Type: boolean |
| `"RULERS": false` | When set to `true`, users can add visual reference lines and customize the markers used on the metric axis.  When set to `false`, users cannot add reference lines and markers. The ruler settings () [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the ruler sidebar.  Type: boolean |
| `"SETTINGS": false` | When set to `true`, users can specify settings for the visual using the visual settings option on the [visual sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu).  When set to `false`, users cannot specify visual settings. The visual settings () [visual sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) option is disabled and users cannot access the visual settings sidebar.  Type: boolean |
| `"SORT": false` | When set to `true`, users can sort and limit the data in a visual.  When set to `false`, users cannot sort and limit visual data. The sort and limit () [visual sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and you cannot access the Sort & Limit sidebar.  Type: boolean |
| `"TIMEBAR_FIELD": false` | When set to `true`, users can change the time field on the [time bar](https://devnet.logianalytics.com/hc/en-us/articles/4405851196695-Use-the-Time-Bar). When set to `false`, users cannot change the time field.  Type: boolean |
| `"TREND_ACTION": false` | When set to `true`, users can view trends for a selected data point using the **Trend** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). When set to `false`, users cannot view trends for a selected data point using the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu).  Type: boolean |
| `"VISUAL_STYLE": false` | When set to `true`, users can change the style of a visual.  When set to `false`, users cannot change the visual style. The visual style settings () [visual sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu) option is disabled when this switch is off and users cannot access the visual type sidebar.  Type: boolean |
| `"ZOOM_ACTION": false` | When set to `true`, users can zoom into a selected data point on a visual using the **Zoom** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). When set to `false`, users cannot zoom into a selected data point on a visual using the **Zoom** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu).  Type: boolean |
