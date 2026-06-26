---
title: "Excel - Exporting Multiple Tables"
id: 4419715292951
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715292951-Excel-Exporting-Multiple-Tables
updated_at: 2022-07-17T01:49:43Z
---

# Excel - Exporting Multiple Tables

# Excel - Exporting Multiple Tables

If a report contains multiple tables, they can be exported into the *same* or *different* worksheets in a single Excel file.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706820503/exportexcel_06.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419699718935/exportexcel_06a.png)

By default, all tables in a report definition will be exported into the same Excel worksheet during an export operation. However, you can instead include tables selectively by entering them as a comma-separated list in the **Export Data Table ID** attribute of the Target.Native Excel element. For example, the configuration shown above will only export two of the report's three tables to Excel.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714754583/exportexcel_07.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419706820759/exportexcel_07a.png)

By adding **Excel Sheet Break** elements in the Body of your report definition, as shown above, you can cause multiple tables to be sent to separate worksheets. The order of the tables in the report definition dictates the order of the worksheets containing them in the export.
