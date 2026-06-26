---
title: "Axis Element Attributes"
id: 4419722735767
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722735767-Axis-Element-Attributes
updated_at: 2022-07-17T02:08:49Z
---

# Axis Element Attributes

# Axis Element Attributes

The X-Axis and Y-Axis elements have the same attributes, except as noted:

| Attribute | Description |
| --- | --- |
| New for 14.1 Auto Rotation Degrees | (X-Axis only) Automatically adjusts the chart's horizontal axis when the data points become crowded. By default, the value for this attribute is "undefined" and labels will word-wrap, when possible. When undefined, the top and bottom axes default to a -45 degree rotation. To utilize this feature, enter a numeric value between 0-90. |
| Axis Padding Left | (X-Axis only) When the X-axis presents Numeric or DateTime data, sets the padding between the edge of the plot area and the first data value, as a percentage of the axis length. This is useful for preventing the first data value from appearing at the very edge of the plot area. Set to *0* to remove all padding. The default value is *1.* |
| Axis Padding Right | (X-Axis only) When the X-axis presents Numeric or DateTime data, sets the padding between the edge of the plot area and the last data value, as a percentage of the axis length. This is useful for preventing the last data value from appearing at the very edge of the plot area. Set to *0* to remove all padding. The default value is *1.* |
| Axis Padding Top | (Y-Axis only) Sets the padding between the edge of the plot area and the highest data value, in pixels. This is useful for preventing the highest data value from appearing right at the edge of the plot area. The default value is *5* pixels. |
| Axis Type | Sets the scaling type for the axis. This can be a "smooth" scale, consistent with a stream of numbers or dates/times or, when working with the X-Axis element, it can also be a category (e.g. Apples, Oranges) which are often visualized using Bar and Pie charts. The default value varies based on the axis column data type: Text = *Category*, DateTime = *DateTimeLinear*, Numeric = *NumericLinear* or *NumericLogarithmic.* |
| Caption | Specifies the text of the axis caption. |
| Fixed Scale Lower Bound | Sets the lower scaling boundary of the axis. Use this attribute, for example, to cause negative Y-axis values to be plotted below the zero line (see [Plotting Negative Values](https://devnet.logianalytics.com/hc/en-us/articles/4419707404183-Plotting-Negative-Values)). Set this value to a number, or leave it blank for automatic scaling. If you specify a lower bound, then you must also specify an upper bound. |
| Fixed Scale Upper Bound | Sets the upper scaling boundary of the axis. Set this value to a number, or leave it blank for automatic scaling. If you specify an upper bound, then you must also specify a lower bound. |
| Hide Axis | Hides the axis from view. |
| Hide First Label | Hides the first tick mark label. The default value is *False*. |
| Hide Last Label | Hides the last tick mark label. The default value is *False*. |
| Line Color | Sets the axis line color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233. |
| Line Color Transparency | Specifies the transparency of the axis line color. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| Line Thickness | Specifies the thickness of the axis line, in pixels. The default value is *1* pixel. |
| Opposite Side | Specifies that the axis be displayed on the opposite side from its normal position, or Left for vertical axes and Bottom for horizontal axes. The default value is *False*. |
| Reverse Axis | Reverses the axis so low and high values are swapped. Chart is then rendered to match. For example, if Y-axis is reversed, low values are at the *top* of the canvas and the chart is drawn "downward" from it. |
| Reversed Stack Series Order | (Y-Axis only) When there are multiple Series in use, or a DataLayer.Crosstab which generates multiple Series, and the Series are stacked, this attribute reverses how the values are stacked. |
| Spacing | Sets the space, in pixels, between the legend and chart plot area. The default value is *10* pixels. |
| New for 14.1 Tick Count | Sets the number of ticks for your X and Y-axis. The default value is *Undefined*. Set this value to a number greater than 2.  Tick Count can only be used with Linear axes. DateTime, Logarithmic, and Category axes are not affected. |
