---
title: "Critical Chrome Browser Update"
id: 4415831044375
section: "Announcements"
category: "General"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415831044375-Critical-Chrome-Browser-Update
updated_at: 2022-03-24T23:49:05Z
---

# Critical Chrome Browser Update

Please Bookmark this article, as it will be updated regularly! There is a direct impact to you if you are a Logi Info customer, and the version you are running makes a difference, so please read this carefully. The impact of this change varies if you are a Composer, Report, Izenda or Exago customer.

**Google is planning to re-enable the following feature in the Chrome browser at some point in 2022:**

*Remove alert(), confirm(), and prompt for cross origin iframes*, [Remove alert(), confirm(), and prompt for cross origin iframes - Chrome Platform Status](https://www.chromestatus.com/feature/5148698084376576).

FOR LOGI INFO CUSTOMERS:

This change has the potential to severely impact your Logi Info and Logi SSRM applications, when you have them embedded in an inline frame (iframe) that uses a URL from a domain different from the parent application containing the iframe itself. In this case, once this Chrome browser update is enabled, and your Logi application is not in the same domain as the parent application, the JavaScript alert(), confirm(), and prompt() methods will no longer work. If you are using Info prior to v14.1, the JavaScript in Logi Info engine uses these methods extensively, especially in the the workflow of the Analysis Grid, Bookmark management, Schedule management, and action-element validations and confirmations in general. In SSRM applications, this update effectively disables analysis grid content generation and bookmark management. In a non-SSRM Logi Info application, the severity of the impact depends on if you use the impacted elements in your application.

You can follow the updates for this change that the chromium project team is publishing here: [1065085 - chromium - An open-source project to help move the web forward. - Monorail](https://bugs.chromium.org/p/chromium/issues/detail?id=1065085#c111). As of 12/2021, this is the latest statement from the team: **“We haven't decided on a timeline yet for when to re-enable this behavior; we'll update this bug when we do. Note that the origin trial will be available as an opt-out for at least 6 months beyond when we re-enable it, possibly with other workarounds available as well.”**

They also promise they “will absolutely give at least several months' notice before re-enabling”.

HOW YOU CAN MITIGATE THIS CHANGE

1. **Upgrade** to the latest version of Logi INFO 14.1 or the next SP on 12.8 (SP to be decided) and 14.0 (SP to be decided) (Note: the Logi INFO 14.1 engine can be used with any version of SSRM 12.7 and higher. It is not necessary to upgrade SSRM itself to resolve this issue.)
2. Or, embed your Logi site on the same domain as the parent app with the iframe calling the Logi app.
3. Reach out to [Support](https://devnet.logianalytics.com/hc/en-us/requests/new) for additional help.

FOR LOGI REPORT CUSTOMERS: Watch this space!

FOR IZENDA CUSTOMERS: Watch this space!

FOR EXAGO CUSTOMERS: Watch this space!

FOR LOGI COMPOSER AND COMPOSER PLAYGROUND CUSTOMERS: Watch this space!
