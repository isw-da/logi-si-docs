---
title: "Series.Pie - Using the Chart Drill to Element"
id: 4406817098775
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817098775-Series-Pie-Using-the-Chart-Drill-to-Element
updated_at: 2022-04-06T06:04:02Z
---

# Series.Pie - Using the Chart Drill to Element

# Series.Pie - Using the Chart Drill to Element

The **Chart Drill To** element, a child of the Series element, enhances charts by allowing users to examine the data "behind" the chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) The parent Chart Canvas element must have an ID attribute value in order to use the Chart Drill To element with it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563513495/series_pie_15.png)

As shown above, when this element is being used, clicking a pie wedge displays a list of columns. Selecting a column re-draws the chart so that only the data representing the clicked wedge is shown:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563513751/series_pie_16.png)

After drilling to a column, the user can click a button to "drill back", as shown above. It's also possible to continue drilling further down into the data (assuming the elements are configured for it) by clicking a wedge again.

Chart Canvas Charts that use the Chart Drill To element can only have a single Series.

The Drill Back button only appears when the mouse cursor is hovered over the upper right-hand corner of the chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584136215/series_pie_16a.png)

As shown above, the Chart Drill To element drills into *grouped* data, so the datalayer used beneath the Chart Canvas Chart or Series element *must* be grouped using a **Group Filter** or **Sql Group** element. The example datalayer has been grouped on the *CategoryName* column and Keep Grouped Rows = *False*.

The Series itself has been configured so that its Label Data Column = *CategoryName* and its Y-axis Data Column = *gacProductSales* (the Group Aggregate Column that sums the ProductSales values).

![](https://devnet.logianalytics.com/hc/article_attachments/4417563514391/series_pie_17.png)

Next, a **Chart Drill To** element has been added beneath the Series element, as shown above. Required child **Drill To Column** elements have also been added; they define the columns the user can select to drill into. They should be added and configured for columns that can be reasonably grouped, such as text-type columns with a limited number of unique values and date-type columns.

You *must* also configure a Drill To Column element for the column that's specified as the chart's Label Data Column, in this example the *CategoryName* column.

The **Column Header** attribute specifies the text that will appear in the Drill to Column drop-down list options. The vertical order of the drop-down list options will match the vertical order of the Drill To Column elements in the definition. Year, Quarter, and Month options will be added automatically for Drill To Columns with Data Type = *Date*. You do not need to add any filter or additional grouping elements to achieve the results shown
in the example above.

The Drill Back button displayed on the chart after drilling has occurred can be styled using the **Drill Back Button Style** element.
