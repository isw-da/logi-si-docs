---
title: "DataLayer.Excel"
id: 4419707243287
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707243287-DataLayer-Excel
updated_at: 2022-07-17T02:03:50Z
---

# DataLayer.Excel

# DataLayer.Excel

Developers often need to read data from Microsoft Excel spreadsheets and Logi Info includes a datalayer element just for this purpose, **DataLayer.Excel**. This topic discusses this datalayer.

* Attributes
* [Working with DataLayer.Excel](#Working)

## Attributes

The **DataLayer.Excel** element has the following attributes:

| Attribute | Description |
| --- | --- |
| Excel File | (Required) Specifies the fully-qualified file system **path** and **filename** for the spreadsheet file. The token @Function.AppPhysicalPath~ can be used to get the application folder path. Both .xls and .xlsx formats are supported. Example: @Function.AppPhysicalPath~\SampleData\Contacts.xls A fully-qualified URL to an Excel file on the Internet can also be specified. Example: http://www.example.com/data/records.xls |
| Cell Range | Specifies a **range of cells** from the worksheet to be read. Multiple ranges, separated by commas, can be specified and will be joined together to include all matching columns and rows. Examples: A1:H10 will include rows 1 through 10 of columns A through H. C:F,H will include all data rows from columns C, D, E, F, and H. C5:E10,H will include rows 5 through 10 of columns C, D, E, and H. 10:30 will include rows 10 through 30 of all data columns. |
| Column Names | If left blank and if the **Column Names Row** attribute has no value, columns retrieved into the datalayer will be assigned default names in the form: Column1, Column2, Column3, etc. If, however, an optional comma-separated list of **custom** datalayer **column names** is specified here, they will override the default names. Or, if the **Column Names Row** attribute specifies a row number, valid text names from the **specified data row** will automatically be assigned as the datalayer column names, overriding the default names. |
| Column Names Row | Specifies the **row number** which contains names for the datalayer columns. This row will not be included in the data, but will be used as column names when the data is valid (names should start with a letter and include only letters or numbers). |
| Connection ID | Specifies a connection to a data source that's defined in the \_Settings definition. |
| Date Columns | Specifies a comma-separated list of column names of those columns that should be formatted as **DateTime** data. The names entered here should match those specified using earlier attributes for the **datalayer****column****names**, e.g. these may be the default names: Column1, Column5, etc. or the custom names specified in the Column Names attribute, or the names read from the row specified in the Column Names Row attribute. |
| ID | Specifies an unique element ID. Recommended for easier identification when debugging. |
| Worksheet | Specifies the worksheet in the Excel file from which to read data. The default value is the *first worksheet*. |

  

## Working with DataLayer.Excel

In most respects, **DataLayer.Excel** functions exactly as other datalayer elements do and its data can be filtered and conditioned using appropriate elements. One major difference, however, is that *there is no need to use a Connection element in the \_Settings definition with this element.* The DataLayer.Excel element directly accesses the file system to read .XLS and .XLSX files.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714620183/dlexcel_01.png)

As shown above, a **DataLayer.Excel** element is added as a child element to a Data Table. Its attributes are set so that it accesses the desired Excel file, reads the right worksheet and columns, and also handles column names as desired.
The datalayer reads and caches the data from the Excel file. You can add child elements beneath the datalayer to affect its contents, including:

* **Filtering**: Sort, group, or restrict the data
* **Extending**: Add virtual columns to the datalayer that contain
  aggregated, calculated, or totaled data values
* **Securing**: Limit access to the data using Logi security
* **Linking**: Make the results reusable elsewhere in your report
  definitions

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) If you have the target spreadsheet open in Excel, the datalayer may not be able to read it.

Data retrieved into the datalayer is cached in XML format, in memory and/or on the web server's file system. The latter is discussed in [The Logi Server Engine](https://devnet.logianalytics.com/hc/en-us/articles/4419715421975-The-Logi-Server-Engine) and may be of interest to developers working with extremely large datasets or large numbers of concurrent users.

The data read with the datalayer is available using @Data tokens,
in the format @Data.*ColumnName*~. The spelling of the column name is
**case-sensitive**. The data is only available within the **scope** of the
parent element of the datalayer, not throughout the entire report
definition. The **DataLayer.Linked** element can be used to make the data reusable
in another datalayer outside this scope.

The [Auto Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419700048023-Auto-Columns) element can be used to quickly display in your report all the data in a datalayer.

The data retrieved into the datalayer can be viewed by turning on the
**Debugging Link** in your \_Settings definition (**General** element) and using
the resulting link at the bottom of your report page to view the **Debugger
Trace** page. A link on the Trace page will display the retrieved data.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706605847/dlexcel_02.png)

Studio includes a **wizard** that will add an Excel datalayer to your definition, letting you select columns and then configuring and inserting the element for you. You can launch the wizard using the right-click context menus shown above.
