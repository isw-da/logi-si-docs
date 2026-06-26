---
title: "Series.Area Range - Using the Quicktips Element"
id: 4419722720919
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722720919-Series-Area-Range-Using-the-Quicktips-Element
updated_at: 2022-04-01T09:24:02Z
---

# Series.Area Range - Using the Quicktips Element

# Series.Area Range - Using the Quicktips Element

By default, a "quicktip" is displayed when the mouse hovers near or over a data point:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699580311/series_arearange_07.png)

The automatically-generated quicktip displays information for the X- and Y-axis, as shown above, left. However, you may want to display other information or format it differently, as shown above, right, which can be done by adding a **Quicktip** child element beneath Series.Area Range.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706675991/series_arearange_08_652x202.png)

The example above shows a Quicktip element (no attributes need to be set) and three **Quicktip Row** child elements, used to create the quicktip shown in the previous image.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706629655/noteicon.jpg) A @Chart token is used access the chart data.

Intrinsic functions are supported in the Quicktip attributes.

The Quicktip Row element has been made context-sensitive with the addition of a **Condition** attribute.
