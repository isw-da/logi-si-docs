---
title: "Using the Radial Menu"
id: 4402537934359
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537934359-Using-the-Radial-Menu
updated_at: 2021-09-15T02:23:04Z
---

# Using the Radial Menu

# Using the Radial Menu

Use the radial menu to explore certain elements of dashboard in greater detail. It allows you to explore and interact with specific data elements.

![](https://devnet.logianalytics.com/hc/article_attachments/4406753437463/noteicon.jpg) The radial menu is not available on arc gauges, histograms, KPI charts, maps, or raw data tables.

To access the radial menu, select a data point in the visual.
In the following example of a Real Time Sales bar chart, select one of the vertical bars to display the menu. It is available for each bar in the visual, that is, for each individual data element, and provides the capability to explore or drill into one specific bar of data.

![](https://devnet.logianalytics.com/hc/article_attachments/4406753444631/radial-menu_576x232.png)

You can rotate the options on the radial menu clockwise (right) and counterclockwise (left) by holding down the shift key and using the left and right arrows on your keyboard.

Controls for these options are provided using the interactivity sidebar. See [*Controlling How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4402537944215-Controlling-How-Users-Interact-With-a-Visual).

The following options are available on the radial menu:

* [*Zoom Option*](#Zoom)
* [*Filter Option*](#Filter)
* [*Link Option*](#Link)
* [*Details Option*](#Details)
* [*Trend Option*](#Trend)
* [*Keyset Option*](#Keyset)
* [*Actions Option*](#Actions)
* [*Remove Option*](#Remove)

## Zoom Option

The **Zoom** menu option allows you to zoom into the selected data point and filter the data for that data point by another filter attribute in the data source. When you select **Zoom**, a menu appears from which you select the second filter attribute.

For example, if you wanted to see the real time sales for every city in Texas, you would select Texas in the bar chart to bring up the radial menu, select **Zoom**, and then select the City attribute from the resulting menu. The result set in the bar chart might look like this:

![](https://devnet.logianalytics.com/hc/article_attachments/4406763914903/radial-zoom_576x249.png)

## Filter Option

The Filter menu option allows you to filter any other visuals in the dashboard that use the same data source by the data point you have selected. For more information, see [*Applying a Filter to Dashboard Visuals Using the Radial Menu*](https://devnet.logianalytics.com/hc/en-us/articles/4402552812823-Applying-a-Filter-to-Dashboard-Visuals-Using-the-Radial-Menu).

## Link Option

The Link menu option allows you to quickly access a dashboard that has been linked to this visual. This option only appears if a dashboard link has been defined for a visual. See [*Linking a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402537754263-Linking-a-Dashboard).

## Details Option

To display additional information about specific data elements, select **Details**. The details for the element are displayed in a raw data table.

![](https://devnet.logianalytics.com/hc/article_attachments/4406763915159/radial-details_576x269.png)

The table header contains the following:

1. Attribute whose details you have selected to view
2. Metric
3. Time attribute and the selected time interval on the time bar
4. Volume metric

Select **Export Raw Data** to export your data set to a CSV file. If the Raw Data Table visual style is enabled for your data source, you can select
**Open in Raw Data Table** to view your information.

You can also view the information in a pop-out window over your visual. Select the collapse icon to minimize the window.

## Trend Option

The
**Trend** menu option lets you view a trends for a selected data point.
The
**Trend** menu option is not available for the following visual styles: Line and Bars Trend, Line Trend: Attribute Values, and Line Trend: Multiple Metrics.

## Keyset Option

The Keyset menu option lets you create a keyset from the selected data point. See [*Creating a Keyset*](https://devnet.logianalytics.com/hc/en-us/articles/4402537823639-Creating-a-Keyset).

## Actions Option

The Actions menu option allows you to invoke an action. If this menu option does not appear on the radial menu, an action template is either not defined or is not enabled for the data source used by the visual.

The invoked action:

* Creates a query definition based on the filters applied to the visual and on the data and limit specifications in the associated action template.
* Sends the query definition to your application. Your application can use the Composer API to run the query and display or use the data that it collects.

![](https://devnet.logianalytics.com/hc/article_attachments/4406753437463/noteicon.jpg) You must be logged in as an administrator or as a user with the **Can Invoke Actions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402537668503-Group-Privilege-Reference)

To invoke an action, see [*Invoking an Action*](https://devnet.logianalytics.com/hc/en-us/articles/4402537677207-Invoking-an-Action).

## Remove Option

The
**Remove** menu option lets you exclude the selected data element from your visual.
