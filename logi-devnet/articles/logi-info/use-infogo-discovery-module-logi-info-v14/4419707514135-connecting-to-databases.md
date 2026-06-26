---
title: "Connecting to Databases"
id: 4419707514135
section: "Use InfoGo/Discovery Module - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707514135-Connecting-to-Databases
updated_at: 2022-07-17T01:52:18Z
---

# Connecting to Databases

# Connecting to Databases

In DM v3.1, a connection to data is called a "Source" and can be an
application, database, or file connection. In this topic, we'll
create a new Source based on a SQL database. There are multiple paths to
the Add Source panel, including:

* **Sources** menu option![](https://devnet.logianalytics.com/hc/article_attachments/4419714617623/menuarrowrt.png)Create New Source.
* **Dataviews** menu option![](https://devnet.logianalytics.com/hc/article_attachments/4419714617623/menuarrowrt.png)Create New Dataview![](https://devnet.logianalytics.com/hc/article_attachments/4419714617623/menuarrowrt.png)From Source tab![](https://devnet.logianalytics.com/hc/article_attachments/4419714617623/menuarrowrt.png)Add
  New Source

The Add Source panel will appear.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706772503/ls31_dvauth_06.png)

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) There will be different fields presented depending on the Data Provider selection.

Select or provide the required information, as follows:

1. **Database** - Select the Database radio button, making the fields shown above visible.
2. **Data Provider** - Select the desired database or provider
   type. There are several MS SQL Server options, allowing for its different security schemes.
3. **New Source Name** - Give the source an arbitrary name for easy recognition later in the list of sources.
4. **Server Name** - Enter the database server name or IP address.
5. **User Name** - Enter the user name required to access the database.
6. **Password** - Enter the password required to access the database.
7. **Database Name** - Enter the target database name (or, for Oracle, the Service Name).   
     
   For Microsoft SQL Server, MySQL, and PostgreSQL providers, you can use the **Get List** button to select the database name from a list.  
     
   For some providers, an *Advanced Options* link will be shown, allowing you to set special configuration options, such as Schema Name or Warehouse Name, specific to that provider.
8. **Port Number** - Enter the Port number for the connection. The default port number for the provider will be displayed.
9. **Test Source** - Click the button to attempt to make the
   connection specified and provide a status message. In addition to
   indicating either success or failure, any existing Source with the *exact same* specifications will be identified so you can decide whether to use it instead or proceed to save your new Source.

Click **Save** to save your new Source. Repeat as necessary to create all the Sources you need.  

## Working with a SQL Server Named Instance

If you're trying to connect to a named instance of Microsoft SQL Server, such as yourDBServer\SQLEXPRESS,8484 then the example connection shown above will not work. You may have noticed that the Data Providers selection list includes several Microsoft SQL Server variants. One of them is *Microsoft SQL Server Named Connection* and here's an example configuration for it:

![](https://devnet.logianalytics.com/hc/article_attachments/4419714727063/ls31_dvauth_06a.png)

The example above shows how a complex SQL Server connection ID is parsed and placed appropriately in the Add Source panel. You have to expand the Advanced Options area to access the Port Number control.
