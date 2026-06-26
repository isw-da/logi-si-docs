---
title: "Hiding/Showing Report Sections Using Show Modes"
id: 4406818110743
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818110743-Hiding-Showing-Report-Sections-Using-Show-Modes
updated_at: 2022-04-06T06:10:14Z
---

# Hiding/Showing Report Sections Using Show Modes

# Hiding/Showing Report Sections Using Show Modes

You can also use **Show Modes** attribute to set Division visibility (and the visibility of its child elements). Under some circumstances, this may be more desirable than using a Condition expression.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575427479/workdiv_01.png)

This can be achieved by placing elements beneath a Division element, then setting the Division element's **Show Modes** attribute accordingly, as shown above.

There are built-in Show Modes values available which can be very useful. For example, using the *rdBrowser* value will cause the division to be seen only when the report is displayed as HTML in a browser; using *rdExportPdf* will cause the division to be visible only when the report is exported as a PDF. For more information, see [Show Modes](https://devnet.logianalytics.com/hc/en-us/articles/4406818147095-Show-Modes).
