---
title: "Add a Database Server Connection"
id: 4419707466263
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707466263-Add-a-Database-Server-Connection
updated_at: 2022-07-17T01:54:22Z
---

# Add a Database Server Connection

# Add a Database Server Connection

The **Connection** element comes in a variety of flavors, depending on the nature of the connection to be made. The best method of connecting is to use a *vendor-specific* connection element, such as Connection.Oracle, or Connection.MySQL, when you can. There are also generic connection elements.
The following example uses **Connection.SQLServer** to connect to Microsoft SQL Server. If you're using a different database server, substitute the appropriate elements and attributes in the following discussion.

##### 

Here's how to add a Connection element:

1. In the Application Panel, double-click the **\_Settings** definition to open it in the Workspace editor. You can see it opens in a different tab than the new definition you added earlier.
2. Select the **Connections** element. In the Element Toolbox panel, double-click the connection element appropriate for your database server to add it. This is the basic technique for adding elements: select a *parent* element and double-click a *child* element which is then added beneath it.
3. When the newly-added connection element is selected, its properties or "attributes" will appear in the Attributes Panel. Find its **ID** attribute and set it to a unique value. The example uses *connNW* because we're going to connect to the Northwind database.
4. In the Attributes Panel, provide the other attribute values shown above, using values appropriate for your database and server.
5. Save your \_Settings definition by clicking the **Save** item in the main menu
6. Close the \_Settings definition by clicking the "X" icon in its editor tab.

The connection is now configured and ready for use.
