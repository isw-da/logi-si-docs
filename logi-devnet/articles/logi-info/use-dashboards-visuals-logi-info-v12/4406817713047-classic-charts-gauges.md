---
title: "Classic Charts & Gauges"
id: 4406817713047
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817713047-Classic-Charts-Gauges
updated_at: 2022-04-06T06:07:44Z
---

# Classic Charts & Gauges

# Classic Charts & Gauges

Logi Info offers developers a rich selection of charts for data visualization.

The following topics discusses one of the families of charts and gauges available, Classic Charts:

* [Gallery of Classic Chart and Gauge Elements](https://devnet.logianalytics.com/hc/en-us/articles/4406822444823-Gallery-of-Classes-Chart-and-Gauge-Elements#Gallery)
* [Gallery of Deprecated Classic Charts](https://devnet.logianalytics.com/hc/en-us/articles/4406817712023-Gallery-of-Deprecated-Classic-Charts#DepClassicCharts)

*A number of Classic Charts have been deprecated; they are still supported and will work, but their elements are no longer available in Studio. Whenever possible use [Chart Canvas Charts](https://devnet.logianalytics.com/hc/en-us/articles/4406817156247-Chart-Canvas-Charts) instead for all new development. See the gallery tables below for details.*

## About the Classic Charting Elements

Chart Canvas Charts were introduced in v11.2.040. The container or root element for charts in this family is the **Chart Canvas** element. These charts use HTML5 features and JavaScript. For more information about these charts, see [Chart Canvas Charts](https://devnet.logianalytics.com/hc/en-us/articles/4406817156247-Chart-Canvas-Charts).

We refer to charts and gauges that were existed *prior* to the introduction of Chart Canvas Charts as our "Classic Charts and Gauges". They fall into two categories: *Static* and *Animated*, depending on whether they can draw themselves with animation.

| Classic Chart Type | Description |
| --- | --- |
| Animated Charts | Classic animated charts and gauges use **HTML5** features and **JavaScript** to render animated visualizations. Flash animation is *not* supported and these charts are *not exportable*. |
| Static Charts | Static charts and gauges are rendered on the report page as an **image**, so they do not require any special browser add-ins to be viewed and they *are**exportable*. |

Some individual charting elements are capable of producing several different types of charts. For example, **Chart.XY** produces *Line*, *Bar*, *Area*, and *Spline* charts. These charting elements give you the ability to adjust many aspects of your charts and, as a result, multi-type chart elements have a lot of attributes, but some of them only apply to a particular chart type and not to others.

If you're just beginning to work with Logi chart elements you'll find that it's a very iterative
process and there are usually many small adjustments to be made until your charts are "just right". This is inherent in having the level of flexibility that our customers demand.

Logi Studio includes several **wizards** that can help you get started creating charts and gauges, but they generate Chart Canvas Charts, not Classic Charts.

Additional information that will allow developers to quickly get started creating charts is available in [Working with Classic Charts](https://devnet.logianalytics.com/hc/en-us/articles/4406818061847-Working-with-Classic-Charts).
