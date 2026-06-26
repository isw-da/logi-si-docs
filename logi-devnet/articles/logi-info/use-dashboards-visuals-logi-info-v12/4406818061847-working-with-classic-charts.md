---
title: "Working with Classic Charts"
id: 4406818061847
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818061847-Working-with-Classic-Charts
updated_at: 2022-04-06T06:09:55Z
---

# Working with Classic Charts

# Working with Classic Charts

Logi Info includes a family of legacy **Chart** and **Gauge** visualization elements, now collectively called "Classic Charting elements", for use in reports.

The following topics discuss the use of those elements and provides guidance for implementing them:

* [General Chart Appearance](https://devnet.logianalytics.com/hc/en-us/articles/4406818058775-General-Chart-Appearance#General)
* [Data Retrieval and Appearance](https://devnet.logianalytics.com/hc/en-us/articles/4406818057239-Data-Retrieval-and-Appearance#Data)
* [Title, Labels, and Legends](https://devnet.logianalytics.com/hc/en-us/articles/4406818060823-Title-Labels-and-Legends#Legends)
* [Drill-Down and Drill-Through Features](https://devnet.logianalytics.com/hc/en-us/articles/4406822613527-Drill-down-and-Drill-through-Features#Down)
* [Interactive Chart Configurations](https://devnet.logianalytics.com/hc/en-us/articles/4406818059799-Interactive-Chart-Configurations#Interactive)
* [Working with Gauges](https://devnet.logianalytics.com/hc/en-us/articles/4406822614423-Work-with-Gauges#NGauges)
* [Default Color Sets](https://devnet.logianalytics.com/hc/en-us/articles/4406822612631-Default-Color-Sets#DefaultColorSet)

## About Working with Classic Charts

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Logi Info includes a set of JavaScript-based charting elements collectively called "Chart Canvas" charts. We recommend that you use them for any new applications you create or if you update existing applications. Wizards in Logi Studio that help you create charts will create Chart Canvas charts. For more information about these chart, see [Chart Canvas Charts](https://devnet.logianalytics.com/hc/en-us/articles/4406817156247-Chart-Canvas-Charts).

*A number of Classic Charts have been deprecated; they are still supported and will work, but their elements are no longer available in Studio. For more information, see [Classic Charts & Gauges](https://devnet.logianalytics.com/hc/en-us/articles/4406817713047-Classic-Charts-Gauges) and [Chart Canvas Charts](https://devnet.logianalytics.com/hc/en-us/articles/4406817156247-Chart-Canvas-Charts).*

Logi Info's Classic Chart and Gauge elements provide powerful features for creating visualizations. The information presented in this topic is intended to allow you to quickly gain an understanding of how Logi charting elements work and to rapidly create simple charts.

Classic charts and gauges fall into two categories: *Static* and *Animated*, depending on whether they can draw themselves with animation.

| Classic Chart Type | Description |
| --- | --- |
| Animated Charts | Classic animated charts and gauges use **HTML5** features and **JavaScript** to render animated visualizations. Flash animation is *not* supported and these charts are *not exportable*. |
| Static Charts | Static charts and gauges are rendered on the report page as an **image**, so they do not require any special browser add-ins to be viewed and they *are**exportable*. |

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Due to the varying nature of the elements, the attributes used in examples below are not *all* available for *all* charting elements. Attributes and child "helper" elements may be quite chart-style specific; developers need to apply common sense when implementing charts based on the examples shown here.

Developers unfamiliar with Logi Classic Chart elements are encouraged to read [Classic Charts & Gauges](https://devnet.logianalytics.com/hc/en-us/articles/4406817713047-Classic-Charts-Gauges) before proceeding.

Due to the large number of attributes available for Classic Charts, in the examples that follow the Attributes Panel screenshots have been edited to show only the relevant attributes in order to conserve space.
