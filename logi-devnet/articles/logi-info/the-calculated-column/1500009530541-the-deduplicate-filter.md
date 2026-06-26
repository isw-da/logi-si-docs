---
title: "The DeDuplicate Filter"
id: 1500009530541
section: "The Calculated Column"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530541-The-DeDuplicate-Filter
updated_at: 2021-06-17T01:58:16Z
---

# The DeDuplicate Filter

# The DeDuplicate Filter

The **DeDuplicate Filter** element is used with datalayer elements to filter out data rows. It's analogous to using a *DISTINCT* clause in a SQL query but, unlike a query, it's applied to the data *after* it's been retrieved into the datalayer. This topic discusses use of this element.

* About the DeDuplicate Filter
* [Apply the DeDuplicate Filter](#sec1)
* [Use Dynamic DeDuplicate Filters](#sec2)

*This element is not available in Logi Report.*

## About the DeDuplicate Filter

The DeDuplicate Filter element, introduced in v10.1.18, is available for use with all datalayer elements and is particularly useful in conjunction with those lacking query capabilities, such as DataLayer.XML and DataLayer.Web Service.

In operation, the element basically examines the values in one or more specified data columns and removes all rows from the datalayer where duplicate values are found in those columns. The *first* row encountered in a set of rows with duplicate values is the one that's retained.

## Apply the DeDuplicate Filter

The following example illustrates how the **DeDuplicate Filter** is used:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771832983/dedupefilter_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771833239/dedupefilter_01a.png)

1. As shown above, a **DeDuplicate Filter** element is added as a child to a datalayer element.
2. Its **Data Columns** attribute value is set to the names of one or more datalayer columns, using a comma-separated list, whose values will be examined.

In the example above, the sequence of events is that the datalayer reads in all the data from the XML data file, then the DeDuplicate Filter **removes** all rows where duplicate values are found in the specified columns. All that remains in the datalayer for use in the report are rows with unique values in the specified columns.

## Use Dynamic DeDuplicate Filters

1. Developers can make DeDuplicate Filter elements **dynamic** by using tokens:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771832983/dedupefilter_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771833495/dedupefilter_02.png)

As shown above, the Data Columns attribute value can accept tokens such as @Request, so that column names can be dynamic at runtime.

Sometimes it is necessary to ensure that tokens have default values when running a report. When using @Request tokens, the **Default Request Params** element can be used to create default values for each **@Request** token.

2. The DeDuplicate Filter element also has an **Include Condition** attribute:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771832983/dedupefilter_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778677015/dedupefilter_03.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be filtered or not.
