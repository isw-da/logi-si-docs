---
title: "Fast Distinct Values"
id: 4402955459863
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955459863-Fast-Distinct-Values
updated_at: 2021-08-07T17:29:36Z
---

# Fast Distinct Values

# Fast Distinct Values

Composer connectors that support fast distinct values can efficiently return distinct values for a field. This functionality optimizes the retrieval of distinct (unique) values in large numbers of records. If a connector supports this feature, the Filter dialog is populated with distinct values for an attribute directly from the data source, without the need to refresh the data and without retrieving or storing the distinct values in Composer's metadata. For example, Elasticsearch keeps lists of distinct values at the ready. Features such as these make fast distinct values possible for your connector.

There is no metric that defines “fast”. This value is based on the judgment of the developer.

When custom ranges or list values are requested for a field, full data scans are not performed.

For most connectors, this feature can be safely left disabled without impact.

Support for this feature by Composer connectors is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? | |
| --- | --- | --- |
| [Amazon Redshift](https://devnet.logianalytics.com/hc/en-us/articles/4402955471255-Manage-the-Amazon-Redshift-Connector) | N/A | |
| [Amazon S3](https://devnet.logianalytics.com/hc/en-us/articles/4402955471895-Manage-the-Amazon-S3-Connector) | N/A | |
| [Apache Drill](https://devnet.logianalytics.com/hc/en-us/articles/4402955472535-Manage-the-Apache-Drill-Connector) | N/A | |
| [Apache Phoenix](https://devnet.logianalytics.com/hc/en-us/articles/4402955473175-Manage-the-Apache-Phoenix-Connector) | N/A | |
| [Apache Phoenix Query Server (QS)](https://devnet.logianalytics.com/hc/en-us/articles/4402955473175-Manage-the-Apache-Phoenix-Connector) | N/A | |
| [Apache Solr](https://devnet.logianalytics.com/hc/en-us/articles/4402955473815-Manage-the-Apache-Solr-Connector) | **Y** | |
| [BigQuery](https://devnet.logianalytics.com/hc/en-us/articles/4402955477655-Manage-the-BigQuery-Connector) | N/A | |
| [Cloudera Impala](https://devnet.logianalytics.com/hc/en-us/articles/4402955478935-Manage-the-Impala-Connector) | N/A | |
| [Cloudera Search](https://devnet.logianalytics.com/hc/en-us/articles/4402955479575-Manage-the-Cloudera-Search-Connector) | **Y** | |
| [Couchbase](https://devnet.logianalytics.com/hc/en-us/articles/4402955480215-Manage-the-Couchbase-Connector) | N/A | |
| [Dremio](https://devnet.logianalytics.com/hc/en-us/articles/4402955481111-Manage-the-Dremio-Connector) | N/A | |
| [Elasticsearch 6.0](https://devnet.logianalytics.com/hc/en-us/articles/4402962910999-Manage-the-Elasticsearch-Connector) | **Y** | |
| [Elasticsearch 7.0](https://devnet.logianalytics.com/hc/en-us/articles/4402962910999-Manage-the-Elasticsearch-Connector) | **Y** | |
| [Flat File](https://devnet.logianalytics.com/hc/en-us/articles/4402962915095-Upload-a-Flat-File-into-Composer) | N/A | |
| [HDFS](https://devnet.logianalytics.com/hc/en-us/articles/4402962915863-Manage-the-HDFS-Connector) | N/A | |
| [Hive](https://devnet.logianalytics.com/hc/en-us/articles/4402955487255-Manage-the-Hive-Connector) | N/A | |
| [MemSQL](https://devnet.logianalytics.com/hc/en-us/articles/4402962917527-Manage-the-MemSQL-Connector) | N/A | |
| [Microsoft SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/4402962918423-Manage-the-Microsoft-SQL-Server-Connector) | N/A | |
| [MongoDB](https://devnet.logianalytics.com/hc/en-us/articles/4402955487895-Manage-the-MongoDB-Connector) | N/A | |
| [MySQL](https://devnet.logianalytics.com/hc/en-us/articles/4402955488535-Manage-the-MySQL-Connector) | N/A | |
| [Oracle](https://devnet.logianalytics.com/hc/en-us/articles/4402962919319-Manage-the-Oracle-Connector) | N/A | |
| [PostgreSQL](https://devnet.logianalytics.com/hc/en-us/articles/4402962920087-Manage-the-PostgreSQL-Connector) | N/A | |
| [Presto](https://devnet.logianalytics.com/hc/en-us/articles/4402955489303-Manage-the-Presto-Connector) | N/A | |
| [Real Time Sales](https://devnet.logianalytics.com/hc/en-us/articles/4402955489943-Manage-the-Real-Time-Sales-Demo-Source) | N/A | |
| [SAP Hana](https://devnet.logianalytics.com/hc/en-us/articles/4402955490583-Manage-the-SAP-Hana-Connector) | N/A | |
| [SAP IQ](https://devnet.logianalytics.com/hc/en-us/articles/4402955491223-Manage-the-SAP-IQ-Connector) | N/A | |
| [Snowflake](https://devnet.logianalytics.com/hc/en-us/articles/4402955491863-Manage-the-Snowflake-Connector) | N/A | |
| [Spark SQL](https://devnet.logianalytics.com/hc/en-us/articles/4402955492503-Manage-the-Spark-SQL-Connector) | N/A | |
| [Teradata](https://devnet.logianalytics.com/hc/en-us/articles/4402962923159-Manage-the-Teradata-Connector) | N/A | |
| [TIBCO DV](https://devnet.logianalytics.com/hc/en-us/articles/4402955493143-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | N/A | |
| [Upload API](https://devnet.logianalytics.com/hc/en-us/articles/4402962872599-Use-the-Upload-API) | N/A | |
| [Vertica](https://devnet.logianalytics.com/hc/en-us/articles/4402962927255-Manage-the-Vertica-Connector) | N/A | |
