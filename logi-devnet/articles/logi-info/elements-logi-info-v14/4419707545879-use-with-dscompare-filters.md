---
title: "Use with DsCompare Filters"
id: 4419707545879
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707545879-Use-with-DsCompare-Filters
updated_at: 2022-07-17T01:50:49Z
---

# Use with DsCompare Filters

# Use with DsCompare Filters

For improved performance, DsCondition Filters can also be used in combination with **DsCompare Filter** elements to create complex expressions that include ANDs and ORs and operations grouping.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714742551/dscondfilter_06.png)

For example, consider the element arrangement shown above. For each row of the Dataview, the three **DsCompare Filters** will be evaluated first. Each of them will produce a *True* or *False* value as a result of their comparison operations. Those values will be assigned to @Compare tokens which include the element ID, for example: @Compare.CompareFilter1~. The scope of these tokens is
limited to the parent DsCondition Filter.

After all of the DsCompare Filters are evaluated, the **DsCondition Filter** will be evaluated and its **DsExpression** attribute value can include expressions that use the @Compare tokens. For example, the complete DsExpression attribute value above might be:

@Compare.CompareFilter1~ AND (@Compare.CompareFilter2~ OR @Compare.CompareFilter3~)

And, of course, you can also use other types of tokens and literal values in the DsCondition attribute to get the expression you need, such as:

[UnitPrice] <= 100 AND (@Compare.CompareFilter1~ OR @Compare.CompareFilter2~)

You may be able achieve the same results with complicated scripting for the DsExpression attribute value, however, in most cases use of multiple DsCompare Filters as shown in this example will produce better performance.
