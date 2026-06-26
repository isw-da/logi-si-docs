---
title: "Create a Word Template"
id: 1500009514442
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514442-Create-a-Word-Template
updated_at: 2021-06-17T01:58:08Z
---

# Create a Word Template

# Create a Word Template

Form-based reporting provides a powerful method for making information available in popular formats. This topic describes how to create a **Microsoft Word** **Template** for use with Logi Info.

* About Word Templates
* [Create the Template and Form Fields](#Ranges)
* [Prepare for Hierarchical Data](#Data)

For basic information about templates and calling them from within Logi applications, see [Form-based Reporting](https://devnet.logianalytics.com/hc/en-us/articles/1500009531081-Form-based-Reporting).

*Template definitions are only available in Logi Report v10 starting with v10.1.59*.

## About Word Templates

Developers use Microsoft Word to create Word templates, which are saved as .**dotx** (Word 2007) or **.dot** (earlier versions) files. For our purposes, one Word template is equivalent to one Word document. Developers can create Word templates with multiple pages, if desired, to better organize template content.

Before creating the template, developers should consider the following:

1. Which areas in the template will be reserved for data?
2. Will the template include any charts or formulas?
3. Is the data itself hierarchical or flat?

## Not Recommended For Mailing Labels

Logi template reports are *not* recommended for "mail merge"-type operations, such as producing pages of mailing labels, that require multiple data records to be used to fill-in data repetitively on the same page using generic field names. It's technically "possible" to do it by flattening the data into temporary files, or manually creating multi-page templates, but these approaches are inefficient and cumbersome.

## Create the Template and Form Fields

Microsoft Word templates consist of static content, called the *template**area*, and landing areas for dynamic content, called *form fields*.

In order to preserve highly-formatted templates, when it generates output, the Logi server engine makes no modifications to the template area. The form fields, however, are **filled-in** at runtime with the data retrieved by one or more queries; developers specify the data
style and format directly in the document. You must create a form field on the template for each data value you wish to display.

Detailed instructions for creating a Word template with form fields in multiple versions of Word are beyond the scope of this topic; please refer to your Word documentation for more information. In more recent versions of Word, the objects needed to define form fields in a document appear in the Developer toolbar and are called "Legacy Tools".

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778709015/createwordtemp_01.png)

When creating the template and adding form fields, you must assign each field a **unique name** using its **Bookmark** property. In the example shown above, in the field's Properties dialog box, the field has been given the unique name "CompanyName".

Developers specify how the template is to be filled-in by creating a special category of definition, the template definition, in Logi Studio.

Logi Studio provides the following template **output modes**:

* *OneForm* - With flat data, all the data returned by a single query is mapped to fields on one document page.
* *OneFormPerDataRow* - With flat data, the data returned by a query is mapped on a row-per-page basis. If ten rows of data are returned, then ten document pages are produced, each containing the data from one data row.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778709271/createwordtemp_02.png)

In this example of *OneForm* mode, shown above, each of the fields on this one form will be filled-in using the data from a single query.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771874967/createwordtemp_03.png)

In this example of *OneFormPerDataRow* mode, shown above, each *row* of data returned from a query will be used to fill-in the fields on one form page; there will be as many pages as there are data rows. All of the pages will be contained in one Word document.

**Working with Charts and Formulas**

If a calculated field in the Word template uses other fields in its formula, it will be updated when those other fields are filled with data. However, charts embedded in the Word template *may not* be updated. If a chart draws its data from form fields, then it can be updated if those fields are filled-in by the Logi report server at runtime.

## Prepare for Hierarchical Data

Hierarchical data is **multi-layered** data that contains numerous **parent-child relationships**. For example, an invoice-style report may contain customer order information and multiple invoice line items per order. If several orders are returned from the database and each contains one or more line items, a **hierarchical dataset** exists where the line items are related to a specific order.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771875351/createwordtemp_04.png)

Remember that form **fields** must be **defined in advance** for **all** the potential data; fields are **not****dynamically-created** based on the amount of data returned from a query. Repeating fields for child data records should be named by appending a number to them, for example, Qty\_01, Qty\_02, Qty\_03, etc.

For information concerning the Template definition used to fill a Word template, see [Fill a Word Template](https://devnet.logianalytics.com/hc/en-us/articles/1500009515082-Fill-a-Word-Template).
