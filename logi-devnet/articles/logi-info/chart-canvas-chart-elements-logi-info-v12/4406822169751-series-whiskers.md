---
title: "Series.Whiskers"
id: 4406822169751
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822169751-Series-Whiskers
updated_at: 2022-04-06T06:04:16Z
---

# Series.Whiskers

# Series.Whiskers

The Chart Canvas element's Series child elements cause a data visualization (the chart) to be rendered in the canvas.

The following topics discuss the Series.Whiskers child element:

* [Series.Whiskers](https://devnet.logianalytics.com/hc/en-us/articles/4406817136535-Series-Whiskers-Attributes) [Attributes](#Attributes)
* [Using the Quicktips Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817139095-Series-Whiskers-Using-the-Quicktips-Element#Quicktips)
* [Using Action Elements](https://devnet.logianalytics.com/hc/en-us/articles/4406822171031-Series-Whiskers-Using-Action-Elements#Action)
* [Using the Refresh Series Timer](https://devnet.logianalytics.com/hc/en-us/articles/4406817140119-Series-Whiskers-Using-the-Refresh-Series-Timer#Timer)

## About Series.Whiskers

The **Series.Whiskers** elementgenerates graphics which, when used with other Series (usually Series.Bar Range), represents the *variability* of the data. It's most often used to indicate the uncertainty or the "margin of error" in the data.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563498391/series_whiskers_01.png)

The example above shows a Bar Range chart, representing projected stock prices for a month, with "whiskers" showing the margin of error in the projections.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584124439/series_whiskers_02.png)

As shown above, the chart is created by adding Series.Bar Range and Series.Whiskers to the canvas, along with a datalayer and, typically, some datalayer child elements that may include a **Group Filter**, and a **Group Aggregate Column** element. Very few attributes need to be set for the Series element in order to produce a basic chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) A datalayer element *must* be used beneath the Chart Canvas element because, unlike other Series elements, Series.Whiskers cannot have its own child datalayer. Both series will then use this datalayer.
