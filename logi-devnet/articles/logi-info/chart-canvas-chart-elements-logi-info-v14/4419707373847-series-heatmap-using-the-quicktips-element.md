---
title: "Series.Heatmap - Using the Quicktips Element"
id: 4419707373847
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707373847-Series-Heatmap-Using-the-Quicktips-Element
updated_at: 2022-07-17T02:25:10Z
---

# Series.Heatmap - Using the Quicktips Element

# Series.Heatmap - Using the Quicktips Element

By default, a "quicktip" is displayed when the mouse hovers near or over a data point:

![](https://devnet.logianalytics.com/hc/article_attachments/7522849110039/series_heatmap_06.png)

The automatically-generated quicktip displays information from the label and size data columns, as shown above, left. However, you may want to display other information or format it differently, perhaps as shown above, right, which can be done by adding a **Quicktip** child element beneath Series.Heatmap and setting its attributes and child elements. Use @Chart tokens to include chart data in the quicktip. Intrinsic functions are supported in the Quicktip attributes.
A default quicktip is also displayed when a Heatmap Group element is used. To customize it, the Quicktip element can also be a child of Heatmap Group.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 You can also configure the tooltip to display values for any available column in the datalayer. To do so, enter a token representing the data column in the Value attribute of the Quicktip Row element.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) To use this feature with DataLayer.ActiveSQL, please make sure the keep Grouped Rows attribute of the SqlGroup element is set to False.
