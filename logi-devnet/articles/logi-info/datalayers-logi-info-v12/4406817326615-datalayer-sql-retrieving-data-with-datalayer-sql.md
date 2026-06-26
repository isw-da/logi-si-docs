---
title: "DataLayer.SQL - Retrieving Data with DataLayer.SQL"
id: 4406817326615
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817326615-DataLayer-SQL-Retrieving-Data-with-DataLayer-SQL
updated_at: 2022-04-06T06:05:24Z
---

# DataLayer.SQL - Retrieving Data with DataLayer.SQL

# DataLayer.SQL - Retrieving Data with DataLayer.SQL

The datalayer receives and caches the results returned by a SQL query or statement. You can add child elements beneath the datalayer to affect the results, including:

* **Filtering**: Sort, group, or restrict the result data
* **Joining**: Apply SQL JOINs to the data in the datalayer
* **Extending**: Add virtual columns to the datalayer that contain aggregated, calculated, or totaled result values
* **Securing**: Limit access to the data using Logi security
* **Linking**: Make the results reusable elsewhere in your report definitions

Data retrieved into the datalayer is cached in **XML** format, in memory and/or on the web server's file system. The latter is discussed in [The Logi Server Engine](https://devnet.logianalytics.com/hc/en-us/articles/4406817743895-The-Logi-Server-Engine) and may be of interest to developers working with extremely large datasets or large numbers of concurrent users.

The data retrieved with a datalayer is available using @Data **tokens**, in the format @Data.*ColumnName*~. The spelling of the column name is *case-sensitive*. The data is only available within the scope of the parent element of the datalayer, not throughout the entire report definition. The **DataLayer.Linked** element can be used to make the data reusable in another datalayer outside this scope.

The [Auto Columns](https://devnet.logianalytics.com/hc/en-us/articles/4406822055959-Auto-Columns) element can be used to quickly display in your report all the data in a datalayer.

The data retrieved into the datalayer can be viewed by turning on the Debugger Trace page in your \_Settings definition (General element) and using the resulting link at the bottom of your report page to view the data.
