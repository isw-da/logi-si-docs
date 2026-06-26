---
title: "Applying a Dynamic Filter"
id: 4406822335639
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822335639-Applying-a-Dynamic-Filter
updated_at: 2022-04-06T06:06:14Z
---

# Applying a Dynamic Filter

# Applying a Dynamic Filter

This topic provides an example that illustrates use of the Compare Filter, with dynamic filtering criteria.

1. Developers can use two or more **consecutive** Compare Filter elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575699223/filteringdls_02.png)

In this case, the comparisons will be evaluated **sequentially**, based on their arrangement from top to bottom in the element tree. So, after the first Compare Filter is applied, only records that meet its criteria will remain in the datalayer to be evaluated for the second Compare Filter.

2. Developers can make Compare Filter elements **dynamic** by using tokens:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563289623/filteringdls_03.png)

As shown above, Compare Value attribute can contain tokens such as @Request, so that comparison values are dynamic at runtime.
Sometimes it is necessary to ensure that tokens have default values when running a report. When using @Request tokens, the **Default Request Params** element can be used to create default values for each **@Request** token.
3. The Compare Filter element also has an **Include Condition** attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563289751/filteringdls_04.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be filtered or not.
