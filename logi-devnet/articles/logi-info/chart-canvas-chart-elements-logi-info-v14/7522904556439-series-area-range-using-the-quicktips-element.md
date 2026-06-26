---
title: "Series.Area Range - Using the Quicktips Element"
id: 7522904556439
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/7522904556439-Series-Area-Range-Using-the-Quicktips-Element
updated_at: 2022-07-17T02:25:44Z
---

# Series.Area Range - Using the Quicktips Element

# Series.Area Range - Using the Quicktips Element

By default, a "blacktop" is displayed when the mouse hovers near or over a data point:

![](https://devnet.logianalytics.com/hc/article_attachments/7522883629079/series_arearange_07.png)

The automatically-generated quicktip displays information for the X- and Y-axis, as shown above, left. However, you may want to display other information or format it differently, as shown above, right, which can be done by adding a **Quicktip** child element beneath Series.Area Range.

![](https://devnet.logianalytics.com/hc/article_attachments/7522883642519/series_arearange_08_652x202.png)

The example above shows a Quicktip element (no attributes need to be set) and three **Quicktip Row** child elements, used to create the quicktip shown in the previous image. Use @Chart tokens to include chart data in the quicktip.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 You can also configure the tooltip to display values for any available column in the datalayer. To do so, enter a token representing the data column in the Value attribute of the Quicktip Row element.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) To use this feature with DataLayer.ActiveSQL, please make sure the keep Grouped Rows attribute of the SqlGroup element is set to False.

To utilize this feature, add a Quicktip Row element below the Quicktip. Then, enter a token representing the data column in the Value attribute.

Intrinsic functions are supported in the Quicktip attributes.

The Quicktip Row element has been made context-sensitive with the addition of a **Condition** attribute.
