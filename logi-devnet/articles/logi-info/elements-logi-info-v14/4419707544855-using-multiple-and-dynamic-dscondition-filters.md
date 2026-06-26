---
title: "Using Multiple and Dynamic DsCondition Filters"
id: 4419707544855
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707544855-Using-Multiple-and-Dynamic-DsCondition-Filters
updated_at: 2022-07-17T02:24:31Z
---

# Using Multiple and Dynamic DsCondition Filters

# Using Multiple and Dynamic DsCondition Filters

Developers can use two or more DsCondition Filter elements:

![](https://devnet.logianalytics.com/hc/article_attachments/7522814677783/dscondfilter_03.png)

In this case, they will be processed in the Dataview *sequentially*, based on their arrangement from top-to-bottom in the element tree. So, in the example above, after the first filter is applied, only records that meet its criteria will remain to be processed in the Dataview by the second filter.

You can also make DsCondition Filter elements *dynamic* by using tokens within their expressions:

![](https://devnet.logianalytics.com/hc/article_attachments/7522825596567/dscondfilter_04.png)

As shown above, DsExpression expressions can contain tokens such as @Request, so that comparison values are dynamic at runtime.

Sometimes it is necessary to ensure that tokens have default values when running a report. When using @Request tokens, the **Default Request Params** element can be used to create default values for each request variable.

Like other filter elements, the DsCondition Filter has an **Include Condition** attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/7522844951191/dscondfilter_05.png)

If the value of this attribute is left blank or contains an expression that evaluates to *True*, the element is applied to the Dataview. If the value evaluates to *False*, the element is ignored and has no affect. This powerful feature allows you to dynamically determine if filtering will be applied.
