---
title: "CSV - Exporting Data Manually"
id: 4406817428119
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817428119-CSV-Exporting-Data-Manually
updated_at: 2022-04-06T06:06:02Z
---

# CSV - Exporting Data Manually

# CSV - Exporting Data Manually

Here's an example of how to create a report with a link that allows data to be exported manually:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583949079/rapid_csv_1267x653.png)

1. In your report definition, add an **Action.Export CSV** element as the child of a **Label**, **Image**, **Button** or **Chart** element, as shown above. Set its required ID attribute.
2. Below it, add the required **Target.CSV** child element.
3. If the data to be exported is part of the *current report*, you need don't need to do anything else. Just save your definition and browse your report. It's that simple. Notice that the example above shows that no attribute values need be set: the default settings will export the current reports' data.

What happens when the link is clicked? The data in the report's datalayer is exported to a temporary .csv file which is created in your application's rdDownload folder on the web server. The temp file is then opened automatically in your browser, usually in the Microsoft Excel plug-in, if it's installed (the .csv file extension gets associated with it when Excel is installed).
With the exception of data column header text, *only* data is exported; report headers, footers, paging controls, images, summary rows, etc. from the source report are *not* exported. If the source data table has column header labels, these will be exported as the first row of the CSV file.

The following table provides explanations for the Target.CSV element's attributes, which are all optional:

| Identifier | Description |
| --- | --- |
| Export Data Preference | Specifies the export preference. Options include Empty (default), Rapid, and Formatted. For more information on Rapid CSV Export, see |
| Export Data Table ID | Specifies the **Data Table** from which data will be exported. This is useful if a report contains multiple data tables; if there is only one table in the report, this attribute can be left blank. To export the data in an **Analysis Grid** element, set this value to "dtAnalysisGrid", the ID of the Analysis Grid's internal data table. |
| Export Filename | Specifies an explicit file name for the CSV file that receives the exported data. This value should be a file name *only*, without a path, and may or may not include the .csv file extension. If left blank, a random GUID file name will be generated and used. |
| Field Delimiter | Specifies the CSV file **data****delimiter**, typically a comma. Enter the desired character. You may use tokens in this attribute to set the delimiter dynamically. If left blank, the delimiter is determined first by inspecting the browser's language setting, and then by using the web server's List Separator character from its Regional Settings. This allows international users to get the appropriate field separator. If you use a Tab delimiter here, it will also remove the double-quotes around the values - see the following section for an example. |
| Frame ID | Specifies the **frame** for the target page. Leave blank for the current browser window, or select *NewWindow* to open a new browser window. You can also specify an existing frame identifier to re-use the same window for each request. |
| ID | Specifies a unique identifier for this element. |
| Report Definition File | Specifies the name of the report definition file that contains the data to be exported. Default: *the current report* |
| Report Show Modes | Specifies the **Show Modes** to be used when rendering the data for export, making it possible to hide some of the data. When this attribute is blank, all of the elements and, therefore, all of the data is exported. To set Show Modes in the exported report, enter a comma-delimited list of Show Mode values in this attribute; the data from any elements in the report definition that have a Show Mode that matches on in this list will appear in the exported data. |
| Request Forwarding | Specifies whether **request variables** will be passed to the report definition file that contains the data to be exported. Has no effect if the current report is being exported. |
| Row Delimiter | Specifies the CSV file **row delimiter** character(s). Default: *standard CRLF characters* |
| String Columns | Specifies the **columns** of the exported data that should be interpreted as **string values**. The CSV format is frequently used to export data into Microsoft Excel. When Excel encounters a value that looks like a number, it removes any leading zeros. This is a problem for some values that should not be treated as numbers and should not have leading zeros removed. For example, "000123" might be an account number wherein the leading zeros are relevant. The removal of leading zeroes in Excel can be suppressed by supplying the appropriate Data Table Column element IDs, in a comma-separated list, in this attribute. |

The temporary files generated during the export are **cleaned up** automatically over time.

## Delimiting with the Tab Character

A common alternate CSV format uses the **Tab** character as the delimiter, which removes the double-quotes that usually enclose the field data. However, you can't type a Tab character in the **Field Delimiter** attribute so, to use this format, enter its ASCII value as an expression, =CHR(9), in the attribute value instead.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575710359/exportcsv_03.png)

As shown above, when you run the report and export the data, it will be Tab delimited and have no double-quotes.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Using the ASCII code for a Tab delimiter is the *only* way to remove the double-quotes from the standard CSV format output. Entering other characters or ASCII codes in the Field Delimiter attribute will not remove them.
