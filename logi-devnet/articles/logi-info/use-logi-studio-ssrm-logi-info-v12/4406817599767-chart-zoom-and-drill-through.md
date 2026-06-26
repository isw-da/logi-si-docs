---
title: "Chart Zoom and Drill-through"
id: 4406817599767
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817599767-Chart-Zoom-and-Drill-through
updated_at: 2022-04-06T06:07:07Z
---

# Chart Zoom and Drill-through

# Chart Zoom and Drill-through

An optional feature, is the ability to click a chart to view it in a larger scale in a separate window, and from there to drill down into the detail data used to generate the chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575626903/chartgrid_08.png)

The feature is included by adding a **Chart Grid Popup Zoom** element, as shown above, to the definition. Its sole attribute is for optional tooltip text.
When the optional **Chart Grid Drillthrough** child element is included, a Drillthrough button appears in the zoomed chart. Clicking this button causes the detailed, exportable data table to be displayed. This element has an optional **Caption** attribute which allows you to specify a title for the data table.
