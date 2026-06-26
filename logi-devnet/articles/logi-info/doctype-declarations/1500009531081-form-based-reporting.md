---
title: "Form-based Reporting"
id: 1500009531081
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531081-Form-based-Reporting
updated_at: 2021-06-17T01:58:27Z
---

# Form-based Reporting

# Form-based Reporting

This topic introduces developers to **form-based reporting**, which delivers highly-formatted reports to clients via a web browser, using Logi reporting products. Topics include:

* About Form-based Reporting
* [Adobe PDF Templates](#sec1)
* [Microsoft Excel Templates](#sec2)
* [Microsoft Word Templates](#Word)
* [The Template Definition](#sec3)
* [Debug Templates](#Debugging)

*Template definitions are only available in Logi Report v10 starting with v10.1.59*.

## About Form-based Reporting

"Form-based reporting" is a special technique in which report developers create report "forms", or **template files**, with specific regions designated in them for data. At runtime, the Logi Server Engine **fills-in** the specified data regions, leaving all the other report layout and formatting information unaffected. Examples of popular implementations of this technique include the generation of employment applications, tax forms, health care forms and invoices. The final
content generated must accurately render the form *and* data without distortion or other formatting changes.

Form-based reporting differs from web-based reporting in the way developers use Logi reporting tools. For web-based reports, developers use Logi Studio as the design front-end; the data and report layout are built using report definitions.

However, for form-based reporting, other vendors' tools are used to create the actual output document layout. Logi Studio is then used to develop the data retrieval and population mechanisms. To facilitate this, Logi reporting tools provide **template****definitions** which are "blueprints" that indicate how data is mapped into the appropriate regions in a document.

Template *files* are typically stored in the \_SupportFiles folder but may be stored in any custom folder that you might want to create within your application root folder. Template *definitions* are stored in the \_Definitions/\_Templates folder.

## Adobe PDF Templates

The Adobe **Portable Document Format** (PDF) is an industry standard for highly-formatted reports and documents. Developers can create PDF templates using any standard PDF editing tool. A PDF template includes editable form fields as well as static information such as graphics, text, bar-coding and boilerplate information.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778562071/introformbased_01.gif)

The image above shows an empty **PDF form** template for an invoice. The locations of the **form fields** within the template determine the placement and appearance of the data in the final document. Developers can define and format text and numeric information on the form, as well as present data in a fixed tabular form.

## Microsoft Excel Templates

Business analysts work with **worksheets** every day to build highly-formatted reports. Logi Analytics gives Logi developers the ability to use Microsoft Excel as the design front-end for this purpose. The Logi server engine fills-in the empty Excel template with data from one or more data sources.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778562327/introformbased_02.gif)

The image above shows an Excel template for synthetic rating estimation, based on firm type, earnings and expenses. Charts, formulas, and pivot tables are dynamically updated based on the data contained in the worksheet. Templates are not restricted to *one* worksheet; a single report template can contain one or more worksheets within a **workbook**. Developers can also specify whether the final document contains one filled template or multiple filled templates by toggling an attribute
within the
Logi Template definition.

## Microsoft Word Templates

Microsoft Word can also be used to design document templates and, as with Excel templates, the Logi server engine fills-in the empty template with data from one or more data sources.

## 

The image above shows part of a Word report template for adverse health care event information. The fields on the form template are filled-in by the Logi server engine and then the Word document can be processed like other templates: returned to the user's browser, saved, emailed, etc.

## The Template Definition

Logi Studio provides a special category of definition file, the **Template definition**, for use with form-based reporting. A Logi Template definition references a PDF, Excel, or Word template file (the target), specifies one or more datasource queries, and specifies how the target template is to be filled-in.

At runtime, the Logi Server Engine fills the data regions specified in the target template with data values and generates a new output document of the specified type. Developers
control the delivery
mechanism for the new document (e.g. return to the browser, save on the server, embed in an email, etc.).

In a Logi application, template definitions are stored in the \_Definitions/\_Templates folder. In Studio, they appear beneath a Templates folder in the Application panel. Each template definition includes elements that are specific to the document type being generated and they're used to map the data into the native document template. The details of creating Template definitions are discussed in separate DevNet topics specific to each document
type.

### Use Template Definitions

Two approaches are available for using Template definitions to product a document:

* In a Logi *Report* definition, the document is generated and returned to the user's web browser.
* In a Logi *Process* definition (in Logi Info only), a task saves the generated document as a file on the web server.

In the first approach, the **Action.Template** and **Target.Template** elements are used to reference template definitions:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778562967/introformbased_03.gif)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771687191/introformbased_04.png)

The example above shows these elements in a Report Definition; they cause the "Invoice" template definition to be used to fill-in and generate the desired document. By default, the document is given a randomly-generated, GUID-based filename and is temporarily stored in the application's rdDownload folder, and then returned to the user's web browser to be viewed immediately, or saved locally.

If a fully-qualified path and filename is specified for the **Export Filename** attribute, the document will be stored as that file on the web server, and then returned to the user's web browser to be viewed immediately, or saved locally. Examples of valid file names are:

@Function.AppPhysicalPath~\Exports\Invoices.xls  
C:\inetpub\wwwroot\MyLogiApp\MyTemplateDocs\FormLetters.xls

Naturally, the account used to run your Logi application must have full File Access permissions to any folder that will contain saved documents.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778563351/introformbased_05.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771687447/introformbased_05a.png)

In the second approach, the **Procedure.SaveTemplate** and **Target.Template** elements are used in a Process task:

The example above shows a Process Definition task; it also causes the "Invoice" template definition to be used to fill-in and generate a document. However, in this case, the document is saved as a file, using the fully-qualified path and filename specified, and is *not* automatically returned to the user's web browser for viewing. Developers, using other elements, can then work with the saved file, perhaps linking it to the browser or sending it out in an
email. Examples of valid file names are the same as those shown above and File Access permissions must be in place as discussed previously.

Templates provide a powerful reporting mechanism and Logi reporting products provide a number of ways of generating and distributing them. For additional information about specific type of templates, see our other Template documents.

## Debug Templates

Beginning with v10.0.269, **debugging features** have been added to make it easier for you to determine what happens when a template is filled. These debugging features are enabled if you have the report's debugging style set to *Debugger Links*, either from Studio's toolbar or by manually configuring in it the \_Settings definition.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771687703/introformbased_06.gif)

For **Excel** templates, a debugging link, as shown above, will be displayed in the template. Clicking this link will display a typical Debugger Trace page, with details of the template operation.

For **Word** and **PDF** templates, no such link will be displayed. However, a file with the debug information will be saved, and you can browse it directly. The filename will be:  *yourLogiAppfolder*/rdDownload/GUID + *templateName*-rdDebug.htm
