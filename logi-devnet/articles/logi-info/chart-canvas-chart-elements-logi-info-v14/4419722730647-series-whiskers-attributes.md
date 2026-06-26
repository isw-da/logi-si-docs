---
title: "Series.Whiskers - Attributes"
id: 4419722730647
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722730647-Series-Whiskers-Attributes
updated_at: 2022-07-17T02:08:50Z
---

# Series.Whiskers - Attributes

# Series.Whiskers - Attributes

The Series.Whiskers element has the following attributes:

| Attribute | Description |
| --- | --- |
| High Value Data Column | (Required) Specifies the name of a datalayer column whose values will be plotted as the highest possible value. |
| Low Value Data Column | (Required) Specifies the name of a datalayer column whose values will be plotted as the lowest possible value. |
| Combine With Series ID | Set this attribute to the element ID of another series to combine it with this series in the legend. When two series are combined, by default only the first one will appear in the legend but clicking the item in the legend toggles both series to appear and disappear. Or, the value *Previous* can be entered to combine this series with the previous series. |
| Disable Mouse Tracking | Disables mouse tracking for the series, when set to *True*. This affects tooltips and click events on graphs and points. For large datasets, this may improve performance. The default value is *False*. |
| ID | Specifies a unique identifier for this element. |
| Linked to X-Axis ID | Specifies the ID of an X-Axis element that this series should be linked to when using multiple X-axes. |
| Linked to Y-Axis ID | Specifies the ID of a Y-Axis element that this series should be linked to when using multiple Y-axes. |
| Stem Color | Specifies the color of the "stem", the vertical line extending from the bar graphic to the whiskers. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #D5F484.  New for 14.1 Or, enter the token @Gradient to use a gradient fill to represent the data. The default value is *Black*. |
| Stem Color Transparency | Specifies the transparency of the Stem Color. The lowest value of *0* specifies that the stem line is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent stem line. Use medium-level transparency to allow different chart layers to show through each other. |
| Stem Line Style | Specifies the pattern of the stem line as either *Solid* or as a combination of dashes and dots. The default value is *Solid* |
| Stem Line Thickness | Sets the thickness of the stem line, in pixels. The default value is *1* pixel. |
| Whisker Color | Specifies the color of the "whiskers", the horizontal lines marking the high and low values. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #D5F484.  New for 14.1 Or, enter the token @Gradient to use a gradient fill to represent the data. The default value is *Black*. |
| Whisker Color Transparency | Specifies the transparency of the Whisker Color. The lowest value of *0* specifies that the whisker lines are opaque, with no transparency. At the other end of the scale, *15* specifies completely transparent whisker lines. Use medium-level transparency to allow different chart layers to show through each other. |
| Whisker Line Thickness | Sets the thickness of the whisker lines, in pixels. The default value is *1* pixel. |
| Whisker Width | Sets the horizontal width of the whisker lines, in pixels. The default value is *33* pixels. |
| X-Axis Data Column | Specifies the name of a datalayer column whose values are being plotted along the X-axis. |
| X-Axis Data Column Type | Specifies the data type of the datalayer column named in the X-axis Data Column attribute. Options include *Auto* (the default), *Text*, *Number*, and *DateTime*. By default, X-axis data values that are *DateTime* type will be automatically distributed evenly across the time series. If you want to disable this behavior, set this attribute value to *Text*. |
