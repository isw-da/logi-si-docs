---
title: "Series.Pie - Using Multiple Series"
id: 4419722711063
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722711063-Series-Pie-Using-Multiple-Series
updated_at: 2022-07-17T01:58:56Z
---

# Series.Pie - Using Multiple Series

# Series.Pie - Using Multiple Series

Just as it is with other Series, it's possible to add multiple Pie charts to one Chart Canvas.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699577239/series_pie_07.png)

Overlaying Pie charts can produce "visual clutter" that's hard to decipher (and that's without any data labels displayed), as you can see in the example above, left. In the example above, right, however, the second Series has been configured so that it's off center, using its **Center X** and **Center Y** attributes, which provides a little more clarity.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706629655/noteicon.jpg) When using multiple series, you may be able to reduce the number of data queries and improve performance by using local data to read all of the data once, see [Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4419707706135-Datalayers). Then, link its datalayer to share it to the series, see [Link Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4419715407255-Link-Datalayers). At each Series element,
link its datalayer to the shared Local Data datalayer and filter the data to meet the needs of each individual series.

You can combine different types of Series elements, for example, Series.Pie and Series.Line, to produce combinations of visualizations.
