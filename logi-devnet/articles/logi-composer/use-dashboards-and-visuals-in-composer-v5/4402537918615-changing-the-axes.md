---
title: "Changing the Axes"
id: 4402537918615
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537918615-Changing-the-Axes
updated_at: 2021-09-15T02:22:53Z
---

# Changing the Axes

# Changing the Axes

Many visual styles show data on a standard coordinate grid, with axes labels identifying the values depicted horizontally and vertically on the visual.
Examples include [bar charts](https://devnet.logianalytics.com/hc/en-us/articles/4402552918295-Bar-Chart-Styles), [line charts](https://devnet.logianalytics.com/hc/en-us/articles/4402537924631-Line-Charts), and [scatter charts](https://devnet.logianalytics.com/hc/en-us/articles/4402552933143-Scatter-Bubble-Charts).

Use the axes labels on these visuals to change the metric (y-axis) and attribute (x-axis) fields graphed in the visual. The number of labels displayed on a visual depend on the [number of metrics and attributes](https://devnet.logianalytics.com/hc/en-us/articles/4402537848855-Visual-Metrics-and-Attributes-Reference) on which the visual is based.

![](https://devnet.logianalytics.com/hc/article_attachments/4406753449751/axes-labels_576x285.png)

You can specify the default visual metric and group fields for visuals on the [Visuals tab](https://devnet.logianalytics.com/hc/en-us/articles/4402537788695-Visuals-Tab) of your data source configurations. A shortcut to this tab is available when working with a visual by selecting **Defaults** on the visual menu (![](https://devnet.logianalytics.com/hc/article_attachments/4406763902743/three-dots-menu_19x11.png)). Controls for these options are provided using the interactivity sidebar. See [*Controlling How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4402537944215-Controlling-How-Users-Interact-With-a-Visual).

See the following topics:

* [*Changing a Group Attribute*](#Changing)
* [*Changing a Metric Field*](#Changing2)

You can also change the metric used to determine the colors on the visual. See [*Changing the Visual Color Metric*](https://devnet.logianalytics.com/hc/en-us/articles/4402537921303-Changing-the-Visual-Color-Metric).

## Changing a Group Attribute

You can change the x-axis field, or group attribute, on a visual that plots data on a coordinated grid.

To change the visual group (x-axis) attribute:

1. Select the group attribute (x-axis) label on your visual. A Group dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763926167/group-dialog_150x319.png)
2. Select a new field to be viewed on the x-axis of your visual.

   The visual renders the newly selected attribute.

## Changing a Metric Field

You can change the y-axis field, or metric, on a visual that plots data on a coordinated grid.

To change the visual metric (y-axis field):

1. Select the metric (y-axis) label on your visual. A Metric dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763926423/metric-dialog_150x136.png)
2. Select a new metric to use as the y-axis of your visual and a metric function to use to aggregate the data on the visual. See [*Available Metric Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402537777687-Available-Metric-Functions).

   The visual is updated and renders the newly selected metric. If you need to perform more complex analysis of your data set, you can
   [add custom metrics](https://devnet.logianalytics.com/hc/en-us/articles/4402537760023-Maintain-Custom-Metrics) .
