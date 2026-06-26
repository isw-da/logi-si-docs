---
title: "Manage Connector Services Page"
id: 4405859190167
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859190167-Manage-Connector-Services-Page
updated_at: 2021-09-21T01:27:15Z
---

# Manage Connector Services Page

# Manage Connector Services Page

![](https://devnet.logianalytics.com/hc/article_attachments/4406743919127/connector-services_576x268.png)

The Manage Connector Services page is where you register a new connector server that is not available out-of-the-box to the Composer instance. It is also where you can remove connector servers available to the instance.

This page is also where you set up and enable connectors for use in your data sources. The connectors you can define depend on which connector servers have been registered. You can also use this page to delete and disable connectors in the Composer instance.

The Manage Connector Services page is split into two sections:

* [*Connector Servers*](#Connecto2)
* [*Connectors*](#Connecto)

## Connector Servers

The Connector Servers section lets the Composer supervisor register and delete the connector servers available in the Composer environment. See [*Obtain Additional Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405850923799-Obtain-Additional-Connector-Servers)
for information about setting up a connector server.

Use the search box above the Connector Servers table to locate a connector server (for example, if your Composer environment contains a large number of connector servers).

Connector servers that you register and connect in Composer are accessible and the registration details can be edited (for example, if the server has moved or changed). Default connector servers provided by Composer are not editable.

The Connector Server table provides the following information.

| Column Title | Description |
| --- | --- |
| Connector Server Name | The name of the connector server (data store) definition. |
| Type | The type of connector server. The following types are supported:   * Discovery: uses the capability integrated into Composer to locate and set up the connector server automatically. * HTTP/Socket: if you manually add a connector server to the Composer environment, then it will be either an HTTP or a Socket type. * Core: identifies connectors that are built into the Composer server.  Type **Core** connectors , including flat files as well as HDFS and S3 buckets, do not require a dedicated connector server. These types of connectors are always available. This means they are always on, and do not require any additional network resources to keep them on. |
| URL/Host | The URL or host name of the connector server (data store). If more than one instance of a connector server is running, the URLs for each instance are shown, separated by commas. |
| Available | Indicates whether the connector server (data store) is available or not. |
| Delete | Provides an option to delete a connector server definition from the Composer instance. This option is not available for Core type connector servers because they are built into Composer and cannot be deleted.  You can delete a connector server that you manually configured. However, you must first delete the connection definitions for the server and the data source configurations that use the connection definitions (see [*Delete a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405859314967-Delete-a-Data-Source-Configuration) and [*Delete Data Store Connections*](https://devnet.logianalytics.com/hc/en-us/articles/4405859166359-Delete-Data-Store-Connections)). Then you need to delete the [connector](#Connecto) (see [*Delete a Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405859184535-Delete-a-Connector)). When the connections and the connector are all deleted, you can then delete the connector server. |

See the following sections:

* [*Obtain Additional Connector Servers*](https://devnet.logianalytics.com/hc/en-us/articles/4405850923799-Obtain-Additional-Connector-Servers)
* [*Register a New Connector Server*](https://devnet.logianalytics.com/hc/en-us/articles/4405850926999-Register-a-New-Connector-Server)
* [*Modifying a Connector Server*](https://devnet.logianalytics.com/hc/en-us/articles/4405850925847-Modifying-a-Connector-Server)
* [*Delete a Connector Server*](https://devnet.logianalytics.com/hc/en-us/articles/4405859188119-Delete-a-Connector-Server)
* [*Migrate Connectors for Other Versions*](https://devnet.logianalytics.com/hc/en-us/articles/4405850924951-Migrate-Connectors-for-Other-Versions)

## Connectors

The Connectors section lists the connectors that are defined in the Composer environment. You can use these connectors to connect to a specific type of data store (such as Impala or Elasticsearch). You can use this section to add and remove connectors and to enable and disable them. A connector that is listed in this table and is enabled is visible on the [Connections](https://devnet.logianalytics.com/hc/en-us/articles/4405850909975-Connections-Page) page in the UI (when you are logged in as a non-supervisory user or administrator and have been assigned appropriate [privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)).

The Connectors table provides the following information.

| Column Title | Description |
| --- | --- |
| Connector | The name of the connector definition. |
| Connector Server Name | The name of the connector server (data store) associated with the connector. If the connector server is a Core-type connector, the connector server name shows as **Internal**. |
| Description | An optional description of the connector. You can provide this description when you add a connector definition. |
| Enabled | A switch that enables or disables the connector definition in the Composer instance. An enabled connector is visible on the [Connections](https://devnet.logianalytics.com/hc/en-us/articles/4405850909975-Connections-Page) page; a disabled connector is not. |
| Delete | Provides an option to delete the connector definition from the Composer instance. This option is not available for Internal connectors (Core type connector servers) because they are built into Composer and cannot be deleted.  You can delete a connector that you manually configured. However, you must first delete the connection definitions for the server and the data source configurations that use the connection definitions. See [*Delete a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405859314967-Delete-a-Data-Source-Configuration) and [*Delete Data Store Connections*](https://devnet.logianalytics.com/hc/en-us/articles/4405859166359-Delete-Data-Store-Connections). |

See the following sections:

* [*Define a New Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405859183255-Define-a-New-Connector)
* [*Modify a Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405850922007-Modify-a-Connector)
* [*Delete a Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405859184535-Delete-a-Connector)
* [*Enable and Disable Connectors*](https://devnet.logianalytics.com/hc/en-us/articles/4405850919959-Enable-and-Disable-Connectors)
