---
title: "Default Port Reference"
id: 4405851144087
section: "Composer v6 Reference Information"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851144087-Default-Port-Reference
updated_at: 2021-09-21T01:29:23Z
---

# Default Port Reference

# Default Port Reference

The following table lists the default ports used by Composer, sorted by port number.

| Port | Microservice | Description |
| --- | --- | --- |
| 443 | `zoomdata` | Composer server web communication  For HTTPS requests, configure your firewall to map port 443 to either port 8443 or port 8080. |
| 5432 | `zoomdata-postgres` | Composer [metadata repository](https://devnet.logianalytics.com/hc/en-us/articles/4405851126039-Metadata-Repository). |
| 5580 | `zoomdata-query-engine` | Composer [query engine](https://devnet.logianalytics.com/hc/en-us/articles/4405859161751-Manage-the-Composer-Query-Engine) microservice |
| 8050 | `zoomdata-admin-server` | [Service Monitor](https://devnet.logianalytics.com/hc/en-us/articles/4405859475735-Composer-Service-Monitor) |
| 8080 | `zoomdata` | Composer server |
| 8081 | `zoomdata-data-writer` | Composer [Data Writer](https://devnet.logianalytics.com/hc/en-us/articles/4405851118743-Data-Writer-Microservice) microservice |
| 8083 | `zoomdata-screenshot-service` | Composer [Screenshot](https://devnet.logianalytics.com/hc/en-us/articles/4405851095575-Set-Up-the-Screenshot-Microservice) microservice |
| 8093 | `zoomdata-edc-bigquery` | [BigQuery](https://devnet.logianalytics.com/hc/en-us/articles/4405859214231-Manage-the-BigQuery-Connector) connector |
| 8095 | `zoomdata-edc-drill` | [Apache Drill](https://devnet.logianalytics.com/hc/en-us/articles/4405850930839-Manage-the-Apache-Drill-Connector) connector |
| 8098 | `zoomdata-edc-impala` | [Cloudera Impala](https://devnet.logianalytics.com/hc/en-us/articles/4405850938647-Manage-the-Impala-Connector) connector |
| 8099 | `zoomdata-edc-memsql` | [MemSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405859228567-Manage-the-MemSQL-Connector) connector |
| 8100 | `zoomdata-edc-mssql` | [Microsoft SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/4405859229975-Manage-the-Microsoft-SQL-Server-Connector) connector |
| 8101 | `zoomdata-edc-mysql` | [MySQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850958487-Manage-the-MySQL-Connector) connector |
| 8102 | `zoomdata-edc-oracle` | [Oracle](https://devnet.logianalytics.com/hc/en-us/articles/4405850959383-Manage-the-Oracle-Connector) connector |
| 8105 | `zoomdata-edc-postgresql` | [PostgreSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850960279-Manage-the-PostgreSQL-Connector) connector, [Flat File](https://devnet.logianalytics.com/hc/en-us/articles/4405850954647-Upload-a-Flat-File-into-Composer) uploads, and [Upload API](https://devnet.logianalytics.com/hc/en-us/articles/4405859140247-Use-the-Upload-API) processing |
| 8107 | `zoomdata-edc-presto` | [Presto](https://devnet.logianalytics.com/hc/en-us/articles/4405859231639-Manage-the-Presto-Connector) connector |
| 8108 | `zoomdata-edc-rts` | [Real Time Sales](https://devnet.logianalytics.com/hc/en-us/articles/4405850962071-Manage-the-Real-Time-Sales-Demo-Source) connector |
| 8109 | `zoomdata-edc-saphana` | [SAP Hana](https://devnet.logianalytics.com/hc/en-us/articles/4405859232791-Manage-the-SAP-Hana-Connector) connector |
| 8111 | `zoomdata-edc-teradata` | [Teradata](https://devnet.logianalytics.com/hc/en-us/articles/4405859235607-Manage-the-Teradata-Connector) connector |
| 8112 | `zoomdata-edc-vertica` | [Vertica](https://devnet.logianalytics.com/hc/en-us/articles/4405850966679-Manage-the-Vertica-Connector) connector |
| 8115 | `zoomdata-edc-apache-solr` | [Apache Solr](https://devnet.logianalytics.com/hc/en-us/articles/4405850931735-Manage-the-Apache-Solr-Connector) connector |
| 8116 | `zoomdata-edc-sparksql` | [Spark SQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850963991-Manage-the-Spark-SQL-Connector) connector |
| 8118 | `zoomdata-edc-elasticsearch-6.0` | [Elasticsearch 6.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) connector |
| 8121 | `zoomdata-edc-sapiq` | [SAP IQ](https://devnet.logianalytics.com/hc/en-us/articles/4405850963095-Manage-the-SAP-IQ-Connector) connector |
| 8123 | `zoomdata-edc-mongo` | [MongoDB](https://devnet.logianalytics.com/hc/en-us/articles/4405850957591-Manage-the-MongoDB-Connector) connector |
| 8124 | `zoomdata-edc-phoenix-4.7` | [Apache Phoenix](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) connector |
| 8125 | `zoomdata-edc-phoenix-4.7-queryserver` | [Apache Phoenix Query Server (QS)](https://devnet.logianalytics.com/hc/en-us/articles/4405859202839-Manage-the-Apache-Phoenix-Connector) connector |
| 8126 | `zoomdata-edc-hdfs` | [HDFS](https://devnet.logianalytics.com/hc/en-us/articles/4405859226903-Manage-the-HDFS-Connector) connector |
| 8129 | `zoomdata-edc-s3` | [Amazon S3](https://devnet.logianalytics.com/hc/en-us/articles/4405850929943-Manage-the-Amazon-S3-Connector) connector |
| 8131 | `zoomdata-edc-snowflake` | [Snowflake](https://devnet.logianalytics.com/hc/en-us/articles/4405859234199-Manage-the-Snowflake-Connector) connector |
| 8132 | `zoomdata-edc-hive` | [Hive](https://devnet.logianalytics.com/hc/en-us/articles/4405850956695-Manage-the-Hive-Connector) connector |
| 8138 | `zoomdata-edc-couchbase` | [Couchbase](https://devnet.logianalytics.com/hc/en-us/articles/4405859220887-Manage-the-Couchbase-Connector) connector |
| 8139 | `zoomdata-edc-elasticsearch-7.0` | [Elasticsearch 7.0](https://devnet.logianalytics.com/hc/en-us/articles/4405850940439-Manage-the-Elasticsearch-Connector) connector |
| 8140 | `zoomdata-edc-tibcodv` | [TIBCO DV](https://devnet.logianalytics.com/hc/en-us/articles/4405850965783-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) connector |
| 8142 | `zoomdata-edc-dremio` | [Dremio](https://devnet.logianalytics.com/hc/en-us/articles/4405859221911-Manage-the-Dremio-Connector) connector |
| 8201 | `zoomdata-edc-cloudera-search` | [Cloudera Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859219863-Manage-the-Cloudera-Search-Connector) connector |
| 8202 | `zoomdata-edc-redshift` | [Amazon Redshift](https://devnet.logianalytics.com/hc/en-us/articles/4405859198103-Manage-the-Amazon-Redshift-Connector) connector |
| 8300 | `zoomdata-consul` | Internal port used by the Consul for inter-node communication in a distributed environment. |
| 8301 | `zoomdata-consul` | Internal port used by the Consul for inter-node communication in a distributed environment. |
| 8302 | `zoomdata-consul` | Internal port used by the Consul for inter-node communication in a distributed environment. |
| 8443 | `zoomdata` | Composer HTTPS requests |
| 8500 | `zoomdata-consul` | Consul |
| 8888 | `zoomdata-config-server` | Composer [configuration](https://devnet.logianalytics.com/hc/en-us/articles/4405851115799-Configuration-Microservice) microservice |
| 9411 | `zoomdata-tracing-server` | Composer [tracing](https://devnet.logianalytics.com/hc/en-us/articles/4405859408535-Tracing-Microservice) microservice |
