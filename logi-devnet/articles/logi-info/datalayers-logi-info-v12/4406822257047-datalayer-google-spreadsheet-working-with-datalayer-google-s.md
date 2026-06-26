---
title: "DataLayer.Google Spreadsheet - Working with DataLayer.Google Spreadsheet"
id: 4406822257047
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822257047-DataLayer-Google-Spreadsheet-Working-with-DataLayer-Google-Spreadsheet
updated_at: 2022-04-06T06:05:16Z
---

# DataLayer.Google Spreadsheet - Working with DataLayer.Google Spreadsheet

# DataLayer.Google Spreadsheet - Working with DataLayer.Google Spreadsheet

The datalayer uses a special connection element, **Connection.GoogleDocs**, to establish the connection with the Google web service.
In order to work with this datalayer, worksheets must be formatted to have non-numeric column headers in the first row. These headers (after spaces and punctuation, except hyphens and periods, are removed and the name is converted to lower-case) become the column names of the data retrieved into the datalayer.
Worksheet data is retrieved from the web service and cached as *rows* and *columns*, one data row per worksheet row. Row 1, as discussed in the previous paragraph, is not read as data. Data retrieved into the datalayer is cached in XML format.
The data retrieved with a datalayer is available using @Data tokens, in the format @Data.*ColumnName*~. The spelling of the column name is *case-sensitive*. The data is only available within the scope of the parent element of the datalayer, not throughout the entire report definition. The DataLayer.Linked element can be used to make the data reusable in another datalayer outside this scope.
Logi Info developers can make use of the **AutoColumns** element to quickly see which "column names" are being returned by the web service. We do not recommend the use of AutoColumns for production deployments.
Developers can also view the data retrieved into the datalayer by turning on the **Debugging Link** in their \_Settings definition (General element) and using the resulting link at the bottom of the report page to view the Debugger Trace page. A link on the Trace page will display the retrieved data.
