---
title: "Interacting with the Composer Context Menu"
id: 34932635535629
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932635535629-Interacting-with-the-Composer-Context-Menu
updated_at: 2026-05-26T22:06:12Z
---

# Interacting with the Composer Context Menu

# Interacting with the ComposerContext Menu

The Composer context menu is a native control that can be added to custom charts to provide users with a set of standard chart interactions. Your chart must be running an aggregated data query to leverage the context menu.

Default context menu actions:

| Action | Description |
| --- | --- |
| Details | Open a panel with a Raw Data table chart displaying the full set of records matching the selected data point. |
| Filter | Open a panel to select other charts in the dashboard to filter with a condition matching the selected data point. |
| Keyset | Open a panel to create a keyset from a data point. |
| Trend | Switches the current chart to the included **Line Chart: Multiple Metrics** chart and adds the selected data point as a filter. |
| Zoom | Open a panel to select a new attribute to drill into. The selection automatically changes the group-by field in the query and adds a filter condition matching the selected data point. |
| Remove | Removes the selected data point by adding a filter to the query to exclude it. |
| Settings | Opens the visual sidebar menu. |

Optional context menu options:

| Action | Description |
| --- | --- |
| Actions | Invoke an action for the visual. Only visible if an action template is defined and enabled for the data source. |
| Link | Access a dashboard that has been linked to the visual. Only visible if a dashboard link exists. |
| Create Alert | Open the create alert work area. |

## Create a Context Menu with Custom Actions

Add custom actions to your context menu, and bind methods to left and right mouse click actions in place of default actions.

menuEventsConfig: {
click: 'filter',
contextmenu: 'openMenu',
customActions: [{
name: 'google help',
action: (data) => window.open (''https://www.google.com/', '\_blank').focus(),
},
}]

Define your base configuration object. This is optional; if you don't define a base configuration object, Composer deploys the default context menu behavior.

Optionally, include a `customActions` items array. Your `customActions` can be bound as a method for the left or right mouse click in place of one of the [default actions](#DefaultActions).

Defining `customActions`:

| Option | Description |
| --- | --- |
| `name` | A name for each of the `customActions`.  Required. |
| `action` | The action you define for the `customActions`.  Required. |
| `icon` | An icon to associate with the `customActions`.  Optional. |
