---
title: "Hiding/Showing Report Sections Using Security Rights"
id: 4406818109719
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818109719-Hiding-Showing-Report-Sections-Using-Security-Rights
updated_at: 2022-04-06T06:10:15Z
---

# Hiding/Showing Report Sections Using Security Rights

# Hiding/Showing Report Sections Using Security Rights

The Division element also has a **Security Right ID** attribute, which can also be used to set its visibility (and the visibility of its child elements). As mentioned earlier, circumstances may dictate that only certain parts of a report be visible to certain users.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562954391/workdiv_04.png)

This can be achieved by placing elements beneath a Division element, then setting the Division element's **Security Right ID** attribute accordingly, as shown above. If Logi Security is enabled and a user's **security role** has the security right identified in this attribute, then the Division and its child elements will be made visible; otherwise they'll be hidden. For more information, see [Logi Security](https://devnet.logianalytics.com/hc/en-us/articles/4406822422295-Logi-Security).
