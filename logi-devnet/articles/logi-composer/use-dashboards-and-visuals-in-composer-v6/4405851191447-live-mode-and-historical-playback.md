---
title: "Live Mode and Historical Playback"
id: 4405851191447
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851191447-Live-Mode-and-Historical-Playback
updated_at: 2021-09-21T01:29:45Z
---

# Live Mode and Historical Playback

# Live Mode and Historical Playback

Live mode and historical playback (also known as Data DVR) allow you to get the most from data stores that support playback. The only difference between live mode and historical playback is the time range that is selected.

* Live mode refreshes field data on your visuals for date-time fields that are indexed as playable. In live mode, your data plays forever without an end date.
* Historical playback (Data DVR) shows the historical record of field data for date-time fields that are indexed as playable. Playback can show up to the last moment before the current period in your data.

Live mode and historical playback require:

* A date-time field in your data store (data base) that is either indexed or partitioned.

  If indexed, the index should be non-clustered.

  If your data store does not support indexing or partitioning, then live mode and historical playback are not available for that data. For most data stores, indexing is the default.
* The time zone used by the date-time field in the Composer data source should align with the time zone used by the date-time field in your data store. The data source time zone can be set using the **Time Zone** attribute on the [Fields tab](https://devnet.logianalytics.com/hc/en-us/articles/4405851026455-Fields-Tab) of the data source definition.
* The data source should have live mode enabled. Use the **Live Mode** switch on the Visuals tab of the data source configuration. See [*Configure Time Bar Defaults*](https://devnet.logianalytics.com/hc/en-us/articles/4405859324311-Configure-Time-Bar-Defaults).
* The data store should be capable of receiving new or updated data, that is, data that is not static like flat files.

Live mode and historical playback are supported for even time intervals. See [*Even Time Intervals*](https://devnet.logianalytics.com/hc/en-us/articles/4405850992919-Even-Time-Intervals). Live mode and historical playback are not supported for fused data sources. See [*Data Fusion Limitations*](https://devnet.logianalytics.com/hc/en-us/articles/4405859357463-Data-Fusion-Limitations).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Live mode and historical playback do not work for tables when the table is grouped. See [*Group and Ungroup Table Data*](https://devnet.logianalytics.com/hc/en-us/articles/4405851238551-Group-and-Ungroup-Table-Data).

Playback mode (Data DVR) is available if the date-time field in your data source has the **playable** property set to **True** and the granularity of the field is not greater than **day**. When is the **playable** property in a data source set to true?

1. If the date-time field in the data store is indexed or partitioned. For Impala data stores, this option can also be enabled if the selected date field has a connection to the partitioned date field.
2. If the data store is Spark (for example, Spark SQL)
3. In Amazon Redshift, data sources for the first sort key.

Support for this feature by Composer connectors is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? | |
| --- | --- | --- |
| [Amazon Redshift](https://devnet.logianalytics.com/hc/en-us/articles/4405859198103-Manage-the-Amazon-Redshift-Connector) | **Y** | |
| [Amazon S3](https://devnet.logianalytics.com/hc/en-us/articles/4405850929943-Manage-the-Amazon-S3-Connector) | **Y** | |
| [Apache Drill](https://devnet.logianalytics.com/hc/en-us/articles/4405850930839-Manage-the-Apache-Drill-Connector) | **Y** | |
| [Apache Phoenix](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) | **Y** | |
| [Apache Phoenix Query Server (QS)](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) | **Y** | |
| [Apache Solr](https://devnet.logianalytics.com/hc/en-us/articles/4405850931735-Manage-the-Apache-Solr-Connector) | **Y** | |
| [BigQuery](https://devnet.logianalytics.com/hc/en-us/articles/4405859214231-Manage-the-BigQuery-Connector) | **Y** | |
| [Cloudera Impala](https://devnet.logianalytics.com/hc/en-us/articles/4405850938647-Manage-the-Impala-Connector) | **Y** | |
| [Cloudera Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859219863-Manage-the-Cloudera-Search-Connector) | **Y** | |
| [Couchbase](https://devnet.logianalytics.com/hc/en-us/articles/4405859220887-Manage-the-Couchbase-Connector) | **Y** | |
| [Dremio](https://devnet.logianalytics.com/hc/en-us/articles/4405859221911-Manage-the-Dremio-Connector) | **Y** | |
| [Elasticsearch 6.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) | **Y** | |
| [Elasticsearch 7.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) | **Y** | |
| [Flat File](https://devnet.logianalytics.com/hc/en-us/articles/4405850954647-Upload-a-Flat-File-into-Composer) | **Y** | |
| [HDFS](https://devnet.logianalytics.com/hc/en-us/articles/4405859226903-Manage-the-HDFS-Connector) | **Y** | |
| [Hive](https://devnet.logianalytics.com/hc/en-us/articles/4405850956695-Manage-the-Hive-Connector) | **Y** | |
| [MemSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405859228567-Manage-the-MemSQL-Connector) | **Y** | |
| [Microsoft SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/4405859229975-Manage-the-Microsoft-SQL-Server-Connector) | **Y** | |
| [MongoDB](https://devnet.logianalytics.com/hc/en-us/articles/4405850957591-Manage-the-MongoDB-Connector) | **Y** | |
| [MySQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850958487-Manage-the-MySQL-Connector) | **Y** | |
| [Oracle](https://devnet.logianalytics.com/hc/en-us/articles/4405850959383-Manage-the-Oracle-Connector) | **Y** | |
| [PostgreSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850960279-Manage-the-PostgreSQL-Connector) | **Y** | |
| [Presto](https://devnet.logianalytics.com/hc/en-us/articles/4405859231639-Manage-the-Presto-Connector) | **Y** | |
| [Real Time Sales](https://devnet.logianalytics.com/hc/en-us/articles/4405850962071-Manage-the-Real-Time-Sales-Demo-Source) | **Y** | |
| [SAP Hana](https://devnet.logianalytics.com/hc/en-us/articles/4405859232791-Manage-the-SAP-Hana-Connector) | **Y** | |
| [SAP IQ](https://devnet.logianalytics.com/hc/en-us/articles/4405850963095-Manage-the-SAP-IQ-Connector) | **Y** | |
| [Snowflake](https://devnet.logianalytics.com/hc/en-us/articles/4405859234199-Manage-the-Snowflake-Connector) | **Y** | |
| [Spark SQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850963991-Manage-the-Spark-SQL-Connector) | **Y** | |
| [Teradata](https://devnet.logianalytics.com/hc/en-us/articles/4405859235607-Manage-the-Teradata-Connector) | **Y** | |
| [TIBCO DV](https://devnet.logianalytics.com/hc/en-us/articles/4405850965783-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | **Y** | |
| [Upload API](https://devnet.logianalytics.com/hc/en-us/articles/4405859140247-Use-the-Upload-API) | **Y** | |
| [Vertica](https://devnet.logianalytics.com/hc/en-us/articles/4405850966679-Manage-the-Vertica-Connector) | **Y** | |

See also [*Configure Time Bar Defaults*](https://devnet.logianalytics.com/hc/en-us/articles/4405859324311-Configure-Time-Bar-Defaults).
