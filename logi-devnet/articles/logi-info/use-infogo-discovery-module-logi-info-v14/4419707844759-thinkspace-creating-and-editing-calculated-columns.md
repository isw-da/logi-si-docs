---
title: "Thinkspace - Creating and Editing Calculated Columns"
id: 4419707844759
section: "Use InfoGo/Discovery Module - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707844759-Thinkspace-Creating-and-Editing-Calculated-Columns
updated_at: 2022-07-17T01:37:17Z
---

# Thinkspace - Creating and Editing Calculated Columns

# Thinkspace - Creating and Editing Calculated Columns

You may want to add new columns to the data which are the result of calculations using existing data. A simple example would be multiplying Quantity values by Unit Price values to obtain a Total. Here's how:

![](https://devnet.logianalytics.com/hc/article_attachments/4419707076119/dm30_workcols_10.png)

Click **New Calculation** on a column's gear menu, as shown above, or click the **Calculated Columns** button, and the calculation definition panel will appear:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714900375/dm30_workcols_12.png)

Use this panel to create the expression that will produce your calculated data. The controls are:

1. **Column Name** - Enter your choice for the new column name here. If you used a column's gear Menu to get here, a new column name (such as "Quantity\_calc") will be suggested.
2. **Expression** - Create your expression here. You can use column names, functions, etc. from below by selecting them (thus avoiding typos) but you'll need to enter basic math operators (+, -, \*, /) manually. See the important information below about expressions.
3. **Test** - Click this button to test your expression. A valid formula will produce this ![](https://devnet.logianalytics.com/hc/article_attachments/4419699905431/dm30_workcols_13.png) success indicator. However, if you see the ![](https://devnet.logianalytics.com/hc/article_attachments/4419707076759/dm30_workcols_14.png) warning, hover your cursor over it to see a tooltip describing the problem.
4. **Formula Parts** - Hover over an object here see its syntax and a brief description. Click it to insert it into your expression. Left and right arrows let you scroll through several categories of objects and functions.
5. **Delete** - Click this to delete an existing calculated column.
6. **Add** - Click this to add the new calculated column to the Data Table. The sliding Enable/Disable switch can be used to turn formatting on and off.

## About Expressions

The expression editor has wizard-like features that help you reference functions, columns, etc. easily and avoid errors. The expression syntax must conform to the SQL syntax rules for **PostgreSQL**. The functions shown in the Calculation panel are not exhaustive - other PostgreSQL functions may be used. For more detailed syntax information, refer to the [*PostgreSQL Reference Manual*](https://www.postgresql.org/docs/9.6/static/functions.html). When in doubt, use the **Test**
button to validate your expression.

Here's some general information about Thinkspace expressions:

*Column References* - All column name references must be enclosed in square brackets
(e.g. *[column name]*). If you select a column from the list, the editor will automatically add the square brackets to the column
reference. If you're typing the formula in directly, typing a "[" will
cause the editor to show a list of valid column names for you to select from.

*Null Values* - By default Null data values are considered when grouping on the
column but ignored for any aggregations or charts.
If you wish to have Null values counted, they must be
converted to a real value (e.g. "N/A", 0, -1, "Unknown") in your expression. For example,
to represent Null values as a real value, you could use:
IFNULL ([column], 'N/A') in your expression.

The IFNULL function can be found
in the "Logical" functions category. When the calculated column resulting from this expression is used, it will behave like other columns of the same data type
and be included in grouping, aggregations, and charts.

*SQL Functions* - You can use ANSI SQL-92-compliant SQL functions if the standard expression functions aren't sufficient by placing them in a SQL\_FUNCTION wrapper and enabling the Passthrough feature in Logi Data Service.

To enable the feature, open the /platform/settings/logiDataService.json file and set:

"enablePassthrough": true,

Save the file and then stop and restart the Logi services. In the Calculated Column expression, wrap your SQL function like this:

SQL\_FUNCTION('SUBSTRING([CustomerID],1,2)')

Column names must be enclosed in square
brackets. Complex SQL statements, like the one shown below, are supported:

SQL\_FUNCTION("CASE WHEN [Country] = 'Argentina' THEN 1 ELSE 0 END")

## Editing a Calculated Column

A Calculated Column's gear Menu will include an **Edit Calculation** item:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714900631/dm30_workcols_15.png)

Click the menu item, shown above, to re-open the calculation definition panel and edit the calculation.
