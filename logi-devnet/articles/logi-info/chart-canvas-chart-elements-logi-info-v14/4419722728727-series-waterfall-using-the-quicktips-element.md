---
title: "Series.Waterfall - Using the Quicktips Element"
id: 4419722728727
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722728727-Series-Waterfall-Using-the-Quicktips-Element
updated_at: 2022-07-17T02:25:05Z
---

# Series.Waterfall - Using the Quicktips Element

# Series.Waterfall - Using the Quicktips Element

By default, a "quicktip" is displayed when the mouse hovers over a bar:

![](https://devnet.logianalytics.com/hc/article_attachments/7522817975319/series_waterfall_06.png)

The automatically-generated quicktip displays information for the X- and Y-axis, as shown above, left. However, you may want to display other information or format it differently, perhaps as shown above, right. This can be done by adding a **Quicktip** child element beneath Series.Waterfall and setting its attributes and child elements. Use @Chart tokens to include chart data in the quicktip. Intrinsic functions are supported in the Quicktip attributes.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 You can also configure the tooltip to display values for any available column in the datalayer. To do so, enter a token representing the data column in the Value attribute of the Quicktip Row element.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) To use this feature with DataLayer.ActiveSQL, please make sure the keep Grouped Rows attribute of the SqlGroup element is set to False.
