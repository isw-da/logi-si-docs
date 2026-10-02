> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage the Apache Phoenix Connector

The Self-Service Analytics Apache Phoenix connector lets you access the data available in your Apache Phoenix storage using the Self-Service Analytics client. The Self-Service Analytics Apache Phoenix connector supports Apache Phoenix version 4.7 and Apache Phoenix Query Server 4.7. Apache Phoenix v4.5 requires a separate download. To obtain a connector for Apache Phoenix 4.4, contact [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support).

Before you can establish a connection from Self-Service Analytics to Apache Phoenix, a Self-Service Analytics connector server for it needs to be installed, configured and enabled. See [Manage Connectors and Connector Servers](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#manage-connectors-and-connector-servers) for general instructions and [Connect to Apache Phoenix](#connect-to-apache-phoenix) for details specific to the Apache Phoenix and Apache Phoenix Query Server connectors.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Create and Manage Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview) for more information.After you set up your data sources, create [dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards), [self service reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage), and [visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#create-and-add-visuals-to-the-visual-gallery) from the data in these data sources.

## Feature Support

Connector support for specific [features](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th colSpan={3}>Supported?</th>
      <th>Notes</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>[Admin-Defined Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/admin-fx-ov)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Box Plots](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#box-plots)</td>
      <td colSpan={3}>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Custom SQL Queries](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#custom-sql-queries-2)</td>
      <td colSpan={3}>**Y**</td>
      <td>If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`.</td>
    </tr>

    <tr>
      <td>[Derived Fields (Row-Level Expressions)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields)</td>
      <td colSpan={3}>**Y**</td>

      <td>
        Apache Phoenix and Apache Phoenix Query Server connectors support row-level expressions (derived fields) with the following limitations:

        <br />

        * The filter IS NULL does not work properly on grouped fields.
        * The LOCATE [text row-level function](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#text-functions) only supports a constant as a argument.
        * A COALESCE [conditional row-level function](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#conditional-functions) specified with and empty argument does not work properly.
        * If the CASE [conditional row-level function](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#conditional-functions) returns a null value as a an argument of another function, a NullPointerException may occur.
        * The LPAD and RPAD [text row-level functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#text-functions) are not supported.
      </td>
    </tr>

    <tr>
      <td>[Distinct Counts](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#distinct-counts)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Fast Distinct Values](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#fast-distinct-values)</td>
      <td colSpan={3}>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Group By Multiple Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-multiple-fields)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Group By Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-time)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Group By UNIX Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-unix-time)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Histogram Floating Point Values](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#histogram-floating-point-values)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Histograms](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#bars-histograms)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Kerberos Authentication](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/kerberos-sso)</td>

      <td colSpan={3}>
        **Y**

        <br />

        /

        <br />

        **N**
      </td>

      <td>Apache Phoenix supports Kerberos, but Apache Phoenix Query Server does not. For more information, see [Enable Kerberos Authentication for Apache Phoenix Connectors](#enable-kerberos-authentication-for-apache-phoenix-connectors).</td>
    </tr>

    <tr>
      <td>[Last Value](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#last-value)</td>
      <td colSpan={3}>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Live Mode and Playback](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar#live-mode-and-historical-playback)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Multivalued Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#multivalued-fields-2)</td>
      <td colSpan={3}>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Nested Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/nested-data-structures)</td>
      <td colSpan={3}>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Partitions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#partitions)</td>
      <td colSpan={3}>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[Pushdown Joins for Fusion Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview#optimize-joins)</td>
      <td colSpan={3}>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Schemas](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#schemas-2)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Text Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#text-search)</td>
      <td colSpan={3}>N/A</td>

      <td />
    </tr>

    <tr>
      <td>[TLS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#tls)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[User Delegation](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#enable-user-delegation)</td>
      <td colSpan={3}>**N**</td>

      <td />
    </tr>

    <tr>
      <td>[Wildcard Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#apply-wildcard-filters-to-a-visual-filter-snippet-or-dashboard)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Wildcard Filters, Case-Insensitive Mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-insensitive-filters)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Wildcard Filters, Case-Sensitive Mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-sensitive-filters)</td>
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>
  </tbody>
</table>

<h2 id="connect-to-apache-phoenix">
  Connect to Apache Phoenix
</h2>

For Apache Phoenix, specify the JDBC URL in the following format:

```
jdbc:phoenix:<zk_quorum>:<zk_port>:<zk_hbase_path>
```

where:

* `<zk_quorum>` is a comma separated list of the ZooKeeper servers
* `<zk_port>` is the ZooKeeper port
* `<zk_hbase_path>` is the path used by HBase to stop information about the instance

For Apache Phoenix Query Server, specify the JDBC URL in the following format:

```
jdbc:phoenix:thin:url=<scheme>://<server-hostname>:<port>
```

where:

* `<scheme>` is a transport protocol for communication with the server
* `<server-hostname>` is the name of the host offering the microservice
* `<port>` is the port number on which the host is listening

<h2 id="add-patched-jar-files-to-an-apache-phoenix-connector-s-classpath">
  Add Patched JAR Files to an Apache Phoenix Connector's Classpath
</h2>

If your Apache Phoenix/HBase servers use patched `.jar` files, you might need to add the patched `.jar` files to the Apache Connector's classpath. If you do not, Apache Phoenix may produce an error indicating that you have outdated `.jar` files.

**Add the patched** `.jar` **files to the Apache Phoenix connector's classpath:**

1. Add the patched `.jar` files to a directory that is accessible to the connector. For example:

   ```
   /usr/local/share/java/zoomdata/phoenix
   ```

2. Add or modify the following property in the `/etc/zoomdata/edc-phoenix-4.7.properties` file to specify the path to your `.jar` files as a comma-separated list in `loader.path` property. Be sure to put the path to your `.jar` files first so you do not corrupt entries already present in this property. For example:

   ```properties theme={null}
   loader.path=/usr/local/share/java/zoomdata/phoenix,lib/edc-phoenix-4.7/phoenix-core-4.7.0-HBase-1.1.jar
   ```

<h2 id="enable-kerberos-authentication-for-apache-phoenix-connectors">
  Enable Kerberos Authentication for Apache Phoenix Connectors
</h2>

Support for Kerberos authentication for Self-Service Analytics Apache Phoenix connectors is only provided for Phoenix 4.7 (and later) connectors. It is not provided for any version of the Phoenix QueryServer connector.

**Enable Kerberos authentication for Apache Phoenix connectors:**

1. Download `hbase-site.xml` and `core-site.xml` files from the Apache HDFS and HBase microservices. For example, for Hortonworks you can use the instructions at the following link: [https://docs.cloudera.com/HDPDocuments/Ambari-2.6.2.2/bk\_ambari-operations/content/downloading\_client\_configs.html](https://docs.cloudera.com/HDPDocuments/Ambari-2.6.2.2/bk_ambari-operations/content/downloading_client_configs.html).

2. Add the following configuration options to the `hbase-site.xml` file:

   ```xml theme={null}
   <property>
       <name>hbase.myclient.principal</name>
       <value>YOUR_PRINCIPAL</value>
   </property>
   <property>
       <name>hbase.myclient.keytab</name>
       <value>PATH_TO_YOUR_KEYTAB</value>
   </property>
   ```

   Substitute the ID of your Kerberos principal for `YOUR_PRINCIPAL` and the path to your Kerberos keytab file for `PATH_TO_YOUR_KEYTAB`.

3. Verify that the `core-site.xml` file contains the following entry:

   ```xml theme={null}
   <property>
       <name>hadoop.security.authentication</name>
       <value>kerberos</value>
   </property>
   ```

4. Make sure that the Apache Phoenix connector has access to the `hbase-site.xml` and `core-site.xml` files as well as the Kerberos keytab file you identified in `PATH_TO_YOUR_KEYTAB`. We recommend that you place these files in the `/etc/zoomdata/edc-phoenix` directory.

5. Add the following property to the `/etc/zoomdata/edc-phoenix-4.7.properties` file to direct the Apache Phoenix connector to the files you created

   ```properties theme={null}
   datasource.config.files-path=/etc/zoomdata/edc-phoenix
   ```

   <Note>
     Self-Service Analytics does not recommend that you provide the Kerberos principal ID and keytab file path using a JDBC URL. The Apache Phoenix driver has a bug that will not refresh a ticket after expiration.
   </Note>
