---
title: "Manipulating the Data"
id: 4419723035799
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723035799-Manipulating-the-Data
updated_at: 2022-07-17T02:07:10Z
---

# Manipulating the Data

# Manipulating the Data

Once data has been retrieved into a datalayer, a number of elements can be used to manipulate its data. This is generally done by either re-arranging rows, removing rows, or by adding columns to the datalayer. These elements are summarized below; the links direct you to individual topics that discuss the use of each element:

| Element | Description |
| --- | --- |
| Aggregate Column | Adds a new column to the datalayer that aggregates data from another column. Functions include *Average*, *Count*, *DistinctCount*, *Max*, *Median*, *Min*, *Mode*, *Sum*, and *StdDev.* For more information, see [The Aggregate Column](https://devnet.logianalytics.com/hc/en-us/articles/4419707269527-The-Aggregate-Column) |
| Calculated Column | Adds a new column to the datalayer whose data is the result of a formula that uses data from other columns in the same row or other token values. For example, multiplying the values from two columns together. JavaScript functions are supported in formulae. |
| Color Spectrum Column | Adds a new column to the datalayer, containing color values that fall between the LowValueColor and HighValueColor attribute values. The color for each row is generated based on where the current Data Column value falls between the Min Range and Max Range. |
| Compare Filter | Analogous to the *WHERE* clause in a SQL query, this element removes rows from the datalayer that do not meet specified criteria. Uses native data engine code for fastest performance. For more information, see [The Compare Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419707415575-The-Compare-Filter). |
| Condition Filter | Similar to the Compare Filter, this element uses scripting to remove rows from the datalayer that do not meet specified criteria. However, this filter uses scripting and therefore performs *much more slowly* than the Compare Filter. We recommend that you use the Compare Filter instead whenever possible. For more information, see [The Condition Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419722756503-The-Condition-Filter). |
| Contain Filter | Analogous to using a *WHERE**x CONTAINS y* clause in a SQL query, this element removes rows from the datalayer that do not return results in a text search of specified columns. For more information, see [The Contain Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419707426199-The-Contain-Filter). |
| Crosstab Filter | "Pivots" the data to convert the datalayer into a "cross-tab" format. |
| DeDuplicate Filter | Analogous to using a *DISTINCT* clause in a SQL query, this element removes rows from the datalayer that have duplicated values in specified columns. For more information, see [The DeDuplicate Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419722861463-The-DeDuplicate-Filter). |
| Difference Column | Adds a new column to the datalayer that contains the difference, as a number or as a percentage, between a numeric value in a column in the current and the previous rows. |
| File Column | Used with BLOBs and CLOBS, this element copies the column data and saves it to a file, then optionally adds columns to the datalayer containing the saved file's name and path. For more information, see [The File Column (BLOBs)](https://devnet.logianalytics.com/hc/en-us/articles/4419707590295-The-File-Column-BLOBs-). |
| Flattener | Processes hierarchical data into a tabular set of rows and columns, so that it can be used with a range of Logi elements. For more information, see [The Flattener](https://devnet.logianalytics.com/hc/en-us/articles/4419722921623-The-Flattener). |
| Forecasting Elements | Forecasting elements use a variety of techniques to produce projected values by analyzing existing values. The future values they "predict" are, in most cases, added as rows or columns to a datalayer so the data can be displayed along with the existing data. For more information, see [The Forecasting Elements](https://devnet.logianalytics.com/hc/en-us/articles/4419722922903-The-Forecasting-Elements). |
| Formatted Column | Adds a new column to the datalayer that represents the source value after formatting. For more information, see [The Formatted Column](https://devnet.logianalytics.com/hc/en-us/articles/4419700079639-The-Formatted-Column). |
| Group Filter | Groups rows in the datalayer based on one or more column values and allows group aggregate values to be created. For more information, see [The Group Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419722944407-The-Group-Filter). |
| Join | Analogous to a *JOIN* clause in a SQL query, this element adds columns to the datalayer so that multiple tables can be joined to create a single dataset. For more information, see [Join Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4419700071319-Join-Datalayers). |
| Lookup Element | Performs a "look up" of related data. It runs its own datalayer once for each row in its parent datalayer and automatically joins the results. For more information, see [The Lookup Element](https://devnet.logianalytics.com/hc/en-us/articles/4419700080663-The-Lookup-Element). |
| Moving Average Column | Adds a new column to the datalayer based on the average value of another column spread over some number of previous rows. Used to smooth data series and make it easier to spot trends. |
| Percent of Total Column | Adds a new column to the datalayer containing the percentage of some value in the row compared to the total of that value in all rows. |
| Rank Column | Adds a new column to the datalayer containing either a numeric or percentile rank based on all the values of some other column. |
| RegEx Filter | Removes rows from the datalayer by applying pattern matching using regular expressions. For more information, see [The RegEx Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419707794839-The-RegEx-Filter). |
| Relevance Filter | Removes rows (*irrelevant* data) from the datalayer that do not meet a threshold; optionally, irrelevant rows can be retained, grouped together, and handled as an individual entity. For more information, see [The Relevance Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419707264023-The-Relevance-Filter). |
| Remove Columns | Removes one of more columns from the datalayer to reduce the size of the data during processing. If a column is no longer required, you can use this element to delete it. |
| Rename Columns | Renames one or more columns in the datalayer. To use it, specify a comma-separated list of existing column names in the Column Names attribute, and a matching number of comma-separated new names in the New Column Name attributes. Columns named in the first list but which do not exist will be ignored. |
| Running Total Column | Adds a new column to the datalayer containing values based on the sum of all previous values of another column. |
| Security Filter | Removes rows from the datalayer, like a Condition Filter, but is applied based on a user's security rights. For more information, see [Securing Data](https://devnet.logianalytics.com/hc/en-us/articles/4419723328535-Securing-Data). |
| Sequence Column | Numbers the rows in a datalayer by adding a new column containing a sequence integer for each row, starting at 1. Also very useful for *counting* the number of datalayer rows. |
| Sort Filter | Sorts the datalayer rows. For more information, see [The Sort Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419707264919-The-Sort-Filter). |
| Switch Column | Makes data replacements. It's analogous to using both a CASE structure and a REPLACE function in a SQL query. For more information, see [The Switch Column](https://devnet.logianalytics.com/hc/en-us/articles/4419707828631-The-Switch-Column). |
| Time Period Column | Adds a new column to the datalayer containing a time period value (Year, Month, Day, Hour, Minute, etc.) parsed from another column's date-time value. Eliminates the need to parse date-time values using Calculated Columns and script functions. For more information, see [Time Period Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419715572119-Time-Period-Columns). |
| UnCrosstab Filter | Used to "un-pivot" or "reverse pivot" rows of data into columns of data, it converts one row of multi-column data into multiple rows, each with a single data value. For more information, see [The UnCrosstab Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419723184023-The-UnCrosstab-Filter). |
| Unit Conversion Column | Converts column values from one standard measurement to another. For more information, see [The Unit Conversion Column](https://devnet.logianalytics.com/hc/en-us/articles/4419707858071-The-Unit-Conversion-Column). |

Columns that are added to a datalayer using these elements are then available for use and subsequent manipulation themselves, like any other datalayer column, and their values are available using @Data tokens.

## The Include Condition Attribute

All of the datalayer manipulation elements listed in the table above have an **Include Condition** attribute. If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be manipulated or not.
