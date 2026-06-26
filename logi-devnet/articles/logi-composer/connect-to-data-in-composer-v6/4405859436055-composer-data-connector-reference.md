---
title: "Composer Data Connector Reference"
id: 4405859436055
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859436055-Composer-Data-Connector-Reference
updated_at: 2021-09-21T01:29:20Z
---

# Composer Data Connector Reference

# Composer Data Connector Reference

Composer data connectors are used to connect to your data stores. Each data connector has capabilities and limitations when connected to the Composer server. This topic highlights those details and provides a link to more information about each connector. For information about setting the parameters required by a connector to connect to a data store, see [*Manage Data Store Connections*](https://devnet.logianalytics.com/hc/en-us/articles/4405850909079-Manage-Data-Store-Connections). For information on how to download and install a connector that is not provided in the default Composer installation, see [*Obtain Additional Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405850923799-Obtain-Additional-Connector-Servers).

| Connector | Microservice | Supported Versions | Connector Port | Other Actions Required & Notes |
| --- | --- | --- | --- | --- |
| [Amazon Redshift](https://devnet.logianalytics.com/hc/en-us/articles/4405859198103-Manage-the-Amazon-Redshift-Connector) | `zoomdata-edc-redshift` | 1.0 | 8202 | Install JDBC driver |
| [Amazon S3](https://devnet.logianalytics.com/hc/en-us/articles/4405850929943-Manage-the-Amazon-S3-Connector) | `zoomdata-edc-s3` |  | 8129 | Separate download |
| [Apache Drill](https://devnet.logianalytics.com/hc/en-us/articles/4405850930839-Manage-the-Apache-Drill-Connector) | `zoomdata-edc-drill` | 1.14 - 1.16 | 8095 | Separate download |
| [Apache Phoenix](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) | `zoomdata-edc-phoenix-4.7` | 4.7 | 8124 | Apache Phoenix 4.4 and 4.5 require separate downloads |
| [Apache Phoenix Query Server (QS)](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) | `zoomdata-edc-phoenix-4.7-queryserver` | 4.7 | 8125 |  |
| [Apache Solr](https://devnet.logianalytics.com/hc/en-us/articles/4405850931735-Manage-the-Apache-Solr-Connector) | `zoomdata-edc-apache-solr` | 7.4 - 8.4 | 8115 |  |
| [BigQuery](https://devnet.logianalytics.com/hc/en-us/articles/4405859214231-Manage-the-BigQuery-Connector) | `zoomdata-edc-bigquery` |  | 8093 |  |
| [Cloudera Impala](https://devnet.logianalytics.com/hc/en-us/articles/4405850938647-Manage-the-Impala-Connector) | `zoomdata-edc-impala` | 2.7 - 3.2 | 8098 |  |
| [Cloudera Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859219863-Manage-the-Cloudera-Search-Connector) | `zoomdata-edc-cloudera-search` | 4.10 - 7.4 | 8201 |  |
| [Couchbase](https://devnet.logianalytics.com/hc/en-us/articles/4405859220887-Manage-the-Couchbase-Connector) | `zoomdata-edc-couchbase` | 6.0.1 | 8138 | Includes Couchbase Community Edition 6.0.0 |
| [Dremio](https://devnet.logianalytics.com/hc/en-us/articles/4405859221911-Manage-the-Dremio-Connector) | `zoomdata-edc-dremio` | 4.1 through 4.8 | 8142 |  |
| [Elasticsearch 6.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) | `zoomdata-edc-elasticsearch-6.0` | 6.0 - 6.8 | 8118 |  |
| [Elasticsearch 7.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) | `zoomdata-edc-elasticsearch-7.0` | 7.0 - 7.12 | 8139 |  |
| [HDFS](https://devnet.logianalytics.com/hc/en-us/articles/4405859226903-Manage-the-HDFS-Connector) | `zoomdata-edc-hdfs` |  | 8126 | Separate download |
| [Hive](https://devnet.logianalytics.com/hc/en-us/articles/4405850956695-Manage-the-Hive-Connector) | `zoomdata-edc-hive` | 2.1 - 3.1 | 8132 |  |
| [MemSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405859228567-Manage-the-MemSQL-Connector) | `zoomdata-edc-memsql` | 6.0 - 6.7 | 8099 | Install JDBC driver |
| [Microsoft SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/4405859229975-Manage-the-Microsoft-SQL-Server-Connector) | `zoomdata-edc-mssql` | 2008 R2 and 2019 (specifically, versions 10.5 - 15.0.2000) | 8100 |  |
| [MongoDB](https://devnet.logianalytics.com/hc/en-us/articles/4405850957591-Manage-the-MongoDB-Connector) | `zoomdata-edc-mongo` | 3.4 - 4.4 | 8123 |  |
| [MySQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850958487-Manage-the-MySQL-Connector) | `zoomdata-edc-mysql` | 5.6 - 8.0 | 8101 | Install JDBC driver |
| [Oracle](https://devnet.logianalytics.com/hc/en-us/articles/4405850959383-Manage-the-Oracle-Connector) | `zoomdata-edc-oracle` | 11.2 - 18.3 | 8102 | Install JDBC driver |
| [PostgreSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850960279-Manage-the-PostgreSQL-Connector) | `zoomdata-edc-postgresql` | 9.4 - 12.1 | 8105 |  |
| [Presto](https://devnet.logianalytics.com/hc/en-us/articles/4405859231639-Manage-the-Presto-Connector) | `zoomdata-edc-presto` | 319 | 8107 | Separate download; used to [connect to Cassandra databases](https://devnet.logianalytics.com/hc/en-us/articles/4405850961175-Connect-to-Cassandra-Databases-Using-Presto). |
| [Real Time Sales](https://devnet.logianalytics.com/hc/en-us/articles/4405850962071-Manage-the-Real-Time-Sales-Demo-Source) | `zoomdata-edc-rts` |  | 8108 | Must be enabled |
| [SAP Hana](https://devnet.logianalytics.com/hc/en-us/articles/4405859232791-Manage-the-SAP-Hana-Connector) | `zoomdata-edc-saphana` | 2.0 | 8109 | Separate download and install JDBC driver |
| [SAP IQ](https://devnet.logianalytics.com/hc/en-us/articles/4405850963095-Manage-the-SAP-IQ-Connector) | `zoomdata-edc-sapiq` | 16 | 8121 | Separate download and install JDBC driver |
| [Snowflake](https://devnet.logianalytics.com/hc/en-us/articles/4405859234199-Manage-the-Snowflake-Connector) | `zoomdata-edc-snowflake` | whatever is currently supported in the cloud | 8131 | Separate download |
| [Spark SQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850963991-Manage-the-Spark-SQL-Connector) | `zoomdata-edc-sparksql` | 2.3 - 3.0 | 8116 |  |
| [Teradata](https://devnet.logianalytics.com/hc/en-us/articles/4405859235607-Manage-the-Teradata-Connector) | `zoomdata-edc-teradata` | 16.20 | 8111 | Separate download and install JDBC driver |
| [TIBCO DV](https://devnet.logianalytics.com/hc/en-us/articles/4405850965783-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | `zoomdata-edc-tibcodv` | 8.0-8.1 | 8140 | Separate download and install JDBC driver  The default TDV server port for JDBC connections is 9401. |
| [Vertica](https://devnet.logianalytics.com/hc/en-us/articles/4405850966679-Manage-the-Vertica-Connector) | `zoomdata-edc-vertica` | 7.2 | 8112 | Separate download and install JDBC driver |

In addition to the official Composer connectors listed above, Composer allows you to :

* Upload a [flat file](https://devnet.logianalytics.com/hc/en-us/articles/4405850954647-Upload-a-Flat-File-into-Composer) for viewing in visuals and dashboards.
* Dynamically upload and stream your data in real time using the Composer [Upload API](https://devnet.logianalytics.com/hc/en-us/articles/4405859140247-Use-the-Upload-API).

Both the [flat file uploads](https://devnet.logianalytics.com/hc/en-us/articles/4405850954647-Upload-a-Flat-File-into-Composer) and the [Upload API](https://devnet.logianalytics.com/hc/en-us/articles/4405859140247-Use-the-Upload-API) use port 8105 and require that PostgreSQL be enabled. While these processes are not strictly data connectors, they are additional methods of providing data for Composer.
