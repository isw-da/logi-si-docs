---
title: "Admin-Defined Functions"
id: 43701029797901
section: "Composer 26 Developer Tools"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701029797901-Admin-Defined-Functions
updated_at: 2026-05-29T14:08:09Z
---

# Admin-Defined Functions

# Admin-Defined Functions

Composer provides a set of functions that you can use in expressions to build derived fields or custom metrics. However, you may want to use your own functions (for which there is no Composer equivalent) to extend your data analytics in Composer. Examples of this might be functions available within your data store either natively or as user-defined functions. In such situations, you can leverage Composer administrator-defined functions to expose this capability throughout Composer.

Administrator-defined functions allow your organization to create functions at the connector level from SQL strings. These functions can be referenced later in [data source configurations](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068934669-Manage-Data-Sources) that use the connector.

Currently, the following limitations exist for administrator-defined functions.

1. They are only available for connectors that are SQL-based and that support row-level expressions in derived fields and custom metrics.
2. They are only available for functions that perform row-level operations, and not aggregation operations (for example, standard deviation or rank).

Support for this feature by connector is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| --- | --- |
| [Amazon Redshift](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009454477-Manage-the-Amazon-Redshift-Connector) | **Y** |
| [Amazon S3](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009509517-Manage-the-Amazon-S3-Connector) | **Y** |
| [Apache Drill](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042973581-Manage-the-Apache-Drill-Connector) | **Y** |
| [Apache Phoenix](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025361549-Manage-the-Apache-Phoenix-Connector) | **Y** |
| [Apache Phoenix Query Server (QS)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025361549-Manage-the-Apache-Phoenix-Connector) | **Y** |
| [Apache Solr](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043021325-Manage-the-Apache-Solr-Connector) | **N** |
| [BigQuery](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009802509-Manage-the-BigQuery-Connector) | **Y** |
| [Business Central Jet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701057330957-Manage-the-Business-Central-Jet-Connector) | **Y** |
| [Cloudera Impala](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025595405-Manage-the-Impala-Connector) | **Y** |
| [Cloudera Search](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009985933-Manage-the-Cloudera-Search-Connector) | **N** |
| [Couchbase](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701040183821-Manage-the-Couchbase-Connector) | **Y** |
| [Dremio](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043446285-Manage-the-Dremio-Connector) | **N** |
| [Elasticsearch 7.0](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector) | **N** |
| [Elasticsearch 8.0](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector) | **N** |
| [File Upload](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads) | **Y** |
| [HDFS](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700995161101-Manage-the-HDFS-Connector) | **Y** |
| [Hive](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026308493-Manage-the-Hive-Connector) | **Y** |
| [Jira](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044185229-Manage-the-Jira-Connector) | **N** |
| [MemSQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011116173-Manage-the-MemSQL-Connector) | **Y** |
| [Microsoft SQL Server](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026525069-Manage-the-Microsoft-SQL-Server-Connector) | **Y** |
| [MongoDB](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026372749-Manage-the-MongoDB-Connector) | **N** |
| [MySQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044330253-Manage-the-MySQL-Connector) | **Y** |
| [OpenSearch](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074183053-Manage-the-OpenSearch-Connector) | **N** |
| [Oracle](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011976717-Manage-the-Oracle-Connector) | **Y** |
| [PostgreSQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701091160973-Manage-the-PostgreSQL-Connector) | **Y** |
| [Python](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074664333-Manage-the-Python-Connector) | **N** |
| [Real Time Sales](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027022221-Manage-the-Real-Time-Sales-Demo-Source) | N/A |
| [Salesforce](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074738317-Manage-the-Salesforce-Connector) | **N** |
| [SAP Hana](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701012179469-Manage-the-SAP-Hana-Connector) | **Y** |
| [SAP S/4HANA](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996045069-Manage-the-SAP-S-4HANA-Connector) | **Y** |
| [SAP IQ](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996022669-Manage-the-SAP-IQ-Connector) | **Y** |
| [Spark SQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701012300173-Manage-the-Spark-SQL-Connector) | **Y** |
| [Snowflake](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074814989-Manage-the-Snowflake-Connector) | **Y** |
| [Teradata](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701091479437-Manage-the-Teradata-Connector) | **Y** |
| [TIBCO DV](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996158349-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | **Y** |
| [Trino](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701045148045-Manage-the-Trino-Connector) | **Y** |
| [File Upload (Upload API)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads) | **Y** |
| [Vertica](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027298189-Manage-the-Vertica-Connector) | **Y** |

If a connector supports derived fields, it also supports row-level expressions.

For more information, see:

* [Activate Admin-Defined Functions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701015148557-Activate-Admin-Defined-Functions)
* [Admin-Defined Function JSON Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701015108109-Admin-Defined-Function-JSON-Files)
