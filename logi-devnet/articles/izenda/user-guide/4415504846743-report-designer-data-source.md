---
title: "Report Designer/Data Source"
id: 4415504846743
section: "User Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415504846743-Report-Designer-Data-Source
updated_at: 2022-09-07T17:24:47Z
---

# Report Designer/Data Source

# Report Designer/Data Source

The **Report Designer/Data Source** page allows user to

* view, search and select data sources to be used in a report
* set up and validate relationships between data sources in a report

![../_images/Report_Designer.png](https://devnet.logianalytics.com/hc/article_attachments/4415504458519/report_designer.png)

## View data sources

1. In browser, log in to Izenda as a user with Report permission.
2. Click New, then Data Source in the left menu.

   ![../_images/Report_Designer_Data_Source_Location.png](https://devnet.logianalytics.com/hc/article_attachments/4415492551063/report_designer_data_source_location_481x215.png)
3. Visible tables, views, or stored procedures from all connections will
   be displayed in the Middle Panel.

   > The categories are expanded by default so the user can see the data sources inside. The user can collapse each category to provide additional screen real estate to uncollapsed categories.
   >
   > ![../_images/Report_Designer_Data_Source_Middle_Panel.png](https://devnet.logianalytics.com/hc/article_attachments/4415511804951/report_designer_data_source_middle_panel_224x314.png)

Note: In Report Designer, it is recommended to collapse the left menu to have maximum screen space for the design.

![../_images/Report_Designer_Collapse_Left_Menu.png](https://devnet.logianalytics.com/hc/article_attachments/4415504458903/report_designer_collapse_left_menu_197x188.png)

## Search for data sources

The list of data
sources can grow very big over time. In this case, the Search box will
help user to quickly find specific items.

1. Type a partial name and click the search icon (🔍).
2. Only data sources with matching names or matching field names will be
   displayed.

![../_images/Report_Designer_Data_Source_Middle_Panel_Search.png](https://devnet.logianalytics.com/hc/article_attachments/4415511805207/report_designer_data_source_middle_panel_search_224x326.png)

## Select and unselect data sources

1. Tick the checkbox on the right of data sources to select them.

   > Existing relationships between selected data sources will be
   > automatically added to the relationship list in Content Panel.
2. Untick the checkbox on the right of data sources to unselect them.

   > Relationships with unselected data sources will be automatically
   > removed from the relationship list in Content Panel.
   >
   > ![../_images/Report_Designer_Select_Data_Source.png](https://devnet.logianalytics.com/hc/article_attachments/4415492551447/report_designer_select_data_source_198x365.png)

Note: Izenda supports using stored procedures as data sources. Just make sure that the account in connection string has necessary permissions for this case, see [Connector Permissions](https://devnet.logianalytics.com/hc/en-us/articles/4415504839575-Data-Connectors#connection-permissions).

## Set the report as Distinct

The Distinct checkbox on top of Middle Panel if ticked will force the
report to return unique values only.

Leave it unticked to allow duplicated values in the result.

## Set the number of preview records

The amount of data in preview panel under the relationship list can be
configured by selecting from Preview Records drop-down at the top.

## Save the report

1. Click Save button at the top to open the Save pop-up.

   > If the report has been saved already then there is another option
   > to Save As a new one.
   >
   > ![../_images/Report_Designer_Save_As.png](https://devnet.logianalytics.com/hc/article_attachments/4415492551703/report_designer_save_as_138x88.png)
2. Enter the name for the report in Report Name box.
3. Select to save as Templates.

   > The option to save as Reports is only available after any field
   > is defined in [Report Designer/Design](https://devnet.logianalytics.com/hc/en-us/articles/4415492934039-Report-Designer-Design) page.
4. Select a category for the report in Category drop down.

   * Type a partial name to quickly search for the category.

     ![../_images/Report_Designer_Save_Quick_Search_Category_Name.png](https://devnet.logianalytics.com/hc/article_attachments/4415504459287/report_designer_save_quick_search_category_name_458x273.png)
   * A new category can be created in-place by typing the name in and
     pressing Enter.

     ![../_images/Report_Designer_Save_With_New_Category.png](https://devnet.logianalytics.com/hc/article_attachments/4415492552471/report_designer_save_with_new_category_458x270.png)
   * Click the x icon to clear the existing one.

     ![../_images/Report_Designer_Save_Clear_Category.png](https://devnet.logianalytics.com/hc/article_attachments/4415492552727/report_designer_save_clear_category_431x66.png)
5. Similarly select a sub-category for the report in Sub-Category drop
   down.
6. Click OK to save the report.

   > The report name will be invalid if it has been given to another
   > report in the same category
   >
   > [![../_images/Report_Designer_Save_Duplicated_Name.png](https://devnet.logianalytics.com/hc/article_attachments/4415511805975/report_designer_save_duplicated_name_458x271.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511805719/report_designer_save_duplicated_name.png)
   >
   > including Uncategorized.
   >
   > [![../_images/Report_Designer_Save_Duplicated_Name_Uncategorized.png](https://devnet.logianalytics.com/hc/article_attachments/4415492553239/report_designer_save_duplicated_name_uncategorized_458x271.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504459799/report_designer_save_duplicated_name_uncategorized.png)

## Add and remove relationships

To run a report from more than one table, relationships among the tables
must be available or defined to join the tables together.

* With most properly designed databases, relationships are already
  available, so after selecting data sources the relationship list will
  have been fully populated.
* However, relationships need to be defined for some cases such as ad
  hoc queries or cross database joins.

For example, from Northwind database, user needs an ad hoc report to
find out if any supplier happens to be in one of the territories. The
join that user needs to build is
`[Suppliers].[City]=[Territories].[TerritoryDescription]`.

1. Select Suppliers and Territories in the Middle Panel.
2. The relationship list remains empty and the report cannot be saved.
3. Click Add Relationship button, a blank new row is inserted into the
   list.
4. Select Inner in Join Type drop-down.
5. Select values in Category, Data Object, Join Field, then Category,
   Foreign Data Object and Field in left-to-right sequence for data to
   populate correctly.
6. Select data so that the row reads:
   `|Category|Suppliers|City|=|Category|Territories|TerritoryDescription|`
7. Click Validate Syntax button and see success message.

   [![../_images/Report_Designer_Data_Source_Validate_Syntax_Success.png](https://devnet.logianalytics.com/hc/article_attachments/4415492554007/report_designer_data_source_validate_syntax_success_365x47.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492553495/report_designer_data_source_validate_syntax_success.png)

To quickly add relationship, user can copy an existing one then modify
it by clicking the Copy icon (that looks a bit like this ❐).

No longer needed relationships can also be removed by clicking the
Remove icon (X).

See also:

* [Wikipedia: Join](https://en.wikipedia.org/wiki/Join_(SQL))
* [Report on Multiple Tables](https://devnet.logianalytics.com/hc/en-us/articles/4415512111383-Report-on-Multiple-Tables)

## Add Key Join Relationship

A single column is needed for the example join above. There are rare
cases when multiple columns are needed in a join. For example, from
Northwind database, user needs an ad hoc report to list out the products
that are used in a single order. One way to do that is to compare the
Quantity in the order with the UnitsOnOrder of the product. The join
that user needs to build is
`[OrderDetails].[ProductID]=[Products].[ProductID]AND[OrderDetails].[Quantity]=[Products].[UnitsOnOrder]`.

1. Select Order Details and Products in the Middle Panel.
2. The relationship list is
   populated with the existing relationship
   `[OrderDetails].[ProductID]=[Products].[ProductID]`.
3. Click the Add Key Join icon in Action, a blank new row is inserted
   under that existing relationship.

   [![../_images/NW_Order_Details_Product_Add_Key_Join.png](https://devnet.logianalytics.com/hc/article_attachments/4415492554263/nw_order_details_product_add_key_join_600x64.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511806231/nw_order_details_product_add_key_join.png)
4. Select values in Operator, Category, Data Object, Join Field, then
   Category, Foreign Data Object and Field in left-to-right sequence for
   data to populate correctly.
5. Select data so that the row reads:
   `|And|OrderDetails|Quantity|=|Products|UnitsOnOrder|`
6. Click Validate Syntax button and see success message.

   [![../_images/NW_Order_Details_Product_Key_Join_Quantity_UnitsOnOrder.png](https://devnet.logianalytics.com/hc/article_attachments/4415504460183/nw_order_details_product_key_join_quantity_unitsonorder_600x65.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492554647/nw_order_details_product_key_join_quantity_unitsonorder.png)

## Add Join Alias

The joined tables can be given alias to be referred to in subsequent join clauses.

* For example, to get data of Products and related Categories and Suppliers, the [Products] table needs to be joined with:

  + [Categories] table `[Products].[CategoryID]=[Categories].[CategoryID]`
  + [Suppliers] table `[Products].[SupplierID]=[Suppliers].[SupplierID]`

  The [Products] table is used twice and therefore should be given an alias as below:

  [![../_images/Table_Alias_Products_Categories_Suppliers.png](https://devnet.logianalytics.com/hc/article_attachments/4415511806487/table_alias_products_categories_suppliers_900x198.png)](https://devnet.logianalytics.com/hc/article_attachments/4415504460439/table_alias_products_categories_suppliers.png)

  That is equivalent to the following SQL statement:

  ```
  SELECT*FROM[Products]ASPRDINNERJOIN[Categories]ONPRD.[CategoryID]=[Categories].[CategoryID]INNERJOIN[Suppliers]ONPRD.[SupplierID]=[Suppliers].[SupplierID]
  ```
* Effects of alias in a key join: if the original table is given an alias, that alias must be selected in the key join.

  [![../_images/Table_Alias_Key_Join_OrderDetails_Products.png](https://devnet.logianalytics.com/hc/article_attachments/4415511806999/table_alias_key_join_orderdetails_products_900x180.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511806743/table_alias_key_join_orderdetails_products.png)

  Fig. 182 The alias OD must be selected instead of the original table name Order Details

  That is equivalent to the following SQL statement:

  ```
  SELECT*FROM[OrderDetails]ASODINNERJOIN[Products]ONOD.[ProductID]=[Products].[ProductID]ANDOD.[Quantity]=[Products].[UnitsOnOrder]
  ```
* An alias is also required in case of a self-join. For example, [Employees].[ReportsTo] is foreign key to [EmployeesID] in the same table, hence, an alias must be given to differentiate the two different [Employees] tables.

  [![../_images/Table_Alias_Self_Join_Employees.png](https://devnet.logianalytics.com/hc/article_attachments/4415511807255/table_alias_self_join_employees_900x59.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492554903/table_alias_self_join_employees.png)

  That is equivalent to the following SQL statement:

  ```
  SELECT*FROM[Employees]ASSubordinateINNERJOIN[Employees]ONSubordinate.[ReportsTo]=[Employees].[EmployeeID]
  ```
