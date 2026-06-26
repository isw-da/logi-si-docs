---
title: "The Aggregate Column"
id: 4419707269527
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707269527-The-Aggregate-Column
updated_at: 2022-07-17T02:25:28Z
---

# The Aggregate Column

# The Aggregate Column

An Aggregate Column element adds a new column to the datalayer that represents an aggregated value of the data in one of the other columns in the datalayer.

The following topics discuss the Aggregate Column element:

* [Aggregate Column Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419700087831-Aggregate-Column-Attributes)
* [Aggregate Usage Example](https://devnet.logianalytics.com/hc/en-us/articles/4419715043095-Aggregate-Column-Usage-Example)

## About the Aggregate Column

The Aggregate Column is similar to other elements designed to **extend** the data available in a datalayer. Like the **Calculated Column** element, the Aggregate Column is added as a child element beneath a datalayer and adds a **new column** to the datalayer. This column contains **derived data** which is accessible using an @Data token.

The new column's value is the result of aggregating the value of the data in one column, for all rows, in the datalayer. The aggregated value is populated in the new column in every
row of the datalayer so that it can be used in further calculations, Summary Rows, Link Params,
etc. It is also populated in the top-level row, allowing reference to the value
anywhere in the report outside of a Data Table.

Similar aggregations can be performed within SQL queries and may offer faster performance when done by the database server. However, the Aggregate Column element allows aggregations to be performed on data from other sources too, such as web services and data files, that do not themselves offer aggregating functions.

### Dynamic Application

The Aggregate Column element has an **Include Condition** attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/7522882073879/aggrcol_01.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the Aggregate Column will be added to the datalayer or not.
