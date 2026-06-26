---
title: "DataLayer.Google Spreadsheet"
id: 1500009530141
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530141-DataLayer-Google-Spreadsheet
updated_at: 2021-06-17T01:58:10Z
---

# DataLayer.Google Spreadsheet

# DataLayer.Google Spreadsheet

**Google Docs** is a free, web-based word processor, spreadsheet, and presentation application offered as a **web service** by
**Google**. The **DataLayer.Google Spreadsheet** element allows developers to connect to Google Docs and retrieve data from spreadsheets stored there; the data can then be used in Logi applications. This topic discusses the datalayer.

* Attributes
* [Work with DataLayer.Google Spreadshee](#WorkingWith)t
* [A Simple Example](#Example)

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)Google introduced a new security scheme, using OAuth2, in late May 2015. This caused many applications, including Logi applications, to fail and supporting it requires considerable effort. Two weeks later Google relented and allowed users to have a choice of security schemes, new or old, controlled by Google account configurations. Please see [Introduction to Datasource Connections](https://devnet.logianalytics.com/hc/en-us/articles/1500009515402-Introduction-to-Datasource-Connections), Vendor-Specific Connections section, for important information regarding this.

## Attributes

The **DataLayer.Google Spreadsheet** element has the following attributes:

| Attribute | Descriptions |
| --- | --- |
| ConnectionID | (Required) The **ID** of a **Connection.GoogleDocs** element, in the \_settings definition. Valid Google Account credentials must be provided in the connection element. |
| Google SpreadsheetName | (Required) The case-insensitive name of the desired **spreadsheet** document stored on Google Docs.  If the value "List spreadsheets" is entered here, a list of the spreadsheet documents associated with the Google Account will be returned. The names of the columns returned to the datalayer will be *Name*, *Author*, and *Updated* (a timestamp). |
| GoogleWorksheetName | The case-insensitive name of the desired **worksheet** within the spreadsheet document stored on Google Docs.  If the name of the spreadsheet specified earlier is valid, and the value "List worksheets" is entered here, a list of the worksheets associated with the spreadsheet will be returned. The names of the columns returned to the datalayer will be *Name*, *Updated* (a timestamp), and *Rows* (the row count). |
| ID | (Required through v10.1.46) A unique element ID. |
| GoogleDateColumns | A comma-delimited list of the worksheet columns, if any, that should be formatted as **dates**. |
| GoogleNumericColumns | A comma-delimited list of the worksheet columns, if any, that should be formatted as **numbers**. |
| Google SpreadsheetCulture | The culture value for the spreadsheet document, provided here to assist in interpreting international data formats. Default: *invariant (en US)* |

## Work with DataLayer.Google Spreadsheet

The datalayer uses a special connection element, **Connection.GoogleDocs**, to establish the connection with the Google web service. This connection requires valid **credentials** that the user or developer must supply; accounts are available at no charge and can be created at [Google Docs](http://docs.google.com/).

In order to work with this datalayer, worksheets must be **formatted** to have **non-numeric column headers** in the first row. These headers (after spaces and punctuation, except hyphens and periods, are removed and the name is converted to lower-case) become the **column names** of the data retrieved into the datalayer.

Worksheet data is retrieved from the web service and cached as **rows** and **columns**, one data row per worksheet row. Row 1, as discussed in the previous paragraph, is not read as data. Data retrieved into the datalayer is cached in **XML** format.

The data retrieved with a datalayer is available using @Data **tokens**, in the format @Data.*ColumnName*~. The spelling of the column name is **case-sensitive**. The data is only available within the **scope** of the **parent** element of the datalayer, not throughout the entire report definition. The DataLayer.Linked element can be used to make the data reusable in another datalayer outside this scope.

Logi Info developers can make use of the **AutoColumns** element to quickly see which "column names" are being returned by the web service.

Developers can also view the data retrieved into the datalayer by turning on the **Debugging Link** in their \_Settings definition (General element) and using the resulting link at the bottom of the report page to view the **Application Trace** page. A link on the Trace page will display the retrieved data.

## A Simple Example

The following example demonstrates how the **DataLayer.Google Spreadsheet** element can be used.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771866903/datalayergspread_01.gif)

The screenshot above shows the first ten rows of the "Mountains" worksheet in the "Geography" spreadsheet, stored on Google Docs in a Logi Analytics demo account.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778702871/datalayergspread_02.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771867159/datalayergspread_02a.gif)

The example definition shown above includes a **Data Table** and a **DataLayer.Google Spreadsheet** element. The datalayer's attributes are set as shown.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771867415/datalayergspread_03.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778703127/datalayergspread_03a.gif)

As shown above, **Label** elements within each **Data Table Column** use tokens to display the data retrieved into the datalayer. Note the correspondence between the worksheet **column header text** and the **column name** used with the @Data token in the definition (and that the text has been made all lower-case).

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771867671/datalayergspread_04.gif)

The screenshot of the resulting **Logi application table**, above, shows the data from the worksheet being used in the sample application.
