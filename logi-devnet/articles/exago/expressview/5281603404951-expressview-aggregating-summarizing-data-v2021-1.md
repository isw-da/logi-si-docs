---
title: "ExpressView: Aggregating/Summarizing Data (v2021.1+)"
id: 5281603404951
section: "ExpressView"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281603404951-ExpressView-Aggregating-Summarizing-Data-v2021-1
updated_at: 2022-05-03T22:09:07Z
---

# ExpressView: Aggregating/Summarizing Data (v2021.1+)

# ExpressView: Aggregating/Summarizing Data (*v2021.1+*)

**Aggregating** leverages the power of ExpressView groups to compile summaries of data. Aggregates may be optionally added for each group and for the entire report.

Pre-defined **aggregate functions** determine how the summary is calculated. The available functions will vary with the data type in the column, but in general they are:

* *Sum* — display the additive total of this column
* *Min* — display the smallest or earliest value in this column
* *Max* — display the largest or latest value in this column
* *Count* — display the number of rows in this column. For example in the data set {1, 2, 3, 3, 4, 4} the count is 6.
* *Distinct Count* — display the number of unique rows in this column. For example in the data set {1, 2, 3, 3, 4, 4} the distinct count is 4.
* *Avg* — display the average of this column
* *None* — do not show an aggregate for this column

![KamUnWUdWj.png](https://devnet.logianalytics.com/hc/article_attachments/5432319377943/kamunwudwj.png)

**Distinct Count** aggregate function on the `Model #` column and **Sum** aggregate function on the `Views` column is computed for each group (Manufacturer and Category) as well as an overall report total

To show only the aggregates, uncheck the **Detail Rows** checkbox in the toolbar.

![tlDV5naVtA.png](https://devnet.logianalytics.com/hc/article_attachments/5432223729047/tldv5navta.png)

The same ExpressView as above, without Detail Rows

## Adding Aggregates

Either **Group Totals** or **Report Totals** (or both) must be checked in the toolbar. Unchecking one or the other hides the respective total from view.

As numeric fields are added to the ExpressView, the *Sum* aggregate function will be automatically applied.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Checking **Group Totals** enables aggregating for all groups.

To aggregate data:

1. Click the **Choose Aggregate**![DashboardMoreArrow.png](https://devnet.logianalytics.com/hc/article_attachments/5432247972119/dashboardmorearrow.png) icon in the desired group footer or report footer.
2. Click an available aggregate function.

![hTx547RWZI.png](https://devnet.logianalytics.com/hc/article_attachments/5432319467927/htx547rwzi.png)

Selecting the Distinct Count aggregate function for the Model # group column

![wIGsLaZuuc.png](https://devnet.logianalytics.com/hc/article_attachments/5432296878999/wigslazuuc.png)

Selecting the Average aggregate function for the Wt (lbs) detail field as a report total

## Changing Aggregates

1. Click the **Choose Aggregate**![DashboardMoreArrow.png](https://devnet.logianalytics.com/hc/article_attachments/5432247972119/dashboardmorearrow.png) icon in the desired group footer or report footer.
2. Click an available aggregate function.

## Removing Aggregates

To stop aggregating on a single column:

1. Click the **Choose Aggregate**![DashboardMoreArrow.png](https://devnet.logianalytics.com/hc/article_attachments/5432247972119/dashboardmorearrow.png) icon in the desired group footer or report footer.
2. Click *None*.

To stop aggregating for a section type:

1. In the toolbar, uncheck the respective **Group Totals** or **Report Totals** checkbox.
