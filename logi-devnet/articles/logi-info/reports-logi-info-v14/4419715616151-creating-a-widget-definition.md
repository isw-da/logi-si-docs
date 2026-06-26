---
title: "Creating a Widget Definition"
id: 4419715616151
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715616151-Creating-a-Widget-Definition
updated_at: 2022-07-17T01:28:29Z
---

# Creating a Widget Definition

# Creating a Widget Definition

A widget definition is simply a different **category** of Logi report definition. In Logi Studio, these definitions appear in the **Application** panel in the Widgets folder.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707205527/workwidgets_01.png)

To create a new widget, right-click the **Widgets** folder and add a new definition. The new file, with an .lgx extension, will be created in the file system in this folder (the folder is not created until you add your first widget to the application):

*<LogiApplicationFolder>*\\_Definitions\\_Widgets

The widget definition can now be opened and edited in the **Workspace** panel, just like any report definition.

![](https://devnet.logianalytics.com/hc/article_attachments/4419700015255/workwidgets_02.png)

In the example above, a line chart that gets its data from an XML data file has been added to the widget.
While there are some elements that are [excluded](#Limitations) from use in a widget, generally most **elements** can be used. Widgets can be fully dynamic and support drill-downs, drill-through's, and links to other pages or applications. Sorting and paging of tables is also supported. Some of the limitations in widgets themselves can be overcome by providing a **link** in the widget to a **Logi application** page that provides the desired functionality.
