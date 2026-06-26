---
title: "Fast Distinct Values"
id: 34932715069197
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715069197-Fast-Distinct-Values
updated_at: 2026-05-26T22:06:25Z
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
| [Amazon Redshift](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932733806989-Manage-the-Amazon-Redshift-Connector) | N/A |
| [Amazon S3](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743032461-Manage-the-Amazon-S3-Connector) | N/A |
| [Apache Drill](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932734193677-Manage-the-Apache-Drill-Connector) | N/A |
| [Apache Phoenix](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743401869-Manage-the-Apache-Phoenix-Connector) | N/A |
| [Apache Phoenix Query Server (QS)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743401869-Manage-the-Apache-Phoenix-Connector) | N/A |
| [Apache Solr](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743530125-Manage-the-Apache-Solr-Connector) | **Y** |
| [BigQuery](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932735000973-Manage-the-BigQuery-Connector) | N/A |
| [Business Central Jet](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932747192973-Manage-the-Business-Central-Jet-Connector) | N/A |
| [Cloudera Impala](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932744502541-Manage-the-Impala-Connector) | N/A |
| [Cloudera Search](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932696536461-Manage-the-Cloudera-Search-Connector) | **Y** |
| [Couchbase](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932720313229-Manage-the-Couchbase-Connector) | N/A |
| [Dremio](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728091149-Manage-the-Dremio-Connector) | N/A |
| [Elasticsearch 7.0](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector) | **Y** |
| [Elasticsearch 8.0](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector) | **Y** |
| [File Upload](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932721668365-Manage-File-Uploads) | N/A |
| [HDFS](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932746629773-Manage-the-HDFS-Connector) | N/A |
| [Hive](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932766095885-Manage-the-Hive-Connector) | N/A |
| [Jira](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932766172941-Manage-the-Jira-Connector) | **N** |
| [MemSQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932747006861-Manage-the-MemSQL-Connector) | N/A |
| [Microsoft SQL Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730176653-Manage-the-Microsoft-SQL-Server-Connector) | N/A |
| [MongoDB](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932729901069-Manage-the-MongoDB-Connector) | N/A |
| [MySQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730297485-Manage-the-MySQL-Connector) | N/A |
| [OpenSearch](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515138873485-Manage-the-OpenSearch-Connector) | **Y** |
| [Oracle](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730448653-Manage-the-Oracle-Connector) | N/A |
| [PostgreSQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932749503629-Manage-the-PostgreSQL-Connector) | N/A |
| [Python](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932738470925-Manage-the-Python-Connector) | **N** |
| [Real Time Sales](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932767352077-Manage-the-Real-Time-Sales-Demo-Source) | N/A |
| [Salesforce](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932756901901-Manage-the-Salesforce-Connector) | **N** |
| [SAP Hana](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932798573197-Manage-the-SAP-Hana-Connector) | N/A |
| [SAP S/4HANA](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932767840781-Manage-the-SAP-S-4HANA-Connector) | N/A |
| [SAP IQ](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932757142925-Manage-the-SAP-IQ-Connector) | N/A |
| [Spark SQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932799029901-Manage-the-Spark-SQL-Connector) | N/A |
| [Snowflake](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932757334669-Manage-the-Snowflake-Connector) | N/A |
| [Teradata](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932773152781-Manage-the-Teradata-Connector) | N/A |
| [TIBCO DV](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932768245901-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | N/A |
| [Trino](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932773334285-Manage-the-Trino-Connector) | N/A |
| [File Upload (Upload API)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932721668365-Manage-File-Uploads) | N/A |
| [Vertica](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932768403725-Manage-the-Vertica-Connector) | N/A |
