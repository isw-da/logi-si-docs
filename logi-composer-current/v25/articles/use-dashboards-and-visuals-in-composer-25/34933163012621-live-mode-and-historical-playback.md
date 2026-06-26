---
title: "Live Mode and Historical Playback"
id: 34933163012621
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933163012621-Live-Mode-and-Historical-Playback
updated_at: 2026-05-26T22:08:26Z
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
* The time zone used by the date-time field in the data source should align with the time zone used by the date-time field in your data store. The data source time zone can be set using the **Time Zone** attribute on the [Fields tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932906721933-Manage-Fields) of the data source definition.
* The data source should have live mode enabled. Use the **Live Mode** switch on the Global Settings tab of the data source configuration. See [Configure Time Bar Defaults](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932879958669-Configure-Time-Bar-Defaults).
* The data store should be capable of receiving new or updated data, that is, data that is not static like flat files.

Live mode and historical playback are supported for even time intervals. See [Even Time Intervals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932833532429-Even-Time-Intervals). Live mode and historical playback are not supported for fused data sources. See [Data Fusion Limitations](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932973239821-Data-Fusion-Limitations).

**Note:** 
Live mode and historical playback do not work for tables when the table is grouped. See [Group and Ungroup Table Data](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933242142605-Group-and-Ungroup-Table-Data).

Playback mode (Data DVR) is available if the date-time field in your data source has the **playable** property set to **True** and the granularity of the field is not greater than **day**. When is the **playable** property in a data source set to true?

1. If the date-time field in the data store is indexed or partitioned. For Impala data stores, this option can also be enabled if the selected date field has a connection to the partitioned date field.
2. If the data store is Spark (for example, Spark SQL).
3. In Amazon Redshift, data sources for the first sort key.

Support for this feature by connector is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| --- | --- |
| [Amazon Redshift](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932733806989-Manage-the-Amazon-Redshift-Connector) | **Y** |
| [Amazon S3](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743032461-Manage-the-Amazon-S3-Connector) | **Y** |
| [Apache Drill](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932734193677-Manage-the-Apache-Drill-Connector) | **Y** |
| [Apache Phoenix](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743401869-Manage-the-Apache-Phoenix-Connector) | **N** |
| [Apache Phoenix Query Server (QS)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743401869-Manage-the-Apache-Phoenix-Connector) | **N** |
| [Apache Solr](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743530125-Manage-the-Apache-Solr-Connector) | **N** |
| [BigQuery](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932735000973-Manage-the-BigQuery-Connector) | **Y** |
| [Business Central Jet](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932747192973-Manage-the-Business-Central-Jet-Connector) | **N** |
| [Cloudera Impala](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932744502541-Manage-the-Impala-Connector) | **Y** |
| [Cloudera Search](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932696536461-Manage-the-Cloudera-Search-Connector) | **N** |
| [Couchbase](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932720313229-Manage-the-Couchbase-Connector) | **N** |
| [Dremio](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728091149-Manage-the-Dremio-Connector) | **Y** |
| [Elasticsearch 7.0](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector) | **Y** |
| [Elasticsearch 8.0](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector) | **Y** |
| [File Upload](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932721668365-Manage-File-Uploads) | **Y** |
| [HDFS](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932746629773-Manage-the-HDFS-Connector) | **Y** |
| [Hive](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932766095885-Manage-the-Hive-Connector) | **Y** |
| [Jira](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932766172941-Manage-the-Jira-Connector) | **Y** |
| [MemSQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932747006861-Manage-the-MemSQL-Connector) | **Y** |
| [Microsoft SQL Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730176653-Manage-the-Microsoft-SQL-Server-Connector) | **Y** |
| [MongoDB](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932729901069-Manage-the-MongoDB-Connector) | **N** |
| [MySQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730297485-Manage-the-MySQL-Connector) | **Y** |
| [OpenSearch](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515138873485-Manage-the-OpenSearch-Connector) | **Y** |
| [Oracle](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730448653-Manage-the-Oracle-Connector) | **Y** |
| [PostgreSQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932749503629-Manage-the-PostgreSQL-Connector) | **Y** |
| [Python](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932738470925-Manage-the-Python-Connector) | **N** |
| [Real Time Sales](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932767352077-Manage-the-Real-Time-Sales-Demo-Source) | **Y** |
| [Salesforce](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932756901901-Manage-the-Salesforce-Connector) | **Y** |
| [SAP Hana](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932798573197-Manage-the-SAP-Hana-Connector) | **Y** |
| [SAP S/4HANA](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932767840781-Manage-the-SAP-S-4HANA-Connector) | **Y** |
| [SAP IQ](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932757142925-Manage-the-SAP-IQ-Connector) | **Y** |
| [Spark SQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932799029901-Manage-the-Spark-SQL-Connector) | **Y** |
| [Snowflake](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932757334669-Manage-the-Snowflake-Connector) | **Y** |
| [Teradata](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932773152781-Manage-the-Teradata-Connector) | **Y** |
| [TIBCO DV](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932768245901-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | **Y** |
| [Trino](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932773334285-Manage-the-Trino-Connector) | **Y** |
| [File Upload (Upload API)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932721668365-Manage-File-Uploads) | **Y** |
| [Vertica](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932768403725-Manage-the-Vertica-Connector) | **Y** |

See also [Configure Time Bar Defaults](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932879958669-Configure-Time-Bar-Defaults).
