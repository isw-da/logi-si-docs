---
title: "The Compare Filter"
id: 4419707415575
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707415575-The-Compare-Filter
updated_at: 2022-07-17T01:56:51Z
---

# The Compare Filter

# The Compare Filter

The **Compare Filter** element is used with datalayer elements to filter out data rows. It's analogous to using a *WHERE* clause in a SQL query but, unlike a query, it's applied to the data *after* it's been retrieved into the datalayer.

The following topics discuss the Compare Filter element:

* [Compare Filter Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419722754455-Compare-Filter-Attributes#Attributes)
* [Applying the Compare Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419722753559-Applying-the-Compare-Filter#Applying)
* [Compare Filter Usage Examples](https://devnet.logianalytics.com/hc/en-us/articles/4419715168407-Compare-Filter-Usage-Example#Examples)
* [Using Multiple and Dynamic Compare Filters](https://devnet.logianalytics.com/hc/en-us/articles/4419707416599-Using-Multiple-and-Dynamic-Compare-Filters#Dynamic)
* [Use with a Condition Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419715169431-Use-with-a-Condition-Filter#Condition)

## About the Compare Filter

The Compare Filter element is available for use with all datalayer elements and is particularly useful in conjunction with those lacking query capabilities, such as DataLayer.XML and DataLayer.Web Service.

In operation, the element basically compares a specified data column value against a specified literal or tokenized value and removes all rows from the datalayer where the comparison returns *False*. A variety of comparisons, such as *Equal*, *Greater Than*, *Less Than*, etc., are supported.

This element is quite similar to element, however, it frequently provides *better performance* because it's implemented as a native part of the Logi Data Engine and so does not need to execute script, as the Condition Filter does.
