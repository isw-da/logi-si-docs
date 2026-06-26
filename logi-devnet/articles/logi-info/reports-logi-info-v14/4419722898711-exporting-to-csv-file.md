---
title: "Exporting to CSV File"
id: 4419722898711
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722898711-Exporting-to-CSV-File
updated_at: 2022-07-17T02:24:26Z
---

# Exporting to CSV File

# Exporting to CSV File

The **Comma-Separated Values** (CSV) format is a well-established data file format and a widely-accepted method of transferring data.

The following topics discuss how to export Logi report data to CSV files:

* [Exporting Data Manually](https://devnet.logianalytics.com/hc/en-us/articles/4419707568663-CSV-Exporting-Data-Manually#Manually)
* [Exporting Data with Automation](https://devnet.logianalytics.com/hc/en-us/articles/4419707567639-CSV-Exporting-Data-with-Automation#Automatically)
* [Adjusting the Encoding](https://devnet.logianalytics.com/hc/en-us/articles/4419707566743-CSV-Adjusting-the-Encoding#Encoding)

## About Exporting Data to CSV

The CSV data format is useful because of its relative simplicity and universal cross-platform accessibility. CSV files are simple text files that are generally used to represent tabular data: each row of text in the file represents one data record and, in the typical format, each column of data is enclosed in double-quotes and delimited by a comma. The first row may represent the column names. Here's an example:

![](https://devnet.logianalytics.com/hc/article_attachments/7522828919191/exportcsv_01.png)

Logi Info provides **Export CSV** elements that make it easy to export report data into CSV
files.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) The data exported to CSV files is *only* the data in the report's datalayers. Summary Rows, for example, are *not* included in the export.
Logi developers can give users the ability to export a data *manually* via user interaction at runtime or developers can *automate* data exports based on an event or a schedule. Manual exports are configured within Report definitions and automated exports are configured within Process definitions.

For large data sets, we recommend using the rapid CSV export option. Below is a formal list of the differences between native CSV and rapid CSV exports:

| Native CSV Export | Rapid CSV Export |
| --- | --- |
| Can export Crosstab Tables | Cannot export Crosstab Tables |
| Can use Field Delimiter, Row Delimiter, and String Column attributes | Cannot use Field Delimiter, Row Delimiter, and String Column attributes |
| Can have a null value for the "Export Data Table ID" | Cannot have a null value for the "Export Data Table ID" parameter |
| Can export a Data Table created with the "Auto Columns" element | Cannot export a Data Table created with the "Auto Columns" element |
| Can use group or count info (like "Header Row" or "Summary Row" elements) | Cannot use group or count info (like "Header Row" or "Summary Row" elements) |
| Can support Data type attribute in “Excel Column Format” element | Can support Data type attribute in “Excel Column Format” element |
| Cannot use format setting "Excel column format" | Can use format setting "Excel column format" |
| Cannot export report title and filter information | New for 14.2 Can export report title and filter information |
| Can export Group or Summary information | New for 14.2 Can export group or summary information |

For more information on the rapid export feature, see [Rapid CSV Export](https://devnet.logianalytics.com/hc/en-us/articles/4419723125655-Rapid-CSV-Export).
