---
title: "The Analysis Grid for End Users"
id: 4419700102935
section: "Use Dashboards & Visuals - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419700102935-The-Analysis-Grid-for-End-Users
updated_at: 2022-07-17T02:25:21Z
---

# The Analysis Grid for End Users

# The Analysis Grid for End Users

The Analysis Grid has its own user interface that allows you manipulate data, create charts, change table layouts, and much more, at runtime.

The following topics introduce Logi Info *end-users* to the Analysis Grid:

* [Selecting Data](https://devnet.logianalytics.com/hc/en-us/articles/4419715072279-Analysis-Grid-Selecting-Data#Data)
* [Adding Formula Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419715058455-Analysis-Grid-Adding-Formula-Columns#Formula)
* [Filtering Rows](https://devnet.logianalytics.com/hc/en-us/articles/4419707291927-Analysis-Grid-Filtering-Rows#Filtering)
* [Showing, Hiding, and Moving Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419707299863-Analysis-Grid-Showing-Hiding-and-Moving-Columns#Columns)
* [Sorting Rows](https://devnet.logianalytics.com/hc/en-us/articles/4419715076631-Analysis-Grid-Sorting-Rows#Sorting)
* [Grouping Rows](https://devnet.logianalytics.com/hc/en-us/articles/4419707297815-Analysis-Grid-Grouping-Rows#Grouping)
* [Creating Aggregations](https://devnet.logianalytics.com/hc/en-us/articles/4419715060119-Analysis-Grid-Creating-Aggregations#Aggregating)
* [Creating Custom Aggregations](https://devnet.logianalytics.com/hc/en-us/articles/4419715062807-Analysis-Grid-Creating-Custom-Aggregations)
* [Controlling Paging](https://devnet.logianalytics.com/hc/en-us/articles/4419707286167-Analysis-Grid-Controlling-Paging#Paging)
* [Formatting Data](https://devnet.logianalytics.com/hc/en-us/articles/4419707295895-Analysis-Grid-Formatting-Data#Formatting)
* [Creating Charts and Gauges](https://devnet.logianalytics.com/hc/en-us/articles/4419715061143-Analysis-Grid-Creating-Charts-and-Gauges#Gauges)
* [Editing Chart Labels and Captions](https://devnet.logianalytics.com/hc/en-us/articles/4419707287959-Analysis-Grid-Editing-Chart-Labels-and-Captions-)![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1
* [Pivoting and Summarizing Data](https://devnet.logianalytics.com/hc/en-us/articles/4419715070999-Analysis-Grid-Pivoting-and-Summarizing-Data#Summarizing)
* [Zoom Control](https://devnet.logianalytics.com/hc/en-us/articles/4419715077655-Analysis-Grid-Zoom-Control-)
* [Exporting Data](https://devnet.logianalytics.com/hc/en-us/articles/4419715063959-Analysis-Grid-Exporting-Data#Exporting)
* [Adding Analysis Grid Charts to Dashboards](https://devnet.logianalytics.com/hc/en-us/articles/4419707285015-Analysis-Grid-Adding-Analysis-Grid-Charts-to-Dashboards-#Dashboards)

Information for *developers* is available in [The Analysis Grid for Developers](https://devnet.logianalytics.com/hc/en-us/articles/4419700096279-The-Analysis-Grid-for-Developers-).

## About the Analysis Grid

The Analysis Grid user interface consists of separate panels for controls, tables, and visualizations. At runtime, you can manipulate the controls, creating data analyses and visualizations on the fly. The Analysis Grid below displays both a chart and table:

![](https://devnet.logianalytics.com/hc/article_attachments/7522850256919/usingag_01.png)

As you can see in the examples below, the Analysis Grid can look quite different depending on the Theme being used. The examples in this topic use the Signal Theme.

![](https://devnet.logianalytics.com/hc/article_attachments/7522834022807/usingag_02.png)

The Analysis Grid consists of a set of panels. The **Controls Panel**, at the top, includes a set of tabs or buttons that allow you to manipulate the data and visualizations at runtime. The visibility of specific controls is configured by the application developer and so you may or may not see the full set shown here.

When a tab or button is clicked, a configuration panel for that feature appears, as shown abelow. Clicking it again hides the panel.

![](https://devnet.logianalytics.com/hc/article_attachments/7522850300951/usingag_03.png)

**Visualization Panels** contain either a Data Table, Crosstab Table, or chart. Panels can be collapsed or expanded using the "+" and "-" icons. You can also rearrange their order by clicking with your mouse near the top of a panel, and dragging it up or down.

Panels containing tables may display an icon for exporting them to Excel, CSV, or PDF. The availability of the different types of exports is under developer control, so those available to you may vary.

![](https://devnet.logianalytics.com/hc/article_attachments/7522881155223/usingag_04.png)

Clicking a panel's **gear** icon will display a configuration area for the
specific visualization. The Table configuration area, shown below, allows you to control a variety of table features.

![](https://devnet.logianalytics.com/hc/article_attachments/7522881163415/usingag_04a_397x293.png)

Table column *headers* contain a variety of features. They can be *dragged*
to rearrange the column order or to adjust column widths. When column
header text is clicked, drop-down menus provide sorting, filter,
formatting, grouping, and other features, as shown below. The
availability of each feature can be restricted during development.

![](https://devnet.logianalytics.com/hc/article_attachments/7522856368535/usingag_04b.png)

If your application has been configured for it, **Undo** and **Redo** icons also display on the Control Panel, circled
below. These allow you to undo and redo your recent
actions.

![](https://devnet.logianalytics.com/hc/article_attachments/7522864468631/usingag_04c.png)

Additionally, if your application has been configured for it, a **Pause Data Retrieval** button displays next to the Control Panel. When clicked, it temporarily halts data retrieval from the server. This feature is useful when data retrieval is slow and you prefer to make several changes to the Analysis Grid without having to wait for data after each change.

![](https://devnet.logianalytics.com/hc/article_attachments/7522834050199/pause_data_retrieval_848x75.png)

Click the **Resume** button, shown below, to resume retrieval.

![](https://devnet.logianalytics.com/hc/article_attachments/7522881211287/resume_data_retrieval_848x196.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 Depending on your application's configuration, this feature may be enabled by default. As always, you can select **Resume** to retrieve data results.
