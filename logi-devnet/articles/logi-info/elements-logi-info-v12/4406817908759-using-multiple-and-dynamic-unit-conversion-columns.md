---
title: "Using Multiple and Dynamic Unit Conversion Columns"
id: 4406817908759
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817908759-Using-Multiple-and-Dynamic-Unit-Conversion-Columns
updated_at: 2022-04-06T06:09:00Z
---

# Using Multiple and Dynamic Unit Conversion Columns

# Using Multiple and Dynamic Unit Conversion Columns

This topic introduces how to use multiple and dynamic Unit Conversion Columns.

1. Developers can use two or more **consecutive** Unit Conversion Column elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583723031/unitconv_03.png)

In this case, the conversions will be conducted **sequentially**, based on their arrangement from top to bottom in the element tree. So, after the first Unit Conversion Column is applied, the second Unit Conversion Column will be applied.

2. Developers can make Unit Conversion Column elements **dynamic** by using some tokens:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575534743/unitconv_04.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417563076759/unitconv_04a.png)

As shown above, all attributes other than the ID attribute, can use @Request, @Session, and @Constant tokens to make their values dynamic at runtime. Due to the order of processing operations, @Data tokens *cannot* be used here.
Sometimes it is necessary to ensure that tokens have default values when running a report. When using @Request tokens, the **Default Request Params** element can be used to create default values for each **@Request** token.

3. The Unit Conversion Column element also has an **Include Condition** attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575534743/unitconv_04.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417575534871/unitconv_05a.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be filtered or not.
