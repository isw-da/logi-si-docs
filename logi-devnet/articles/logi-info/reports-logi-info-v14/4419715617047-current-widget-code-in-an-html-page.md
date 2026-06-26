---
title: "Current Widget Code in an HTML Page"
id: 4419715617047
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715617047-Current-Widget-Code-in-an-HTML-Page
updated_at: 2022-07-17T01:28:28Z
---

# Current Widget Code in an HTML Page

# Current Widget Code in an HTML Page

There are certain **limitations** for widgets and not all Logi report elements are available for use with them. As our Logi Widget technology continues to evolve, the following limitations may be reduced. These elements *cannot* be used with widgets:

* Action.AppDev
* Action.Exit
* Action.Export (all varieties)
* Action.GoogleSpreadsheet
* Action.Process
* Action.RefreshElement
* Action.Template
* Analysis Chart
* Analysis Grid
* Dashboard
* Interactive Data View
* Google Map
* Input Date
* Input File Upload
* OLAP Grid
* Procedure (all varieties)
* Security Filter
* Shapes (all varieties)
* Sub-Report
* Tabs
* UserRoles (all varieties)

The unsupported "super elements", including Analysis Chart, Analysis Grid, Dashboard, IDV, and Google Map, can be used by placing them in separate Logi application pages and accessing them via a drill-through link on the widget.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) Widgets *cannot* use **shared elements** that are defined in other definition types. For example, shared elements created in a report definition are not available for use in a widget definition.
