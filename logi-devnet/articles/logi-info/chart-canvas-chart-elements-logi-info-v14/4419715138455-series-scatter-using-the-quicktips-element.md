---
title: "Series.Scatter - Using the Quicktips Element"
id: 4419715138455
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715138455-Series-Scatter-Using-the-Quicktips-Element
updated_at: 2022-07-17T02:25:06Z
---

# Series.Scatter - Using the Quicktips Element

# Series.Scatter - Using the Quicktips Element

By default, a "quicktip" is displayed when the mouse hovers over a symbol:

![](https://devnet.logianalytics.com/hc/article_attachments/7522818064279/series_scatter_10.png)

The automatically-generated quicktip displays information from the X- and Y-axes, as shown above, left. However, you may want to display other information or format it differently, perhaps as shown above, right, which can be done by adding a **Quicktip** child element beneath Series.Scatter and setting its attributes and child elements. Use @Chart tokens to include chart data in the quicktip.
Intrinsic functions are supported in the Quicktip attributes.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 You can also configure the tooltip to display values for any available column in the datalayer. To do so, enter a token representing the data column in the Value attribute of the Quicktip Row element.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) To use this feature with DataLayer.ActiveSQL, please make sure the keep Grouped Rows attribute of the SqlGroup element is set to False.
