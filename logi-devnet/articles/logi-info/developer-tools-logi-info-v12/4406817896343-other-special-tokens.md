---
title: "Other Special Tokens"
id: 4406817896343
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817896343-Other-Special-Tokens
updated_at: 2022-04-06T06:08:55Z
---

# Other Special Tokens

# Other Special Tokens

These tokens are used for special purposes:

| Token | Resolves To |
| --- | --- |
| @Chart.rdExtraColumnID~ | References different parts of the data (such as bar segments) when using an **Extra Data Column** element. Useful in determining which bar segment was clicked, for example. *This token is only available for Classic static XY-type charts, not animated or Chart Canvas charts.* |
| @Data.rdSalesforceTable~ | A list of table names returned from a LIST TABLES query to Salesforce.com. |
| @Data.rdSalesforceField~ | A list of field names returned from a LIST *<tablename>* query to Salesforce.com. |
| @Request.rdReport~ | The name of the currently loaded report definition. Example: *Default* |
| @Request.rdReportFormat~ | Sets/gets the exported report format as one of: *PDF*, *NativeExcel*, *NativeWord*, *CSV*, *HtmlExport*, *HtmlEmail*, *Excel*, *Word*, *XML*, or *GoogleSpreadsheet*. Doesn't exist (is null) for reports in browser. |
| @Session.SessionID~ | The current session ID. |
| @Session.rdLastErrorLogFilename~ | The error log file name, in the application's rdErrorLog folder, when error logging is enabled. |
