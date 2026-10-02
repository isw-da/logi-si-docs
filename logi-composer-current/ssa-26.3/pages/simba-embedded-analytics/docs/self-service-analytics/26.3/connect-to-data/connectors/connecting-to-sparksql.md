> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage the Spark SQL Connector

The Self-Service Analytics Spark SQL connector lets you access the data available in Spark SQL databases using the Self-Service Analytics client. The Self-Service Analytics Spark SQL connector supports Spark SQL versions 2.3 through 3.0.

Before you can establish a connection from Self-Service Analytics to Spark SQL storage, a connector server needs to be installed and configured. See [Manage Connectors and Connector Servers](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#manage-connectors-and-connector-servers) for general instructions and [Connect to Spark SQL](#connect-to-spark-sql) for details specific to the Spark SQL connector.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Create and Manage Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview) for more information. After you set up your data sources, create [dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards), [self service reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage), and [visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#create-and-add-visuals-to-the-visual-gallery) from the data in these data sources.

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
      <td colSpan={3}>**Y**</td>

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

      <td />
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
      <td colSpan={3}>**Y**</td>
      <td>To enable Kerberos authentication, see [Connect to Spark SQL Sources on a Kerberized HDP Cluster](#connect-to-spark-sql-sources-on-a-kerberized-hdp-cluster).</td>
    </tr>

    <tr>
      <td>[Last Value](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#last-value)</td>
      <td colSpan={3}>**Y**</td>

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
      <td colSpan={3}>**Y**</td>

      <td />
    </tr>

    <tr>
      <td>[Pushdown Joins for Fusion Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview#optimize-joins)</td>
      <td colSpan={3}>**Y**</td>

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
      <td colSpan={3}>**N**</td>

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

<h2 id="connect-to-spark-sql">
  Connect to Spark SQL
</h2>

When establishing a connection to Spark SQL, you need to provide the following information when setting up the partition settings.

Configure the partition settings. For the partitioned fields you can select one of the following options:

* **No**
* **Date** - this option is available for the Time field type. If you select this option, the list of the partitioned columns will be displayed in the Configure column.

Numeric and time-based fields can be edited using the Fields tab:

* Numeric type Number - ability to select a default aggregation function
* Time fields - ability to define the default time pattern and granularity; if the time field provides granularities of hour, minute and second, then a time zone label may be applied.

When you create a data source, the specific number of distinct values for the attribute fields are saved in Self-Service Analytics depending on the data sample from your data set. You can filter the data on your visual by these values. While editing a data source, if you want to use all distinct values in the filter (that is from whole data source), select **Refresh** in the **Statistics** column.

<h2 id="connect-to-spark-sql-sources-on-a-kerberized-hdp-cluster">
  Connect to Spark SQL Sources on a Kerberized HDP Cluster
</h2>

A secure Hortonworks Data Platform (HDP) cluster uses Kerberos authentication to validate and confirm access requests. You can set up Self-Service Analytics to connect to the secure HDP cluster using the following instructions.

### Prepare the Spark SQL Cluster

* To enable Kerberos for HDP distribution using a Spark SQL source, refer to Hortonworks' documentation [Enabling Kerberos Authentication Using Ambari](https://docs.cloudera.com/HDPDocuments/HDP2/HDP-2.6.1/bk_security/content/configuring_amb_hdp_for_kerberos.html).
* Kerberos authentication requires precise time correspondence on all instances to work properly. You need to enable the Network Time Protocol service in your network. See [Use the Network Time Protocol to Synchronize Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#use-the-network-time-protocol-to-synchronize-time).
* Set up a Thrift JDBC/ODBC server in your environment. See [Spark documentation](https://spark.apache.org/docs/latest/sql-distributed-sql-engine.html).

<h3 id="configure-self-service-analytics-microservices">
  Configure Self-Service Analytics Microservices
</h3>

#### Obtain Kerberos Credentials

Each microservice must have its own unique identifier called a [principal](http://web.mit.edu/kerberos/krb5-1.5/krb5-1.5.4/doc/krb5-user/What-is-a-Kerberos-Principal_003f.html). Perform the following steps:

1. Install the Kerberos client on the [CentOS](https://www.theurbanpenguin.com/configuring-a-centos-7-kerberos-kdc/) or [Ubuntu](https://help.ubuntu.com/lts/serverguide/kerberos.html#kerberos-linux-client) machine where the Self-Service Analytics server resides.

2. Generate the Kerberos principal and corresponding keytab for the Self-Service Analytics microservice. Before you proceed, make sure that:

   * The Self-Service Analytics microservice is running on a node with proper Kerberos configuration: `/etc/krb5.conf` or similar location for your Linux distribution.
   * The Kerberos realm on your environment is the same as the realm specified in the `kdc.conf` file from the Spark SQL server.

3. Check the Kerberos configuration (that is, `krb5.conf`) and validity of the principal and keytab pair using MIT Kerberos client:

   ```
   kinit -V -k -t <composer_principal>.keytab <composer_principal@KERBEROS.REALM>
   ```

4. Make the keytab accessible for Self-Service Analytics's Spark SQL connector:

   ```bash theme={null}
   sudo mkdir /etc/zoomdata sudo mv <composer_principal>.keytab /etc/zoomdata sudo chown zoomdata:zoomdata /etc/zoomdata/<composer_principal>.keytab sudo chmod 600 /etc/zoomdata/<composer_principal>.keytab
   ```

#### Configure a Spark SQL Connector

1. Create or update the file named `/etc/zoomdata/edc-sparksql.properties`. If this file already exists, verify that the information below exists in the file:

   ```properties theme={null}
   kerberos.krb5.conf.location=/etc/krb5.conf kerberos.service.account.authentication=true kerberos.service.account.principal=<composer_principal@KERBEROS.REALM> kerberos.service.account.keytab.location=/etc/zoomdata/<composer_principal>.keytab
   ```

2. Restart the Spark SQL connector:

   ```bash theme={null}
   sudo systemctl restart zoomdata-edc-sparksql
   ```

#### Connect to the Kerberized Spark SQL Source

You are now ready to create the Spark SQL source:

1. Open a new browser window and log into Self-Service Analytics.

2. Select **Sources**.

3. Select **Spark SQL**.

4. Specify the name of your source and add a description (if desired). Then select **Next**.

5. On the **Connection** page, define the connection source. You can use an existing connection, if available, or create a new one. To create a new connection, select the **Input New Credentials** option button and specify the connection name and JDBC URL. Make sure that you enter the JDBC URL in the correct format:

   ```
   jdbc:hive2://<spark-sql-host>:10000/;principal=<spark-sql-principal@KERBEROS.REALM>
   ```

   Replace the placeholders as follows:

   * `<spark_sql_host>`: Specify the IP address or host name of the Spark SQL node to which you are connecting.

   * `<spark_sql_principal@KERBEROS.REALM>`: Enter the principal of the Spark SQL node you are connecting to. To get the list of all Spark SQL principals, navigate to Ambari > Admin > Kerberos > Advanced > Spark SQL.

     <Note>
       The `principal` spec contained in the JDBC URL refers to the principal of the Spark SQL node. `spark_sql_principal@KERBEROS.REALM` principal has nothing to do with the `zoomdata_principal@KERBEROS.REALM` principal specified for the Self-Service Analytics connector.
     </Note>

6. Select **Validate** and, after your connection is valid, select **Next**.

You can continue configuring the data source as described in [Create and Manage Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview).

After you have completed the configuration, Self-Service Analytics will begin accessing Spark SQL using `zoomdata_principal@KERBEROS.REALM` authenticated by its keytab in `/etc/zoomdata/<composer_principal>.keytab`.
