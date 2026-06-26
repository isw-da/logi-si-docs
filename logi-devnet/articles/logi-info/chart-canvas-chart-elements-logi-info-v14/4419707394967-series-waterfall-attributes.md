---
title: "Series.Waterfall - Attributes"
id: 4419707394967
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707394967-Series-Waterfall-Attributes
updated_at: 2022-07-17T02:08:52Z
---

# Series.Waterfall - Attributes

# Series.Waterfall - Attributes

The Series.Waterfall element has the following attributes:

| Attribute | Description |
| --- | --- |
| Y-Axis Data Column | (Required) Specifies the name of a datalayer column whose values determine the height of each bar. |
| Bar Border Color | Sets the color of the thin border line around each bar. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233. New for 14.1 Or, enter the token @Gradient to use a gradient fill to represent the data. |
| Bar Border Color Transparency | Specifies the transparency of the thin border line around each bar. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| Bar Border Radius | Sets the amount of rounding for bar corners, in pixels. The default value is *0* pixels, which produces square corners. |
| Bar Border Thickness | Sets the thickness of the bar border lines, in pixels, when the related Bar Border Color attribute has a value. The default value is *1* pixel. |
| Bar Thickness | Sets the width of the bar in pixels. If left blank, the width will be determined automatically. |
| Color | Sets the bar fill color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233.  New for 14.1 Or, enter the token @Gradient to use a gradient fill to represent the data. |
| Combine With Series ID | Set this attribute to the element ID of another series to combine it with this series in the legend. When two series are combined, by default only the first one will appear in the legend but clicking the item in the legend toggles both series to appear and disappear. Or, the value *Previous* can be entered to combine this series with the previous series. |
| Disable Mouse Tracking | Disables mouse tracking for the series, when set to *True*. This affects tooltips and click events. For large datasets, this may improve performance. The default value is *False*. |
| Hover Brightness | Specifies the change in a bar's brightness when the mouse pointer hovers over it. Values can be *0* (no change) through *15* (lighter). The default value is *2*. |
| Intermediate Sum Bar Color | Sets the fill color of the Intermediate Sum bar. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233.  New for 14.1 Or, enter the token @Gradient to use a gradient fill to represent the data. |
| Intermediate Sum Bar Color Transparency | Specifies the transparency of the thin border line around the Intermediate Sum bar. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| Intermediate Sum Column | Controls the display of an "Intermediate Sum" bar, which is an extra bar in the chart showing the sum of data values, beginning with the first value, up to a specific point on the X-axis. To show an intermediate sum, configure the datalayer so it includes a "special" row inserted at the point of the desired intermediate sum. In this row, include a column with a value of *True*. Specify the name of that column in this attribute. Any other data values in this special row are ignored. You can add multiple Intermediate Sum bars by adding additional special rows in the desired places in the datalayer; just duplicate the first special row where desired. However, when calculating each intermediate sum, the previous special row resets the summarization to zero. For example: A special row in the datalayer at record 10 will produce a sum of the values for rows 1-9. A second special row at record 15 will produce a sum of the values for rows 11-14. There is no cumulative or running total effect for all rows. |
| Label Data Column X-axis | Specifies the name of a datalayer column whose values be represented by the bars. |
| Legend Label | Indicates text that will be shown for this series inside the chart legend. When a value is provided, it automatically causes the legend to be displayed. |
| Linked to X-Axis ID | Specifies the ID of an X-Axis element that this series should be linked to when using multiple X-axes. |
| Linked to Y-Axis ID | Specifies the ID of a Y-Axis element that this series should be linked to when using multiple Y-axes. |
| Negative Color | Sets the color for negative values. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #D5F484. |
| Negative Color Transparency | Specifies the transparency of the Negative Color. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| Total Bar Color | Sets the color for the automatically-generated "total bar" at the right side of the chart. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #D5F484. |
| Total Bar Color Transparency | Specifies the transparency of the Total Bar Color. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| Total Bar Label | Specifies the label text for the total bar. When set to *None*, the total bar will not be generated. The default value is *Total*. |
| Transparency | Specifies the transparency of the general chart bars. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different series to show through each other. |
