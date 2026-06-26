---
title: "DataLayer.SP - Retrieving Data with DataLayer.SP"
id: 4419707504023
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707504023-DataLayer-SP-Retrieving-Data-with-DataLayer-SP
updated_at: 2022-07-17T01:52:56Z
---

# DataLayer.SP - Retrieving Data with DataLayer.SP

# DataLayer.SP - Retrieving Data with DataLayer.SP

The datalayer receives and caches the results returned by a SQL stored procedure. You can add child elements beneath the datalayer to affect the results, including:

* **Filtering**: Sort, group, or restrict the result data
* **Joining**: Apply SQL JOINs to the data in the datalayer
* **Extending**: Add virtual columns to the datalayer that contain aggregated, calculated, or totaled result values
* **Securing**: Limit access to the data using Logi security
* **Linking**: Make the results reusable elsewhere in your report definitions

Data retrieved into the datalayer is cached in **XML** format, in memory and/or on the web server's file system. The latter is discussed in [The Logi Server Engine](https://devnet.logianalytics.com/hc/en-us/articles/4419715421975-The-Logi-Server-Engine) and may be of interest to developers working with extremely large datasets or large numbers of concurrent users.

The data retrieved with a datalayer is available using @Data **tokens**, in the format @Data.*ColumnName*~. The spelling of the column name is *case-sensitive*. The data is only available within the scope of the parent element of the datalayer, not throughout the entire report definition. The **DataLayer.Linked** element can be used to make the data reusable in another datalayer outside this scope.

The [Auto Columns](https://devnet.logianalytics.com/hc/en-us/articles/4419700048023-Auto-Columns) element can be used to quickly display in your report all the data in a datalayer.

The data retrieved into the datalayer can be viewed by turning on the Debugger Trace page in your \_Settings definition (General element) and using the resulting link at the bottom of your report page to view the data.

In most respects, DataLayer.SP functions exactly as other datalayer elements do, however, stored procedures typically provide better performance than a standard SQL statement and have the added benefit of offering protection against SQL injection attacks.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699654295/dlsp_01.png)

In the example shown above, a **DataLayer.SP** element has been added as a child element of a Data Table and its attributes set so that it calls the desired stored procedure on the database server.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) The *only* text in the **Command** attribute value is the *name* of the stored procedure; you do not need to enter "EXECUTE" or other SQL commands here. For most major database servers, you can click the arrow at the end of this attribute to retrieve a list of available stored procedure names and then select the one you want. Input and output parameters are handled using special elements that are children of the datalayer and they're discussed in [DataLayer.SP - Stored Procedure Parameters](https://devnet.logianalytics.com/hc/en-us/articles/4419715230359-DataLayer-SP-Stored-Procedure-Parameters).

Result set data returned into the datalayer can be referenced using @Data tokens.
