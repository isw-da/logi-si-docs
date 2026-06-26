---
title: "The Analysis Grid for End Users"
id: 4406816992279
section: "Use Dashboards & Visuals - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816992279-The-Analysis-Grid-for-End-Users
updated_at: 2022-04-06T06:03:15Z
---

# The Analysis Grid for End Users

# The Analysis Grid for End Users

The Analysis Grid has its own user interface that allows you manipulate data, create charts, change table layouts, and much more, at runtime.

The following topics introduce Logi Info *end-users* to the Analysis Grid:

* [Selecting Data](https://devnet.logianalytics.com/hc/en-us/articles/4406817000215-Analysis-Grid-Selecting-Data#Data)
* [Adding Formula Columns](https://devnet.logianalytics.com/hc/en-us/articles/4406822097047-Analysis-Grid-Adding-Formula-Columns#Formula)
* [Filtering Rows](https://devnet.logianalytics.com/hc/en-us/articles/4406822101271-Analysis-Grid-Filtering-Rows#Filtering)
* [Showing, Hiding, and Moving Columns](https://devnet.logianalytics.com/hc/en-us/articles/4406817001495-Analysis-Grid-Showing-Hiding-and-Moving-Columns#Columns)
* [Sorting Rows](https://devnet.logianalytics.com/hc/en-us/articles/4406817002519-Analysis-Grid-Sorting-Rows#Sorting)
* [Grouping Rows](https://devnet.logianalytics.com/hc/en-us/articles/4406816998167-Analysis-Grid-Grouping-Rows#Grouping)
* [Creating Aggregations](https://devnet.logianalytics.com/hc/en-us/articles/4406822098199-Analysis-Grid-Creating-Aggregations#Aggregating)
* [Creating Custom Aggregations](https://devnet.logianalytics.com/hc/en-us/articles/4406816995479-Analysis-Grid-Creating-Custom-Aggregations)
* [Controlling Paging](https://devnet.logianalytics.com/hc/en-us/articles/4406816993303-Analysis-Grid-Controlling-Paging#Paging)
* [Formatting Data](https://devnet.logianalytics.com/hc/en-us/articles/4406816997143-Analysis-Grid-Formatting-Data#Formatting)
* [Creating Charts and Gauges](https://devnet.logianalytics.com/hc/en-us/articles/4406822099095-Analysis-Grid-Creating-Charts-and-Gauges#Gauges)
* [Pivoting and Summarizing Data](https://devnet.logianalytics.com/hc/en-us/articles/4406816999191-Analysis-Grid-Pivoting-and-Summarizing-Data#Summarizing)
* [Exporting Data](https://devnet.logianalytics.com/hc/en-us/articles/4406822100247-Analysis-Grid-Exporting-Data#Exporting)
* [Adding Analysis Grid Charts to Dashboards](https://devnet.logianalytics.com/hc/en-us/articles/4406816991127-Analysis-Grid-Adding-Analysis-Grid-Charts-to-Dashboards#Dashboards)

Information for *developers* is available in [The Analysis Grid for Developers](https://devnet.logianalytics.com/hc/en-us/articles/4406816977175-The-Analysis-Grid-for-Developers).

## About the Analysis Grid

The Analysis Grid user interface consists of separate panels for controls, tables, and visualizations. At runtime, you can manipulate the controls, creating data analyses and visualizations on the fly.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584186775/usingag_01.png)

In the example Analysis Grid shown above, both a table and a chart are displayed.

![](https://devnet.logianalytics.com/hc/article_attachments/4417591973015/usingag_02.png)

As you can see in the examples above, the Analysis Grid can look quite different depending on the Theme being used. The examples in this topic use the **Signal** Theme.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584187031/usingag_03.png)

The Analysis Grid consists of a set of panels. The **Controls Panel**, at the top, includes a set of tabs or buttons that allow you to manipulate the data and visualizations at runtime. The visibility of specific controls is configured by the application developer and so you may or may not see the full set shown here.

When a tab or button is clicked, a configuration panel for that feature appears, as shown above. Clicking it again hides the panel.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584187415/usingag_04.png)

**Visualization Panels** contain either a data table, crosstab table, or chart. Panels can be collapsed or expanded using the "+" and "-" icons. You can also rearrange their order by clicking with your mouse near the top of a panel, and dragging it up or down.

Panels containing tables may display an icon for exporting them to Excel, CSV, or PDF. The availability of the different types of exports is under developer control, so those available to you may vary.

![](https://devnet.logianalytics.com/hc/article_attachments/4417591973655/usingag_04a_397x293.png)

Clicking a panel's gear icon will display a configuration area for the
specific visualization. The Table configuration area, shown above, let's
users control a variety of table features.

![](https://devnet.logianalytics.com/hc/article_attachments/4417591973911/usingag_04b.png)

Table column *headers* contain a variety of features. They can be *dragged*
to rearrange the column order or to adjust column widths. When column
header text is clicked, drop-down menus provide sorting, filter,
formatting, grouping, and other features, as shown above. The
availability of each feature can be restricted during development.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584188311/usingag_04c.png)

If your application has been configured for it, you'll see Undo and Redo icons, circled
above, beside Add Crosstab. These allow you to undo and redo your recent
actions.

Now, let's get started using the Analysis Grid.
