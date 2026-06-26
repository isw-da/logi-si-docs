---
title: "Series.Area Range - Using Multiple Series"
id: 4406822155543
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822155543-Series-Area-Range-Using-Multiple-Series
updated_at: 2022-04-06T06:04:06Z
---

# Series.Area Range - Using Multiple Series

# Series.Area Range - Using Multiple Series

You can add additional series to the chart by adding additional Series elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584130199/series_arearange_04.png)

The example above shows two Series, one for each set of temperature ranges. A legend can also be added very easily.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584130327/series_arearange_05.png)

The example above shows the two Series elements, their datalayers and optional Quicktips, and the X-Axis and Y-Axis elements used to produce the previous chart. You can adjust which data range appears "in front" of the other in the chart by changing the order of the Series elements in the definition. Setting the Series elements' **Legend Label** attribute will automatically cause the legend to be displayed.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) When using multiple series, you may be able to reduce the number of data queries and improve performance by using local data to read all of the data once, see [Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4406817655319-Datalayers). Then, link its datalayer to share it to the series, see [Link Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4406822443671-Link-Datalayers). At each Series element,
link its datalayer to the shared Local Data datalayer and filter the data to meet the needs of each individual series.

You can combine different types of Series elements, for example, Series.Area and Series.Bar, to produce combinations of visualizations.
