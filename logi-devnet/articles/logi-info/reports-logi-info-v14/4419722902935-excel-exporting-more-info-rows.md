---
title: "Excel - Exporting More Info Rows"
id: 4419722902935
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722902935-Excel-Exporting-More-Info-Rows
updated_at: 2022-07-17T02:24:26Z
---

# Excel - Exporting More Info Rows

# Excel - Exporting More Info Rows

If your report contains a Data Table and you're using the **More Info Row** element to show/hide additional detail data within the table, you may want the detail rows (when visible) to be exported along with the main table data.

![](https://devnet.logianalytics.com/hc/article_attachments/7522825066647/exportexcel_13.png)![](https://devnet.logianalytics.com/hc/article_attachments/7522810820375/exportexcel_13a.png)

To enable this, as shown above, set your Target.Native Excel element's **Keep Show Elements** attribute to *True*, and leave the **Export Data Table ID** setting **blank**. If you place a value here, you risk not displaying all of the rows in the spreadsheet.

Keep Show Elements works with Action.Show Elements (used to show/hide the More Info Row) so that items that have been shown or hidden by the user remain that way when the report is re-displayed or exported.
