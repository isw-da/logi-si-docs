---
title: "Manage Connectors and Connector Servers"
id: 34932741363981
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932741363981-Manage-Connectors-and-Connector-Servers
updated_at: 2026-05-26T22:10:16Z
---

# Manage Connectors and Connector Servers

# Manage Connectors and Connector Servers

Composer connects to a wide array of data sources available in the marketplace today—from modern databases (including Hadoop, Search, Streaming, and NoSQL) to traditional sources like SQL-based stores. Composer comes prepackaged with connectors that are automatically installed during the Composer installation process.

JDBC drivers for a few of the connectors are no longer included in the installation package. This means that if you use one of these connectors, you also need to configure a JDBC driver before it can be enabled and accessible from Composer. For additional details, including the list of connectors, see [Add a JDBC Driver](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932998821005-Add-a-JDBC-Driver).

If the connector you are looking for is not shown, it may be because:

* The connector is installed but is not enabled. For more information, see [Enable and Disable Connectors](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932710074509-Enable-and-Disable-Connectors).
* The connector was not installed and needs to be downloaded separately. For more information, see [Obtain Additional Connector Servers](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932693640717-Obtain-Additional-Connector-Servers).
* The connector requires you to provide a licensed JDBC driver. For more information, see [Add a JDBC Driver](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932998821005-Add-a-JDBC-Driver).

See [Data Connector Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933117968525-Data-Connector-Reference) for the full list of supported Composer connectors.

Management of connector microservices is split into two sections:

* Connector Servers
* Connectors

Each connector server runs independently in the Composer environment. You can set up a connection type for each connector server and manage the ones to be available to users in the Composer account.

This means that you are able to enable or disable any of these servers at any time, depending on the data stores that you use and need to use with Composer. The following figure provides a high level concept diagram of the Composer environment.

![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167420490381)

The setup and management of connector servers in the Composer environment is handled on the Manage Connector Services page, which is accessible to supervisors. To make the actual connection between Composer and your data source after the connector server has been configured, log into Composer as an administrator and access the [Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932895238669-Data-Sources-Page) page, accessible from the
[UI menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143886477-The-Composer-UI-Menu). See
[Connect Composer  to Data Stores](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932717445901-Connect-Composer-to-Data-Stores).

The Manage Connector Services page (available to supervisors) lets you register or remove connector servers that are not available out-of-the-box in the Composer instance. You can also use this page to maintain, enable, and disable connector definitions based on the connector servers defined in the Composer instance. See [Manage Connector Services Page](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932711365773-Manage-Connector-Services-Page).

The [Connections](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932690166541-Connections-Page) page (available to administrators and users with appropriate [privileges](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference)) lets you define the connection for a connector between Composer and a data store. See [Connect Composer  to Data Stores](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932717445901-Connect-Composer-to-Data-Stores).

**Note:** 
If you try to delete a visual, filter snippet, dashboard, dashboard link, source, or source field, Composer displays an error message naming any objects dependent on the item you’re trying to delete. You can delete the item after you’ve removed the association from the dependent object.
See[Fields Usage](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932867958541-Fields-Usage).

See the following topics:

* [Obtain Additional Connector Servers](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932693640717-Obtain-Additional-Connector-Servers)
* [Register a New Connector Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932742145165-Register-a-New-Connector-Server)
* [Modifying a Connector Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932717801869-Modifying-a-Connector-Server)
* [Delete a Connector Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932733001741-Delete-a-Connector-Server)
* [Define a New Connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932709865869-Define-a-New-Connector)
* [Modify a Connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932732698125-Modify-a-Connector)
* [Enable and Disable Connectors](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932710074509-Enable-and-Disable-Connectors)
* [Delete a Connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932724461325-Delete-a-Connector)
* [Connector Graceful Shutdown](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932693283341-Connector-Graceful-Shutdown)
