---
title: "React to Resize Events"
id: 43701053416973
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053416973-React-to-Resize-Events
updated_at: 2026-05-29T14:07:17Z
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
