---
title: "Maintain Derived Fields"
id: 4402955538711
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955538711-Maintain-Derived-Fields
updated_at: 2021-08-07T17:30:35Z
---

# Maintain Derived Fields

# Maintain Derived Fields

Derived fields are supported by certain connectors that come out-of-the-box in Composer. To see what functions are available, see [*Supported Row-Level Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402955544471-Supported-Row-Level-Functions).

Support for this feature by Composer connectors is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? | | | Notes |
| --- | --- | --- | --- | --- |
| [Amazon Redshift](https://devnet.logianalytics.com/hc/en-us/articles/4402955471255-Manage-the-Amazon-Redshift-Connector) | **Y** | | |  |
| [Amazon S3](https://devnet.logianalytics.com/hc/en-us/articles/4402955471895-Manage-the-Amazon-S3-Connector) | **Y** | | |  |
| [Apache Drill](https://devnet.logianalytics.com/hc/en-us/articles/4402955472535-Manage-the-Apache-Drill-Connector) | **Y** | | |  |
| [Apache Phoenix](https://devnet.logianalytics.com/hc/en-us/articles/4402955473175-Manage-the-Apache-Phoenix-Connector) | **Y** | | | Apache Phoenix and Apache Phoenix Query Server connectors support row-level expressions (derived fields) with the following limitations:   * The filter IS NULL does not work properly on grouped fields. * The LOCATE [text row-level function](https://devnet.logianalytics.com/hc/en-us/articles/4402955543831-Text-Functions) only supports a constant as a argument. * A COALESCE [conditional row-level function](https://devnet.logianalytics.com/hc/en-us/articles/4402955542551-Conditional-Functions) specified with and empty argument does not work properly. * If the CASE [conditional row-level function](https://devnet.logianalytics.com/hc/en-us/articles/4402955542551-Conditional-Functions) returns a null value as a an argument of another function, a NullPointerException may occur. * The LPAD and RPAD [text row-level functions](https://devnet.logianalytics.com/hc/en-us/articles/4402955543831-Text-Functions) are not supported. |
| [Apache Phoenix Query Server (QS)](https://devnet.logianalytics.com/hc/en-us/articles/4402955473175-Manage-the-Apache-Phoenix-Connector) | **Y** | | |
| [Apache Solr](https://devnet.logianalytics.com/hc/en-us/articles/4402955473815-Manage-the-Apache-Solr-Connector) | **N** | | |  |
| [BigQuery](https://devnet.logianalytics.com/hc/en-us/articles/4402955477655-Manage-the-BigQuery-Connector) | **Y** | | |  |
| [Cloudera Impala](https://devnet.logianalytics.com/hc/en-us/articles/4402955478935-Manage-the-Impala-Connector) | **Y** | | |  |
| [Cloudera Search](https://devnet.logianalytics.com/hc/en-us/articles/4402955479575-Manage-the-Cloudera-Search-Connector) | **N** | | |  |
| [Couchbase](https://devnet.logianalytics.com/hc/en-us/articles/4402955480215-Manage-the-Couchbase-Connector) | **Y** | | |  |
| [Dremio](https://devnet.logianalytics.com/hc/en-us/articles/4402955481111-Manage-the-Dremio-Connector) | **N** | | |  |
| [Elasticsearch 6.0](https://devnet.logianalytics.com/hc/en-us/articles/4402962910999-Manage-the-Elasticsearch-Connector) | **Y** | | |  |
| [Elasticsearch 7.0](https://devnet.logianalytics.com/hc/en-us/articles/4402962910999-Manage-the-Elasticsearch-Connector) | **Y** | | |
| [Flat File](https://devnet.logianalytics.com/hc/en-us/articles/4402962915095-Upload-a-Flat-File-into-Composer) | **Y** | | |  |
| [HDFS](https://devnet.logianalytics.com/hc/en-us/articles/4402962915863-Manage-the-HDFS-Connector) | **Y** | | |  |
| [Hive](https://devnet.logianalytics.com/hc/en-us/articles/4402955487255-Manage-the-Hive-Connector) | **Y** | | |  |
| [MemSQL](https://devnet.logianalytics.com/hc/en-us/articles/4402962917527-Manage-the-MemSQL-Connector) | **Y** | | |  |
| [Microsoft SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/4402962918423-Manage-the-Microsoft-SQL-Server-Connector) | **Y** | | |  |
| [MongoDB](https://devnet.logianalytics.com/hc/en-us/articles/4402955487895-Manage-the-MongoDB-Connector) | **Y** | | | MongoDB connectors support derived fields with some exceptions. See the discussion in [*Manage the MongoDB Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4402955487895-Manage-the-MongoDB-Connector). |
| [MySQL](https://devnet.logianalytics.com/hc/en-us/articles/4402955488535-Manage-the-MySQL-Connector) | **Y** | | |  |
| [Oracle](https://devnet.logianalytics.com/hc/en-us/articles/4402962919319-Manage-the-Oracle-Connector) | **Y** | | |  |
| [PostgreSQL](https://devnet.logianalytics.com/hc/en-us/articles/4402962920087-Manage-the-PostgreSQL-Connector) | **Y** | | |  |
| [Presto](https://devnet.logianalytics.com/hc/en-us/articles/4402955489303-Manage-the-Presto-Connector) | **N** | | |  |
| [Real Time Sales](https://devnet.logianalytics.com/hc/en-us/articles/4402955489943-Manage-the-Real-Time-Sales-Demo-Source) | N/A | | |  |
| [SAP Hana](https://devnet.logianalytics.com/hc/en-us/articles/4402955490583-Manage-the-SAP-Hana-Connector) | **Y** | | |  |
| [SAP IQ](https://devnet.logianalytics.com/hc/en-us/articles/4402955491223-Manage-the-SAP-IQ-Connector) | **Y** | | |  |
| [Snowflake](https://devnet.logianalytics.com/hc/en-us/articles/4402955491863-Manage-the-Snowflake-Connector) | **Y** | | |  |
| [Spark SQL](https://devnet.logianalytics.com/hc/en-us/articles/4402955492503-Manage-the-Spark-SQL-Connector) | **Y** | | |  |
| [Teradata](https://devnet.logianalytics.com/hc/en-us/articles/4402962923159-Manage-the-Teradata-Connector) | **Y** | | |  |
| [TIBCO DV](https://devnet.logianalytics.com/hc/en-us/articles/4402955493143-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | **Y** | | |  |
| [Upload API](https://devnet.logianalytics.com/hc/en-us/articles/4402962872599-Use-the-Upload-API) | **Y** | | |  |
| [Vertica](https://devnet.logianalytics.com/hc/en-us/articles/4402962927255-Manage-the-Vertica-Connector) | **Y** | | |  |

A derived field is an in-memory column for your data table that is populated with results from calculations performed on data already in your table. You can create derived fields using [row-level expressions](https://devnet.logianalytics.com/hc/en-us/articles/4402962967831-Row-Level-Expressions) that are built using [row-level functions](https://devnet.logianalytics.com/hc/en-us/articles/4402955544471-Supported-Row-Level-Functions).

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

Composer supports row-level functions in derived fields. See [*Supported Row-Level Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402955544471-Supported-Row-Level-Functions).

Derived fields can be hidden. See [*Hide Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4402962975895-Hide-Fields).

For information on maintaining derived fields, see the following links:

* [*Derived Field Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4402955537943-Derived-Field-Editor)
* [*Create and Modify Derived Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4402955534359-Create-and-Modify-Derived-Fields)
* [*Duplicate Derived Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4402955533719-Duplicate-Derived-Fields)
* [*Supported Row-Level Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402955544471-Supported-Row-Level-Functions)
* [*Delete Derived Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4402955535127-Delete-Derived-Fields)
* [*Hide Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4402962975895-Hide-Fields)
