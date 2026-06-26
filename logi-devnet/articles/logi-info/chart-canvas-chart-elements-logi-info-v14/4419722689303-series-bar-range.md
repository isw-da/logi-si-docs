---
title: "Series.Bar Range"
id: 4419722689303
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722689303-Series-Bar-Range
updated_at: 2022-07-17T02:00:03Z
---

# Series.Bar Range

# Series.Bar Range

The Chart Canvas element's Series child elements cause a data visualization (the chart) to be rendered in the canvas.

The following topics discuss the Series.Bar Range child element:

* [Using Multiple Series](https://devnet.logianalytics.com/hc/en-us/articles/4419722691479-Series-Bar-Range-Using-Multiple-Series#Multiple)
* [Series.Bar Range Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419715123863-Series-Bar-Range-Attributes)
* [Using the Data Labels Element](https://devnet.logianalytics.com/hc/en-us/articles/4419722690455-Series-Bar-Range-Using-the-Data-Labels-Element#Labels)
* [Using the Quicktips Element](https://devnet.logianalytics.com/hc/en-us/articles/4419707359767-Series-Bar-Range-Using-the-Quicktips-Element#Quicktips)
* [Using Action Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419707357719-Series-Bar-Range-Using-Action-Elements#Action)
* [Using Input Selection](https://devnet.logianalytics.com/hc/en-us/articles/4419707358615-Series-Bar-Range-Using-Input-Selection#Selection)
* [Using the Refresh Series Timer](https://devnet.logianalytics.com/hc/en-us/articles/4419707360663-Series-Bar-Range-Using-the-Refresh-Series-Timer#Timer)

## About Series.Bar Range

The **Series.Bar Range** element generates a Bar Range chart, which is commonly used to represent separate events that have starting and ending values, over time.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706663319/series_barrange_01.png)

The example above shows a simple Bar Range chart, presenting daily low and high stock prices for a month.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714656791/series_barrange_02.png)

As shown above, the chart is created by adding Series.Bar Range to the canvas, along with a datalayer. Very few attributes need to be set for this Series element in order to produce a basic chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706629655/noteicon.jpg) A datalayer element can be used either beneath Series.Bar Range, as shown above, or beneath Chart Canvas. If used as a child of Chart Canvas, its data is available to *all* child Series elements. This can improve performance if you have several series, all using the *same* data, beneath the same Chart Canvas element.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706663703/series_barrange_03.png)

The properties of the X- and Y-axis, including captions, are set using the **X-Axis** and **Y-Axis** elements. For example, in order to provide a caption for the X-axis, add an **X-Axis** element beneath Chart Canvas and set its **Caption** attribute, as shown above. Repeat for the Y-axis.
