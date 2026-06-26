---
title: "Modify  Data Store Connections"
id: 43701054605453
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054605453-Modify-Data-Store-Connections
updated_at: 2026-05-29T14:11:34Z
---

# Modify  Data Store Connections

# Modify Data Store Connections

You can modify data store connections.

**Note:** 
You must be logged in as an administrator or as a user with the [group privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) **Manage Connections** to maintain data store connection definitions.

**Modify a data store connection definition:**

1. Make sure you are logged in as a user with the [group privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) **Manage Connections**.
2. Select **Connections** on the [top-level navigation banner](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701115577869-The-Top-Level-Navigation-Banner) or the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243300355725)) or select the **Connections** option on the [Home page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page). The [Connections page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008155149-Connections-Page) appears. Search the list to locate the data store connection definition you want to modify. See [Search and Filter Lists](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008213517-Search-and-Filter-Lists).

   The Connections page lists the data store connections you have defined and identifies how many data source configurations each connection uses.
3. Select the data store connection definition you want to modify. The **Connection Details** tab opens.
4. Select the edit icon ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243316967053) next to the name at the top of the page to change the name of this connection. The field is now editable.

   Change the name and select **Save**.
5. Use the fields on the Connection Details tab to alter the URL and other connection details and, if applicable, the authentication credentials (**User Name** and **Password** fields) required to connect to the data store. Any connection requirements for a specific data store are described in the connector documentation for that data store. See the [Data Connector Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113495693-Data-Connector-Reference).

   You can insert variables for connection parameters, if you have defined any custom attributes in your environment. See [Insert Variables for Connection Parameters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993364749-Insert-Variables-for-Connection-Parameters). Additionally, you can select any user attributes you have defined for connection parameters using the up and down arrows in the connection parameter section. See [Use User Attributes for Connection Parameters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042127373-Use-User-Attributes-for-Connection-Parameters).
6. If the **Do As User** option is available, optionally specify the custom user attributes you set up to enable user delegation. See [Apply User Delegation to a Connection](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039356557-Apply-User-Delegation-to-a-Connection).
7. This is an optional step.

   Each data source configuration specifies refresh settings for the data from the data store. If a data store connection requires special credentials to refresh the data source data, select the **Add an Override** button under **Scheduler Overrides** and select an override setting to use. The override settings you can specify mirror the regular data store connection settings (except for the connection definition name) and vary based on the type of data store connector used for the connection. See [Data Connector Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113495693-Data-Connector-Reference).

   More than one override setting can be specified. Simply select the **Add an Override** button again and select a different setting and provide its input value. Repeat this process until all override settings required by the data store have been specified.
8. Select **Validate** to validate the connection. If the connection is valid, you can save the connection. If invalid, make changes, then select **Validate** again.
9. Select **Save** to save the connection.
10. To see the data source configuration definitions that use this connection definition, select the **Data Sources** tab.
11. Select **Back** at the top of the page to return to the [Connections page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008155149-Connections-Page) that lists the connection definitions.
