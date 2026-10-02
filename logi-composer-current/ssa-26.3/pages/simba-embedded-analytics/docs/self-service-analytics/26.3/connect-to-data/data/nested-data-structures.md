> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Support of Nested Data Structures in Self-Service Analytics

Self-Service Analytics supports aggregations for nested (or hierarchical) data structures for some data stores.

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| - | - |
| [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift) | N/A |
| [Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3) | N/A |
| [Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill) | N/A |
| [Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | N/A |
| [Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | N/A |
| [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr) | **N** |
| [BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery) | N/A |
| [Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central) | N/A |
| [Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector) | N/A |
| [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search) | N/A |
| [Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase) | N/A |
| [Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio) | N/A |
| [Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi) | source-dependent |
| [Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **Y** |
| [Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **Y** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | N/A |
| [HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs) | N/A |
| [Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive) | N/A |
| [Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira) | **N** |
| [MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql) | N/A |
| [Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server) | N/A |
| [MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb) | **Y** |
| [MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql) | N/A |
| [OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch) | **Y** |
| [Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle) | N/A |
| [PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql) | N/A |
| [Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python) | **N** |
| [Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source) | N/A |
| [Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce) | **N** |
| [SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana) | N/A |
| [SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana) | N/A |
| [SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql) | N/A |
| [Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql) | N/A |
| [Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake) | N/A |
| [Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata) | N/A |
| [TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv) | N/A |
| [Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino) | N/A |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | N/A |
| [Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica) | N/A |

There are two ways to store nested structure:

1. Store all hierarchy as a single document, for example, in JSON format (nested documents).
2. Store hierarchy items as separate documents and additional info on hierarchical links internally (block join).

## Nested Documents

Hierarchical structure can be represented in JSON format. In MongoDB and Elasticsearch, storing such structures is supported.

Consider the following example. We need to store a hierarchy of divisions by country with two divisions in country. Also we need to store some general country information, for example, foundation year.

In this case, the following JSON is sent to the index document:

```json theme={null}
{
	"country":"Germany",
	"foundation year":2008,
	"divisions":[
		{
			"city":"Berlin",
			"sales":200,
			"manager":{
				"first name":"Robert",
				"last name":"Simmons",
				"years in company":4
				}
		},
		{
			"city":"Munich",
			"sales":200,
			"manager":{
				"first name":"Robert",
				"last name":"Simmons",
				"years in company":4
				}
		}
	]
}
```

In MongoDB, you can store such documents and then query them as is, without any restrictions. However, the performance may be slow if the document contains a lot of arrays.

In Elasticsearch, we recommend using the "nested" type for complex objects before the document is indexed.

## Block Join Support

There is another way to store hierarchical structures. All hierarchy items are stored as separate elements, with information about the hierarchical links stored internally. Apache Solr supports this approach.

Consider the following example. We need to store a hierarchy of divisions by country with two divisions in country. Also we need to store some general country information, for example, foundation year.

In this case, the following JSON is sent to the index document:

```json theme={null}
{ "country":"Germany", "foundationYear":2008, "_childDocuments_":[ { "city":"Berlin", "sales":200, "managerFirstName":"Robert", "managerLastName":"Simmons", "managerYearsInCompany":4 }, { "city":"Munich", "sales":200, "managerFirstName":"Robert", "managerLastName":"Simmons", "managerYearsInCompany":4 } ] }
```

As a result, there are three documents in the index. Information on hierarchical linking of these objects is stored internally in Solr.

```json theme={null}
{ "country":"Germany", "foundationYear":2008 }, { "city":"Berlin", "sales":200, "managerFirstName":"Robert", "managerLastName":"Simmons", "managerYearsInCompany":4 }, { "city":"Munich", "sales":200, "managerFirstName":"Robert", "managerLastName":"Simmons", "managerYearsInCompany":4 }
```

You must specify what fields are used in parent documents. To do this, you must select the checkbox in the **Parent Field** column on the **Fields** tab while [creating](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#define-a-source) or [modifying](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#edit-a-data-source) the data source configuration .

<h2 id="visualize-schemas-and-joins">
  Visualize Schemas and Joins
</h2>

Visualize the fields and tables in schemas included with your connection, and created by other users. Add relationships as needed. Visualize join nodes in your data sources.

When you create join nodes in a source, you can visualize and update your joins as well. See [Fuse Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview).

<h3 id="edit-and-view-relationships-in-schemas">
  Edit and View Relationships in Schemas
</h3>

Users with appropriate permissions can view and edit the relationships using the Relationship tab for a supported connection. Select a schema from the list in the drop-down, then make and save any additions to the relationships as needed.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/cmp-rship-edit-connection-24-2-rev.jpg?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=a6d089e607ceb7a1e6b602330cd3b3d8" alt="Use this work area to view and update relationships in available schemas" width="1189" height="700" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/cmp-rship-edit-connection-24-2-rev.jpg" />

**View or edit a schema for a connection**

1. Open a supported connection and navigate to the **Relationship** tab. A work area opens you can use to navigate among the tables and relationships of a selected schema.

2. Select an available schema from the drop-down list. Larger data sets may take a few moments to load.

3. View the existing relationships and any user defined relationships.

4. Optionally, draw more relationships in this work area, then **Save** your changes.

   <Note>
     To remove a user-applied join node, double-click to select the join node, then select the backspace key. The relationship is removed.
   </Note>

5. View or edit as many schemas as you need.

<Warning>
  If you add joins that create one-to-many relationships here, Self-Service Analytics may return an error that prevents use of the data in a visual. For best results, when you create a one-to-many relationship with a specific left entity, any additional joins must refer to that table as the right entity. See [Recommended Joins](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview#recommended-joins).
</Warning>

<Note>
  For Postgres connections, both tables and data relationship information are read from the connection. Other supported connections include table information but do not read relationship information. See [Connector Support for Schema Visualization](#connector-support-for-schema-visualization). No information is provided for unsupported connections.
</Note>

<h3 id="view-relationships-of-a-schema-in-a-source">
  View Relationships of a Schema in a Source
</h3>

You can view the relationships present in schemas you are using in your sources that use a supported connection. The [Source Creation tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-source-creation-tab) of the [source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview) includes a Schema drop-down you can use to select a schema for the source, with a view button that opens the work area.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/cmp-view-schema-source-24-2-rev.jpg?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=9724f041579ec83ed9a04d73a7ff722b" alt="Use this work area to view relationships in available schemas" width="1103" height="693" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/connectors/cmp-view-schema-source-24-2-rev.jpg" />

**View a schema in a source**

1. Create or edit a source that uses a schema.
2. [Select the view icon next](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#view-relationships-for-a-schema-in-a-source) to your selected Schema. A schema work area opens you can use to view the tables and relationships of that schema. Larger data sets may take a few moments to load.
3. View the existing relationships and any user defined join nodes to better understand the relationships present.
4. Close the schema or join nodes modal when you're done viewing the schema information, and repeat for other schemas if needed.

<h4 id="connector-support-for-schema-visualization">
  Connector Support for Schema Visualization
</h4>

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - may not be supported.

| Connector | Supported? |
| - | - |
| [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift) | **Y** |
| [Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3) | **Y** |
| [Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill) | N/A |
| [Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | N/A |
| [Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | N/A |
| [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr) | N/A |
| [BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery) | N/A |
| [Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector) | **Y** |
| [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search) | N/A |
| [Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase) | N/A |
| [Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi) | N/A |
| [Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio) | N/A |
| [Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **N** |
| [Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | N/A |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | N/A |
| [HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs) | **Y** |
| [Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive) | N/A |
| [Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira) | **Y** |
| [MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql) | **Y** |
| [Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server) | **Y** |
| [MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb) | **Y** |
| [MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql) | **Y** |
| [Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle) | **Y** |
| [PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql) | **Y** |
| [Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python) | N/A |
| [Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source) | **Y** |
| [Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce) | **Y** |
| [SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana) | N/A |
| [SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana) | N/A |
| [SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql) | N/A |
| [Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql) | N/A |
| [Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake) | **Y** |
| [Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata) | N/A |
| [TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv) | N/A |
| [Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino) | N/A |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | N/A |
| [Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica) | N/A |
