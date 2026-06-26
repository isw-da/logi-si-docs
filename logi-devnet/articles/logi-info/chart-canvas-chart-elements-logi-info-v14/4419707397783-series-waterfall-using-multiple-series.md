---
title: "Series.Waterfall - Using Multiple Series"
id: 4419707397783
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707397783-Series-Waterfall-Using-Multiple-Series
updated_at: 2022-07-17T02:25:05Z
---

# Series.Waterfall - Using Multiple Series

# Series.Waterfall - Using Multiple Series

Waterfall charts do not generally lend themselves to use with other series types, but it is possible. You can add additional series to the chart by adding additional Series elements:

![](https://devnet.logianalytics.com/hc/article_attachments/7522848719383/series_waterfall_03.png)

The example above shows Series.Waterfall with Series.Line. The series have been linked to two separate Y-axis elements to provide two separate scales.

![](https://devnet.logianalytics.com/hc/article_attachments/7522832745111/series_waterfall_04.png)

The example above shows the two Series elements and their datalayers, used to produce the previous chart. You can adjust which series appears "in front" of the other in the chart by changing the order of the Series elements in the definition. The Line series has been linked to one of the two Y-Axis elements, creating a secondary scale on the right-hand side.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 Charts with multiple series or aggregations are encouraged to use the ChartCanvas element's attribute, Tooltip Split. This attribute allows you to split a chart's tooltip into one label per series, rather than per segment. The default value for this attribute is False. Once enabled, when hovering over a data point, it displays all the values for the series. This method is recommended over shared tooltips for charts with multiple line series, and as such, takes precedence over tooltip.shared.

![](https://devnet.logianalytics.com/hc/article_attachments/7522774430103/noteicon.jpg) When using multiple series, you may be able to reduce the number of data queries and improve performance by using local data to read all of the data once, see [Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4419707706135-Datalayers). Then, link its datalayer to share it to the series, see [Link Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4419715407255-Link-Datalayers). At each Series element,
link its datalayer to the shared Local Data datalayer and filter the datato meet the needs of each individual series.
