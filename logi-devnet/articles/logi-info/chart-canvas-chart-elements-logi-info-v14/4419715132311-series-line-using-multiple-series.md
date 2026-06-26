---
title: "Series.Line - Using Multiple Series"
id: 4419715132311
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715132311-Series-Line-Using-Multiple-Series
updated_at: 2022-07-17T02:25:09Z
---

# Series.Line - Using Multiple Series

# Series.Line - Using Multiple Series

You can add additional series to the chart by adding additional Series elements:

![](https://devnet.logianalytics.com/hc/article_attachments/7522832988311/series_line_04.png)

The example above shows three Series, one for each year, with a legend.

![](https://devnet.logianalytics.com/hc/article_attachments/7522863336599/series_line_05.png)

The example above shows the three Series elements, their datalayers, the X- and Y-Axis elements, and the **Legend** element used to produce the previous chart. You can adjust which series appears "in front" of the others in the chart by changing the order of the Series elements in the definition. Setting the Series elements' **Legend Label** attribute will automatically cause the legend to be displayed.

![](https://devnet.logianalytics.com/hc/article_attachments/7522818258455/series_line_06.png)

In order to produce the legend shown in the previous example, a **Legend** element must be added and its attributes configured as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 Charts with multiple series or aggregations are encouraged to use the ChartCanvas element's attribute, Tooltip Split. This attribute allows you to split a chart's tooltip into one label per series, rather than per segment. The default value for this attribute is False. Once enabled, when hovering over a data point, it displays all the values for the series. This method is recommended over shared tooltips for charts with multiple line series, and as such, takes precedence over tooltip.shared.

![](https://devnet.logianalytics.com/hc/article_attachments/7522774430103/noteicon.jpg) When using multiple series, you may be able to reduce the number of data queries and improve performance by using local data to read all of the data once, see [Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4419707706135-Datalayers). Then, link its datalayer to share it to the series, see [Link Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4419715407255-Link-Datalayers). At each Series element,
link its datalayer to the shared Local Data datalayer and filter the data to meet the needs of each individual series.

You can combine different types of Series elements, for example, Series.Line and Series.Bar, to produce combinations of visualizations.

## Forecasting

Forecasting elements use a variety of techniques to produce projected values by analyzing existing values. The future values they "predict" are, in most cases, added as rows or columns to a datalayer so the data can be displayed along with the existing data. When using Chart Canvas charts, the forecast data is typically displayed using a Series.Line element, in conjunction with other series elements.

![](https://devnet.logianalytics.com/hc/article_attachments/7522833002519/series_line_07.png)

Forecasting elements add a "forecast value" column to the datalayer, and this column is used as the series' Y-axis data column. For more information about using forecasting elements, see [The Forecasting Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419722922903-The-Forecasting-Elements).
