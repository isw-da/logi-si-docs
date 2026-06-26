---
title: "InfoGo - Pivoting and Summarizing Data"
id: 4419707885591
section: "Use InfoGo/Discovery Module - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707885591-InfoGo-Pivoting-and-Summarizing-Data
updated_at: 2022-07-17T02:23:17Z
---

# InfoGo - Pivoting and Summarizing Data

# InfoGo - Pivoting and Summarizing Data

Click the **Add Crosstab** tab to use the feature that lets you create a crosstab (also known as a "pivot") table:

![](https://devnet.logianalytics.com/hc/article_attachments/7522782378647/image-20220112-161241_907x820.png)

Here's how to use this feature:

1. Select the **Header Values Column**, whose values will be shown *horizontally*,
   as column headers, across the top of the Crosstab Table. ![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) To prevent unmanageably wide tables, *numeric* columns in the original data and numeric Formula columns are not available for use here. Additional controls
   may appear depending on the data type of the selected column.
2. Select the **Label Values Column**, whose values will be shown *vertically*, in the left-most column of each row. ![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) To prevent unmanageably long tables, *numeric* columns in the original data and numeric Formula columns are not available for use here.
3. ![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1 Select the **Secondary Label Column**, whose values will be shown *vertically,* as column headers, after the Label Values Column. This column is used to group Value Columns and Label Columns together. ![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) To prevent unmanageably long tables, *numeric* columns in the original data and numeric Formula columns are not available for use here.
4. Select the **Extra Label Column**, whose values will be shown
5. Select the **Aggregate Values Column**, whose values will be *aggregated* to produce the contents for the rest of the table cells.
6. Select the **Aggregate Function** to be applied to the column selected in Step 3. Options include *Sum*, *Average*, *Standard Deviation*, *Count* and *Distinct Count, Minimum,* and *Maximum.*
7. Select a **Summary Function** to display a summary result.
8. Check the **Compare Label Columns** check box to cause the difference
   between column values to be displayed, along with a cell shading indicator.

If it exists, click **OK** to generate the Crosstab Table, in its own panel; otherwise the table will be generated automatically as you make changes.

The Summary Function and Label Column Comparison features provide interesting ways to analyze the data:

![](https://devnet.logianalytics.com/hc/article_attachments/7522765746199/usinginfogo125_33.png)

As shown above, summarizing the data totals the rows and columns, inserting a row and column to display the results. Comparing Label columns can produce color spectrum backgrounds or directional arrows, and can display the value differences as values or percentages, in the cells.

Click the **gear** icon to hide the configuration area.
