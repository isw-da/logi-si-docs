---
title: "X-Axis and Y-Axis Elements"
id: 4406817147799
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817147799-X-Axis-and-Y-Axis-Elements
updated_at: 2022-04-06T06:04:17Z
---

# X-Axis and Y-Axis Elements

# X-Axis and Y-Axis Elements

When the Chart Canvas element renders charts that use Cartesian coordinates, an X-axis and a Y-axis are drawn on the chart.

The following topics discuss how these axes can be configured:

* [Axis Element Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4406817146647-Axis-Element-Attributes#Attributes)
* [Plotting Negative Values](https://devnet.logianalytics.com/hc/en-us/articles/4406817151255-Plotting-Negative-Values#NegValues)
* [Styling the Axis Caption](https://devnet.logianalytics.com/hc/en-us/articles/4406817153687-Styling-the-Axis-Caption#Caption)
* [Styling the Axis Labels](https://devnet.logianalytics.com/hc/en-us/articles/4406822174871-Styling-the-Axis-Labels#Labels)
* [Adding a Marker Line](https://devnet.logianalytics.com/hc/en-us/articles/4406822173079-Adding-a-Marker-Line#Line)
* [Adding a Marker Band](https://devnet.logianalytics.com/hc/en-us/articles/4406817143319-Adding-a-Marker-Band#Band)
* [Configuring Major Ticks and Grid Lines](https://devnet.logianalytics.com/hc/en-us/articles/4406817148823-Configuring-Major-Ticks-and-Grid-Lines#Major)
* [Configuring Minor Ticks and Grid Lines](https://devnet.logianalytics.com/hc/en-us/articles/4406817149847-Configuring-Minor-Ticks-and-Grid-Lines#Minor)
* [Showing Totals for Stacked Series](https://devnet.logianalytics.com/hc/en-us/articles/4406817152663-Showing-Totals-for-Stacked-Series#Stacked)
* [Adding Multiple Axes](https://devnet.logianalytics.com/hc/en-us/articles/4406817145495-Adding-Multiple-Axes#Multiple)

## About the Axis Elements

When a chart uses Cartesian coordinates, the X- and Y-axes provide the two references used by the eye to compare data values. Though they can be reversed, we generally think of the X-axis as the "label" and the Y-axis as the "data value".

![](https://devnet.logianalytics.com/hc/article_attachments/4417563493527/introcccharts_99.png)

You can think of them as an "overlay" on the canvas, providing the reference points over which the data values will be drawn. The **X-Axis** and **Y-Axis** elements are children of the Chart Canvas and can be used to control a variety of visual elements in the chart associated with the axes.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) A Chart Canvas element will draw an X- and Y-axis by default; the X-Axis and Y-Axis elements are only needed if you want to customize the axis.
