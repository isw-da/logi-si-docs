---
title: "Database Problems"
id: 4406817901463
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817901463-Database-Problems
updated_at: 2022-04-06T06:08:55Z
---

# Database Problems

# Database Problems

This topic introduces the different types of database problems you could run into when developing Logi Studio, as well as possible solutions.

Problems Connecting to Database

* If using non-native connections (JDBC, ODBC, OLEDB, etc.) confirm that
  the Connection String has a valid DataSource value.
* Confirm that the database server is started and accessible via the
  network.
* Check that the password is being saved in the database connection
  string. This must be part of the connection string to ensure that a
  connection is established.
* If connecting to a database via OLEDB, make sure to use the appropriate
  provider. For SQL Server, this is the SQL Server Provider. If you have a
  choice of OLEDB or ODBC providers, we recommend using the OLEDB provider
  for all databases. For help creating an OLEDB connection string, use the
  "Connection String" wizard.
* If using a native Connection element, ensure that you're using the right
  one. For example, there is a Connection.MySql element for use with MySQL
  databases, Connection.SqlServer for MS SQL Server, etc.

Creating a Single Result Set From Two Databases:

* When JOINing tables, ensure that SELECT statements avoid ambiguous
  results by qualifying column names with table identifiers.
* A UNION of query results can be created by adding additional datalayers
  to elements like the Data Table element. This will combine the results
  into a single result set.
