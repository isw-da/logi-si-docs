---
title: "Series.Bubble - Using Multiple Series"
id: 4406817070871
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817070871-Series-Bubble-Using-Multiple-Series
updated_at: 2022-04-06T06:03:47Z
---

# Series.Bubble - Using Multiple Series

# Series.Bubble - Using Multiple Series

You can add additional series to the chart by adding additional Series
elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584144407/series_bubble_04.png)

The example above shows two Series, one for each year, with a legend.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563527191/series_bubble_05.png)

The example above shows the two Series elements, their datalayers, and
**X-** and **Y-Axis** elements used to produce the previous chart.
Should they overlap, you can adjust which bubbles appear "in
front" of the others in the chart by changing the order of the Series
elements in the definition. Setting the Series elements'
**Legend Label** attribute will automatically cause the legend to be
displayed.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) When using multiple series, you may be able to reduce the number of data queries and improve performance by using local data to read all of the data once, see [Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4406817655319-Datalayers). Then, link its datalayer to share it to the series, see [Link Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4406822443671-Link-Datalayers). At each Series element, link its datalayer to the
shared Local Data datalayer and filter the data to meet the needs of each
individual series. You can combine different types of Series elements, for
example, Series.Bubble and Series.Line, to produce combinations of
visualizations.
