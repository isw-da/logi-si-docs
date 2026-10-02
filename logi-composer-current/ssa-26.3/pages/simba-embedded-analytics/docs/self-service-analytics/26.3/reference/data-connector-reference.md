> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Data Connector Reference

Self-Service Analytics data connectors are used to connect to your data stores. Each data connector has capabilities and limitations when connected to the Self-Service Analytics server. This topic highlights those details and provides a link to more information about each connector. For information about setting the parameters required by a connector to connect to a data store, see [Create and Manage Data Store Connections](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing). For information on how to download and install a connector that is not provided in the default Self-Service Analytics installation, see [Obtain Additional Connector Servers](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#obtain-additional-connector-servers).

<Warning>
  You can use a Dundas BI connection as a data source or in a fusion data source in Self-Service Analytics. See [Add Data Store Connections](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#add-data-store-connections).
</Warning>

<table>
  <thead>
    <tr>
      <th scope="col">Connector</th>
      <th>Microservice</th>
      <th>Supported Versions</th>
      <th>Connector Port</th>
      <th>Other Actions Required & Notes</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>[Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift)</td>
      <td>`zoomdata-edc-redshift`</td>
      <td>1.0</td>
      <td>8202</td>
      <td>Install JDBC driver.</td>
    </tr>

    <tr>
      <td>[Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3)</td>
      <td>`zoomdata-edc-s3`</td>

      <td />

      <td>8129</td>
      <td>Separate download.</td>
    </tr>

    <tr>
      <td>[Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill)</td>
      <td>`zoomdata-edc-drill`</td>
      <td>1.14 - 1.16</td>
      <td>8095</td>
      <td>Separate download.</td>
    </tr>

    <tr>
      <td>[Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix)</td>
      <td>`zoomdata-edc-phoenix-4.7`</td>
      <td>4.7</td>
      <td>8124</td>
      <td>Apache Phoenix 4.4 and 4.5 require separate downloads.</td>
    </tr>

    <tr>
      <td>[Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix)</td>
      <td>`zoomdata-edc-phoenix-4.7-queryserver`</td>
      <td>4.7</td>
      <td>8125</td>

      <td />
    </tr>

    <tr>
      <td>[Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr)</td>
      <td>`zoomdata-edc-apache-solr`</td>
      <td>7.4 - 8.4</td>
      <td>8115</td>

      <td />
    </tr>

    <tr>
      <td>[BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery)</td>
      <td>`zoomdata-edc-bigquery`</td>

      <td />

      <td>8093</td>

      <td />
    </tr>

    <tr>
      <td>[Business Central](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connect-to-biz-central)</td>
      <td>`zoomdata-edc-businesscentral-jet`</td>
      <td>N/A</td>
      <td>8156</td>
      <td>Separate download.</td>
    </tr>

    <tr>
      <td>[Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector)</td>
      <td>`zoomdata-edc-impala`</td>
      <td>3.2 - 3.4</td>
      <td>8098</td>

      <td />
    </tr>

    <tr>
      <td>[Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search)</td>
      <td>`zoomdata-edc-cloudera-search`</td>
      <td>4.10 - 7.4</td>
      <td>8201</td>

      <td />
    </tr>

    <tr>
      <td>[Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase)</td>
      <td>`zoomdata-edc-couchbase`</td>
      <td>6.0.1</td>
      <td>8138</td>
      <td>Includes Couchbase Community Edition 6.0.0.</td>
    </tr>

    <tr>
      <td>[Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio)</td>
      <td>`zoomdata-edc-dremio`</td>
      <td>4.1 through 4.8</td>
      <td>8142</td>

      <td />
    </tr>

    <tr>
      <td>[Dundas BI (formerly Managed) Connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi)</td>
      <td>`zoomdata-edc-managed`</td>
      <td>Dundas BI 26.2 and later</td>
      <td>8013\*</td>

      <td>
        \*The default port is 8013, or depending on your configuration, set to 8080. Verify the exact port in use in the environment hosting the data source.

        <br />

        The user interface to interact with this connector must be enabled. See [Server-Level Variables](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables).
      </td>
    </tr>

    <tr>
      <td>[Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search)</td>
      <td>`zoomdata-edc-elasticsearch-7.0`</td>
      <td>7.0 - 7.17</td>
      <td>8139</td>

      <td />
    </tr>

    <tr>
      <td>[Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search)</td>
      <td>`zoomdata-edc-elasticsearch-8-0`</td>
      <td>8.1 - 8.3</td>
      <td>8147</td>

      <td />
    </tr>

    <tr>
      <td>[HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs)</td>
      <td>`zoomdata-edc-hdfs`</td>

      <td />

      <td>8126</td>
      <td>Separate download.</td>
    </tr>

    <tr>
      <td>[Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive)</td>
      <td>`zoomdata-edc-hive`</td>
      <td>2.1 - 3.1</td>
      <td>8132</td>

      <td />
    </tr>

    <tr>
      <td>[Jira Connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira)</td>
      <td>`zoomdata-edc-jira`</td>
      <td>Jira JDBC Driver 1.7.8.1002</td>
      <td>8151</td>
      <td>Separate download.</td>
    </tr>

    <tr>
      <td>[MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql)</td>
      <td>`zoomdata-edc-memsql`</td>
      <td>7.1 - 7.6</td>
      <td>8099</td>
      <td>Install JDBC driver.</td>
    </tr>

    <tr>
      <td>[Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server)</td>
      <td>`zoomdata-edc-mssql`</td>
      <td>12.0 (SQL Server 2014) - 16.0 (SQL Server 2022)</td>
      <td>8100</td>

      <td />
    </tr>

    <tr>
      <td>[MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb)</td>
      <td>`zoomdata-edc-mongo`</td>
      <td>3.4 - 4.4</td>
      <td>8123</td>

      <td />
    </tr>

    <tr>
      <td>[MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql)</td>
      <td>`zoomdata-edc-mysql`</td>
      <td>5.6 - 8.0</td>
      <td>8101</td>
      <td>Install JDBC driver.</td>
    </tr>

    <tr>
      <td>[Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle)</td>
      <td>`zoomdata-edc-oracle`</td>
      <td>11.2 - 21c</td>
      <td>8102</td>
      <td>Install JDBC driver.</td>
    </tr>

    <tr>
      <td>[OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch)</td>
      <td>`zoomdata-edc-opensearch`</td>
      <td>2.x to 2.17</td>
      <td>8134</td>

      <td />
    </tr>

    <tr>
      <td>[PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql)</td>
      <td>`zoomdata-edc-postgresql`</td>
      <td>9.6 - 14.0</td>
      <td>8105</td>

      <td />
    </tr>

    <tr>
      <td>[Python](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python)</td>
      <td>`zoomdata-edc-python`</td>

      <td />

      <td>8153</td>
      <td>Install Docker image. See [Manage the Python Connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-python).</td>
    </tr>

    <tr>
      <td>[Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source)</td>
      <td>`zoomdata-edc-rts`</td>

      <td />

      <td>8108</td>
      <td>Must be enabled.</td>
    </tr>

    <tr>
      <td>[Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce)</td>
      <td>`zoomdata-edc-salesforce`</td>
      <td>Simba Salesforce JDBC Driver 2.1.22</td>
      <td>8152</td>
      <td>Separate download.</td>
    </tr>

    <tr>
      <td>[SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana)</td>
      <td>`zoomdata-edc-saphana`</td>
      <td>2.0</td>
      <td>8109</td>
      <td>Separate download and install JDBC driver.</td>
    </tr>

    <tr>
      <td>[SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana)</td>
      <td>`zoomdata-edc-saphanacloud`</td>
      <td>N/A</td>
      <td>8205</td>
      <td>Separate download and install JDBC driver.</td>
    </tr>

    <tr>
      <td>[SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql)</td>
      <td>`zoomdata-edc-sapiq`</td>
      <td>16</td>
      <td>8121</td>
      <td>Separate download and install JDBC driver.</td>
    </tr>

    <tr>
      <td>[Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake)</td>
      <td>`zoomdata-edc-snowflake`</td>
      <td>whatever is currently supported in the cloud</td>
      <td>8131</td>
      <td>Separate download.</td>
    </tr>

    <tr>
      <td>[Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql)</td>
      <td>`zoomdata-edc-sparksql`</td>
      <td>2.3 - 3.0</td>
      <td>8116</td>

      <td />
    </tr>

    <tr>
      <td>[Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata)</td>
      <td>`zoomdata-edc-teradata`</td>
      <td>16.20</td>
      <td>8111</td>
      <td>Separate download and install JDBC driver.</td>
    </tr>

    <tr>
      <td>[TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv)</td>
      <td>`zoomdata-edc-tibcodv`</td>
      <td>8.0-8.1</td>
      <td>8140</td>

      <td>
        Separate download and install JDBC driver.

        <br />

        The default TDV server port for JDBC connections is 9401.
      </td>
    </tr>

    <tr>
      <td>[Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino)</td>
      <td>`zoomdata-edc-trino`</td>
      <td>351-390</td>
      <td>8148</td>
      <td>Separate download.</td>
    </tr>

    <tr>
      <td>[Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica)</td>
      <td>`zoomdata-edc-vertica`</td>
      <td>7.2</td>
      <td>8112</td>
      <td>Separate download and install JDBC driver.</td>
    </tr>
  </tbody>
</table>

In addition to the official connectors listed above, you can:

* Upload a [flat file](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) for viewing in visuals and dashboards.
* Dynamically upload and stream your data in real time using the [Upload API](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file#work-with-the-upload-api).

Both the [flat file uploads](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) and the [Upload API](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file#work-with-the-upload-api) use port 8105 and require that PostgreSQL be enabled. While these processes are not strictly data connectors, they are additional methods of providing data for Self-Service Analytics.
