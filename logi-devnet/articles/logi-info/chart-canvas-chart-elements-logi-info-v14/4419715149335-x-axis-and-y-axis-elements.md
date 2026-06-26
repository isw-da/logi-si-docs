---
title: "X-Axis and Y-Axis Elements"
id: 4419715149335
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715149335-X-Axis-and-Y-Axis-Elements
updated_at: 2022-07-17T01:57:51Z
---

# X-Axis and Y-Axis Elements

# X-Axis and Y-Axis Elements

When the Chart Canvas element renders charts that use Cartesian coordinates, an X-axis and a Y-axis are drawn on the chart.

The following topics discuss how these axes can be configured:

* [Axis Element Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419722735767-Axis-Element-Attributes#Attributes)
* [Plotting Negative Values](https://devnet.logianalytics.com/hc/en-us/articles/4419707404183-Plotting-Negative-Values#NegValues)
* [Styling the Axis Caption](https://devnet.logianalytics.com/hc/en-us/articles/4419715150487-Styling-the-Axis-Caption#Caption)
* [Styling the Axis Labels](https://devnet.logianalytics.com/hc/en-us/articles/4419715151383-Styling-the-Axis-Labels#Labels)
* [Adding a Marker Line](https://devnet.logianalytics.com/hc/en-us/articles/4419722734871-Adding-a-Marker-Line#Line)
* [Adding a Marker Band](https://devnet.logianalytics.com/hc/en-us/articles/4419707400343-Adding-a-Marker-Band#Band)
* [Configuring Major Ticks and Grid Lines](https://devnet.logianalytics.com/hc/en-us/articles/4419707402391--Heading-Level1-#Major)
* [Configuring Minor Ticks and Grid Lines](https://devnet.logianalytics.com/hc/en-us/articles/4419707403287-Configuring-Minor-Ticks-and-Grid-Lines#Minor)
* [Showing Totals for Stacked Series](https://devnet.logianalytics.com/hc/en-us/articles/4419722736919-Showing-Totals-for-Stacked-Series#Stacked)
* [Adding Multiple Axes](https://devnet.logianalytics.com/hc/en-us/articles/4419707401367-Adding-Multiple-Axes#Multiple)

## About the Axis Elements

When a chart uses Cartesian coordinates, the X- and Y-axes provide the two references used by the eye to compare data values. Though they can be reversed, we generally think of the X-axis as the "label" and the Y-axis as the "data value".

![](https://devnet.logianalytics.com/hc/article_attachments/4419699587735/introcccharts_99.png)

You can think of them as an "overlay" on the canvas, providing the reference points over which the data values will be drawn. The **X-Axis** and **Y-Axis** elements are children of the Chart Canvas and can be used to control a variety of visual elements in the chart associated with the axes.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706629655/noteicon.jpg) A Chart Canvas element will draw an X- and Y-axis by default; the X-Axis and Y-Axis elements are only needed if you want to customize the axis.
