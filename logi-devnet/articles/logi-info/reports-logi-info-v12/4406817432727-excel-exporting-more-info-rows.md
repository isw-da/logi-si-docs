---
title: "Excel - Exporting More Info Rows"
id: 4406817432727
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817432727-Excel-Exporting-More-Info-Rows
updated_at: 2022-04-06T06:06:04Z
---

# Excel - Exporting More Info Rows

# Excel - Exporting More Info Rows

If your report contains a data table and you're using the **More Info Row** element to show/hide additional detail data within the table, you may want the detail rows (when visible) to be exported along with the main table data.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575708823/exportexcel_13.png)![](https://devnet.logianalytics.com/hc/article_attachments/4417583947671/exportexcel_13a.png)

To enable this, as shown above, set your Target.Native Excel element's **Keep Show Elements** attribute to *True*, and leave the **Export Data Table ID** setting **blank**. If you place a value here, you risk not displaying all of the rows in the spreadsheet.

Keep Show Elements works with Action.Show Elements (used to show/hide the More Info Row) so that items that have been shown or hidden by the user remain that way when the report is re-displayed or exported.
