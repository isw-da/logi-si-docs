---
title: "DataLayer.LDAP - Working with DataLayer.LDAP"
id: 4419722830743
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722830743-DataLayer-LDAP-Working-with-DataLayer-LDAP
updated_at: 2022-07-17T01:53:13Z
---

# DataLayer.LDAP - Working with DataLayer.LDAP

# DataLayer.LDAP - Working with DataLayer.LDAP

The datalayer receives and **caches** the results returned by the LDAP query statement. You can add **child elements** beneath the datalayer to affect the results, including:

* **Filtering**: Sort, group, or restrict the result data
* **Joining**: Apply SQL-like JOINs to the data in the datalayer
* **Extending**: Add virtual columns to the datalayer that contain aggregated, calculated, or totaled result values
* **Securing**: Limit access to the data using Logi security
* **Linking**: Make the results reusable elsewhere in your report definitions

Data retrieved into the datalayer is cached in **XML** format, in memory and/or on the web server's file system. The latter is discussed in [The Logi Server Engine](https://devnet.logianalytics.com/hc/en-us/articles/4419715421975-The-Logi-Server-Engine) and may be of interest to developers working with extremely large datasets or large numbers of concurrent users.

The data retrieved with a datalayer is available using @Data **tokens**, in the format @Data.*ColumnName*~. The spelling of the column name is **case-sensitive**. The data is only available within the **scope** of the **parent** element of the datalayer, not throughout the entire report definition. The **DataLayer.Linked** element can be used to make the data reusable in another datalayer outside this scope.

The [Auto Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419700048023-Auto-Columns) element can be used to quickly display in your report all the data in a datalayer.
