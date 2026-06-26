---
title: "Series.Bar Range - Using the Quicktips Element"
id: 4419707359767
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707359767-Series-Bar-Range-Using-the-Quicktips-Element
updated_at: 2022-07-17T02:25:12Z
---

# Series.Bar Range - Using the Quicktips Element

# Series.Bar Range - Using the Quicktips Element

By default, a "quicktip" is displayed when the mouse hovers near or over a data point:

![](https://devnet.logianalytics.com/hc/article_attachments/7522855288215/series_barrange_07.png)

The automatically-generated quicktip displays information for the X- and Y-axis, as shown above, left. However, you may want to display other information or format it differently, as shown above, right, which can be done by adding a **Quicktip** child element beneath Series.Bar Range.

![](https://devnet.logianalytics.com/hc/article_attachments/7522880209815/series_barrange_08_652x190.png)

The example above shows a Quicktip element (no attributes need to be set) and three **Quicktip Row** child elements, used to create the quicktip shown in the previous image. Use @Chart tokens to include chart data in the quicktip.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 You can also configure the tooltip to display values for any available column in the datalayer. To do so, enter a token representing the data column in the Value attribute of the Quicktip Row element.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) To use this feature with DataLayer.ActiveSQL, please make sure the keep Grouped Rows attribute of the SqlGroup element is set to False.

Intrinsic functions are supported in the Quicktip attributes.

The Quicktip Row element has been made context-sensitive with the addition of a **Condition** attribute.
