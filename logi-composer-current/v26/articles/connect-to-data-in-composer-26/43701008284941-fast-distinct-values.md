---
title: "Fast Distinct Values"
id: 43701008284941
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008284941-Fast-Distinct-Values
updated_at: 2026-05-29T14:07:26Z
---

# Fast Distinct Values

# Fast Distinct Values

Connectors that support fast distinct values can efficiently return distinct values for a field. This functionality optimizes the retrieval of distinct (unique) values in large numbers of records. If a connector supports this feature, the Filter dialog is populated with distinct values for an attribute directly from the data source, without the need to refresh the data and without retrieving or storing the distinct values in the metadata. For example, Elasticsearch keeps lists of distinct values at the ready. Features such as these make fast distinct values possible for your connector.

There is no metric that defines "fast". This value is based on the judgment of the developer.

When custom ranges or list values are requested for a field, full data scans are not performed.

For most connectors, this feature can be safely left disabled without impact.

Support for this feature by connector is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| --- | --- |
| [Amazon Redshift](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009454477-Manage-the-Amazon-Redshift-Connector) | N/A |
| [Amazon S3](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009509517-Manage-the-Amazon-S3-Connector) | N/A |
| [Apache Drill](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042973581-Manage-the-Apache-Drill-Connector) | N/A |
| [Apache Phoenix](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025361549-Manage-the-Apache-Phoenix-Connector) | N/A |
| [Apache Phoenix Query Server (QS)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025361549-Manage-the-Apache-Phoenix-Connector) | N/A |
| [Apache Solr](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043021325-Manage-the-Apache-Solr-Connector) | **Y** |
| [BigQuery](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009802509-Manage-the-BigQuery-Connector) | N/A |
| [Business Central Jet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701057330957-Manage-the-Business-Central-Jet-Connector) | N/A |
| [Cloudera Impala](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025595405-Manage-the-Impala-Connector) | N/A |
| [Cloudera Search](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009985933-Manage-the-Cloudera-Search-Connector) | **Y** |
| [Couchbase](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701040183821-Manage-the-Couchbase-Connector) | N/A |
| [Dremio](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043446285-Manage-the-Dremio-Connector) | N/A |
| [Elasticsearch 7.0](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector) | **Y** |
| [Elasticsearch 8.0](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector) | **Y** |
| [File Upload](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads) | N/A |
| [HDFS](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700995161101-Manage-the-HDFS-Connector) | N/A |
| [Hive](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026308493-Manage-the-Hive-Connector) | N/A |
| [Jira](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044185229-Manage-the-Jira-Connector) | **N** |
| [MemSQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011116173-Manage-the-MemSQL-Connector) | N/A |
| [Microsoft SQL Server](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026525069-Manage-the-Microsoft-SQL-Server-Connector) | N/A |
| [MongoDB](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026372749-Manage-the-MongoDB-Connector) | N/A |
| [MySQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044330253-Manage-the-MySQL-Connector) | N/A |
| [OpenSearch](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074183053-Manage-the-OpenSearch-Connector) | **Y** |
| [Oracle](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011976717-Manage-the-Oracle-Connector) | N/A |
| [PostgreSQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701091160973-Manage-the-PostgreSQL-Connector) | N/A |
| [Python](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074664333-Manage-the-Python-Connector) | **N** |
| [Real Time Sales](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027022221-Manage-the-Real-Time-Sales-Demo-Source) | N/A |
| [Salesforce](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074738317-Manage-the-Salesforce-Connector) | **N** |
| [SAP Hana](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701012179469-Manage-the-SAP-Hana-Connector) | N/A |
| [SAP S/4HANA](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996045069-Manage-the-SAP-S-4HANA-Connector) | N/A |
| [SAP IQ](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996022669-Manage-the-SAP-IQ-Connector) | N/A |
| [Spark SQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701012300173-Manage-the-Spark-SQL-Connector) | N/A |
| [Snowflake](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074814989-Manage-the-Snowflake-Connector) | N/A |
| [Teradata](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701091479437-Manage-the-Teradata-Connector) | N/A |
| [TIBCO DV](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996158349-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | N/A |
| [Trino](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701045148045-Manage-the-Trino-Connector) | N/A |
| [File Upload (Upload API)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads) | N/A |
| [Vertica](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027298189-Manage-the-Vertica-Connector) | N/A |
