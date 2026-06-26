---
title: "Analysis Grid Developers - Controlling Column Availability"
id: 4419707277591
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707277591-Analysis-Grid-Developers-Controlling-Column-Availability
updated_at: 2022-07-17T02:02:06Z
---

# Analysis Grid Developers - Controlling Column Availability

# Analysis Grid Developers - Controlling Column Availability

Each **Analysis Grid Column** element has attributes that allow you to control whether or not that column can be used with a specific feature. For example, you may decide that some columns should be available for Sorting, while others should not.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706638999/workag_10.png)

For example, assume that an Analysis Grid Column that displays freight charges is *not* a good candidate for grouping. Setting this column's **No Grouping** attribute to *True* removes this column from the list of available columns in the Grouping feature, as shown above.

Developers can improve the overall usability of the Analysis Grid by determining in advance which columns are good candidates for aggregation, grouping, sorting, etc. and configuring the Analysis Grid columns accordingly.
