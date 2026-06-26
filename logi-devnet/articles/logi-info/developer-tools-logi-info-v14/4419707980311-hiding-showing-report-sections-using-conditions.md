---
title: "Hiding/Showing Report Sections using Conditions"
id: 4419707980311
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707980311-Hiding-Showing-Report-Sections-using-Conditions
updated_at: 2022-07-17T02:22:51Z
---

# Hiding/Showing Report Sections using Conditions

# Hiding/Showing Report Sections using Conditions

The Division element also has a **Condition** attribute, which can also be used to set its visibility (and the visibility of its child elements). As discussed earlier, circumstances may dictate that only certain parts of a report be visible to a user.

![](https://devnet.logianalytics.com/hc/article_attachments/7522742683287/workdiv_02.png)

This can be achieved by placing elements beneath a Division element, then setting the Division element's **Condition** attribute accordingly, as shown above. If the Condition attribute value evaluates to *True*, then the Division and its child elements will be made visible; otherwise they'll be hidden. For more information, see [Conditions](https://devnet.logianalytics.com/hc/en-us/articles/5163559394711-Conditions).
