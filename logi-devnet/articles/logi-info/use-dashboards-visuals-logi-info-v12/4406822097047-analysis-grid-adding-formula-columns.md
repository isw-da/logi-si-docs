---
title: "Analysis Grid - Adding Formula Columns"
id: 4406822097047
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822097047-Analysis-Grid-Adding-Formula-Columns
updated_at: 2022-04-06T06:03:14Z
---

# Analysis Grid - Adding Formula Columns

# Analysis Grid - Adding Formula Columns

Click the **Formula** tab or button to use the feature that allows you to add calculated columns
to the data:

![](https://devnet.logianalytics.com/hc/article_attachments/4417591974423/usingag_11.png)

New columns are added at the right side of the table but can be relocated by dragging them. Here's how to use this feature:

1. Help constructing a formula is available via the **Formula Help** button.  
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417575435927/notev12.7base.png)The Formula Help pages have been relocated; if you created a browser bookmark for them, you'll need to update it.
2. Enter the **Name** for the column that will be added to the table.
3. **Insert** column names, functions, and operators into the Formula box by selecting them here.
4. And/or enter the formula by typing it into the **Formula** box. Column names should be enclosed within square brackets [ ] and typical math operator symbols, such as + - \* / should be used. You can always edit or delete anything in this space.   
   You can enter formulas that don't contain data columns.
5. Specify the **Data Type** for the new column.
6. Specify a **Display Format**. Formatting options include numeric and date formats. Click **Add** to create the new column and refresh the table.
7. As **Formula Columns** are created, they're added to the Formula Columns list. Use the adjacent **Replace** button and **Remove** (Trashcan) icon to manage the list. Columns that have been added are now included in the list of available columns (3) for use in other formulae.

Your application developer will have to advise you concerning which function set is valid in the Formula box. These can vary depending on the way in which data is retrieved from the data source. In once case, JavaScript-style functions can be used, but in another case only functions supported by the database server itself can be used. The help shown when you click the **Formula Help** button will provide useful information depending on the data source.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) To prevent creation of unmanageable tables, numeric type Formula columns are not available for use in a Crosstab table as the Header Values Column or the Label Values Column.

Click the **Formula** tab or button to hide the controls when done.
