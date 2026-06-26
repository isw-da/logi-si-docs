---
title: "Applying the DeDuplicate Filter"
id: 4406817360151
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817360151-Applying-the-DeDuplicate-Filter
updated_at: 2022-04-06T06:05:37Z
---

# Applying the DeDuplicate Filter

# Applying the DeDuplicate Filter

The following example illustrates how the **DeDuplicate Filter** is used:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583987095/dedupefilter_01.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417563344919/dedupefilter_01a.png)

1. As shown above, a **DeDuplicate Filter** element is added as a child to a datalayer element.
2. Its **Data Columns** attribute value is set to the names of one or more datalayer columns, usinga comma-separated list, whose values will be examined.

In the example above, the sequence of events is that the datalayer reads in all the data from the XML data file, then the DeDuplicate Filter **removes** all rows where duplicate values are found in the specified columns. All that remains in the datalayer for use in the report are rows with unique values in the specified columns.
