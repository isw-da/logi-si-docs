---
title: "Analysis Grid - Creating Aggregations"
id: 4419715060119
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715060119-Analysis-Grid-Creating-Aggregations
updated_at: 2022-07-17T02:25:21Z
---

# Analysis Grid - Creating Aggregations

# Analysis Grid - Creating Aggregations

The Aggregate feature enables you to control aggregation functions in your Analysis Grid. You can combine standard calculations or create custom aggregations and save them to use more than once.

For information on how to customize an aggregation, see [Analysis Grid - Creating Custom Aggregations](https://devnet.logianalytics.com/hc/en-us/articles/4419715062807-Analysis-Grid-Creating-Custom-Aggregations).

Access this feature by selecting the **gear** icon or selecting any **table column header** when viewing a table:

![](https://devnet.logianalytics.com/hc/article_attachments/7522864366871/usingag_19.png)

Here's how to use standard aggregations:

1. Select the **Data Column** you want to be part of your aggregation.
2. Select the **Aggregate Function**. Options include: *Sum*, *Average*, *Standard Deviation*, *Count*, *Distinct Count*, *Minimum*, *Maximum*, and any *Custom* aggregations you may have.
3. Select **Add**. Logi Info aggregates the data and refreshes the table. Info matches the formatting of the aggregation to that of the column.
4. Logi Info adds aggregates to the Aggregate list as they are created. Select the adjacent **Replace** button or **trash can** icon to manage the list.
5. You can specify that aggregate results appear in an extra table row at the top or bottom of the table, as shown above. If *Grouping* is in effect, aggregate values will also appear at each grouping level in the table.
6. Select the **gear** icon to hide the configuration area.

By default, columns with Null values are *excluded* from aggregations. However, you can configure your Analysis Grid to include them; check with your developer for details.

For information about filtering by aggregate, see [Analysis Grid - Filtering Rows](https://devnet.logianalytics.com/hc/en-us/articles/4419707291927-Analysis-Grid-Filtering-Rows).
