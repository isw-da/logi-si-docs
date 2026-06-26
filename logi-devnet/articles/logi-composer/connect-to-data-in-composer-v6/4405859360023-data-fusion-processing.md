---
title: "Data Fusion Processing"
id: 4405859360023
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859360023-Data-Fusion-Processing
updated_at: 2021-09-21T01:28:42Z
---

# Data Fusion Processing

# Data Fusion Processing

With data fusion, Composer can perform Group By operations using fields that are available across tables. A variety of table structures residing in data repositories can be fused, including lookup tables, fact tables, star and snowflake schema structures. See [*Data Fusion Table Structures*](https://devnet.logianalytics.com/hc/en-us/articles/4405851074199-Data-Fusion-Table-Structures).

For example, if a table in one data store contains the IDs and address information of sellers and another table in another data store contains IDs, events, and sales information for sellers, these disparate fields can be fused into one sellers table with the three fields joined and accessible (as shown below).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747415191/concept-data-fusion-sellers_279x191.png)

Using data fusion, you can join disparate data sources that are connected to Composer. Multiple data sources (three or more) can be fused into a single Fusion data source.

To fuse these disparate sources together, you must join matching fields from the different data sources on the Editor tab of the Data Fusion [data source configuration](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations). This is the key step to data fusion and must adhere to specific rules. Joins are defined on the Editor tab of the Data Fusion [data source configuration](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations). In a fused data source, Composer uses information about column uniqueness when building its query plan. This can be critical for a connector's resource usage and query time. Column uniqueness can be specified in the fused data source definition on the Editor tab by selecting the Unique checkbox. See [*Data Fusion Join Rules*](https://devnet.logianalytics.com/hc/en-us/articles/4405851073175-Data-Fusion-Join-Rules) and [*Create a Fusion Data Source*](https://devnet.logianalytics.com/hc/en-us/articles/4405859361431-Create-a-Fusion-Data-Source).

Joins are usually performed in-memory. However, if a data connector supports pushdown joins and the data to be joined comes from the same data source connection, Composer pushes the join operation to the underlying data engines and allows those data stores to join the data instead. In addition, if the joins are [inner joins](https://www.w3schools.com/sql/sql_join_inner.asp) and aggregate functions SUM, MIN, MAX, or COUNT are used in the data, the Composer engine intelligently pushes the aggregate queries to the underlying data engines, thus reducing the amount of data that needs to be processed. This aggregate pushdown occurs when joining data from the same or from different data sources. For more information about optimizing joins in your Fusion data sources, see [*Optimize Joins*](https://devnet.logianalytics.com/hc/en-us/articles/4405859358487-Optimize-Joins).

Because most joins are performed in-memory, a configurable limit has been placed on the number of records that can be processed from each joined source. This limit is initially set at 1,000,000 records per joined data source and can be configured by your Composer administrator or supervisor using the `qe.zengine.edc.rows.limit` property in the `query-engine.properties` file. See [*Manage the Composer Query Engine*](https://devnet.logianalytics.com/hc/en-us/articles/4405859161751-Manage-the-Composer-Query-Engine). When this threshold is exceeded, no data is shown on the visuals containing the fused data and a message appears indicating that the threshold (maximum row number) is exceeded. If you find you are hitting this limit, use filters on the visual or dashboard to reduce the number of records processed and shown.

After you have joined the necessary fields from the data sources and saved your Fusion data source, you can visualize and explore the fused data in visuals and dashboards.
