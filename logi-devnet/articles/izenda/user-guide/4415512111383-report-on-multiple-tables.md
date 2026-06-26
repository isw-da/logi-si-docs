---
title: "Report on Multiple Tables"
id: 4415512111383
section: "User Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415512111383-Report-on-Multiple-Tables
updated_at: 2021-12-10T03:10:44Z
---

# Report on Multiple Tables

# Report on Multiple Tables

Data required for a report does not always come from a single table,
there are scenarios where multiple tables are needed.

## Reports on two tables with direct relationship

In this scenario, data needed for a report does not come from one single
table, but from a primary table and a related one. The primary table
must have a field to contain the id value of the related table. Both
tables simply need to be selected for the report to work.

[![../_images/NW_Order_Details_ProductID_Discount_Desc.png](https://devnet.logianalytics.com/hc/article_attachments/4415504542743/nw_order_details_productid_discount_desc_135x213.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492618007/nw_order_details_productid_discount_desc.png)

For example, table Order
Details in Northwind database stores the list of products (ProductID)
together with the discount percentage in each order. This data allows
for a report on products with the highest discount percentage. However,
that report can only show the meaningless product IDs.

[![../_images/NW_Order_Details_ProductID_ProductName_Discount_Desc.png](https://devnet.logianalytics.com/hc/article_attachments/4415511867927/nw_order_details_productid_productname_discount_desc_212x209.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492618263/nw_order_details_productid_productname_discount_desc.png)

The report will be more
useful if it includes the product name (stored inside table Products). To do that:

1. Select both tables Order Details and Products in Middle Panel.
2. Define relationship between two tables if needed (See [Add and remove relationships](https://devnet.logianalytics.com/hc/en-us/articles/4415504846743-Report-Designer-Data-Source#Add))
   (in this case the relationship has already been defined and
   automatically populated).
3. Add a Grid report part.
4. In Columns box, use the ProductName field instead of ProductID.

   > In the screenshot below, the ProductID is intentionally kept to be compared with the previous figure.

   [![../_images/NW_Order_Details_Products_Relationship.png](https://devnet.logianalytics.com/hc/article_attachments/4415492619031/nw_order_details_products_relationship_968x178.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492618647/nw_order_details_products_relationship.png)

## Reports on two tables with relationships via a third table

Sometimes, data in two tables are related to each other through a third
table (many-to-many relationship). These two tables have no direct
relationship, so a report with these two tables only will not work: all
three tables need to be selected.

Note: A rule of thumb to detect this scenario is that the third table usually has only two fields, each contains the id value of either related table.

For example, a report is needed for the total sales per year in each of
two cities Rio de Janeiro and Sao Paulo. The city values are in City
field in Customers table while the sales are calculated from UnitPrice,
Quantity and Discount fields in Order Details table. These tables are
linked to each other by the Orders table although no field from this
table is needed for the calculation. To design this report:

1. Select all three tables Customers, Order Details and Orders.
2. Define relationships if needed (See [Add and remove relationships](https://devnet.logianalytics.com/hc/en-us/articles/4415504846743-Report-Designer-Data-Source#Add))
   (in this case the relationship has already been defined and
   automatically populated).
3. Drag the City field in Customers table into the Filter box.
4. Click the City field in Filter box to open Filter Properties.
5. Go to Filter Settings group, Filter Operator drop-down, select
   Equivalence then Equals (Manual Entry) then Multiple.
6. Type Rio de Janeiro and press Enter.
7. Type Sao Paulo and press Enter.
8. In Middle Panel, click Add Calculated Field to open Add Calculated
   Field pop-up.
9. Name the field “Sales”.
10. Build the expresion

    ```
    [Northwind].[dbo].[OrderDetails].[UnitPrice]*[Northwind].[dbo].[OrderDetails].[Quantity]-[Northwind].[dbo].[OrderDetails].[UnitPrice]*[Northwind].[dbo].[OrderDetails].[Quantity]*[Northwind].[dbo].[OrderDetails].[Discount]
    ```
11. Click Ok to save the calculated field.
12. Add a Grid report part.
13. In Columns box, add the City field and the Sales calculated field.
14. Select City field in Columns box to open Field Properties.
15. Select “Group” as Function.
16. Select Sales field in Columns box to open Field Properties.
17. Select “Sum” as Function.
18. Select descending as Sort.
