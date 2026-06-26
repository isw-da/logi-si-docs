---
title: "The Switch Column"
id: 4419707828631
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707828631-The-Switch-Column
updated_at: 2022-07-17T01:37:50Z
---

# The Switch Column

# The Switch Column

The **Switch Column** element is used with datalayer elements to make data replacements. It's analogous to using both a CASE structure and a REPLACE function in a SQL query but, unlike a query, it's applied to the data *after* it's been retrieved into the datalayer.

The following topics discuss the Switch Column element:

* [Applying the Switch Column](https://devnet.logianalytics.com/hc/en-us/articles/4419707827607-Applying-the-Switch-Column#sec1)
* [Using Multiple and Dynamic Switch Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419707829527-Using-Multiple-and-Dynamic-Switch-Columns-#sec2)

## About the Switch Column

The **Switch Column** element is available for use with all datalayer elements and is particularly useful in conjunction with those lacking query capabilities, such as DataLayer.XML and DataLayer.Web Service.

In operation, the element basically searches a specified data column in each datalayer row for a specified value and, if found, *replaces**it* with another value. Optionally, the replacement value can be put into a new column that's added to the datalayer, leaving the original column's data intact.

This is useful for replacing storage-friendly codes, such "1,2,3..." withreadable text, such as "Overnight Delivery,Second Day Delivery, Ground Delivery..." or "1, 0" into "True, False". These replacements are temporary (they happen onlyin the cached datalayer) and don't effect the original data in the datasource, so they're great for increasinglegibility in reports.
