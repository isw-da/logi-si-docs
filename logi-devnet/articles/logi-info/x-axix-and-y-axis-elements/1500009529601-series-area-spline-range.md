---
title: "Series.Area Spline Range"
id: 1500009529601
section: "X-Axix and Y-Axis Elements"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009529601-Series-Area-Spline-Range
updated_at: 2021-06-17T01:58:01Z
---

# Series.Area Spline Range

# Series.Area Spline Range

The Chart Canvas element's Series child elements cause a data visualization (the chart) to be rendered in the canvas. This topic discusses the **Series.Area Spline Range** element.

* About Series.Area Spline Range
* [Multiple Series](#Multiple)
* [Attributes](#Attributes)
* [Data Labels Element](#Labels)
* [Quicktips Element](#Quicktips)
* [Action Elements](#Action)
* [Input Selection](#Selection)

## About Series.Area Spline Range

The **Series.Area Spline Range** element generates an Area Spline Range chart, which is commonly used to represent sets of low and high values, as numbers or
percentages, over time.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771932183/introcccharts_33.png)

The example above shows a simple Area Spline Range chart, presenting the low and high temperatures for a month.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771932439/introcccharts_34.png)

As shown above, the chart is created by adding Series.Area Spline Range to the canvas, along with a datalayer. Very few attributes need to be set for this Series element in order to produce a basic chart.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771450519/plusicon.gif) Note that a datalayer element can be used either beneath Series.Area Spline Range, as shown above, or beneath Chart Canvas. If used as a child of Chart Canvas, its data is available to *all* child Series elements. This can improve performance if you have several series, all using the *same* data, beneath the same Chart Canvas element.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771932695/introcccharts_35.png)

The properties of the X- and Y-axis, including captions, are set using the **X-Axis** and **Y-Axis** elements. For example, in order to provide a caption for the X-axis, add an **X-Axis** element beneath Chart Canvas and set its **Caption** attribute, as shown above. Repeat for the Y-axis.

#### Using Multiple Series

You can add additional series to the chart by adding additional Series elements:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778742039/introcccharts_36_557x393.png)

The example above shows two Series, one for each set of temperature ranges. A legend can also be added very easily.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771933207/introcccharts_37.png)

The example above shows the two Series elements, their datalayers and optional Quicktips, and the X-Axis and Y-Axis elements used to produce the previous chart. You can adjust which data range appears "in front" of the other in the chart by changing the order of the Series elements in the definition. Setting the Series elements' **Legend Label** attribute will automatically cause the legend to be displayed.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771450519/plusicon.gif) When using multiple series, you may be able to reduce the number of data queries and improve performance by using Local Data (see [Introducing Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/1500009530161-Introducing-Datalayers)) to read all of the data once and then link its datalayer (see [Link Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/1500009530221-Link-Datalayers)) to share it
to the series. At each Series element,
link its datalayer to the shared Local Data datalayer and filter the data to meet the needs of each individual series.

You can combine different types of Series elements, for example, Series.Area and Series.Bar, to produce combinations of visualizations.

## Attributes

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

## Using the Data Labels Element

A "data label" is text shown next to each data point that shows its value. When the **Data Labels** element is used as a child of Series.Area Spline Range, text representing the data values will appear on the chart:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778742423/introcccharts_38.png)

The Data Labels element has attributes that allow you to control the font family, color, size, and weight, the data format, border color, and positioning of the text.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771435287/notev11.3.png)The Data Labels element's color-related attribute values can be set using @Chart tokens.

## Using the Quicktips Element

By default, a "quicktip" is displayed when the mouse hovers near or over a data point:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778742807/introcccharts_39.png)

The automatically-generated quicktip displays information for the X- and Y-axis, as shown above, left. However, you may want to display other information or format it differently, as shown above, right, which can be done by adding a **Quicktip** child element beneath Series.Area Spline Range.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771933463/introcccharts_40.png)

The example above shows a Quicktip element (no attributes need to be set) and three **Quicktip Row** child elements, used to create the quicktip shown in the previous image. Note that an @Chart token is used access the chart data.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771435287/notev11.3.png)Intrinsic functions are supported in the Quicktip attributes.

## Using Action Elements

Action elements initiate processing of a report or process task definition, redirection to a link, or other processing when a data point in the series is clicked.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778743191/introcccharts_40a.png)

In the example above, an **Action.Report** element has been added as a child of the Series, along with its **Target.Report** and **Link Parameters** child elements. To reference chart data in parameters, use the @Chart token, as shown above.

A variety of Action elements are available for use with Series, including Action.Link, Action.Process, and Action.Refresh Element. Additional Action elements will be added in future releases.

## Using Input Selection

This series can also be used with the **Input Selection** family of elements, which turn the chart into an input control. This allows users, at runtime, to select points or values on the chart with their mouse and your report can then take action using the selected data. This is very useful, for example, for drilling into the data.

For more information about this functionality, see [Input Selection](https://devnet.logianalytics.com/hc/en-us/articles/1500009514042-Input-Selection).
