---
title: "DataLayer.SQL - Attributes"
id: 4419707505047
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707505047-DataLayer-SQL-Attributes
updated_at: 2022-07-17T01:52:51Z
---

# DataLayer.SQL - Attributes

# DataLayer.SQL - Attributes

The DataLayer.SQL element has the following attributes:

| Attribute | Description |
| --- | --- |
| Source | (Required) Specifies the SQL statement to be executed. Typically this is a SQL query, e.g. SELECT \* FROM *MyTable*. However, multi-line SQL statements, including queries and statements like DECLARE, can be entered into the Attribute Zoom window for this attribute and will run correctly. Tokens may be used here so, for example, you could create a constant (in the \_Settings definition) to hold your query text, then use a token like @Constant.myQuery~ in this attribute. That would allow you to maintain the query in a single place, while using it in multiple datalayers. EXECUTE statements can be entered here as well, though use of stored procedures via the [DataLayer.SP](https://devnet.logianalytics.com/hc/en-us/articles/4419715229335-DataLayer-SP) element is recommended instead. When a connection to a non-OLAP datasource is being used, the Browse button for this attribute can be used to launch the SQL Query Builder wizard. If an OLAP connection is being used, the Browse button can be used to launch the MDX Query Builder. See the SQL Query Builder and MDX Query Builder sections of our [Using Logi Studio](https://devnet.logianalytics.com/hc/en-us/articles/4419707934103-Using-Logi-Studio) for more information on these topics. |
| ID | Specifies a unique element ID. Providing a value here is *highly recommended* for easier identification of data when debugging. |
| Connection ID | Specifies the ID of a database Connection element defined in the \_Settings definition. If this value is left blank, the datalayer will use the *first* connection in the \_Settings definition. For clarity, developers are advised to enter an ID here in all cases. |
| Handle Quotes Inside Tokens | Specifies how to handle any single-quotes found in token values used to form part of the SQL statement in the Source attribute. When *True*, it ensures SQL syntax validity by **doubling** any single-quotes found. For example, imagine the SQL statement "SELECT \* FROM Customers WHERE CompanyName LIKE '%@Request.Name~%' ". If the value of the Request token is "Trail's Head", the embedded single-quote could be problematic. With the HandlesQuotesInTokens attribute set to *True*, the SQL statement sent to the database server will become "SELECT \* FROM Customers WHERE CompanyName LIKE '%Trail''s Head%' ". Default: *False* |
| Maximum Rows | Specifies the maximum number of results rows to retrieve. Default: no limit. |
