---
title: "The Analysis Chart"
id: 4406816963863
section: "Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816963863-The-Analysis-Chart
updated_at: 2022-04-06T06:03:06Z
---

# The Analysis Chart

# The Analysis Chart

The Analysis Chart is a dynamic chart set that provides interactive data analysis capabilities.

The following topics introduce developers to the **Analysis Chart** super-element:

* [Analysis Chart Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4406816961431-Analysis-Chart-Attributes#Attributes)
* [Adding Analysis Chart Columns](https://devnet.logianalytics.com/hc/en-us/articles/4406816958231-Analysis-Chart-Add-Analysis-Chart-Columns#AddColumns)
* [Adding a Second Series](https://devnet.logianalytics.com/hc/en-us/articles/4406822081559-Analysis-Chart-Adding-a-Second-Series#Series)
* [Adding Forecasting](https://devnet.logianalytics.com/hc/en-us/articles/4406816960279-Analysis-Chart-Adding-Forecasting#Forecasting)
* [Saving Individual User Settings](https://devnet.logianalytics.com/hc/en-us/articles/4406816962839-Analysis-Chart-Saving-Individual-User-Settings#Settings)
* [Adding Charts to Dashboards](https://devnet.logianalytics.com/hc/en-us/articles/4406816959255-Analysis-Chart-Adding-Charts-to-Dashboards#Dashboards)
* [Customizing Analysis Chart Appearance](https://devnet.logianalytics.com/hc/en-us/articles/4406822082967-Analysis-Chart-Customizing-Analysis-Chart-Appearance#Customizing)

## About the Analysis Chart

The Analysis Chart allow users to display charts at runtime, based on a discrete data set and limited to chart types the developer chooses to include.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Chart Canvas charts are used by default by the Analysis Chart, in all *new applications*. Older Logi applications that are *upgraded* to v12 will use the classic static charts for their Analysis Charts. To force upgraded apps to use Chart Canvas charts, add the constant rdFavorChartCanvas
= *True*
to your \_Settings definition.

Like data tables, the Analysis Chart uses child column elements to include data for display.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584203799/workac_01.png)

The example above shows a typical set of Analysis Chart elements:

* An **Analysis Chart** element
* A **DataLayer** element to retrieve the data
* One or more **Analysis Chart Column** elements to make data available for analysis

Analysis Chart Column elements do not require any child elements, such as a Label element, in order to make data visible. The element's **Data Type** attribute determines how each column can be used. "Text"-type columns can be used as Label Columns for Pie and Bar charts. "Number"-type columns may be used in the X- and Y-axis of Line and Scatter charts. "Date" columns may be used in the X-axis. In addition, the **Format** attribute can be used to format the values
that appear in tooltips displayed when the cursor is hovered over various chart areas.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584204055/workac_02.png)

As shown above, the display produced by this element consists of a **Control Panel** and a **Chart Area**. By default, the Control Panel will appear *above* the Chart Area, as shown. However, the Analysis Chart can be configured to display the Control Panel to the *left* of the Chart Area instead.

The chart's **title** changes dynamically based on the selections the user makes at runtime; it cannot be set independently by the developer.

**Resizing handles**, which are only visible when the mouse hovers over the chart, are also provided so that the user can resize the chart at runtime.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575917591/workac_03.png)

Chart type options, shown above, allow the user to select different chart types at runtime. The types available to the user can be restricted by the developer when configuring the element and will also be limited based on the nature of the data. For example, Pie and Bar chart types are only available when there is at least one Analysis Chart Column with its **Data Type** attribute set to *Text*.

The default orientation of bar charts that are not based on a time series is *Horizontal*, to make it easier to read X-axis label data values. This can be changed at runtime by the user to Vertical.

A built-in **Group Filter** is available for X-axis (Label) values:

[![](https://devnet.logianalytics.com/hc/article_attachments/4417591986199/new_date_options.png)](../../../../../Users/Mshaffer/OneDrive%20-%20Logi%20Analytics,%20Inc/Desktop/new%20date%20options.png)

![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png) For example, if a DateTime type column is selected, the filter appears in the control panel automatically, as shown above. It allows users to group data by Year, Quarter, Month, Week, Day Hour, Minute time periods.

**Quicktips** are automatically included:

![](https://devnet.logianalytics.com/hc/article_attachments/4417591986455/workac_03b.png)

As shown above, this feature displays a pop-up "balloon", containing detail data, when the mouse is hovered over a data point. This feature is available for *all* chart types and no action on the developer's part is required to enable it.

If you're working with **very large data sets**, you may be able to use a special-purpose datalayer for better performance. You can find out more about it and review the restrictions in [DataLayer.ActiveSQL](https://devnet.logianalytics.com/hc/en-us/articles/4406817277847-DataLayer-ActiveSQL).

This datalayer provides the basic SQL query needed to retrieve data but doesn't initially retrieve and cache
*all* of the result set. Instead, in response to runtime
manipulations of the Analysis Chart interface, it dynamically modifies
its own SQL query and retrieves the minimum required amount of data with
each request. This increases the number and frequency of SQL queries
the database server must handle (and, generally, does not prove to be a
burden on the database server) but improves performance for the user.

A **Zero Rows Message** element is available as a child element of the Analysis Chart. This element allows developers to display a customized message if the datasource returns no data. The message text and its font type, size, and color can be set using the element's attributes.

## Studio Wizard Available

Logi Studio includes a wizard that will help you to build and configure an Analysis Chart:

![](https://devnet.logianalytics.com/hc/article_attachments/4417584204823/workac_03c.png)

As shown above, you can launch the wizard from Studio's main menu Wizards tab, or by right-clicking a container element and using its context menus. The wizard will walk you through decisions about connecting to and retrieving data, and about which data columns to use, and will then insert the configured elements into your definition.

## Retaining User Settings

With all these possibilities, it may be important for users to be able to **save** their **settings** between sessions. Settings can be automatically saved on the web server and made available to users during their next session (this is discussed in more detail below).

## Embedded Sub-Report Caveat

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) We *do not* recommend that you use this element within an embedded sub-report.
