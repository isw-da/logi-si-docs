---
title: "Series.Pyramid - Using Multiple Series"
id: 4419707382551
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707382551-Series-Pyramid-Using-Multiple-Series
updated_at: 2022-07-17T01:58:46Z
---

# Series.Pyramid - Using Multiple Series

# Series.Pyramid - Using Multiple Series

Pyramid charts do not generally lend themselves to use with other series types, but it is possible. You can add additional series to the chart by adding additional Series elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699579031/series_pyramid_04.png)

The example above shows Series.Pyramid with Series.Line. The Pyramid's transparency has been set to allow the grid and data lines to show through it. In addition, the Pyramid's connector lines have been hidden and its labels offset to overlay the pyramid segments.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706674967/series_pyramid_05.png)

The example above shows the two Series elements and their datalayers, used to produce the previous chart. You can adjust which series appears "in front" of the other in the chart by changing the order of the Series elements in the definition. The Pyramid's **Transparency** attribute has been set to allow the grid and data lines to show through it.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706629655/noteicon.jpg) When using multiple series, you may be able to reduce the number of data queries and improve performance by using local data to read all of the data once, see [Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4419707706135-Datalayers). Then, link its datalayer to share it to the series, see [Link Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4419715407255-Link-Datalayers). At each Series element,
link its datalayer to the shared Local Data datalayer and filter the datato meet the needs of each individual series.
