---
title: "Kerberos Authentication for Connectors"
id: 6988519094039
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/6988519094039-Kerberos-Authentication-for-Connectors
updated_at: 2022-06-23T20:00:43Z
---

# Kerberos Authentication for Connectors

# Kerberos Authentication for Connectors

Kerberos is an enterprise authentication protocol that uses the concept of tickets and three-way authentication to enable users and computers to identify themselves and secure access to resources. Kerberos support does not apply to some connectors.

Support for this feature by Composer connectors is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? | | | Notes |
| --- | --- | --- | --- | --- |
| [Amazon Redshift](https://devnet.logianalytics.com/hc/en-us/articles/4405859198103-Manage-the-Amazon-Redshift-Connector) | **N** | | |  |
| [Amazon S3](https://devnet.logianalytics.com/hc/en-us/articles/4405850929943-Manage-the-Amazon-S3-Connector) | **N** | | |  |
| [Apache Drill](https://devnet.logianalytics.com/hc/en-us/articles/4405850930839-Manage-the-Apache-Drill-Connector) | **Y** | | |  |
| [Apache Phoenix](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) | **Y** | | | Apache Phoenix supports Kerberos, but Apache Phoenix Query Server does not. For more information, see [*Enable Kerberos Authentication for Apache Phoenix Connectors*](https://devnet.logianalytics.com/hc/en-us/articles/4405850933527-Enable-Kerberos-Authentication-for-Apache-Phoenix-Connectors). |
| [Apache Phoenix Query Server (QS)](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) | **N** | | |
| [Apache Solr](https://devnet.logianalytics.com/hc/en-us/articles/4405850931735-Manage-the-Apache-Solr-Connector) | **Y** | | |  |
| [BigQuery](https://devnet.logianalytics.com/hc/en-us/articles/4405859214231-Manage-the-BigQuery-Connector) | N/A | | |  |
| [Cloudera Impala](https://devnet.logianalytics.com/hc/en-us/articles/4405850938647-Manage-the-Impala-Connector) | **Y** | | |  |
| [Cloudera Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859219863-Manage-the-Cloudera-Search-Connector) | **Y** | | |  |
| [Couchbase](https://devnet.logianalytics.com/hc/en-us/articles/4405859220887-Manage-the-Couchbase-Connector) | N/A | | |  |
| [Dremio](https://devnet.logianalytics.com/hc/en-us/articles/4405859221911-Manage-the-Dremio-Connector) | **N** | | |  |
| [Elasticsearch 6.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) | **N** | | |  |
| [Elasticsearch 7.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) | **N** | | |
| [Flat File](https://devnet.logianalytics.com/hc/en-us/articles/4405850954647-Upload-a-Flat-File-into-Composer) | **N** | | |  |
| [HDFS](https://devnet.logianalytics.com/hc/en-us/articles/4405859226903-Manage-the-HDFS-Connector) | **Y** | | |  |
| [Hive](https://devnet.logianalytics.com/hc/en-us/articles/4405850956695-Manage-the-Hive-Connector) | **Y** | | |  |
| [MemSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405859228567-Manage-the-MemSQL-Connector) | **N** | | |  |
| [Microsoft SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/4405859229975-Manage-the-Microsoft-SQL-Server-Connector) | **N** | | |  |
| [MongoDB](https://devnet.logianalytics.com/hc/en-us/articles/4405850957591-Manage-the-MongoDB-Connector) | **N** | | |  |
| [MySQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850958487-Manage-the-MySQL-Connector) | **N** | | |  |
| [Oracle](https://devnet.logianalytics.com/hc/en-us/articles/4405850959383-Manage-the-Oracle-Connector) | **N** | | |  |
| [PostgreSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850960279-Manage-the-PostgreSQL-Connector) | **N** | | |  |
| [Presto](https://devnet.logianalytics.com/hc/en-us/articles/4405859231639-Manage-the-Presto-Connector) | **N** | | |  |
| [Real Time Sales](https://devnet.logianalytics.com/hc/en-us/articles/4405850962071-Manage-the-Real-Time-Sales-Demo-Source) | N/A | | |  |
| [SAP Hana](https://devnet.logianalytics.com/hc/en-us/articles/4405859232791-Manage-the-SAP-Hana-Connector) | **N** | | |  |
| [SAP IQ](https://devnet.logianalytics.com/hc/en-us/articles/4405850963095-Manage-the-SAP-IQ-Connector) | **Y** | | |  |
| [Snowflake](https://devnet.logianalytics.com/hc/en-us/articles/4405859234199-Manage-the-Snowflake-Connector) | **N** | | |  |
| [Spark SQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850963991-Manage-the-Spark-SQL-Connector) | **Y** | | | To enable Kerberos authentication for Spark SQL connectors, see [*Connect to Spark SQL Sources on a Kerberized HDP Cluster*](https://devnet.logianalytics.com/hc/en-us/articles/4405850964887-Connect-to-Spark-SQL-Sources-on-a-Kerberized-HDP-Cluster). |
| [Teradata](https://devnet.logianalytics.com/hc/en-us/articles/4405859235607-Manage-the-Teradata-Connector) | **N** | | |  |
| [TIBCO DV](https://devnet.logianalytics.com/hc/en-us/articles/4405850965783-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | **N** | | |  |
| [Upload API](https://devnet.logianalytics.com/hc/en-us/articles/4405859140247-Use-the-Upload-API) | **N** | | |  |
| [Vertica](https://devnet.logianalytics.com/hc/en-us/articles/4405850966679-Manage-the-Vertica-Connector) | **N** | | |  |
