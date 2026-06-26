---
title: "Preparing for Hierarchical Data"
id: 4406817217687
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817217687-Preparing-for-Hierarchical-Data
updated_at: 2022-04-06T06:04:41Z
---

# Preparing for Hierarchical Data

# Preparing for Hierarchical Data

Hierarchical data is *multi-layered* data that contains numerous
parent-child relationships. For example, for each customer, an
invoice-style report may contain customer contact information and data for
multiple orders. If the data for several customers is returned from a
query and each customer has placed one or more orders, then a
*hierarchical dataset* exists. The only rule you need to follow when
creating a template for hierarchical data is that each level in the
hierarchy must have its own row.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584075031/createxltemp_04_507x199.png)

For example, the report template shown above is configured properly for
three levels of hierarchical data. If additional data at the third level
is retrieved, data in the correct columns will be extended downward in
additional rows.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563436823/createxltemp_05.png)

However, the example shown above *is not* configured properly
for multiple levels of data. If additional data at the second or third
level is retrieved, data for all three levels will be extended downward in
additional and meaningless rows.
