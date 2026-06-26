---
title: "Report Designer/Chart"
id: 4415504845847
section: "User Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504845847-Report-Designer-Chart
updated_at: 2021-12-10T03:10:33Z
---

# Report Designer/Chart

# Report Designer/Chart

Chart is a built-in type of report part that displays data using
graphical symbols, such as bars in a bar chart, lines in a line chart,
or slices in a pie chart.

## Configure Report Part Properties for Chart

1. Select the chart in Report Body (See [Manage Report Parts](https://devnet.logianalytics.com/hc/en-us/articles/4415492934039-Report-Designer-Design#manage-report-parts) for how to
   add a chart).
2. Click the expand icon (<) on the right to open the Properties boxes
   if needed.
3. Select the vertical Report Part Properties box.
4. The properties are listed in Report Part Properties box in 7
   sections.

   * General Info
   * Chart
   * Labels
   * Legends
   * Grouping
   * Data
   * View

![../_images/Chart_Line_Properties.png](https://devnet.logianalytics.com/hc/article_attachments/4415504435479/chart_line_properties_245x343.png)

User can configure the properties and see changes reflected in
Preview pane:

* Select a type in Chart Type drop-down. (See below for each type)
* Configure border settings:

  1. In Chart group, click the gear icon (⚙) to open Border Settings
     pop-up.
  2. Choose the border to be visible or not.
  3. Select a border color.
  4. Select the border thickness (in pixels).
  5. Click OK to close the Border Settings pop-up.

     [![../_images/NW_Orders_Chart_Border_Settings.png](https://devnet.logianalytics.com/hc/article_attachments/4415492526487/nw_orders_chart_border_settings_650x397.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492525975/nw_orders_chart_border_settings.png)
* Set the background color.

  1. In Chart group, click the gear icon (⚙) to open Chart Background
     Color Settings pop-up.
  2. Select a background color.
  3. Choose to apply the color to the entire chart (the area inside the
     border above) or to the plot area only (on the right).
  4. Click OK to close the Chart Background Color Settings pop-up.

     [![../_images/NW_Orders_Chart_Background_Color_Settings.png](https://devnet.logianalytics.com/hc/article_attachments/4415492528407/nw_orders_chart_background_color_settings_455x405.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492527511/nw_orders_chart_background_color_settings.png)
* Configure the X-axis
  and Y-axis (applicable to the chart types Line, Column, Bar, Area,
  and Combination only).

  1. Customize the title (“Month” instead of “Group (OrderDate)” and
     “Freight” instead of “Sum(Freight)”).
  2. Set the title font face and font size.
  3. Choose title text effects bold, italic and underlined.
  4. Choose title text color and background color.
  5. Choose title text alignment.
  6. Customize the starting value for the chart. In the sample
     screenshot, “3000” is entered into the Starting Point box of
     Y-axis, so only the points having Sum(Freight) value greater than
     or equal to 3000 are displayed.
  7. Customize the relative distance between the tick marks. In the
     sample screenshot, “10000” is entered into the Intervals box of
     Y-axis, so there will be exactly one tick mark after every 1000
     units on Y-axis (4000.00, 5000.00, 6000.00, 7000.00, etc).

     [![../_images/NW_Orders_Chart_XY-Plane_Settings.png](https://devnet.logianalytics.com/hc/article_attachments/4415504437399/nw_orders_chart_xy-plane_settings_600x540.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504436887/nw_orders_chart_xy-plane_settings.png)
* Configure the grid lines.

  1. Choose the grid lines to be visible or not.
  2. Select a line color.
  3. Select a line pattern: Solid (default), Dot or Dash.
  4. Select the line thickness (in pixels).

     [![../_images/NW_Orders_Chart_Grid_Lines_Settings.png](https://devnet.logianalytics.com/hc/article_attachments/4415511790615/nw_orders_chart_grid_lines_settings_680x569.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504437655/nw_orders_chart_grid_lines_settings.png)
* Configure color theme. This option is available from version 2.9.0.

  1. In Chart group, click the gear icon (⚙) next to the Color Theme option to open Color Theme Selection pop-up.
  2. Select a color theme and click OK to the pop-up.

     **Note:** When the System Admin changes the [Default Color Setting](https://devnet.logianalytics.com/hc/en-us/articles/4415492925079-System-Configuration-Report#set-default-color-theme), all report parts using the default color theme will change to use the new default theme.

     [![../_images/Color_Theme_Selection.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415492531479/color_theme_selection_680x503.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511790871/color_theme_selection.png)
* Configure multiple colors. This option is available from version 2.9.0.

  1. In Chart group, select Multi-Color check box.
  2. Then the chart will receive one color per point.

     **Note:**

     - Multi-Color option is only available for single metric charts. When using multiple metrics each metric is a different color.   
     - Sparkline chart type does not support Multi-Color option.   
     - Multi-Color option is available for Bubble and Scatter from version 2.10.0.

  ![../_images/Multi-Color-CountOrder-Country.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415504437911/multi-color-countorder-country.png)
* Configure the text direction for
  the labels.

  [![../_images/NW_Orders_Chart_Labels_Settings.png](https://devnet.logianalytics.com/hc/article_attachments/4415492532503/nw_orders_chart_labels_settings_635x210.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504438167/nw_orders_chart_labels_settings.png)
* Configure the legends.

  [![../_images/Report_Chart_Legend_Settings.png](https://devnet.logianalytics.com/hc/article_attachments/4415504439063/report_chart_legend_settings_684x426.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511791383/report_chart_legend_settings.png)
* Select to use Separator.

  > The Separator option displays multiple charts according to each
  > unique value of the field(s) defined in Separators box. For
  > example: this report with multiple pies, each one for each
  > country in Northwind Orders table.
  >
  > > [![../_images/NW_Orders_Pie_Separators_ShipCountry_Group_by_ShipRegion_ShipCity.png](https://devnet.logianalytics.com/hc/article_attachments/4415504440343/nw_orders_pie_separators_shipcountry_group_by_shipregion_shipcity_950x230.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492533143/nw_orders_pie_separators_shipcountry_group_by_shipregion_shipcity.png)

  1. Tick Use Separator check-box in Grouping in Report Part Properties
     to see Separators box inside the chart configuration.
  2. Add [ShipRegion] and [ShipCity] to Labels (X-axis) box, they will
     show up as Group(ShipRegion) and Group(ShipCity).
  3. Add [OrderID] to Values (Y-axis) box, then choose Count as the
     Function, it should show up as Count(OrderID).
  4. Add [ShipCountry] to Separators box, it will show up as
     Group(ShipCountry).
  5. Bottom X% Grouped to Other is used to set the threshold where
     percentage values lower than that will be grouped together into
     Others group. See examples below:

     > Before: ![Report Chart Pie Bottom X Before.png](https://devnet.logianalytics.com/hc/article_attachments/4415504440855/report_chart_pie_bottom_x_before.png) and After
     > setting 60%: ![Report Chart Pie Bottom X After.png](https://devnet.logianalytics.com/hc/article_attachments/4415511793943/report_chart_pie_bottom_x_after.png)
* Choose to display values of
  data points or not.

  [![../_images/NW_Orders_Chart_Data_Show_Value_Labels.png](https://devnet.logianalytics.com/hc/article_attachments/4415511794455/nw_orders_chart_data_show_value_labels_635x138.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511794199/nw_orders_chart_data_show_value_labels.png)
* Add threshold lines to the chart.

  1. In Data group, click the gear icon (⚙) to open Thresholds Settings pop-up.
  2. In Y-axis, click Add Setting.
  3. Specify the threshold type: Static or Dynamic. Dynamic thresholds option is available from version 2.11.0.
  4. Specify the Field that the threshold belongs to.
  5. Input Label for the threshold. The text format for the static threshold’s label can be customized by clicking the gear icon (⚙)
  6. Input a value for static threshold or add a field then choose a function for
  7. For Static threshold, input a number in Value text box. For Dynamic threshold click “Add a field” then choose a field with its function and specify the format to draw threshold line.
  8. Configure Dashstyle, Color and Thickness.
  9. Remember to tick the Visible text box.
  10. Click OK to close the Thresholds Settings pop-up.

  [![../_images/NW_Orders_Chart_Data_Thresholds_Settings.png](https://devnet.logianalytics.com/hc/article_attachments/4415511795351/nw_orders_chart_data_thresholds_settings_845x425.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511794839/nw_orders_chart_data_thresholds_settings.png)
* Add regression line (applicable to the chart types Line, Column, Bar, Area, Combination, Scatter, and Bubble only). New in 2.12.0.

  1. In Data group, click the gear icon (⚙) to open Regression Line Settings pop-up.
  2. Select a field to apply the regression line.
  3. Specify whether to display this regression line in the chart plot area or not.
  4. Specify whether to hide this regression line in the chart legend or not.
  5. Input the name for the regression line. If the name is not defined, the equation will display as the regression line’s name. This name is only shown in the tool tip and the legend, it is not displayed in the chart on the line.
  6. Select one of the types from Linear, Polynomial, Logarithmic, or Exponential in Regression Type drop-down.
  7. Input the decimal places for the regression line.
  8. Choose the Order number if the regression line is Polynomial.
  9. Configure the color, dashstyle, and thickness.
  10. Input the extrapolate number if the regression type is Linear or Polynomial.
  11. Click OK to close the Regression Line Settings pop-up.

  [![../_images/Report_Chart_Regression_Line_Setting.png](https://devnet.logianalytics.com/hc/article_attachments/4415492535319/report_chart_regression_line_setting_805x479.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492535063/report_chart_regression_line_setting.png)

  [![../_images/Report_Chart_Regression_Line_Setting_Linear.png](https://devnet.logianalytics.com/hc/article_attachments/4415504444823/report_chart_regression_line_setting_linear_805x444.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492535959/report_chart_regression_line_setting_linear.png)

  [![../_images/Report_Chart_Regression_Line_Setting_Logarithmic.png](https://devnet.logianalytics.com/hc/article_attachments/4415511797527/report_chart_regression_line_setting_logarithmic_805x419.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511797143/report_chart_regression_line_setting_logarithmic.png)

  [![../_images/Report_Chart_Regression_Line_Setting_Exponential.png](https://devnet.logianalytics.com/hc/article_attachments/4415492537495/report_chart_regression_line_setting_exponential_805x417.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492537239/report_chart_regression_line_setting_exponential.png)

  Zoom into a region of the chart.

  ![../_images/NW_Orders_Chart_Zoom.png](https://devnet.logianalytics.com/hc/article_attachments/4415492539927/nw_orders_chart_zoom_330x115.png)

  1. In View group, select the axis to be magnified:
     + XY: both axis will be magnified.
     + X: X-axis will be magnified while Y-axis remains fixed.
     + Y: Y-axis will be magnified while X-axis remains fixed.
  2. Hold the mouse button and drag over a region, then release the
     mouse button to actually zoom into that region.
  3. Repeat to zoom closer.
  4. Click the Reset zoom button to restore the chart to normal.
* Invert the X-axis and Y-axis by ticking the Inverted check-box in
  View group.
* Choose a step chart style.

  [![../_images/NW_Orders_Chart_View_Center_Step.png](https://devnet.logianalytics.com/hc/article_attachments/4415511798935/nw_orders_chart_view_center_step_633x176.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492540183/nw_orders_chart_view_center_step.png)
* Choose a spline chart style.

  [![../_images/NW_Orders_Chart_View_Spline.png](https://devnet.logianalytics.com/hc/article_attachments/4415492541079/nw_orders_chart_view_spline_633x193.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492540823/nw_orders_chart_view_spline.png)
* Configure how
  often data is refreshed when report is being viewed.

  ![../_images/Report_Designer_Data_Refresh_Interval.png](https://devnet.logianalytics.com/hc/article_attachments/4415504448919/report_designer_data_refresh_interval_455x259.png)

  1. Click the gear icon (⚙) to open Data Refresh Interval Settings
     pop-up.
  2. Choose to have data refreshed automatically or manually.
  3. Enter an interval between each refresh (in seconds).
  4. Choose to view all data or enter a number to view that specific
     number of latest records only.

Choose Single Y-axis to show all metrics in one Y-axis. This option is only available for combination charts that contain at least two metrics. New in version 2.12.0.   
When Single Y-axis is selected, the All axis will be applied and the same format with the first metric’s axis.   
The metrics in the combination chart are stacked in the order they are added in the configuration, the first metric added is the on the bottom and the last metric added is on the top. In the example image above, the area chart metric is on top and is the last metric in the chart set up.

![../_images/Report_Chart_Single_Yaxis.png](https://devnet.logianalytics.com/hc/article_attachments/4415504449175/report_chart_single_yaxis_588x353.png)

Note: If the **Show Preview section in Configuration Mode** check box (In Others tab in Advanced Settings) is unticked then The Preview section will not be displayed for following pop-ups:

> - Chart Border Settings   
> - Chart Background Color Settings   
> - XY-Plane Settings   
> - Grid Lines Settings   
> - Legend Settings   
> - Thresholds Settings   
> - Regression Line Settings
>
> [![../_images/NW_Orders_Chart_Border_Settings_No_Preview.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415504449687/nw_orders_chart_border_settings_no_preview_464x295.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504449431/nw_orders_chart_border_settings_no_preview.png)

Please see [Update Others Settings](https://devnet.logianalytics.com/hc/en-us/articles/4415504834839-Advanced-Settings#advanced-settings-others) for more details.

## Line Chart

A line chart displays data as a series of data points ordered by value
and connected by lines. Therefore the line chart is used to visualize a
trend in data over intervals of time.

[![../_images/NW_Orders_Line_Chart_Freight_by_Month.png](https://devnet.logianalytics.com/hc/article_attachments/4415492541847/nw_orders_line_chart_freight_by_month_342x126.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504449943/nw_orders_line_chart_freight_by_month.png)

For example, table Orders in
Northwind database stores the OrderDate together with the Freight cost
of each order. From that data, a report such as the trend of total
Freight cost over each month would be best visualized using a line
chart.

1. “Each month” means using “Month” format for OrderDate field to get
   the month numeric value, then using the Group function to group data
   with the same month numeric value together.
2. Then “total Freight cost over each month” means applying the Sum
   function for Freight value within each month group.

To configure the report like above:

1. Select “Line” as the Chart Type in General Info group, two boxes will
   appear in Configuration section: “Labels (X-axis)” and “Values
   (Y-axis)”.
2. Add the field OrderDate into Labels box (drag the field from Middle
   Panel or use the Add icon +).
3. The field will be given the alias “Group(OrderDate)”.
4. Select the field in Labels box to open the Field Properties box.
5. Check to confirm that in Data Formatting group, “Group” is selected
   for the Function and “Month” is selected for the Format.
6. Add the field Freight into Values box (drag the field from Middle
   Panel or use the Add icon +).
7. The field will be given the alias “Sum(Freight)”.
8. Select the field in Values box to open the Field Properties box.
9. Check to confirm that in Data Formatting group, “Sum” is selected for
   the Function.

## Bar Chart and Column Chart

A bar chart displays groups of data as rectangular bars with lengths
proportional to the values that they represent. Therefore the bar chart
is used to show comparisons among different groups.

The column chart is the same as the bar chart, except for being
displayed vertically.

[![../_images/NW_Suppliers_Column_Chart_Supplier_Count_by_Country.png](https://devnet.logianalytics.com/hc/article_attachments/4415511799959/nw_suppliers_column_chart_supplier_count_by_country_350x158.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492542103/nw_suppliers_column_chart_supplier_count_by_country.png)

For example, table
Suppliers in Northwind database stores the list of suppliers specified
by SupplierID together with the Country. From that data, a report such
as comparing the number of suppliers per country would be best
visualized using a column chart.

1. “Per country” means using the Group function to group data with the
   same country text value together.
2. Then “the number of suppliers per country” means applying the Count
   function for SupplierID value within each country group.

To configure the report like above:

1. Select “Column” as the Chart Type in General Info group, two boxes
   will appear in Configuration section: “Labels (X-axis)” and “Values
   (Y-axis)”.
2. Add the field Country into Labels box (drag the field from Middle
   Panel or use the Add icon +).
3. The field will be given the alias “Group(Country)”.
4. Select the field in Labels box to open the Field Properties box.
5. Check to confirm that in Data Formatting group, “Group” is selected
   for the Function.
6. Add the field SupplierID into Values box (drag the field from Middle
   Panel or use the Add icon +).
7. The field will be given the alias “Count(SupplierID)”.
8. Select the field in Values box to open the Field Properties box.
9. Check to confirm that in Data Formatting group, “Count” is selected
   for the Function.

## Area Chart

An area chart displays graphically quantitative data. It is based on the
[Line Chart](#line-chart). The area between axis and line are
commonly emphasized with colors, textures and hatchings. Commonly one
compares with an area chart two or more quantities.

For example, this
area chart compares the amount of Product units in stock versus the
amount on order.

> [![../_images/Report_Chart_Area_UnitsInStock_UnitsOnOrder.png](https://devnet.logianalytics.com/hc/article_attachments/4415511800343/report_chart_area_unitsinstock_unitsonorder_600x253.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492542359/report_chart_area_unitsinstock_unitsonorder.png)

Another example with Range Only option.

> [![../_images/Area_Chart_Range_Only.png](https://devnet.logianalytics.com/hc/article_attachments/4415492542999/area_chart_range_only_672x265.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492542615/area_chart_range_only.png)

## Pie Chart

A pie chart displays data in a circle, divided into slices to illustrate
numerical proportion.

[![../_images/NW_Orders_Pie_Freight_by_Country_City.png](https://devnet.logianalytics.com/hc/article_attachments/4415492543639/nw_orders_pie_freight_by_country_city_315x244.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492543255/nw_orders_pie_freight_by_country_city.png)

For example, a pie chart
will compare proportions of the freight cost among different countries.

[![../_images/NW_Orders_Pie_Freight_by_Country_City_in_France.png](https://devnet.logianalytics.com/hc/article_attachments/4415504454551/nw_orders_pie_freight_by_country_city_in_france_315x246.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504454167/nw_orders_pie_freight_by_country_city_in_france.png)

This pie chart also
drills down data to freight cost among different cities in a selected
country.

To configure the report like that:

1. Select “Pie” as the Chart Type in General Info group, two boxes will
   appear in Configuration section: “Labels (X-axis)” and “Values
   (Y-axis)”.
2. Add the field ShipCountry into Labels box (drag the field from Middle
   Panel or use the Add icon +).
3. The field will be given the alias “Group(ShipCountry)” (Group
   function is used as expected).
4. Add the field ShipCity into Labels box (drag the field from Middle
   Panel or use the Add icon +).
5. The field will be given the alias “Group(ShipCity)” (Group function
   is used as expected).
6. Add the field Freight into Values box (drag the field from Middle
   Panel or use the Add icon +).
7. The field will be given the alias “Sum(Freight)” (Sum function is
   used as expected).

## Funnel Chart

A funnel chart displays values as progressively decreasing proportions.
Ideally the funnel chart shows a process that starts at 100% and ends
with a lower percentage where it is noticeable in what stages the fall
out happens and at what rate - the funnel chart illustrates where the
biggest bottlenecks are in the process.

Data like this sales pipeline data is best displayed using the funnel
chart:

[![../_images/SalesPipeline_Funnel.png](https://devnet.logianalytics.com/hc/article_attachments/4415492544151/salespipeline_funnel_218x145.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492543895/salespipeline_funnel.png)

|  |  |
| --- | --- |
| **Stage** | **Amount** |
| Prospects | 500 |
| Qualified prospects | 400 |
| Needs analysis | 200 |
| Price quotes | 150 |
| Negotiations | 100 |
| Closed sales | 50 |

## Donut Chart

Donut Chart displays data in a ring, divided into slices to illustrate
numerical proportion.

See also: [Pie Chart](#Pie_Chart)

## Combination Chart

A combination chart allows combining multiple charts of different types
together in the same report part.

* Comparison between Sales with and without Discount

  [![../_images/NW_Order_Details_Combination_Sales_and_DiscountSales.png](https://devnet.logianalytics.com/hc/article_attachments/4415492544663/nw_order_details_combination_sales_and_discountsales_434x231.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492544407/nw_order_details_combination_sales_and_discountsales.png)
* Relationship
  between ServiceTime and Sales

  [![../_images/ServiceTimeSales_Combination_Chart.png](https://devnet.logianalytics.com/hc/article_attachments/4415492545047/servicetimesales_combination_chart_750x318.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511801495/servicetimesales_combination_chart.png)

|  |  |  |
| --- | --- | --- |
| **Id** | **ServiceTime** | **Sales** |
| 1 | 150 | 200 |
| 2 | 80 | 930 |
| 3 | 30 | 1370 |
| 4 | 10 | 1504 |

* Area type is available in Combination chart from version 2.12.0.

  [![../_images/ServiceTimeSales_Combination_Chart_with_Area.png](https://devnet.logianalytics.com/hc/article_attachments/4415492545303/servicetimesales_combination_chart_with_area_470x312.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511801751/servicetimesales_combination_chart_with_area.png)

## Tree Map Chart

Tree Map displays data as a set of rectangles. It is good for comparing
proportions and spotting patterns. It can also display a large amount of
items on the screen simultaneously.

A Tree Map
comparing Products by their Units in Stock.

> [![../_images/Report_Part_Tree_Map.png](https://devnet.logianalytics.com/hc/article_attachments/4415492545943/report_part_tree_map_600x161.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504455191/report_part_tree_map.png)

To configure the report like that:

1. Select “Tree Map” as the Chart Type in General Info group, two boxes
   will appear in Configuration section: “Labels (X-axis)” and “Values
   (Y-axis)”.
2. Add the field ProductName into Labels box (drag the field from Middle
   Panel or use the Add icon +).
3. The field will be given the alias “Group(ProductName)” (Group
   function is used as expected).
4. Add the field UnitsInStock into Values box (drag the field from
   Middle Panel or use the Add icon +).
5. The field will be given the alias “Sum(UnitsInStock)” (Sum function
   is used as expected).
6. Click the Report Part’s header to open Report Part Properties panel
   again.
7. In Data group, tick Show Value Labels and Show Slice Labels.

## Heat Map Chart

Heat Map displays values in a matrix, with larger values represented by
darker colors.

A Heat Map
comparing Freights by Year and Country.

> [![../_images/Report_Heat_Map.png](https://devnet.logianalytics.com/hc/article_attachments/4415504455831/report_heat_map_600x204.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504455575/report_heat_map.png)

To configure the report like that:

1. Select “Heat Map” as the Chart Type in General Info group, three
   boxes will appear in Configuration section: “Labels (X-axis)”,
   “Values (Y-axis)” and “Value Label”.
2. Add the field OrderDate into Labels box (drag the field from Middle
   Panel or use the Add icon +).
3. The field will be given the alias “Group(OrderDate)”, Group as
   Function and Year as Format in Field Properties.
4. Add the field ShipCountry into Values box (drag the field from Middle
   Panel or use the Add icon +).
5. The field will be given the alias “Group(ShipCountry)” (Group
   function is used as expected).
6. Add the field Freight into Values box (drag the field from Middle
   Panel or use the Add icon +).
7. The field will be given the alias “Sum(Freight)” (Sum function is
   used as expected).
8. Click the Report Part’s header to open Report Part Properties panel
   again.
9. Click the gear icon next to Settings in Legends group to open Legend
   Settings pop-up.
10. Tick Visible check-box to show the legend.
11. Click OK to close the pop-up.
12. In Data group, tick Show Value Labels.

## Scatter Chart

A scatter chart displays data as data points, at the intersection of an
x and a y numerical value. For a scatter chart, both horizontal and
vertical axis are value axis, there is no category axis like the line
chart.

[![../_images/NW_Orders_Report_Chart_Scatter.png](https://devnet.logianalytics.com/hc/article_attachments/4415492549399/nw_orders_report_chart_scatter_767x206.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504456087/nw_orders_report_chart_scatter.png)

Above is a sample Scatter Chart Showing Number of Orders and Total
Freight by Country.

* The countries that appear further on the right have more orders.
* The countries that appear higher on the chart have more total
  freight.

To configure the report like that:

1. Select “Scatter” as the Chart Type in General Info group, three boxes
   will appear in Configuration section: “Labels (X-axis)”, “Values
   (Y-axis)” and “Value Label”.

   > For this chart, the numerical fields will be added before the
   > categories/labels.
2. Add the field OrderID into Labels box (drag the field from Middle
   Panel or use the Add icon +).
3. The field will be given the alias “Sum(OrderID)” (not the Count
   function as expected).
4. Click on the field “Sum(OrderID)” in Labels box to open Field
   Properties box.
5. Select Count as the Function in Data Formatting group, the field is
   now given the alias “Count(OrderID)”.
6. Add the field Freight into Values (Y-axis) box (drag the field from
   Middle Panel or use the Add icon +).
7. The field will be given the alias “Sum(Freight)” (Sum function is
   used as expected).
8. Add the field ShipCountry into Value Label box (drag the field from
   Middle Panel or use the Add icon +).
9. The field will be given the alias “Group(ShipCountry)” (Group
   function is used as expected).
10. Click the Report Part’s header to open Report Part Properties panel
    again.
11. In Data group, tick Show Value Labels check-box.

## Bubble Chart

Bubble chart is a variation of scatter chart in which the data points
are replaced with bubbles, and the size of the bubbles represents an
additional dimension of the data.

[![../_images/NW_Orders_Report_Chart_Bubble.png](https://devnet.logianalytics.com/hc/article_attachments/4415511803671/nw_orders_report_chart_bubble_767x235.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492549911/nw_orders_report_chart_bubble.png)

Above is a sample Bubble Chart Showing Number of Orders and Total
Freight by Country.

* The countries that appear further on the right have more orders.
* The countries that appear higher on the chart have more total
  freight.
* The countries in bigger bubbles have more cities being shipped to.

To configure the report like that:

1. Select “Bubble” as the Chart Type in General Info group, four boxes
   will appear in Configuration section: “Labels (X-axis)”, “Values
   (Y-axis)”, “Value Label” and “Bubble Size”.

   > For this chart, the numerical fields will be added before the
   > categories/labels.
2. Add the field OrderID into Labels box (drag the field from Middle
   Panel or use the Add icon +).
3. The field will be given the alias “Sum(OrderID)” (not the Count
   function as expected).
4. Click on the field “Sum(OrderID)” in Labels box to open Field
   Properties box.
5. Select Count as the Function in Data Formatting group, the field is
   now given the alias “Count(OrderID)”.
6. Add the field Freight into Values (Y-axis) box (drag the field from
   Middle Panel or use the Add icon +).
7. The field will be given the alias “Sum(Freight)” (Sum function is
   used as expected).
8. Add the field ShipCountry into Value Label box (drag the field from
   Middle Panel or use the Add icon +).
9. The field will be given the alias “Group(ShipCountry)” (Group
   function is used as expected).
10. Add the field ShipCity into Bubble Size box (drag the field from
    Middle Panel or use the Add icon +).
11. The field will be given the alias “Count(ShipCity)” (not the Count
    Distinct function as expected).
12. Click on the field “Count(ShipCity)” in Bubble Size box to open Field
    Properties box.
13. Select Count Distinct as the Function in Data Formatting group, the
    field is now given the alias “Count Distinct(ShipCity)”.
14. Click the Report Part’s header to open Report Part Properties panel
    again.
15. In Data group, tick Show Value Labels check-box.

## Waterfall Chart

A waterfall chart shows a running total as values are added or
subtracted. It’s useful for understanding how an initial value is
affected by a series of positive and negative values.

[![../_images/Report_Chart_Waterfall.png](https://devnet.logianalytics.com/hc/article_attachments/4415504456599/report_chart_waterfall_762x200.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511803927/report_chart_waterfall.png)

Sample
report on Northwind database, “Summary of Sales by Year” view showing
running sales by year.

To configure the report like that:

1. Select “Waterfall” as the Chart Type in General Info group, three
   boxes will appear in Configuration section: “Labels (X-axis)”,
   “Values (Y-axis)” and “Total Label”.
2. Add the field ShippedDate into Labels box (drag the field from Middle
   Panel or use the Add icon +).
3. The field will be given the alias “Group(ShippedDate)” (Group
   function and Year format are used as expected).
4. Add the field Subtotal into Values box (drag the field from Middle
   Panel or use the Add icon +).
5. The field will be given the alias “Sum(Subtotal)” (Sum function is
   used as expected).
6. Click the Report Part’s header to open Report Part Properties panel
   again.
7. In Data group, tick Show Value Labels check-box.

## Sparkline Chart

Sparkline is a tiny chart, usually drawn without axis and labels. It
provides a visual representation of data in a simple and compact way. It
is most commonly used as embedded report.

[![../_images/Report_Chart_Sparkline.png](https://devnet.logianalytics.com/hc/article_attachments/4415492550167/report_chart_sparkline_781x260.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504456855/report_chart_sparkline.png)

Sample sparkline chart comparing the related total freight and
number of orders by year.

To configure the report like that:

1. Select “Sparkline” as the Chart Type in General Info group, two boxes
   will appear in Configuration section: “Intervals (X-axis)” and
   “Values (Y-axis)”.
2. Add the field OrderDate into Labels box (drag the field from Middle
   Panel or use the Add icon +).
3. The field will be given the alias “Group(OrderDate)” (Group function
   and Year format are used as expected).
4. Add the field Freight into Metric 1 Value box (drag the field from
   Middle Panel or use the Add icon +).
5. The field will be given the alias “Sum(Freight)” (Sum function is
   used as expected).
6. Select Line as the Chart Type.
7. Click the Add Metrics at the end to add another Metric.
8. Add the field OrderID into Metric 2 Value box (drag the field from
   Middle Panel or use the Add icon +).
9. The field will be given the alias “Sum(OrderID)” (not the Count
   function as expected).
10. Click on the field “Sum(OrderID)” to open Field Properties box.
11. Select Count as the Function in Data Formatting group, the field is
    now given the alias “Count(OrderID)”.
12. Select Line as the Chart Type.
13. Click the Report Part’s header to open Report Part Properties panel
    again.

To be updated: screenshot of sparkline chart embedded inside a grid.

## Others

* Grid view pop-up option. This option is available from version 2.10.0.

  Click ![gridViewIcon](https://devnet.logianalytics.com/hc/article_attachments/4415492550423/grid_view_icon.png) icon to see the grid view of the chart data associated with the current drill-down level and metric.

  [![../_images/Chart_Grid_View_Popup.png](https://devnet.logianalytics.com/hc/article_attachments/4415504457623/chart_grid_view_popup_653x238.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504457239/chart_grid_view_popup.png)

- Metric drop-down.

> [![../_images/Chart_Metric_Dropdown.png](https://devnet.logianalytics.com/hc/article_attachments/4415504458007/chart_metric_dropdown_308x229.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511804439/chart_metric_dropdown.png)
