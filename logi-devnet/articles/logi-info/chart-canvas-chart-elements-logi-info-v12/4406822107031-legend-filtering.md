---
title: "Legend Filtering"
id: 4406822107031
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822107031-Legend-Filtering
updated_at: 2022-04-06T06:03:24Z
---

# Legend Filtering

# Legend Filtering

Legend "filtering" allows users to toggle the display of series at runtime, by clicking on legend items:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584168471/introcccharts_08.png)

When legend items are selected, the Chart Canvas element refreshes and changes the other appropriate legend objects' color attributes from HEX codes to "CCC", creating a greyed-out appearance. In the example above, the 2012 series is hidden by clicking its legend item. Clicking again will redisplay the series.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png) By default, the legend filtering is set to "Show All," and in turn, the Show All feature is greyed out. As you select legend items to display in the chart, the Show All legend object will redisplay and become actionable:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563108631/show_all_caption_642x396.png)

Legend filtering is a standard feature that's always enabled.

## Legend Item Order

The top-to-bottom order of the items in the legend, by default, is the same as the order of the Series elements in the report definition. This order can be reversed by setting the Legend element's **Reversed Item Order** attribute to *True*.
