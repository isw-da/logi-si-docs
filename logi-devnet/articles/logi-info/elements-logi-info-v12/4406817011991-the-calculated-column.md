---
title: "The Calculated Column"
id: 4406817011991
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817011991-The-Calculated-Column
updated_at: 2022-04-06T06:03:21Z
---

# The Calculated Column

# The Calculated Column

The **Calculated Column** element adds a new column to a datalayer containinga value that's the result of a formula. The formula can include data from other columns, tokens, and literals, and is evaluated for every row in the datalayer.

The following topics discuss the Calculated Column element:

* [Calculated Column Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4406817009815-Calculated-Column-Attributes#Attributes)
* [Calculated Column Usage Examples](https://devnet.logianalytics.com/hc/en-us/articles/4406817010839-Calculated-Column-Usage-Examples#Simple)
* [NaN Errors](https://devnet.logianalytics.com/hc/en-us/articles/4406822103063-NaN-Errors#Errors)

## About the Calculated Column

The Calculated Column is similar to other elements designed to *extend* the data available in a datalayer. Like the **Aggregate Column** element, the Calculated Column is added as a child element beneath a datalayer and adds a new column to the datalayer. This column value is *derived data* which is accessible using an @Data token.

The new column's value results from evaluating a formula, for each row in the datalayer. This calculated value is populated in the new column in every
row of the datalayer and can be used in further calculations, Summary Rows, Link Params,
etc.

Similar calculations could be performed within SQL queries and *may* offer better performance when done by the database server. However, the Calculated Column element allows calculations to be performed on data from other sources too, such as web services and data files, that do not themselves offer SQL-like queries.
