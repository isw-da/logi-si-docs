---
title: "Data Connector Reference"
id: 43701113495693
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113495693-Data-Connector-Reference
updated_at: 2026-05-29T14:09:11Z
---

# Data Connector Reference

# Data Connector Reference

Composer data connectors are used to connect to your data stores. Each data connector has capabilities and limitations when connected to the Composer server. This topic highlights those details and provides a link to more information about each connector. For information about setting the parameters required by a connector to connect to a data store, see [Manage Data Store Connections](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038107149-Manage-Data-Store-Connections). For information on how to download and install a connector that is not provided in the default Composer installation, see [Obtain Additional Connector Servers](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701024898061-Obtain-Additional-Connector-Servers).

| Connector | Microservice | Supported Versions | Connector Port | Other Actions Required & Notes |
| --- | --- | --- | --- | --- |
| [Amazon Redshift](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009454477-Manage-the-Amazon-Redshift-Connector) | `zoomdata-edc-redshift` | 1.0 | 8202 | Install JDBC driver. |
| [Amazon S3](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009509517-Manage-the-Amazon-S3-Connector) | `zoomdata-edc-s3` |  | 8129 | Separate download. |
| [Apache Drill](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042973581-Manage-the-Apache-Drill-Connector) | `zoomdata-edc-drill` | 1.14 - 1.16 | 8095 | Separate download. |
| [Apache Phoenix](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025361549-Manage-the-Apache-Phoenix-Connector) | `zoomdata-edc-phoenix-4.7` | 4.7 | 8124 | Apache Phoenix 4.4 and 4.5 require separate downloads. |
| [Apache Phoenix Query Server (QS)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025361549-Manage-the-Apache-Phoenix-Connector) | `zoomdata-edc-phoenix-4.7-queryserver` | 4.7 | 8125 |  |
| [Apache Solr](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043021325-Manage-the-Apache-Solr-Connector) | `zoomdata-edc-apache-solr` | 7.4 - 8.4 | 8115 |  |
| [BigQuery](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009802509-Manage-the-BigQuery-Connector) | `zoomdata-edc-bigquery` |  | 8093 |  |
| [Business Central](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701057330957-Manage-the-Business-Central-Jet-Connector) | `zoomdata-edc-businesscentral-jet` | N/A | 8156 | Separate download. |
| [Cloudera Impala](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025595405-Manage-the-Impala-Connector) | `zoomdata-edc-impala` | 3.2 - 3.4 | 8098 |  |
| [Cloudera Search](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009985933-Manage-the-Cloudera-Search-Connector) | `zoomdata-edc-cloudera-search` | 4.10 - 7.4 | 8201 |  |
| [Couchbase](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701040183821-Manage-the-Couchbase-Connector) | `zoomdata-edc-couchbase` | 6.0.1 | 8138 | Includes Couchbase Community Edition 6.0.0. |
| [Dremio](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043446285-Manage-the-Dremio-Connector) | `zoomdata-edc-dremio` | 4.1 through 4.8 | 8142 |  |
| [Elasticsearch 7.0](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector) | `zoomdata-edc-elasticsearch-7.0` | 7.0 - 7.17 | 8139 |  |
| [Elasticsearch 8.0](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector) | `zoomdata-edc-elasticsearch-8-0` | 8.1 - 8.3 | 8147 |  |
| [HDFS](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700995161101-Manage-the-HDFS-Connector) | `zoomdata-edc-hdfs` |  | 8126 | Separate download. |
| [Hive](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026308493-Manage-the-Hive-Connector) | `zoomdata-edc-hive` | 2.1 - 3.1 | 8132 |  |
| [Jira Connector](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044185229-Manage-the-Jira-Connector) | `zoomdata-edc-jira` | Jira JDBC Driver 1.7.8.1002 | 8151 | Separate download. |
| [MemSQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011116173-Manage-the-MemSQL-Connector) | `zoomdata-edc-memsql` | 7.1 - 7.6 | 8099 | Install JDBC driver. |
| [Microsoft SQL Server](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026525069-Manage-the-Microsoft-SQL-Server-Connector) | `zoomdata-edc-mssql` | 12.0 (SQL Server 2014) - 16.0 (SQL Server 2022) | 8100 |  |
| [MongoDB](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026372749-Manage-the-MongoDB-Connector) | `zoomdata-edc-mongo` | 3.4 - 4.4 | 8123 |  |
| [MySQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044330253-Manage-the-MySQL-Connector) | `zoomdata-edc-mysql` | 5.6 - 8.0 | 8101 | Install JDBC driver. |
| [Oracle](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011976717-Manage-the-Oracle-Connector) | `zoomdata-edc-oracle` | 11.2 - 21c | 8102 | Install JDBC driver. |
| [OpenSearch](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074183053-Manage-the-OpenSearch-Connector) | `zoomdata-edc-opensearch` | 2.x to 2.17 | 8134 |  |
| [PostgreSQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701091160973-Manage-the-PostgreSQL-Connector) | `zoomdata-edc-postgresql` | 9.6 - 14.0 | 8105 |  |
| [Python](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074664333-Manage-the-Python-Connector) | `zoomdata-edc-python` |  | 8153 | Install Docker image. See [Manage the Python Connector](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074664333-Manage-the-Python-Connector). |
| [Real Time Sales](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027022221-Manage-the-Real-Time-Sales-Demo-Source) | `zoomdata-edc-rts` |  | 8108 | Must be enabled. |
| [Salesforce](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074738317-Manage-the-Salesforce-Connector) | `zoomdata-edc-salesforce` | Simba Salesforce JDBC Driver 2.1.22 | 8152 | Separate download. |
| [SAP Hana](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701012179469-Manage-the-SAP-Hana-Connector) | `zoomdata-edc-saphana` | 2.0 | 8109 | Separate download and install JDBC driver. |
| [SAP S/4HANA](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996045069-Manage-the-SAP-S-4HANA-Connector) | `zoomdata-edc-saphanacloud` | N/A | 8205 | Separate download and install JDBC driver. |
| [SAP IQ](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996022669-Manage-the-SAP-IQ-Connector) | `zoomdata-edc-sapiq` | 16 | 8121 | Separate download and install JDBC driver. |
| [Snowflake](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074814989-Manage-the-Snowflake-Connector) | `zoomdata-edc-snowflake` | whatever is currently supported in the cloud | 8131 | Separate download. |
| [Spark SQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701012300173-Manage-the-Spark-SQL-Connector) | `zoomdata-edc-sparksql` | 2.3 - 3.0 | 8116 |  |
| [Teradata](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701091479437-Manage-the-Teradata-Connector) | `zoomdata-edc-teradata` | 16.20 | 8111 | Separate download and install JDBC driver. |
| [TIBCO DV](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996158349-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | `zoomdata-edc-tibcodv` | 8.0-8.1 | 8140 | Separate download and install JDBC driver.  The default TDV server port for JDBC connections is 9401. |
| [Trino](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701045148045-Manage-the-Trino-Connector) | `zoomdata-edc-trino` | 351-390 | 8148 | Separate download. |
| [Vertica](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027298189-Manage-the-Vertica-Connector) | `zoomdata-edc-vertica` | 7.2 | 8112 | Separate download and install JDBC driver. |

In addition to the official Composer connectors listed above, Composer allows you to:

* Upload a [flat file](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads) for viewing in visuals and dashboards.
* Dynamically upload and stream your data in real time using the Composer [Upload API](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads#Working).

Both the [flat file uploads](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads) and the [Upload API](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads#Working) use port 8105 and require that PostgreSQL be enabled. While these processes are not strictly data connectors, they are additional methods of providing data for Composer.
