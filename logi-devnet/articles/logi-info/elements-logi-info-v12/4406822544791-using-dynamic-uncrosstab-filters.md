---
title: "Using Dynamic UnCrosstab Filters "
id: 4406822544791
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822544791-Using-Dynamic-UnCrosstab-Filters
updated_at: 2022-04-06T06:08:59Z
---

# Using Dynamic UnCrosstab Filters 

# Using Dynamic UnCrosstab Filters

The UnCrosstab Filter element also has an **Include Condition** attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583724439/uncrosstab_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417583724567/uncrosstab_03.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be altered or not.
