---
title: "React to Resize Events"
id: 34932658600845
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932658600845-React-to-Resize-Events
updated_at: 2026-05-26T22:06:09Z
---

# React to Resize Events

# React to Resize Events

When a user resizes a chart widget, you must account for the new widget dimensions. You can specify your own resize handler function by overriding the `controller.resize` method.

Example:

controller.resize = function(newWidth, newHeight) {
// If needed, use the newWidth and newHeight values to resize chart
}

The specified handler executes every time a user action causes the widget dimensions to change. The following list provides a few examples of actions that trigger the resize event:

* A user changes the dimensions of the browser window.
* A user changes the dimensions of an individual widget.

Hiding or displaying controls like the Time Bar may reduce or increase the space available for widgets in a dashboard.
