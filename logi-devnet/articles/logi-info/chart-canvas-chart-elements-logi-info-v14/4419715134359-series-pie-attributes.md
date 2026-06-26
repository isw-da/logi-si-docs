---
title: "Series.Pie - Attributes"
id: 4419715134359
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715134359-Series-Pie-Attributes
updated_at: 2022-07-17T02:08:57Z
---

# Series.Pie - Attributes

# Series.Pie - Attributes

The Series.Pie element has the following attributes:

| Attribute | Description |
| --- | --- |
| Y-Axis Data Column | (Required) Specifies the name of a datalayer column whose values will be plotted along the Y-axis, dictating how large each pie slice is. |
| Angle End | Sets the ending angle of the Pie chart's *last* slice, in degrees. For example, to create a Pie chart which has 180 degrees total, facing upwards, set these attributes: Angle Start = *270*, Angle End = *450* |
| Angle Start | Sets the starting angle of the Pie chart's *first* slice, in degrees. The default value of *0* starts the first slice at the 12 o'clock position and a value of *90* is the 3 o'clock position. |
| Border Color | Sets the color of the border line around the pie and around each slice. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, like #112233.  New for 14.1 Or, enter the token @Gradient to use a gradient fill to represent the data. |
| Border Color Transparency | Specifies the transparency of the border line. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| Border Thickness | The thickness of border line around the pie and around each slice, in pixels. The default is value is *1* pixel. |
| Center X | Sets the horizontal center point of the Pie chart, in pixels, within the canvas. |
| Center Y | Sets the vertical center point of the Pie chart, in pixels, within the canvas. |
| Colors | Sets the colors of the pie slices, which should be entered as a comma-separated list. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233.  New for 14.1 Or, enter the token @Gradient to use a gradient fill to represent the data. When there are more slices than colors specified, the listed colors are used again from the beginning. A default set of colors is used if this is left blank and no theme has been applied, see [Chart Canvas Charts](https://devnet.logianalytics.com/hc/en-us/articles/4419715153303-Chart-Canvas-Charts). |
| Disable Mouse Tracking | Disables mouse tracking for the series, when set to *True*. This affects tooltips and click events on graphs and points. For large datasets, this may improve performance. The default value is *False*. |
| Donut Hole Size | Sets the size of the inner diameter of the Pie chart, in pixels. Any size greater than *0* renders a "doughnut" style chart. The default value is *0* pixels. |
| Hover Brightness | Specifies the amount to change a pie slice's color when the mouse pointer is hovered over it. Values can be between *0* (no change) and *15* (lighter). The default value is *2*. |
| Label Data Column X-Axis | Set this to a column returned from the DataLayer. It represents the "name", or x-axis value, of each pie slice. |
| Label Location | Specifies how Pie chart slice labels will appear. Select:   - *SideLayout* to have labels appear outside the pie, with arrows connecting them to slices. - *Legend* to have slices identified in a legend. The legend can be clicked to toggle the visibility of individual slices in the pie. - *NoLabels* to hide the labels altogether.  The default value is *SideLayout*. |
| Min Radius | Sets the minimum acceptable size of the Pie chart, in pixels. During rendering, the pie radius will try to shrink automatically, if necessary, to accommodate any exterior slice labels and still fit the canvas, but it can be no smaller than this size. |
| Pie Label Style | Specifies how Pie chart slice labels will appear. Select:   - *SideLayout* to have labels appear outside the pie, with arrows connecting them to slices. - *Legend* to have slices identified in a legend. The legend can be clicked to toggle the visibility of individual slices in the pie. - *NoLabels* to hide the labels altogether.  The default value is *SideLayout*. |
| Radius | Determines the size, by setting the radius, of a Pie chart, in pixels. If left blank, the chart size is determined automatically. |
| Show Data Values | Specifies if the value of each data point should be shown on the Pie chart. Depending on the value of the Label Location attribute, they may be shown alone or with the label values. The default value is *False*. |
| Show Data Values Format | Specifies formatting characteristics for data values. For dates, the non-specific formats, such as *General Date*, *Short Time*, etc., are converted according to the browser's international settings. For very large reports, the non-specific formats perform better. Special formats include:  *<* and *>* - change strings to lower and upper case. *Expanded Spaces* - preserves space characters that would otherwise be collapsed by the web browser. *mp* - formats numbers with the "metric prefix". For example, to format 1,234,567 as "$1.23M", enter *$#.00mp*. Supported metric prefixes are from 1000^6 to 1000^-6. For more information see [this page](http://en.wikipedia.org/wiki/Metric_prefix).  *qq* - returns the number of the quarter when the value being formatted represents a date. To return the year and quarter together like "2010 Q1", set the format to *yyyy Qqq*. |
| New for 14.1 Show Second Data Values | Specifies if the value of the second data point should be shown on the Pie chart. Depending on the value of the Label Location attribute, they may be shown alone or with the label values. The default value is *False*. |
| New for 14.1 Show Second Data Values Format | Specifies formatting characteristics for the second data values. For dates, the non-specific formats, such as *General Date*, *Short Time*, etc., are converted according to the browser's international settings. For very large reports, the non-specific formats perform better. Special formats include:  *<* and *>* - change strings to lower and upper case. *Expanded Spaces* - preserves space characters that would otherwise be collapsed by the web browser. *mp* - formats numbers with the "metric prefix". For example, to format 1,234,567 as "$1.23M", enter *$#.00mp*. Supported metric prefixes are from 1000^6 to 1000^-6. For more information see [this page](http://en.wikipedia.org/wiki/Metric_prefix).  *qq* - returns the number of the quarter when the value being formatted represents a date. To return the year and quarter together like "2010 Q1", set the format to *yyyy Qqq*. |
| Transparency | Specifies the transparency of the pie slice color. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
