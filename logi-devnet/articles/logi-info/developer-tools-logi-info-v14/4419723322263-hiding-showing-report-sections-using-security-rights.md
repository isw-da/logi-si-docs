---
title: "Hiding/Showing Report Sections Using Security Rights"
id: 4419723322263
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723322263-Hiding-Showing-Report-Sections-Using-Security-Rights
updated_at: 2022-07-17T02:22:51Z
---

# Hiding/Showing Report Sections Using Security Rights

# Hiding/Showing Report Sections Using Security Rights

The Division element also has a **Security Right ID** attribute, which can also be used to set its visibility (and the visibility of its child elements). As mentioned earlier, circumstances may dictate that only certain parts of a report be visible to certain users.

![](https://devnet.logianalytics.com/hc/article_attachments/7522700072215/workdiv_04.png)

This can be achieved by placing elements beneath a Division element, then setting the Division element's **Security Right ID** attribute accordingly, as shown above. If Logi Security is enabled and a user's **security role** has the security right identified in this attribute, then the Division and its child elements will be made visible; otherwise they'll be hidden. For more information, see [Logi Security](https://devnet.logianalytics.com/hc/en-us/articles/4419715379607-Logi-Security).
