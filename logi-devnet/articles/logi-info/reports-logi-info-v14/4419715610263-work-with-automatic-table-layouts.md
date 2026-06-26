---
title: "Work with Automatic Table Layouts"
id: 4419715610263
section: "Reports - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715610263-Work-with-Automatic-Table-Layouts
updated_at: 2022-07-17T01:28:41Z
---

# Work with Automatic Table Layouts

# Work with Automatic Table Layouts

In general, HTML table layout is concerned with size, alignment, and spanning. The layout type is configured by setting the Rows element's **Layout** attribute to *Auto (*the default) or *Fixed.*

Automatic table layouts rely on the web browser's ability to automatically calculate the column widths required to fit its contents, while fixed
layouts restrict column widths to the values you specify.

There's even a hybrid mode: when using automatic layouts you can specify the size of *some* columns and let the browser figure out the rest. Column widths, when specified, can be an exact number of pixels or percentages of the overall table width.

![](https://devnet.logianalytics.com/hc/article_attachments/4419700013591/worktable_05.png)

In the example above, the parent table's width is set to 30% of the total browser window's width. If the **Width** attribute value is too small, the browser will automatically calculate the amount of space needed to display the table's contents on a single line.

![](https://devnet.logianalytics.com/hc/article_attachments/4419700013847/worktable_05a.png)

The element arrangement used to create the previous example is shown above.

In general, the three elements used with tables, **Rows**, **Row**, and **Column Cell**, are all "container" elements and all have a **Class** attribute that allows you to apply style classes to them (and to the elements they contain). This can very useful when formatting content. For example, a table column can have style applied to it that centers everything within the column, sets a default font size, or creates padding that provides a small area of white space between the edges of
the column and its content.

Table alignment is controlled by style sheet classes when automatic layouts are used. You can use the *text-align* and *vertical-align* style attributes to align table contents. Define a *class* selector or *ID* selector class to align a specific table. Logi reporting products support CSS and you're encouraged to use
style classes to control the layout and appearance of report content when it makes sense to do so.

TABLE {  
 vertical-align: middle;  
 text-align: center;  
}  
  
TR {  
 vertical-align: middle;  
 text-align: center;  
}  
  
TD {  
 vertical-align: middle;  
 text-align: center;  
}

When using element selector classes, you can define a class for any of the three HTML tags that comprise a table, as shown above.
You can control overall table height by defining the *height* property in a style class.
