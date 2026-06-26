---
title: "The Template Definition"
id: 4419707599383
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707599383-The-Template-Definition
updated_at: 2022-07-17T02:24:22Z
---

# The Template Definition

# The Template Definition

Logi Studio provides a special category of definition file, the
Template definition, for use with form-based reporting. A Logi
Template definition references a PDF, Excel, or Word template file (the
target), specifies one or more datasource queries, and specifies how the
target template is to be filled-in.

At runtime, the Logi Server Engine fills the data regions specified in the
target template with data values and generates a new output document of
the specified type. Developers control the delivery mechanism for the new
document (e.g. return to the browser, save on the server, embed in an
email, etc.).

In a Logi application, template definitions are stored in the
\_Definitions/\_Templates
folder. In Studio, they appear beneath a Templates folder in the
Application panel. Each template definition includes elements that are
specific to the document type being generated and they're used to map the
data into the native document template. The details of creating Template
definitions are discussed in separate DevNet topics specific to each
document type.

## Using Template Definitions

Two approaches are available for using Template definitions to product a
document:

* In a Logi Info *Report* definition, the document is generated and
  returned to the user's web browser.
* In a Logi Info *Process* definition, a task saves the generated
  document as a file on the web server.

In the first approach, the **Action.Template** and
**Target.Template** elements are used to reference template
definitions:

![](https://devnet.logianalytics.com/hc/article_attachments/7522813851415/introformbased_04_600x252.png)

The example above shows these elements in a Report Definition; they cause
the "Invoice" template definition to be used to fill-in and
generate the desired document. By default, the document is given a
randomly-generated, GUID-based filename and is temporarily stored in the
application's
rdDownload
folder, and then returned to the user's web browser to be viewed
immediately, or saved locally.
If a fully-qualified path and filename is specified for the
**Export Filename** attribute, the document will be stored as that file
on the web server, and then returned to the user's web browser to be
viewed immediately, or saved locally. Examples of valid file names are:

@Function.AppPhysicalPath~\Exports\Invoices.xlsx  
 C:\inetpub\wwwroot\MyLogiApp\MyTemplateDocs\FormLetters.xlsx

Naturally, the account used to run your Logi application must have full
File Access permissions to any folder that will contain saved documents.

![](https://devnet.logianalytics.com/hc/article_attachments/7522841318551/introformbased_05_577x107.png)

In the second approach, the **Procedure.SaveTemplate** and **Target.Template** elements are used
in a Process task:

The example above shows a Process Definition task; it also causes the
"Invoice" template definition to be used to fill-in and generate
a document. However, in this case, the document is saved as a file, using
the fully-qualified path and filename specified, and is
*not* automatically returned to the user's web browser for viewing.
Using other elements, you can then work with the saved file, perhaps
linking it to the browser or sending it out in an email. Examples of valid
file names are the same as those shown above and File Access permissions
must be in place as discussed previously.

Templates provide a powerful reporting mechanism and Logi reporting
products provide a number of ways of generating and distributing them. For
additional information about specific type of templates, see our other
Template documents.
