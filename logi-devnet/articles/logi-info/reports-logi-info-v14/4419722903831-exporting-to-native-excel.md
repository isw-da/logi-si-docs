---
title: "Exporting To Native Excel"
id: 4419722903831
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722903831-Exporting-To-Native-Excel
updated_at: 2022-07-17T02:07:50Z
---

# Exporting To Native Excel

# Exporting To Native Excel

Exporting reports into Microsoft Excel worksheets is a popular and useful method of applying additional analysis to data.

The following topics discuss techniques for exporting reports to Excel:

* [Exporting a Report Manually](https://devnet.logianalytics.com/hc/en-us/articles/4419707572375-Excel-Exporting-a-Report-Manually#Manually)
* [Exporting a Report using a Process Task](https://devnet.logianalytics.com/hc/en-us/articles/4419722904855-Excel-Exporting-a-Report-using-a-Process-Task#Task)
* [Specifying Excel Column Formatting](https://devnet.logianalytics.com/hc/en-us/articles/4419707574295-Excel-Specifying-Excel-Column-Formatting#Formatting)
* [Exporting Multiple Tables](https://devnet.logianalytics.com/hc/en-us/articles/4419715292951-Excel-Exporting-Multiple-Tables#Multiple)
* [Hiding Elements When Exporting](https://devnet.logianalytics.com/hc/en-us/articles/4419707573399-Excel-Hiding-Elements-When-Exporting#Hiding)
* [Exporting More Info Rows](https://devnet.logianalytics.com/hc/en-us/articles/4419722902935-Excel-Exporting-More-Info-Rows#MoreInfo)
* [Cascading Style Sheet Support](https://devnet.logianalytics.com/hc/en-us/articles/4419722899863-Excel-Cascading-Style-Sheet-Support#CSS)
* [Debugging Exports](https://devnet.logianalytics.com/hc/en-us/articles/4419722901783-Excel-Debugging-Exports#Debugging)
* [Export Considerations](https://devnet.logianalytics.com/hc/en-us/articles/4419707571095-Excel-Export-Considerations#Considerations)

## About Exporting Reports to Excel

Exporting tabular data into a worksheet allows further computations and analysis to be performed. Microsoft's widely-used Excel spreadsheet program is ideal for this practice and Logi Studio provides appropriate elements for exporting data and reports.

Export features include the ability to export multiple Data Tables in the same operation (to the same or to separate worksheets), to apply style sheets to the exported data, to export report headers**,** images and charts or just raw table data, to maintain proper time and date formats, and to maintain Data Table internal cell linefeeds. ![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 The report title, grouping, summary, and filter information display on the export results, if your application has been configured for it.

Data Table cell background and text colors generated using [The Color Range Column](https://devnet.logianalytics.com/hc/en-us/articles/4419722746263-The-Color-Range-Column) are exported to Excel worksheets.

**Group Header Row** and **Group Summary Row** elements now have a Show Modes attribute, which lets you hide them when exporting a report to Excel. For more information, see [Show Modes](https://devnet.logianalytics.com/hc/en-us/articles/4419707995543-Show-Modes). In addition, if using these two elements with their **Append Blank Rows** or **Prepend Blank Rows** attributes set to a number, blank rows will now *not* be
appended/prepended when the report is exported to Excel.

In a Data Table report, when Append Blank Rows to the Group Summary Row is set, the width of the newly added blank rows will be the same as the largest width in the existing Table Row.

Developers interested in inserting data into pre-defined worksheet forms should see [Create an Excel Template](https://devnet.logianalytics.com/hc/en-us/articles/4419707432727-Create-an-Excel-Template).

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Excel imposes column and row limits per worksheet (the exact numbers vary based on the version of Excel). Exported data that exceeds these limits will overflow onto the next worksheet.

You can specify that the exported output be in Excel 2007 (.xlsx) format or Excel 2003 and earlier (.xls) format.

### Use "Export Native Excel"

Use the **Action.Export Native Excel** element, **Procedure.Export Native Excel** element, or **Rapid Excel Export** element for all of your Excel exports. Earlier versions of Logi Info included a now-deprecated Action.Export Word Or Excel element that has only been retained for backward compatibility.

For large data sets, we recommend using the rapid Excel export option. Below is a formal list of the differences between native Excel and rapid Excel exports:

| Native Excel Export | Rapid Excel Export |
| --- | --- |
| Can export a report of one or more specified Tables/Crosstabs to a file | Can only export one specified Data Table to a file |
| Can support Data type attribute in “Excel Column Format” element | Can support Data type attribute in “Excel Column Format” element |
| Can export a Crosstab | Cannot export a Crosstab |
| Can export a Data Table created with the "Auto Columns" element | Cannot export a Data Table with the "Auto Columns" element |
| Can use the "Excel Paper Size" attribute | Cannot use the "Excel Paper Size" attribute |
| Can use the "Show Gridlines" attribute | Cannot use the "Show Gridlines" attribute |
| Can use the "Caption" attribute | Cannot use the "Caption" attribute |
| Can use group or count info (like "Header Row" or "Summary Row" elements) | Cannot use group or count info (like "Header Row" or "Summary Row" elements) |
| Can support Style info (like background color or text color) | Cannot support Style info (like background color or text color) |
| Can support the "More Info Row" element | Cannot support the "More Info Row" element |
| New for 14.2 Can export report title and filter information | New for 14.2 Can export report title and filter information |
| New for 14.2 Can remove empty rows if there is no detail data under a particular group | Cannot remove empty rows if there is no detail data under a particular group |
| Can support token resolution | New for 14.2 Can support token resolution |
| Can export group or summary information | New for 14.2 Can export group or summary information |

For more information on the rapid export feature, see [Rapid Excel Export](https://devnet.logianalytics.com/hc/en-us/articles/4419715446423-Rapid-Excel-Export).

### Manual vs Process Task Export

You can give your users the ability to export a report in two ways:

* Manual - An exported report is made available for download and opened using an Excel browser plug-in or Excel itself, or
* Process Task - An exported report is saved, as an .xlsx or .xls file, to the web server, as part of process task execution. This also allows you to distribute exported Excel files as email attachments.

Manual exports are configured within *report definitions* and process exports are configured within *process definitions*.
