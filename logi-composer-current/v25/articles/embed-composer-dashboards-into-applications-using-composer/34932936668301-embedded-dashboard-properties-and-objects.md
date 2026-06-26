---
title: "Embedded Dashboard Properties and Objects"
id: 34932936668301
section: "Embed Composer Dashboards Into Applications Using Composer"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932936668301-Embedded-Dashboard-Properties-and-Objects
updated_at: 2026-05-26T22:07:18Z
---

# Embedded Dashboard Properties and Objects

# Embedded Dashboard Properties and Objects

Properties can be passed as parameters to the [`createComponent` method](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932928903565-EmbedManager-Methods#top) when embedding Composer dashboards.

Here is a sample embedding `"componentInstanceId":"<id>"`:

embedManager.createComponent('dashboard',
const componentConfig = {
"[dashboardId](#dashboardId)": "<dashboard-ID>",
"[componentInstanceId](#componentInstanceId)":"<component-instance-ID>",
}
);

The following table describes available options for these properties and objects.

| Property/Object | Default | Description |
| --- | --- | --- |
| `"dashboardId":"<dashboard-ID>"` | none | The dashboard ID. If no dashboard ID is specified, an empty dashboard is embedded.  Type: string |
| `"componentInstanceId":"<component-instance-ID>"` | none | The instance ID for the dashboard is generated when the dashboard is created.  Type: string |

Here is a sample embedding `"type"`:

embedManager.createComponent('dashboard',
const componentConfig = {
"dashboardId": "<dashboard-ID>",
"componentInstanceId":"<component-instance-ID>",
"[type](#type)":"dashboard",
}
);

The following table describes available options for these properties and objects.

| Property/Object | Default | Description |
| --- | --- | --- |
| `"type":"dashboard"` |  | The type of embedded Composer component. |

Here is a sample embedding `"application"`:

embedManager.createComponent('dashboard',
const componentConfig = {
"dashboardId": "<dashboard-ID>",
"componentInstanceId":"<component-instance-ID>",
"type":"dashboard",
"application":{
"[banner](#application_banner)":false,
"[logo](#application_logo)":true
}
}
);

The following table describes available options for these properties and objects.

| Property/Object | Default | Description |
| --- | --- | --- |
| `"application.banner": true` | `false` | Indicates whether the Composer [top-level navigation banner](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933120256397-The-Top-Level-Navigation-Banner) should be shown with the embedded dashboard. Valid values are `true` or `false`.  Type: boolean  This property is deprecated and will be removed in a future release. |
| `"application.logo": true` | `false` | Indicates whether the Composer logo should be shown with the embedded dashboard. Valid values are `true` or `false`.  Type: boolean  This property is deprecated and will be removed in a future release. |

Here is a sample embedding `"interactivityProfileName"`:

embedManager.createComponent('dashboard',
const componentConfig = {
"dashboardId": "<dashboard-ID>",
"componentInstanceId":"<component-instance-ID>",
"type":"dashboard",
"application":{
"banner":false,
"logo":true
}
"[interactivityProfileName](#interactivityProfileName)":"interactive",
}
);

The following table describes available options for these properties and objects.

| Property/Object | Default | Description |
| --- | --- | --- |
| `"interactivityProfileName" :"interactive"` | `interactive` | Determines the way in which your users will be able to work with the embedded dashboard. Valid values are `readonly` and `interactive`. If you do not want the user of your application to change anything and only be able to view the dashboard, specify `readonly`. If you want your users to be able to make changes to the dashboard, specify `interactive`.  When the mode is `readonly`, the dashboard cannot be changed.  **Note:**  This setting is backward-compatible with the `interactive` option for public shared link embeds. If you are migrating to Composer's JavaScript embed technology, specify `interactive` for this setting to ease the migration.  Type: string |

Here is a sample embedding `"interactivityOverrides"`:

embedManager.createComponent('dashboard',
const componentConfig = {
"dashboardId": "<dashboard-ID>",
"componentInstanceId":"<component-instance-ID>",
"type":"dashboard",
"application":{
"banner":false,
"logo":true
}
"interactivityProfileName":"interactive",
"[interactivityOverrides](#interactivityOverrides)":"<interactivity-overrides-ID>",
}
);

The following table describes available options for these properties and objects.

| Property/Object | Default | Description |
| --- | --- | --- |
| `"interactivityOverrides":"<interactivity-overrides-ID>"` | none | Specifies specific dashboard and visual interactivity settings for an embedded dashboard. The visual interactivity settings specified in this object will override any interactivity settings specified for the individual visuals.  These settings will also override the dashboard interactivity profile linked to the dashboard (the one saved with the dashboard) and the dashboard interactivity profile passed by the `interactivityProfileName` property.  Type: object |

Here is a sample embedding `"mode"`:

embedManager.createComponent('dashboard',
const componentConfig = {
"dashboardId": "<dashboard-ID>",
"componentInstanceId":"<component-instance-ID>",
"type":"dashboard",
"application":{
"banner":false,
"logo":true
}
"interactivityProfileName":"interactive",
"interactivityOverrides":"<interactivity-overrides-ID>",
"[mode](#mode)":"interactive",
}
);

The following table describes available options for these properties and objects.

| Property/Object | Default | Description |
| --- | --- | --- |
| `"mode":"interactive"` | `interactive` | When a dashboard interactivity profile is specified (using the `interactivityOverrides` object or the `interactivityProfileName` parameter), the `mode` parameter is ignored. The `mode` parameter is also deprecated in Composer and will be removed in a future release.  Type: string |

Here is a sample embedding `"theme"`:

embedManager.createComponent('dashboard',
const componentConfig = {
"dashboardId": "<dashboard-ID>",
"componentInstanceId":"<component-instance-ID>",
"type":"dashboard",
"application":{
"banner":false,
"logo":true
}
"interactivityProfileName":"interactive",
"interactivityOverrides":"<interactivity-overrides-ID>",
"mode":"interactive",
"[theme](#theme)":"modern",
}
);

The following table describes available options for these properties and objects.

| Property/Object | Default | Description |
| --- | --- | --- |
| `"theme":"dark"` | `composer` | The theme for the embedded dashboard. Valid values are `composer`, `modern`, or `dark`. The initial default theme, `composer`, is the same as the `modern` theme. However, if you [add your own themes](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933172226573-Manage-UI-Themes) to the application, more options are available in this list and you may have introduced a different default.  Type: string |

Here is a sample embedding `"editor"`:

embedManager.createComponent('dashboard',
const componentConfig = {
"dashboardId": "<dashboard-ID>",
"componentInstanceId":"<component-instance-ID>",
"type":"dashboard",
"application":{
"banner":false,
"logo":true
}
"interactivityProfileName":"interactive",
"interactivityOverrides":"<interactivity-overrides-ID>",
"mode":"interactive",
"theme":"modern",
"editor":{
"[placement](#editor_placement)": "docRight"
}
}
);

The following table describes available options for these properties and objects.

| Property/Object | Default | Description |
| --- | --- | --- |
| `"editor.placement":"docRight"` | `modals` | Indicates where the dashboard editor appears. Valid editor placements are `dockRight` and `modals`.  Type: string |

Here is a sample embedding `"header"`:

embedManager.createComponent('dashboard',
const componentConfig = {
"dashboardId": "<dashboard-ID>",
"componentInstanceId":"<component-instance-ID>",
"type":"dashboard",
"application":{
"banner":false,
"logo":true
}
"interactivityProfileName":"interactive",
"interactivityOverrides":"<interactivity-overrides-ID>",
"mode":"interactive",
"theme":"modern",
"editor":{
"placement": "docRight"
}
"header": {
"[title](#header_title)": "My Dash"
"[showActions](#header_showActions)": false,
"[showTitle](#header_showTitle)": false,
"[visible](#header_visible)": false
}
}
);

The following table describes available options for these properties and objects.

| Property/Object | Default | Description |
| --- | --- | --- |
| `"header.title":"<newtitle>"` | none | Allows you to overwrite the title of the embedded dashboard. The embedded dashboard title is read only; it cannot be changed while the dashboard is embedded.  Type: string |
| `"header.showActions": false` | `true` | Indicates whether dashboard actions should be visible for the embedded dashboard. Valid values are `true` or `false`.  Type: boolean |
| `"header.showTitle": false` | `true` | Indicates whether the dashboard title should be shown for the embedded dashboard. Valid values are `true` or `false`.  Type: Boolean |
| `"header.visible": false` | `true` | Indicates whether the dashboard header should be shown for the embedded dashboard. Valid values are `true` or `false`. |

Here is a sample embedding `"intialFilters"`:

intialFilters: {
sourceId: "<source-id>"
timeFilter: {
from: "+$start\_of\_data",
to: "+$end\_of\_data",
timeField: "\_saledate",
},
filters: [{
"operation": "BETWEEN"
"paths": "returns",
"value": [ 1, 25 ]
}]
}

The following table describes available options for these properties and objects.

| Property/Object | Default | Description |
| --- | --- | --- |
| `initialFilters` | none | Allows you to pass initial filters to the specified dashboard. Pass parameters for `filters`, `sourceId`, `timeFilter`, and `applyFiltersStrategy`.  Type: string |
| `applyFiltersStrategy` | `overrideSamePath` | Use `overrideSamePath` to overwrite filters using the same path.  Use `replaceExisting` to remove all filters and use only defined `initialFilters`. |

You can also refresh your data in the dashboard as needed.

| Method | Description |
| --- | --- |
| `component.refreshData()` | Refreshes data in the dashboard when called. |
