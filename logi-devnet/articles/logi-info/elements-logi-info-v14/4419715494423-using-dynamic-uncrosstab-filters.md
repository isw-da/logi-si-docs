---
title: "Using Dynamic UnCrosstab Filters "
id: 4419715494423
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715494423-Using-Dynamic-UnCrosstab-Filters
updated_at: 2022-07-17T02:23:26Z
---

# Using Dynamic UnCrosstab Filters 

# Using Dynamic UnCrosstab Filters

The UnCrosstab Filter element also has an **Include Condition** attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/7522803508119/uncrosstab_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522803517719/uncrosstab_03.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be altered or not.
