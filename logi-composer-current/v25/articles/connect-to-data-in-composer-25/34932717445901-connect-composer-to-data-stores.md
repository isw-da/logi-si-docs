---
title: "Connect Composer\u00a0 to Data Stores"
id: 34932717445901
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932717445901-Connect-Composer-to-Data-Stores
updated_at: 2026-05-26T22:06:27Z
---

# Connect Composer  to Data Stores

# Connect Composer  to Data Stores

Using connectors, you can connect to a wide array of data stores, from modern databases such as Hadoop, Search, Streaming, and NoSQL, to traditional sources like SQL-based stores. By default, your environment comes preconfigured with certain connectors enabled. However, additional connectors are available. If the connector you are looking for is not shown, it may be because:

* The connector is installed but is not enabled. For more information, see [Manage Connectors and Connector Servers](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932741363981-Manage-Connectors-and-Connector-Servers).
* The connector was not installed and needs to be downloaded separately. For more information, see [Obtain Additional Connector Servers](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932693640717-Obtain-Additional-Connector-Servers).
* The connector requires you to provide a licensed JDBC driver. For more information, see [Add a JDBC Driver](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932998821005-Add-a-JDBC-Driver).

Certain connectors require a JDBC driver, which is obtained through a separate download. This allows you to select and add a driver that meets your operation needs or policies.

To connect to a data store and use its data in a Composer visual, you must first verify that a connector and its connector server have been defined in Composer for the data store. See [Manage Connectors and Connector Servers](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932741363981-Manage-Connectors-and-Connector-Servers). Then you must define a data store connection and a data source configuration that uses the connection. The data store connection can be defined while you are setting up the data source configuration. See [Manage Data Store Connections](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932706697357-Manage-Data-Store-Connections) and [Manage Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932941009037-Manage-Data-Sources) for more information.

**Note:** Composer supports only underscores and dashes in data store field names. No other special characters or white space are supported. If your data store uses special characters other than underscores and dashes in field names, please remove them before attempting to create a data source configuration.

For information about what versions of data stores are supported by the Composer connectors, see [Data Connector Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933117968525-Data-Connector-Reference). For information about which features are supported by different connectors, see [Connector Feature Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932704861453-Connector-Feature-Support).
