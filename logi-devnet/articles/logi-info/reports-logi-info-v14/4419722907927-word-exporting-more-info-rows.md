---
title: "Word - Exporting More Info Rows"
id: 4419722907927
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722907927-Word-Exporting-More-Info-Rows
updated_at: 2022-07-17T01:49:30Z
---

# Word - Exporting More Info Rows

# Word - Exporting More Info Rows

If your report contains a Data Table and you're using the **More Info Row** element to show/hide additional detail data within the table, you may want the detail rows (when visible) to be exported along with the main table data.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699722135/exportword_09.png)

To enable this, as shown above, set your Target.Native Word element's **Keep Show Elements** attribute to *True*.
Keep Show Elements works with Action.Show Elements (used to show/hide the More Info Row) so that items that have been
shown or hidden by the user remain that way when the report is re-displayed or
