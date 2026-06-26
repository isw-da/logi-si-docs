---
title: "Series.Pie - Using the Quicktips Element"
id: 4406822151191
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822151191-Series-Pie-Using-the-Quicktips-Element
updated_at: 2022-04-06T06:04:03Z
---

# Series.Pie - Using the Quicktips Element

# Series.Pie - Using the Quicktips Element

By default, a "quicktip" is displayed when the mouse hovers near or over a pie slice:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563512983/series_pie_11.png)

The automatically-generated quicktip displays information for the X- and Y-axis, as shown above, left. However, you may want to display other information or format it differently, perhaps as shown above, right. This "custom" Quicktip is created by adding a **Quicktip** child element beneath Series.Pie and setting its attributes and, optionally, using its **Quicktip Row** child element. Use @Chart tokens to include chart data in the Quicktip.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584135319/series_pie_12_751x202.png)

The example above shows another custom Quicktip in use and this time the chart data values are displayed in the Quicktip as *percentages*. This is done by adding a **Percent of Total Column** element to your datalayer and using its @Chart token in a **Quicktip Row** element's **Value** attribute. The Quicktip Row element's **Format** attribute is then set to *Percent*, as shown.

Intrinsic functions are supported in the Quicktip attributes.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575435927/notev12.7base.png)The Quicktip Row element has been made context-sensitive with the addition of a **Condition** attribute.
