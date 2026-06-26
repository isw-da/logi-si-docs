---
title: "Adding a Marker Band"
id: 4419707400343
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707400343-Adding-a-Marker-Band
updated_at: 2022-07-17T01:57:56Z
---

# Adding a Marker Band

# Adding a Marker Band

The **Marker** **Band** child element allows you to add a value-based band to the chart, independent of the series:

![](https://devnet.logianalytics.com/hc/article_attachments/4419699587223/introcccharts_104.png)

A marker band is shown in the example above. The Marker Band element has attributes that allow you to set the properties of the band, such as color and transparency, and to set its caption and values. Its **From Value** and **To Value** attributes accept tokens and can be set from data, however, it's a *straight* band rather than a band based on a number of data points, so using a data token that represents a range of values will produce unpredictable results.

The Marker Band element has a child element, the **Marker Label Style** element, which allows you to style the optional caption, by specifying its font properties, format, positioning, and alignment.
