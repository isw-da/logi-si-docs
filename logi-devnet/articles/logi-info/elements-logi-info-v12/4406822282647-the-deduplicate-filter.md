---
title: "The DeDuplicate Filter"
id: 4406822282647
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822282647-The-DeDuplicate-Filter
updated_at: 2022-04-06T06:05:36Z
---

# The DeDuplicate Filter

# The DeDuplicate Filter

The **DeDuplicate Filter** element is used with datalayer elements to filter out data rows. It's analogous to using a *DISTINCT* clause in a SQL query but, unlike a query, it's applied to the data *after* it's been retrieved into the datalayer.

The following topics discuss the DeDuplicate Filter element:

* [Applying the DeDuplicate Filter](https://devnet.logianalytics.com/hc/en-us/articles/4406817360151-Applying-the-DeDuplicate-Filter#sec1)
* [Using Dynamic DeDuplicate Filters](https://devnet.logianalytics.com/hc/en-us/articles/4406817361303-Using-Dynamic-DeDuplicate-Filters#sec2)

## About the DeDuplicate Filter

The DeDuplicate Filter element is available for use with all datalayer elements and is particularly useful in conjunction with those lacking query capabilities, such as DataLayer.XML and DataLayer.Web Service.

In operation, the element basically examines the values in one or more specified data columns and removes all rows from the datalayer where duplicate values are found in those columns. The *first* row encountered in a set of rows with duplicate values is the one that's retained.
