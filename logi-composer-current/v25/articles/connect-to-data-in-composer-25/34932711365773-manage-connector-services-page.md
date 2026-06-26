---
title: "Manage Connector Services Page"
id: 34932711365773
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932711365773-Manage-Connector-Services-Page
updated_at: 2026-05-26T22:10:14Z
---

# Manage Connector Services Page

# Manage Connector Services Page

![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167375083021)

The Manage Connector Services page is where you register a new connector server that is not available out-of-the-box to the Composer instance. It is also where you can remove connector servers available to the instance.

This page is also where you set up and enable connectors for use in your data sources. The connectors you can define depend on which connector servers have been registered. You can also use this page to delete and disable connectors in the Composer instance.

## Connector Servers

The Connector Servers section lets the Composer admins and supervisors group users register and delete the connector servers available in the Composer environment. See [Obtain Additional Connector Servers](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932693640717-Obtain-Additional-Connector-Servers)
for information about setting up a connector server.

**Note:** 
The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.

Use the search box above the Connector Servers table to locate a connector server (for example, if your Composer environment contains a large number of connector servers).

Connector servers that you register and connect in Composer are accessible and the registration details can be edited (for example, if the server has moved or changed). Default connector servers provided by Composer are not editable.

The Connector Server table provides the following information.

| Column Title | Description |
| --- | --- |
| Connector Server Name | The name of the connector server (data store) definition. |
| Type | The type of connector server. The following types are supported:   * Discovery: uses the capability integrated into Composer to locate and set up the connector server automatically. * HTTP/Socket: if you manually add a connector server to the Composer environment, then it will be either an HTTP or a Socket type. * Core: identifies connectors that are built into the Composer server.  **Note:**    Type **Core** connectors , including flat files as well as HDFS and S3 buckets, do not require a dedicated connector server. These types of connectors are always available. This means they are always on, and do not require any additional network resources to keep them on. |
| URL/Host | The URL or host name of the connector server (data store). If more than one instance of a connector server is running, the URLs for each instance are shown, separated by commas. |
| Available | Indicates whether the connector server (data store) is available or not. |
| Delete | Provides an option to delete a connector server definition from the Composer instance. This option is not available for Core type connector servers because they are built into Composer and cannot be deleted.  You can delete a connector server that you manually configured. However, you must first delete the connection definitions for the server and the data source configurations that use the connection definitions (see [Delete a Data Source Configuration](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932908359309-Delete-a-Data-Source-Configuration) and [Delete Data Store Connections](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932662325517-Delete-Data-Store-Connections)). Then you need to delete the [connector](#Connecto) (see [Delete a Connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932724461325-Delete-a-Connector)). When the connections and the connector are all deleted, you can then delete the connector server. |

See the following topics:

* [Obtain Additional Connector Servers](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932693640717-Obtain-Additional-Connector-Servers)
* [Register a New Connector Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932742145165-Register-a-New-Connector-Server)
* [Modifying a Connector Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932717801869-Modifying-a-Connector-Server)
* [Delete a Connector Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932733001741-Delete-a-Connector-Server)

## Connectors

The Connectors section lists the connectors that are defined in the Composer environment. You can use these connectors to connect to a specific type of data store (such as Impala or Elasticsearch). You can use this section to add and remove connectors and to enable and disable them. A connector that is listed in this table and is enabled is visible on the [Connections](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932690166541-Connections-Page) page in the UI (when you are logged in as a non-supervisory user or administrator and have been assigned appropriate [privileges](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference)).

The Connectors table provides the following information.

| Column Title | Description |
| --- | --- |
| Connector | The name of the connector definition. |
| Connector Server Name | The name of the connector server (data store) associated with the connector. If the connector server is a Core-type connector, the connector server name shows as **Internal**. |
| Description | An optional description of the connector. You can provide this description when you add a connector definition. |
| Enabled | A switch that enables or disables the connector definition in the Composer instance. An enabled connector is visible on the [Connections](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932690166541-Connections-Page) page; a disabled connector is not. |
| Delete | Provides an option to delete the connector definition from the Composer instance. This option is not available for Internal connectors (Core type connector servers) because they are built into Composer and cannot be deleted.  You can delete a connector that you manually configured. However, you must first delete the connection definitions for the server and the data source configurations that use the connection definitions. See [Delete a Data Source Configuration](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932908359309-Delete-a-Data-Source-Configuration) and [Delete Data Store Connections](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932662325517-Delete-Data-Store-Connections). |

See the following topics:

* [Define a New Connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932709865869-Define-a-New-Connector)
* [Modify a Connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932732698125-Modify-a-Connector)
* [Delete a Connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932724461325-Delete-a-Connector)
* [Enable and Disable Connectors](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932710074509-Enable-and-Disable-Connectors)
