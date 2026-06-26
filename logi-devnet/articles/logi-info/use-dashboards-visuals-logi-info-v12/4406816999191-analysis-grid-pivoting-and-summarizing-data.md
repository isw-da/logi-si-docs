---
title: "Analysis Grid - Pivoting and Summarizing Data"
id: 4406816999191
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816999191-Analysis-Grid-Pivoting-and-Summarizing-Data
updated_at: 2022-04-06T06:03:19Z
---

# Analysis Grid - Pivoting and Summarizing Data

# Analysis Grid - Pivoting and Summarizing Data

Click the **Add Crosstab** tab or button to use the feature that lets you create a crosstab (also known as a "pivot") table:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584178711/usingag_23.png)

Here's how to use this feature:

1. Select the **Header Values Column**, whose values will be shown *horizontally*,
   as column headers, across the top of the crosstab table.
   1. ![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) To prevent unmanageably wide tables, *numeric* columns in the original data and numeric Formula columns are not available for use here. Additional controls
      may appear depending on the data type of the selected column.
2. Select the **Label Values Column**, whose values will be shown *vertically*, in the left-most column of each row.
   1. ![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) To prevent unmanageably long tables, *numeric* columns in the original data and numeric Formula columns are not available for use here.
3. Select the **Aggregate Values Column**, whose values will be *aggregated* to produce the contents for the rest of the table cells.
4. Select the **Aggregate Function** to be applied to the column selected in Step 3. Options include *Sum*, *Average*, *Standard Deviation*, *Count* and *Distinct Count, Minimum* (v12.2), and *Maximum* (v12.2)*.*
5. Select a **Summary Function** to display a summary result.
6. If you application has been configured for this, check the **Compare Label Columns** check box to cause the difference
   between column values to be displayed, along with a cell shading indicator.

Also, depending on the application configuration, you may see an **OK** button like the one shown above that applies all of your selection changes to the table as a batch. Otherwise, your table will be updated immediately when you make individual changes.

The Summary Function feature, introduced in v12.1, and the Label Column Comparison feature provide interesting ways to analyze the data:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575906583/usingag_23a.png)

As shown above, summarizing the data totals the rows and columns, inserting a row and column to display the results. Comparing Label columns can produce color spectrum backgrounds or directional arrows, and can display the value differences as values or percentages, in the cells.

Hide the crosstab configuration area by clicking the gear icon, or delete the table entirely by clicking the Remove (Trashcan) icon.

Crosstab tables are displayed in their own panels, so you can expand and collapse them using their "+" and "-" icons. You can also rearrange the order of chart and table panels by clicking with your mouse near the top of a panel, and dragging it up or down.
