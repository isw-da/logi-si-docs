---
title: "Showing Totals for Stacked Series"
id: 4406817152663
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817152663-Showing-Totals-for-Stacked-Series
updated_at: 2022-04-06T06:04:21Z
---

# Showing Totals for Stacked Series

# Showing Totals for Stacked Series

When multiple Series are used and stacked, the Data Labels element can be used to display the individual data values. However, what if you want to display a *total* of the stacked values?

![](https://devnet.logianalytics.com/hc/article_attachments/4417563492375/introcccharts_108.png)

The examples above illustrates the first scenario: Data Labels elements used beneath its Series.Bar elements, resulting in individual values being displayed within the bars.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584118295/introcccharts_109.png)

However, if you don't use Data Labels but instead use a Y-Axis element and its **Stack Labels** child element, the stacked values will be totaled and displayed above the bars, as shown above. The Stack Labels element allows you to configure the font-related, format, and positioning attributes of the total text.
