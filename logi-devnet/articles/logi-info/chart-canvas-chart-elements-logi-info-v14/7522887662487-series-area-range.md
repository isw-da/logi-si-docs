---
title: "Series.Area Range"
id: 7522887662487
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/7522887662487-Series-Area-Range
updated_at: 2022-07-17T02:25:43Z
---

# Series.Area Range

# Series.Area Range

The Chart Canvas element's Series child elements cause a data visualization (the chart) to be rendered in the canvas.

The following topics discuss the Series.Area Range child element:

* [Using Multiple Series](https://devnet.logianalytics.com/hc/en-us/articles/7522868147735-Series-Area-Range-Using-Multiple-Series#Multiple)
* [Series.Area Range Attributes](https://devnet.logianalytics.com/hc/en-us/articles/7522904473239-Series-Area-Range-Attributes#Attributes)
* [Using the Data Labels Element](https://devnet.logianalytics.com/hc/en-us/articles/7522860216983-Series-Area-Range-Using-the-Data-Labels-Element#Labels)
* [Using the Quicktips Element](https://devnet.logianalytics.com/hc/en-us/articles/7522904556439-Series-Area-Range-Using-the-Quicktips-Element#Quicktips)
* [Using Action Elements](https://devnet.logianalytics.com/hc/en-us/articles/7522887668375-Series-Area-Range-Using-Action-Elements#Action)
* [Using Input Selection](https://devnet.logianalytics.com/hc/en-us/articles/7522887700503-Series-Area-Range-Using-Input-Selection#Selection)
* [Using the Refresh Series Timer](https://devnet.logianalytics.com/hc/en-us/articles/7522868162071-Series-Area-Range-Using-the-Refresh-Series-Timer#Timer)

## About Series.Area Range

The **Series.Area Range** element generates an Area Range chart, which is commonly used to represent sets of low and high values, as numbers or
percentages, over time.

![](https://devnet.logianalytics.com/hc/article_attachments/7522871677079/series_arearange_01.png)

The example above shows a simple Area Range chart, presenting the low and high temperatures for a month.

![](https://devnet.logianalytics.com/hc/article_attachments/7522866826903/series_arearange_02.png)

As shown above, the chart is created by adding Series.Area Range to the canvas, along with a datalayer. Very few attributes need to be set for this Series element in order to produce a basic chart.

![](https://devnet.logianalytics.com/hc/article_attachments/7522774430103/noteicon.jpg) A datalayer element can be used either beneath Series.Area Range, as shown above, or beneath Chart Canvas. If used as a child of Chart Canvas, its data is available to *all* child Series elements. This can improve performance if you have several series, all using the *same* data, beneath the same Chart Canvas element.

![](https://devnet.logianalytics.com/hc/article_attachments/7522852774935/series_arearange_03.png)

The properties of the X- and Y-axis, including captions, are set using the **X-Axis** and **Y-Axis** elements. For example, in order to provide a caption for the X-axis, add an **X-Axis** element beneath Chart Canvas and set its **Caption** attribute, as shown above. Repeat for the Y-axis.
