> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage the Dundas BI (Managed) Connector

You can use the Dundas BI Connector to [connect to any data source used in that environment](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#connect-to-a-dundas-bi-data-store), or to connect to a data cube or other warehoused data in that environment. This feature also allows you to leverage data organized in a data cube for integration into your analytics environment.

If you are transitioning from an earlier release of Symphony, complete these steps as you work with technical support to reconnect to the data in your Dundas BI environment.

<Warning>
  You will need appropriate licensing for all relevant components to complete this procedure.
</Warning>

### Feature Support

This connector brings data into your environment for analytics use. Supported features will vary based on the capabilities of the primary data source.

### Register

Before you can add a connector or source, you need to register the connector server. See [Register the Dundas BI (Managed) Connection Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#register-the-dundas-bi-managed-connection-server).

### Connect

When connecting to this resource, provide the following information:

* **Connection Name**: The name of this connection, for example, **Data Cube - Sales Information**.
* **Project**: Provide the name of the project to which your data source or data cube belongs.
* **Credentials** information: Select a Credentials option from the drop-down list. This is usually `user.credentials` unless otherwise specified by your system administrator or tenant administrator.

<Warning>
  You will need to make the `IMPERSONATE_ACCOUNT` field visible.
</Warning>

### Reconnect

After establishing a connection to the appropriate project, edit each source to reconnect to your data through this connector. Edit each source, ensuring the Folder and Entity match your original configuration. See [Edit a Data Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview#edit-a-data-source).
