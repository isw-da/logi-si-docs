---
title: "Series.Scatter - Using the Quicktips Element"
id: 4406817118615
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817118615-Series-Scatter-Using-the-Quicktips-Element
updated_at: 2022-04-06T06:04:10Z
---

# Series.Scatter - Using the Quicktips Element

# Series.Scatter - Using the Quicktips Element

By default, a "quicktip" is displayed when the mouse hovers over a symbol:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575870999/series_scatter_10.png)

The automatically-generated quicktip displays information from the X- and Y-axes, as shown above, left. However, you may want to display other information or format it differently, perhaps as shown above, right, which can be done by adding a **Quicktip** child element beneath Series.Scatter and setting its attributes and child elements. Use @Chart tokens to include chart data in the quicktip.

Intrinsic functions are supported in the Quicktip attributes.
