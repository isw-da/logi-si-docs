---
title: "Series.Scatter - Attributes"
id: 4406822157335
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822157335-Series-Scatter-Attributes
updated_at: 2022-04-06T06:04:06Z
---

# Series.Scatter - Attributes

# Series.Scatter - Attributes

The Series.Scatter element has the following attributes:

| Attribute | Description |
| --- | --- |
| Y-Axis Data Column | (Required) Specifies the name of a datalayer column whose values will be plotted along the Y-axis. |
| Color | Sets the chart symbol color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233. @Chart tokens may be used here to provide dynamic, data-driven data point colors. |
| Combine With Series ID | Set this attribute to the element ID of another series to combine it with this series in the legend. When two series are combined, by default only the first one will appear in the legend but clicking the item in the legend toggles both series to appear and disappear. Or, the value *Previous* can be entered to combine this series with the previous series. |
| Disable Mouse Tracking | Disables mouse tracking for the series, when set to *True*. This affects tooltips and click events on graphs and points. For large datasets, this may improve performance.  The default value is *False*. |
| Legend Label | Indicates text that will be shown for this series inside the chart legend. When a value is provided, automatically causes the legend to be displayed. |
| Linked to X-Axis ID | Specifies the ID of an X-Axis element that this series should be linked to when using multiple X-axes. |
| Linked to Y-Axis ID | Specifies the ID of a Y-Axis element that this series should be linked to when using multiple Y-axes. |
| Transparency | Specifies the transparency of the symbol color. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| X-Axis Data Column | Specifies the name of a datalayer column whose values will be plotted along the X-axis. |
| X-Axis Data Column Type | Specifies the data type of the datalayer column named in the X-axis Data Column attribute. Options include *Auto* (the default), *Text*, *Number*, and *DateTime*. By default, X-axis data values that are *DateTime* type will be automatically distributed evenly across the time series. If you want to disable this behavior, set this attribute value to *Text*. |
