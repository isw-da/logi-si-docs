---
title: "Connector Properties and Property Files"
id: 4405850892439
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850892439-Connector-Properties-and-Property-Files
updated_at: 2021-09-21T01:26:49Z
---

# Connector Properties and Property Files

# Connector Properties and Property Files

Composer's architecture enables the deployment of Composer's data connectors as standalone components running in their own process space. Each connector has its own dedicated connector server and a corresponding property files.
Some properties are common to all connectors and some properties are unique to a specific connector. The properties for each connector are documented in the property files.

The kinds of configuration properties found in these files include:

* logging properties
* actuator properties (Spring Boot management endpoint configuration)
* data source connection pool properties
* data source-specific properties
* Kerberos configuration properties (for some connectors)
* service discovery properties
* tracing microservice properties
* other connector-specific properties.

The connector property files have names in the following format: `edc-<connector>.properties`. The following table lists these property files and identifies the associated connector.

| Connector | Property File Name |
| --- | --- |
| Amazon Redshift | `edc-redshift.properties` |
| Amazon S3 | `edc-s3.properties` |
| Apache Drill | `edc-drill.properties` |
| Apache Phoenix 4.7 | `edc-phoenix-4.7.properties` |
| Apache Phoenix Query Server 4.7 | `edc-phoenix-4.7-queryserver.properties` |
| Apache Solr | `edc-apache-solr.properties` |
| BigQuery | `edc-bigquery.properties` |
| Cloudera Impala | `edc-impala.properties` |
| Cloudera Search | `edc-cloudera-search.properties` |
| Couchbase | `edc-couchbase.properties` |
| Dremio | `edc-dremio.properties` |
| Elasticsearch 6.0 | `edc-elasticsearch-6.0.properties` |
| Elasticsearch 7.0 | `edc-elasticsearch-7.0.properties` |
| HDFS | `edc-hdfs.properties` |
| Hive | `edc-hive.properties` |
| MemSQL | `edc-memsql.properties` |
| Microsoft SQL Server | `edc-mssql.properties` |
| MongoDB | `edc-mongo.properties` |
| MySQL | `edc-mysql.properties` |
| Oracle | `edc-oracle.properties` |
| PostgreSQL | `edc-postgresql.properties` |
| Presto | `edc-presto.properties` |
| Real-Time Sales | `edc-rts.properties` |
| SAP Hana | `edc-saphana.properties` |
| SAP IQ | `edc-sapiq.properties` |
| Snowflake | `edc-snowflake.properties` |
| Spark SQL | `edc-sparksql.properties` |
| Teradata | `edc-teradata.properties` |
| TIBCO DV | `edc-tibcodv.properties` |
| Vertica | `edc-vertica.properties` |

For more information about editing property files, see [*Edit a Composer Configuration File*](https://devnet.logianalytics.com/hc/en-us/articles/4405850887703-Edit-a-Composer-Configuration-File).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg)Composer discourages changing properties in the `/opt/zoomdata/conf` directory. Instead we recommend that you copy the files you want to change to the `/etc/zoomdata` directory and change them there. This will ensure that your changes are not overwritten when Composer is next upgraded. In addition, you can quickly determine what changes you've made to a properties file using `diff`. For example:

```
diff /opt/zoomdata/conf/edc-<connector-name>.properties /etc/zoomdata/<edc-<connector-name>.properties
```

or

```
diff /opt/zoomdata/conf/zoomdata.properties /etc/zoomdata/zoomdata.properties
```
