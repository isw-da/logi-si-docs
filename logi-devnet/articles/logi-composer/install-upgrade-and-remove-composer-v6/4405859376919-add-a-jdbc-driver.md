---
title: "Add a JDBC Driver"
id: 4405859376919
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859376919-Add-a-JDBC-Driver
updated_at: 2021-10-21T23:03:28Z
---

# Add a JDBC Driver

# Add a JDBC Driver

For certain data sources, the JDBC drivers needed are no longer included in the installation package of Composer. You need to provide your own JDBC driver for the following data sources:

* [Amazon Redshift](https://devnet.logianalytics.com/hc/en-us/articles/4405859198103-Manage-the-Amazon-Redshift-Connector)
* [Dremio](https://devnet.logianalytics.com/hc/en-us/articles/4405859221911-Manage-the-Dremio-Connector)
* [MemSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405859228567-Manage-the-MemSQL-Connector)
* [MySQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850958487-Manage-the-MySQL-Connector)
* [Oracle](https://devnet.logianalytics.com/hc/en-us/articles/4405850959383-Manage-the-Oracle-Connector)
* [SAP Hana](https://devnet.logianalytics.com/hc/en-us/articles/4405859232791-Manage-the-SAP-Hana-Connector)
* [SAP IQ](https://devnet.logianalytics.com/hc/en-us/articles/4405850963095-Manage-the-SAP-IQ-Connector)
* [Snowflake](https://devnet.logianalytics.com/hc/en-us/articles/4405859234199-Manage-the-Snowflake-Connector)
* [Teradata](https://devnet.logianalytics.com/hc/en-us/articles/4405859235607-Manage-the-Teradata-Connector)
* [Vertica](https://devnet.logianalytics.com/hc/en-us/articles/4405850966679-Manage-the-Vertica-Connector)

The following Composer connectors are distributed with a JDBC driver, but you can download and install newer versions using the information in this topic: [Snowflake](https://devnet.logianalytics.com/hc/en-us/articles/4405859234199-Manage-the-Snowflake-Connector).

This approach allows you the flexibility to add a specific JDBC driver that meets your licensing, support policies or operational needs. As a result, in order to connect to and visualize data from Composer, you first need to download and install a JDBC driver.

## Caveats

If the JDBC driver for the Composer connector is not configured, the connector server will not start and the connector cannot be enabled within Composer. See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers).

## Install a JDBC Driver

To use any of the connectors listed above, perform the following steps to install the required JDBC driver after successful installation of Composer microservices:

1. Download the required driver from the vendor’s site to the corresponding Composer instance. Place the required driver in the following folder: `/usr/local/share/java/zoomdata`.

   If this folder does not exist, you need to create it in the location mentioned above. See the following table for resources for vendor’s JDBC drivers. Make sure that the Composer administrator has read-level access rights to the JDBC driver (JAR) file.

   | Connector | Link to JDBC Driver | License Type | Supported Version |
   | --- | --- | --- | --- |
   | Amazon Redshift | [http://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html#download-jdbc-driver](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html#download-jdbc-driver) | Commercial | 1.2.16.1027 |
   | Dremio | <https://www.dremio.com/drivers/> | LGPL | 4.1 |
   | MemSQL | <https://dev.mysql.com/downloads/connector/j/> | LGPL | 8.0.13 |
   | MySQL | <https://dev.mysql.com/downloads/connector/j/> | LGPL | 8.0.13 |
   | Oracle | <https://www.oracle.com/database/technologies/appdev/jdbc-ucp-183-downloads.html> | Commercial | 18.3.0.0 |
   | SAP Hana | <https://developers.sap.com/trials-downloads.html> | Commercial | 2.0 |
   | SAP IQ | <https://www.sap.com/index.html> | Commercial | 16 |
   | Snowflake | <https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc/> | LGPL |  |
   | Teradata | <https://downloads.teradata.com/download/connectivity/jdbc-driver> | Commercial | 15.00.00.30 |
   | Vertica | <https://www.vertica.com/client-drivers/> | Commercial | All |
2. Use the following command to access and open the property file:

   ```
   vi /etc/zoomdata/edc-<connector_name>.properties
   ```

   If you are not logged in as a root user, enter `sudo vi /etc/zoomdata/edc-<connector_name>.properties` to create the desired file. If the properties file does not exist, this command creates it.

   Replace `<connector_name>` with the name of the connector you are configuring:

   | Connector | Connector Property File Name |
   | --- | --- |
   | Amazon Redshift | edc-redshift.properties |
   | MemSQL | edc-memsql.properties |
   | Microsoft SQL Server | edc-mssql.properties |
   | MySQL | edc-mysql.properties |
   | Oracle | edc-oracle.properties |
   | SAP Hana | edc-saphana.properties |
   | SAP IQ | edc-sapiq.properties |
   | Snowflake | edc-snowflake.properties |
   | Teradata | edc-teradata.properties |
   | Vertica | edc-vertica.properties |
3. In the edc-<connector\_name>.properties file, add the following property:

   ```
   datasource.driver-config.jar-path=<JDBC_driver_filepath>
   ```

   If you need to add multiple paths, use a comma-separated list:

   ```
   datasource.driver-config.jar-path=<JDBC_driver_filepath1>,<JDBC_driver_filepath2>
   ```
4. For [MemSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405859228567-Manage-the-MemSQL-Connector) and [MySQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850958487-Manage-the-MySQL-Connector) connectors, add the following property to the property files:

   ```
   datasource.driver-config.class-name=com.mysql.cj.jdbc.Driver
   ```
5. Save your changes to the properties file.
6. Restart the corresponding connector by running the appropriate command:

   * For CentOS 7 or 8 and Ubuntu 16 or 18: `systemctl restart zoomdata-edc-<connector_name>`
7. Log in as the supervisor, access the Connectors page, and verify that the connector is enabled so it appears in the data source list. After the JDBC driver has been configured and the connector has been enabled, users with the correct access privileges can use the connector to connect to the data store in a [data source configuration](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations).
