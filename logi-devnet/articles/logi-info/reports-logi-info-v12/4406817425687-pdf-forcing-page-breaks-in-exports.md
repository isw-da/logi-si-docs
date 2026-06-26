---
title: "PDF - Forcing Page Breaks in Exports"
id: 4406817425687
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817425687-PDF-Forcing-Page-Breaks-in-Exports
updated_at: 2022-04-06T06:06:00Z
---

# PDF - Forcing Page Breaks in Exports

# PDF - Forcing Page Breaks in Exports

When a report is paginated during an export, it may be useful to be able to force a page break, for example, to ensure that sections of the report start on new pages. This can be done using the **Printer Page Break** element.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563307415/exportpdf_06.png)

You can add one or more **Printer Page****Break** elements beneath the **Body** element to break the exported pages where desired. In the example above, these elements ensure that the "dtProducts" table and the "dtOrders" table start on new pages. When the report is viewed in the browser, however, like the Printable Paging element, the Printer Page Break element has no effect.

### Forcing a Data Table Row Break

When working with data tables with multi-line rows, developers may want to ensure that rows break cleanly across pages of their PDF exports. In other words, they want to prevent different lines of the same data table row from appearing on different PDF pages. This can be accomplished through CSS, using code like:

.noPageBreakCell { page-break-inside: avoid; }

Assigning the above class to a **Data Table Column** element will create the desired effect.

### Printer Page Break Attribute Restriction

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) The Gecko-based rendering engine used in PDF exports does not fully support printer page breaks within HTML tables. This means that enabling the Printer Page Break attribute for the **Group Header Row**, **Group Summary Row**, and **More Info Row Column** elements, which use tables internally, will produce unpredictable
results in PDF exports.

As a "last resort" alternative you can make these page breaks work by switching to the older IE rendering
engine; this is done by creating
the constant rdPdfRenderingType=*MSHTML* in your \_Settings definition. Unfortunately, this will also eliminate some of the benefits of the Gecko engine, such as the ability to export Chart Canvas Charts
as SVG objects, and so it's not generally recommended.
