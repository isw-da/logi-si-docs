---
title: "Add  Data Store Connections"
id: 34932713955597
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932713955597-Add-Data-Store-Connections
updated_at: 2026-05-26T22:10:18Z
---

# Add  Data Store Connections

# Add Data Store Connections

You can add and validate data store connections on the [Connections page](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932690166541-Connections-Page) in the UI.

**Note:** 
You must be logged in as a user with the [group privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) **Manage Connections** to maintain data store connection definitions.

**Add and validate a connection**

1. Log in as a user with the [group privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) **Manage Connections**.
2. Select **Connections** on the [top-level navigation banner](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933120256397-The-Top-Level-Navigation-Banner), the [UI menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143886477-The-Composer-UI-Menu) (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167965186829)), or select the **Connections** option on the [Home page](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933063528717-Home-Page). The [Connections page](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932690166541-Connections-Page) appears.

   The Connections page lists the data store connections you have defined, identifies the number of associated data sources, and other overview information about your existing connections.
3. Select **Create Connection** in the upper right corner of the connection list. The Select a Connection Type dialog appears.
4. Select the connection type you want to use for the connection definition. The Add <type> Connection page appears.
5. Optionally, change the default name for the connection in the **Connection Name** field.
6. The connection details required to connect to a data store vary by data store. Use the fields in Connection Details to specify the URL and other connection details and, if applicable, authentication credentials (**User Name** and **Password** fields) required to connect to the data store. Fields highlighted in red are required. Any connection requirements for a specific data store are described in the connector documentation for that data store. See the [Data Connector Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933117968525-Data-Connector-Reference).

   You can insert variables for connection parameters, if you have defined any custom attributes in your environment. See [Insert Variables for Connection Parameters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932732148493-Insert-Variables-for-Connection-Parameters). Additionally, you can select any user attributes you have defined for connection parameters using the up and down arrows in the connection parameter section. See [Use User Attributes for Connection Parameters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932716668301-Use-User-Attributes-for-Connection-Parameters).
7. If the **Do As User** option is available, optionally specify the custom user attributes you set up to enable user delegation. See [Apply User Delegation to a Connection](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932694331917-Apply-User-Delegation-to-a-Connection).
8. This is an optional step.

   Each data source configuration specifies refresh settings for the data from the data store. If a data store connection requires special credentials to refresh the data source data, select the **Add an Override** button under **Scheduler Overrides** and select an override setting to use. The override settings you can specify mirror the regular data store connection settings (except for the connection definition name) and vary based on the type of data store connector used for the connection. See [Data Connector Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933117968525-Data-Connector-Reference).

   More than one override setting can be specified. Simply select the **Add an Override** button again and select a different setting and provide its input value. Repeat this process until all override settings required by the data store have been specified.
9. Select **Validate** to validate the connection. If the connection is valid, you can save the connection. If invalid, make changes, then select **Validate** again.
10. Select **Save** to save the connection.

After you create a connection, you can update the Connection Details or view Data Sources associated with this connection at any time. See [Modify Data Store Connections](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932714462221-Modify-Data-Store-Connections).
