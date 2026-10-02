> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Default Port Reference

The following table lists the default ports used by Self-Service Analytics, sorted by port number.

<table>
  <thead>
    <tr>
      <th scope="col">Port</th>
      <th>Microservice</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>80</td>
      <td>data gateway service</td>
      <td>The port for the [data gateway service](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/data-gateway#set-up-and-use-the-data-gateway-service).</td>
    </tr>

    <tr>
      <td>443</td>
      <td>`zoomdata`</td>

      <td>
        Self-Service Analytics server web communication.

        <br />

        For HTTPS requests, configure your firewall to map port 443 to either port 8443 or port 8080.
      </td>
    </tr>

    <tr>
      <td>5432</td>
      <td>`zoomdata-postgres`</td>
      <td>Self-Service Analytics [metadata repository](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis#metadata-repository).</td>
    </tr>

    <tr>
      <td>5580</td>
      <td>`zoomdata-query-engine`</td>
      <td>Self-Service Analytics [query engine](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#manage-the-self-service-analytics-query-engine) microservice.</td>
    </tr>

    <tr>
      <td>8013\*</td>
      <td>`zoomdata-edc-managed`</td>

      <td>
        [Dundas BI (Managed) Connector](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/dbi) to communicate with Dundas BI managed resources.

        <br />

        \*The default port is 8013, or depending on your configuration, set to 8080. Verify the exact port in use in the environment hosting the data source.

        <br />

        The user interface to interact with this connector must be enabled. See [Server-Level Variables](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables).
      </td>
    </tr>

    <tr>
      <td>8050</td>
      <td>`zoomdata-admin-server`</td>
      <td>[Service Monitor](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/service-monitor-overview).</td>
    </tr>

    <tr>
      <td>8080</td>
      <td>`zoomdata`</td>
      <td>Self-Service Analytics server.</td>
    </tr>

    <tr>
      <td>8081</td>
      <td>`zoomdata-data-writer`</td>
      <td>Self-Service Analytics [Data Writer](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#data-writer-microservice) microservice.</td>
    </tr>

    <tr>
      <td>8083</td>
      <td>`zoomdata-screenshot-service`</td>
      <td>Self-Service Analytics [Screenshot](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/screenshot-install) microservice.</td>
    </tr>

    <tr>
      <td>8093</td>
      <td>`zoomdata-edc-bigquery`</td>
      <td>[BigQuery](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-bigquery) connector.</td>
    </tr>

    <tr>
      <td>8095</td>
      <td>`zoomdata-edc-drill`</td>
      <td>[Apache Drill](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-drill) connector.</td>
    </tr>

    <tr>
      <td>8098</td>
      <td>`zoomdata-edc-impala`</td>
      <td>[Cloudera Impala](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-ov#manage-the-impala-connector) connector.</td>
    </tr>

    <tr>
      <td>8099</td>
      <td>`zoomdata-edc-memsql`</td>
      <td>[MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql) connector.</td>
    </tr>

    <tr>
      <td>8100</td>
      <td>`zoomdata-edc-mssql`</td>
      <td>[Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server) connector.</td>
    </tr>

    <tr>
      <td>8101</td>
      <td>`zoomdata-edc-mysql`</td>
      <td>[MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql) connector.</td>
    </tr>

    <tr>
      <td>8102</td>
      <td>`zoomdata-edc-oracle`</td>
      <td>[Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle) connector.</td>
    </tr>

    <tr>
      <td>8105</td>
      <td>`zoomdata-edc-postgresql`</td>
      <td>[PostgreSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-postgresql) connector, [Flat File](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) and API uploads for processing.</td>
    </tr>

    <tr>
      <td>8108</td>
      <td>`zoomdata-edc-rts`</td>
      <td>[Real Time Sales](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source) connector.</td>
    </tr>

    <tr>
      <td>8109</td>
      <td>`zoomdata-edc-saphana`</td>
      <td>[SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana) connector.</td>
    </tr>

    <tr>
      <td>8111</td>
      <td>`zoomdata-edc-teradata`</td>
      <td>[Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata) connector.</td>
    </tr>

    <tr>
      <td>8112</td>
      <td>`zoomdata-edc-vertica`</td>
      <td>[Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica) connector.</td>
    </tr>

    <tr>
      <td>8115</td>
      <td>`zoomdata-edc-apache-solr`</td>
      <td>[Apache Solr](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-solr) connector.</td>
    </tr>

    <tr>
      <td>8116</td>
      <td>`zoomdata-edc-sparksql`</td>
      <td>[Spark SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sparksql) connector.</td>
    </tr>

    <tr>
      <td>8121</td>
      <td>`zoomdata-edc-sapiq`</td>
      <td>[SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql) connector.</td>
    </tr>

    <tr>
      <td>8123</td>
      <td>`zoomdata-edc-mongo`</td>
      <td>[MongoDB](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mongodb) connector.</td>
    </tr>

    <tr>
      <td>8124</td>
      <td>`zoomdata-edc-phoenix-4.7`</td>
      <td>[Apache Phoenix](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) connector.</td>
    </tr>

    <tr>
      <td>8125</td>
      <td>`zoomdata-edc-phoenix-4.7-queryserver`</td>
      <td>[Apache Phoenix Query Server (QS)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-apache-phoenix) connector.</td>
    </tr>

    <tr>
      <td>8126</td>
      <td>`zoomdata-edc-hdfs`</td>
      <td>[HDFS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hdfs) connector.</td>
    </tr>

    <tr>
      <td>8129</td>
      <td>`zoomdata-edc-s3`</td>
      <td>[Amazon S3](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-s3) connector.</td>
    </tr>

    <tr>
      <td>8131</td>
      <td>`zoomdata-edc-snowflake`</td>
      <td>[Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake) connector.</td>
    </tr>

    <tr>
      <td>8132</td>
      <td>`zoomdata-edc-hive`</td>
      <td>[Hive](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/hive) connector.</td>
    </tr>

    <tr>
      <td>8138</td>
      <td>`zoomdata-edc-couchbase`</td>
      <td>[Couchbase](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/couchbase) connector.</td>
    </tr>

    <tr>
      <td>8139</td>
      <td>`zoomdata-edc-elasticsearch-7.0`</td>
      <td>[Elasticsearch 7.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) connector.</td>
    </tr>

    <tr>
      <td>8140</td>
      <td>`zoomdata-edc-tibcodv`</td>
      <td>[TIBCO DV](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/tibcodv) connector.</td>
    </tr>

    <tr>
      <td>8142</td>
      <td>`zoomdata-edc-dremio`</td>
      <td>[Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio) connector.</td>
    </tr>

    <tr>
      <td>8147</td>
      <td>`zoomdata-edc-elasticsearch-8-0`</td>
      <td>[Elasticsearch 8.0](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search) connector.</td>
    </tr>

    <tr>
      <td>8148</td>
      <td>`zoomdata-edc-trino`</td>
      <td>[Trino](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-trino) connector.</td>
    </tr>

    <tr>
      <td>8201</td>
      <td>`zoomdata-edc-cloudera-search`</td>
      <td>[Cloudera Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/cloudera-search) connector.</td>
    </tr>

    <tr>
      <td>8202</td>
      <td>`zoomdata-edc-redshift`</td>
      <td>[Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift) connector.</td>
    </tr>

    <tr>
      <td>8205</td>
      <td>`zoomdata-edc-saphanacloud`</td>
      <td>[SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana) connector.</td>
    </tr>

    <tr>
      <td>8300</td>
      <td>`zoomdata-consul`</td>
      <td>Internal port used by the Consul for inter-node communication in a distributed environment.</td>
    </tr>

    <tr>
      <td>8301</td>
      <td>`zoomdata-consul`</td>
      <td>Internal port used by the Consul for inter-node communication in a distributed environment.</td>
    </tr>

    <tr>
      <td>8302</td>
      <td>`zoomdata-consul`</td>
      <td>Internal port used by the Consul for inter-node communication in a distributed environment.</td>
    </tr>

    <tr>
      <td>8443</td>
      <td>`zoomdata`</td>
      <td>Self-Service Analytics HTTPS requests.</td>
    </tr>

    <tr>
      <td>8500</td>
      <td>`zoomdata-consul`</td>
      <td>Consul.</td>
    </tr>

    <tr>
      <td>8888</td>
      <td>`zoomdata-config-server`</td>
      <td>Self-Service Analytics [configuration](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#configuration-microservice) microservice.</td>
    </tr>
  </tbody>
</table>
