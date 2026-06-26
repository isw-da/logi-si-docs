---
title: "DataLayer.SQL - Using SQL Parameters"
id: 4419722844951
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722844951-DataLayer-SQL-Using-SQL-Parameters
updated_at: 2022-07-17T02:24:37Z
---

# DataLayer.SQL - Using SQL Parameters

# DataLayer.SQL - Using SQL Parameters

The **SQL Parameters** and **SQL Parameter** elements can be used to include tokenized parameters, if you prefer not to embed tokens directly into the SQL statement. This approach also allows you to enforce a data type for the parameter value and also offers protection against SQL Injection attacks.

To use parameters, you write your SQL statement using "placeholder" notation. The exact syntax depends on your database *and* the Connection element you're using. For example, if you're using **Connection.SQLServer**, you use this notation:

SELECT \* FROM Customers WHERE State=@state AND City=@city

and the **ID** attribute of each SQL Parameter element must match a placeholder *name*. So, in the example, the value of an element with an ID of *state* will replace the @state placeholder at runtime.

Similarly, if you're using **Connection.Oracle**, you use this notation:

SELECT \* FROM Customers WHERE State=:state AND City=:city

and, as before, the **ID** attribute of each SQL Parameter element must match a placeholder *name*.  
If you're using **Connection.OLEDB**, you use this notation:

SELECT \* FROM Customers WHERE State=? AND City=?

Unlike the previous examples, these are *positional* parameters so, at runtime, placeholders in the statement will be replaced, starting with the first placeholder, by the values specified in the SQL Parameter elements, based on the elements' *top-to-bottom order* in the definition. The element IDs are ignored.

![](https://devnet.logianalytics.com/hc/article_attachments/7522801241623/dlsql_02a.png)

The example above illustrates the relationship, in this scenario, between SQL Parameter element order and placeholders in the statement.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) SQL Parameters will not work when using **Connection.ODBC**.
Consult your database documentation for its specific placeholder syntax.
