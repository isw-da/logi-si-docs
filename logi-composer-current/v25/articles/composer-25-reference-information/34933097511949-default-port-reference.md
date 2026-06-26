---
title: "Default Port Reference"
id: 34933097511949
section: "Composer 25 Reference Information"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933097511949-Default-Port-Reference
updated_at: 2026-05-26T22:07:55Z
---

# Default Port Reference

# Default Port Reference

The following table lists the default ports used by Composer, sorted by port number.

| Port | Microservice | Description |
| --- | --- | --- |
| 80 | data gateway service | The port for the [data gateway service](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540530701-Set-Up-and-Use-the-Data-Gateway-Service). |
| 443 | `zoomdata` | Composer server web communication.  For HTTPS requests, configure your firewall to map port 443 to either port 8443 or port 8080. |
| 5432 | `zoomdata-postgres` | Composer [metadata repository](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933064302093-Metadata-Repository). |
| 5580 | `zoomdata-query-engine` | Composer [query engine](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932686805645-Manage-the-Composer-Query-Engine) microservice. |
| 8050 | `zoomdata-admin-server` | [Service Monitor](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933184901773-Composer-Service-Monitor). |
| 8080 | `zoomdata` | Composer server. |
| 8081 | `zoomdata-data-writer` | Composer [Data Writer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933071011725-Data-Writer-Microservice) microservice. |
| 8083 | `zoomdata-screenshot-service` | Composer [Screenshot](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933044663181-Set-Up-the-Screenshot-Microservice) microservice. |
| 8093 | `zoomdata-edc-bigquery` | [BigQuery](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932735000973-Manage-the-BigQuery-Connector) connector. |
| 8095 | `zoomdata-edc-drill` | [Apache Drill](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932734193677-Manage-the-Apache-Drill-Connector) connector. |
| 8098 | `zoomdata-edc-impala` | [Cloudera Impala](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932744502541-Manage-the-Impala-Connector) connector. |
| 8099 | `zoomdata-edc-memsql` | [MemSQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932747006861-Manage-the-MemSQL-Connector) connector. |
| 8100 | `zoomdata-edc-mssql` | [Microsoft SQL Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730176653-Manage-the-Microsoft-SQL-Server-Connector) connector. |
| 8101 | `zoomdata-edc-mysql` | [MySQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730297485-Manage-the-MySQL-Connector) connector. |
| 8102 | `zoomdata-edc-oracle` | [Oracle](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730448653-Manage-the-Oracle-Connector) connector. |
| 8105 | `zoomdata-edc-postgresql` | [PostgreSQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932749503629-Manage-the-PostgreSQL-Connector) connector, [Flat File](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932721668365-Manage-File-Uploads) and API uploads for processing. |
| 8108 | `zoomdata-edc-rts` | [Real Time Sales](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932767352077-Manage-the-Real-Time-Sales-Demo-Source) connector. |
| 8109 | `zoomdata-edc-saphana` | [SAP Hana](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932798573197-Manage-the-SAP-Hana-Connector) connector. |
| 8111 | `zoomdata-edc-teradata` | [Teradata](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932773152781-Manage-the-Teradata-Connector) connector. |
| 8112 | `zoomdata-edc-vertica` | [Vertica](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932768403725-Manage-the-Vertica-Connector) connector. |
| 8115 | `zoomdata-edc-apache-solr` | [Apache Solr](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743530125-Manage-the-Apache-Solr-Connector) connector. |
| 8116 | `zoomdata-edc-sparksql` | [Spark SQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932799029901-Manage-the-Spark-SQL-Connector) connector. |
| 8121 | `zoomdata-edc-sapiq` | [SAP IQ](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932757142925-Manage-the-SAP-IQ-Connector) connector. |
| 8123 | `zoomdata-edc-mongo` | [MongoDB](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932729901069-Manage-the-MongoDB-Connector) connector. |
| 8124 | `zoomdata-edc-phoenix-4.7` | [Apache Phoenix](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743401869-Manage-the-Apache-Phoenix-Connector) connector. |
| 8125 | `zoomdata-edc-phoenix-4.7-queryserver` | [Apache Phoenix Query Server (QS)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743401869-Manage-the-Apache-Phoenix-Connector) connector. |
| 8126 | `zoomdata-edc-hdfs` | [HDFS](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932746629773-Manage-the-HDFS-Connector) connector. |
| 8129 | `zoomdata-edc-s3` | [Amazon S3](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932743032461-Manage-the-Amazon-S3-Connector) connector. |
| 8131 | `zoomdata-edc-snowflake` | [Snowflake](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932757334669-Manage-the-Snowflake-Connector) connector. |
| 8132 | `zoomdata-edc-hive` | [Hive](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932766095885-Manage-the-Hive-Connector) connector. |
| 8138 | `zoomdata-edc-couchbase` | [Couchbase](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932720313229-Manage-the-Couchbase-Connector) connector. |
| 8139 | `zoomdata-edc-elasticsearch-7.0` | [Elasticsearch 7.0](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector) connector. |
| 8140 | `zoomdata-edc-tibcodv` | [TIBCO DV](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932768245901-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) connector. |
| 8142 | `zoomdata-edc-dremio` | [Dremio](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728091149-Manage-the-Dremio-Connector) connector. |
| 8147 | `zoomdata-edc-elasticsearch-8-0` | [Elasticsearch 8.0](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932728155405-Manage-the-Elasticsearch-Connector) connector. |
| 8148 | `zoomdata-edc-trino` | [Trino](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932773334285-Manage-the-Trino-Connector) connector. |
| 8201 | `zoomdata-edc-cloudera-search` | [Cloudera Search](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932696536461-Manage-the-Cloudera-Search-Connector) connector. |
| 8202 | `zoomdata-edc-redshift` | [Amazon Redshift](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932733806989-Manage-the-Amazon-Redshift-Connector) connector. |
| 8205 | `zoomdata-edc-saphanacloud` | [SAP S/4HANA](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932767840781-Manage-the-SAP-S-4HANA-Connector) connector. |
| 8300 | `zoomdata-consul` | Internal port used by the Consul for inter-node communication in a distributed environment. |
| 8301 | `zoomdata-consul` | Internal port used by the Consul for inter-node communication in a distributed environment. |
| 8302 | `zoomdata-consul` | Internal port used by the Consul for inter-node communication in a distributed environment. |
| 8443 | `zoomdata` | Composer HTTPS requests. |
| 8500 | `zoomdata-consul` | Consul. |
| 8888 | `zoomdata-config-server` | Composer [configuration](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933101946765-Configuration-Microservice) microservice. |
