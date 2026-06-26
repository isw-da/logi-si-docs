---
title: "Series.Area Spline Range - Attributes"
id: 4406817047575
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817047575-Series-Area-Spline-Range-Attributes
updated_at: 2022-04-06T06:03:34Z
---

# Series.Area Spline Range - Attributes

# Series.Area Spline Range - Attributes

The Series.Area Spline Range element has the following attributes:

| Attribute | Description |
| --- | --- |
| High Value Data Column | (Required) Specifies the name of the datalayer column containing the high data value for each row. |
| Low Value Data Column | (Required) Specifies the name of the datalayer column containing the low data value for each row. |
| Color | Sets the data region fill color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233. |
| Combine With Series ID | Set this attribute to the element ID of another series to combine it with this series in the legend. When two series are combined, by default only the first one will appear in the legend but clicking the item in the legend toggles both series to appear and disappear. Or, the value *Previous* can be entered to combine this series with the previous series. |
| Connect Nulls | Specifies if data rows with null or blank values are to be ignored, allowing adjacent values to be connected in the chart. The default value is *False*. |
| Disable Mouse Tracking | Disables mouse tracking for the series, when set to *True*. This affects tooltips and click events on graphs and points. For large datasets, this may improve performance. The default value is *False*. |
| Hover Line Thickness | Sets the thickness of the line, in pixels, when the mouse pointer is hovered over it. The default value is *1* pixel. |
| Legend Label | Indicates text that will be shown for this series inside the chart legend. When a value is provided, automatically causes the legend to be displayed. |
| Line Color | Sets the data region's border line color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233. |
| Line Color Transparency | Specifies the transparency of the data region border line color. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| Line Style | Specifies the pattern of the data region's border line as either *Solid* or a combination of dashes and dots. |
| Line Thickness | Specifies the thickness of the data region's border line, in pixels. The default value is *1* pixel. |
| Linked to X-Axis ID | Specifies the ID of an X-Axis element that this series should be linked to when using multiple X-axes. |
| Linked to Y-Axis ID | Specifies the ID of a Y-Axis element that this series should be linked to when using multiple Y-axes. |
| Negative Color | Sets the color for negative values. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #D5F484. The default value is *Red*. |
| Negative Color Transparency | Specifies the transparency of the Negative Color. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| Negative Fill Color | Sets the data region fill color for negative values. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #D5F484.  The default value is *Red*. |
| Negative Fill Color Transparency | Specifies the transparency of the Negative Fill Color. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| Negative Threshold | Sets the positive-negative value threshold, also called the "zero level" or "base level". The default value is *0*. |
| Transparency | Specifies the transparency of the data region fill color. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| X-Axis Data Column | Specifies the name of a datalayer column whose values will be plotted along the X-axis. |
| X-Axis Data Column Type | Specifies the data type of the datalayer column named in the X-axis Data Column attribute. Options include *Auto* (the default), *Text*, *Number*, and *DateTime*.  By default, X-axis data values that are *DateTime* type will be automatically distributed evenly across the time series. If you want to disable this behavior, set this attribute value to *Text*. |
