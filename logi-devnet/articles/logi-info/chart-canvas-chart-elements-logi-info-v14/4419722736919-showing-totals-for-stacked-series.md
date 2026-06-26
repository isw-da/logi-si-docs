---
title: "Showing Totals for Stacked Series"
id: 4419722736919
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722736919-Showing-Totals-for-Stacked-Series
updated_at: 2022-07-17T02:25:03Z
---

# Showing Totals for Stacked Series

# Showing Totals for Stacked Series

When multiple Series are used and stacked, the Data Labels element can be used to display the individual data values. However, what if you want to display a *total* of the stacked values?

The examples below illustrates the first scenario: Data Labels elements used beneath its Series.Bar elements, resulting in individual values being displayed within the bars.

![](https://devnet.logianalytics.com/hc/article_attachments/7522854712343/introcccharts_108.png)  

![](https://devnet.logianalytics.com/hc/article_attachments/7522774430103/noteicon.jpg)![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 One Data Labels element attribute, Series Name as Caption, allows you to specify the y-axis label, x-axis label, or legend label as the data point value inside the chart.

However, if you don't use Data Labels but instead use a Y-Axis element and its **Stack Labels** child element, the stacked values will be totaled and displayed above the bars, as shown below. The Stack Labels element allows you to configure the font-related, format, and positioning attributes of the total text.

![](https://devnet.logianalytics.com/hc/article_attachments/7522854720023/introcccharts_109.png)
