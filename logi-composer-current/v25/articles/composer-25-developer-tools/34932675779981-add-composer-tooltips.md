---
title: "Add Composer Tooltips"
id: 34932675779981
section: "Composer 25 Developer Tools"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932675779981-Add-Composer-Tooltips
updated_at: 2026-05-26T22:06:11Z
---

# Add Composer Tooltips

# Add Composer Tooltips

Charting libraries often include a tooltip implementation that may not look similar to the tooltips included with Composer native charts. As a developer, you can re-use the tooltip design in your custom charts by leveraging the `show` and `hide` methods in `controller.tooltip`.

To show a tooltip, use `controller.tooltip.show`. The `show`method takes an object as its only argument with the following properties:

| Option | Description |
| --- | --- |
| `x` | The x coordinate on the screen where the tooltip should render. |
| `y` | The y coordinate on the screen where the tooltip should render. |
| `data` | Function that returns a Composer data element. |

Optional properties:

| Option | Description |
| --- | --- |
| `event` | Takes a native browser event to specify the tooltip position. Use as an alternative to x and y properties. |
| `content` | Function that returns an HTML string to replace the content inside of the tooltip boxes. This can be used to render custom tooltips. |

Example:

myChart.on('mouseover', function(param) {
controller.tooltip.show({
x: param.x,
y: param.y,
data: function() {
return param.composerDataElement;
},
});
});

In the above example, we have a reference to chart instance stored in the `myChart` variable. It hooks into the `mouseover`event of the chart and provides a handler function. The chart provides the handler function with an object argument `param` with the x and y screen coordinates that describe where the tooltip should display.

In this example, the chart has also provided the original Composer data element for the hovered point. `controller.tooltip.show` can be called with an object that specifies the tooltip location and data for the tooltip.

To hide the tooltip, we can call the `controller.tooltip.hide` method.

Example:

myChart.on('mouseout', function() {
controller.tooltip.hide();
})

Here you hook into the `mouseout` event and provide a handler function that calls the `controller.toolitp.hide` method.
