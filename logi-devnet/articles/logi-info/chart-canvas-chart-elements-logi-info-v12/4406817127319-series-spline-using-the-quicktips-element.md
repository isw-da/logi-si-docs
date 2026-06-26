---
title: "Series.Spline - Using the Quicktips Element"
id: 4406817127319
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817127319-Series-Spline-Using-the-Quicktips-Element
updated_at: 2022-04-06T06:04:11Z
---

# Series.Spline - Using the Quicktips Element

# Series.Spline - Using the Quicktips Element

By default, a "quicktip" is displayed when the mouse hovers near or over a data point:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563500439/series_spline_09.png)

The automatically-generated quicktip displays information for the X- and Y-axis, as shown above, left. However, you may want to display other information or format it differently, perhaps as shown above, right, which can be done by adding a **Quicktip** child element beneath Series.Spline and setting its attributes and child elements. Use @Chart tokens to include chart data in the quicktip.
Intrinsic functions are supported in the Quicktip attributes.
