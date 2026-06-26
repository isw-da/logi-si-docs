---
title: "Visualize Schemas and Joins"
id: 43701038666125
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038666125-Visualize-Schemas-and-Joins
updated_at: 2026-05-29T14:11:33Z
---

# Visualize Schemas and Joins

# Visualize Schemas and Joins

Visualize the fields and tables in schemas included with your connection, and created by other users. Add relationships as needed. Visualize joins in your data sources.

When you create joins in a source, you can visualize and update your joins as well. See[Fuse Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072155405-Fuse-Data-Sources).

## Edit and View Relationships in Schemas

Users with appropriate permissions can view and edit the relationships using the Relationship tab for a supported connection. Select a schema from the list in the drop-down, then make and save any additions to the relationships as needed.

![Use this work area to view and update relationships in available schemas](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242726494477 "Relationship tab for a connector")

**View or edit a schema for a connection**

1. Open a supported connection and navigate to the **Relationship** tab. A work area opens you can use to navigate among the tables and relationships of a selected schema.
2. Select an available schema from the drop-down list. Larger data sets may take a few moments to load.
3. View the existing relationships and any user defined relationships.
4. Optionally, draw more relationships in this work area, then **Save** your changes.

   **Note:** To remove a user-applied join, double-click to select the join, then select the backspace key. The relationship is removed.
5. View or edit as many schemas as you need.

**Important:** If you add joins that create one-to-many relationships here, Logi Composer may return an error that prevents use of the data in a visual. For best results, when you create a one-to-many relationship with a specific left entity, any additional joins must refer to that table as the right entity. See [Recommended Joins](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072201741-Create-a-Fusion-Source#Recs).

**Note:** For Postgres connections, both tables and data relationship information are read from the connection. Other supported connections include table information but do not read relationship information. See [Connector Support for Schema Visualization](#support). No information is provided for unsupported connections.

## View Relationships of a Schema in a Source

You can view the relationships present in schemas you're using in your sources that use a supported connection. The [Source Creation tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080568205-Source-Creation-Tab) of the [source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068934669-Manage-Data-Sources) includes a Schema drop-down you can use to select a schema for the source, with a view button that opens the work area.

![Use this work area to view relationships in available schemas](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243331860109 "view a schema work area")

**View a schema in a source**

1. Create or edit a source that uses a schema.
2. [Select the view icon next](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080450061-Define-a-Source#view) to your selected Schema. A schema work area opens you can use to view the tables and relationships of that schema. Larger data sets may take a few moments to load.
3. View the existing relationships and any user defined joins to better understand the relationships present.
4. Close the schema or joins modal when you're done viewing the schema information, and repeat for other schemas if needed.

### Connector Support for Schema Visualization

Support for this feature by connector is shown in the following table.

**Key:****Y** - Supported; **N** - Not Supported; N/A - may not be supported.

| Connector | Supported? |
| --- | --- |
| [Amazon Redshift](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009454477-Manage-the-Amazon-Redshift-Connector) | **Y** |
| [Amazon S3](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009509517-Manage-the-Amazon-S3-Connector) | **Y** |
| [Apache Drill](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042973581-Manage-the-Apache-Drill-Connector) | N/A |
| [Apache Phoenix](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025361549-Manage-the-Apache-Phoenix-Connector) | N/A |
| [Apache Phoenix Query Server (QS)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025361549-Manage-the-Apache-Phoenix-Connector) | N/A |
| [Apache Solr](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043021325-Manage-the-Apache-Solr-Connector) | N/A |
| [BigQuery](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009802509-Manage-the-BigQuery-Connector) | N/A |
| [Cloudera Impala](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025595405-Manage-the-Impala-Connector) | **Y** |
| [Cloudera Search](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009985933-Manage-the-Cloudera-Search-Connector) | N/A |
| [Couchbase](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701040183821-Manage-the-Couchbase-Connector) | N/A |
| [Dremio](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043446285-Manage-the-Dremio-Connector) | N/A |
| [Elasticsearch 7.0](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector) | **N** |
| [Elasticsearch 8.0](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector) | N/A |
| [File Upload](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads) | N/A |
| [HDFS](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700995161101-Manage-the-HDFS-Connector) | **Y** |
| [Hive](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026308493-Manage-the-Hive-Connector) | N/A |
| [Jira](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044185229-Manage-the-Jira-Connector) | **Y** |
| [MemSQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011116173-Manage-the-MemSQL-Connector) | **Y** |
| [Microsoft SQL Server](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026525069-Manage-the-Microsoft-SQL-Server-Connector) | **Y** |
| [MongoDB](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701026372749-Manage-the-MongoDB-Connector) | **Y** |
| [MySQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044330253-Manage-the-MySQL-Connector) | **Y** |
| [Oracle](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011976717-Manage-the-Oracle-Connector) | **Y** |
| [PostgreSQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701091160973-Manage-the-PostgreSQL-Connector) | **Y** |
| [Python](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074664333-Manage-the-Python-Connector) | N/A |
| [Real Time Sales](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027022221-Manage-the-Real-Time-Sales-Demo-Source) | **Y** |
| [Salesforce](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074738317-Manage-the-Salesforce-Connector) | **Y** |
| [SAP Hana](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701012179469-Manage-the-SAP-Hana-Connector) | N/A |
| [SAP S/4HANA](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996045069-Manage-the-SAP-S-4HANA-Connector) | N/A |
| [SAP IQ](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996022669-Manage-the-SAP-IQ-Connector) | N/A |
| [Spark SQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701012300173-Manage-the-Spark-SQL-Connector) | N/A |
| [Snowflake](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074814989-Manage-the-Snowflake-Connector) | **Y** |
| [Teradata](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701091479437-Manage-the-Teradata-Connector) | N/A |
| [TIBCO DV](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996158349-Manage-the-TIBCO-Data-Virtualization-TDV-Connector) | N/A |
| [Trino](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701045148045-Manage-the-Trino-Connector) | N/A |
| [File Upload (Upload API)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads) | N/A |
| [Vertica](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027298189-Manage-the-Vertica-Connector) | N/A |
