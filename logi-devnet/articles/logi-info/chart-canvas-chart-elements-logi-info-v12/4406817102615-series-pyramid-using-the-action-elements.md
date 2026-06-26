---
title: "Series.Pyramid - Using the Action Elements"
id: 4406817102615
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817102615-Series-Pyramid-Using-the-Action-Elements
updated_at: 2022-04-06T06:04:02Z
---

# Series.Pyramid - Using the Action Elements

# Series.Pyramid - Using the Action Elements

Action elements initiate processing of a report or process task definition, redirection to a link, or other processing when a segment in the pyramid is clicked.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584133271/series_pyramid_09.png)

In the example above, an **Action.Report** element has been added as a child of the Series, along with its **Target.Report** and **Link Parameters** child elements. To reference chart data in parameters, use the @Chart token, as shown above.
A variety of Action elements are available for use with Series, including Action.Link, Action.Process, and Action.Refresh Element. Additional Action elements will be added in future releases.
