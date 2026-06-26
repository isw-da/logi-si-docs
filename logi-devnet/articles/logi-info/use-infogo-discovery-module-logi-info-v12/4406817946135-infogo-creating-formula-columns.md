---
title: "InfoGo - Creating Formula Columns"
id: 4406817946135
section: "Use InfoGo/Discovery Module - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817946135-InfoGo-Creating-Formula-Columns
updated_at: 2022-04-06T06:09:13Z
---

# InfoGo - Creating Formula Columns

# InfoGo - Creating Formula Columns

Click the **Formula** tab to use the feature that allows you to add calculated columns
to the data.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583706263/usinginfogo125_14.png)

New columns are added at the right side of the table but can be relocated by dragging them. Here's how to use this feature:

1. Help constructing a formula is available via the **Formula Help** button.
2. Enter the **Name** for the column that will be added to the table.
3. **Insert** column names, functions, and operators into the Formula box by selecting them here.
4. And/or enter the formula by typing it into the **Formula**
   box. Column names should be enclosed within square brackets [ ] and
   typical math operator symbols, such as + - \* / should be used. You can
   always edit or delete anything in this space and you can enter formulas that don't contain data columns.
5. Specify the **Data Type** for the new column.
6. Specify a **Display Format**. Formatting options include numeric and date formats. Click **Add** to create the new column and refresh the table.
7. As **Formula Columns** are created, they're added to the Formula Columns list. Use the adjacent **Replace** and **Remove**
   buttons to manage the list. Columns that have been added are now
   included in the list of available columns (3) for use in other formulae.

Your application developer will have to advise you concerning which
function set is valid in the Formula box. These can vary depending on
the way in which data is retrieved from the data source. For example, in one scenario,
JavaScript-style functions can be used, but in another only
functions supported by the database server itself can be used. The help
shown when you click the **Formula Help** button will provide useful information, based on the data source.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) To prevent creation of unmanageable tables, numeric type Formula columns are not available for use in a Crosstab table as the Header Values Column or the Label Values Column.

When done, click the **Formula** tab or button to hide the panel.
