---
title: "Series.Area - Using the Quicktips Element "
id: 4406817034903
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817034903-Series-Area-Using-the-Quicktips-Element
updated_at: 2022-04-06T06:03:30Z
---

# Series.Area - Using the Quicktips Element 

# Series.Area - Using the Quicktips Element

By default, a "quicktip" is displayed when the mouse hovers near or over a data point:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584162199/series_area_09.png)

The automatically-generated quicktip displays information for the X- and Y-axis, as shown above, left. However, you may want to display other information or format it differently, perhaps as shown above, right, which can be done by adding a **Quicktip** child element beneath Series.Area and setting its attributes and child elements. Use @Chart tokens to include chart data in the quicktip.

Intrinsic functions are supported in the Quicktip attributes.

You can deliberately add additional lines by adding child **Quicktip Row** elements beneath the Quicktip, one for each additional line of text you want to include.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575435927/notev12.7base.png)The Quicktip Row element has been made context-sensitive with the addition of a **Condition** attribute.
