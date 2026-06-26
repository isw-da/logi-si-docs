---
title: "Conditional Grouping"
id: 4419707615255
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707615255-Conditional-Grouping
updated_at: 2022-07-17T02:24:19Z
---

# Conditional Grouping

# Conditional Grouping

The Group Filter element has an **Include Condition** attribute.

![](https://devnet.logianalytics.com/hc/article_attachments/7522828252823/groupfilter_07.png)

If the value of this attribute is left blank or contains a formula that evaluates to *True*, the element is applied to the datalayer. If the value evaluates to *False*, the element is ignored and does not affect the datalayer. This powerful feature allows you to dynamically determine if the data will be grouped or not.

More than one group filter can be put under any level, specified by the attribute "IncludeCondition" for each group filter. For example, @Request.GroupColumn~ = 'City' or IncludeCondition =@Request.GroupColumn~ = 'Sales'. Once the Report is run without an error, there will be different grouping based on the given token value 'City' or 'Sales'.

![](https://devnet.logianalytics.com/hc/article_attachments/7522799171095/group_filter_replacement.png)

In this case, the token value set in the parameters was 'City' grouping the filter by City:

![](https://devnet.logianalytics.com/hc/article_attachments/7522813427607/filtered_list_replacement_255x168.png)
