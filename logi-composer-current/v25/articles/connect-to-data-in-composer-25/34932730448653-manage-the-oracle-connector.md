---
title: "Manage the Oracle Connector"
id: 34932730448653
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730448653-Manage-the-Oracle-Connector
updated_at: 2026-05-26T22:10:07Z
---

# Manage the Oracle Connector

# Manage the Oracle Connector

The Composer Oracle connector lets you access the data available in Oracle databases using the Composer client. The Composer Oracle connector supports Oracle versions 13 - 23.4.

Before you can establish a connection from Composer to Oracle storage, a connector server needs to be installed and configured.
See [Manage Connectors and Connector Servers](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932741363981-Manage-Connectors-and-Connector-Servers) for general instructions and [Connect to Oracle](#Connecti) for details specific to the Oracle connector.

After setting up the connector, create data sources that specify the necessary connection information and identify the data you want to use. See [Manage Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932941009037-Manage-Data-Sources) for more information. After you set up your data sources, create [dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763355021-Create-Dashboards) and [visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933273224589-Create-and-Add-Visuals-to-the-Visual-Gallery) from from the data in these data sources. See [Create Dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763355021-Create-Dashboards).

## Feature Support

Connector support for specific  [features](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932704861453-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | Notes |
| --- | --- | --- |
| [Admin-Defined Functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932796673933-Admin-Defined-Functions) | **Y** |  |
| [Box Plots](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933208692493-Box-Plots) | **Y** |  |
| [Custom SQL Queries](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932704947213-Custom-SQL-Queries) | **Y** | If you need to access a BigQuery partition, explicitly include an alias for the built in partition column in your select clause, such as `select *, _PARTITIONTIME as pt from projectId.datasetId.tableId`. |
| [Derived Fields (Row-Level Expressions)](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932839148813-Maintain-Derived-Fields) | **Y** |  |
| [Distinct Counts](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932867905037-Distinct-Counts) | **Y** |  |
| [Fast Distinct Values](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715069197-Fast-Distinct-Values) | N/A |  |
| [Group By Multiple Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715164173-Group-By-Multiple-Fields) | **Y** |  |
| [Group By Time](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932690999309-Group-By-Time) | **Y** |  |
| [Group By UNIX Time](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730700429-Group-By-UNIX-Time) | **Y** |  |
| [Histogram Floating Point Values](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932708132109-Histogram-Floating-Point-Values) | **Y** |  |
| [Histograms](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933212496141-Bars-Histograms) | **Y** |  |
| [Kerberos Authentication](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933139627149-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **N** |  |
| [Last Value](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730888205-Last-Value) | **Y** |  |
| [Live Mode and Playback](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933163012621-Live-Mode-and-Historical-Playback) | **Y** |  |
| [Multivalued Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715662093-Multivalued-Fields) | N/A |  |
| [Nested Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932861225357-Support-of-Nested-Data-Structures-in-Composer) | N/A |  |
| [Partitions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932715778445-Partitions) | **N** |  |
| [Pushdown Joins for Fusion Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932963077133-Optimize-Joins) | **Y** |  |
| [Schemas](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932691729805-Schemas) | **Y** |  |
| [Text Search](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932739827853-Text-Search) | N/A |  |
| [TLS](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932692004749-TLS) | **Y** |  |
| [User Delegation](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932742695053-Enable-User-Delegation) | **Y** | The Composer Oracle connector supports user delegation only via user credential pass-through. |
| [Wildcard Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932977272717-Apply-Wildcard-Filters-to-a-Visual-Filter-Snippet-or-Dashboard) | **Y** |  |
| [Wildcard Filters, Case-Insensitive Mode](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932723779981-Wildcard-Case-Insensitive-Filters) | **Y** |  |
| [Wildcard Filters, Case-Sensitive Mode](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932692417677-Wildcard-Case-Sensitive-Filters) | **Y** |  |

## Connect to Oracle

The Oracle connector requires a JDBC driver to be configured before you can connect to your data source. You can download the driver from the vendor's site. If you are upgrading, keep in mind you need to configure the JDBC driver- see [Upgrade Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933226897037-Upgrade-Composer) for instructions. For more information and steps, see [Add a JDBC Driver](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932998821005-Add-a-JDBC-Driver).

When setting up a connection to Oracle, provide the following.

* Specify the connection name and JDBC URL. The JDBC URL for Oracle database being connected must be:
  `jdbc:oracle:thin@//ORACLEHOST:PORT/DATABASE_NAME` or `jdbc:oracle:thin:@ORACLEHOST:PORT:SID`

  To connect to Oracle with TLS enabled, see [Connect to Oracle with TLS Enabled](#Connecti2).
* Provide the user name and password for Oracle database.
* You can use an Impersonation feature to work with Oracle data source on behalf of a proxy user. Before you begin, you must configure proxy users with the corresponding privileges in the Oracle database. To use this, select the **Impersonation Enabled** checkbox and specify the **Impersonation Username** and **Impersonation Password**.
  See [Configure Settings to Use a Proxy User](#Configur).
* If you need to use Composer's Oracle connector to access a table that uses the XML data type, complete the additional setup steps described in [Enable Access to Oracle Tables That Use the XML Data Type](#Enabling).

**Note:** 
If there are any changes in the Oracle database, you must clear the Composer cache. See [How Composer Caches Data](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932848587917-How-Composer-Caches-Data).

## Connect to Oracle with TLS Enabled

Before you attempt to connect to Oracle with TLS enabled, make sure you have first installed Java Cryptography Extension (JCE). See <https://www.oracle.com/java/technologies/javase-jce8-downloads.html>.

**Connect to Oracle with TLS enabled**

1. Create a JDBC URL with TLS parameters. To specify TLS-related parameters, use the following template for a JDBC URL:

   jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=<oracle\_host>)
   (PORT=<oracle\_tls\_port))CONNECT\_DATA=(SID=<service\_id>)))

   where:

   * `<oracle_host>` is the host of the Oracle database.
   * `<oracle_tls_port>` is the port of the Oracle database with TLS enabled
   * `<service_id>` is the Oracle service ID or database to which you want to connect

   Make sure your JDBC URL uses the correct protocol. For a TLS connection, you should use `tcps`.
2. If your Oracle database is configured with a custom certificate, you should configure a truststore for the Oracle connector, as described in the following steps:

   1. Copy a truststore to the machine on which Composer's Oracle connector is running.
   2. Add the following lines to file `edc-oracle.jvm`.

      -Djavax.net.ssl.trustStore=<path\_to\_truststore>
      -Djavax.net.ssl.trustStorePassword=<truststore\_password>

      * Linux: Copy the file `edc-oracle.jvm` from the `/opt/zoomdata/conf` directory if a copy is not in `/etc/zoomdata/`.
      * Windows: Copy the file `edc-oracle.jvm` from the `<install-path>/conf` directory if a copy is not in `<install-path>/conf-modify`.

      where:

      * `<path_to_truststore>` is the absolute path to your truststore
      * `<truststore_password>` is the password for your truststore
3. Restart the Oracle connector microservice, `zoomdata-edc-oracle`. See  [Restart Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Restart).

## Configure Settings to Use a Proxy User

To enable a Composer user work as a proxy user, specify the user attributes of corresponding oracle user (that will be used as proxy user) in the account details of a Composer user.

You must specify the user attributes for each Composer user that will access the Oracle data source as a proxy user.

Perform the following steps:

1. Select Settings and then select
   **Users and Groups**.
2. Select a user from the list and select the
   **Custom Attributes** tab.
3. Select
   **Add Custom Attribute**. Specify credentials for a user as follows:

* Key - specify the login attribute for proxy user. Corresponding reference name is listed in the
  **Usage** column. You have to specify the value from the
  **Usage** column in the
  **Impersonation****Username** field while creating a connection.
* Value - specify the actual name of the oracle user, that you want to use as proxy user.
* Select the checkbox in the
  **Secure** column to encrypt the value of the key.

4. If the proxy user requires a password, select **Add Custom Attribute** and specify the key and value for the password. You have to specify the reference name from the **Usage** column in the **Impersonation Password** field while creating the connection.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167406379533)

