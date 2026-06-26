---
title: "Conditions Example: Using the Data Table Column Element"
id: 4419707975319
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707975319-Conditions-Example-Using-the-Data-Table-Column-Element
updated_at: 2022-07-17T02:22:52Z
---

# Conditions Example: Using the Data Table Column Element

# Conditions Example: Using the Data Table Column Element

A **Data Table Column** element's Condition attribute allows the column
to be displayed or hidden dynamically, based on criteria you set.

![](https://devnet.logianalytics.com/hc/article_attachments/7522742827031/usingcond_03.png)

The example report definition shown above displays Product information in
a Data Table. However, the display of *sensitive* data, such as the
unit cost, needs to be restricted so that it can only be viewed by
specific users. If the application starts by authenticating the user and
classifying them using a Session variable before calling this report,
sensitive data can be hidden, using a Condition attribute, from everyone
except authorized users. The Unit Cost column will not be displayed at all
unless the Condition evaluates to *True*.
