---
title: "The Condition Filter"
id: 4406822191255
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822191255-The-Condition-Filter
updated_at: 2022-04-06T06:04:32Z
---

# The Condition Filter

# The Condition Filter

The **Condition Filter** element is used with datalayer elements to filter out data rows that don't meet certain criteria.

The following topics discuss the use of this filter:

* About the Condition Filter
* [Applying the Condition Filter](https://devnet.logianalytics.com/hc/en-us/articles/4406822189719-Applying-the-Condition-Filter)
* [Using Multiple and Dynamic Condition Filters](https://devnet.logianalytics.com/hc/en-us/articles/4406817195031-Using-Multiple-and-Dynamic-Condition-Filters)
* [Use with Compare Filters](https://devnet.logianalytics.com/hc/en-us/articles/4406817193879-Use-with-Compare-Filters)

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png)  In many circumstances you will find that [The Compare Filter](https://devnet.logianalytics.com/hc/en-us/articles/4406817189655-The-Compare-Filter) provides similar functionality and better performance.

## About the Condition Filter

The **Condition Filter** element is used with datalayer elements to filter out data rows that don't meet specified criteria. It's analogous to using a *WHERE* clause in a SQL query but, unlike a query, it's applied to data *after* it's been retrieved into the datalayer.
The Condition Filter is available to all datalayer elements but is most useful when used with those lacking conditional query capabilities, such as DataLayer.XML and DataLayer.CSV.
