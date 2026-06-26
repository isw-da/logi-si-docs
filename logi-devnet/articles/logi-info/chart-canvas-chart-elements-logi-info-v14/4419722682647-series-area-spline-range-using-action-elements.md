---
title: "Series.Area Spline Range - Using Action Elements"
id: 4419722682647
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722682647-Series-Area-Spline-Range-Using-Action-Elements
updated_at: 2022-07-17T02:00:24Z
---

# Series.Area Spline Range - Using Action Elements

# Series.Area Spline Range - Using Action Elements

Action elements initiate processing of a report or process task definition, redirection to a link, or other processing when a data point in the series is clicked.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714653207/series_areasplinerange_09.png)

In the example above, an **Action.Report** element has been added as a child of the Series, along with its **Target.Report** and **Link Parameters** child elements. To reference chart data in parameters, use the @Chart token, as shown above.

A variety of Action elements are available for use with Series, including Action.Link, Action.Process, and Action.Refresh Element. Additional Action elements will be added in future releases.
