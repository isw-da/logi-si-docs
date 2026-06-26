---
title: "Report Designer/Grid"
id: 4415492936855
section: "User Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492936855-Report-Designer-Grid
updated_at: 2021-12-10T03:10:36Z
---

# Report Designer/Grid

# Report Designer/Grid

Grid is a built-in type of report part that displays data in a tabular
format. It currently supports 4 different vertical, horizontal, pivot
and drill-down styles.

## Configure Report Part Properties for Grid

1. Select the grid in Report Body (See [Manage Report Parts](https://devnet.logianalytics.com/hc/en-us/articles/4415492934039-Report-Designer-Design#manage-report-parts) for how to
   add a grid).
2. Click the expand icon (<) on the right to open the Properties boxes
   if needed.
3. Select the vertical Report Part Properties box.
4. The properties are listed in Report Part Properties box in 7
   sections.
   * General Info
   * Table
   * Columns
   * Rows
   * Headers
   * Grouping
   * View

![../_images/Report_Designer_Grid_Properties.png](https://devnet.logianalytics.com/hc/article_attachments/4415511827991/report_designer_grid_properties_248x488.png)

User can define the properties and see changes reflected in Preview
pane:

* Select a style in Grid Style drop-down.

  + Vertical: data is displayed vertically.
  + Horizontal: data is displayed horizontally.
  + Pivot (cross tabulation): data is displayed in a matrix format.
  + Drill Down: data is displayed in collapsible groups of values to
    see the detailed or summarized numbers.

  ![../_images/Report_Designer_Border_Settings_Pop-up.png](https://devnet.logianalytics.com/hc/article_attachments/4415504488599/report_designer_border_settings_pop-up_455x346.png)

  Define table border settings.

  1. Click the gear icon (⚙) to open Border Settings pop-up.
  2. Select pre-defined border styles: None (default), Outside, Inside
     or All,

     [![../_images/Grid_Pre-defined_Border_Styles.png](https://devnet.logianalytics.com/hc/article_attachments/4415492579735/grid_pre-defined_border_styles.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492579735/grid_pre-defined_border_styles.png)

     Fig. 227 Pre-defined Grid Border Style

     or click specific border style buttons in Preview section to apply.
  3. Select a line pattern: Solid (default), Dot or Dash.
  4. Select a border color.
  5. Select the border thickness (in pixels).
  6. Click OK to close the Border Settings pop-up.

  ![../_images/Report_Designer_Background_Color.png](https://devnet.logianalytics.com/hc/article_attachments/4415492579991/report_designer_background_color.png)
* Set the background color.

  ![../_images/Report_Designer_Alternative_Background_Color.png](https://devnet.logianalytics.com/hc/article_attachments/4415504488855/report_designer_alternative_background_color.png)
* Set the alternative background (New in version 2.9.0) by selecting one of four options:

  > + **None**: Do not apply alternative background color. When selecting this option, the Alternative Background Color does not display.
  > + **Rows**: Apply alternative background color for rows.
  > + **Columns**: Apply alternative background color for columns.
  > + **Rows and Columns**: Apply alternative background color for both rows and columns.
  >
  > ![../_images/Report_Designer_Columns_Width_Setting.png](https://devnet.logianalytics.com/hc/article_attachments/4415504489367/report_designer_columns_width_setting.png)
* Set the column width in pixels and turn on/off column word wrap (column word wrap is available from version 2.10.0).

  ![../_images/Report_Designer_Headers_Setting.png](https://devnet.logianalytics.com/hc/article_attachments/4415504489879/report_designer_headers_setting_218x288.png)
* Choose a header font
  face and font size.
* Choose header text effects bold, italic and underlined.
* Choose header text color and cell color.
* Choose header text alignment left, center, right or justify and top, middle or bottom. Vertical alignment is available from version 2.10.0.
* Turn on or off word wrap option.
* Choose Freeze Headers (available from version 2.10.0).
* **Note:**
  :   + The Freeze Header setting will apply for the report part in report designer, report viewer and dashboard.
      + If a sub-report has Freeze Header setting, the setting will apply for Link or Pop-up type but NOT for Embedded type.
* Optionally hides the header in export.
* Select to use Separators, and select a display format for multiple-field Separator.

  The Separators option displays multiple grids according to each unique value of the field(s) defined in Separators box.

  [![../_images/NW_Orders_Grid_Separators_ShipCountry,_ShipRegion_Group_by_ShipCity_Count_OrderID.png](https://devnet.logianalytics.com/hc/article_attachments/4415504490903/nw_orders_grid_separators_shipcountry__shipregion_group_by_shipcity_count_orderid_212x277.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504490519/nw_orders_grid_separators_shipcountry__shipregion_group_by_shipcity_count_orderid.png)

  For example, to display multiple grids, each one for each country and region in Northwind Orders table:

  1. Tick Use Separator check-box in Grouping in Report Part Properties
     to see Separators box inside the grid configuration.
  2. Add [ShipCountry] and [ShipRegion] to Separators box, they will
     show up as Group(ShipCountry) and Group(ShipRegion).
  3. Add [ShipCity] to Columns box, then choose Group as the Function,
     it should show up as Group(ShipCity).
  4. Add [OrderID] to Columns box, then choose Count as the Function,
     it should show up as Count(OrderID).
  5. The result should be multiple grids, each for a specific country
     and region.
  6. Select a different
     Separator Style if needed.

     [![../_images/NW_Orders_Separators_Multi_Level_With_Label.png](https://devnet.logianalytics.com/hc/article_attachments/4415492580887/nw_orders_separators_multi_level_with_label_608x251.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504491671/nw_orders_separators_multi_level_with_label.png)
  7. Optionally choose to print each grid in a new page by checking
     **Page Break After Separator** in Printing group.

  ![../_images/Report_Designer_Data_Refresh_Interval.png](https://devnet.logianalytics.com/hc/article_attachments/4415504448919/report_designer_data_refresh_interval_455x259.png)
* Configure how
  often data is refreshed when report is being viewed.

  1. Click the gear icon (⚙) to open Data Refresh Interval pop-up.
  2. Choose to have data refreshed automatically or manually.
  3. Enter an interval between each refresh (in seconds).
  4. Choose to view all data or enter a number to view that specific
     number of latest records only.
* Optionally display a long report in multiple pages.
* Screenshot for Pivot columns per exported page to be added.

## Choose a Grid Style

* The
  pivot grid styles must used when all the label values depend on the
  actual data (not predetermined). For example, this report with all
  the header values calculated from the data (OrderDate) must use the
  pivot style.

  ![../_images/NW_Orders_Order_Count_by_OrderYear_ShipCountry_ShipCity.png](https://devnet.logianalytics.com/hc/article_attachments/4415511828631/nw_orders_order_count_by_orderyear_shipcountry_shipcity_387x158.png)
* The
  drill-down grid style must be used for the need to expand and
  collapse groups of values to see the detailed or summarized numbers.
  For example, this report with the number of suppliers per city then
  per country must use the drill-down style.

  ![../_images/NW_Suppliers_Drill-down_Preview.png](https://devnet.logianalytics.com/hc/article_attachments/4415504491927/nw_suppliers_drill-down_preview_341x349.png)
* The
  vertical and horizontal styles are used when some label values are
  already determined at design time. And horizontal style should be
  used when the list of label values is expectedly longer than the
  number of columns. For example: the list of US States and Territories
  by Population.

  ![../_images/List_of_US_States_and_Territories_by_Population.png](https://devnet.logianalytics.com/hc/article_attachments/4415492581143/list_of_us_states_and_territories_by_population_488x445.png)

## Define a Vertical or Horizontal Grid Content

A newly-added grid will have the default vertical style. User only needs
to enter the title, description and define the columns to get it
working.

1. Optionally enter a title for the report.
2. Optionally enter a description.
3. Drag data source fields from middle panel into Columns text box to
   add them to the report.

A horizontal grid is defined in the same way as the vertical except that
data source fields are added to Rows text box.

## Define a Pivot Grid Content

[![../_images/NW_Orders_Order_Count_by_OrderYear_ShipCountry_ShipCity.png](https://devnet.logianalytics.com/hc/article_attachments/4415492581399/nw_orders_order_count_by_orderyear_shipcountry_shipcity.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492581399/nw_orders_order_count_by_orderyear_shipcountry_shipcity.png)

To
define this sample report:

1. Select “Pivot” as the Grid Style in General Info group.
2. Drag OrderDate field in Orders table from Middle Panel into Columns
   box.
3. The field will be given the alias “Group(OrderDate)” (Group function
   is used as expected).
4. Select the field in Columns box to open the Field Properties.
5. Check to confirm that in Data Formatting group, “Year” is selected
   for the format.
6. Drag ShipCountry field in Orders table from Middle Panel into Rows
   box.
7. The field will be given the alias “Group(ShipCountry)” (Group
   function is used as expected).
8. Drag ShipCity field in Orders table from Middle Panel into Rows
   box.
9. The field will be given the alias “Group(ShipCity)” (Group function
   is used as expected).
10. Drag OrderID field in Orders table from Middle Panel into Values
    box.
11. The field will be given the alias “Sum(OrderID)” (not the expected
    Count function).
12. Select the field in Values box to open the Field Properties.
13. In Data Formatting, select “Count” as the Function.
14. Drag Freight field in Orders table from Middle Panel into Values
    box.
15. The field will be given the alias “Sum(Freight)” (Sum function
    is used as expected).

Side Total

In a Pivot Grid report, Side Total values will provide the sum of all values for each field in Values box across each row.

To set up Side Total for a Pivot Grid report, check on the “Add Side Total” checkbox under Columns section in Configuration Section in report part backside.

[![../_images/NW_Side_Total_Example.png](https://devnet.logianalytics.com/hc/article_attachments/4415511829015/nw_side_total_example.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511829015/nw_side_total_example.png)

## Define a Drill Down Grid Content

To define this
sample report:

1. Select Suppliers table in report Data Source.
2. Add a grid to report body.
3. Select “Drill Down” as the Grid Style in General Info group.
4. Drag Country field in Suppliers table from Middle Panel into Groups
   box.
5. The field will be given the alias “Group(Country)” (Group function is
   used as expected).
6. Drag Region field in Suppliers table from Middle Panel into Groups
   box.
7. The field will be given the alias “Group(Region)” (Group function is
   used as expected).
8. Drag City field in Suppliers table from Middle Panel into Groups box.
9. The field will be given the alias “Group(City)” (Group function is
   used as expected).
10. Drag SupplierID field in Suppliers table from Middle Panel into
    Values box.
11. The field will be given the alias “Sum(SupplierID)” (not the expected
    Count function).
12. Select the field in Columns box to open the Field Properties.
13. In Data Formatting, select “Count” as the Function.
14. The Field Name Alias can be renamed to be more user-friendly (“Suppl
    Cnt”).

![../_images/NW_Suppliers_Drill-down_Preview.png](https://devnet.logianalytics.com/hc/article_attachments/4415504491927/nw_suppliers_drill-down_preview_341x349.png)
