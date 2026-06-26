---
title: "Data Table Basics"
id: 4406817272727
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817272727-Data-Table-Basics
updated_at: 2022-04-06T06:05:06Z
---

# Data Table Basics

# Data Table Basics

Data tables are dynamic, data-driven reporting components. Unlike basic HTML tables built using the Rows, Row, and Column Cell elements, data tables are designed column-by-column rather than row-by-row.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584034071/createtable_01.png)

As shown above, every data table must have the following components:

* A **Data Table** element
* One or more **DataLayer** elements to retrieve and cache the data, possibly with child Filter elements
* One or more **Data Table Column** elements to display each column
* One or more report content elements, such as a **Label**, to present the data

This column-wise approach can be confusing. Just remember that, at runtime, *every**record* in the datalayer will be iterated and rows for all of the data will be displayed in the table. Developers create and configure each column, while the number of rows is entirely dependent on the data.

The **Data Table Column** element, for example, is configured to provide the column header text, column width (if not automatically determined), and so forth.

The actual data values in the datalayer are accessed using *tokens*, such as @Data.CategoryID~, where the second part of the token is the column name in the datalayer. This case-sensitive token can be used in Label element Captions, for example, to display the data. For more information about tokens, see [Token Reference](https://devnet.logianalytics.com/hc/en-us/articles/4406817899415-Token-Reference).

![](https://devnet.logianalytics.com/hc/article_attachments/4417563394455/createtable_02.png)

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The table shown above has had style applied to it to specify its fonts, borders, and background colors. An easy way to quickly style a data table is to apply a Theme to your report definition. For more information, see [Themes](https://devnet.logianalytics.com/hc/en-us/articles/4406818168855-Themes).

The most common way to design data tables is to have a **Data Table Column** element for each column in the datalayer, as shown above. This works well when you have many records that you want to show in a table.

The *order* of the columns in the displayed data table is governed by the order of the Data Table Column elements in the definition. The top-most of these elements in the definition will be the left-most column in the displayed data table. Developers are free to rearrange the order of columns by selecting a Data Table Column element in Logi Studio and dragging it, or by using the Up/Down Arrow buttons in the toolbar. This is particularly useful if a wizard has been used to create the data table and a
different column arrangement is desired.

The one-to-one correspondence of data columns to Data Table Columns elements discussed above is *not required* and developers have complete freedom over the way data is presented in a report. Suppose, for example, that you don't want the typical tabular format.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575778199/createtable_03.png)

Suppose instead you want to stack the data in a kind of form when you display it. This is easy to do, as shown above. The data is presented in a form-like manner by using just *one* Data Table Column element and placing multiple **Label** elements within it. Each Label element displays the data from a different data column in the datalayer. There's no limit on the number of elements you can place beneath a single Data Table Column element and you can, in fact, even place HTML tables and charts
there!

**Important Scope Limitation**
The *scope* of the data in a datalayer is limited to the **Data Table** element that contains it and its child elements. So, looking at the example above, the token @Data.CategoryID~ is valid in all elements beneath the data table *dtCategories*, but will be empty if you attempt to use it elsewhere, such as in the Report Header element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The only exception to this scope limitation is the **Local Data** element. This element works with a datalayer which retrieves just one result row but its data is available, using the @Local.*<columnName>*~ token, anywhere in the report definition.
