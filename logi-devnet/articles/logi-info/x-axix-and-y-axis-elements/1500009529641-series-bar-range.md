---
title: "Series.Bar Range"
id: 1500009529641
section: "X-Axix and Y-Axis Elements"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009529641-Series-Bar-Range
updated_at: 2021-06-17T01:58:02Z
---

# Series.Bar Range

# Series.Bar Range

The Chart Canvas element's Series child elements cause a data visualization (the chart) to be rendered in the canvas. This topic discusses the **Series.Bar Range** element.

* About Series.Bar Range
* [Use Multiple Series](#Multiple)
* [Attributes](#Attributes)
* [Use the Data Labels Element](#Labels)
* [Use the Quicktips Element](#Quicktips)
* [Use Action Elements](#Action)
* [Use Input Selection](#Selection)

## About Series.Bar Range

The **Series.Bar Range** element generates a Bar Range chart, which is commonly used to represent separate events that have starting and ending values, over time.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771927575/introcccharts_49.png)

The example above shows a simple Bar Range chart, presenting daily low and high stock prices for a month.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771927831/introcccharts_50.png)

As shown above, the chart is created by adding Series.Bar Range to the canvas, along with a datalayer. Very few attributes need to be set for this Series element in order to produce a basic chart.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771450519/plusicon.gif) Note that a datalayer element can be used either beneath Series.Bar Range, as shown above, or beneath Chart Canvas. If used as a child of Chart Canvas, its data is available to *all* child Series elements. This can improve performance if you have several series, all using the *same* data, beneath the same Chart Canvas element.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778738199/introcccharts_51.png)

The properties of the X- and Y-axis, including captions, are set using the **X-Axis** and **Y-Axis** elements. For example, in order to provide a caption for the X-axis, add an **X-Axis** element beneath Chart Canvas and set its **Caption** attribute, as shown above. Repeat for the Y-axis.

## Use Multiple Series

You can add additional series to the chart by adding additional Series elements:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771928215/introcccharts_52.png)

The example above shows two Series, for a set of stock prices from different years, along with a legend.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771928471/introcccharts_53.png)

The example above shows the two Series elements, their datalayers and optional Quicktips, and the X-Axis and Y-Axis elements used to produce the previous chart. You can adjust which data range appears "in front" of the other in the chart and in the legend by changing the order of the Series elements in the definition. Setting the Series elements' **Legend Label** attribute will automatically cause the legend to be displayed.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771450519/plusicon.gif) When using multiple series, you may be able to reduce the number of data queries and improve performance by using Local Data (see [Introducing Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/1500009530161-Introducing-Datalayers)) to read all of the data once and then link its datalayer (see [Link Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/1500009530221-Link-Datalayers)) to share it
to the series. At each Series element,
link its datalayer to the shared Local Data datalayer and filter the data to meet the needs of each individual series.

You can combine different types of Series elements, for example, Series.Area and Series.Bar, to produce combinations of visualizations.

## Use Attributes

The Series.Bar Range element has the following attributes:

| Attribute | Description |
| --- | --- |
| High Value Data Column | (Required) Specifies the name of the datalayer column containing the high data value for each row. |
| Low Value Data Column | (Required) Specifies the name of the datalayer column containing the low data value for each row. |
| Bar Border Color | Sets the color of the thin border line around each bar. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233. |
| Bar Border Color Transparency | Specifies the transparency of the thin border line around each bar. The lowest value of *0* specifies that the background is opaque, with no transparency. At the other end of the scale, *15* specifies a completely transparent background. Use medium-level transparency to allow different chart layers to show through each other. |
| Bar Border Radius | Sets the amount of rounding for bar corners, in pixels. The default value is *0* pixels, which produces square corners. |
| Bar Border Thickness | Sets the thickness of the bar border lines, in pixels, when the related Bar Border Color attribute has a value. The default value is 1 pixel. |
| Bar Thickness | Sets the width of the bar in pixels. If left blank, the width will be determined automatically. |
| Color | Sets the data region fill color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233. |
| Combine With Series ID | Set this attribute to the element ID of another series to combine it with this series in the legend. When two series are combined, by default only the first one will appear in the legend but clicking the item in the legend toggles both series to appear and disappear. Or, the value *Previous* can be entered to combine this series with the previous series. |
| Disable Bar Grouping | Disables grouping of side-by-side bars, when set to *True*. Bars that are not grouped are drawn individually and overlap each other. The default value is *False*. |
| Disable Mouse Tracking | Disables mouse tracking for the series, when set to *True*. This affects tooltips and click events on graphs and points. For large datasets, this may improve performance. The default value is *False*. |
| Hover Brightness | Specifies the amount to change a bar's color when the mouse pointer is hovered over it. Values can be between *0* (no change) and *15* (lighter). The default value is *2*. |
| Legend Label | Indicates text that will be shown for this series inside the chart legend. When a value is provided, automatically causes the legend to be displayed. |
| Line Color | Sets the data region's border line color. Enter a color by name, decimal RGB value, or hex RGB value. Prefix hex values with the pound sign, e.g. #112233. |
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

## Use Data Labels Element

A "data label" is text shown next to each data point that shows its value. When the **Data Labels** element is used as a child of Series.Bar Range, text representing the data values will appear on the chart:  

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771928855/introcccharts_54.png)

The Data Labels element has attributes that allow you to control the font family, color, size, and weight, the data format, border color, and positioning of the text.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771435287/notev11.3.png)The Data Labels element's color-related attribute values can be set using @Chart tokens.

## Use Quicktips Element

By default, a "quicktip" is displayed when the mouse hovers near or over a data point:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778738455/introcccharts_55.png)

The automatically-generated quicktip displays information for the X- and Y-axis, as shown above, left. However, you may want to display other information or format it differently, as shown above, right, which can be done by adding a **Quicktip** child element beneath Series.Bar Range.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778738711/introcccharts_56.png)

The example above shows a Quicktip element (no attributes need to be set) and three **Quicktip Row** child elements, used to create the quicktip shown in the previous image. Note that an @Chart token is used access the chart data.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771435287/notev11.3.png)Intrinsic functions are supported in the Quicktip attributes.

## Use Action Elements

Action elements initiate processing of a report or process task definition, redirection to a link, or other processing when a data point in the series is clicked.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771929111/introcccharts_56a.png)

In the example above, an **Action.Report** element has been added as a child of the Series, along with its **Target.Report** and **Link Parameters** child elements. To reference chart data in parameters, use the @Chart token, as shown above.

A variety of Action elements are available for use with Series, including Action.Link, Action.Process, and Action.Refresh Element. Additional Action elements will be added in future releases.

## Use Input Selection

This series can also be used with the **Input Selection** family of elements, which turn the chart into an input control. This allows users, at runtime, to select points or values on the chart with their mouse and your report can then take action using the selected data. This is very useful, for example, for drilling into the data.

For more information about this functionality, see [Input Selection](https://devnet.logianalytics.com/hc/en-us/articles/1500009514042-Input-Selection).
