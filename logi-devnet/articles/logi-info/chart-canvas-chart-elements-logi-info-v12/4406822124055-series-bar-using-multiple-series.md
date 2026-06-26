---
title: "Series.Bar - Using Multiple Series"
id: 4406822124055
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822124055-Series-Bar-Using-Multiple-Series
updated_at: 2022-04-06T06:03:38Z
---

# Series.Bar - Using Multiple Series

# Series.Bar - Using Multiple Series

You can add additional series to the chart by adding additional Series elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584148503/series_bar_04.png)
+

The example above uses three Series, one for each year, and two different "stacking modes" are shown, along with a legend. *Overlay* and *StackedPercentage* stacking modes are also available. Combinations of stacking modes are also possible, for example, two years stacked, and one year beside them.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The scaling of the data axis may change depending on the stacking mode.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575891351/series_bar_05.png)

The example above shows the two Series elements, their datalayers, and an X-Axis element used to produce the previous chart. You can adjust the order of the series in the chart and the legend by changing the order of the Series elements in the definition. Setting the Series elements' **Legend Label** attribute will automatically cause the legend to be displayed.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) When using multiple series, you may be able to reduce the number of data queries and improve performance by using local data to read all of the data once, see [Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4406817655319-Datalayers). Then, link its datalayer to share it to the series, see [Link Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4406822443671-Link-Datalayers). At each Series element,
link its datalayer to the shared Local Data datalayer and filter the data to meet the needs of each individual series.

You can combine different types of Series elements, for example, Series.Bar and Series.Line, to produce combinations of visualizations. A good example of this is when you wish to use forecasting.

## Forecasting

Forecasting elements use a variety of techniques to produce projected values by analyzing existing values. The future values they "predict" are, in most cases, added as rows or columns to a datalayer so the data can be displayed along with the existing data. When using Chart Canvas charts, the forecast data is typically displayed using a Series.Line element, in conjunction with other series elements.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584148759/series_bar_06.png)

Forecasting elements add a "forecast value" column to the datalayer, and this column is used as the series' Y-axis data column. For more information about using forecasting elements, see [The Forecasting Elements](https://devnet.logianalytics.com/hc/en-us/articles/4406822338967-The-Forecasting-Elements).
