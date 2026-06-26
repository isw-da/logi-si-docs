---
title: "Export Chart Canvas Charts"
id: 4406822067095
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822067095-Export-Chart-Canvas-Charts
updated_at: 2022-04-06T06:02:51Z
---

# Export Chart Canvas Charts

# Export Chart Canvas Charts

Chart Canvas Charts can be exported in several ways.

* Exporting to .PDF Document
* [Exporting to .PNG Image](#PNG)

## Exporting to .PDF Document

If you choose to export Chart Canvas charts as part of a complete report
page, using Action.Export PDF and Target.PDF elements, the charts are
exported as SVG objects rather than as images. This results in Chart
Canvas charts exported to a PDF document having extremely high resolution
- they can be zoomed or printed with high-quality at any resolution.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) When exporting Chart Canvas charts to PDF, the **Chart Canvas** element
*must* have Height and Width attribute values set.

The attributes of the Action and Target elements can be configured to
specify a variety of things that relate mostly to the overall report
rather than to any charts they contain. During the process, however, a
"hidden" copy of the report page is generated and used as the
source for the PDF export engine. Ensure that this copy receives all of
the parameters used to generate the visible page by using a Link
Parameters element, a child of the Action element, and passing necessary
values.

## Exporting to .PNG Image

Chart Canvas charts can be configured to include an "export to .PNG
image" feature.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584231831/exportchart_01.png)

This is done by adding either a **Chart Export** element as a child of
a specific Chart Canvas Chart element, as shown above left, or by adding a
**Global Chart Export** element as a child of the General element in
the \_Settings definition, as shown above right.
Adding either Chart Export element enables the feature in the chart:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575927063/exportchart_02.png)

When enabled, hovering your mouse cursor over the upper right-hand corner
of the chart will cause the **Get Image** button to appear. Click it to
proceed.

![](https://devnet.logianalytics.com/hc/article_attachments/4417592016791/exportchart_03.png)

You're essentially *downloading* the image, so the browser will
behave in whatever manner it's been configured for when handling
downloads. It may automatically save the image to its Downloads folder or,
as shown above, you may be prompted to open (view) the image or select a
location for saving it.

### Attributes

Both of the Chart Export and Global Chart Export elements have an optional
**Export Filename** attribute that allows you to specify a name for the
downloaded .PNG image file and it accept tokens, so you can dynamically
include time stamps, user names, etc. in it. If not specified, then the
file is simply downloaded as "chart.png".
The Chart Export element also allows you to optionally specify an
**ID** and a **Security Right ID**. When using Logi Security, the
latter allows you to control who can export a chart image.

### Child Elements

Two child element are available that let you style the Get Image button.
The **Chart Export Button Style** element lets you position, style, and
customize the button, and the
**Chart Export Button Hover Style** element lets you control the
appearance of the button when the mouse cursor is hovered over it.
