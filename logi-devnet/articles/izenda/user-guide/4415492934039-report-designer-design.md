---
title: "Report Designer/Design"
id: 4415492934039
section: "User Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492934039-Report-Designer-Design
updated_at: 2021-12-10T03:10:34Z
---

# Report Designer/Design

# Report Designer/Design

Tip: [Cross Filtering](#apply-cross-filtering-to-multiple-report-parts) is available from release v2.1.0.

The **Report Designer/Design** page allows users to

|  |  |
| --- | --- |
| * view data source fields’ properties * add report-level calculated fields * define report filters based on data source fields | * add report parts to report body * add data source fields to report * configure formatting and calculation properties for data source fields in report |

## View data source fields

1. Open an existing report if not already open.
2. Click Design in the left menu.

   ![../_images/Report_Designer_Fields_Location.png](https://devnet.logianalytics.com/hc/article_attachments/4415511807767/report_designer_fields_location_485x318.png)
3. Data sources will be displayed under Selected Data Source group in
   the Middle Panel, initially collapsed.
4. User-defined calculated fields are under Calculated Fields group, if
   available.
5. Click on a data source to expand its fields.
6. The data source fields are listed together with an icon representing
   their data types.

   ![../_images/Report_Designer_Fields_Middle_Panel.png](https://devnet.logianalytics.com/hc/article_attachments/4415511808023/report_designer_fields_middle_panel_223x496.png)

Note: The list of data source fields also supports searching via the top search box.

## View data source fields’ properties

1. Select a data source field to view its properties.
2. Properties of the selected field is displayed in the Field Properties
   box.

   ![../_images/Report_Designer_Fields_Field_Properties.png](https://devnet.logianalytics.com/hc/article_attachments/4415492555415/report_designer_fields_field_properties_263x440.png)

## Add Calculated Field

Calculated fields can also be added to a specific report.

> [![../_images/Report_Level_Calculated_Field_Discounted_Cost.png](https://devnet.logianalytics.com/hc/article_attachments/4415492555927/report_level_calculated_field_discounted_cost_724x550.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492555671/report_level_calculated_field_discounted_cost.png)
>
> A report-level calculated field. Note that in Expression box the connection name [Northwind] and schema name [dbo] are included since the fields can come from different connections.

Sample expressions:

> ```
> Casewhen([northwind].[dbo].[Orders].[EmployeeID]=1)then'less'when([northwind].[dbo].[Orders].[EmployeeID]=3)then'mid'when([northwind].[dbo].[Orders].[EmployeeID]=4)then'high'else'not evaluated'endCasewhen(BETWEEN([northwind].[dbo].[Orders].[EmployeeID],1,3))then'less'when(BETWEEN([northwind].[dbo].[Orders].[EmployeeID],4,6))then'mid'when(BETWEEN([northwind].[dbo].[Orders].[EmployeeID],7,10))then'high'else'not evaluated'endIF([northwind].[dbo].[Orders].[EmployeeID]<3)then'Less'else(IF(BETWEEN([northwind].[dbo].[Orders].[EmployeeID],3,6))then'More'else'Most'END)ENDCount(DISTINCT([Northwind].[dbo].[Orders].[ShipCity]))DATEPART(yyyy,[Northwind].[dbo].[Orders].[OrderDate])DATEPART(m,[Northwind].[dbo].[Orders].[OrderDate])CASEwhen(DATEPART(yyyy,[Northwind].[dbo].[Orders].[OrderDate])=1996)then1else0endDATEADD(year,1,[Northwind].[dbo].[Orders].[OrderDate])CAST([Northwind].[dbo].[Orders].[OrderID]astext)
> ```

See also: [Izenda Functions](https://devnet.logianalytics.com/hc/en-us/articles/4415504688663-Izenda-Functions)

Warning:

Calculated fields have a limitation for nesting up to 6 levels. Please see the example below:

Calculated Field [One] = [Retail].[dbo].[Orders].[OrderID] \* 2   
Calculated Field [Two] = [One] \* 2   
Calculated Field [Three] = [Two] \* 2   
Calculated Field [Four] = [Three] \* 2   
Calculated Field [Five] = [Four] \* 2   
Calculated Field [Six] = [Five] \* 2

If the user tries to create Calculated Field [Seven] as [Six] \* 2 the system will show an error that the nesting is too deep.

## Add a report filter

From the data sources, user can add report filters to select only the
rows that they need.

For example with Northwind database, to do a report on customers that
are in Atlanta city:

1. User should have selected “Customers” table in Data Source page.
2. Click Fields in the left menu.
3. Expand Filter section if needed by clicking the **>** icon.
4. Click on Selected Data Source in Middle Panel to expand the list.
5. Click on “Customers” data source to expand its fields.
6. Either drag the field “City” into the Filter box or click Add Filter
   button and select “City” in the drop-down.
7. Click on the filter area outside of the drop-down (in darker color)
   to expand the Filter Properties box.

   [![../_images/Report_Designer_Filter_Click_to_Select.png](https://devnet.logianalytics.com/hc/article_attachments/4415511808535/report_designer_filter_click_to_select_150x28.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511808279/report_designer_filter_click_to_select.png)
8. The properties are listed in Filter Properties box in 3 sections:

   * Source
   * Filter Operator
   * Filter Settings
   * Filter Formatting

![../_images/Report_Designer_Filter_Properties.png](https://devnet.logianalytics.com/hc/article_attachments/4415492556183/report_designer_filter_properties_265x878.png)

1. Select Equivalence in Filter Operator section.
2. Select Equals (Manual Entry) in the next drop-down.
3. Type in “Atlanta”.

Note:

* Any field marked as not filterable in Data Model cannot be used in a filter. It can neither be dragged into the Filter box, nor appear in a filter drop-down.
* The Use Lookup checkbox only display for table/view fields having valid filter lookup key-value setting in Data Model.

Note: In case data source is a stored procedure, its parameters are automatically added as report filters.

[![../_images/Report_Designer_Filter_SP_Parameter.png](https://devnet.logianalytics.com/hc/article_attachments/4415504462743/report_designer_filter_sp_parameter_719x241.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511808791/report_designer_filter_sp_parameter.png)

## Configure filter properties in Filter Settings section

In this section, user can:

* Choose a filter
  alias.

  > This alias will be the display text on report at runtime, if
  > visible.
  > The alias must be unique inside the whole report. Any duplicated
  > value will result in an error message ([Fig. 190](#report-designer-duplicated-filter-alias)).
  > The alias can contain any characters except for “[” and “]”.
  >
  > [![../_images/Report_Designer_Duplicated_Filter_Alias.png](https://devnet.logianalytics.com/hc/article_attachments/4415511809687/report_designer_duplicated_filter_alias_515x69.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511809175/report_designer_duplicated_filter_alias.png)
* Select the filter to be visible or not at runtime.

  > A filter with a fixed condition (such as “City” always equals
  > “Atlanta”) should be hidden at runtime.
* Select the filter to be required or not.
  :   A required filter will force end-user to enter filter values in
      order to run it.
      Contrary to a fixed condition, the example report above could be
      more flexible if the “City”-equals-“Atlanta” filter is visible
      and not required. Then the report still shows customers in
      Atlanta by default, but end-user can select another city or even
      empty the value to show all customers. Screenshot to be updated.

      Note

      For a stored procedure’s parameter, if the Required checkbox is not selected and the filter value is empty, the stored procedure will be executed with ‘null’ value. If your stored procedures do not return all results when null is passed, leaving this value as null will always return no results. This is a new behavior from version 2.12.0.
* Select the filter to be cascading or not.

  > A cascading filter will constrain the available values in other
  > filters behind it. For example, if a report has two filters:
  > Country and City, and a value was selected for Country, then the
  > only possible values that can be selected for City will be ones
  > with a match for the current Country. Screenshot to be updated.
* Choose sorting order for filter values: unsorted, ascending or
  descending by repeatedly clicking the icon.
* Select the filter condition.

  1. Select the operator group Comparison, Equivalence, Field
     Comparison or String.
  2. Select the specific operator.
  3. Enter or select the fields or values depending on each operator.

     ![../_images/Report_Designer_Filter_Operator.png](https://devnet.logianalytics.com/hc/article_attachments/4415511809943/report_designer_filter_operator_221x386.png)

Table 1 The list of available operators depends on the data type of the field:










| Operator Type / Operator | Text | Numeric | Money | Datetime | Boolean | Image | LOB |
| --- | --- | --- | --- | --- | --- | --- | --- |
| …/Blank/Not Blank | Y | Y | Y | Y | Y | ? | ? |
| Comparison | Y | Y | Y | Y | Y | ? | ? |
| Equivalence | Y | Y | Y | Y | Y | ? | ? |
| Field Comparison | Y | Y | Y | Y | Y | ? | ? |
| Date & Time |  |  |  | Y |  |  |  |
| String | Y |  |  |  |  |  |  |
| Boolean |  |  |  |  | Y |  |  |

## Configure filter properties in Filter Formatting section

In this section, user can:

* Choose a font face and font size.
* Choose text effects bold, italic and underlined.
* Set text color and cell color.

## Build complex filter logic

In most cases, user simply adds new filters when needed, and the report
returns data that matches all of the filter conditions.

In some other cases, that simple match-all condition is not enough. For
example, user needs a report of all customers that are in Atlanta city
with either CompanyName or ContactName “John”. Such “either A or B”
condition requires building a filter logic.

1. Add a filter for “City”, “Equivalence”, “Equals”, “Atlanta” (see [Add
   a report filter](#add-a-report-filter)).
2. Similarly, add a filter for “CompanyName”, “String”, “Like”, “John”.
3. Similarly, add a filter for “ContactName”, “String”, “Like”, “John”.
4. The filters are subsequently numbered 1, 2 and 3 in the filter box.
5. Enter the logic into Filter Logic box. The following rule of thumb
   may help:
6. For each “either A or B” condition, write an “or” condition using the
   filter numbers, and wrap it in parentheses - `(2OR3)` for this
   example.
7. Fill in other “and” conditions using the filter numbers -
   `1AND(2OR3)` for this example.
8. Click Validate Syntax button to check the logic.

   [![../_images/Report_Designer_Filter_Logic_1_AND_(2_OR_3).png](https://devnet.logianalytics.com/hc/article_attachments/4415504463383/report_designer_filter_logic_1_and__2_or_3__953x234.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492557463/report_designer_filter_logic_1_and__2_or_3_.png)

## Apply Cross Filtering to Multiple Report Parts

New in version 2.1.0.

Cross filtering allows user to drill up and drill down data in multiple [report parts](https://devnet.logianalytics.com/hc/en-us/articles/4415492696343-Glossary#term-report-part) together. For each drilling action from user, it will filter related report parts automatically. Cross filtering is initalized on charts, gauges, or maps which have more than one x-axis field as the drill down feature of these items is what triggers the cross fitlering functionality for all other report parts.

[![../_images/Report_Cross_Filtering_ShipCountry_ShipCity_by_Germany.png](https://devnet.logianalytics.com/hc/article_attachments/4415504463767/report_cross_filtering_shipcountry_shipcity_by_germany_810x566.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492557847/report_cross_filtering_shipcountry_shipcity_by_germany.png)

1. Select related report parts to apply cross filtering. In this example Chart and Grid will be drilled up and down together while Map remains independent.

   [![../_images/Report_Cross_Filtering_Report_Part_Selection.png](https://devnet.logianalytics.com/hc/article_attachments/4415504464151/report_cross_filtering_report_part_selection_454x341.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492558103/report_cross_filtering_report_part_selection.png)
2. Set up report parts to have common data source fields. In this example Chart and Grid display aggregated data for ShipCountry and ShipCity.
3. Drill down on one report part by clicking on a data point.

   [![../_images/Report_Cross_Filtering_ShipCountry_ShipCity_by_All.png](https://devnet.logianalytics.com/hc/article_attachments/4415492558359/report_cross_filtering_shipcountry_shipcity_by_all_810x506.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504465047/report_cross_filtering_shipcountry_shipcity_by_all.png)
4. The related report parts are filtered automatically, and the Cross Filtering breadcrumb tells which report part is being drilled down.
5. To reset, either drill up the exact report part, or remove the drill-down on the breadcrumb.

   [![../_images/Remove_a_Cross_Filter.png](https://devnet.logianalytics.com/hc/article_attachments/4415492558743/remove_a_cross_filter_810x41.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504465303/remove_a_cross_filter.png)

## Manage Report Parts

There are many ways to
display data in a report: bar chart, line chart, pie chart, map, data
grid, etc, each is supported by a different [report part](https://devnet.logianalytics.com/hc/en-us/articles/4415492696343-Glossary#term-report-part). Built-in report
parts include:

* Chart (Bar Chart, Line Chart, Pie Chart, etc.)
* Form
* Grid (Horizontal, Vertical, Pivot)
* Gauge
* Map

Any new report will include one default blank report part. Additional
report parts of the same or different types can be added by:

* clicking Add Report Part button at the top.
* clicking the add icon (+) in any available background cell.

  [![../_images/Report_Designer_Add_Report_Part.png](https://devnet.logianalytics.com/hc/article_attachments/4415511814295/report_designer_add_report_part_524x241.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511813783/report_designer_add_report_part.png)

Note: When the “Snap To Grid” checkbox is selected, each report part that is added aligns itself right beside or below the last report part that was added. If you have already put the report parts right beside or below the last report part you created manually, you will not see any difference.

* clicking the copy icon in the configuration header.

  [![../_images/Report_Designer_Copy_Report_Part.png](https://devnet.logianalytics.com/hc/article_attachments/4415504465943/report_designer_copy_report_part_656x107.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492558999/report_designer_copy_report_part.png)

A report part can be removed by clicking the delete icon in the
configuration header.

> [![../_images/Report_Designer_Remove_Report_Part.png](https://devnet.logianalytics.com/hc/article_attachments/4415504466199/report_designer_remove_report_part_94x64.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511814807/report_designer_remove_report_part.png)

Report parts can be resized, dragged to a new location, or switched
position with each other in Preview Mode.

> [![../_images/Report_Designer_Switch_to_Preview_Mode.png](https://devnet.logianalytics.com/hc/article_attachments/4415511815063/report_designer_switch_to_preview_mode_128x46.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504466583/report_designer_switch_to_preview_mode.png)

* To resize:

  1. Hover the cursor over borders and corners of a report part.
  2. When the cursor changes, click and drag to resize the report part.
  3. The color of the dragged report part remains purple if the new
     size is acceptable, and changes to orange if the new size overlaps
     with other report parts.
  4. Release the mouse when the color is purple to accept the new size.
  5. Release the mouse when the color is orange to cancel.
* To change location:

  [![../_images/Report_Designer_Drag_Report_Part_to_Invalid_Location.png](https://devnet.logianalytics.com/hc/article_attachments/4415504467095/report_designer_drag_report_part_to_invalid_location_524x309.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504466839/report_designer_drag_report_part_to_invalid_location.png)

  1. Hover the cursor over the report part header.
  2. When the cursor changes, click and drag the report part to a new
     location.
  3. The shadow rectangle is where the report part will land.
  4. The color of the dragged report part remains purple if the new
     location is acceptable, and changes to orange if the new location
     overlaps with other report parts.
  5. Release the mouse when the color is purple to accept the new
     location.
  6. Release the mouse when the color is orange to cancel.
* To switch position with another report part:

  [![../_images/Report_Designer_Drag_Report_Part_to_Switch_Location.png](https://devnet.logianalytics.com/hc/article_attachments/4415492559767/report_designer_drag_report_part_to_switch_location_507x376.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511815319/report_designer_drag_report_part_to_switch_location.png)

  1. Hover the cursor over the report part header.
  2. When the cursor changes, click and drag the report part over
     another.
  3. The shadow rectangle is where the report part will land.
  4. Drag the report part so that the shadow rectangle completely
     covers or is completely covered by the other report part, and the
     color of the dragged report part remains purple.
  5. Release the mouse when the color is purple to accept the new
     location.

[![../_images/Report_Designer_FreightGrid_FreightChart_OrdersGrid.png](https://devnet.logianalytics.com/hc/article_attachments/4415504467735/report_designer_freightgrid_freightchart_ordersgrid_951x434.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511815831/report_designer_freightgrid_freightchart_ordersgrid.png)

## Configure report part properties

See:

* [Report Designer/Chart](https://devnet.logianalytics.com/hc/en-us/articles/4415504845847-Report-Designer-Chart)
* [Report Designer/Form](https://devnet.logianalytics.com/hc/en-us/articles/4415504847767-Report-Designer-Form)
* [Report Designer/Gauge](https://devnet.logianalytics.com/hc/en-us/articles/4415492935959-Report-Designer-Gauge)
* [Report Designer/Grid](https://devnet.logianalytics.com/hc/en-us/articles/4415492936855-Report-Designer-Grid)
* [Report Designer/Map](https://devnet.logianalytics.com/hc/en-us/articles/4415492937751-Report-Designer-Map)

## Open Field Properties box for data source fields in report

1. Click on a data source field inside report body.
2. The properties are listed in Field Properties box in 4 sections:
   * Data Source
   * Data Formatting
   * Header Formatting
   * Drill Down

Note: Instead of trying to find a field inside report body and click on it, user can quickly select a report part then one of its fields using the two drop-downs on top of Field Properties box.

[![../_images/Report_Designer_Data_Source_Report_Part_And_Field_Drop-downs.png](https://devnet.logianalytics.com/hc/article_attachments/4415511816983/report_designer_data_source_report_part_and_field_drop-downs_219x244.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504467991/report_designer_data_source_report_part_and_field_drop-downs.png)

## Configure field properties in Data Source section

In this section, user can:

* Choose an alias
  for the selected data source field.

  > The alias must be unique inside the whole report. Any duplicated
  > value will result in an error message.
  > The alias can contain any characters except for “[” and “]”.
  >
  > ![../_images/Report_Designer_Fields_Duplicated_Field_Alias.png](https://devnet.logianalytics.com/hc/article_attachments/4415511817239/report_designer_fields_duplicated_field_alias_219x217.png)
* Select visible or not for the field. A not visible field will not
  appear on the report screen at runtime.

## Configure field properties in Data Formatting section

In this section, user can:

* Apply a function to the field.

  > The list of available functions depends on the data type and
  > includes two lists:

  + User-defined functions marked as Field Level in Data Model which
    require a single input parameter in a compatible data type.
  + System built-in functions for that specific data type.

Table 2 List of system built-in functions for each data type











| Built-in   Function | Description | Text | Numeric | Money | Datetime | Boolean | Image | LOB |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Average | Returns the average of the values in a field. |  | Y | Y |  |  |  |  |
| Count | Returns the number of items in a field. | Y | Y | Y | Y | Y |  |  |
| Count   Distinct | Returns the number of unique items in a field. | Y | Y | Y | Y | Y |  |  |
| Maximum | Returns the maximum value in a field. | Y | Y | Y | Y |  |  |  |
| Minimum | Returns the minimum value in a field. | Y | Y | Y | Y |  |  |  |
| Sum | Returns the sum of all values in a field. |  | Y | Y |  |  |  |  |
| Sum   Distinct | Returns the sum of all unique values in a field. |  | Y | Y |  |  |  |  |
| Group | Groups data together by field values for aggregating. | Y | Y | Y | Y | Y |  |  |
| Days Old | Returns the number of days counting from today’s date. |  |  |  | Y |  |  |  |
| Average   Days Old | Returns the average number of days counting from today’s date. |  |  |  | Y |  |  |  |
| Sum   Days Old | Return the sum of numbers of days counting from today’s date. |  |  |  | Y |  |  |  |
| Group   Days Old | Groups data together by numbers of days for aggregating. |  |  |  | Y |  |  |  |

* Choose a display format for the field.

> The list of available formats depends on the data type of
> the field.
>
> Note: New in version 2.6.0: Add new formats for Numeric and Money Data Types.
>
> - % of Subtotal   
> - % of Subtotal (with rounding)   
> - % of Grandtotal   
> - % of Grandtotal (with rounding)   
> - % of Sidetotal   
> - % of Sidetotal (with rounding)
>
> When a sub/grand total is not yet defined, it should default to the sum.

* Choose a font face and font size.
* Choose text effects bold, italic and underlined.
* Choose text alignment left, center, right or justify and top, middle or bottom. Vertical alignment is available for grid from version 2.10.0.
* Turn on or off word wrap option. (This option available from v2.10.0).
* Choose data sorting order unsorted, ascending or descending by
  repeatedly clicking the icon.
* Set text
  color and cell color for different ranges of value.

  1. Click either icon.
  2. Select Value, Range Value or Range Percentage in Text Color
     Settings or Cell Color Settings pop-up.
  3. Click Add Setting.

![../_images/Report_Designer_Field_Text_Color_Range.png](https://devnet.logianalytics.com/hc/article_attachments/4415504469143/report_designer_field_text_color_range_457x300.png)

* * Enter a value or a range of value then pick a color.
  * Continue to click Add Setting to add more ranges and colors.
  * Click OK to save the setting.

  ![../_images/Report_Designer_Field_Alternative_Text_Value.png](https://devnet.logianalytics.com/hc/article_attachments/4415492561687/report_designer_field_alternative_text_value_457x194.png)

  * Set alternative text for different ranges of value.

    1. Click the icon.
    2. Select Value, Range Value or Range Percentage in Alternative Text
       Settings pop-up.
    3. Click Add Setting.
    4. Enter a value or a range of value then type in an alternative
       text.
    5. Continue to click Add Setting to add more ranges and alternative
       texts.
    6. Click OK to save the setting.
  * Set custom URL.

    1. Click the icon.
    2. Enter the url into the text box.
    3. Choose an option to open the url in a new window, a new tab or the
       current window.
    4. Click OK to save the setting.
  * Write customized action in embedded JavaScript.

System variables

Some system variables are available for use in Custom URL or Embedded JavaScript pop-ups.

* `pXvalue=a_value` sets `a_value` as the value for filter number X.
* `{column_name}` will be replaced by the value in the column specified.
* `{0}` will be replaced by the value in current column.

For example:

* `http://www.google.com/?q={0}` when clicked on will open Google and search for the value in this column.
* `http://www.google.com/?q={[OrderDay]}` when clicked on will open Google and search for the value in column OrderDay.
* `http://127.0.0.1/new/e8d89dc0-5933-4946-816c-c0ee4e30f2b2?p1value={[OrderDay]}` when clicked on will take the value in column OrderDay, open the report with id=e8d89dc0-5933-4946-816c-c0ee4e30f2b2 and pass the value to the first filter of that report.

* Set Grand Total and Sub Total.

Grand Total and Sub Total

In report tables, the Grand Total for a field will provide the sum of all values within that field across the entire table. For example, in a report for Northwind database’s Orders table, the Grand Total for Freight field will tell the sum of all Freight costs until now. Screenshot to be updated.

To have the sum for all Freight costs to each country without having to create additional reports, Grouping and Sub Total can be used. Grouping will group data for each ShipCountry together, while Sub Total for Freight field will give the sum of all Freight costs in each country/group. Screenshot to be updated.

Grand Total and Sub Total is not necessarily the sum calculation. Other functions include minimum, maximum, average, count and user-defined expression.

For more detail about Grand Total and Sub Total please read [Grand Total and Sub Total](https://devnet.logianalytics.com/hc/en-us/articles/4415512098967-Grand-Total-and-Sub-Total).

To set up both Grand Total and Sub Total for Freight costs in Northwind database’s Orders table as an example:

> 1. Choose Orders table as Data Source, add a Grid report part, add [ShipCountry] and [Freight] to the list of columns.
>
>    ![../_images/Report_Designer_Added_ShipCountry_and_Freight.png](https://devnet.logianalytics.com/hc/article_attachments/4415504469399/report_designer_added_shipcountry_and_freight_443x240.png)
> 2. Select [ShipCountry] in the report part.
> 3. Choose Group in Function drop-down. Data will be grouped by each
>    available value in [ShipCountry].
>
>    ![../_images/Report_Designer_ShipCountry_Group_Function.png](https://devnet.logianalytics.com/hc/article_attachments/4415504469783/report_designer_shipcountry_group_function_252x334.png)
> 4. Select
>    [Freight] in the report part.
> 5. Click the Grand Total icon to open the pop-up.
> 6. Enter the display label in Grand Total Label box (e.g. “Total
>    Freight Costs”).
> 7. Select Sum in Grand Total Function drop-down.
> 8. The data type Money is automatically suggested in Data Type
>    drop-down.
> 9. Select a format in Format drop-down.
>
>    New in version 2.6.0: Add new formats:
>
>    - % of Subtotal   
>    - % of Subtotal (with rounding)   
>    - % of Grandtotal   
>    - % of Grandtotal (with rounding)
> 10. Click OK to close the pop-up.
>
>     [![../_images/Report_Designer_Freight_Grand_Total_Sum.png](https://devnet.logianalytics.com/hc/article_attachments/4415504470039/report_designer_freight_grand_total_sum_590x369.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511818903/report_designer_freight_grand_total_sum.png)
> 11. Click
>     the Sub Total icon to open the pop-up.
> 12. Enter the display label in Subtotal Label box (e.g. “Freight
>     Costs for this Country”).
> 13. Select Sum in Subtotal Function drop-down.
> 14. The data type Money is automatically suggested in Data Type
>     drop-down.
> 15. Select a format in Format drop-down.
>
>     New in version 2.6.0: Add new formats:
>
>     - % of Subtotal   
>     - % of Subtotal (with rounding)   
>     - % of Grandtotal   
>     - % of Grandtotal (with rounding)
> 16. Click OK to close the pop-up.
> 17. Click OK to close the pop-up.
>
>     [![../_images/Report_Designer_Freight_Sub_Total_Sum.png](https://devnet.logianalytics.com/hc/article_attachments/4415504476055/report_designer_freight_sub_total_sum_596x376.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504470551/report_designer_freight_sub_total_sum.png)
> 18. Click Save at the top.

## Configure field properties in Header Formatting section

In this section, user can adjust formatting for the header row:

* Set column width.
* Choose a font face and font size.
* Choose text effects bold, italic and underlined.
* Choose text alignment left, center, right or justify and top, middle or bottom. Vertical alignment is available for grid from version 2.10.0.
* Choose text color and cell color (see [Configure field properties in
  Data Formatting
  section](#configure-field-properties-in-data-formatting-section)).
* Turn on or off word wrap option.
* Set the “grouping key” for specific columns to stand next to each
  other. Screenshot to be updated.

## Configure Subreports using field properties in Drill Down section

In this section, user can connect another report as subreport via the
values in this parent report.

1. Click the icon to open Subreport Settings pop-up.
2. Select the subreport from the drop-down list.
3. Tick the checkbox in case subreport needs to filter in the same way
   as parent report.
4. Click Add Field Mapping button to insert a new mapping row.
5. Select a field in current report to use its values as filter
6. Select a field in subreport to be filtered by those values.

   ![../_images/Report_Designer_Sub-report_Field_Mapping.png](https://devnet.logianalytics.com/hc/article_attachments/4415504476439/report_designer_sub-report_field_mapping_458x284.png)
7. Continue to add more field mappings as needed.
8. Choose a display style for the subreport in the Style drop-down.
9. Click OK to save the setting.

See also: [Report on Multiple Tables](https://devnet.logianalytics.com/hc/en-us/articles/4415512111383-Report-on-Multiple-Tables)
