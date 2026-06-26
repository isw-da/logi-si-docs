---
title: "Series.Area Spline"
id: 4419715111063
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715111063-Series-Area-Spline
updated_at: 2022-07-17T02:00:40Z
---

# Series.Area Spline

# Series.Area Spline

The Chart Canvas element's Series child elements cause a data visualization (the chart) to be rendered in the canvas.

The following topics discuss the Series.Area Spline child element:

* [Using Multiple Series](https://devnet.logianalytics.com/hc/en-us/articles/4419722681367-Series-Area-Spline-Using-Multiple-Series#Multiple)
* [Series.Area Spline Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419722679063-Series-Area-Spline-Attributes#Attributes)
* [Using the Data Labels Element](https://devnet.logianalytics.com/hc/en-us/articles/4419707343767-Series-Area-Spline-Using-the-Data-Label-Element#Labels)
* [Using the Marker Points Element](https://devnet.logianalytics.com/hc/en-us/articles/4419707344663-Series-Area-Spline-Using-the-Marker-Points-Element#Points)
* [Using the Quicktips Element](https://devnet.logianalytics.com/hc/en-us/articles/4419715115671-Series-Area-Spline-Using-the-Quicktips-Element#Quicktips)
* [Using the Trend Line Element](https://devnet.logianalytics.com/hc/en-us/articles/4419707345815-Series-Area-Spline-Using-the-Trend-Line-Element#Trend)
* [Using Action Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419707342743-Series-Area-Spline-Using-Action-Elements#Action)
* [Using Input Selection](https://devnet.logianalytics.com/hc/en-us/articles/4419722680087-Series-Area-Spline-Using-Input-Selection#Selection)
* [Using the Refresh Series Timer](https://devnet.logianalytics.com/hc/en-us/articles/4419715116567-Series-Area-Spline-Using-the-Refresh-Series-Timer#Timer)

## About Series.Area Spline

The **Series.Area Spline** element generates an Area chart with the characteristic curves of a Spline chart, which is commonly used to represent aggregated totals, as numbers or
percentages, over time.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699555863/series_areaspline_01.png)

The example above shows a simple Area Spline chart, representing sales per month for a year. Notice that, unlike a regular Area chart, the data region border is smoothly curved.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714652695/series_areaspline_02.png)

As shown above, the chart is created by adding Series.Area Spline to the canvas, along with a datalayer and, typically, some child elements that may include **Time Period Column** elements, a **Group Filter**, and a **Group Aggregate Column** element. Very few attributes need to be set for the Series element in order to produce a basic chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706629655/noteicon.jpg) A datalayer element can be used either beneath Series.Area Spline, as shown above, or beneath Chart Canvas. If used as a child of Chart Canvas, its data is available to *all* child Series elements. This can improve performance if you have several series, all using the *same* data, beneath the same Chart Canvas element.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706657943/series_areaspline_03.png)

The properties of the X- and Y-axis, including captions, are set using the **X-Axis** and **Y-Axis** elements. For example, in order to angle the X-axis labels, add an X-Axis element beneath Chart Canvas (none of its attributes need to be set) and add its child **Label Style** element. Set the Label Style element's attribute as shown above.
