---
title: "Series.Bar - Using the Quicktips Element"
id: 4406817058199
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817058199-Series-Bar-Using-the-Quicktips-Element
updated_at: 2022-04-06T06:03:37Z
---

# Series.Bar - Using the Quicktips Element

# Series.Bar - Using the Quicktips Element

By default, a "quicktip" is displayed when the mouse hovers near or over a data point:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584147991/series_bar_08.png)

The automatically-generated quicktip displays information for the X- and Y-axis, as shown above, left. However, you may want to display other information or format it differently, perhaps as shown above, right, which can be done by adding a **Quicktip** child element beneath Series.Bar and setting its attributes and child elements. Use @Chart tokens to include chart data in the quicktip.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563531927/series_bar_09.png)

When using stacked series, if each series has its own Quicktips child element, the data shown in the quicktip will vary depending on which stacked segment the cursor hovers over, as shown above.
Intrinsic functions are supported in the Quicktip attributes.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png) To display a percentage for each bar in a Stacked Bar Chart, use the special token *@Chart.rdStackedChartPercentage~*, like below:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575891095/stacked_chart_percentage1.png)

This feature enables the user to hover over the stacked bars and show the percentage for each value. The Title attribute can be used to distinguish between values in a stacked chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The format of the percentage will display according to the Format property in QuickTipRow. If this format is not set, it will display the default format "Percent" (0.000%).
