---
title: "Adding Multiple Axes"
id: 4419707401367
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707401367-Adding-Multiple-Axes
updated_at: 2022-07-17T01:57:53Z
---

# Adding Multiple Axes

# Adding Multiple Axes

It's not unusual to need to produce a chart that has multiple series, requiring a secondary axis. Here's an example:

![](https://devnet.logianalytics.com/hc/article_attachments/4419706682647/introcccharts_85.png)

The example above shows two Series but, because they have different data value scales, a secondary Y-axis has been added on the right side. Many charts that compare multiple data series over time can use the same data scale for all series, but that's not the case here, so a secondary Y-axis is necessary. It's easy to add a secondary axis to a chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714673431/introcccharts_86.png)

To add a second Y-axis to the chart, add a second **Y-Axis** element to the definition, as shown above. Set its **Opposite Side** attribute to *True* and give both Y-Axis elements a unique element ID. This creates the secondary Y-axis, on the *right* side of the chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699587479/introcccharts_87.png)

But which Series will use which Y-axis? You associate a Series with a Y-Axis element by setting the Series' **Linked to Y-Axis ID** attribute, as shown above, to the element ID of the desired Y-Axis element. Do this for each Series element.
