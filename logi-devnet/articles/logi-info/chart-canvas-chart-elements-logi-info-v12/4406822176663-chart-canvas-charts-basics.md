---
title: "Chart Canvas Charts Basics"
id: 4406822176663
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822176663-Chart-Canvas-Charts-Basics
updated_at: 2022-04-06T06:04:22Z
---

# Chart Canvas Charts Basics

# Chart Canvas Charts Basics

The Chart Canvas chart elements are based on a library written entirely in **HTML5** and **JavaScript**, and work very well in all modern desktop and mobile device browsers. No client-side technology, such as Flash or Java, is required. These elements provide a wide range of features *and* the flexibility to customize them to your requirements. Many desirable features, including animations and quicktips, are enabled by default, making it very easy to create great-looking charts quickly. In addition,
these charts are exportable in reports.

By default, Chart Canvas charts are rendered by the browser using SVG technology.
For browsers that do not support SVG, primarily IE 7 & 8, charts are rendered with
VML.

The PDF export engine was changed to Gecko-based technology and Chart Canvas charts are now exported as SVG objects rather than as images. This results in Chart Canvas charts exported to PDF having extremely high resolution - they can be zoomed or printed with high-quality at any resolution.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) When exporting Chart Canvas charts to PDF, the **Chart Canvas** element must have Height and Width attribute values set.
The legacy Static and Animated charts available in earlier versions of Logi Info have been deprecated. Developers should use Chart Canvas Charts for all new projects.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Chart Canvas charts are used by default for Super Elements, such as the Analysis Grid, in all *new applications.* Logi applications that are *upgraded* to v12 will use the classic static charts for their Super Elements. To force upgraded apps to use Chart Canvas charts, add the constant rdFavorChartCanvas
= True
to your \_Settings definition.

## Chart Geography

The following image explains many of the terms used to describe a typical Chart Canvas chart:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575853463/introcccharts_02.png)

The background color, line properties, and transparency of the areas and lines shown can all be controlled by setting attributes. Additional major and minor tick marks, and grid lines can be added. The spacing, style, and format of all the items shown can also be configured.
