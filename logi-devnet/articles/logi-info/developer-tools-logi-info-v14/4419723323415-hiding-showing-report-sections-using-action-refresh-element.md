---
title: "Hiding/Showing Report Sections Using Action.Refresh Element"
id: 4419723323415
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723323415-Hiding-Showing-Report-Sections-Using-Action-Refresh-Element
updated_at: 2022-07-17T01:28:50Z
---

# Hiding/Showing Report Sections Using Action.Refresh Element

# Hiding/Showing Report Sections Using Action.Refresh Element

The **Action.Refresh Element** element, using AJAX technology, allows you to *refresh* a portion of a report page instead of the regenerating the entire report page. It can be used, for example, to refresh Division elements and, when used with a **Link Parameters** element, can pass parameters that can cause divisions to be shown or hidden.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) To get the refresh to work properly, you must place the Division element(s) to be refreshed *beneath* a parent Division element and then make that parent element the target of your Action.Refresh Element element. Do not target the child Division element(s).

![](https://devnet.logianalytics.com/hc/article_attachments/4419700012183/workdiv_03.png)

In the example shown above, two Division elements have their Condition attributes set so they're displayed based on a Request parameter value. They're both children of the "divParent" element. Clicking the link "lblTest" will refresh "divParent" and pass a parameter value. The two child Division elements will be shown or hidden based on that parameter value.

Tokens may be used in theAction.Refresh Element element's **Element ID**attribute value.
