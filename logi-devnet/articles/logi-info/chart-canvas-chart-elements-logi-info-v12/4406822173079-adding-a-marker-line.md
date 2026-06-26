---
title: "Adding a Marker Line"
id: 4406822173079
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822173079-Adding-a-Marker-Line
updated_at: 2022-04-06T06:04:19Z
---

# Adding a Marker Line

# Adding a Marker Line

The **Marker Line** child element allows you to add a value-based line to the chart, independent of the series:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563494423/introcccharts_103.png)

A marker line is shown in the example above. The Marker Line element has attributes that allow you to set the properties of the line, such as color, thickness, and line style, and to set its caption and value. Its **Value** attribute accepts tokens and can be set from data, however, it's a *straight* line rather than a line based on a number of data points, so using a data token that represents a range of values will produce unpredictable results.

The Marker Line element has a child element, the **Marker Label Style** element, whichallows you to style the optional caption, by specifying its font properties, format, positioning, and alignment.
