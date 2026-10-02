> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage the Oracle Connector

The Self-Service Analytics Oracle connector lets you access the data available in Oracle databases using the Self-Service Analytics client. The Self-Service Analytics Oracle connector supports Oracle versions 13 - 23.4.

Before you can establish a connection from Self-Service Analytics to Oracle storage, a connector server needs to be installed and configured. See [Manage Connectors and Connector Servers](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#manage-connectors-and-connector-servers) for general instructions and [Connect to Oracle](#connect-to-oracle) for details specific to the Oracle connector.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Create and Manage Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview) for more information. After you set up your data sources, create [dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#create-dashboards), [self service reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage), and [visuals](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-add-dash#create-and-add-visuals-to-the-visual-gallery) from the data in these data sources.

### Feature Support

Connector support for specific [features](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | Notes |
| - | - | - |
| [Admin-Defined Functions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/admin-fx-ov) | **Y** | |
| [Box Plots](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/scatter-plot#box-plots) | **Y** | |
| [Custom SQL Queries](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#custom-sql-queries-2) | **Y** | If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`. |
| [Derived Fields (Row-Level Expressions)](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/derived-fields) | **Y** | |
| [Distinct Counts](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/fx-aggregate#distinct-counts) | **Y** | |
| [Fast Distinct Values](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#fast-distinct-values) | N/A | |
| [Group By Multiple Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-multiple-fields) | **Y** | |
| [Group By Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-time) | **Y** | |
| [Group By UNIX Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#group-by-unix-time) | **Y** | |
| [Histogram Floating Point Values](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#histogram-floating-point-values) | **Y** | |
| [Histograms](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/bar-standard#bars-histograms) | **Y** | |
| [Kerberos Authentication](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/kerberos-sso) | **N** | |
| [Last Value](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#last-value) | **Y** | |
| [Live Mode and Playback](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/time-bar#live-mode-and-historical-playback) | **Y** | |
| [Multivalued Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#multivalued-fields-2) | N/A | |
| [Nested Fields](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/nested-data-structures) | N/A | |
| [Partitions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#partitions) | **N** | |
| [Pushdown Joins for Fusion Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-fusion-overview#optimize-joins) | **Y** | |
| [Schemas](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#schemas-2) | **Y** | |
| [Text Search](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#text-search) | N/A | |
| [TLS](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#tls) | **Y** | |
| [User Delegation](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#enable-user-delegation) | **Y** | The Self-Service Analytics Oracle connector supports user delegation only via user credential pass-through. |
| [Wildcard Filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/filters/filters-attr#apply-wildcard-filters-to-a-visual-filter-snippet-or-dashboard) | **Y** | |
| [Wildcard Filters, Case-Insensitive Mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-insensitive-filters) | **Y** | |
| [Wildcard Filters, Case-Sensitive Mode](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connector-feature-support#wildcard-case-sensitive-filters) | **Y** | |

<h3 id="connect-to-oracle">
  Connect to Oracle
</h3>

The Oracle connector requires a JDBC driver to be configured before you can connect to your data source. You can download the driver from the vendor's site. If you are upgrading, keep in mind you need to configure the JDBC driver- see [Upgrade Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/upgrading-server) for instructions. For more information and steps, see [Add a JDBC Driver](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#add-a-jdbc-driver).

When setting up a connection to Oracle, provide the following.

* Specify the connection name and JDBC URL. The JDBC URL for Oracle database being connected must be: `jdbc:oracle:thin@//ORACLEHOST:PORT/DATABASE_NAME` or `jdbc:oracle:thin:@ORACLEHOST:PORT:SID`

  To connect to Oracle with TLS enabled, see [Connect to Oracle with TLS Enabled](#connect-to-oracle-with-tls-enabled).

* Provide the user name and password for Oracle database.

* You can use an Impersonation feature to work with Oracle data source on behalf of a proxy user. Before you begin, you must configure proxy users with the corresponding privileges in the Oracle database. To use this, select the **Impersonation Enabled** checkbox and specify the **Impersonation Username** and **Impersonation Password**. See [Configure Settings to Use a Proxy User](#configure-settings-to-use-a-proxy-user).

* If you need to use Self-Service Analytics's Oracle connector to access a table that uses the XML data type, complete the additional setup steps described in [Enable Access to Oracle Tables That Use the XML Data Type](#enable-access-to-oracle-tables-that-use-the-xml-data-type).

<Note>
  If there are any changes in the Oracle database, you must clear the Self-Service Analytics cache. See [How Self-Service Analytics Caches Data](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-global-settings-tab#how-self-service-analytics-caches-data).
</Note>

<h3 id="connect-to-oracle-with-tls-enabled">
  Connect to Oracle with TLS Enabled
</h3>

Before you attempt to connect to Oracle with TLS enabled, make sure you have first installed Java Cryptography Extension (JCE). See [https://www.oracle.com/java/technologies/javase-jce8-downloads.html](https://www.oracle.com/java/technologies/javase-jce8-downloads.html).

**Connect to Oracle with TLS enabled**

1. Create a JDBC URL with TLS parameters. To specify TLS-related parameters, use the following template for a JDBC URL:

   ```
   jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=<oracle_host>)
   (PORT=<oracle_tls_port))CONNECT_DATA=(SID=<service_id>)))
   ```

   where:

   * `<oracle_host>` is the host of the Oracle database.
   * `<oracle_tls_port>` is the port of the Oracle database with TLS enabled
   * `<service_id>` is the Oracle service ID or database to which you want to connect

   Make sure your JDBC URL uses the correct protocol. For a TLS connection, you should use `tcps`.

2. If your Oracle database is configured with a custom certificate, you should configure a truststore for the Oracle connector, as described in the following steps:

   1. Copy a truststore to the machine on which Self-Service Analytics's Oracle connector is running.

   2. Add the following lines to file `edc-oracle.jvm`.

      ```properties theme={null}
      -Djavax.net.ssl.trustStore=<path_to_truststore>
      -Djavax.net.ssl.trustStorePassword=<truststore_password>
      ```

      * Linux: Copy the file `edc-oracle.jvm` from the `/opt/zoomdata/conf` directory if a copy is not in `/etc/zoomdata/`.
      * Windows: Copy the file `edc-oracle.jvm` from the `<install-path>/conf` directory if a copy is not in `<install-path>/conf-modify`.

      where:

      * `<path_to_truststore>` is the absolute path to your truststore
      * `<truststore_password>` is the password for your truststore

3. Restart the Oracle connector microservice, `zoomdata-edc-oracle`. See [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

<h3 id="configure-settings-to-use-a-proxy-user">
  Configure Settings to Use a Proxy User
</h3>

To enable a Self-Service Analytics user work as a proxy user, specify the user attributes of corresponding oracle user (that will be used as proxy user) in the account details of a Self-Service Analytics user.

You must specify the user attributes for each Self-Service Analytics user that will access the Oracle data source as a proxy user.

Perform the following steps:

1. Log in as an administrator or member of the supervisors group for your instance or selected tenant.
2. Select **Users** from the menu. The Users work area appears, listing all users in your instance or selected tenant.
3. Select a user from the list and select their **Custom Attributes** tab.
4. Select **Add Custom Attribute**. Specify credentials for a user as follows:

* **Key** - specify the login attribute for proxy user. Corresponding reference name is listed in the **Usage** column. You have to specify the value from the **Usage** column in the **Impersonation** **Username** field while creating a connection.
* **Value** - specify the actual name of the oracle user that you want to use as proxy user.
* Select the checkbox in the **Secure** column to encrypt the value of the key.

4. If the proxy user requires a password, select **Add Custom Attribute** and specify the key and value for the password. You have to specify the reference name from the **Usage** column in the **Impersonation Password** field while creating the connection.

<h3 id="enable-access-to-oracle-tables-that-use-the-xml-data-type">
  Enable Access to Oracle Tables That Use the XML Data Type
</h3>

Before you enable access to Oracle tables that use the XML data type, be sure you have set up the Oracle JDBC driver. See [Add a JDBC Driver](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#add-a-jdbc-driver).

**Enable access to Oracle tables that use the XML data type**

1. Download the `xdb6.jar` and `xmlparserv2.jar` files from Oracle to the corresponding Self-Service Analytics instance. You can download obtain `xdb6.jar` by downloading it from [https://www.oracle.com/database/technologies/jdbc-ucp-122-downloads.html](https://www.oracle.com/database/technologies/jdbc-ucp-122-downloads.html). You can obtain `xmlparserve2.jar` by extracting it from the `lib` directory in the Oracle XML Developers Kit, which can be downloaded from [https://www.oracle.com/downloads/](https://www.oracle.com/downloads/).

   Place these files in the following folder:

   * Linux: `/opt/zoomdata/lib/edc-oracle/`
   * Windows: `<install-path>/lib/edc-oracle/`

   <Note>
     Note that this is the same folder where you downloaded the Oracle JDBC driver (see [Add a JDBC Driver](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#add-a-jdbc-driver)).
   </Note>

2. Add the following lines to the connector JVM file:

   ```properties theme={null}
   -Djavax.xml.parsers.DocumentBuilderFactory=org.apache.xerces.jaxp.DocumentBuilderFactoryImpl
   -Djavax.xml.transform.TransformerFactory=com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl
   ```

   * Linux: `/etc/zoomdata/edc-oracle.jvm`
   * Windows: `<install-path>/conf-modify/`

3. Restart the Oracle connector microservice, `zoomdata-edc-oracle`. See [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).
