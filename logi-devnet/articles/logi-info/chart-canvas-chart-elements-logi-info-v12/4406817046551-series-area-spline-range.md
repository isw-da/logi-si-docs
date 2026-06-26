---
title: "Series.Area Spline Range"
id: 4406817046551
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817046551-Series-Area-Spline-Range
updated_at: 2022-04-06T06:03:34Z
---

# Series.Area Spline Range

# Series.Area Spline Range

The Chart Canvas element's Series child elements cause a data visualization (the chart) to be rendered in the canvas.

The following topics discuss the Series.Area Spline Range child element:

* [Using Multiple Series](https://devnet.logianalytics.com/hc/en-us/articles/4406817051031-Series-Area-Spline-Range-Using-Multiple-Series#Multiple)
* [Series.Area Spline Range Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4406817047575-Series-Area-Spline-Range-Attributes#Attributes)
* [Using the Data Labels Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817049623-Series-Area-Spline-Range-Using-the-Data-Labels-Element#Labels)
* [Using the Quicktips Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817052055-Series-Area-Spline-Range-Using-the-Quicktips-Element#Quicktips)
* [Using Action Elements](https://devnet.logianalytics.com/hc/en-us/articles/4406817048599-Series-Area-Spline-Range-Using-Action-Elements#Action)
* [Using Input Selection](https://devnet.logianalytics.com/hc/en-us/articles/4406822120215-Series-Area-Spline-Range-Using-Input-Selection#Selection)
* [Using the Refresh Series Timer](https://devnet.logianalytics.com/hc/en-us/articles/4406822121111-Series-Area-Spline-Range-Using-the-Refresh-Series-Timer#Timer)

## About Series.Area Spline Range

The **Series.Area Spline Range** element generates an Area Spline Range chart, which is commonly used to represent sets of low and high values, as numbers or
percentages, over time.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575894039/series_areasplinerange_01.png)

The example above shows a simple Area Spline Range chart, presenting the low and high temperatures for a month.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584153111/series_areasplinerange_02.png)

As shown above, the chart is created by adding Series.Area Spline Range to the canvas, along with a datalayer. Very few attributes need to be set for this Series element in order to produce a basic chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) A datalayer element can be used either beneath Series.Area Spline Range, as shown above, or beneath Chart Canvas. If used as a child of Chart Canvas, its data is available to *all* child Series elements. This can improve performance if you have several series, all using the *same* data, beneath the same Chart Canvas element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575894423/series_areasplinerange_03.png)

The properties of the X- and Y-axis, including captions, are set using the **X-Axis** and **Y-Axis** elements. For example, in order to provide a caption for the X-axis, add an **X-Axis** element beneath Chart Canvas and set its **Caption** attribute, as shown above. Repeat for the Y-axis.
