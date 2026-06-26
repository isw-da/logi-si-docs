---
title: "Series.Bar - Using the Chart Drill to Element"
id: 4406817055639
section: "Chart Canvas Chart Elements - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817055639-Series-Bar-Using-the-Chart-Drill-to-Element
updated_at: 2022-04-06T06:03:35Z
---

# Series.Bar - Using the Chart Drill to Element

# Series.Bar - Using the Chart Drill to Element

The **Chart Drill To** element, a child of the Series element, enhances charts by allowing users to examine the data "behind" the chart.
![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) The parent Chart Canvas element must have an ID attribute value in order to use the Chart Drill To element with it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575891991/series_bar_13.png)

As shown above, when this element is being used, clicking a chart bar displays a list of columns. Selecting a column re-draws the chart so that only the data representing the clicked bar is shown, and the X-axis is changed to the selected Drill To column:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563534743/series_bar_14.png)

After drilling to a column, the user can click a button to "drill back", as shown above. It's also possible to continue drilling further down into the data (assuming the elements are configured for it). For example, we could click on the Munchen chart bar next and then select Customer ID to drill down to the customers in that city.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Chart Canvas Charts that use the Chart Drill To element can only have a single Series.
The Drill Back button only appears when the mouse cursor is hovered over the upper right-hand corner of the chart.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584150935/series_bar_14a.png)

As shown above, the Chart Drill To element drills into *grouped* data, so the datalayer used beneath the Chart Canvas Chart or Series element *must* be grouped using a **Group Filter** or **Sql Group** element. The example datalayer has been grouped on the *ShipCountry* column and Keep Grouped Rows = *False*.
The Series itself has been configured so that its X-axis Data Column = *ShipCountry* and its Y-axis Data Column = *gacFreight* (the Group Aggregate Column that sums the Freight values).

![](https://devnet.logianalytics.com/hc/article_attachments/4417563535127/series_bar_15.png)

Next, a **Chart Drill To** element has been added beneath the Series element, as shown above. Required child **Drill To Column** elements have also been added; they define the columns the user can select to drill into. They should be added and configured for columns that can be reasonably grouped, such as text-type columns with a limited number of unique values and date-type columns.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) You *must* also configure a Drill To Column element for the column that's specified as the chart's X-axis Data Column, in this example the *ShipCountry* column.

The **Column Header** attribute specifies the text that will appear in the Drill to Column drop-down list options and will become the drilled chart's X-axis caption. The vertical order of the drop-down list options will match the vertical order of the Drill To Column elements in the definition. Year, Quarter, and Month options will be added automatically for Drill To Columns with Data Type = *Date*. You do not need to add any filter or additional grouping elements to achieve the results shown
in the example above.

The Drill Back button displayed on the chart after drilling has occurred can be styled using the **Drill Back Button Style** element.
