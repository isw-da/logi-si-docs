---
title: "DataLayer.ActiveSQL - DataLayer.ActiveSQL Attributes"
id: 4406817276823
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817276823-DataLayer-ActiveSQL-DataLayer-ActiveSQL-Attributes
updated_at: 2022-04-06T06:05:06Z
---

# DataLayer.ActiveSQL - DataLayer.ActiveSQL Attributes

# DataLayer.ActiveSQL - DataLayer.ActiveSQL Attributes

The DataLayer.ActiveSQL element has the following attributes:

| Attribute | Description |
| --- | --- |
| Source | (Required) Specifies the initial SQL query to be executed, for example SELECT \* FROM *MyTable*. This query will be modified dynamically by the datalayer as its parent element's user interface is manipulated.  If other elements allow the user to dynamically affect the data, queries should *not* include an **ORDER BY** clause. Use a SQL Sort element instead. Also, SQL queries that include a form of the **JOIN** clause should individually list all of the desired field names in the SELECT clause. Queries that don't include a JOIN clause can use the asterisk (\*), if desired.  **Tokens** can be used, for example, in WHERE clauses, to create dynamic queries.  The Browse button for this attribute can be used to launch the **Query Builder** wizard. |
| ActiveSql Buffer Size | Specifies the maximum number of rows to buffer locally. Customizing this value can help performance when the data includes a large number of columns. Default value: *5,000 rows* |
| Connection ID | Specifies the ID of a **Connection.Oracle**, **Connection.MySQL**, **Connection.SqlServer** (to MS SQL Server 2005+), **Connection.PostgreSQL, Connection.DB2,** **Connection.Redshift, or Connection.Vertica** element defined in the \_Settings definition. Other connection types *will not work*. If left blank, the top-most Connection element defined will be used by default. |
| Handle Quotes Inside Tokens | Specifies how to handle any single-quotes found in token values used to form part of the SQL statement in the Source attribute. When *True*, it ensures SQL syntax validity by **doubling** any single-quotes found.  For example, imagine the SQL statement "SELECT \* FROM Customers WHERE CompanyName LIKE '%@Request.Name~%' ". If the value of the Request token is "Trail's Head", the embedded single-quote could be problematic. With the HandlesQuotesInTokens attribute set to *True*, the SQL statement sent to the database server will become "SELECT \* FROM Customers WHERE CompanyName LIKE '%Trail''s Head%' ".  Default: *False* |
| ID | Specifies a unique element ID. Providing a value here is *highly recommended* for easier identification of data when debugging. |
| Maximum Rows | The maximum number of rows to retrieve from the data source, per request.  Default: *5,000 rows*  The default was changed to *200 rows* or, if pagination is being used, *10 pages*, whichever is greater. |
