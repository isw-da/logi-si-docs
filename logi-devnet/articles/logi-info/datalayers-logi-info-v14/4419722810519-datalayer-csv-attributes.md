---
title: "DataLayer.CSV - Attributes"
id: 4419722810519
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722810519-DataLayer-CSV-Attributes
updated_at: 2022-07-17T01:54:00Z
---

# DataLayer.CSV - Attributes

# DataLayer.CSV - Attributes

A **DataLayer.CSV** element is added as a child element to a Data Table or other data container element. Its attributes are set so that it accesses the desired .CSV data file, and so it handles column names as desired.
The datalayer reads and caches the data from the .CSV file. You can add child elements beneath the datalayer to affect its contents, including:

### 

The DataLayer.CSV element has the following attributes:

| Attribute | Description |
| --- | --- |
| CSV File | (Required) Specifies the fully-qualified file system **path** and **filename** for the data file. The token @Function.AppPhysicalPath~ can be used to get the application folder path.  Example: @Function.AppPhysicalPath~\SampleData\Contacts.csv  May also be a complete URL to a file on another web server. Example: http://www.example.com/data/records.csv |
| Column Names | If left blank and if the **Column Names In First Row** attribute is set *False* or is blank, columns retrieved into the datalayer will be assigned default names in the form: Column1, Column2, Column3, etc. If, however, an optional comma-separated list of **custom** datalayer **column names** is specified here, they will override the default names. Or, if the **Column Names In First Row** attribute is set *True*, valid text names from the **first data row** will automatically be assigned as the datalayer column names, overriding the default names. |
| Column Names In First Row | Specifies if the text in the **first data row** should be used as the column names in the datalayer. The default value is *False*. |
| Connection ID | Specifies a connection to a data source that's defined in the \_Settings definition. |
| CSV Delimiter | Specifies the **character** used to **delimit** the columns of data in the .CSV file. You may use *\t* = Tab, *\v* = Vertical Tab, *\r* = Carriage Return, *\n* = Line Feed, or *Space* = blank space. The default character is a *comma*. |
| Date Columns | Specifies a comma-separated list of column names of those columns that should be formatted as **DateTime** data. The names entered here should match those specified using earlier attributes for the **datalayer** column names, e.g. these may be the default names: Column1, Column5, etc. or the custom names specified in the Column Names attribute, or the names read from the first row of data. |
| ID | Specifies an unique element ID. Recommended for easier identification when debugging. |
| Maximum Rows | Specifies the maximum number of rows to retrieve from the data source. |
| Text Qualifier | Specifies the **character** used to **qualify** data that is to be handled as text. The default character is the double-quote. When data is read into the datalayer, the text qualified character is removed from the beginning and end of a column (and should therefore always occur in pairs). If the qualifier character is *doubled* within the column, it will be replaced with a single instance of the character.  For example, the text 'Dave''s Rail Car' in the file becomes Dave's Rail Car in the datalayer. |
