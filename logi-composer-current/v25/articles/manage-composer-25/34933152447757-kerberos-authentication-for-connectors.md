---
title: "Kerberos Authentication for Connectors"
id: 34933152447757
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933152447757-Kerberos-Authentication-for-Connectors
updated_at: 2026-05-26T22:08:07Z
---

# Kerberos Authentication for Connectors

# Kerberos Authentication for Connectors

Kerberos is an enterprise authentication protocol that uses the concept of tickets and three-way authentication to enable users and computers to identify themselves and secure access to resources.
Kerberos support does not apply to some connectors.

Support for this feature by connector is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? | Notes |
| --- | --- | --- |
| [Amazon Redshift](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932733806989-Manage-the-Amazon-Redshift-Connector) | **N** |  |
| [Amazon S3](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743032461-Manage-the-Amazon-S3-Connector) | **N** |  |
| [Apache Drill](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932734193677-Manage-the-Apache-Drill-Connector) | **Y** |  |
| [Apache Phoenix](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743401869-Manage-the-Apache-Phoenix-Connector) | **Y** | Apache Phoenix supports Kerberos, but Apache Phoenix Query Server does not. For more information, see [Enable Kerberos Authentication for Apache Phoenix Connectors](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932719212429-Enable-Kerberos-Authentication-for-Apache-Phoenix-Connectors). |
| [Apache Phoenix Query Server (QS)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743401869-Manage-the-Apache-Phoenix-Connector) | **N** |
| [Apache Solr](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743530125-Manage-the-Apache-Solr-Connector) | **Y** |  |
| [BigQuery](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932735000973-Manage-the-BigQuery-Connector) | **N** | If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`. |
| [Cloudera Impala](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932744502541-Manage-the-Impala-Connector) | **Y** |  |
| [Cloudera Search](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932696536461-Manage-the-Cloudera-Search-Connector) | **Y** |  |
| [Couchbase](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932720313229-Manage-the-Couchbase-Connector) | N/A |  |
| [Dremio](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728091149-Manage-the-Dremio-Connector) | **N** |  |
| [Elasticsearch 7.0](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector) | **N** |  |
| [Elasticsearch 8.0](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector) | **N** |
| [File Upload](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932721668365-Manage-File-Uploads) | **N** |  |
| [HDFS](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932746629773-Manage-the-HDFS-Connector) | **Y** |  |
| [Hive](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932766095885-Manage-the-Hive-Connector) | **Y** |  |
| [Jira](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932766172941-Manage-the-Jira-Connector) | **N** |  |
| [MemSQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932747006861-Manage-the-MemSQL-Connector) | **N** |  |
| [Microsoft SQL Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730176653-Manage-the-Microsoft-SQL-Server-Connector) | **N** |  |
| [MongoDB](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932729901069-Manage-the-MongoDB-Connector) | **N** |  |
| [MySQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730297485-Manage-the-MySQL-Connector) | **N** |  |
| [Oracle](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730448653-Manage-the-Oracle-Connector) | **N** |  |
| [PostgreSQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932749503629-Manage-the-PostgreSQL-Connector) | **N** |  |
| [Python](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932738470925-Manage-the-Python-Connector) | **N** |  |
| [Real Time Sales](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932767352077-Manage-the-Real-Time-Sales-Demo-Source) | N/A |  |
| [Salesforce](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932756901901-Manage-the-Salesforce-Connector) | **N** |  |
| [SAP Hana](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932798573197-Manage-the-SAP-Hana-Connector) | **N** |  |
| [SAP S/4HANA](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932767840781-Manage-the-SAP-S-4HANA-Connector) | **N** |  |
| [SAP IQ](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932757142925-Manage-the-SAP-IQ-Connector) | **Y** |  |
| [Spark SQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932799029901-Manage-the-Spark-SQL-Connector) | **Y** | To enable Kerberos authentication for Spark SQL connectors, see [Connect to Spark SQL Sources on a Kerberized HDP Cluster](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932768085773-Connect-to-Spark-SQL-Sources-on-a-Kerberized-HDP-Cluster). |
| [Snowflake](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932757334669-Manage-the-Snowflake-Connector) | **N** |  |
| [Teradata](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932773152781-Manage-the-Teradata-Connector) | **N** |  |
| [TIBCO DV](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932768245901-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | **N** |  |
| [Trino](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932773334285-Manage-the-Trino-Connector) | **N** |  |
| [File Upload (Upload API)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932721668365-Manage-File-Uploads) | **N** |  |
| [Vertica](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932768403725-Manage-the-Vertica-Connector) | **N** |  |
