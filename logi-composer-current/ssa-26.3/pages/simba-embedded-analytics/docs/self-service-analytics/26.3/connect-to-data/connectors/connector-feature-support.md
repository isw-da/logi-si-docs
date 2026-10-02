> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Connector Feature Support

Self-Service Analytics queries each connector to better understand its data store's capabilities and behavior. The connector's response describes to Self-Service Analytics the Self-Service Analytics features that the connector and the data store can support and any limitations to that support. It identifies the type of data requests that the connector and its data store can fulfill.

To learn more about a Self-Service Analytics feature and the connectors that support it, select the feature from the list below, organized by feature category:

<h3 id="derived-fields-row-level-expressions">
  [Derived Fields (Row-Level Expressions)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields)
</h3>

* [Admin-Defined Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/admin-fx-ov)

### Advanced Visualizations

* [Box Plot](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#box-plots)
* [Histograms](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#bars-histograms)
* [Histogram Floating Point Values](#histogram-floating-point-values)

### Group By Functionality

* [Group By Multiple Fields](#group-by-multiple-fields)
* [Group By Time](#group-by-time)
* [Group By UNIX Time](#group-by-unix-time)

### Filters

* [Wildcard Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#apply-wildcard-filters-to-a-visual-filter-snippet-or-dashboard)
* [Wildcard Filters Case-Insensitive](#wildcard-case-insensitive-filters)
* [Wildcard Filters Case-Sensitive](#wildcard-case-sensitive-filters)
* [Text Search](#text-search)

### Metrics

* [Distinct Counts](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#distinct-counts)
* [Last Value](#last-value)
* [Metric Aggregation Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#metric-aggregation-functions)

### Security

* [Kerberos Authentication](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/kerberos-sso#kerberos-authentication-for-connectors)
* [TLS](#tls)
* [User Delegation](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#enable-user-delegation)

### [Custom SQL Queries](#custom-sql-queries-2)

### [Live Mode and Playback](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar#live-mode-and-historical-playback)

### [Multivalued Fields](#multivalued-fields-2)

### [Nested Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/nested-data-structures)

### [Schemas](#schemas-2)

### Performance

* [Fast Distinct Values](#fast-distinct-values)
* [Partitions](#partitions)
* [Pushdown Joins for Fusion Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview#optimize-joins)

<Note>
  Fused data sources inherit the limitations of the underlying connectors used by the fused sources. In addition, fused sources have other feature limitations. See [Data Fusion Limitations](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview#data-fusion-limitations).
</Note>

<h2 id="custom-sql-queries-2">
  Custom SQL Queries
</h2>

Applicable only to SQL-based connectors, a data source using a connector that supports custom SQL queries can use an SQL query to select fields from the table. The custom SQL statement can be specified on the [Custom SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-source-creation-tab#custom-sql) area of the Source Creation tab after selecting the **Custom SQL** option. Any visual you create displays fields in the order they are retrieved from the source. When you create a source using custom SQL, your field data is shown in the order you specify.

<Warning>
  Custom SQL queries are a powerful tool for performing complex data queries. However, be careful when creating custom SQL queries because it is easy to define a heavy query or a query that may overwhelm your database. Use this feature carefully.
</Warning>

In SQL-based sources, Self-Service Analytics typically wraps the query with select \* from. For example, suppose the original query is this:

```
select count(*), someField from myCollection GROUP By someField
```

The resulting query that Self-Service Analytics uses is this:

```
select * from (select count(*), someField from myCollection GROUP By someField)
```

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| - | - |
| [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift) | **Y** |
| [Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3) | **N** |
| [Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill) | **Y** |
| [Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr) | N/A |
| [BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery) | **Y** |
| [Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central) | **N** |
| [Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector) | **Y** |
| [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search) | N/A |
| [Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase) | **N** |
| [Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio) | **Y** |
| [Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi) | source-dependent |
| [Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | N/A |
| [Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | N/A |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs) | **N** |
| [Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive) | **Y** |
| [Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira) | **Y** |
| [MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql) | **Y** |
| [Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server) | **Y** |
| [MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb) | N/A |
| [MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql) | **Y** |
| [OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch) | N/A |
| [Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle) | **Y** |
| [PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql) | **Y** |
| [Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python) | **Y** |
| [Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source) | **N** |
| [Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce) | **Y** |
| [SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana) | **Y** |
| [SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana) | **Y** |
| [SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql) | **Y** |
| [Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql) | **Y** |
| [Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake) | **Y** |
| [Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata) | **Y** |
| [TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv) | **Y** |
| [Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino) | **Y** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **N** |
| [Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica) | **Y** |

<h2 id="fast-distinct-values">
  Fast Distinct Values
</h2>

Connectors that support fast distinct values can efficiently return distinct values for a field. This functionality optimizes the retrieval of distinct (unique) values in large numbers of records. If a connector supports this feature, the Filter dialog is populated with distinct values for an attribute directly from the data source, without the need to refresh the data and without retrieving or storing the distinct values in the metadata. For example, Elasticsearch keeps lists of distinct values at the ready. Features such as these make fast distinct values possible for your connector.

There is no metric that defines "fast". This value is based on the judgment of the developer.

When custom ranges or list values are requested for a field, full data scans are not performed.

For most connectors, this feature can be safely left disabled without impact.

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| - | - |
| [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift) | N/A |
| [Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3) | N/A |
| [Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill) | N/A |
| [Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | N/A |
| [Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | N/A |
| [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr) | **Y** |
| [BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery) | N/A |
| [Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central) | N/A |
| [Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector) | N/A |
| [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search) | **Y** |
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
| [MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb) | N/A |
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

<h2 id="group-by-multiple-fields">
  Group By Multiple Fields
</h2>

Many connectors can group by more than one field in a query. Here is a sample SQL query:

```
select firstField, secondField, count(distinct otherField) from myCollection group by firstField, secondField
```

If multi-group querying is not supported, some visuals will be unavailable for a data source.

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

<table>
  <thead>
    <tr>
      <th>Connector</th>
      <th>Supported?</th>
      <th>Notes</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>[Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix)</td>
      <td>**Y**</td>

      <td rowSpan={2} />
    </tr>

    <tr>
      <td>[Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix)</td>
      <td>**Y**</td>
    </tr>

    <tr>
      <td>[Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery)</td>
      <td>**Y**</td>
      <td>If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`.</td>
    </tr>

    <tr>
      <td>[Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi)</td>
      <td>source-dependent</td>

      <td />
    </tr>

    <tr>
      <td>[Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search)</td>
      <td>**Y**</td>

      <td rowSpan={2} />
    </tr>

    <tr>
      <td>[Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search)</td>
      <td>**Y**</td>
    </tr>

    <tr>
      <td>[File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica)</td>
      <td>**Y**</td>

      <td />
    </tr>
  </tbody>
</table>

<h2 id="group-by-time">
  Group By Time
</h2>

Many connectors support grouping data by a real time field. This function is a prerequisite for all time-based visuals.

Most commonly, the data includes a date or time stamp field type that corresponds to Self-Service Analytics’s date field type. Here is a sample SQL query:

```
select timeField, max(otherField) from myCollection group by timeField
```

If grouping on time is not supported, some visuals will be unavailable for the data source.

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| - | - |
| [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift) | **Y** |
| [Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3) | **Y** |
| [Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill) | **Y** |
| [Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr) | **Y** |
| [BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery) | **Y** |
| [Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central) | **Y** |
| [Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector) | **Y** |
| [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search) | **N** |
| [Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase) | **Y** |
| [Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio) | **Y** |
| [Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi) | source-dependent |
| [Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **Y** |
| [Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **Y** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs) | **Y** |
| [Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive) | **Y** |
| [Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira) | **Y** |
| [MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql) | **Y** |
| [Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server) | **Y** |
| [MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb) | **Y** |
| [MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql) | **Y** |
| [OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch) | **Y** |
| [Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle) | **Y** |
| [PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql) | **Y** |
| [Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python) | **Y** |
| [Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source) | **Y** |
| [Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce) | **Y** |
| [SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana) | **Y** |
| [SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana) | **Y** |
| [SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql) | **Y** |
| [Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql) | **Y** |
| [Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake) | **Y** |
| [Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata) | **Y** |
| [TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv) | **Y** |
| [Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino) | **Y** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica) | **Y** |

<h2 id="group-by-unix-time">
  Group By UNIX Time
</h2>

Many connectors support grouping data by an integer field that contains times in Unix (epoch) time.

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| - | - |
| [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift) | **Y** |
| [Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3) | **Y** |
| [Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill) | **Y** |
| [Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr) | **Y** |
| [BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery) | **Y** |
| [Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central) | **Y** |
| [Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector) | **Y** |
| [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search) | **N** |
| [Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase) | **Y** |
| [Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio) | **Y** |
| [Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi) | source-dependent |
| [Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **N** |
| [Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **N** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs) | **Y** |
| [Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive) | **Y** |
| [Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira) | **Y** |
| [MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql) | **Y** |
| [Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server) | **Y** |
| [MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb) | **N** |
| [MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql) | **Y** |
| [OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch) | **N** |
| [Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle) | **Y** |
| [PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql) | **Y** |
| [Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python) | **Y** |
| [Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source) | **N** |
| [Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce) | **Y** |
| [SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana) | **Y** |
| [SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana) | **N** |
| [SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql) | **Y** |
| [Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql) | **Y** |
| [Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake) | **Y** |
| [Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata) | **Y** |
| [TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv) | **Y** |
| [Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino) | **Y** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica) | **Y** |

<h2 id="histogram-floating-point-values">
  Histogram Floating Point Values
</h2>

Many connectors support the calculations necessary for histogram visuals with non-integer values, such as floating point (32-bit) and double-precision (64-bit) floating point data types.

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| - | - |
| [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift) | **Y** |
| [Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3) | **Y** |
| [Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill) | **Y** |
| [Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr) | **N** |
| [BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery) | **Y** |
| [Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central) | **Y** |
| [Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector) | **Y** |
| [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search) | **N** |
| [Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase) | **Y** |
| [Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio) | **Y** |
| [Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi) | source-dependent |
| [Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **Y** |
| [Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **Y** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs) | **Y** |
| [Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive) | **Y** |
| [Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira) | **Y** |
| [MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql) | **Y** |
| [Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server) | **Y** |
| [MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb) | **Y** |
| [MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql) | **Y** |
| [OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch) | **Y** |
| [Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle) | **Y** |
| [PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql) | **Y** |
| [Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python) | **Y** |
| [Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source) | **Y** |
| [Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce) | **Y** |
| [SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana) | **Y** |
| [SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana) | **Y** |
| [SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql) | **Y** |
| [Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql) | **Y** |
| [Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake) | **Y** |
| [Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata) | **Y** |
| [TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv) | **Y** |
| [Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino) | **Y** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica) | **Y** |

<h2 id="last-value">
  Last Value
</h2>

The last value metric in data is the last value in all the data values for a field, sorted by the time attribute selected for the time bar. If the latest date and time for the time attribute is exactly the same in multiple records, the last value for the field is the maximum value of the field in the records with the latest date and time.

When a connector supports the last value feature, it determines and uses the last value of a selected field in the data.

Although many data stores implement a last value function, the Self-Service Analytics last value indicates that the last value in a given field collection can be loaded and used in a visual immediately.

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| - | - |
| [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift) | **Y** |
| [Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3) | **Y** |
| [Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill) | **Y** |
| [Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **N** |
| [Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **N** |
| [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr) | **N** |
| [BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery) | **Y** |
| [Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central) | **Y** |
| [Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector) | **Y** |
| [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search) | **N** |
| [Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase) | **N** |
| [Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio) | **Y** |
| [Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi) | source-dependent |
| [Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **Y** |
| [Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **Y** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs) | **Y** |
| [Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive) | **Y** |
| [Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira) | **N** |
| [MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql) | **Y** |
| [Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server) | **Y** |
| [MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb) | **N** |
| [MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql) | **Y** |
| [OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch) | **Y** |
| [Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle) | **Y** |
| [PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql) | **Y** |
| [Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python) | **Y** |
| [Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source) | **Y** |
| [Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce) | **N** |
| [SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana) | **Y** |
| [SAP S/HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana) | **Y** |
| [SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql) | **Y** |
| [Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql) | **Y** |
| [Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake) | **Y** |
| [Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata) | **Y** |
| [TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv) | **Y** |
| [Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino) | **Y** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica) | **Y** |

<h2 id="multivalued-fields-2">
  Multivalued Fields
</h2>

Some connectors support aggregation by multivalued fields, such as arrays.

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

<table>
  <thead>
    <tr>
      <th>Connector</th>
      <th>Supported?</th>
      <th>Notes</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>[Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix)</td>
      <td>N/A</td>

      <td rowSpan={2} />
    </tr>

    <tr>
      <td>[Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix)</td>
      <td>N/A</td>
    </tr>

    <tr>
      <td>[Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr)</td>
      <td>**Y**</td>
      <td>The Apache Solr JSON API does not support metrics by multivalued fields.</td>
    </tr>

    <tr>
      <td>[BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery)</td>
      <td>N/A</td>
      <td>If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`.</td>
    </tr>

    <tr>
      <td>[Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase)</td>
      <td>N/A</td>
      <td>The Couchbase connector supports multivalued fields with some limitations. See the detailed description in [Manage the Couchbase Connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase).</td>
    </tr>

    <tr>
      <td>[Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi)</td>
      <td>source-dependent</td>

      <td />
    </tr>

    <tr>
      <td>[Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search)</td>
      <td>**Y**</td>

      <td rowSpan={2} />
    </tr>

    <tr>
      <td>[Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search)</td>
      <td>**Y**</td>
    </tr>

    <tr>
      <td>[File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb)</td>
      <td>**Y**</td>
      <td>Mongo DB unwinds multivalued fields which may result in incorrect metrics' results.</td>
    </tr>

    <tr>
      <td>[MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file)</td>
      <td>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica)</td>
      <td>N/A</td>

      <td />
    </tr>
  </tbody>
</table>

<h2 id="partitions">
  Partitions
</h2>

Some connectors support partitions and pruning. This feature enables the Partition column on the Fields tab of the [data source configuration](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#data-sources-page), when the data source uses a supporting connector. Partitioning allows you to link a partitioned field to another field to help improve the performance of filtering operations for a data source.

Although many data stores support partitions in some form, this feature specifically tells Self-Service Analytics that the partitions may be used for manual pruning of result sets to increase speed.

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| - | - |
| [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift) | N/A |
| [Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3) | N/A |
| [Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill) | **Y** |
| [Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | N/A |
| [Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | N/A |
| [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr) | N/A |
| [BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery) | N/A |
| [Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central) | **N** |
| [Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector) | **Y** |
| [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search) | N/A |
| [Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase) | **N** |
| [Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio) | N/A |
| [Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi) | source-dependent |
| [Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | N/A |
| [Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | N/A |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **N** |
| [HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs) | N/A |
| [Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive) | **Y** |
| [Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira) | **N** |
| [MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql) | N/A |
| [Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server) | **N** |
| [MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb) | N/A |
| [MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql) | **N** |
| [OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch) | N/A |
| [Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle) | **N** |
| [PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql) | **N** |
| [Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python) | **N** |
| [Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source) | N/A |
| [Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce) | **N** |
| [SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana) | **N** |
| [SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana) | **N** |
| [SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql) | **N** |
| [Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql) | **Y** |
| [Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake) | **N** |
| [Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata) | **N** |
| [TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv) | N/A |
| [Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino) | **N** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **N** |
| [Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica) | **N** |

<h2 id="schemas-2">
  Schemas
</h2>

When a connector supports schemas, it supports namespace, schema, or catalog notation for organizing collections. When schemas are supported, the [Source Creation tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-source-creation-tab) of the [data source configuration](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview) displays a Schema drop-down you can use to select a schema for the data source configuration. Elasticsearch has a custom UI for displaying multiple indices.

Visualize the relationships in your schemas in supported data sources, and connections. Add more relationships in connections as needed. See [Visualize Schemas and Joins](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/nested-data-structures#visualize-schemas-and-joins)

If you would like to make a default schema available to your users, or hide a schema from your users, update the properties file of your connector. See [Select Schemas](#select-schemas) .

<h3 id="select-schemas">
  Select Schemas
</h3>

Control which data source schemas are treated as internal by Self-Service Analytics and are not disclosed to users during source creation. Supported schemas are included in the Schema drop-down selector in the [Source Creation tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-source-creation-tab) of the [data source configuration](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview).

Add or edit the `system.schemas` property to the properties file of supported connectors to specify the schemas to use. Restart the connector after making these changes. The schemas you want to make available to users are visible in the Schema drop-down.

| Action | Update the properties file by: |
| - | - |
| Hide a data source schema from users | List the value of all default schemas, and add the value of the schema you want to hide to the `system.schemas` property. This hides all default schemas and the additional schema. |
| Show a data source schema that is hidden by default to users | List the value of all default schemas in the `system.schemas` property, except for the default schema you want to include for users. This hides all listed schemas, and displays the omitted default schema in the Schema drop-down. |

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| - | - |
| [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift) | **Y** |
| [Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3) | **Y** |
| [Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill) | **Y** |
| [Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr) | N/A |
| [BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery) | **Y** |
| [Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central) | **Y** |
| [Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector) | **Y** |
| [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search) | N/A |
| [Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase) | **Y** |
| [Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio) | **Y** |
| [Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi) | source-dependent |
| [Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | N/A |
| [Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | N/A |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs) | **Y** |
| [Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive) | **Y** |
| [Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira) | **Y** |
| [MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql) | **Y** |
| [Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server) | **Y** |
| [MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb) | **Y** |
| [MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql) | **Y** |
| [OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch) | N/A |
| [Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle) | **Y** |
| [PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql) | **Y** |
| [Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python) | **N** |
| [Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source) | **Y** |
| [Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce) | **Y** |
| [SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana) | **Y** |
| [SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana) | **Y** |
| [SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql) | **Y** |
| [Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql) | **Y** |
| [Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake) | **Y** |
| [Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata) | **Y** |
| [TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv) | **Y** |
| [Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino) | **Y** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica) | **Y** |

<h2 id="text-search">
  Text Search
</h2>

When a connector supports text searches, it can perform an efficient search on text fields. When text searches are supported, search control is enabled on dashboards using data sources that use the connector. To turn on text search, **Enable Text Search** in the [Global Settings tab](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#other-settings) for your sources.

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| - | - |
| [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift) | N/A |
| [Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3) | N/A |
| [Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill) | N/A |
| [Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | N/A |
| [Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | N/A |
| [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr) | **Y** |
| [BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery) | N/A |
| [Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central) | N/A |
| [Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector) | N/A |
| [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search) | **Y** |
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
| [MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb) | N/A |
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

<h2 id="tls">
  TLS
</h2>

Many connectors support SSL/TLS encryption.

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

| Connector | Supported? |
| - | - |
| [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift) | **Y** |
| [Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3) | **N** |
| [Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill) | **Y** |
| [Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) | **Y** |
| [Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr) | **N** |
| [BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery) | **Y** |
| [Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central) | **Y** |
| [Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector) | **Y** |
| [Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search) | **Y** |
| [Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase) | **Y** |
| [Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio) | **N** |
| [Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi) | source-dependent |
| [Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **Y** |
| [Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) | **Y** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs) | **N** |
| [Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive) | **Y** |
| [Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira) | **N** |
| [MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql) | **Y** |
| [Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server) | **Y** |
| [MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb) | **Y** |
| [MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql) | **Y** |
| [OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch) | **Y** |
| [Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle) | **Y** |
| [PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql) | **Y** |
| [Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python) | **N** |
| [Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source) | N/A |
| [Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce) | **N** |
| [SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana) | **Y** |
| [SAP S4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana) | **Y** |
| [SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql) | **Y** |
| [Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql) | **N** |
| [Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake) | **Y** |
| [Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata) | **Y** |
| [TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv) | **N** |
| [Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino) | **Y** |
| [File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) | **Y** |
| [Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica) | **Y** |

<h2 id="wildcard-case-insensitive-filters">
  Wildcard Case-Insensitive Filters
</h2>

Many connectors support case-insensitive wildcard filters.

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

<table>
  <thead>
    <tr>
      <th>Connector</th>
      <th>Supported?</th>
      <th>Notes</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>[Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix)</td>
      <td>**Y**</td>

      <td rowSpan={2} />
    </tr>

    <tr>
      <td>[Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix)</td>
      <td>**Y**</td>
    </tr>

    <tr>
      <td>[Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr)</td>
      <td>**N**</td>
      <td>Apache Solr connectors support wildcard filters, but case-sensitivity cannot be enforced. Consequently, neither case-sensitive or case-insensitive wildcard filters are supported.</td>
    </tr>

    <tr>
      <td>[BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery)</td>
      <td>**Y**</td>
      <td>If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`.</td>
    </tr>

    <tr>
      <td>[Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search)</td>
      <td>**N**</td>
      <td>Cloudera Search connectors support wildcard filters, but case-sensitivity cannot be enforced. Consequently, neither case-sensitive or case-insensitive wildcard filters are supported.</td>
    </tr>

    <tr>
      <td>[Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi)</td>
      <td>source-dependent</td>

      <td />
    </tr>

    <tr>
      <td>[Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search)</td>
      <td>**N**</td>
      <td rowSpan={2}>Elasticsearch connectors support wildcard filters, but case-sensitivity cannot be enforced. Consequently, neither case-sensitive or case-insensitive wildcard filters are supported.</td>
    </tr>

    <tr>
      <td>[Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search)</td>
      <td>**N**</td>
    </tr>

    <tr>
      <td>[File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica)</td>
      <td>**Y**</td>

      <td />
    </tr>
  </tbody>
</table>

<h2 id="wildcard-case-sensitive-filters">
  Wildcard Case-Sensitive Filters
</h2>

Many connectors support case-sensitive wildcard filters.

Support for this feature by connector is shown in the following table.

<strong>Key:</strong>**Y** - Supported; **N** - Not Supported; N/A - not applicable

<table>
  <thead>
    <tr>
      <th>Connector</th>
      <th>Supported?</th>
      <th>Notes</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>[Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix)</td>
      <td>**Y**</td>

      <td rowSpan={2} />
    </tr>

    <tr>
      <td>[Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix)</td>
      <td>**Y**</td>
    </tr>

    <tr>
      <td>[Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr)</td>
      <td>**N**</td>
      <td>Apache Solr connectors support wildcard filters, but case-sensitivity cannot be enforced. Consequently, neither case-sensitive or case-insensitive wildcard filters are supported.</td>
    </tr>

    <tr>
      <td>[BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery)</td>
      <td>**Y**</td>
      <td>If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`.</td>
    </tr>

    <tr>
      <td>[Business Central Jet](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search)</td>
      <td>**N**</td>
      <td>Cloudera Search connectors support wildcard filters, but case-sensitivity cannot be enforced. Consequently, neither case-sensitive or case-insensitive wildcard filters are supported.</td>
    </tr>

    <tr>
      <td>[Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Dundas BI (Managed)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi)</td>
      <td>source-dependent</td>

      <td />
    </tr>

    <tr>
      <td>[Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search)</td>
      <td>**N**</td>
      <td rowSpan={2}>Elasticsearch connectors support wildcard filters, but case-sensitivity cannot be enforced. Consequently, neither case-sensitive or case-insensitive wildcard filters are supported.</td>
    </tr>

    <tr>
      <td>[Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search)</td>
      <td>**N**</td>
    </tr>

    <tr>
      <td>[File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv)</td>
      <td>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[File Upload (Upload API)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file)</td>
      <td>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica)</td>
      <td>**Y**</td>

      <td />
    </tr>
  </tbody>
</table>
