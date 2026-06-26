---
title: "Data Model/Tables, Views and Stored Procedures"
id: 4415492931607
section: "Administrator Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492931607-Data-Model-Tables-Views-and-Stored-Procedures
updated_at: 2021-12-10T03:10:29Z
---

# Data Model/Tables, Views and Stored Procedures

# Data Model/Tables, Views and Stored Procedures

The **Data Model/Tables**, **Data Model/Views** and **Data Model/Stored Procedures** pages allow user to

* manage tables, views, their columns and relationships
* add and remove calculated fields
* manage stored procedures, their parameters, output columns and
  relationships
* assign filter values for stored procedure parameters
* mark stored procedures as dynamic

**Note:**
:   Stored Procedures are not supported in AWS Redshift databases.

## List tables, views or stored procedures

1. In browser, log in to Izenda as a user with Data Model permission.
2. Click Settings, then Data Setup then Data Model in the left menu.
3. Select the Setting Level: either System or a specific tenant.
4. Click Tables, Views or Stored Procedures in the Middle Panel.

   [![../_images/Data_Model_Tables_Views_Stored_Procedures_Location.png](https://devnet.logianalytics.com/hc/article_attachments/4415504406679/data_model_tables_views_stored_procedures_location_476x381.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511751063/data_model_tables_views_stored_procedures_location.png)
5. Visible tables, views, or stored procedures from all connections will
   be displayed in the upper data source grid, and columns of the
   currently selected one will be displayed in the lower Column Grid.

   [![../_images/Data_Model_Tables_and_Views_Column_Grid.png](https://devnet.logianalytics.com/hc/article_attachments/4415492494103/data_model_tables_and_views_column_grid_476x229.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504315287/data_model_tables_and_views_column_grid.png)
6. By default, only the first page with 10 items are displayed. To see
   more, either use the next page icon

   [![../_images/Data_Model_Next_Page_Icon.png](https://devnet.logianalytics.com/hc/article_attachments/4415504403991/data_model_next_page_icon_92x33.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492492695/data_model_next_page_icon.png)

   or select a larger number in Items per page box.

   [![../_images/Data_Model_Items_per_page.png](https://devnet.logianalytics.com/hc/article_attachments/4415504404503/data_model_items_per_page_172x85.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504404247/data_model_items_per_page.png)

## Search for tables, views or stored procedures

The Search box at the top allows user to search for specific tables,
views or stored procedures.

1. Select a specific element to search for in the dropdown on the left
   of the Search box. Default is All.

   ![../_images/Data_Model_Tables_and_Views_Search_by_Elements.png](https://devnet.logianalytics.com/hc/article_attachments/4415492494359/data_model_tables_and_views_search_by_elements_289x147.png)
2. Type a partial name and click the search icon (🔍).
3. Only the matching tables, views or stored procedures will be
   displayed.

## Assign a category to a table, view or stored procedure

1. Select a name in the Category dropdown to assign it to the table,
   view or stored procedure.
2. If the category name is not yet in the list, user can add it by typing the name in and press Enter.

   [![../_images/Data_Model_New_Category.png](https://devnet.logianalytics.com/hc/article_attachments/4415511752087/data_model_new_category_600x135.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511751831/data_model_new_category.png)
3. Continue to assign category to more tables, views or stored
   procedures in the same page.
4. Click Save button at the top, then click OK in the confirmation
   pop-up.

   > Note: User must save the assignments before moving to another page or another group in the Middle Panel.

See also: [Advanced Settings/Add data source categories](https://devnet.logianalytics.com/hc/en-us/articles/4415504834839-Advanced-Settings#add-data-source-categories).

## Assign an alias to a table, view or stored procedure

1. Enter an alias into the Database Source Alias box to assign it to the
   table, view or stored procedure.
2. Continue to assign alias to more tables, views or stored procedures
   in the same page.

   > The alias can contain any characters except for “[” and “]”.
3. Click Save button at the top, then click OK in the confirmation
   pop-up.

   > Note: User must save the assignments before moving to another page or another group in the Middle Panel.

Note: Within a category, the aliases cannot be duplicated. In , Alias\_1 is duplicated because the data sources are in the same Category2, and Alias\_2 is valid because the data sources are in different categories.

[![../_images/Data_Model_Duplicated_Category_and_Alias.png](https://devnet.logianalytics.com/hc/article_attachments/4415511754391/data_model_duplicated_category_and_alias_966x254.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504407319/data_model_duplicated_category_and_alias.png)

## Manage relationships for a table, view or stored procedure

1. Click the relationhips icon at the end of each line to open the
   Relationships dialog.
2. See [Data Model/Relationships and Schema](https://devnet.logianalytics.com/hc/en-us/articles/4415492930711-Data-Model-Relationships-and-Schema) for how to manage
   relationships.

## Assign an alias to a column in table, view or stored procedure

1. In the Column Grid, enter an alias into the Column Alias box to
   assign it to the column.
2. Continue to assign alias to more columns in the same page.

   > The alias can contain any characters except for “[” and “]”.
3. Click Save button at the top, then click OK in the confirmation
   pop-up.

   > Note: User must save the assignments before moving to another page or another group in the Middle Panel.

Note: Within a table or view, the aliases cannot be duplicated.

[![../_images/Data_Model_Duplicated_Column_Alias.png](https://devnet.logianalytics.com/hc/article_attachments/4415511754903/data_model_duplicated_column_alias_702x201.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492494743/data_model_duplicated_column_alias.png)

## Select visible or not for a column in table, view or stored procedure

A visible column will be included in any field selection control in
report.

1. Untick the Visible check-box to exclude the column from field
   selection controls in report, or leave it checked to include.
2. Continue for more columns in the same page.
3. Click Save button at the top, then click OK in the confirmation
   pop-up.

   > Note: User must save the changes before moving to another page or another group in the Middle Panel.

## Select filterable or not for a column in table, view or stored procedure

A filterable (and visible) column will be included in any filter in
report.

Note: A not visible column will be excluded from any filter in report no matter it is filterable or not.

1. Untick the Filterable check-box to exclude the column from filters in
   report, or leave it checked to include.
2. Continue for more columns in the same page.
3. Click Save button at the top, then click OK in the confirmation
   pop-up.

   > Note: User must save the changes before moving to another page or another group in the Middle Panel.

## Update Filter Value for a table/view field or a stored procedure parameter

This feature are only available for tables/views’ fields from version 2.14.0

1. Click the icon in Filter Value box.

   Note*:* For Store Procedures, Filter Value icon only appears for parameters.
2. Select either Filter Lookup Key - Value or User Defined Filter Value

   * Example to set
     parameter @OrderID to look up from NorthwindA.dbo.Orders.OrderID,
     displaying column ShipName to end-user.

     [![../_images/Data_Model_SP_Filter_Lookup_Key_-_Value.png](https://devnet.logianalytics.com/hc/article_attachments/4415492495511/data_model_sp_filter_lookup_key_-_value_458x311.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504407959/data_model_sp_filter_lookup_key_-_value.png)
   * Example to set
     parameter @OrderID to look up from a list of 3 values: the value
     of Tenant ID and 2 fixed values NewValueA and NewValueB.

     [![../_images/Data_Model_SP_User_Defined_Filter_Value.png](https://devnet.logianalytics.com/hc/article_attachments/4415504408983/data_model_sp_user_defined_filter_value_458x220.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504408215/data_model_sp_user_defined_filter_value.png)
3. The selected filter value will appear in the Filter Value box.

   ![../_images/Data_Model_SP_View_User_Defined_Filter_Value.png](https://devnet.logianalytics.com/hc/article_attachments/4415511756311/data_model_sp_view_user_defined_filter_value_245x55.png)
4. Click Save button at the top, then click OK in the confirmation
   pop-up.

## Add a calculated field to table or view

Calculated field

Calculated field is a virtual field calculated from an expression that can use other fields in the same table or view. A calculated field is created to simplify the select queries by hiding the detailed formula, and the formula can be replaced without any change in existing queries. A calculated field will also avoid data redundancy since it is re-calculated in each query.

For example, from a student test score, the grade can be calculated by this formula:

```
WHENscore>=0ANDscore<7THEN'GOOD'WHENscore>=7ANDscore<9THEN'EXCELLENT'WHENscore>=9THEN'OUTSTANDING'
```

If defined as a calculated field, the grade can later use another formula without changing any queries.

Note: Calculated fields cannot be used in relationships between tables or views.

See also: [Computed Columns](https://technet.microsoft.com/en-us/library/ms191250(v=sql.105).aspx)

1. Select the table or view in the upper data source grid.
2. Click Add Field button on top of the Column Grid to open Add
   Calculated Field pop-up.
3. Enter the field name
   into Column Name box.

   > The field name must be unique in that table or view.
   >
   > [![../_images/Data_Model_Calculated_Field_Duplicated_Name.png](https://devnet.logianalytics.com/hc/article_attachments/4415504409879/data_model_calculated_field_duplicated_name_456x89.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492498711/data_model_calculated_field_duplicated_name.png)
4. Enter the
   definition for the calculated field into Expression box.

   > Click the bulb icon (💡) to see the list of available fields,
   > functions and operators.
   > Then click a field, function or operator to insert it into the
   > cursor position.
   >
   > [![../_images/Data_Model_Calculated_Field_Bulb_Pop-up.png](https://devnet.logianalytics.com/hc/article_attachments/4415504410263/data_model_calculated_field_bulb_pop-up_518x475.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492498967/data_model_calculated_field_bulb_pop-up.png)
5. Depending on the
   formula, a suitable data type is suggested in Data Type drop-down.
6. Click Preview button to see a sample result of the formula.
7. Click OK to accept the formula and close the pop-up.

   ![../_images/Data_Model_Calculated_Field_FirstName_WhiteSpace_LastName.png](https://devnet.logianalytics.com/hc/article_attachments/4415504410647/data_model_calculated_field_firstname_whitespace_lastname_456x346.png)
8. Click Save at the top.

See also:

* [Izenda Data Types](https://devnet.logianalytics.com/hc/en-us/articles/4415492762135-Izenda-Data-Types)
* [Izenda Operators](https://devnet.logianalytics.com/hc/en-us/articles/4415492763031-Izenda-Operators)
* [Izenda Functions](https://devnet.logianalytics.com/hc/en-us/articles/4415504688663-Izenda-Functions)

## Remove a calculated field from table or view

1. Select the table or view in the upper data source grid.
2. Click the remove icon (X) at the end of the calculated field.

   > The remove icon is only enabled for calculated fields.
   >
   > [![../_images/Data_Model_Calculated_Field_Remove_Icon.png](https://devnet.logianalytics.com/hc/article_attachments/4415492499223/data_model_calculated_field_remove_icon_1026x189.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504411031/data_model_calculated_field_remove_icon.png)
3. Click OK in the confirmation pop-up.

   > If the calculated field has been used in any report, user will
   > have to confirm that these reports will not be viewable anymore.
4. Click Save at the top.

## Set stored procedure as dynamic

For stored procedures with any input parameter, they can be set as
dynamic.

Dynamic stored procedure

A stored procedure with one (or more) input parameter might have different output schemas based on the value of that input parameter. The reports have 2 options to handle this situation:

* Dynamic: The schema is only determined at report design time by a user-supplied input value.
  :   The schema is empty in Data Model.
* Non-dynamic: The schema is assumed to remain consistent regardless of the input value.
  :   System can try getting that schema for Data Model by executing with null input parameters. In case it cannot because any parameter requires NOT NULL, user will be prompted for a proper input value.

      The exact rule for NOT NULL input parameters:

      1. If Filter Value has been defined for a parameter, the first value in that list will be used as input value.
      2. If not, then null will be used as input value.

Non-dynamic should be the default value since in practice, well-coded stored procedures should return a consistent schema.

1. Tick the Dynamic check-box to set a stored procedure as dynamic.
2. Click OK in the confirmation pop-up.

![../_images/Data_Model_SP_Set_Dynamic_Confirmation.png](https://devnet.logianalytics.com/hc/article_attachments/4415504411415/data_model_sp_set_dynamic_confirmation_456x149.png)

1. Click Save button at the top, then click OK in the confirmation
   pop-up.
2. The stored procedure will be set as dynamic and its schema will be
   removed from the lower Column Grid. The Execute button is also
   disabled.

## Set stored procedure as non-dynamic

1. Untick the Dynamic check-box to set a stored procedure as
   non-dynamic.
2. Click Save button at the top, then click OK in the confirmation
   pop-up.
3. The stored procedure will be set as non-dynamic. The Execute button
   is also enabled for user to get the schema.

## Execute a non-dynamic stored procedure to get the schema

1. Click the Execute button above the lower Column Grid.
2. System tries running the stored procedure to get the schema.
3. The schema will be populated into the lower Column Grid.
4. Click Save button at the top, then click OK in the confirmation
   pop-up.

The action will fail if one of the parameters requires not null and
Filter Value has not been defined.

In this case, please update the Filter Value section.
