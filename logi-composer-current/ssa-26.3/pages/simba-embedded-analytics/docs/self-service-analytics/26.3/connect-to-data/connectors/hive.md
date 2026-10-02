> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage the Hive Connector

The Self-Service Analytics Hive connector lets you access the data available in Hive storage using the Self-Service Analytics client. It can connect to both Hive on Tez and Hive on Tez with LLAP, depending on the JDBC URL you provide (see [Connect to Hive](#connect-to-hive) below). The Hive connector supports Hive versions 2.1 through 3.1.

Before you can establish a connection from Self-Service Analytics to Hive storage, a connector server needs to be installed and configured. See [Manage Connectors and Connector Servers](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#manage-connectors-and-connector-servers) for general instructions and [Connect to Hive](#connect-to-hive) for details specific to the Hive connector.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Create and Manage Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview) for more information. After you set up your data sources, create [dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards) and [visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#create-and-add-visuals-to-the-visual-gallery) from the data in these data sources.

## Feature Support

Connector support for specific [features](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? |
| - | - |
| [Admin-Defined Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/admin-fx-ov) | **Y** |
| [Box Plots](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#box-plots) | **Y** |
| [Custom SQL Queries](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#custom-sql-queries-2) | **Y** |
| [Derived Fields (Row-Level Expressions)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields) | **Y** |
| [Distinct Counts](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#distinct-counts) | **Y** |
| [Fast Distinct Values](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#fast-distinct-values) | N/A |
| [Group By Multiple Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-multiple-fields) | **Y** |
| [Group By Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-time) | **Y** |
| [Group By UNIX Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-unix-time) | **Y** |
| [Histogram Floating Point Values](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#histogram-floating-point-values) | **Y** |
| [Histograms](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#bars-histograms) | **Y** |
| [Kerberos Authentication](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/kerberos-sso) | **Y** |
| [Last Value](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#last-value) | **Y** |
| [Live Mode and Playback](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar#live-mode-and-historical-playback) | **Y** |
| [Multivalued Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#multivalued-fields-2) | N/A |
| [Nested Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/nested-data-structures) | N/A |
| [Partitions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#partitions) | **Y** |
| [Pushdown Joins for Fusion Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview#optimize-joins) | **Y** |
| [Schemas](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#schemas-2) | **Y** |
| [Text Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#text-search) | N/A |
| [TLS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#tls) | **Y** |
| [User Delegation](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#enable-user-delegation) | **Y** |
| [Wildcard Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#apply-wildcard-filters-to-a-visual-filter-snippet-or-dashboard) | **Y** |
| [Wildcard Filters, Case-Insensitive Mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-insensitive-filters) | **Y** |
| [Wildcard Filters, Case-Sensitive Mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-sensitive-filters) | **Y** |

<h2 id="connect-to-hive">
  Connect to Hive
</h2>

To establish a connection to Hive, you must specify a JDBC URL on the Connection page of your Self-Service Analytics data source definition for the Hive connection.

* Specify the JDBC URL for Hive.
* If authentication has been set up, provide the user name and password.
* If required, specify the Hive/YARN queue name in the Queue Name box.
* Specify the server timezone. If the timezone of your Hive server is in UTC, leave the Server Timezone box blank. Otherwise, specify the timezone abbreviation in all caps for correct handling the time data (for example, EST, EDT, or CST).
* Select **Validate** to test the connection.

To connect to Hive LLAP, the JDBC URL you must specify is different. If you use Hortonworks Data Platform (HDP), you can copy the URL from Ambari. See [https://docs.cloudera.com/HDPDocuments/HDP3/HDP-3.1.4/performance-tuning/content/hive\_connect\_clients\_to\_llap.html](https://docs.cloudera.com/HDPDocuments/HDP3/HDP-3.1.4/performance-tuning/content/hive_connect_clients_to_llap.html).

See also [Connect to Hive Sources on A Kerberized HDP Cluster](#connect-to-hive-sources-on-a-kerberized-hdp-cluster).

## Troubleshooting

If you run into a warning message that is displayed when you try to open a dashboard based on a Hive data source, see [Resolve the Hive Timeout Warning Message](#resolve-the-hive-timeout-warning-message).

<h2 id="connect-to-hive-sources-on-a-kerberized-hdp-cluster">
  Connect to Hive Sources on A Kerberized HDP Cluster
</h2>

A secure Hortonworks Data Platform (HDP) cluster uses Kerberos authentication to validate and confirm access requests. You can set up Self-Service Analytics to connect to the secure HDP cluster using the following instructions.

### Prepare the Hive Cluster

* To enable Kerberos for HDP distribution using a Hive source, refer to Hortonworks' documentation [Enabling Kerberos Authentication Using Ambari](https://docs.cloudera.com/HDPDocuments/HDP2/HDP-2.6.1/bk_security/content/configuring_amb_hdp_for_kerberos.html).
* Kerberos authentication requires precise time correspondence on all instances to work properly. You need to enable the Network Time Protocol service in your network. See [Use the Network Time Protocol to Synchronize Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#use-the-network-time-protocol-to-synchronize-time).

<h3 id="configure-self-service-analytics-microservices">
  Configure Self-Service Analytics Microservices
</h3>

#### Obtain Kerberos Credentials

Each microservice must have its own unique identifier called a [principal](http://web.mit.edu/kerberos/krb5-1.5/krb5-1.5.4/doc/krb5-user/What-is-a-Kerberos-Principal_003f.html). Perform the following steps:

1. Install the Kerberos client on the [CentOS](https://www.theurbanpenguin.com/configuring-a-centos-7-kerberos-kdc/) or [Ubuntu](https://help.ubuntu.com/lts/serverguide/kerberos.html#kerberos-linux-client) machine where the Self-Service Analytics server resides.

2. Generate the Kerberos principal and corresponding keytab for the Self-Service Analytics microservice. Before you proceed, make sure that:

   * The Self-Service Analytics microservice is running on a node with proper Kerberos configuration: `/etc/krb5.conf` or similar location for your Linux distribution.
   * The Kerberos realm on your environment is the same as the realm specified in the `kdc.conf` file from the Hive server.

3. Check the Kerberos configuration (that is, `krb5.conf`) and validity of the principal and keytab pair using MIT Kerberos client:

   ```
   kinit -V -k -t <composer_principal>.keytab <composer_principal@KERBEROS.REALM>
   ```

4. Make the keytab accessible for Self-Service Analytics's Hive connector:

   ```bash theme={null}
   sudo mkdir /etc/zoomdata
   sudo mv <composer_principal>.keytab /etc/zoomdata
   sudo chown zoomdata:zoomdata /etc/zoomdata/<composer_principal>.keytab
   sudo chmod 600 /etc/zoomdata/<composer_principal>.keytab
   ```

#### Configure a Hive Connector

1. Create or update the file named `/etc/zoomdata/edc-hive.properties`. If this file already exists, verify that the information below exists in the file:

   ```properties theme={null}
   kerberos.krb5.conf.location=/etc/krb5.conf
   kerberos.service.account.authentication=true
   kerberos.service.account.principal=<composer_principal@KERBEROS.REALM>
   kerberos.service.account.keytab.location=/etc/zoomdata/<composer_principal>.keytab
   ```

2. Restart the Hive connector:

   ```bash theme={null}
   sudo systemctl restart zoomdata-edc-hive
   ```

#### Connect to the Kerberized Hive Source

You are now ready to create the Hive source:

1. Open a new browser window and log into Self-Service Analytics.

2. Select **Sources**.

3. Select **Hive**.

4. Specify the name of your source and add a description (if desired). Then select **Next**.

5. On the **Connection** page, define the connection source. You can use an existing connection, if available, or create a new one. To create a new connection, select the **Input New Credentials** option button and specify the connection name and JDBC URL. Make sure that you enter the JDBC URL in the correct format:

   ```
   jdbc:hive2://<hive_host>:10000/;principal=<hive_principal@KERBEROS.REALM>
   ```

   Replace the placeholders as follows:

   * `<hive_host>`: Specify the IP address or host name of the Hive node to which you are connecting.

   * `<hive_principal@KERBEROS.REALM>`: Enter the principal of the Hive node you are connecting to. To get the list of all Hive principals, navigate to Ambari > Admin > Kerberos > Advanced > Hive.

     <Note>
       The *principal* spec contained in the JDBC URL refers to the principal of the Hive node. `<hive_principal@KERBEROS.REALM >` principal has nothing to do with the `<zoomdata_principal@KERBEROS.REALM>` principal specified for the Self-Service Analytics connector.
     </Note>

6. Select **Validate** and, after your connection is valid, select **Next**.

You can continue configuring the data source as described in [Create and Manage Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview).

After you have completed the configuration, Self-Service Analytics will begin accessing Hive using `zoomdata_principal@KERBEROS.REALM` authenticated by its keytab in `/etc/zoomdata/<composer_principal>.keytab`.

<h2 id="resolve-the-hive-timeout-warning-message">
  Resolve the Hive Timeout Warning Message
</h2>

<h3 id="resolve-the-hive-timeout-warning-message-troubleshooting">
  Troubleshooting
</h3>

**Issue description:** A timeout warning message is displayed when you try to open a dashboard based on a Hive data source. This is possibly being caused by the configuration of the Hive server.

**Workaround:** If you are encountering timeout errors, you can first try to create or modify the settings in the Hive configuration file `edc-hive.properties`. See [Configure Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov).

* Increase the timeout value that causes this exception to 2 minutes:

  ```properties theme={null}
  datasource.time-limits.max-wait-time-sec=120
  ```

* If the Hive server has at least 64 GB storage and 16 cores, modify the values for the following parameters:

  ```properties theme={null}
  datasource.connection-limits.max-idle=5
  datasource.connection-limits.max-total=5
  ```
