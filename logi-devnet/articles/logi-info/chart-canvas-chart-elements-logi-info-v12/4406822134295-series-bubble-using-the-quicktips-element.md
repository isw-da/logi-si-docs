---
title: "Series.Bubble - Using the Quicktips Element"
id: 4406822134295
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822134295-Series-Bubble-Using-the-Quicktips-Element
updated_at: 2022-04-06T06:03:50Z
---

# Series.Bubble - Using the Quicktips Element

# Series.Bubble - Using the Quicktips Element

By default, a "quicktip" is displayed when the mouse hovers over a
bubble:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563526423/series_bubble_08.png)
The automatically-generated quicktip displays information from the X- and
Y-axes and the bubble size, as shown above, left. However, you may want to
display other information or format it differently, perhaps as shown above,
right, which can be done by adding a **Quicktip** child element beneath
Series.Bubble and setting its attributes and child elements. Use @Chart
tokens to include chart data in the quicktip. Intrinsic functions are
supported in the Quicktip attributes.
