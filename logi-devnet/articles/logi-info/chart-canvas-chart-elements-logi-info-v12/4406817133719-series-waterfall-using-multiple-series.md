---
title: "Series.Waterfall - Using Multiple Series"
id: 4406817133719
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817133719-Series-Waterfall-Using-Multiple-Series
updated_at: 2022-04-06T06:04:14Z
---

# Series.Waterfall - Using Multiple Series

# Series.Waterfall - Using Multiple Series

Waterfall charts do not generally lend themselves to use with other series types, but it is possible. You can add additional series to the chart by adding additional Series elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584125079/series_waterfall_03.png)

The example above shows Series.Waterfall with Series.Line. The series have been linked to two separate Y-axis elements to provide two separate scales.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584125207/series_waterfall_04.png)

The example above shows the two Series elements and their datalayers, used to produce the previous chart. You can adjust which series appears "in front" of the other in the chart by changing the order of the Series elements in the definition. The Line series has been linked to one of the two Y-Axis elements, creating a secondary scale on the right-hand side.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) When using multiple series, you may be able to reduce the number of data queries and improve performance by using local data to read all of the data once, see [Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4406817655319-Datalayers). Then, link its datalayer to share it to the series, see [Link Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4406822443671-Link-Datalayers). At each Series element,
link its datalayer to the shared Local Data datalayer and filter the datato meet the needs of each individual series.
