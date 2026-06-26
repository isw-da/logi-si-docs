---
title: "Embedded Dashboard Properties and Objects"
id: 4405851050647
section: "Embed Composer Dashboards Into Applications using Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851050647-Embedded-Dashboard-Properties-and-Objects
updated_at: 2021-09-21T01:28:30Z
---

# Embedded Dashboard Properties and Objects

# Embedded Dashboard Properties and Objects

Properties can be passed as parameters to the [`createComponent` method](https://devnet.logianalytics.com/hc/en-us/articles/4405859341847-Supported-EmbedManager-Methods) when embedding Composer dashboards.

Here is a sample:

```
embedManager.createComponent('dashboard',
    {
      "dashboardId": "<dashboard-ID>",
      "<property>": "<propertyValue>"
    }
);
```

The following table describes all of the available properties.

| Property/Object | Default | Description |
| --- | --- | --- |
| `"application.banner": true` | `false` | Indicates whether the Composer [top-level navigation banner](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner) should be shown with the embedded dashboard. Valid values are `true` or `false`.  Type: boolean  This property is deprecated and will be removed in a future release. |
| `"application.logo": true` | `false` | Indicates whether the Composer logo should be shown with the embedded dashboard. Valid values are `true` or `false`.  Type: boolean  This property is deprecated and will be removed in a future release. |
| `"componentInstanceId":"<id>"` | none | The instance ID for the dashboard is generated when the dashboard is created.  Type: string |
| `"dashboardId":"<id>"` | none | The dashboard ID. If no dashboard ID is specified, an empty dashboard is embedded.  Type: string |
| `"editor.placement":"docRight"` | `modals` | Indicates where the dashboard editor appears. Valid editor placements are `dockRight` and `modals`.  Type: string |
| `"header.showActions": false` | `true` | Indicates whether dashboard actions should be visible for the embedded dashboard. Valid values are `true` or `false`.  Type: boolean |
| `"header.showTitle": false` | `true` | Indicates whether the dashboard title should be shown for the embedded dashboard. Valid values are `true` or `false`.  Type: Boolean |
| `"header.title":"<newtitle>"` | none | Allows you to overwrite the title of the embedded dashboard. The embedded dashboard title is read only; it cannot be changed while the dashboard is embedded.  Type: string |
| `"header.visible": false` | `true` | Indicates whether the dashboard header should be shown for the embedded dashboard. Valid values are `true` or `false`. |
| `"interactivityOverrides"` | none | Specifies specific dashboard and visual interactivity settings for an embedded dashboard. The visual interactivity settings specified in this object will override any interactivity settings specified for the individual visuals. These settings will also override the dashboard interactivity profile linked to the dashboard (the one saved with the dashboard) and the dashboard interactivity profile passed by the `interactivityProfileName` property.  Type: object |
| `"interactivityProfileName":"interactive"` | `interactive` | Determines the way in which your users will be able to work with the embedded dashboard. Valid values are `readonly` and `interactive`. If you do not want the user of your application to change anything and only be able to view the dashboard, specify `readonly`. If you want your users to be able to make changes to the dashboard, specify `interactive`.  When the mode is `readonly`, the dashboard cannot be changed.  This setting is backward-compatible with the `interactive` option for public shared link embeds. If you are migrating to Composer's JavaScript embed technology, specify `interactive` for this setting to ease the migration.  Type: string |
| `"mode":"interactive"` | `interactive` | When a dashboard interactivity profile is specified (using the `interactivityOverrides` object or the `interactivityProfileName` parameter), the `mode` parameter is ignored. The `mode` parameter is also deprecated in Composer 6.7 and will be removed in a future release.  Type: string |
| `"theme":"dark"` | `composer` | The theme for the embedded dashboard. Valid values are `composer`, `modern`, or `dark`. The initial default theme, `composer`, is the same as the `modern` theme. However, if you [add your own themes](https://devnet.logianalytics.com/hc/en-us/articles/4405859480983-Manage-UI-Themes) to the application, more options are available in this list and you may have introduced a different default.  Type: string |
| `"type":"dashboard"` |  | The type of embedded Composer component. |
