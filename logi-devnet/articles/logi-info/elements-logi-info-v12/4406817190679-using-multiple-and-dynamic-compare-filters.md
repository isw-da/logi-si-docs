---
title: "Using Multiple and Dynamic Compare Filters"
id: 4406817190679
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817190679-Using-Multiple-and-Dynamic-Compare-Filters
updated_at: 2022-04-06T06:04:31Z
---

# Using Multiple and Dynamic Compare Filters

# Using Multiple and Dynamic Compare Filters

Developers can use two or more *consecutive* Compare Filter elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563455383/compfilter_06.png)

In this case, the comparisons will be evaluated *sequentially*, based on their arrangement from top to bottom in the element tree. So, after the first Compare Filter is applied, only records that meet its criteria will remain in the datalayer to be evaluated for the second Compare Filter.  
Developers can make Compare Filter elements dynamic by using tokens:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563455895/compfilter_07.png)

As mentioned earlier and shown above, the Compare Value attribute can contain tokens such as @Request, so that comparison values are dynamic at runtime.

Sometimes it is necessary to ensure that tokens have default values when running a report. When using @Request tokens, the **Default Request Params** element can be used to create default values for each **@Request** token.

The Compare Filter element also has an **Include Condition** attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575830039/compfilter_08.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be filtered or not.
