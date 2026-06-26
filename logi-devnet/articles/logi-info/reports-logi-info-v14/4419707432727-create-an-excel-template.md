---
title: "Create an Excel Template"
id: 4419707432727
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707432727-Create-an-Excel-Template
updated_at: 2022-07-17T01:56:02Z
---

# Create an Excel Template

# Create an Excel Template

Form-based reporting provides a powerful method for making data available
in popular formats.

The following topics provide guidance for creating a
Microsoft Excel Template to use with form-based reporting
and Logi Info applications:

* [Creating the Template and Data Ranges](https://devnet.logianalytics.com/hc/en-us/articles/4419722776215-Creating-the-Template-and-Data-Ranges#Ranges)
* [Working with Charts and Formulas](https://devnet.logianalytics.com/hc/en-us/articles/4419722777239-Working-with-Charts-and-Formulas#Formulas)
* [Preparing for Hierarchical Data](https://devnet.logianalytics.com/hc/en-us/articles/4419715183127-Preparing-for-Hierarchical-Data#Data)

For basic information about templates and calling them from within Logi
applications, see
[Form-based Reporting](https://devnet.logianalytics.com/hc/en-us/articles/4419722927127-Form-based-Reporting).

## About Excel Templates

Developers use Microsoft Excel to create Excel Templates, which are saved
as one of these file types:

* **.xltx** - called an "Excel Template"
* **.xlt** - called an "Excel 97-2003 Template"

These templates become the
"blueprint" for mapping the data from a datasource, retrieved
using a Logi application, into Excel worksheets.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png)
These are the *only* file types supported as templates in a Logi
application. Use of other file types may produce unpredictable results.
In this scheme, one Excel template populates one Excel workbook. You can
create Excel templates that use multiple worksheets, if desired, to
utilize 3-D formulas or to better organize template content.
Before creating the template, developers should consider the following:

* Which areas in the template will be reserved for data?
* Will the template include any charts or formulas?
* Is the data itself hierarchical or flat?

Once these questions have been answered, you're ready to begin creating a
template.
