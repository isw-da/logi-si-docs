---
title: "Using Multiple and Dynamic Switch Columns "
id: 4406817864343
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817864343-Using-Multiple-and-Dynamic-Switch-Columns
updated_at: 2022-04-06T06:08:42Z
---

# Using Multiple and Dynamic Switch Columns 

# Using Multiple and Dynamic Switch Columns

This topic introduces how to use multiple and dynamic Switch Columns.

1. Developers can use two or more *consecutive* Switch Column elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583734551/switchcol_04.png)

In this case, the operations will be conducted **sequentially**, based on their arrangement from top to bottom in the element tree. So, after the first Switch Column is applied, rows that may have been changed by it will be evaluated bythe second Switch Column.

2. The Switch Column element also has an **Include Condition** attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583734807/switchcol_01.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417583735063/switchcol_05.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be altered or not.
