---
title: "PDF - Exporting More Info Rows"
id: 4419707563799
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707563799-PDF-Exporting-More-Info-Rows
updated_at: 2022-07-17T01:50:02Z
---

# PDF - Exporting More Info Rows

# PDF - Exporting More Info Rows

If your report contains a Data Table and you're using the **More Info Row** element to show/hide additional detail data within the table, you may want the detail rows (when visible) to be exported along with the main table data.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699706391/exportpdf_13.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419714749719/exportpdf_13a.png)

To enable this, as shown above, set your Target.PDF element's **Keep Show Elements** attribute to *True*.

Keep Show Elements works with Action.Show Elements (used to show/hide the More Info Row) so that items that have been shown or hidden by the user remain that way when the report is re-displayed or exported.

In addition, you may want to set the **Keep Table Headers with More Info Row** attribute to *True* if you want to ensure that all the tables in the
report have repeatable table headers, even if they have a More Info Row
containing other reports with tables.

It is possible to "nest" More Info Row elements, so that you have one More Info Row element as a child of a table that's a child of another More Info Row. However, be aware that the lowest More Info Row contents may not export correctly, or at all, so we don't recommend this design arrangement if exporting of expanded rows is desired.
