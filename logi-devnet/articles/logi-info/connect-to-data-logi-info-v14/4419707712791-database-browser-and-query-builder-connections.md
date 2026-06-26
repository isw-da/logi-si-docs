---
title: "Database Browser and Query Builder Connections"
id: 4419707712791
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707712791-Database-Browser-and-Query-Builder-Connections
updated_at: 2022-07-17T01:43:19Z
---

# Database Browser and Query Builder Connections

# Database Browser and Query Builder Connections

The Database Browser and Query Builder tools *will* work with the databases for which we provide "native" Connection elements, such as Oracle\*, MS SQL Server, and MySQL. They *may* work with other databases that use a connection that mimics that of a database for which we provide a native connection, such as PostgreSQL. They are not guaranteed to
work with every possible database and, in that case, we recommend that you use tools provided with the database to examine and manipulate data, and create and test queries, outside of Studio.

\* Due to the way in which Oracle configures its software, the Database Browser and Query Builder will *not* connect, using our native Connection.Oracle element, to Oracle databases when Logi Studio is run on a 64-bit platform. In this situation, developers can choose to do without these tools or to use Connection.ODBC to connect.
