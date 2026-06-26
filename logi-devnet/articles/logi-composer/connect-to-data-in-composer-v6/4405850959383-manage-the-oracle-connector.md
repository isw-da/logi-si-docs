---
title: "Manage the Oracle Connector"
id: 4405850959383
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850959383-Manage-the-Oracle-Connector
updated_at: 2021-09-21T01:27:29Z
---

# Manage the Oracle Connector

# Manage the Oracle Connector

The Composer Oracle connector lets you access the data available in Oracle databases using the Composer client. The Composer Oracle connector supports Oracle versions 11.2 - 18.3.

Before you can establish a connection from Composer to Oracle storage, a connector server needs to be installed and configured.
See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers) for general instructions and [*Connect to Oracle*](#Connecti) for details specific to the Oracle connector.

After the connector has been set up, you can create data source configurations that specify the necessary connection information and identify the data you want to use. See [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) for more information. After data sources are configured, they can be used to create dashboards and visuals from your data. See [*Create Dashboards*](https://devnet.logianalytics.com/hc/en-us/articles/4405859261207-Create-Dashboards).

## Composer Feature Support

Oracle connector support for specific [Composer features](https://devnet.logianalytics.com/hc/en-us/articles/4405859170583-Connector-Feature-Support) is shown in the following table.

**Key:** **Y** - Supported; **N** - Not Supported; N/A - not applicable

| Feature | Supported? | | | Notes |
| --- | --- | --- | --- | --- |
| [Admin-Defined Functions](https://devnet.logianalytics.com/hc/en-us/articles/4405850995991-Admin-Defined-Functions) | **Y** | | |  |
| [Box Plots](https://devnet.logianalytics.com/hc/en-us/articles/4405859517207-Box-Plots) | **Y** | | |  |
| [Custom SQL Queries](https://devnet.logianalytics.com/hc/en-us/articles/4405859171735-Custom-SQL-Queries) | **Y** | | |  |
| [Derived Fields (Row-Level Expressions)](https://devnet.logianalytics.com/hc/en-us/articles/4405859299479-Maintain-Derived-Fields) | **Y** | | |  |
| [Distinct Counts](https://devnet.logianalytics.com/hc/en-us/articles/4405859300503-Enable-Distinct-Counts) | **Y** | | |  |
| [Fast Distinct Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850912279-Fast-Distinct-Values) | N/A | | |  |
| [Group By Multiple Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405850913303-Group-By-Multiple-Fields) | **Y** | | |  |
| [Group By Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850914199-Group-By-Time) | **Y** | | |  |
| [Group By UNIX Time](https://devnet.logianalytics.com/hc/en-us/articles/4405850915095-Group-By-UNIX-Time) | **Y** | | |  |
| [Histogram Floating Point Values](https://devnet.logianalytics.com/hc/en-us/articles/4405850915991-Histogram-Floating-Point-Values) | **Y** | | |  |
| [Histograms](https://devnet.logianalytics.com/hc/en-us/articles/4405859514775-Bars-Histograms) | **Y** | | |  |
| [Kerberos Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4405859461271-Configure-Kerberos-Single-Sign-On-SSO-Settings) | **N** | | |  |
| [Last Value](https://devnet.logianalytics.com/hc/en-us/articles/4405859174295-Last-Value) | **Y** | | |  |
| [Live Mode and Playback](https://devnet.logianalytics.com/hc/en-us/articles/4405851191447-Live-Mode-and-Historical-Playback) | **Y** | | |  |
| [Multivalued Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405859175319-Multivalued-Fields) | N/A | | |  |
| [Nested Fields](https://devnet.logianalytics.com/hc/en-us/articles/4405851022871-Support-of-Nested-Data-Structures-in-Composer) | N/A | | |  |
| [Partitions](https://devnet.logianalytics.com/hc/en-us/articles/4405859176343-Partitions) | **N** | | |  |
| [Pushdown Joins for Fusion Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405859358487-Optimize-Joins) | **Y** | | |  |
| [Schemas](https://devnet.logianalytics.com/hc/en-us/articles/4405859177367-Schemas) | **Y** | | |  |
| [Text Search](https://devnet.logianalytics.com/hc/en-us/articles/4405859178391-Text-Search) | N/A | | |  |
| [TLS](https://devnet.logianalytics.com/hc/en-us/articles/4405859179671-TLS) | **Y** | | |  |
| [User Delegation](https://devnet.logianalytics.com/hc/en-us/articles/4405859193111-Enable-User-Delegation) | **Y** | | | The Composer Oracle connector supports user delegation only via user credential pass-through. |
| [Wild Card Filters](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | | |  |
| [Wild Card Filters, Case-Insensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | | |  |
| [Wild Card Filters, Case-Sensitive Mode](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard) | **Y** | | |  |

## Connect to Oracle

The Oracle connector requires a JDBC driver to be configured before you can connect to your data source. You can download the driver from the vendor's site. If you are upgrading, keep in mind you need to configure the JDBC driver- see [*Upgrade Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859509271-Upgrade-Composer) for instructions. For more information and steps, see [*Add a JDBC Driver*](https://devnet.logianalytics.com/hc/en-us/articles/4405859376919-Add-a-JDBC-Driver).

When setting up a connection to Oracle, provide the following.

* Specify the connection name and JDBC URL. The JDBC URL for Oracle database being connected must be:
  `jdbc:oracle:thin@//ORACLEHOST:PORT/DATABASE_NAME` or `jdbc:oracle:thin:@ORACLEHOST:PORT:SID`

  To connect to Oracle with TLS enabled, see [*Connect to Oracle with TLS Enabled*](#Connecti2).
* Provide the user name and password for Oracle database.
* You can use an Impersonation feature to work with Oracle data source on behalf of a proxy user. Before you begin, you must configure proxy users with the corresponding privileges in the Oracle database. To use this, select the **Impersonation Enabled** checkbox and specify the **Impersonation Username** and **Impersonation Password**.
  See [*Configure Settings to Use a Proxy User*](#Configur).
* If you need to use Composer's Oracle connector to access a table that uses the XML data type, complete the additional setup steps described in [*Enable Access to Oracle Tables That Use the XML Data Type*](#Enabling).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If there are any changes in the Oracle database, you must clear the Composer cache. See [*How Composer Caches Data*](https://devnet.logianalytics.com/hc/en-us/articles/4405859286935-How-Composer-Caches-Data).

## Connect to Oracle with TLS Enabled

Before you attempt to connect to Oracle with TLS enabled, make sure you have first installed Java Cryptography Extension (JCE). See <https://www.oracle.com/java/technologies/javase-jce8-downloads.html>.

To connect to Oracle with TLS enabled:

1. Create a JDBC URL with TLS parameters. To specify TLS-related parameters, use the following template for a JDBC URL:

   ```
   jdbc:oracle:thin:@(DESCRIPTION=(ADDRESS=(PROTOCOL=tcps)(HOST=<oracle_host>)
   (PORT=<oracle_tls_port))CONNECT_DATA=(SID=<service_id>)))
   ```

   where:

   * `<oracle_host>` is the host of the Oracle database.
   * `<oracle_tls_port>` is the port of the Oracle database with TLS enabled
   * `<service_id>` is the Oracle service ID or database to which you want to connect

   Make sure your JDBC URL uses the correct protocol. For a TLS connection, you should use `tcps`.
2. If your Oracle database is configured with a custom certificate, you should configure a truststore for the Oracle connector, as described in the following steps:

   1. Copy a truststore to the machine on which Composer's Oracle connector is running.
   2. Add the following lines to file `/etc/zoomdata/edc-oracle.jvm`. Copy the file `edc-oracle.jvm` from the `/opt/zoomdata/conf` directory if a copy is not in `/etc/zoomdata/`.

      ```
      -Djavax.net.ssl.trustStore=<path_to_truststore>
        
      -Djavax.net.ssl.trustStorePassword=<truststore_password>
      ```

      where:

      * `<path_to_truststore>` is the absolute path to your truststore
      * `<truststore_password>` is the password for your truststore
3. Restart the Oracle connector microservice, `zoomdata-edc-oracle`. See [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).

## Configure Settings to Use a Proxy User

To enable a Composer user work as a proxy user, specify the user attributes of corresponding oracle user (that will be used as proxy user) in the account details of a Composer user.

You must specify the user attributes for each Composer user that will access the Oracle data source as a proxy user.

Perform the following steps:

1. Select Settings and then select
   **Users & Groups**.
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

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747447191/custom-attribute_400x279.png)

## Enable Access to Oracle Tables That Use the XML Data Type

Before you enable access to Oracle tables that use the XML data type, be sure you have set up the Oracle JDBC driver. See [*Add a JDBC Driver*](https://devnet.logianalytics.com/hc/en-us/articles/4405859376919-Add-a-JDBC-Driver).

To enable access to Oracle tables that use the XML data type:

1. Download the `xdb6.jar` and `xmlparserv2.jar` files from Oracle to the corresponding Composer instance. You can download obtain `xdb6.jar` by downloading it from <https://www.oracle.com/database/technologies/jdbc-ucp-122-downloads.html>. You can obtain `xmlparserve2.jar` by extracting it from the `lib` directory in the Oracle XML Developers Kit, which can be downloaded from *<https://www.oracle.com/downloads/>*.

   Place these files in the following folder: `/usr/local/share/java/zoomdata`.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Note that this is the same folder where you downloaded the Oracle JDBC driver (see [*Add a JDBC Driver*](https://devnet.logianalytics.com/hc/en-us/articles/4405859376919-Add-a-JDBC-Driver)).
2. Add the following lines to the connector JVM file in `/etc/zoomdata/edc-oracle.jvm`:

   ```
   -Djavax.xml.parsers.DocumentBuilderFactory=org.apache.xerces.jaxp.DocumentBuilderFactoryImpl
   -Djavax.xml.transform.TransformerFactory=com.sun.org.apache.xalan.internal.xsltc.trax.TransformerFactoryImpl
   ```
3. Restart the Oracle connector microservice, `zoomdata-edc-oracle`. See [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).
