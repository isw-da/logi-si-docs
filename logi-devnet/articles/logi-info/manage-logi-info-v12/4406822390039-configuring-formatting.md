---
title: "Configuring Formatting "
id: 4406822390039
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822390039-Configuring-Formatting
updated_at: 2022-04-06T06:06:56Z
---

# Configuring Formatting 

# Configuring Formatting

A number of individual elements include a **Format** attribute, which formats the data being used. A commonly-used example is the **Label** element. Format attribute values can be entered directly or selected from a drop-down list of formats, which include *Long Date*, *Short Date*, *Short Time*, *Currency*, and *Metric Prefix* (mp).

![](https://devnet.logianalytics.com/hc/article_attachments/4417563220759/intlocal_03a.png)

These and other formats are directly affected by the formats set in the Operating System and attributes in the Globalization element. For example, if the browser language or Globalization element's User Culture attribute is set to English/United Kingdom [en-GB]then setting a Format attribute to *Currency* will result in numeric values being shown with the Pound symbol ![](https://devnet.logianalytics.com/hc/article_attachments/4417563220887/intlocal_03b.png).
For more information about individual formatting options, see [Format Data](https://devnet.logianalytics.com/hc/en-us/articles/4406817477911-Format-Data).
