---
title: "Series.Whiskers - Using the Quicktips Element"
id: 4406817139095
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817139095-Series-Whiskers-Using-the-Quicktips-Element
updated_at: 2022-04-06T06:04:16Z
---

# Series.Whiskers - Using the Quicktips Element

# Series.Whiskers - Using the Quicktips Element

By default, a "quicktip" is displayed when the mouse hovers near or over a stem or whisker line. This is separate from the quicktips which are displayed for the chart bars.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563496471/series_whiskers_03.png)

The automatically-generated quicktip displays information for the low and high values, as shown above, left. However, you may want to display other information or format it differently, perhaps as shown above, right, which can be done by adding a **Quicktip** child element beneath Series.Whiskers and setting its attributes and child elements. Use @Chart tokens to include chart data in the quicktip and intrinsic functions are supported in the Quicktip element attributes.
