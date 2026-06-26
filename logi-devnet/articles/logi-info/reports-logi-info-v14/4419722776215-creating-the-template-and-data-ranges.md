---
title: "Creating the Template and Data Ranges"
id: 4419722776215
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722776215-Creating-the-Template-and-Data-Ranges
updated_at: 2022-07-17T01:56:01Z
---

# Creating the Template and Data Ranges

# Creating the Template and Data Ranges

Microsoft Excel templates generally consist of both static content, called
the *template**area*, and landing areas for dynamic
content, called the *data* *area* or *data range*. In
order to preserve highly-formatted templates, when it generates output,
the Logi server engine makes no modifications to the template area. The
data range, however, is *filled-in* at runtime with the data
retrieved by one or more data queries; developers specify the data style
and format directly in the worksheet. If the template includes macros,
they will run normally after the data is inserted.
You specify how the template is to be filled-in by creating a special
category of definition, the **Template definition**, in Logi Studio.
The Logi server engine provides two template output modes,
*OneWorksheet* and *OneWorksheetPerDataRow*.

## One Worksheet Mode

For flat data in **OneWorksheet** mode, data ranges are
*dynamic* if more than one data row is returned by a query. For
example, if ten rows are returned, the data range appears ten times on one
worksheet.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706704407/createxltemp_01_532x163.png)

In the example above, the data range (the yellow cells) is meant for order
information. To make the data range dynamic so that it uses a worksheet
row for each data row, you must choose OneWorksheet mode.
New *rows* are inserted into the worksheet for dynamic data ranges as
needed. Any information that lies beneath a dynamic data range is
"pushed down" as new rows are inserted.

## One Worksheet Per Data Row Mode

For flat data in **OneWorksheetPerDataRow** mode, data ranges are
*static* if more than one data row is returned by a query. If
ten rows are returned, then ten worksheets are produced, each containing
the data from one data row.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699603735/createxltemp_02_509x342.png)

In the example above, the data range shown is meant for a customer's
billing address. In order to make the data range static and produce one
worksheet for each customer returned by the query, you must choose
OneWorksheetPerDataRow mode.
