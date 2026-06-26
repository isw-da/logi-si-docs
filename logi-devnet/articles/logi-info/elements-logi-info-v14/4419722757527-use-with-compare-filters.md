---
title: "Use with Compare Filters"
id: 4419722757527
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722757527-Use-with-Compare-Filters
updated_at: 2022-07-17T02:24:57Z
---

# Use with Compare Filters

# Use with Compare Filters

For improved performance, Condition Filters can also be used in combination with [The Compare Filter](https://devnet.logianalytics.com/hc/en-us/articles/4419707415575-The-Compare-Filter) to create complex expressions that include ANDs and ORs and levels of parentheses.

![](https://devnet.logianalytics.com/hc/article_attachments/7522817528343/condfilter_06.png)

For example, consider the element arrangement shown above. For each row of the datalayer, the three **Compare Filters** will be evaluated first. Each of them will produce a *True* or *False* value as a result of their comparison operations. Those values will be assigned to @Compare tokens which include the element ID, for example: @Compare.CompareFilter1~. The scope of these tokens is
limited to the parent Condition Filter.
After all of the Compare Filters are evaluated, the **Condition Filter** will be evaluated and its **Condition** attribute value can include expressions that use the @Compare tokens. For example, the Condition attribute value above might be:

@Compare.CompareFilter1~ AND (@Compare.CompareFilter2~ OR @Compare.CompareFilter3~)

And, of course, you can also use other types of tokens and literal values in the Condition attribute to get the expression you need, such as:

@Data.UnitPrice~ <= 100 AND (@Compare.CompareFilter1~ OR @Compare.CompareFilter2~)

You may be able achieve the same results with complicated scripting for the Condition attribute value, however, in most cases use of multiple Compare Filters as shown in this example will produce better performance than scripting.
