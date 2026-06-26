---
title: "Series.Area Spline Range - Using Multiple Series"
id: 4419715118999
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715118999-Series-Area-Spline-Range-Using-Multiple-Series
updated_at: 2022-07-17T02:25:14Z
---

# Series.Area Spline Range - Using Multiple Series

# Series.Area Spline Range - Using Multiple Series

You can add additional series to the chart by adding additional Series elements:

![](https://devnet.logianalytics.com/hc/article_attachments/7522849563671/series_areasplinerange_04_557x393.png)

The example above shows two Series, one for each set of temperature ranges. A legend can also be added very easily.

![](https://devnet.logianalytics.com/hc/article_attachments/7522855606039/series_areasplinerange_05.png)

The example above shows the two Series elements, their datalayers and optional Quicktips, and the X-Axis and Y-Axis elements used to produce the previous chart. You can adjust which data range appears "in front" of the other in the chart by changing the order of the Series elements in the definition. Setting the Series elements' **Legend Label** attribute will automatically cause the legend to be displayed.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 Charts with multiple series or aggregations are encouraged to use the ChartCanvas element's attribute, Tooltip Split. This attribute allows you to split a chart's tooltip into one label per series, rather than per segment. The default value for this attribute is False. Once enabled, when hovering over a data point, it displays all the values for the series. This method is recommended over shared tooltips for charts with multiple line series, and as such, takes precedence over tooltip.shared.

![](https://devnet.logianalytics.com/hc/article_attachments/7522774430103/noteicon.jpg) When using multiple series, you may be able to reduce the number of data queries and improve performance by using local data to read all of the data once, see [Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4419707706135-Datalayers). Then, link its datalayer to share it to the series, see [Link Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4419715407255-Link-Datalayers). At each Series element,
link its datalayer to the shared Local Data datalayer and filter the data to meet the needs of each individual series.

You can combine different types of Series elements, for example, Series.Area and Series.Bar, to produce combinations of visualizations.
