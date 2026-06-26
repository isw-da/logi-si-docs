---
title: "Add Data Store Connections"
id: 4405859165335
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859165335-Add-Data-Store-Connections
updated_at: 2021-09-21T01:27:00Z
---

# Add Data Store Connections

# Add Data Store Connections

You can add and validate data store connections on the [Connections page](https://devnet.logianalytics.com/hc/en-us/articles/4405850909975-Connections-Page) in the UI. You can also add and validate them when you create a new data source configuration using the data source configuration wizard. See [*Connection Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405851023767-Connection-Tab).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) You must be logged in as an administrator or as a user with the [group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)**Can Manage Connections** to maintain data store connection definitions.

To manually add and validate a data store connection definition using the Connections page in the UI:

1. Make sure you are logged into Composer as an administrator or as a user with the [group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)**Can Manage Connections**.
2. Select **Connections** on the [top-level navigation banner](https://devnet.logianalytics.com/hc/en-us/articles/4405851152407-The-Top-Level-Navigation-Banner) or the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)) or select the **Connections** box on the [Home page](https://devnet.logianalytics.com/hc/en-us/articles/4405851121559-Home-Page). The [Connections page](https://devnet.logianalytics.com/hc/en-us/articles/4405850909975-Connections-Page) appears.

   The Connections page lists the data store connections you have defined and identifies how many data source configurations each connection uses.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743924119/add-connection-btn_97x23.png) in the upper right corner of the data store connection list. The Select a Connection Type dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743924375/select-connection-type_288x202.png)
4. Select the connection type you want to use for the connection definition. The Add <type> Connection page appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747453591/add-connection_288x414.png)
5. Optionally, change the name for the connection in the **Connection Name** box. A default name based on the connector is initially set by Composer.
6. The connection details required to connect to a data store vary by data store. Use the boxes on the Connection Details tab to specify the URL and other connection details and, if applicable, authentication credentials (**User Name** and **Password** boxes) required to connect to the data store. Boxes that are highlighted in red are required. Any connection requirements for a specific data store are described in the connector documentation for that data store. See the [*Composer Data Connector Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405859436055-Composer-Data-Connector-Reference).

   You can insert variables for connection parameters, if any custom attributes have been defined. See [*Insert Variables for Connection Parameters*](https://devnet.logianalytics.com/hc/en-us/articles/4405850919063-Insert-Variables-for-Connection-Parameters). In addition, if user attributes have been set up for connection parameters, they can be selected using the up and down arrows in the connection parameter box. See [*Use User Attributes for Connection Parameters*](https://devnet.logianalytics.com/hc/en-us/articles/4405859180951-Use-User-Attributes-for-Connection-Parameters).
7. If the **Do As User** box is available and you want to enable user delegation, optionally specify the custom user attribute set up for user delegation. See [*Apply User Delegation to a Connection*](https://devnet.logianalytics.com/hc/en-us/articles/4405850928919-Apply-User-Delegation-to-a-Connection).
8. This is an optional step.

   Each data source configuration specifies refresh settings for the data from the data store. If a data store connection requires special credentials in order for Composer to refresh the data source data, select the ![](https://devnet.logianalytics.com/hc/article_attachments/4406747431959/add-override-btn_90x28.png) button under **Scheduler Overrides** and select an override setting to use. The override settings you can specify mirror the regular data store connection settings (except for the connection definition name) and vary based on the type of data store connector used for the connection. See [*Composer Data Connector Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405859436055-Composer-Data-Connector-Reference).

   More than one override setting can be specified. Simply select the ![](https://devnet.logianalytics.com/hc/article_attachments/4406743850775/add-override-btn_89x27.png) button again and select a different setting and provide its input value. Repeat this process until all override settings required by the data store have been specified.
9. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747451799/validate-btn.png) to validate the connection. If the connection is valid, it is saved.
10. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747453079/back.png) at the top of the page to return to the [Connections page](https://devnet.logianalytics.com/hc/en-us/articles/4405850909975-Connections-Page).
