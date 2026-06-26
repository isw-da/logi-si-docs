---
title: "The Aggregate Column"
id: 1500009513922
section: "The Calculated Column"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009513922-The-Aggregate-Column
updated_at: 2023-02-03T22:48:03Z
---

# The Aggregate Column

# The Aggregate Column

An Aggregate Column element adds a new column to the datalayer that represents an aggregated value of the data in one of the other columns in the datalayer.

* About the Aggregate Column
* [Usage Example](#Simple)

## About the Aggregate Column

The Aggregate Column is similar to other elements designed to **extend** the data available in a datalayer. Like the **Calculated Column** element, the Aggregate Column is added as a child element beneath a datalayer and adds a **new column** to the datalayer. This column contains **derived data** which is accessible using an @Data token.

The new column's value is the result of aggregating the value of the data in one column, for all rows, in the datalayer. The aggregated value is populated in the new column in every
row of the datalayer so that it can be used in further calculations, Summary Rows, Link Params,
etc. It is also populated in the top-level row, allowing reference to the value
anywhere in the report outside of a Data Table.

Similar aggregations can be performed within SQL queries and may offer faster performance when done by the database server. However, the Aggregate Column element allows aggregations to be performed on data from other sources too, such as web services and data files, that do not themselves offer aggregating functions.

## Dynamic Application

Beginning in v10.0.319, the Aggregate Column element has an **Include Condition** attribute:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778747799/aggrcol_01.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the Aggregate Column will be added to the datalayer or not.

## Usage Example

The following example, which provides a count of all customers, illustrates how the Aggregate Column works:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778748055/aggrcol_02.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778748311/aggrcol_02a.png)

In the definition shown above, a data table and a datalayer element have been added. An **Aggregate Column** element has been added and its attributes have been configured so that it will count the number of customer IDs in the data retrieved into the datalayer.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771947671/aggrcol_03.png)

The resulting count will be placed in a new column, named agrCustCount, in every row of the datalayer, and will be accessible as the token @Data.agrCustCount~. Because the value is in every row, it's available for use with every row of data in the table.

### Aggregate Column Attributes

The attributes for the Aggregate Column element are described below:

| Attribute | Description |
| --- | --- |
| Aggregate Column | (Required) The name of the column in the datalayer that contains the values to be aggregated. |
| Aggregate Function | (Required) The aggregating function to be applied to the column named in the previous attribute. The available functions include:   * Average * Concat (added in v10.0.319 - see discussion below) * Count * Distinct Count * Max * Median * Min * Mode * Std Deviation * Sum   In prior versions, aggregations *included* columns with Null values by default. This behavior has been changed and Null values are now *excluded* by default. Create the constant rdCalculationsIncludeNulls and set it to *True* if you want to restore the old behavior. |
| ID | (Required) The unique element ID for the Aggregate Column element. |
| Concat Separator | (v10.0.319) The character used to separate concatenated text values, if any. Default: *comma* |
| Data Type | The data type of the column named in the Aggregate Column attribute value. |
| Include Condition | (v10.0.319) Determines if the aggregation will be applied. If left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. |

### The Concat Function

The Concat function, introduced in v10.0.319, builds a string of concatenated values by taking all the text in the specified data column and concatenating it together using the default (a comma) or specified separator character.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771949207/aggrcol_04.png)

This can be useful for a variety of purposes, including creating default values for select lists.
