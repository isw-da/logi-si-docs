---
title: "Using Multiple and Dynamic Contains"
id: 4419707428119
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707428119-Using-Multiple-and-Dynamic-Contains
updated_at: 2022-07-17T02:24:53Z
---

# Using Multiple and Dynamic Contains

# Using Multiple and Dynamic Contains

This topic describes how to use multiple and dynamic contains.

1. Developers can use two or more **consecutive** Contain Filter elements:

![](https://devnet.logianalytics.com/hc/article_attachments/7522862209687/containfilter_02.png)

In this case, the searches will be conducted **sequentially**, based on their arrangement from top to bottom in the element tree. So, after the first Contain Filter is applied, only records that meet its criteria will remain in the datalayer to be evaluated bythe second Contain Filter.

2. Developers can make Contain Filter elements **dynamic** by using tokens:

![](https://devnet.logianalytics.com/hc/article_attachments/7522853920535/containfilter_01.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522853932183/containfilter_03.png)

As shown above, the Search String attribute value can contain tokens such as @Request, so that comparison values are dynamic at runtime.
Sometimes it is necessary to ensure that tokens have default values when running a report. When using @Request tokens, the **Default Request Params** element can be used to create default values for each **@Request** token.

3. The Contain Filter element also has an **Include Condition** attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/7522853920535/containfilter_01.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522847890455/containfilter_04.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be filtered or not.
