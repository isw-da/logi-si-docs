---
title: "Series.Bubble - Attributes"
id: 4419707362583
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707362583-Series-Bubble-Attributes
updated_at: 2022-07-17T02:09:03Z
---

# Series.Bubble - Attributes

# Series.Bubble - Attributes

The Series.Bubble element has the following attributes:  

| Attribute | Description |
| --- | --- |
| Size Data Column | (Required) Specifies the name of a datalayer column that contains values for bubble sizes. |
| Y-Axis Data Column | (Required) Specifies the name of a datalayer column whose values will be plotted along the Y-axis. |
| Bubble Max Size | Sets the maximum bubble size, in pixels or a percentage. Bubbles will be automatically sized between the Bubble Min Size and Bubble Max Size to produce the size of each bubble. Indicate "pixels" by entering just a number, or a "percentage" of the lesser of the plot width and height by entering a number and the percent sign. The default value is *20%*. |
| Bubble Min Size | Sets the minimum bubble size, in pixels or a percentage. Bubbles will be automatically sized between the Bubble Min Size and Bubble Max Size to produce the size of each bubble. Indicate "pixels" by entering just a number, or a "percentage" of the lesser of the plot width and height by entering a number and the percent sign. The default value is *20%*. |
| Color | Sets the bubble color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233.  New for 14.1 Or, enter the token @Gradient to use a gradient fill to represent the data. |
| Combine With Series ID | Set this attribute to the element ID of another series to combine it with this series in the legend. When two series are combined, by default only the first one will appear in the legend but clicking the item in the legend toggles both series to appear and disappear. Or, the value *Previous* can be entered to combine this series with the previous series. |
| Disable Mouse Tracking | Disables mouse tracking for the series, when set to *True*. This affects tooltips and click events on graphs and points. For large datasets, this may improve performance.   The default value is *False*. |
| Legend Label | Indicates text that will be shown for this series inside the chart legend. When a value is provided, automatically causes the legend to be displayed. |
| Linked to X-Axis ID | Specifies the ID of an X-Axis element that this series should be linked to when using multiple X-axes. |
| Linked to Y-Axis ID | Specifies the ID of a Y-Axis element that this series should be linked to when using multiple Y-axes. |
| Transparency | Specifies the transparency of the bubble color. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| X-Axis Data Column | Specifies the name of a datalayer column whose values will be plotted along the X-axis. |
| X-Axis Data Column Type | Specifies the data type of the datalayer column named in the X-axis Data Column attribute. Options include *Auto* (the default), *Text*, *Number*, and *DateTime*. By default, X-axis data values that are *DateTime* type will be automatically distributed evenly across the time series. If you want to disable this behavior, set this attribute value to *Text*. |
