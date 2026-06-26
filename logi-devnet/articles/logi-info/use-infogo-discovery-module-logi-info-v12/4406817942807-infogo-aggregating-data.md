---
title: "InfoGo - Aggregating Data"
id: 4406817942807
section: "Use InfoGo/Discovery Module - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817942807-InfoGo-Aggregating-Data
updated_at: 2022-04-06T06:09:10Z
---

# InfoGo - Aggregating Data

# InfoGo - Aggregating Data

The **Aggregate** feature in the Table configuration area, which can
be displayed by clicking the gear icon or by clicking any table column
header, lets you calculate totals, averages, and other aggregations:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563060247/usinginfogo125_26.png)

Here's how to use this feature:

1. Select the **Data Column** to be aggregated from the column list.
2. Select the **Aggregate Function**. Options include: *Sum*, *Average*, *Standard Deviation*, *Count*, *Distinct Count*, *Minimum*, and *Maximum*. Click **Add** to aggregate the data and refresh the table. The formatting of the aggregation will match that of the column.
3. As aggregates are created, they're added to the Aggregates list. Use the adjacent **Replace** and **Remove** buttons to manage the list.
4. Aggregate results appear in an extra table row that can be positioned at the top or bottom of the table, as shown above. If **Grouping** is in effect, aggregate values will also appear at each grouping level in the table.
5. Aggregating can be also be accomplished by clicking a column header in
   the table and then selecting the desired options from the context menu.

Generally, columns with Null values are *excluded* from
aggregations. However, your application may be configured to include
them; check with the developer of your application for details.

Click the gear icon to hide the configuration area.

## Aggregate Awareness: Selecting the Order of Operations

If you're going to aggregate a Formula column (created by executing a calculation), the "order of operations" may be important. For example, should the Analysis Grid do the calculation first, then apply the aggregation, or apply the aggregation and then do the calculation? The choice can result in completely different results.

The Analysis Grid includes "aggregate awareness" and, upon detecting this situation, will prompt you to choose the desired order of operations. Here's how it works:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583707671/usinginfogo125_26a.png)

In the example above, the TotalValue column is a Formula column, created using the formula [Quantity] \* [UnitPrice].

![](https://devnet.logianalytics.com/hc/article_attachments/4417563060375/usinginfogo125_26b.png)

We'd like to know the *average* TotalValue, so we click the TotalValue column header and select **Aggregate**![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)**Average**, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575525271/usinginfogo125_26c.png)

Because the Analysis Grid knows that TotalValue is a Formula column, it will display the modal dialog box shown above, allowing us to decide which order of operations to use. This level of control ensures that you'll get the aggregation you expected, and is especially useful when working with complex formulas, such as per capita and pro rata calculations, with multiple columns.
