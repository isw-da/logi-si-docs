---
title: "Manage the Dundas BI (Managed) Connector"
id: 47441922925197
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47441922925197-Manage-the-Dundas-BI-Managed-Connector
updated_at: 2026-08-31T04:12:34Z
---

# Manage the Dundas BI (Managed) Connector

# Manage the Dundas BI (Managed) Connector

You can use the Dundas BI Connector to [connect to any data source used in that environment](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054605453-Modify-Data-Store-Connections#Reconnec "connect to any data source used in that environment"), or to connect to a data cube or other warehoused data in that environment. This feature also allows you to leverage data organized in a data cube for integration into your analytics environment.

If you are transitioning from an earlier release of Symphony, complete these steps as you work with technical support to reconnect to the data in your Dundas BI environment.

**Important:** You will need appropriate licensing for all relevant components to complete this procedure.

## Feature Support

This connector brings data into your environment for analytics use. Supported features will vary based on the capabilities of the primary data source.

## Register

Before you can add a connector or source, you need to register the connector server. See [Register the Dundas BI (Managed) Connection Server](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042690957-Register-a-New-Connector-Server#Register).

## Connect

When connecting to this resource, provide the following information:

* **Connection Name**: The name of this connection, for example, **Data Cube - Sales Information**.
* **Project**: Provide the name of the project to which your data source or data cube belongs.
* **Credentials** information: Select a Credentials option from the drop-down list. This is usually `user.credentials` unless otherwise specified by your system administrator or tenant administrator.

**Important:** You will need to make the `IMPERSONATE_ACCOUNT` field visible.

## Reconnect

After establishing a connection to the appropriate project, edit each source to reconnect to your data through this connector. Edit each source, ensuring the Folder and Entity match your original configuration. See [Edit a Data Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116405261-Edit-a-Data-Source).
