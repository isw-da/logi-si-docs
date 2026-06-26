---
title: "The Crosstab Filter"
id: 4406822216727
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822216727-The-Crosstab-Filter
updated_at: 2022-04-06T06:04:46Z
---

# The Crosstab Filter

# The Crosstab Filter

The **Crosstab Filter** element is used with datalayer elements to "pivot" *columns* of data into *rows* of data. It converts related rows of data into a single row with multiple columns.

The following topics discuss the Crosstab Filter element:

* [Applying the Crosstab Filter to a Crosstab Table](https://devnet.logianalytics.com/hc/en-us/articles/4406822214935-Applying-the-Crosstab-Filter-to-a-Crosstab-Table#DataTable)
* [Applying the Crosstab Filter to a Chart](https://devnet.logianalytics.com/hc/en-us/articles/4406822215831-Applying-the-Crosstab-Filter-to-a-Chart#Chart)
* [Using Dynamic Crosstab Filters](https://devnet.logianalytics.com/hc/en-us/articles/4406817227415-Using-Dynamic-Crosstab-Filters#Dynamic)

## About the Crosstab Filter

The **Crosstab Filter** element is available for use with all datalayer elements and is the functional opposite of the UnCrosstab Filter element.
In operation, the element basically converts all rows in the datalayer which share a common identifying value into a single row with multiple columns that contain the column values from all the original rows.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563430167/crosstab_01.png)

It's a little easier to understand the filter's actions when you can see the effect limited to one set of related rows, as shown above.

This "pivot" action denormalizes the data on the fly and, among other applications, can be really useful when having to work with data imported from spreadsheets.

To configure a Crosstab Filter, you specify datalayer columns as the **Crosstab Column**, the **Label Column**, and the **Value Column**, and select a **Value Function** (*Any*, *Average*, *Count*, *DistinctCount, Median*, *Mode*, *StdDev*, or *Sum*).

When the filter runs, a row is generated in the resulting datalayer for each distinct value in the designated Label Column, and a column is generated for each distinct value found in the designated Crosstab Column. The columns or "cells" in the resulting datalayer are derived from
the designated Value Column by adding, counting, averaging, etc. (depending on the Value Function chosen) all the values unique to each Crosstab Column and Label Column.

Datalayer rows that initially have blank Label Column values or blank Crosstab Column values are *not* included by default in the resulting datalayer. To include these rows, add a Calculated Column child element to the datalayer *before* the Crosstab Filter, configure it to provide a non-blank value if a blank value is found, then use it as the Crosstab Column or Label Column.

Other datalayer filter elements you may choose to add to your definition must not be configured to affect the columns designated when configuring the Crosstab Filter.
