---
title: "Applying the DsCondition Filter"
id: 4406817392023
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817392023-Applying-the-DsCondition-Filter
updated_at: 2022-04-06T06:05:49Z
---

# Applying the DsCondition Filter

# Applying the DsCondition Filter

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The DsCondition Filter element discussed here is available in Logi Info v12.5 but has been deprecated in later Info versions; consult the [Release Notes](https://clm.logianalytics.com/rdPage.aspx?rdReport=RelNotesINF) for specific details.
The following example illustrates how the **DsCondition Filter** element is used:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563320983/dscondfilter_01.png)

1. As shown above, a DsCondition Filter element is added as a child of the **DataLayer.Data Services** element..
2. Its **DsExpression** attribute value is set to an expression that compares the data to some value.

The element causes a filtering operation to be included in the processing of the Dataview referenced by the datalayer. All records where the expression evaluates to *False* are removed; in this case, where the values in the *Freight* column equal 50 or less.

The DsCondition Filter element's **DsExpression** attribute also supports script functions and can evaluate them to filter data:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563321111/dscondfilter_02.png)

1. As shown above, a DsCondition Filter element is added as a child of the datalayer element.
2. Its DsExpression attribute value is set to an expression that uses the function *Left()* to compare the data to some value.

The element causes a filtering operation to be included in the processing of the Dataview referenced by the datalayer. All records where the expression evaluates to *False* are removed; in this case, where the values in the *CustomerID* column do not start with "AXG".

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The syntax you use to create expressions is discussed in detail in [Dsexpression Reference](https://devnet.logianalytics.com/hc/en-us/articles/4406822306071-Dsexpression-Reference).
