---
title: "PostgreSQL v8 Object Case Sensivity"
id: 4419715036439
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715036439-PostgreSQL-v8-Object-Case-Sensivity
updated_at: 2022-07-17T02:03:06Z
---

# PostgreSQL v8 Object Case Sensivity

# PostgreSQL v8 Object Case Sensivity

Here's an interesting fact about **PostgreSQL** v.8 schemas: for some
Catalog normalization requirements within the PostgreSQL DB engine, all
object names should be referenced in *lower-case* from Logi
applications, including database, table, and column names. For instance:

SELECT productname, productid FROM products

Under normal circumstances, the query shown above is valid,

SELECT ProductName, ProductId FROM Products

but the second one is not.   
However, it is possible to define objects that have mixed- or upper-case
names. If you encounter a DB where this is the case, then you may use
mixed- or upper-case names in your queries, *if* you wrap object
names with double-quotes:

SELECT "ProductName", "ProductId" FROM
"Products"

as shown above.
Perhaps the most noticeable impact will be with the functioning of Logi
Studio's **Query Builder** and **Database Browser** tools. Neither
tool will wrap object names in double-quotes and will therefore fail to
work if you have any upper-case characters within the table, view, or
database list.
