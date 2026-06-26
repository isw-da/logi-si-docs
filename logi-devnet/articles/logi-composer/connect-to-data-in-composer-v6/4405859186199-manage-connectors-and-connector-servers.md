---
title: "Manage Connectors and Connector Servers"
id: 4405859186199
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859186199-Manage-Connectors-and-Connector-Servers
updated_at: 2021-09-21T01:27:11Z
---

# Manage Connectors and Connector Servers

# Manage Connectors and Connector Servers

Composer connects to a wide array of data sources available in the marketplace today—from modern databases (including Hadoop, Search, Streaming, and NoSQL) to traditional sources like SQL-based stores. Composer comes prepackaged with connectors that are automatically installed during the Composer installation process.

JDBC drivers for a few of the connectors are no longer included in the installation package. This means that if you use one of these connectors, you also need to configure a JDBC driver before it can be enabled and accessible from Composer. For additional details, including the list of connectors, see [*Add a JDBC Driver*](https://devnet.logianalytics.com/hc/en-us/articles/4405859376919-Add-a-JDBC-Driver).

If the connector you are looking for is not shown, it may be because:

* The connector is installed but is not enabled. For more information, see [*Enable and Disable Connectors*](https://devnet.logianalytics.com/hc/en-us/articles/4405850919959-Enable-and-Disable-Connectors).
* The connector was not installed and needs to be downloaded separately. For more information, see [*Obtain Additional Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405850923799-Obtain-Additional-Connector-Servers).
* The connector requires you to provide a licensed JDBC driver. For more information, see [*Add a JDBC Driver*](https://devnet.logianalytics.com/hc/en-us/articles/4405859376919-Add-a-JDBC-Driver).

See [*Composer Data Connector Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405859436055-Composer-Data-Connector-Reference) for the full list of supported Composer connectors.

Management of connector microservices is split into two sections:

* Connector Servers
* Connectors

Each connector server runs independently in the Composer environment. You can set up a connection type for each connector server and manage the ones to be available to users in the Composer account.

This means that you are able to enable or disable any of these servers at any time, depending on the data stores that you use and need to use with Composer. The following figure provides a high level concept diagram of the Composer environment.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743920919/concept-diagram_576x310.png)

The setup and management of connector servers in the Composer environment is handled on the Manage Connector Services page, which is accessible to supervisors. To make the actual connection between Composer and your data source after the connector server has been configured, log into Composer as an administrator and access the [Sources](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page) page, accessible from the
[UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu). See
[*Connect Composer to Data Stores*](https://devnet.logianalytics.com/hc/en-us/articles/4405850922903-Connect-Composer-to-Data-Stores).

The **Manage Connector Services** page (available to supervisors) lets you register or remove connector servers that are not available out-of-the-box in the Composer instance. You can also use this page to maintain, enable, and disable connector definitions based on the connector servers defined in the Composer instance. See [*Manage Connector Services Page*](https://devnet.logianalytics.com/hc/en-us/articles/4405859190167-Manage-Connector-Services-Page).

The [Connections](https://devnet.logianalytics.com/hc/en-us/articles/4405850909975-Connections-Page) page (available to administrators and users with appropriate [privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)) lets you define the connection for a connector between Composer and a data store. See [*Connect Composer to Data Stores*](https://devnet.logianalytics.com/hc/en-us/articles/4405850922903-Connect-Composer-to-Data-Stores).

See the following topics:

* [*Obtain Additional Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405850923799-Obtain-Additional-Connector-Servers)
* [*Register a New Connector Server*](https://devnet.logianalytics.com/hc/en-us/articles/4405850926999-Register-a-New-Connector-Server)
* [*Modifying a Connector Server*](https://devnet.logianalytics.com/hc/en-us/articles/4405850925847-Modifying-a-Connector-Server)
* [*Delete a Connector Server*](https://devnet.logianalytics.com/hc/en-us/articles/4405859188119-Delete-a-Connector-Server)
* [*Migrate Connectors for Other Versions*](https://devnet.logianalytics.com/hc/en-us/articles/4405850924951-Migrate-Connectors-for-Other-Versions)
* [*Define a New Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405859183255-Define-a-New-Connector)
* [*Modify a Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405850922007-Modify-a-Connector)
* [*Enable and Disable Connectors*](https://devnet.logianalytics.com/hc/en-us/articles/4405850919959-Enable-and-Disable-Connectors)
* [*Delete a Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405859184535-Delete-a-Connector)
* [*Connector Graceful Shutdown*](https://devnet.logianalytics.com/hc/en-us/articles/4405850920983-Connector-Graceful-Shutdown)
