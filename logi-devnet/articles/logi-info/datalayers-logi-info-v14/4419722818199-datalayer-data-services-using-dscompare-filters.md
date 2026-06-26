---
title: "DataLayer.Data Services - Using DsCompare Filters"
id: 4419722818199
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722818199-DataLayer-Data-Services-Using-DsCompare-Filters
updated_at: 2022-07-17T01:53:47Z
---

# DataLayer.Data Services - Using DsCompare Filters

# DataLayer.Data Services - Using DsCompare Filters

The **DsCompare Filter**, which is used with a DsCondition Filter element, is quite similar to the standard [The Compare Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419707415575-The-Compare-Filter) element. It may be easier to organize a complex filter using this element.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706748439/dlds_04.png)

Consider a typical arrangement like the one shown above, which just uses a DsCondition Filter. The DsExpression attribute value used is:

[Freight] > 50 AND ([CustomerID] == 'HANAR' OR [CustomerID] == 'MAGAA')

There are three comparisons that must evaluate to *True* in order for a row in the data to be retained. Now let's see how we can might improve performance by spreading those evaluations out, using DsCompare Filters:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699646231/dlds_05.png)

In the example above, three DsCompare Filter elements have been added beneath the DsCondition Filter element. Each has a unique ID and its attributes are set to handle one of the three comparisons from our previous example and each of these "sub evaluations" will return a *True* or *False* result.
Finally, we change the DsCondition Filter element's DsExpression attribute to evaluate the results of the three DsCompare Filter "sub evaluations", like this:

@Compare.compareFreight~ AND (@Compare.compareCustomer1~ OR @Compare.compareCustomer2~)

Note the use of a special token, @Compare, to represent the results of each "sub evaluation".
This approach not only provides better performance for large data sets, it may also be easier to use when there are many more comparisons and/or more complexity involved.
This table provides information about the DsCompare Filter element's **Compare Type** options:

| Operator | Description |
| --- | --- |
| =, <>, <, >, <=, >= | Basic standard comparison operators. String types evaluated are culture-sensitive. |
| InList | For the row to be retained, the value in the specified Data Column *must* be one of the values specified in a comma-separated list in the Compare Value. |
| StartsWith | For the row to be retained, the text value in the specified Data Column *must* start with the text in the Compare Value. |
