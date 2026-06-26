---
title: "Maintain Derived Fields"
id: 4405859299479
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859299479-Maintain-Derived-Fields
updated_at: 2021-09-21T01:28:06Z
---

# Maintain Derived Fields

# Maintain Derived Fields

Derived fields are supported by certain connectors that come out-of-the-box in Composer. To see what functions are available, see [*Supported Row-Level Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851021079-Supported-Row-Level-Functions).

Support for this feature by Composer connectors is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? | | | Notes |
| --- | --- | --- | --- | --- |
| [Amazon Redshift](https://devnet.logianalytics.com/hc/en-us/articles/4405859198103-Manage-the-Amazon-Redshift-Connector) | **Y** | | |  |
| [Amazon S3](https://devnet.logianalytics.com/hc/en-us/articles/4405850929943-Manage-the-Amazon-S3-Connector) | **Y** | | |  |
| [Apache Drill](https://devnet.logianalytics.com/hc/en-us/articles/4405850930839-Manage-the-Apache-Drill-Connector) | **Y** | | |  |
| [Apache Phoenix](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) | **Y** | | | Apache Phoenix and Apache Phoenix Query Server connectors support row-level expressions (derived fields) with the following limitations:   * The filter IS NULL does not work properly on grouped fields. * The LOCATE [text row-level function](https://devnet.logianalytics.com/hc/en-us/articles/4405851020183-Text-Functions) only supports a constant as a argument. * A COALESCE [conditional row-level function](https://devnet.logianalytics.com/hc/en-us/articles/4405851017239-Conditional-Functions) specified with and empty argument does not work properly. * If the CASE [conditional row-level function](https://devnet.logianalytics.com/hc/en-us/articles/4405851017239-Conditional-Functions) returns a null value as a an argument of another function, a NullPointerException may occur. * The LPAD and RPAD [text row-level functions](https://devnet.logianalytics.com/hc/en-us/articles/4405851020183-Text-Functions) are not supported. |
| [Apache Phoenix Query Server (QS)](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) | **Y** | | |
| [Apache Solr](https://devnet.logianalytics.com/hc/en-us/articles/4405850931735-Manage-the-Apache-Solr-Connector) | **N** | | |  |
| [BigQuery](https://devnet.logianalytics.com/hc/en-us/articles/4405859214231-Manage-the-BigQuery-Connector) | **Y** | | |  |
| [Cloudera Impala](https://devnet.logianalytics.com/hc/en-us/articles/4405850938647-Manage-the-Impala-Connector) | **Y** | | |  |
| [Cloudera Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859219863-Manage-the-Cloudera-Search-Connector) | **N** | | |  |
| [Couchbase](https://devnet.logianalytics.com/hc/en-us/articles/4405859220887-Manage-the-Couchbase-Connector) | **Y** | | |  |
| [Dremio](https://devnet.logianalytics.com/hc/en-us/articles/4405859221911-Manage-the-Dremio-Connector) | **N** | | |  |
| [Elasticsearch 6.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) | **Y** | | |  |
| [Elasticsearch 7.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) | **Y** | | |
| [Flat File](https://devnet.logianalytics.com/hc/en-us/articles/4405850954647-Upload-a-Flat-File-into-Composer) | **Y** | | |  |
| [HDFS](https://devnet.logianalytics.com/hc/en-us/articles/4405859226903-Manage-the-HDFS-Connector) | **Y** | | |  |
| [Hive](https://devnet.logianalytics.com/hc/en-us/articles/4405850956695-Manage-the-Hive-Connector) | **Y** | | |  |
| [MemSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405859228567-Manage-the-MemSQL-Connector) | **Y** | | |  |
| [Microsoft SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/4405859229975-Manage-the-Microsoft-SQL-Server-Connector) | **Y** | | |  |
| [MongoDB](https://devnet.logianalytics.com/hc/en-us/articles/4405850957591-Manage-the-MongoDB-Connector) | **Y** | | | MongoDB connectors support derived fields with some exceptions. See the discussion in [*Manage the MongoDB Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405850957591-Manage-the-MongoDB-Connector). |
| [MySQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850958487-Manage-the-MySQL-Connector) | **Y** | | |  |
| [Oracle](https://devnet.logianalytics.com/hc/en-us/articles/4405850959383-Manage-the-Oracle-Connector) | **Y** | | |  |
| [PostgreSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850960279-Manage-the-PostgreSQL-Connector) | **Y** | | |  |
| [Presto](https://devnet.logianalytics.com/hc/en-us/articles/4405859231639-Manage-the-Presto-Connector) | **N** | | |  |
| [Real Time Sales](https://devnet.logianalytics.com/hc/en-us/articles/4405850962071-Manage-the-Real-Time-Sales-Demo-Source) | N/A | | |  |
| [SAP Hana](https://devnet.logianalytics.com/hc/en-us/articles/4405859232791-Manage-the-SAP-Hana-Connector) | **Y** | | |  |
| [SAP IQ](https://devnet.logianalytics.com/hc/en-us/articles/4405850963095-Manage-the-SAP-IQ-Connector) | **Y** | | |  |
| [Snowflake](https://devnet.logianalytics.com/hc/en-us/articles/4405859234199-Manage-the-Snowflake-Connector) | **Y** | | |  |
| [Spark SQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850963991-Manage-the-Spark-SQL-Connector) | **Y** | | |  |
| [Teradata](https://devnet.logianalytics.com/hc/en-us/articles/4405859235607-Manage-the-Teradata-Connector) | **Y** | | |  |
| [TIBCO DV](https://devnet.logianalytics.com/hc/en-us/articles/4405850965783-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | **Y** | | |  |
| [Upload API](https://devnet.logianalytics.com/hc/en-us/articles/4405859140247-Use-the-Upload-API) | **Y** | | |  |
| [Vertica](https://devnet.logianalytics.com/hc/en-us/articles/4405850966679-Manage-the-Vertica-Connector) | **Y** | | |  |

A derived field is an in-memory column for your data table that is populated with results from calculations performed on data already in your table. You can create derived fields using [row-level expressions](https://devnet.logianalytics.com/hc/en-us/articles/4405859311511-Row-Level-Expressions) that are built using [row-level functions](https://devnet.logianalytics.com/hc/en-us/articles/4405851021079-Supported-Row-Level-Functions).

These calculations are performed at the level of a row, that is, a record, and do not include other data from your table that is outside of that particular row. If a source supports derived fields, then you can use them as arguments for aggregate functions when creating other calculations.

Derived fields can be created from other derived fields.

Consider the following examples:

Your data source has records that list the revenue generated and the term of employment but does not have an average of the two. You can use a derived field to create an average of the two for each record.
Use the following formula:

```
(revenue/lengthofemployment)
```

Your data source continues values that have been brought in as text strings. In order to cross-reference this data with the time values, you need to change the text to a numeric value. Use the following formula as a base:

```
TEXT_TO_NUM (LTRIM (Field_A, '$')) SUM(TEXT_TO_NUM(SUBSTRING("$124456.00", 2, 10)))
```

Your data source contains records that list the start of employment and termination of employment for your company. You want to find the differences between these time values to average out the length of employment. Use the following formula as a base:

```
TIME_DIFF (timePart, startTime : Time, endTime : Time) : Numeric
```

Composer supports row-level functions in derived fields. See [*Supported Row-Level Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851021079-Supported-Row-Level-Functions).

Derived fields can be hidden. See [*Hide Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4405851036695-Hide-Fields).

For information on maintaining derived fields, see the following links:

* [*Derived Field Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4405851014551-Derived-Field-Editor)
* [*Create and Modify Derived Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4405851011735-Create-and-Modify-Derived-Fields)
* [*Duplicate Derived Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4405859293207-Duplicate-Derived-Fields)
* [*Supported Row-Level Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851021079-Supported-Row-Level-Functions)
* [*Delete Derived Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4405859294359-Delete-Derived-Fields)
* [*Hide Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4405851036695-Hide-Fields)
