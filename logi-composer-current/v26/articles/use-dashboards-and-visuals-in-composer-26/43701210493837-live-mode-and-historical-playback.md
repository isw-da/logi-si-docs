---
title: "Live Mode and Historical Playback"
id: 43701210493837
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210493837-Live-Mode-and-Historical-Playback
updated_at: 2026-05-29T14:09:33Z
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
* The time zone used by the date-time field in the data source should align with the time zone used by the date-time field in your data store. The data source time zone can be set using the **Time Zone** attribute on the [Fields tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields) of the data source definition.
* The data source should have live mode enabled. Use the **Live Mode** switch on the Global Settings tab of the data source configuration. See [Configure Time Bar Defaults](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080606477-Configure-Time-Bar-Defaults).
* The data store should be capable of receiving new or updated data, that is, data that is not static like flat files.

Live mode and historical playback are supported for even time intervals. See [Even Time Intervals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701077393293-Even-Time-Intervals). Live mode and historical playback are not supported for fused data sources. See [Data Fusion Limitations](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134173965-Data-Fusion-Limitations).

**Note:** 
Live mode and historical playback do not work for tables when the table is grouped. See [Group and Ungroup Table Data](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701183802381-Group-and-Ungroup-Table-Data).

Playback mode (Data DVR) is available if the date-time field in your data source has the **playable** property set to **True** and the granularity of the field is not greater than **day**. When is the **playable** property in a data source set to true?

1. If the date-time field in the data store is indexed or partitioned. For Impala data stores, this option can also be enabled if the selected date field has a connection to the partitioned date field.
2. If the data store is Spark (for example, Spark SQL).
3. In Amazon Redshift, data sources for the first sort key.

Support for this feature by connector is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| --- | --- |
| [Amazon Redshift](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009454477-Manage-the-Amazon-Redshift-Connector) | **Y** |
| [Amazon S3](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009509517-Manage-the-Amazon-S3-Connector) | **Y** |
| [Apache Drill](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042973581-Manage-the-Apache-Drill-Connector) | **Y** |
| [Apache Phoenix](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025361549-Manage-the-Apache-Phoenix-Connector) | **N** |
| [Apache Phoenix Query Server (QS)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025361549-Manage-the-Apache-Phoenix-Connector) | **N** |
| [Apache Solr](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043021325-Manage-the-Apache-Solr-Connector) | **N** |
| [BigQuery](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009802509-Manage-the-BigQuery-Connector) | **Y** |
| [Business Central Jet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701057330957-Manage-the-Business-Central-Jet-Connector) | **N** |
| [Cloudera Impala](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025595405-Manage-the-Impala-Connector) | **Y** |
| [Cloudera Search](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009985933-Manage-the-Cloudera-Search-Connector) | **N** |
| [Couchbase](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701040183821-Manage-the-Couchbase-Connector) | **N** |
| [Dremio](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043446285-Manage-the-Dremio-Connector) | **Y** |
| [Elasticsearch 7.0](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector) | **Y** |
| [Elasticsearch 8.0](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector) | **Y** |
| [File Upload](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads) | **Y** |
| [HDFS](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700995161101-Manage-the-HDFS-Connector) | **Y** |
| [Hive](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026308493-Manage-the-Hive-Connector) | **Y** |
| [Jira](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044185229-Manage-the-Jira-Connector) | **Y** |
| [MemSQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011116173-Manage-the-MemSQL-Connector) | **Y** |
| [Microsoft SQL Server](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026525069-Manage-the-Microsoft-SQL-Server-Connector) | **Y** |
| [MongoDB](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026372749-Manage-the-MongoDB-Connector) | **N** |
| [MySQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044330253-Manage-the-MySQL-Connector) | **Y** |
| [OpenSearch](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074183053-Manage-the-OpenSearch-Connector) | **Y** |
| [Oracle](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011976717-Manage-the-Oracle-Connector) | **Y** |
| [PostgreSQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701091160973-Manage-the-PostgreSQL-Connector) | **Y** |
| [Python](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074664333-Manage-the-Python-Connector) | **N** |
| [Real Time Sales](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027022221-Manage-the-Real-Time-Sales-Demo-Source) | **Y** |
| [Salesforce](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074738317-Manage-the-Salesforce-Connector) | **Y** |
| [SAP Hana](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701012179469-Manage-the-SAP-Hana-Connector) | **Y** |
| [SAP S/4HANA](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996045069-Manage-the-SAP-S-4HANA-Connector) | **Y** |
| [SAP IQ](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996022669-Manage-the-SAP-IQ-Connector) | **Y** |
| [Spark SQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701012300173-Manage-the-Spark-SQL-Connector) | **Y** |
| [Snowflake](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074814989-Manage-the-Snowflake-Connector) | **Y** |
| [Teradata](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701091479437-Manage-the-Teradata-Connector) | **Y** |
| [TIBCO DV](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996158349-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | **Y** |
| [Trino](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701045148045-Manage-the-Trino-Connector) | **Y** |
| [File Upload (Upload API)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads) | **Y** |
| [Vertica](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027298189-Manage-the-Vertica-Connector) | **Y** |

See also [Configure Time Bar Defaults](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080606477-Configure-Time-Bar-Defaults).
