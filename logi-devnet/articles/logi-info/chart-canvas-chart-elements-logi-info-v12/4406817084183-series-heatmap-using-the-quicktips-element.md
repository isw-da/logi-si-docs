---
title: "Series.Heatmap - Using the Quicktips Element"
id: 4406817084183
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817084183-Series-Heatmap-Using-the-Quicktips-Element
updated_at: 2022-04-06T06:03:56Z
---

# Series.Heatmap - Using the Quicktips Element

# Series.Heatmap - Using the Quicktips Element

By default, a "quicktip" is displayed when the mouse hovers near or over a data point:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584139799/series_heatmap_06.png)

The automatically-generated quicktip displays information from the label and size data columns, as shown above, left. However, you may want to display other information or format it differently, perhaps as shown above, right, which can be done by adding a **Quicktip** child element beneath Series.Heatmap and setting its attributes and child elements. Use @Chart tokens to include chart data in the quicktip. Intrinsic functions are supported in the Quicktip attributes.
A default quicktip is also displayed when a Heatmap Group element is used. To customize it, the Quicktip element can also be a child of Heatmap Group.
