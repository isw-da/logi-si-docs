---
title: "Crosstab Tables"
id: 4419707444631
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707444631-Crosstab-Tables
updated_at: 2022-04-01T09:24:28Z
---

# Crosstab Tables

# Crosstab Tables

A **Cross Tabulation** (often abbreviated as "crosstab") is a Data Table that displays the *joint distribution* of two or more variables simultaneously. Sometimes called "pivot tables", they make it easy to sort, count, and total their data. The Logi **Crosstab Table** element makes it easy to implement this kind of table.

The following topics discuss Crosstab Tables:

* [Using the Crosstab Table Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4419722784791-Using-the-Crosstab-Table-Wizard#Wizard)
* [Creating Crosstab Tables Manually](https://devnet.logianalytics.com/hc/en-us/articles/4419707443735-Creating-Crosstab-Tables-Manually#Creating)
* [Working with Crosstab Table Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419722785687-Working-with-Crosstab-Table-Columns#Columns)
* [Arranging and Sizing Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419707442711-Arranging-and-Sizing-Columns#Arranging)
* [Comparing, Sorting, and Summarizing Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419715190551-Comparing-Sorting-and-Summarizing-Columns-#Comparing)
* [Drillthrough to Column Detail](https://devnet.logianalytics.com/hc/en-us/articles/4419722781975-Drillthrough-to-Column-Detail#Detail)
* [Working with the Crosstab Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419715192599-Working-with-the-Crosstab-Filter#Filter)
* [Planning the Tutorial Crosstab Table](https://devnet.logianalytics.com/hc/en-us/articles/4419707445783-Planning-the-Tutorial-Crosstab-Table#Planning)
* [Building the Basic Table Structure](https://devnet.logianalytics.com/hc/en-us/articles/4419722780823-Building-the-Basic-Table-Structure#Basic)
* [Adding Extra Crosstab Values](https://devnet.logianalytics.com/hc/en-us/articles/4419715189399-Adding-Extra-Crosstab-Values#ExtraValues)
* [Summarizing Value Rows](https://devnet.logianalytics.com/hc/en-us/articles/4419722783895-Summarizing-Value-Rows#SumRows)
* [Adding a Header Row](https://devnet.logianalytics.com/hc/en-us/articles/4419707441687-Adding-Header-Rows-#HeaderRow)
* [Summarizing Value Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419722782871-Summarizing-Value-Columns-#SumColumns)

## About the Crosstab Table

The Logi Info **Crosstab Table** element is a dynamic, data-driven reporting component that consists of the following three datalayer column types:

* Crosstab (also called Header) Column- Creates a new *column* in the Crosstab Table for each *unique* value. The column value appears in the table header.
* Label Column- creates a new *row* in the Crosstab Table for each *unique* value. The column value appears in the first (left-most) column of the row.
* Value Column- displays a value in each cell at the intersection of the Crosstab columns and Label rows (excluding the header row and first column).

Here's how each of these data column types appear in a Crosstab Table:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699614743/xtabtable_04.png)

Each value displayed in the Value Column cells is the result of an *aggregation*, performed on the original data from the specified Value Column. The example above displays years for the Crosstab Column, employee names for the Label Column and a *sum* of corresponding subtotals for the Value Columns. So, when the year is *2013* and the employee is *Nancy Davolio*, the sum of all corresponding subtotals is *$35,764.51*.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) To prevent creation of unmanageable tables, numeric type columns are not available for use in a Crosstab Table as the Crosstab (Header) or the Label columns.

The following functions are available for aggregating Value Columns:

* **Any -** Displays a value from any of the rows. This can be used when the specified Value Column data is a string that isn't appropriate for aggregation; for example, when there's just one record to represent each crosstab cell.
* **Average -** Returns the average of all corresponding records in the specified Value Column.
* **Count -** Returns the total number of corresponding records in the specified Value Column.
* **DistinctCount** - Returns the total number of unique corresponding records in the specified Value Column.
* **Max** - Returns the maximum value in the specified Value Column.
* **Median -** Returns the value that separates the higher half of all values in the specified Value Column from the lower half.
* **Min** - Returns the minimum value in the specified Value Column.
* **Mode** - Returns the value that occurs the most frequently in records in the specified Value Column.
* **StdDev** - (Standard Deviation) Returns a simple measure of the variability of data in records in the specified Value Column. A low standard deviation indicates that the values tend to be very close to each other, while a high standard deviation indicates that the values are "spread out" over a large range.
* **Sum -** Returns the sum of all corresponding records in the specified Value Column

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) Columns with null values are *excluded* from aggregations by default. If you want to include them instead, create the constant rdCalculationsIncludeNulls in your \_Settings definition and set it to *True.* This will affect all calculations throughout the application.

What about differences between columns, either as values or as percentages? The **Crosstab Comparison** element can display these differences in a variety of ways. The element is discussed in detail in [Comparing, Sorting, and Summarizing Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419715190551-Comparing-Sorting-and-Summarizing-Columns-).
