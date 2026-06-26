---
title: "The Contain Filter"
id: 4419707426199
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707426199-The-Contain-Filter
updated_at: 2022-07-17T01:56:17Z
---

# The Contain Filter

# The Contain Filter

The **Contain Filter** element is used with datalayer elements to filter out data rows. It's analogous to using a *WHERE**x CONTAINS y* clause in a SQL query but, unlike a query, it's applied to the data *after* it's been retrieved into the datalayer.

The following topics discuss the Contain Filter element:

* [Applying the Contain Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419722771607-Applying-the-Contain-Filter#sec1)
* [Using Multiple and Dynamic Contain Filters](https://devnet.logianalytics.com/hc/en-us/articles/4419707428119-Using-Multiple-and-Dynamic-Contains#sec2)

## About the Contain Filter

The Contain Filter element is available for use with all datalayer elements and is particularly useful in conjunction with those lacking query capabilities,such as DataLayer.XML and DataLayer.Web Service.

In operation, the element basically searches a specified data column valuefor a specified text string and removes all rows from the datalayer where the string is not found in the column.

This element is similar to element, however, it frequently provides *better performance* because it's implemented as a native part of the Logi Data Engine and so does not need to execute script, asthe Condition Filter does.
