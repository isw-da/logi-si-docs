---
title: "Excel - Hiding Elements When Exporting"
id: 4419707573399
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707573399-Excel-Hiding-Elements-When-Exporting
updated_at: 2022-07-17T01:49:37Z
---

# Excel - Hiding Elements When Exporting

# Excel - Hiding Elements When Exporting

When exporting complete reports to Excel, developers commonly want to hide some of the elements in the report page, like the Export button or link. This can be done very easily using **Show Modes**.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706821399/exportexcel_08.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419699720855/exportexcel_08a.png)

Consider the example shown above. The definition, on the left, includes an image that can be clicked to export the report to Excel. However, when it's exported, shown on the right, the Excel Export icon appears in the worksheet itself. We don't want that icon to appear in the worksheet.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699721111/exportexcel_09.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419714755607/exportexcel_09a.png)

To "hide" the icon image in the export, simply place it beneath a Division element. This element supports Show Modes, which the Image element does not.

Then set the Division element's Show Modes attribute value to the built-in Show Mode value *rdBrowser*, as shown above. Elements with this Show Mode value will only be visible in the browser.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706821911/exportexcel_11.png)

When the report is run and exported, as shown above, the document no longer includes the Export Excel icon.
