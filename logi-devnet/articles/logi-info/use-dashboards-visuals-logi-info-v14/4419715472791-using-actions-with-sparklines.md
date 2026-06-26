---
title: "Using Actions with Sparklines"
id: 4419715472791
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715472791-Using-Actions-with-Sparklines
updated_at: 2022-07-17T01:38:00Z
---

# Using Actions with Sparklines

# Using Actions with Sparklines

Sparklines can be made interactive by using **Action** elements with
them:

![](https://devnet.logianalytics.com/hc/article_attachments/4419707065623/spark_08.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419714897943/spark_08a.png)

In the example shown above, **Action.Report**, **Target.Report** and
**Link Parameters** elements are used beneath a Sparkline element. Any
of the following Action elements can be used:

* Action.Report
* Action.Link
* Action.Process
* Action.Javascript

and additional Action elements will likely be added in the near future.
Link Parameters associated with these actions can reference both the @Data
tokens (the Data Table data) and @Chart tokens (the Sparkline data)
available at runtime.
