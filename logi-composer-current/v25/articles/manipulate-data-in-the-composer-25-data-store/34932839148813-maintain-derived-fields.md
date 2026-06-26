---
title: "Maintain Derived Fields"
id: 34932839148813
section: "Manipulate Data In The Composer 25 Data Store"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932839148813-Maintain-Derived-Fields
updated_at: 2026-05-26T22:07:01Z
---

# Maintain Derived Fields

# Maintain Derived Fields

Derived fields are supported by certain connectors that come out-of-the-box in Composer. To see what functions are available, see [Supported Row-Level Functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932902575629-Supported-Row-Level-Functions).

Support for this feature by connector is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? | Notes |
| --- | --- | --- |
| [Amazon Redshift](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932733806989-Manage-the-Amazon-Redshift-Connector) | **Y** |  |
| [Amazon S3](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743032461-Manage-the-Amazon-S3-Connector) | **Y** |  |
| [Apache Drill](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932734193677-Manage-the-Apache-Drill-Connector) | **Y** |  |
| [Apache Phoenix](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743401869-Manage-the-Apache-Phoenix-Connector) | **Y** | Apache Phoenix and Apache Phoenix Query Server connectors support row-level expressions (derived fields) with the following limitations:   * The filter IS NULL does not work properly on grouped fields. * The LOCATE [text row-level function](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932874867597-Text-Functions) only supports a constant as a argument. * A COALESCE [conditional row-level function](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932874388621-Conditional-Functions) specified with and empty argument does not work properly. * If the CASE [conditional row-level function](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932874388621-Conditional-Functions) returns a null value as a an argument of another function, a NullPointerException may occur. * The LPAD and RPAD [text row-level functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932874867597-Text-Functions) are not supported. |
| [Apache Phoenix Query Server (QS)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743401869-Manage-the-Apache-Phoenix-Connector) | **Y** |
| [Apache Solr](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743530125-Manage-the-Apache-Solr-Connector) | **N** |  |
| [BigQuery](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932735000973-Manage-the-BigQuery-Connector) | **Y** | If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`. |
| [Business Central Jet](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932747192973-Manage-the-Business-Central-Jet-Connector) | **Y** |  |
| [Cloudera Impala](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932744502541-Manage-the-Impala-Connector) | **Y** |  |
| [Cloudera Search](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932696536461-Manage-the-Cloudera-Search-Connector) | **N** |  |
| [Couchbase](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932720313229-Manage-the-Couchbase-Connector) | **Y** |  |
| [Dremio](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728091149-Manage-the-Dremio-Connector) | **N** |  |
| [Elasticsearch 7.0](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector) | **Y** |  |
| [Elasticsearch 8.0](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector) | **Y** |
| [File Upload](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932721668365-Manage-File-Uploads) | **Y** |  |
| [HDFS](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932746629773-Manage-the-HDFS-Connector) | **Y** |  |
| [Hive](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932766095885-Manage-the-Hive-Connector) | **Y** |  |
| [Jira](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932766172941-Manage-the-Jira-Connector) | **Y** |  |
| [MemSQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932747006861-Manage-the-MemSQL-Connector) | **Y** |  |
| [Microsoft SQL Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730176653-Manage-the-Microsoft-SQL-Server-Connector) | **Y** |  |
| [MongoDB](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932729901069-Manage-the-MongoDB-Connector) | **Y** | MongoDB connectors support derived fields with some exceptions. See the discussion in [Manage the MongoDB Connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932729901069-Manage-the-MongoDB-Connector). |
| [MySQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730297485-Manage-the-MySQL-Connector) | **Y** |  |
| [OpenSearch](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515138873485-Manage-the-OpenSearch-Connector) | **Y** |  |
| [Oracle](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730448653-Manage-the-Oracle-Connector) | **Y** |  |
| [PostgreSQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932749503629-Manage-the-PostgreSQL-Connector) | **Y** |  |
| [Python](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932738470925-Manage-the-Python-Connector) | **Y** |  |
| [Real Time Sales](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932767352077-Manage-the-Real-Time-Sales-Demo-Source) | N/A |  |
| [Salesforce](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932756901901-Manage-the-Salesforce-Connector) | **Y** |  |
| [SAP Hana](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932798573197-Manage-the-SAP-Hana-Connector) | **Y** |  |
| [SAP S/4HANA](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932767840781-Manage-the-SAP-S-4HANA-Connector) | **Y** |  |
| [SAP IQ](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932757142925-Manage-the-SAP-IQ-Connector) | **Y** |  |
| [Spark SQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932799029901-Manage-the-Spark-SQL-Connector) | **Y** |  |
| [Snowflake](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932757334669-Manage-the-Snowflake-Connector) | **Y** |  |
| [Teradata](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932773152781-Manage-the-Teradata-Connector) | **Y** |  |
| [TIBCO DV](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932768245901-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | **Y** |  |
| [Trino](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932773334285-Manage-the-Trino-Connector) | **N** |  |
| [File Upload (Upload API)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932721668365-Manage-File-Uploads) | **Y** |  |
| [Vertica](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932768403725-Manage-the-Vertica-Connector) | **Y** |  |

A derived field is an in-memory column for your data table that is populated with results from calculations performed on data already in your table. You can create derived fields using [row-level expressions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932904405901-Row-Level-Expressions) that are built using [row-level functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932902575629-Supported-Row-Level-Functions).

These calculations are performed at the level of a row, that is, a record, and do not include other data from your table that is outside of that particular row. If a source supports derived fields, then you can use them as arguments for aggregate functions when creating other calculations.

Derived fields can be created from other derived fields.

## Examples

Your data source has records that list the revenue generated and the term of employment but does not have an average of the two. You can use a derived field to create an average of the two for each record.
Use the following formula:

(revenue/lengthofemployment)

Your data source continues values that have been brought in as text strings. In order to cross-reference this data with the time values, you need to change the text to a numeric value. Use the following formula as a base:

TEXT\_TO\_NUM (LTRIM (Field\_A, '$')) SUM(TEXT\_TO\_NUM(SUBSTRING("$124456.00", 2, 10)))

Your data source contains records that list the start of employment and termination of employment for your company. You want to find the differences between these time values to average out the length of employment. Use the following formula as a base:

TIME\_DIFF (timePart, startTime : Time, endTime : Time) : Numeric

Composer supports row-level functions in derived fields. See [Supported Row-Level Functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932902575629-Supported-Row-Level-Functions).

Derived fields can be hidden. See [Hide Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932913581069-Hide-Fields).

For information on maintaining derived fields, see the following links:

* [Derived Field Editor](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932882620813-Derived-Field-Editor)
* [Create and Modify Derived Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932837821709-Create-and-Modify-Derived-Fields)
* [Supported Row-Level Functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932902575629-Supported-Row-Level-Functions)
* [Delete Derived Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932847686925-Delete-Derived-Fields)
* [Hide Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932913581069-Hide-Fields)
