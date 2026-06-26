---
title: "DataLayer.Google Spreadsheet - DataLayer.Google Spreadsheet Example"
id: 4419707488791
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707488791-DataLayer-Google-Spreadsheet-DataLayer-Google-Spreadsheet-Example
updated_at: 2022-07-17T01:53:32Z
---

# DataLayer.Google Spreadsheet - DataLayer.Google Spreadsheet Example

# DataLayer.Google Spreadsheet - DataLayer.Google Spreadsheet Example

The following example demonstrates how the DataLayer.Google Spreadsheet element can be used.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714718103/dlgoogsheet_01.png)

The screenshot above shows the first few rows of the "Mountains" worksheet in the "World Geography" spreadsheet, stored on Google Docs in a Logi Analytics demo account.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706749719/dlgoogsheet_02.png)

The example definition shown above includes a **Data Table** and a **DataLayer.Google Spreadsheet** element. The datalayer's attributes are set as shown.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699647767/dlgoogsheet_03.png)

As shown above, **Label** elements within each **Data Table Column** use tokens to display the data retrieved into the datalayer. Note the correspondence between the worksheet **column header text** and the **column name** used with the @Data token in the definition (and that the text has been made all lower-case).

![](https://devnet.logianalytics.com/hc/article_attachments/4419699648535/dlgoogsheet_04.png)

The screenshot of the resulting Logi application Data Table, above, shows the data from the worksheet being used in the sample application.
