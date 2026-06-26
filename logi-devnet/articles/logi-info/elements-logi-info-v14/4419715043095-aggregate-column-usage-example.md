---
title: "Aggregate Column Usage Example"
id: 4419715043095
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715043095-Aggregate-Column-Usage-Example
updated_at: 2022-07-17T02:02:39Z
---

# Aggregate Column Usage Example

# Aggregate Column Usage Example

The following example, which provides a count of all customers, illustrates how the Aggregate Column works:

![](https://devnet.logianalytics.com/hc/article_attachments/4419706630423/aggrcol_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419714633367/aggrcol_02a.png)

In the definition shown above, a Data Table and a datalayer element have been added. An **Aggregate Column** element has been added and its attributes have been configured so that it will count the number of customer IDs in the data retrieved into the datalayer.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714633623/aggrcol_03.png)

The resulting count will be placed in a new column, named agrCustCount, in every row of the datalayer, and will be accessible as the token @Data.agrCustCount~. Because the value is in every row, it's available for use with every row of data in the table.
