---
title: "Connect Composer to Data Stores"
id: 4405850922903
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850922903-Connect-Composer-to-Data-Stores
updated_at: 2021-09-21T01:27:12Z
---

# Connect Composer to Data Stores

# Connect Composer to Data Stores

Using connectors, Composer can connect to a wide array of data stores—from modern databases such as Hadoop, Search, Streaming, and NoSQL, to traditional sources like SQL-based stores. By default, your environment comes preconfigured with certain connectors enabled. However, additional connectors are available. If the connector you are looking for is not shown, it may be because:

* The connector is installed but is not enabled. For more information, see [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers).
* The connector was not installed and needs to be downloaded separately. For more information, see [*Obtain Additional Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405850923799-Obtain-Additional-Connector-Servers).
* The connector requires you to provide a licensed JDBC driver. For more information, see [*Add a JDBC Driver*](https://devnet.logianalytics.com/hc/en-us/articles/4405859376919-Add-a-JDBC-Driver).

Certain connectors require a JDBC driver, which is obtained through a separate download. This allows you to select and add a driver that meets your operation needs or policies. The following connectors require a JDBC driver to be installed before configuring and connecting can occur: [Amazon Redshift](https://devnet.logianalytics.com/hc/en-us/articles/4405859198103-Manage-the-Amazon-Redshift-Connector), [MemSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405859228567-Manage-the-MemSQL-Connector), [MySQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850958487-Manage-the-MySQL-Connector), [Oracle](https://devnet.logianalytics.com/hc/en-us/articles/4405850959383-Manage-the-Oracle-Connector), SAP IQ, and [Teradata](https://devnet.logianalytics.com/hc/en-us/articles/4405859235607-Manage-the-Teradata-Connector).

To connect to a data store and use its data in a Composer visual, you must first verify that a connector and its connector server have been defined in Composer for the data store. See [*Manage Connectors and Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers). Then you must define a data store connection and a data source configuration that uses the connection. The data store connection can be defined while you are setting up the data source configuration. See [*Manage Data Store Connections*](https://devnet.logianalytics.com/hc/en-us/articles/4405850909079-Manage-Data-Store-Connections) and [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4405851027479-Manage-Data-Source-Configurations) for more information.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Composer supports only underscores and dashes in data store field names. No other special characters or white space are supported. If your data store uses special characters other than underscores and dashes in field names, please remove them before attempting to create a data source configuration.

For information about what versions of data stores are supported by the Composer connectors, see [*Composer Data Connector Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405859436055-Composer-Data-Connector-Reference). For information about which features are supported by different connectors, see [*Connector Feature Support*](https://devnet.logianalytics.com/hc/en-us/articles/4405859170583-Connector-Feature-Support).
