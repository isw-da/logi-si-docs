---
title: "Logi OLAP - Using Two-Dimensional Data"
id: 4419723023767
section: "Elements - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723023767-Logi-OLAP-Using-Two-Dimensional-Data
updated_at: 2022-07-17T01:44:15Z
---

# Logi OLAP - Using Two-Dimensional Data

# Logi OLAP - Using Two-Dimensional Data

It's possible to use two-dimensional data from SSAS
cubes for use in standard Data Tables, charts and other visualizations.
This is done using **Connection.OLEDB** and **DataLayer.SQL** with
an MDX query statement in its Source attribute. Unlike your
Connection.OLAP configuration, the connection string for Connection.OLEDB
will need to include the User ID and Password needed to log into the
database.
Logi Studio includes a tool, the
MDX Query Builder, that can help you construct such a query for use with DataLayer.SQL.
For more information, see [The MDX Query Builder](https://devnet.logianalytics.com/hc/en-us/articles/4419715550359-The-MDX-Query-Builder).
