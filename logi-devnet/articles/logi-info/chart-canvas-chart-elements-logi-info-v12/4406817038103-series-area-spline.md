---
title: "Series.Area Spline"
id: 4406817038103
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817038103-Series-Area-Spline
updated_at: 2022-04-06T06:03:30Z
---

# Series.Area Spline

# Series.Area Spline

The Chart Canvas element's Series child elements cause a data visualization (the chart) to be rendered in the canvas.

The following topics discuss the Series.Area Spline child element:

* [Using Multiple Series](https://devnet.logianalytics.com/hc/en-us/articles/4406817043351-Series-Area-Spline-Using-Multiple-Series#Multiple)
* [Series.Area Spline Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4406817039127-Series-Area-Spline-Attributes#Attributes)
* [Using the Data Labels Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817040279-Series-Area-Spline-Using-the-Data-Label-Element#Labels)
* [Using the Marker Points Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817042327-Series-Area-Spline-Using-the-Marker-Points-Element#Points)
* [Using the Quicktips Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817044375-Series-Area-Spline-Using-the-Quicktips-Element#Quicktips)
* [Using the Trend Line Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817045527-Series-Area-Spline-Using-the-Trend-Line-Element#Trend)
* [Using Action Elements](https://devnet.logianalytics.com/hc/en-us/articles/4406822115479-Series-Area-Spline-Using-Action-Elements#Action)
* [Using Input Selection](https://devnet.logianalytics.com/hc/en-us/articles/4406817041303-Series-Area-Spline-Using-Input-Selection#Selection)
* [Using the Refresh Series Timer](https://devnet.logianalytics.com/hc/en-us/articles/4406822116375-Series-Area-Spline-Using-the-Refresh-Series-Timer#Timer)

## About Series.Area Spline

The **Series.Area Spline** element generates an Area chart with the characteristic curves of a Spline chart, which is commonly used to represent aggregated totals, as numbers or
percentages, over time.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575897495/series_areaspline_01.png)

The example above shows a simple Area Spline chart, representing sales per month for a year. Notice that, unlike a regular Area chart, the data region border is smoothly curved.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584159767/series_areaspline_02.png)

As shown above, the chart is created by adding Series.Area Spline to the canvas, along with a datalayer and, typically, some child elements that may include **Time Period Column** elements, a **Group Filter**, and a **Group Aggregate Column** element. Very few attributes need to be set for the Series element in order to produce a basic chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) A datalayer element can be used either beneath Series.Area Spline, as shown above, or beneath Chart Canvas. If used as a child of Chart Canvas, its data is available to *all* child Series elements. This can improve performance if you have several series, all using the *same* data, beneath the same Chart Canvas element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584160023/series_areaspline_03.png)

The properties of the X- and Y-axis, including captions, are set using the **X-Axis** and **Y-Axis** elements. For example, in order to angle the X-axis labels, add an X-Axis element beneath Chart Canvas (none of its attributes need to be set) and add its child **Label Style** element. Set the Label Style element's attribute as shown above.
