---
title: "Form-based Reporting"
id: 4419722927127
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722927127-Form-based-Reporting
updated_at: 2022-07-17T02:07:44Z
---

# Form-based Reporting

# Form-based Reporting

Form-based reporting delivers highly-formatted reports generated using Logi
Info, via a web browser.

The following topics discuss form-based reporting:

* [Adobe PDF Templates](https://devnet.logianalytics.com/hc/en-us/articles/4419707596439-Adobe-PDF-Template#sec1)
* [Microsoft Excel Templates](https://devnet.logianalytics.com/hc/en-us/articles/4419707598359-Microsoft-Excel-Templates#sec2)
* [Microsoft Word Templates](https://devnet.logianalytics.com/hc/en-us/articles/4419722928023-Microsoft-Word-Templates#Word)
* [The Template Definition](https://devnet.logianalytics.com/hc/en-us/articles/4419707599383-The-Template-Definition#sec3)
* [Debugging Templates](https://devnet.logianalytics.com/hc/en-us/articles/4419707597463-Debugging-Templates#Debugging)

## About Form-based Reporting

*Form-based reporting* is a special technique in which
developers create *forms*, or *templates*, with specific
regions designated in them for data. At runtime, the Logi Server Engine
retrieves data and *fills-in* the specified data regions, leaving all
the other report layout and formatting information unaffected. Examples of
popular implementations of this technique include the generation of
employment applications, tax forms, health care forms, and invoices. The
final content generated must accurately render the form *and* the
data without distortion or other formatting changes.

Form-based reporting differs from web-based reporting in the way
developers use Logi Info. For web-based reports, developers use Logi
Studio as the design front-end and the data and report layout are built
using report definitions.

However, for form-based reporting, other vendors' tools are used to create
the actual output document layout, or **template file**. Logi Studio is
then used to develop the data retrieval and data population scheme. To
facilitate this, Logi Info provides **template** **definitions** which are "blueprints" that indicate how data
is mapped into the appropriate regions in a document.

Template *files* create with other vendor's tools are typically
stored in the
 \_SupportFiles
folder but may be stored in any custom folder that you might want to
create within your application root folder. Logi Template
*definitions* are stored in the application's
\_Definitions/\_Templates
folder. In Logi Studio, these definitions appear in a separate Templates
folder in the Application Panel.
