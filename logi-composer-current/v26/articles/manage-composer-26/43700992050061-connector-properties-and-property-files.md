---
title: "Connector Properties and Property Files"
id: 43700992050061
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992050061-Connector-Properties-and-Property-Files
updated_at: 2026-05-29T14:07:21Z
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
* other connector-specific properties.

**Note:** insightsoftware discourages changing properties in the `/opt/zoomdata/conf` directory (Linux) or `<install-path>/conf` (Windows). Copy the files you want to change to the `/etc/zoomdata` directory (Linux) or `<install-path>/conf-modify` (Windows) and change them there. This will ensure that your changes are not overwritten when Composer is next upgraded.

Quickly determine what changes you've made to a properties file using `diff` in Linux. For example:

diff /opt/zoomdata/conf/edc-<connector-name>.properties /etc/zoomdata/<edc-<connector-name>.properties

or

diff /opt/zoomdata/conf/zoomdata.properties /etc/zoomdata/zoomdata.properties

For Windows environments, use your preferred diff utility to compare the differences between your original and updated property files.

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
| Elasticsearch 7.0 | `edc-elasticsearch-7.0.properties` |
| Elasticsearch 8.0 | `edc-elasticsearch-8.0.properties` |
| HDFS | `edc-hdfs.properties` |
| Hive | `edc-hive.properties` |
| Jira | `edc-jira.properties` |
| MemSQL | `edc-memsql.properties` |
| Microsoft SQL Server | `edc-mssql.properties` |
| MongoDB | `edc-mongo.properties` |
| MySQL | `edc-mysql.properties` |
| OpenSearch | `edc-opensearch.properties` |
| Oracle | `edc-oracle.properties` |
| PostgreSQL | `edc-postgresql.properties` |
| Python | `edc-python.properties` |
| Real-Time Sales | `edc-rts.properties` |
| Salesforce | `edc-salesforce.properties` |
| SAP Hana | `edc-saphana.properties` |
| SAP S/4HANA | `edc-saphanacloud.properties` |
| SAP IQ | `edc-sapiq.properties` |
| Snowflake | `edc-snowflake.properties` |
| Spark SQL | `edc-sparksql.properties` |
| Teradata | `edc-teradata.properties` |
| TIBCO DV | `edc-tibcodv.properties` |
| Trino | `edc-trino.properties` |
| Vertica | `edc-vertica.properties` |

For more information about editing property files, see [Edit a Configuration File](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053803917-Edit-a-Configuration-File).
