---
title: "DataLayer.Google Spreadsheet - Attributes"
id: 4406817297943
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817297943-DataLayer-Google-Spreadsheet-Attributes
updated_at: 2022-04-06T06:05:15Z
---

# DataLayer.Google Spreadsheet - Attributes

# DataLayer.Google Spreadsheet - Attributes

The **DataLayer.Google Spreadsheet** element has the following attributes:

| Attribute | Description |
| --- | --- |
| ConnectionID | (Required) Specifies the element ID of a **Connection.GoogleDocs** element, in the \_Settings definition. Valid Google Account credentials must be provided in the connection element. |
| Google SpreadsheetName | (Required) Specifies the case-insensitive name of the desired **spreadsheet** document stored on Google Docs. If the value "List spreadsheets" is entered here, a list of the spreadsheet documents associated with the Google Account will be returned. The names of the columns returned to the datalayer will be *Name*, *Author*, and *Updated* (a timestamp). You may want to temporarily use an AutoColumns element to display the list of spreadsheets. |
| GoogleWorksheetName | (Required) Specifies the case-insensitive name of the desired **worksheet** within the spreadsheet document stored on Google Docs. If the name of the spreadsheet specified earlier is valid, and the value "List worksheets" is entered here, a list of the worksheets associated with the spreadsheet will be returned. The names of the columns returned to the datalayer will be *Name*, *Updated* (a timestamp), and *Rows* (the row count). You may want to temporarily use an AutoColumns element to display the list of workheets. |
| ID | Specifies an optional element ID. Recommended for easier identification when debugging. |
| GoogleDateColumns | Specifies a comma-delimited list of the worksheet columns, if any, that should be formatted as *dates*. |
| GoogleNumericColumns | Specifies a comma-delimited list of the worksheet columns, if any, that should be formatted as *numbers*. |
| Google SpreadsheetCulture | Specifies the culture value for the spreadsheet document, provided here to assist in interpreting international data formats. Default: *invariant (en US)* |
