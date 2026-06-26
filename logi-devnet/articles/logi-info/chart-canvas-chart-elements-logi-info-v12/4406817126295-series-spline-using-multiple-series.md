---
title: "Series.Spline - Using Multiple Series "
id: 4406817126295
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817126295-Series-Spline-Using-Multiple-Series
updated_at: 2022-04-06T06:04:12Z
---

# Series.Spline - Using Multiple Series 

# Series.Spline - Using Multiple Series

You can add additional series to the chart by adding additional Series elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575867031/series_spline_04.png)

The example above shows three Series, one for each year, with a legend.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563500567/series_spline_05.png)

The example above shows the three Series elements, their datalayers, the X- and Y-Axis elements, and the **Legend** element used to produce the previous chart. You can adjust which series appears "in front" of the others in the chart by changing the order of the Series elements in the definition. Setting the Series elements' **Legend Label** attribute will automatically cause the legend to be displayed.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) When using multiple series, you may be able to reduce the number of data queries and improve performance by using local data to read all of the data once, see [Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4406817655319-Datalayers). Then, link its datalayer to share it to the series, see [Link Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4406822443671-Link-Datalayers). At each Series element,
link its datalayer to the shared Local Data datalayer and filter the data to meet the needs of each individual series.

You can combine different types of Series elements, for example, Series.Spline and Series.Bar, to produce combinations of visualizations.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563500695/series_spline_06.png)

In order to produce the legend shown in the previous example, a **Legend** element must be added and its attributes configured as shown above.
