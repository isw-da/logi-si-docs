---
title: "Series.Pie - Using the Chart Drill to Element"
id: 4419722709143
section: "Chart Canvas Chart Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722709143-Series-Pie-Using-the-Chart-Drill-to-Element
updated_at: 2022-07-17T02:25:08Z
---

# Series.Pie - Using the Chart Drill to Element

# Series.Pie - Using the Chart Drill to Element

The **Chart Drill To** element, a child of the Series element, enhances charts by allowing users to examine the data "behind" the chart.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) The parent Chart Canvas element must have an ID attribute value in order to use the Chart Drill To element with it.

When the Drill To element is enabled, selecting a pie wedge displays a list of columns, as shown below:

![](https://devnet.logianalytics.com/hc/article_attachments/7522818175127/series_pie_15.png)

Selecting a column re-draws the chart so that only the data representing the clicked wedge is shown.

Select **Drill Back** to return the chart to it's previous state:

![](https://devnet.logianalytics.com/hc/article_attachments/7522832927255/series_pie_16.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Chart Canvas Charts that use the Chart Drill To element can only have a single Series.
The Drill Back button only appears when the mouse cursor is hovered over the upper right-hand corner of the chart.

Or, continue drilling further down into the data (assuming the elements are configured for it) by selecting a wedge again.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.2 If your chart has been configured for it, as you drill further into the data, a breadcrumb trail becomes available. The breadcrumb trail can be used to access previously drilled levels, or clear the Drill To data altogether. To enable this feature, set the **Show DrillTo Breadcrumb** attribute to *True*.

As shown below, the Chart Drill To element drills into *grouped* data, so the datalayer used beneath the Chart Canvas Chart or Series element *must* be grouped using a **Group Filter** or **Sql Group** element. The example datalayer has been grouped on the *CategoryName* column and the Keep Grouped Rows attribute was set to *False*. The Series itself has been configured so that its Label Data Column = *CategoryName* and its Y-axis Data Column = *gacProductSales* (the Group Aggregate Column that sums the ProductSales values).

![](https://devnet.logianalytics.com/hc/article_attachments/7522855042839/series_pie_16a.png)

Next, a **Chart Drill To** element was added beneath the Series element, shown below. Required child **Drill To Column** elements have also been added; they define the columns the user can select to drill into. They should be added and configured for columns that can be reasonably grouped, such as text-type columns with a limited number of unique values and date-type columns.

![](https://devnet.logianalytics.com/hc/article_attachments/7522855067927/series_pie_17.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) You *must* also configure a Drill To Column element for the column that's specified as the chart's Label Data Column, in this example the *CategoryName* column.

The **Column Header** attribute specifies the text that will appear in the Drill to Column drop-down list options. The vertical order of the drop-down list options will match the vertical order of the Drill To Column elements in the definition. Year, Quarter, and Month options will be added automatically for Drill To Columns with Data Type = *Date*. You do not need to add any filter or additional grouping elements to achieve the results shown
in the example above.

The Drill Back button displayed on the chart after drilling has occurred can be styled using the **Drill Back Button Style** element.
