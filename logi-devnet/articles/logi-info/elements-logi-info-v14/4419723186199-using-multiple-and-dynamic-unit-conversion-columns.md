---
title: "Using Multiple and Dynamic Unit Conversion Columns"
id: 4419723186199
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723186199-Using-Multiple-and-Dynamic-Unit-Conversion-Columns
updated_at: 2022-07-17T02:23:25Z
---

# Using Multiple and Dynamic Unit Conversion Columns

# Using Multiple and Dynamic Unit Conversion Columns

This topic introduces how to use multiple and dynamic Unit Conversion Columns.

1. Developers can use two or more **consecutive** Unit Conversion Column elements:

![](https://devnet.logianalytics.com/hc/article_attachments/7522788994199/unitconv_03.png)

In this case, the conversions will be conducted **sequentially**, based on their arrangement from top to bottom in the element tree. So, after the first Unit Conversion Column is applied, the second Unit Conversion Column will be applied.

2. Developers can make Unit Conversion Column elements **dynamic** by using some tokens:

![](https://devnet.logianalytics.com/hc/article_attachments/7522757471255/unitconv_04.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522775744919/unitconv_04a.png)

As shown above, all attributes other than the ID attribute, can use @Request, @Session, and @Constant tokens to make their values dynamic at runtime. Due to the order of processing operations, @Data tokens *cannot* be used here.
Sometimes it is necessary to ensure that tokens have default values when running a report. When using @Request tokens, the **Default Request Params** element can be used to create default values for each **@Request** token.

3. The Unit Conversion Column element also has an **Include Condition** attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/7522757471255/unitconv_04.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522757486359/unitconv_05a.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be filtered or not.
