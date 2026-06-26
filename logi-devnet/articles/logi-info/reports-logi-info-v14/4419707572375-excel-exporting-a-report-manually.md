---
title: "Excel - Exporting a Report Manually"
id: 4419707572375
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707572375-Excel-Exporting-a-Report-Manually
updated_at: 2022-07-17T02:24:26Z
---

# Excel - Exporting a Report Manually

# Excel - Exporting a Report Manually

Here's an example of how to create a report, with a link,
that exports itself manually:

![](https://devnet.logianalytics.com/hc/article_attachments/7522825060119/image-20220601-192544_1352x513.png)

1. In your report definition, add an **Action.Export Native Excel** element beneath a Label, Image, Button, or Chart element, as shown above.
2. Add the required **Target.Native Excel** element.
3. If the report to export *is* the current report, you need do nothing more. Just save your definition and browse your report. It's that simple.
4. If the report to export *is not* the current report, specify that report by setting the Target.Native Excel element's **Report Definition File** attribute.
5. All Target.Native Excel element attributes are *optional*. The default settings will export the current report in its entirety.

What Happens: The report is exported to a temporary file created in your application's rdDownload folder on the web server. The temp file is then returned to the client and opened automatically in the Excel plug-in within your browser (you maybe prompted to Open or Save the Excel file) or in Excel itself. Temporary files on the server are cleaned up automatically over time.

The following table describes the attributes of the **Target.Native Excel** element, all of which are optional:

| Attribute | Description |
| --- | --- |
| Excel Output Format | Specifies the desired output format of the Excel file created. Set to *Excel2007* to produce an .xlsx file, which supports up to 16K columns and 1M rows per worksheet. Set to *Excel2003* to create an .xls file, with 255 columns and 64K rows per worksheet.  .xlsx files can be opened with Office 2003, but they will lose any data beyond the 255 columns and 64K rows that are supported.  Default: *Excel2003 (.xls)* |
| Excel Paper Size | Specifies the default paper size of the Excel workbook, used when it's being printed. Options include *A4*, *Letter*, *Legal*, etc. |
| Export Data Preference | Specifies the export preference. Options include Empty (default), Rapid, and Formatted. For more information, see [Rapid Excel Export](https://devnet.logianalytics.com/hc/en-us/articles/4419715446423-Rapid-Excel-Export). |
| Export Data Table ID | Specifies the ID of a particular Data Table to be exported, and causes a *Data Table only* export. Only the Data Table caption, columns (with header text), and data rows will be output. No report headers, images, report footers, etc. will be output. If this attribute is left blank, the full report with all report headers, report footers, Data Tables, images, etc. will be output.  To export the data for an Analysis Grid element, set this value to *dtAnalysisGrid*. This is the ID of the Analysis Grid's internal Data Table. |
| Export File Name | Specifies a custom name for the export files. When left blank, file names consist of a random GUID number and extension. |
| Frame ID | Specifies the frame for the target HTML page. Leave blank for the current browser window, or enter NewWindow to open a new browser window. You can also specify an existing frame ID to re-use the same window for each request. |
| Keep Show Elements | Specifies whether page items that have been shown or hidden by the user, using Action.Show Element, remain that way when the report is exported. Set to *True* so that those elements that were originally hidden but then shown by the user get included in the export. Alternatively, any elements hidden by the user will not be exported. Default: *False.* |
| New for 14.2 Remove Empty Group Rows | Specifies whether the Excel output displays empty rows when there is no detail data under a particular group. Default: Empty, or *False*.  This attribute only supports Native Excel and Formatted exports. |
| Report Definition File | Specifies the name of a the report definition file to be exported. Default: *the current report.* |
| Report Show Modes | Specifies the Show Modes strings to be passed to the report when it's rendered for export; makes it possible to hide elements in reports. See [Excel - Hiding Elements When Exporting](https://devnet.logianalytics.com/hc/en-us/articles/4419707573399-Excel-Hiding-Elements-When-Exporting). |
| Request Forwarding | Specifies whether to pass all request parameters to the report when it's rendered for export. Default: *False.* |
| Show Gridlines | Specifies grid line behavior in the exported report. In Excel, if two consecutive rows or columns are set to the same style (font, background, foreground color, etc.) the gridlines between them will disappear and this may not provide the desired appearance. Set this attribute to *True* to show the gridlines in all cases. Default: *False.* |
