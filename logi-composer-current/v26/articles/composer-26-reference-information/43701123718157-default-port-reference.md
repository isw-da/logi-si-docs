---
title: "Default Port Reference"
id: 43701123718157
section: "Composer 26 Reference Information"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701123718157-Default-Port-Reference
updated_at: 2026-05-29T14:09:14Z
---

# Default Port Reference

# Default Port Reference

The following table lists the default ports used by Composer, sorted by port number.

| Port | Microservice | Description |
| --- | --- | --- |
| 80 | data gateway service | The port for the [data gateway service](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701209528205-Set-Up-and-Use-the-Data-Gateway-Service). |
| 443 | `zoomdata` | Composer server web communication.  For HTTPS requests, configure your firewall to map port 443 to either port 8443 or port 8080. |
| 5432 | `zoomdata-postgres` | Composer [metadata repository](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701122518797-Metadata-Repository). |
| 5580 | `zoomdata-query-engine` | Composer [query engine](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701037846797-Manage-the-Composer-Query-Engine) microservice. |
| 8050 | `zoomdata-admin-server` | [Service Monitor](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701149014925-Composer-Service-Monitor). |
| 8080 | `zoomdata` | Composer server. |
| 8081 | `zoomdata-data-writer` | Composer [Data Writer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701106979981-Data-Writer-Microservice) microservice. |
| 8083 | `zoomdata-screenshot-service` | Composer [Screenshot](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073104013-Set-Up-the-Screenshot-Microservice) microservice. |
| 8093 | `zoomdata-edc-bigquery` | [BigQuery](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009802509-Manage-the-BigQuery-Connector) connector. |
| 8095 | `zoomdata-edc-drill` | [Apache Drill](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042973581-Manage-the-Apache-Drill-Connector) connector. |
| 8098 | `zoomdata-edc-impala` | [Cloudera Impala](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025595405-Manage-the-Impala-Connector) connector. |
| 8099 | `zoomdata-edc-memsql` | [MemSQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011116173-Manage-the-MemSQL-Connector) connector. |
| 8100 | `zoomdata-edc-mssql` | [Microsoft SQL Server](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026525069-Manage-the-Microsoft-SQL-Server-Connector) connector. |
| 8101 | `zoomdata-edc-mysql` | [MySQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044330253-Manage-the-MySQL-Connector) connector. |
| 8102 | `zoomdata-edc-oracle` | [Oracle](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011976717-Manage-the-Oracle-Connector) connector. |
| 8105 | `zoomdata-edc-postgresql` | [PostgreSQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701091160973-Manage-the-PostgreSQL-Connector) connector, [Flat File](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads) and API uploads for processing. |
| 8108 | `zoomdata-edc-rts` | [Real Time Sales](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027022221-Manage-the-Real-Time-Sales-Demo-Source) connector. |
| 8109 | `zoomdata-edc-saphana` | [SAP Hana](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701012179469-Manage-the-SAP-Hana-Connector) connector. |
| 8111 | `zoomdata-edc-teradata` | [Teradata](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701091479437-Manage-the-Teradata-Connector) connector. |
| 8112 | `zoomdata-edc-vertica` | [Vertica](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027298189-Manage-the-Vertica-Connector) connector. |
| 8115 | `zoomdata-edc-apache-solr` | [Apache Solr](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043021325-Manage-the-Apache-Solr-Connector) connector. |
| 8116 | `zoomdata-edc-sparksql` | [Spark SQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701012300173-Manage-the-Spark-SQL-Connector) connector. |
| 8121 | `zoomdata-edc-sapiq` | [SAP IQ](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996022669-Manage-the-SAP-IQ-Connector) connector. |
| 8123 | `zoomdata-edc-mongo` | [MongoDB](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026372749-Manage-the-MongoDB-Connector) connector. |
| 8124 | `zoomdata-edc-phoenix-4.7` | [Apache Phoenix](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025361549-Manage-the-Apache-Phoenix-Connector) connector. |
| 8125 | `zoomdata-edc-phoenix-4.7-queryserver` | [Apache Phoenix Query Server (QS)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025361549-Manage-the-Apache-Phoenix-Connector) connector. |
| 8126 | `zoomdata-edc-hdfs` | [HDFS](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700995161101-Manage-the-HDFS-Connector) connector. |
| 8129 | `zoomdata-edc-s3` | [Amazon S3](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009509517-Manage-the-Amazon-S3-Connector) connector. |
| 8131 | `zoomdata-edc-snowflake` | [Snowflake](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074814989-Manage-the-Snowflake-Connector) connector. |
| 8132 | `zoomdata-edc-hive` | [Hive](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026308493-Manage-the-Hive-Connector) connector. |
| 8138 | `zoomdata-edc-couchbase` | [Couchbase](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701040183821-Manage-the-Couchbase-Connector) connector. |
| 8139 | `zoomdata-edc-elasticsearch-7.0` | [Elasticsearch 7.0](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector) connector. |
| 8140 | `zoomdata-edc-tibcodv` | [TIBCO DV](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996158349-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) connector. |
| 8142 | `zoomdata-edc-dremio` | [Dremio](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043446285-Manage-the-Dremio-Connector) connector. |
| 8147 | `zoomdata-edc-elasticsearch-8-0` | [Elasticsearch 8.0](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector) connector. |
| 8148 | `zoomdata-edc-trino` | [Trino](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701045148045-Manage-the-Trino-Connector) connector. |
| 8201 | `zoomdata-edc-cloudera-search` | [Cloudera Search](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009985933-Manage-the-Cloudera-Search-Connector) connector. |
| 8202 | `zoomdata-edc-redshift` | [Amazon Redshift](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009454477-Manage-the-Amazon-Redshift-Connector) connector. |
| 8205 | `zoomdata-edc-saphanacloud` | [SAP S/4HANA](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996045069-Manage-the-SAP-S-4HANA-Connector) connector. |
| 8300 | `zoomdata-consul` | Internal port used by the Consul for inter-node communication in a distributed environment. |
| 8301 | `zoomdata-consul` | Internal port used by the Consul for inter-node communication in a distributed environment. |
| 8302 | `zoomdata-consul` | Internal port used by the Consul for inter-node communication in a distributed environment. |
| 8443 | `zoomdata` | Composer HTTPS requests. |
| 8500 | `zoomdata-consul` | Consul. |
| 8888 | `zoomdata-config-server` | Composer [configuration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136628877-Configuration-Microservice) microservice. |
