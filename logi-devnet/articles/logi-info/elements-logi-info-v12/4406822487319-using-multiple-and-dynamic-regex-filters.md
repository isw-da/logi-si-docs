---
title: "Using Multiple and Dynamic RegEx Filters"
id: 4406822487319
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822487319-Using-Multiple-and-Dynamic-RegEx-Filters
updated_at: 2022-04-06T06:08:19Z
---

# Using Multiple and Dynamic RegEx Filters

# Using Multiple and Dynamic RegEx Filters

This topic introduces how to use multiple and dynamic RegEx filters.

1. Developers can use two or more **consecutive** RegEx Filter elements:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575558295/regexfilter_02.png)

In this case, the matches will be evaluated **sequentially**, based on their arrangement from top to bottom in the element tree. So, after the first RegEx Filter is applied, only records that match its pattern will remain in the datalayer to be matched to the second RegEx Filter.
2. The RegEx Filter element also has an **Include Condition** attribute:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563110807/regexfilter_01.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417563111063/regexfilter_03.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows developers to dynamically determine if the datalayer will be filtered or not.
