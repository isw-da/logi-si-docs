---
title: "Add  Data Store Connections"
id: 43700992503437
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992503437-Add-Data-Store-Connections
updated_at: 2026-08-26T07:11:35Z
---

# Add  Data Store Connections

# Add Data Store Connections

You can add and validate data store connections on the [Connections page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008155149-Connections-Page) in the UI for connector servers that [are registered](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042690957-Register-a-New-Connector-Server) in your environment.

**Note:** 
You must be logged in as a user with the [group privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) **Manage Connections** to maintain data store connection definitions.

## Add and Validate a Connection

1. Log in as a user with the [group privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) **Manage Connections**.
2. Select the **Connection** card on your home page or **Connections** from the main menu. The [Connections work area](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008155149-Connections-Page) appears.

   The Connections page lists the data store connections you have defined, identifies the number of associated data sources, and other overview information about your existing connections.
3. Select **Create Connection** in the upper right corner of the connection list. The Select a Connection Type dialog appears.
4. Select the connection type you want to use for the connection definition. The Add <type> Connection page appears.
5. Optionally, change the default name for the connection in the **Connection Name** field.
6. The connection details required to connect to a data store vary by data store. Use the fields in Connection Details to specify the URL and other connection details and, if applicable, authentication credentials (**User Name** and **Password** fields) required to connect to the data store. Fields highlighted in red are required. Any connection requirements for a specific data store are described in the connector documentation for that data store. See the [Data Connector Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113495693-Data-Connector-Reference).

   You can insert variables for connection parameters, if you have defined any custom attributes in your environment. See [Insert Variables for Connection Parameters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993364749-Insert-Variables-for-Connection-Parameters). Additionally, you can select any user attributes you have defined for connection parameters using the up and down arrows in the connection parameter section. See [Use User Attributes for Connection Parameters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042127373-Use-User-Attributes-for-Connection-Parameters).
7. If the **Do As User** option is available, optionally specify the custom user attributes you set up to enable user delegation. See [Apply User Delegation to a Connection](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039356557-Apply-User-Delegation-to-a-Connection).
8. This is an optional step.

   Each data source configuration specifies refresh settings for the data from the data store. If a data store connection requires special credentials to refresh the data source data, select the **Add an Override** button under **Scheduler Overrides** and select an override setting to use. The override settings you can specify mirror the regular data store connection settings (except for the connection definition name) and vary based on the type of data store connector used for the connection. See [Data Connector Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113495693-Data-Connector-Reference).

   More than one override setting can be specified. Simply select the **Add an Override** button again and select a different setting and provide its input value. Repeat this process until all override settings required by the data store have been specified.
9. Select **Validate** to validate the connection. If the connection is valid, you can save the connection. If invalid, make changes, then select **Validate** again.
10. Select **Save** to save the connection.

After you create a connection, you can update the Connection Details or view Data Sources associated with this connection at any time. See [Modify Data Store Connections](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054605453-Modify-Data-Store-Connections).

### **Add and Validate a Connection to a Dundas BI Data Source or Data Cube**

You can use the Dundas BI Connector to [connect to any data source used in that environment](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054605453-Modify-Data-Store-Connections#Reconnec "connect to any data source used in that environment"), or to connect to a data cube or other warehoused data in that environment. This feature also allows you to leverage data organized in a data cube for integration into your analytics environment.

1. Log in as a user with the [group privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) **Manage Connections**.
2. Select **Connections** from the main menu. The Connections work area opens.

   The Connections page lists the data store connections you have defined, identifies the number of associated data sources, and other overview information about your existing connections.
3. Select **Create Connection** in the upper right corner of the connection list. The **Select a Connection Type** dialog appears.
4. Select **Managed** from the available connection types. An **Add Managed Connection** work area opens.
5. Enter a **Connection Name**, and the name of the **Project** to which the data source or data cube you want to use belongs.
6. Select a **Credentials** option from the drop-down list, usually `User.credentials`, unless otherwise specified by your system administrator or tenant administrator. Make the `IMPERSONATE_ACCOUNT` field visible.
7. Select **Validate** to validate the connection. If the connection is valid, you can save the connection. If invalid, make changes, then select **Validate** again.
8. Select **Save** to save the validated connection.

After you create a connection, you can update the Connection Details or view Data Sources associated with this connection at any time. See [Modify Data Store Connections](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054605453-Modify-Data-Store-Connections).