## Enable Access to Oracle Tables That Use the XML Data Type

Before you enable access to Oracle tables that use the XML data type, be sure you have set up the Oracle JDBC driver. See [Add a JDBC Driver](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932998821005-Add-a-JDBC-Driver).

**Enable access to Oracle tables that use the XML data type**

1. Download the `xdb6.jar` and `xmlparserv2.jar` files from Oracle to the corresponding Composer instance. You can download obtain `xdb6.jar` by downloading it from <https://www.oracle.com/database/technologies/jdbc-ucp-122-downloads.html>. You can obtain `xmlparserve2.jar` by extracting it from the `lib` directory in the Oracle XML Developers Kit, which can be downloaded from <https://www.oracle.com/downloads/>.

   Place these files in the following folder:

   * Linux: `/opt/zoomdata/lib/edc-oracle/`
   * Windows: `<install-path>/lib/edc-oracle/`

   **Note:** 
   Note that this is the same folder where you downloaded the Oracle JDBC driver (see [Add a JDBC Driver](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932998821005-Add-a-JDBC-Driver)).
2. Add the following lines to the connector JVM file:

   -Djavax.xml.parsers.DocumentBuilderFactory=org.apache.xerces.jaxp.DocumentBuilderFactoryImpl
   -Djavax.xml.transform.TransformerFactory=com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl

   * Linux: `/etc/zoomdata/edc-oracle.jvm`
   * Windows: `<install-path>/conf-modify/`
3. Restart the Oracle connector microservice, `zoomdata-edc-oracle`. See  [Restart Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Restart).
