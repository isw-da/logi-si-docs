---
title: "Enable Distinct Counts"
id: 4405859300503
section: "Manipulate Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859300503-Enable-Distinct-Counts
updated_at: 2021-09-21T01:28:06Z
---

# Enable Distinct Counts

# Enable Distinct Counts

Distinct count functionality determines the number of unique values in a column or expression within a selected table by comparing all the records pulled from the data store by a data source configuration. Users with editing access to data sources can enable distinct counts for specific fields. When distinct counts are enabled, unique value results are returned when analyzing data. For example, distinct counts could return the number of:

* Unique customers in a sales database
* Unique UPC codes for a category of products
* The number of trucks in a company's fleet

For example, given a single collection and string field with the following three values:

1. Apple
2. Orange
3. Apple

The distinct count returns 2, since there are only two distinct values (“Apple” and “Orange”), while an ordinary count returns 3 to reflect the total number of records. SQL-based connectors might produce a query that looks like this:

```
select count(distinct myField) from myCollection
```

You enable distinct counts for a field in a data source configuration when you first define the data source or, later, when you edit it.

Support for this feature by Composer connectors is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? | | | Notes |
| --- | --- | --- | --- | --- |
| [Amazon Redshift](https://devnet.logianalytics.com/hc/en-us/articles/4405859198103-Manage-the-Amazon-Redshift-Connector) | **Y** | | |  |
| [Amazon S3](https://devnet.logianalytics.com/hc/en-us/articles/4405850929943-Manage-the-Amazon-S3-Connector) | **Y** | | |  |
| [Apache Drill](https://devnet.logianalytics.com/hc/en-us/articles/4405850930839-Manage-the-Apache-Drill-Connector) | **Y** | | |  |
| [Apache Phoenix](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) | **Y** | | |  |
| [Apache Phoenix Query Server (QS)](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) | **Y** | | |
| [Apache Solr](https://devnet.logianalytics.com/hc/en-us/articles/4405850931735-Manage-the-Apache-Solr-Connector) | **Y** | | |  |
| [BigQuery](https://devnet.logianalytics.com/hc/en-us/articles/4405859214231-Manage-the-BigQuery-Connector) | **Y** | | |  |
| [Cloudera Impala](https://devnet.logianalytics.com/hc/en-us/articles/4405850938647-Manage-the-Impala-Connector) | **Y** | | | Cloudera Impala connectors can receive only a single distinct count field in a query. |
| [Cloudera Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859219863-Manage-the-Cloudera-Search-Connector) | **Y** | | |  |
| [Couchbase](https://devnet.logianalytics.com/hc/en-us/articles/4405859220887-Manage-the-Couchbase-Connector) | **Y** | | |  |
| [Dremio](https://devnet.logianalytics.com/hc/en-us/articles/4405859221911-Manage-the-Dremio-Connector) | **Y** | | |  |
| [Elasticsearch 6.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) | **Y** | | |  |
| [Elasticsearch 7.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) | **Y** | | |
| [Flat File](https://devnet.logianalytics.com/hc/en-us/articles/4405850954647-Upload-a-Flat-File-into-Composer) | **Y** | | |  |
| [HDFS](https://devnet.logianalytics.com/hc/en-us/articles/4405859226903-Manage-the-HDFS-Connector) | **Y** | | |  |
| [Hive](https://devnet.logianalytics.com/hc/en-us/articles/4405850956695-Manage-the-Hive-Connector) | **Y** | | |  |
| [MemSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405859228567-Manage-the-MemSQL-Connector) | **Y** | | |  |
| [Microsoft SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/4405859229975-Manage-the-Microsoft-SQL-Server-Connector) | **Y** | | |  |
| [MongoDB](https://devnet.logianalytics.com/hc/en-us/articles/4405850957591-Manage-the-MongoDB-Connector) | **Y** | | |  |
| [MySQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850958487-Manage-the-MySQL-Connector) | **Y** | | |  |
| [Oracle](https://devnet.logianalytics.com/hc/en-us/articles/4405850959383-Manage-the-Oracle-Connector) | **Y** | | |  |
| [PostgreSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850960279-Manage-the-PostgreSQL-Connector) | **Y** | | |  |
| [Presto](https://devnet.logianalytics.com/hc/en-us/articles/4405859231639-Manage-the-Presto-Connector) | **Y** | | |  |
| [Real Time Sales](https://devnet.logianalytics.com/hc/en-us/articles/4405850962071-Manage-the-Real-Time-Sales-Demo-Source) | **Y** | | |  |
| [SAP Hana](https://devnet.logianalytics.com/hc/en-us/articles/4405859232791-Manage-the-SAP-Hana-Connector) | **Y** | | |  |
| [SAP IQ](https://devnet.logianalytics.com/hc/en-us/articles/4405850963095-Manage-the-SAP-IQ-Connector) | **Y** | | |  |
| [Snowflake](https://devnet.logianalytics.com/hc/en-us/articles/4405859234199-Manage-the-Snowflake-Connector) | **Y** | | |  |
| [Spark SQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850963991-Manage-the-Spark-SQL-Connector) | **Y** | | |  |
| [Teradata](https://devnet.logianalytics.com/hc/en-us/articles/4405859235607-Manage-the-Teradata-Connector) | **Y** | | |  |
| [TIBCO DV](https://devnet.logianalytics.com/hc/en-us/articles/4405850965783-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | **Y** | | |  |
| [Upload API](https://devnet.logianalytics.com/hc/en-us/articles/4405859140247-Use-the-Upload-API) | **Y** | | |  |
| [Vertica](https://devnet.logianalytics.com/hc/en-us/articles/4405850966679-Manage-the-Vertica-Connector) | **Y** | | |  |

To enable distinct counts for a field:

1. Edit a data source configuration for a connector that supports distinct counts. See [*Edit a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405851024663-Edit-a-Data-Source-Configuration).
2. Select the [**Fields** tab](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) in the data source configuration.
3. Locate the field in the field table for which you want to enable distinct counts.
4. Select the checkbox in the **Distinct Count** column of the field table for the field. When an attribute field has Distinct Counts enabled, Composer treats it as a metric. See [*Metrics*](https://devnet.logianalytics.com/hc/en-us/articles/4405859309975-Metrics).
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743851671/save-white_39x22.png) to save the data source configuration.
