---
title: "Series.Bar Range - Attributes"
id: 4419715123863
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715123863-Series-Bar-Range-Attributes
updated_at: 2022-07-17T02:09:05Z
---

# Series.Bar Range - Attributes

# Series.Bar Range - Attributes

The Series.Bar Range element has the following attributes:

| Attribute | Description |
| --- | --- |
| High Value Data Column | (Required) Specifies the name of the datalayer column containing the high data value for each row. |
| Low Value Data Column | (Required) Specifies the name of the datalayer column containing the low data value for each row. |
| Bar Border Color | Sets the color of the thin border line around each bar. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233.  New for 14.1 Or, enter the token @Gradient to use a gradient fill to represent the data. |
| Bar Border Color Transparency | Specifies the transparency of the thin border line around each bar. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| Bar Border Radius | Sets the amount of rounding for bar corners, in pixels. The default value is *0* pixels, which produces square corners. |
| Bar Border Thickness | Sets the thickness of the bar border lines, in pixels, when the related Bar Border Color attribute has a value. The default value is 1 pixel. |
| Bar Thickness | Sets the width of the bar in pixels. If left blank, the width will be determined automatically. |
| Color | Sets the data region fill color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233.  New for 14.1 Or, enter the token @Gradient to use a gradient fill to represent the data. |
| Combine With Series ID | Set this attribute to the element ID of another series to combine it with this series in the legend. When two series are combined, by default only the first one will appear in the legend but clicking the item in the legend toggles both series to appear and disappear. Or, the value *Previous* can be entered to combine this series with the previous series. |
| Disable Bar Grouping | Disables grouping of side-by-side bars, when set to *True*. Bars that are not grouped are drawn individually and overlap each other. The default value is *False*. |
| Disable Mouse Tracking | Disables mouse tracking for the series, when set to *True*. This affects tooltips and click events on graphs and points. For large datasets, this may improve performance. The default value is *False*. |
| Hover Brightness | Specifies the amount to change a bar's color when the mouse pointer is hovered over it. Values can be between *0* (no change) and *15* (lighter). The default value is *2*. |
| Legend Label | Indicates text that will be shown for this series inside the chart legend. When a value is provided, automatically causes the legend to be displayed. |
| Line Color | Sets the data region's border line color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233.  New for 14.1 Or, enter the token @Gradient to use a gradient fill to represent the data. |
| Line Color Transparency | Specifies the transparency of the data region border line color. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| Line Style | Specifies the pattern of the data region's border line as either *Solid* or a combination of dashes and dots. |
| Line Thickness | Specifies the thickness of the data region's border line, in pixels. The default value is *1* pixel. |
| Linked to X-Axis ID | Specifies the ID of an X-Axis element that this series should be linked to when using multiple X-axes. |
| Linked to Y-Axis ID | Specifies the ID of a Y-Axis element that this series should be linked to when using multiple Y-axes. |
| Negative Color | Sets the color for negative values. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #D5F484. The default value is *Red*. |
| Negative Color Transparency | Specifies the transparency of the Negative Color. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| Negative Threshold | Sets the positive-negative value threshold, also called the "zero level" or "base level". The default value is *0*. |
| Transparency | Specifies the transparency of the data region fill color. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| X-Axis Data Column | Specifies the name of a datalayer column whose values will be plotted along the X-axis. |
| X-Axis Data Column Type | Specifies the data type of the datalayer column named in the X-axis Data Column attribute. Options include *Auto* (the default), *Text*, *Number*, and *DateTime*.  By default, X-axis data values that are *DateTime* type will be automatically distributed evenly across the time series. If you want to disable this behavior, set this attribute value to *Text*. |
