---
title: "Series.Area Spline Range"
id: 4419707346711
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707346711-Series-Area-Spline-Range
updated_at: 2022-07-17T02:00:27Z
---

# Series.Area Spline Range

# Series.Area Spline Range

The Chart Canvas element's Series child elements cause a data visualization (the chart) to be rendered in the canvas.

The following topics discuss the Series.Area Spline Range child element:

* [Using Multiple Series](https://devnet.logianalytics.com/hc/en-us/articles/4419715118999-Series-Area-Spline-Range-Using-Multiple-Series#Multiple)
* [Series.Area Spline Range Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419707347607-Series-Area-Spline-Range-Attributes#Attributes)
* [Using the Data Labels Element](https://devnet.logianalytics.com/hc/en-us/articles/4419707348631-Series-Area-Spline-Range-Using-the-Data-Labels-Element#Labels)
* [Using the Quicktips Element](https://devnet.logianalytics.com/hc/en-us/articles/4419722683927-Series-Area-Spline-Range-Using-the-Quicktips-Element#Quicktips)
* [Using Action Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419722682647-Series-Area-Spline-Range-Using-Action-Elements#Action)
* [Using Input Selection](https://devnet.logianalytics.com/hc/en-us/articles/4419715117719-Series-Area-Spline-Range-Using-Input-Selection#Selection)
* [Using the Refresh Series Timer](https://devnet.logianalytics.com/hc/en-us/articles/4419707350679-Series-Area-Spline-Range-Using-the-Refresh-Series-Timer#Timer)

## About Series.Area Spline Range

The **Series.Area Spline Range** element generates an Area Spline Range chart, which is commonly used to represent sets of low and high values, as numbers or
percentages, over time.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714652951/series_areasplinerange_01.png)

The example above shows a simple Area Spline Range chart, presenting the low and high temperatures for a month.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699558039/series_areasplinerange_02.png)

As shown above, the chart is created by adding Series.Area Spline Range to the canvas, along with a datalayer. Very few attributes need to be set for this Series element in order to produce a basic chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706629655/noteicon.jpg) A datalayer element can be used either beneath Series.Area Spline Range, as shown above, or beneath Chart Canvas. If used as a child of Chart Canvas, its data is available to *all* child Series elements. This can improve performance if you have several series, all using the *same* data, beneath the same Chart Canvas element.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699558295/series_areasplinerange_03.png)

The properties of the X- and Y-axis, including captions, are set using the **X-Axis** and **Y-Axis** elements. For example, in order to provide a caption for the X-axis, add an **X-Axis** element beneath Chart Canvas and set its **Caption** attribute, as shown above. Repeat for the Y-axis.
