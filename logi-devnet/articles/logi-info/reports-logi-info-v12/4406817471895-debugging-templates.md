---
title: "Debugging Templates"
id: 4406817471895
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817471895-Debugging-Templates
updated_at: 2022-04-06T06:06:18Z
---

# Debugging Templates

# Debugging Templates

Special debugging features make it easier for you to determine what
happens when a template is filled. These debugging features are enabled if
you have the report's debugging style set to *Debugger Links*, either
from Studio's toolbar or by manually configuring in it the \_Settings
definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583936535/introformbased_06_367x292.png)

For **Excel** templates, a debugging link, as shown above, will be
displayed in the template. Clicking this link will display a typical
Debugger Trace page, with details of the template operation.

For **Word** and **PDF** templates, no such link will be displayed.
However, a file with the debug information will be saved, and you can
browse it directly. The filename will be:

yourLogiAppfolder/rdDownload/GUID + *templateName*-rdDebug.htm
