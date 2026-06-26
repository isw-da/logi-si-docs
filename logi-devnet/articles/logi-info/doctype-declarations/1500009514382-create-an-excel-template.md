---
title: "Create an Excel Template"
id: 1500009514382
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514382-Create-an-Excel-Template
updated_at: 2021-06-17T01:58:07Z
---

# Create an Excel Template

# Create an Excel Template

Form-based reporting provides a powerful method for making data available in popular formats. This topic describes how to create a **Microsoft Excel** **Template** for use with form-based reporting and Logi reporting products.

* About Excel Templates
* [Create the Template and Data Ranges](#Ranges)
* [Work with Charts and Formulas](#Formulas)
* [Prepare for Hierarchical Data](#Data)

*Template definitions are only available in Logi Report v10 starting with v10.1.59*.

For basic information about templates and calling them from within Logi applications, see [Form-based Reporting](https://devnet.logianalytics.com/hc/en-us/articles/1500009531081-Form-based-Reporting).

## About Excel Templates

Developers use Microsoft Excel to create Excel templates, which are saved as **.xltx** (Excel 2007) or **.xlt** (earlier versions) files. These become the "blueprint" for mapping data, using Logi reports, from datasource to Excel worksheets.

In this scheme, one Excel template populates one Excel workbook. Developers can create Excel templates that use multiple worksheets, if desired, to utilize 3-D formulas or to better organize template content.

Before creating the template, developers should consider the following:

* Which areas in the template will be reserved for data?
* Will the template include any charts or formulas?
* Is the data itself hierarchical or flat?

Once these questions have been answered, you're ready to begin creating a template.

## Create the Template and Data Ranges

Microsoft Excel templates generally consist of both static content, called the *template**area*, and landing areas for dynamic content, called the *data* *area* or *data range*. In order to preserve highly-formatted templates, when it generates output, the Logi server engine makes **no modifications** to the template area. The data range, however, is **filled-in** at runtime with the data retrieved by one or more data queries; developers specify the data
style and format directly in the worksheet.

Developers specify how the template is to be filled-in by creating a special category of definition, the template definition, in Logi Studio.

The Logi server engine provides two template output modes, OneWorksheet and OneWorksheetPerDataRow.

### One Worksheet Mode

For flat data in **OneWorksheet** mode, data ranges are **dynamic** if more than one data row is returned by a query. For example, if ten rows are returned, the data range appears ten times on one worksheet.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771881367/createxltemp_01.png)

In the example above, the data range (the yellow cells) is meant for order information. To make the data range dynamic so that it uses a worksheet row for each data row, the developer must choose **OneWorksheet** mode.

New rows are **inserted** into the worksheet for dynamic data ranges as needed. Any information that lies beneath a dynamic data range is "pushed down" as new rows are inserted.

### One Worksheet Per Data Row Mode

For flat data in **OneWorksheetPerDataRow** mode, data ranges are **static** if more than one data row is returned by a query. If ten rows are returned, then ten worksheets are produced, each containing the data from one data row.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771881623/createxltemp_02.png)

In the example above, the data range shown is meant for a customer's billing address. In order to make the data range static and produce one worksheet for each customer returned by the query, the developer must choose **OneWorksheetPerDataRow** mode.

## Work with Charts and Formulas

Charts and formulae in the template are **automatically updated** when the report is run. Microsoft Excel requires at least **two values** in a formula so that the formula is updated properly when new data rows are inserted into the worksheet. Developers are encouraged to use dummy values in order to test formulae, charts and other objects included in the report template.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771881879/createxltemp_03.png)

Extra rows can be added to the data range for the purposes of testing a formula or adding a chart. To prevent them from being included in the final report, developers can use special ranges called **disposable ranges**. Logi Studio provides a way to declare a range "disposable" and the Logi report server removes these ranges in the final report. See [Fill an Excel Template](https://devnet.logianalytics.com/hc/en-us/articles/1500009515062-Fill-an-Excel-Template) for more details.

## Prepare for Hierarchical Data

Hierarchical data is **multi-layered** data that contains numerous **parent-child relationships**. For example, for each customer, an invoice-style report may contain customer contact information and data for multiple orders. If the data for several customers is returned from a query and each customer has placed one or more orders, then a **hierarchical dataset** exists. The only **rule** developers must follow when creating a template for hierarchical data is
that **each level** in the hierarchy
must have its own **row**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771882135/createxltemp_04.png)

For example, the report template shown above **is configured properly** for three levels of hierarchical data. If additional data at the third level is retrieved, data in the correct columns will be extended downward in additional rows.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771882391/createxltemp_05.png)

However, the example shown above *is not* configured properly for multiple levels of data. If additional data at the second or third level is retrieved, data for all three levels will be extended downward in additional and meaningless rows.
