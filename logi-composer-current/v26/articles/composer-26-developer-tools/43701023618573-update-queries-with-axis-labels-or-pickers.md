---
title: "Update Queries with Axis Labels or Pickers"
id: 43701023618573
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701023618573-Update-Queries-with-Axis-Labels-or-Pickers
updated_at: 2026-05-29T14:07:18Z
---

# Update Queries with Axis Labels or Pickers

# Update Queries with Axis Labels or Pickers

Axis Labels or Axis Pickers are Composer native controls that can be added to charts to provide a way for users to change query parameters dynamically. Chart developers can these controls by calling the method `controller.createaAxisLabel`. The `createAxislabel` method takes an object as its only argument with the following properties:

| Option | Description |
| --- | --- |
| `picks` | Name of the query variable.  **Note:**  Use the data accessor’s `getName` method to avoid hardcoding variable names. |
| `position` | Location of the axis label in the chart widget.  Valid options: `bottom`, `left`, `right`, `top` |
| `orientation` | Orientation of the axis label text.  Valid options: `vertical`, `horizontal` |

Example:

controller.createAxisLabel({
picks: 'Group By',
position: 'bottom',
orientation: 'horizontal',
});
controller.createAxisLabel({
picks: 'Size',
position: 'bottom',
orientation: 'horizontal',
});

The above example adds two axis pickers to the chart that provide users with the ability to change the fields used for the `Group By` and `Size` query variables.
