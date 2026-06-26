---
title: "Series.Funnel - Using Multiple Series"
id: 4406817076375
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817076375-Series-Funnel-Using-Multiple-Series
updated_at: 2022-04-06T06:03:52Z
---

# Series.Funnel - Using Multiple Series

# Series.Funnel - Using Multiple Series

Funnel charts do not generally lend themselves to use with other series types, but it is possible. You can add additional series to the chart by adding additional Series elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584142359/series_funnel_04.png)

The example above shows Series.Funnel with Series.Line. The funnel's transparency has been set to allow the grid and data lines to show through it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575887255/series_funnel_05.png)

The example above shows the two Series elements and their datalayers, used to produce the previous chart. You can adjust which series appears "in front" of the other in the chart by changing the order of the Series elements in the definition. The funnel's **Transparency** attribute has been set to allow the grid and data lines to show through it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) When using multiple series, you may be able to reduce the number of data queries and improve performance by using local data to read all of the data once, see [Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4406817655319-Datalayers). Then, link its datalayer to share it to the series, see [Link Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4406822443671-Link-Datalayers). At each Series element,
link its datalayer to the shared Local Data datalayer and filter the datato meet the needs of each individual series.
