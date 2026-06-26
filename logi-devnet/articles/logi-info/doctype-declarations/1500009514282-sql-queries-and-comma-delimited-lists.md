---
title: "SQL Queries and Comma-Delimited Lists"
id: 1500009514282
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514282-SQL-Queries-and-Comma-Delimited-Lists
updated_at: 2021-06-17T01:58:05Z
---

# SQL Queries and Comma-Delimited Lists

# SQL Queries and Comma-Delimited Lists

Developers may encounter a need to pass in, as a single parameter, a **comma-delimited list** of values to a SQL query or stored procedure. Unfortunately, SQL parameters don't have a way to represent comma-delimited lists. Here are two solutions, one for MS SQL Server and the other for Oracle, that solve this problem, using a sub-query and the IN search qualifier respectively.

The following query is for MS SQL Server, where @sel\_customers is the parameter with the delimited list of values:

|  |  |
| --- | --- |
|  | -- my stored procedure     @sel\_customer varchar(200)   -- this is the parameter     SELECT SalesOrderID, OrderDate, CustomerID     FROM AdvWorks.Sales.SalesOrderHeader     WHERE CustomerID IN      (SELECT CustomerID FROM AdvWorks.Sales.Customer WHERE CHARINDEX(STR(CustomerID), @sel\_customers) > 0) |

With this technique, the SQL statement does not vary between executions and will therefore be cached. By putting the expression into a sub-query, the DBMS optimizer will only execute it once (because it's not correlated). Since the sub-query just accesses a lookup table, the speed will be very fast as opposed to evaluating the expression for each row of the primary query table.

The example above shows a query in a stored procedure, but the same query could be used by itself, replacing the parameter with an @Request token.

Here's a similar query for use with an Oracle DB:

|  |  |
| --- | --- |
|  | SELECT ACTIVITY\_ID, CODE\_VALUE, CATEGORY\_ID,     FROM SYSADM.ACTIVITY\_TYPE     WHERE CATEGORY\_ID IN      (SELECT CATEGORY\_ID      FROM SYSADM.ACTIVITY\_CATEGORY      WHERE instr(:@sel\_ActivityCategories, '''' || to\_char(CATEGORY\_ID) || '''') > 0 ) |

This sub-query is slightly more complex because quotes are needed around the search argument (CATEGORY\_ID) in order to prevent partial key matches (e.g. the key value '1' is part of the key '123'). This isn't an issue in MS SQL Server because Microsoft conveniently adds a space at the beginning of the number for sign, therefore eliminating partial key matches.

[![](https://logianalytics.zendesk.com/hc/article_attachments/4402778391063/totop.gif)](#)  [Back to the top](#)
