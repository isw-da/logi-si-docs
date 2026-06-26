---
title: "DsAggregate Column Usage Example"
id: 4406822303127
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822303127-DsAggregate-Column-Usage-Example
updated_at: 2022-04-06T06:05:49Z
---

# DsAggregate Column Usage Example

# DsAggregate Column Usage Example

The following example, which provides a count of all customers, illustrates how the DsAggregate Column works:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575726999/dsaggrcol_01.png)

In the example shown above, a data table and a DataLayer.Data Services element have been added. A **DsAggregate Column** element has been added beneath the datalayer and its attributes have been configured so that it will count the number of customer IDs in the data.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583966743/dsaggrcol_02.png)

The resulting count will be placed in a new column, named "agrCustCount", in every row of the datalayer, and will be accessible as the token @Data.agrCustCount~. Because the value is in every row, it's available for use with every row of data in the table.

## Dynamic Application

The DsAggregate Column element has an **Include Condition** attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575727511/dsaggrcol_03.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the Dataview. If the value evaluates to *False*, the element is ignored and does not affect the Dataview. This powerful feature allows you to dynamically determine if the DsAggregate Column will be added to the Dataview or not.
