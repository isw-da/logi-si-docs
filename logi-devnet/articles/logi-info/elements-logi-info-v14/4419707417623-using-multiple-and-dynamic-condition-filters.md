---
title: "Using Multiple and Dynamic Condition Filters"
id: 4419707417623
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707417623-Using-Multiple-and-Dynamic-Condition-Filters
updated_at: 2022-07-17T02:24:58Z
---

# Using Multiple and Dynamic Condition Filters

# Using Multiple and Dynamic Condition Filters

You can use two or more Condition Filter elements together:

![](https://devnet.logianalytics.com/hc/article_attachments/7522832327703/condfilter_03.png)

In this case, the conditions will be evaluated *sequentially*, based on their arrangement from top to bottom in the element tree. So, in the example above, after the first condition filter is applied, only records that meet its criteria will remain in the datalayer to be evaluated by the second condition filter.  
 
You can also make Condition Filter elements *dynamic* by using tokens within expressions:

![](https://devnet.logianalytics.com/hc/article_attachments/7522879191447/condfilter_04.png)

As shown above, condition formulae can contain tokens such as @Request, so that comparison values are dynamic at runtime.
Sometimes it is necessary to ensure that tokens have default values when running a report. When using @Request tokens, the **Default Request Params** element can be used to create default values for each Request variable.  
 
Like other filter elements, the Condition Filter has an **Include Condition** attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/7522879201047/condfilter_05.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows you to dynamically determine if the datalayer will be filtered or not.
