---
title: "The Condition Filter"
id: 4419722756503
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722756503-The-Condition-Filter
updated_at: 2022-07-17T02:08:41Z
---

# The Condition Filter

# The Condition Filter

The **Condition Filter** element is used with datalayer elements to filter out data rows that don't meet certain criteria.

The following topics discuss the use of this element:

* About the Condition Filter
* [Applying the Condition Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419722755607-Applying-the-Condition-Filter)
* [Using Multiple and Dynamic Condition Filters](https://devnet.logianalytics.com/hc/en-us/articles/4419707417623-Using-Multiple-and-Dynamic-Condition-Filters)
* [Use with Compare Filters](https://devnet.logianalytics.com/hc/en-us/articles/4419722757527-Use-with-Compare-Filters)

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png)  In many circumstances you will find that [The Compare Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419707415575-The-Compare-Filter) provides similar functionality and better performance.

## About the Condition Filter

The **Condition Filter** element is used with datalayer elements to filter out data rows that don't meet specified criteria. It's analogous to using a *WHERE* clause in a SQL query but, unlike a query, it's applied to data *after* it's been retrieved into the datalayer.
The Condition Filter is available to all datalayer elements but is most useful when used with those lacking conditional query capabilities, such as DataLayer.XML and DataLayer.CSV.
