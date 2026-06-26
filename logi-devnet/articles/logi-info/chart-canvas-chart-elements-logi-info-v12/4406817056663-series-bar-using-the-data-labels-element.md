---
title: "Series.Bar - Using the Data Labels Element"
id: 4406817056663
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817056663-Series-Bar-Using-the-Data-Labels-Element
updated_at: 2022-04-06T06:03:38Z
---

# Series.Bar - Using the Data Labels Element

# Series.Bar - Using the Data Labels Element

A "data label" is text shown near each data point that shows its value. When the **Data Labels** element is used as a child of Series.Bar, text representing the data values will appear on the chart:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584148887/series_bar_07.png)

By default, with a single data series, the data labels will appear outside the bar, as shown above, left. The Data Labels element has attributes that allow you to control the font family, color, size, and weight, the data format, border color, and positioning of the text. The example above, right, shows data labels placed inside the bars and rotated 90-degrees. When series stacking is being used, the default is for data labels to appear *inside* the bars.

The Data Labels element's color-related attribute values can be set using @Chart tokens.
