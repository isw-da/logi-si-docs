---
title: "Modify  Data Store Connections"
id: 43701054605453
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054605453-Modify-Data-Store-Connections
updated_at: 2026-08-26T07:11:36Z
---

# Modify  Data Store Connections

# Modify Data Store Connections

You can modify data store connections as needed if credentials or addresses change. Once updated, your data sources will automatically reference the new connection configuration.

**Note:** In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.

## **Modify a Data Store Connection Definition**

1. Log in as an administrator, or user with the [group privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) **Manage Connections**.
2. Select the **Connection** card on your home page or **Connections** from the main menu. The [Connections work area](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008155149-Connections-Page) appears. The [Connections page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008155149-Connections-Page) appears.

   Search the list of data store connections defined to locate the data store connection definition you want to modify. See [Search and Filter Lists](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008213517-Search-and-Filter-Lists).
3. Select the data store connection definition you want to modify. The **Connection Details** tab opens.
4. Select the edit icon next to the name at the top of the page to change the name of this connection. The field is now editable. If you are using the enhanced experience user interface, select the name at the top of the work area to make the field editable. Change the name and select **Save**.
5. Use the fields on the Connection Details tab to alter the URL and other connection details and, if applicable, the authentication credentials (**User Name** and **Password** fields) required to connect to the data store. Any connection requirements for a specific data store are described in the connector documentation for that data store. See the [Data Connector Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113495693-Data-Connector-Reference).

   You can insert variables for connection parameters, if you have defined any custom attributes in your environment. See [Insert Variables for Connection Parameters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993364749-Insert-Variables-for-Connection-Parameters). Additionally, you can select any user attributes you have defined for connection parameters using the up and down arrows in the connection parameter section. See [Use User Attributes for Connection Parameters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042127373-Use-User-Attributes-for-Connection-Parameters).
6. If the **Do As User** option is available, optionally specify the custom user attributes you set up to enable user delegation. See [Apply User Delegation to a Connection](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701039356557-Apply-User-Delegation-to-a-Connection).
7. This is an optional step.

   Each data source configuration specifies refresh settings for the data from the data store. If a data store connection requires special credentials to refresh the data source data, select the **Add an Override** button under **Scheduler Overrides** and select an override setting to use. The override settings you can specify mirror the regular data store connection settings (except for the connection definition name) and vary based on the type of data store connector used for the connection. See [Data Connector Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113495693-Data-Connector-Reference).

   More than one override setting can be specified. Simply select the **Add an Override** button again and select a different setting and provide its input value. Repeat this process until all override settings required by the data store have been specified.
8. Select **Validate** to validate the connection. If the connection is valid, you can save the connection. If invalid, make changes, then select **Validate** again.
9. Select **Save** to save the connection.
10. To see the data source configuration definitions that use this connection definition, select the **Data Sources** tab.
11. Select **Back** at the top of the page to return to the [Connections work area](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701008155149-Connections-Page) that lists the connection definitions.

### Connect to a Dundas BI Data Store

If you are transitioning from an earlier release of Symphony, complete these steps as you work with technical support to reconnect to the data in your Dundas BI environment.

**Important:** You will need appropriate licensing for all relevant components to complete this procedure.

* Register the Dundas BI (formerly Managed) connector server, then add the connector. See [Register the Dundas BI (Managed) Connection Server](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701042690957-Register-a-New-Connector-Server#Register) and [Define a New Connector](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700993403661-Define-a-New-Connector).
* Add the credentials to a new connection using the Managed connector. See [Add Data Store Connections](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992503437-Add-Data-Store-Connections).
* If you are reconnecting to a Dundas BI data store, update your existing sources to use the new connection.

1. Create and validate a new Managed connection. You will need to provide the `PROJECT` information associated with the data source, your Dundas BI credentials, and make the `IMPERSONATE_ACCOUNT` field visible. See [Add Data Store Connections](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992503437-Add-Data-Store-Connections).
2. Navigate to your [Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701081381901-Data-Sources-Page) page, then select each Managed source to update it to use the new connection. The Folder and Entity you select must match your original configuration. See [Edit a Data Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116405261-Edit-a-Data-Source).
3. **Save** your changes. Once updated, your data sources will automatically reference the new connection configuration.

For more information on specifically connecting to a Data Cube, see [Add and Validate a Connection to a Dundas BI Data Source or Data Cube](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992503437-Add-Data-Store-Connections#data_cube).
