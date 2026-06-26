---
title: "The Color Range Column"
id: 4419722746263
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722746263-The-Color-Range-Column
updated_at: 2022-07-17T01:57:11Z
---

# The Color Range Column

# The Color Range Column

The **Color Range Column** element, introduced in v12.6, adds new columns, containing color values that are correlated to data, to a datalayer. This allows you to dynamically set the background and text colors in individual Data Table cells.

The following topics introduce the Color Range Column element:

* [Color Range Column Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419715162391-Color-Range-Column-Attributes#Attributes)
* [Color Range Column Usage Examples: Numeric Data](https://devnet.logianalytics.com/hc/en-us/articles/4419722747159-Color-Range-Column-Usage-Examples-Numeric-Data#Numeric)
* [Color Range Column Usage Examples: Text Data](https://devnet.logianalytics.com/hc/en-us/articles/4419715163415-Color-Range-Column-Usage-Example-Text-Data#Text)

## About the Color Range Column

The **Color Range Column** is similar to other elements designed to *extend* the data available in a datalayer. It's added as a child element beneath a datalayer and adds a two new columns to the datalayer. These column values are derived data, accessible using @Data tokens.

The new columns' values result from testing other column data values against specified ranges, for each row in the datalayer, and correlating them to specified color values. These color values populate the new columns in every
row of the datalayer and, via their @Data tokens, can be used to dynamically set background and text color values for each Data Table cell.

When definitions using Color Range Columns are exported to Excel or to PDF, the Data Table cell text and background colors are exported as well.

Each Color Range Column element evaluates one other data column; multiple Color Range Column elements can be used, if needed.
