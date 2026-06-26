---
title: "Using Dynamic DeDuplicate Filters"
id: 4406817361303
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817361303-Using-Dynamic-DeDuplicate-Filters
updated_at: 2022-04-06T06:05:36Z
---

# Using Dynamic DeDuplicate Filters

# Using Dynamic DeDuplicate Filters

This topic describes how to use dynamic DeDuplicate Filters.

1. Developers can make DeDuplicate Filter elements **dynamic** by using tokens:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583987095/dedupefilter_01.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417563344535/dedupefilter_02.png)

As shown above, the Data Columns attribute value can accept tokens such as @Request, so that column names can bedynamic at runtime.
Sometimes it is necessary to ensure that tokens have default values when running a report. When using @Request tokens, the **Default Request Params** element can be used to create default values for each **@Request** token.

2. The DeDuplicate Filter element also has an **Include Condition** attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583987095/dedupefilter_01.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417563344663/dedupefilter_03.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be filtered or not.
