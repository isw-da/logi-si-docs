---
title: "Custom SQL\u00a0Queries"
id: 43701041493645
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701041493645-Custom-SQL-Queries
updated_at: 2026-05-29T14:07:26Z
---

# Custom SQL Queries

# Custom SQL Queries

Applicable only to SQL-based connectors, a data source using a connector that supports custom SQL queries can use an SQL query to select fields from the table. The custom SQL statement can be specified on the [Custom SQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080568205-Source-Creation-Tab#Custom)  area of the Source Creation tab after selecting the **Custom SQL** option.
Any visual you create displays fields in the order they are retrieved from the source. When you create a source using custom SQL, your field data is shown in the order you specify.

**Important:** 
Custom SQL queries are a powerful tool for performing complex data queries. However, be careful when creating custom SQL queries because it is easy to define a heavy query or a query that may overwhelm your database. Use this feature carefully.

In SQL-based sources, Composer typically wraps the query with select \* from. For example, suppose the original query is this:

select count(\*), someField from myCollection GROUP By someField

The resulting query that Composer uses is this:

select \* from (select count(\*), someField from myCollection GROUP By someField)

Support for this feature by connector is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| --- | --- |
| [Amazon Redshift](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009454477-Manage-the-Amazon-Redshift-Connector) | **Y** |
| [Amazon S3](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009509517-Manage-the-Amazon-S3-Connector) | **N** |
| [Apache Drill](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042973581-Manage-the-Apache-Drill-Connector) | **Y** |
| [Apache Phoenix](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025361549-Manage-the-Apache-Phoenix-Connector) | **Y** |
| [Apache Phoenix Query Server (QS)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025361549-Manage-the-Apache-Phoenix-Connector) | **Y** |
| [Apache Solr](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043021325-Manage-the-Apache-Solr-Connector) | N/A |
| [BigQuery](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009802509-Manage-the-BigQuery-Connector) | **Y** |
| [Business Central Jet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701057330957-Manage-the-Business-Central-Jet-Connector) | **N** |
| [Cloudera Impala](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025595405-Manage-the-Impala-Connector) | **Y** |
| [Cloudera Search](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009985933-Manage-the-Cloudera-Search-Connector) | N/A |
| [Couchbase](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701040183821-Manage-the-Couchbase-Connector) | **N** |
| [Dremio](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043446285-Manage-the-Dremio-Connector) | **Y** |
| [Elasticsearch 7.0](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector) | N/A |
| [Elasticsearch 8.0](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector) | N/A |
| [File Upload](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads) | **Y** |
| [HDFS](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700995161101-Manage-the-HDFS-Connector) | **N** |
| [Hive](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026308493-Manage-the-Hive-Connector) | **Y** |
| [Jira](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044185229-Manage-the-Jira-Connector) | **Y** |
| [MemSQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011116173-Manage-the-MemSQL-Connector) | **Y** |
| [Microsoft SQL Server](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026525069-Manage-the-Microsoft-SQL-Server-Connector) | **Y** |
| [MongoDB](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026372749-Manage-the-MongoDB-Connector) | N/A |
| [MySQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044330253-Manage-the-MySQL-Connector) | **Y** |
| [OpenSearch](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074183053-Manage-the-OpenSearch-Connector) | N/A |
| [Oracle](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011976717-Manage-the-Oracle-Connector) | **Y** |
| [PostgreSQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701091160973-Manage-the-PostgreSQL-Connector) | **Y** |
| [Python](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074664333-Manage-the-Python-Connector) | **Y** |
| [Real Time Sales](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027022221-Manage-the-Real-Time-Sales-Demo-Source) | **N** |
| [Salesforce](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074738317-Manage-the-Salesforce-Connector) | **Y** |
| [SAP Hana](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701012179469-Manage-the-SAP-Hana-Connector) | **Y** |
| [SAP S/4HANA](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996045069-Manage-the-SAP-S-4HANA-Connector "SAP S/4HANA link") | **Y** |
| [SAP IQ](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996022669-Manage-the-SAP-IQ-Connector) | **Y** |
| [Spark SQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701012300173-Manage-the-Spark-SQL-Connector) | **Y** |
| [Snowflake](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074814989-Manage-the-Snowflake-Connector) | **Y** |
| [Teradata](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701091479437-Manage-the-Teradata-Connector) | **Y** |
| [TIBCO DV](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996158349-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | **Y** |
| [Trino](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701045148045-Manage-the-Trino-Connector) | **Y** |
| [File Upload (Upload API)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads) | **N** |
| [Vertica](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027298189-Manage-the-Vertica-Connector) | **Y** |
