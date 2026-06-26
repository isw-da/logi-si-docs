---
title: "Input Selection"
id: 4419715093399
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715093399-Input-Selection
updated_at: 2022-07-17T02:01:16Z
---

# Input Selection

# Input Selection

The Chart Canvas element's Series child elements cause a data visualization (the chart) to be rendered in the canvas. The **Input Selection** family of elements is available beneath some Series elements and provides the ability to interactively select portions of charts using the mouse and initiate actions using the selected data.

The following topics discuss the Input Selection child element:

* [Using Input Selection Point](#Point)
* [Using Input Selection Range](#Range)

## About Input Selection

Input Selection elements turn a chart into an input control, allowing the user to make selections on the chart at runtime. The data represented within the selected chart area can then be used with other actions. Drilling into detail data is one example of how this can be used.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699552279/introcccharts_126.png)

In the example above, at runtime, a "selection area" has been "drawn" (by dragging the mouse)
onto the chart to select values. The values within the selection area are
automatically submitted to the next definition as Request tokens. Page submission may or may not be triggered when drawing the area ends. The appearance of selected areas or points can be independently styled.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706655127/introcccharts_126a.png)

The example shown above uses Input Selection Point configured to allow selection of multiple data points. In this case, the page submission is *not* triggered by the selection process.

Let's examine the elements used for chart input selection.
