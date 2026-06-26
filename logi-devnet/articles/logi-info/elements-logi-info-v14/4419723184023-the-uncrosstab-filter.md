---
title: "The UnCrosstab Filter"
id: 4419723184023
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723184023-The-UnCrosstab-Filter
updated_at: 2022-07-17T01:36:44Z
---

# The UnCrosstab Filter

# The UnCrosstab Filter

The **UnCrosstab Filter** element is used with datalayer elements to "un-pivot" or "reverse pivot" rows of data into columns of data. It converts one row of multi-column data into multiple rows, each with a single data
value.

The following topics discuss the UnCrosstab Filter element:

* [Applying the UnCrosstab Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419723183127-Applying-the-UnCrosstab-Filter#sec1)
* [Using Dynamic UnCrosstab Filters](https://devnet.logianalytics.com/hc/en-us/articles/4419715494423-Using-Dynamic-UnCrosstab-Filters-#sec2)

## About the UnCrosstab Filter

The **UnCrosstab Filter** element is available for use with all datalayer elements and is the functional opposite of the Crosstab Filter element.
In operation, the element basically converts each row in the datalayer, each of which has multiple columns, into multiple rows, each of which has one value column.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707082007/uncrosstab_01.png)

It's a little easier to understand the filter's actions when you can see the effect limited to one row, in a Data Table, as shown above.
This "un-pivot" action normalizes the data on the fly and, among other applications, can be really useful when having to work with data imported from spreadsheets.
