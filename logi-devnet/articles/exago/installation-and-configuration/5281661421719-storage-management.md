---
title: "Storage Management"
id: 5281661421719
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management
updated_at: 2023-04-03T17:52:19Z
---

# Storage Management

# Storage Management

This topic applies to the **Admin Console** >**![TreeStorageMgmt.png](https://devnet.logianalytics.com/hc/article_attachments/5432175848087/treestoragemgmt.png) Storage Management** settings.

---

### Assembly Location

The path and file name of the DLL that implements the `IStorageManagement` interface. The default value is *<WebApp>\bin\WebReports.ContentDatabase.dll*, which will use Exago’s Storage Management implementation, where <WebApp> represents the Web Application’s installation directory.

Provide the fully qualified path to the file. If no path is supplied, Exago checks the Web Application’s `bin` directory for the DLL, or in *v2020.1.15+* and *v2021.1.3+* falls back to the internal Exago implementation of Storage Management.

### Class Name

The name of the class in the assembly that implements the `IStorageManagement` interface. The default value is *WebReports.ContentDatabase.StorageMgmtDatabase*, which uses Exago’s Storage Management implementation.

Click the **Validate Assembly**![CheckmarkAdmin.png](https://devnet.logianalytics.com/hc/article_attachments/5432158412439/checkmarkadmin.png) icon to validate that the assembly exists and that all methods of `IStorageManagement` can be found by Exago in that class.

## Database

Out-of-the-box, Exago provides a SQLite implementation of the Storage Management database. The default values noted for each setting below reflect the default SQLite installation.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Exago recommends using the included SQLite database for development, testing and demonstration purposes only. Use MSSQL, MySQL, Oracle or PostgreSQL in a production environment.

### Database Type

Choose the type of the Storage Management database:

* *SQLite* (default value)
* *MSSQL* — Microsoft SQL Server
* *MySQL*
* *Oracle*
* *PostgreSQL*

### Database Provider

Specify the name of the database provider Exago uses to connect to the Storage Management database. This matches the *InvariantName* found as a property of **DbProviderFactories** in the server’s `machine.config` file. The default value is *SQLite*

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The `machine.config` file is located in the `%SystemRoot%\Microsoft\.NETFramework\%VersionNumber%\CONFIG` directory.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> Use the applicable database provider name from the **Admin Console** > ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Database Settings**.

### Database Connection

Connection string Exago uses to connect to the Storage Management database.

Default value for SQLite is *Data Source=<FILENAME>*. Replace *<FILENAME>* with the absolute path and file name to the database file. For example: `Data Source=D:\StorageMgmt.sqlite`. When using SQLite, the default location will be the `/Config` directory under the Exago Web Application install directory.

For PostgreSQL on Windows, include `Unicode=true` in the connection string.

## Tables

Review [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema) and [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction) for more information about the purpose of each of these tables. Each table name may also include a schema (for example *dbo.content*).

### Table Prefix

Provide an optional prefix for all Storage Management database tables. Review the [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema) topic for information. This option can be used to add a schema if it exists.

**Examples**:

1. `test_` will result in tables named *test\_content*, *test\_party\_type*, *test\_content\_access* and *test\_storage\_meta*
2. `dbo.` will result in tables named *dbo.content*, *dbo.party\_type*, *dbo.content\_access* and *dbo.storage\_meta*

### Check Database Settings

Select to verify the connection between Exago and the Storage Management database. Also checks that the tables exist in the database.

### Show Prepare Database SQL

Click to display the SQL statements that initialize a Storage Management database with the schema and default party types. Works similar to the **Prepare Database** button but displays the SQL statements on screen instead of executing them.

This button also show any SQL statements needed to update the schema if necessary on an existing database.

### Prepare Database

Click to create the four Storage Management tables, load default party types into the Party Type table and create the **Public** and **My Reports** folders if they don’t already exist.

This button also updates the schema if necessary on an existing database. It is not destructive.

### Load Themes

Click to load new chart, ExpressView, CrossTab and GeoChart themes from the `<WebApp>\Themes` folder into the Storage Management database.

This is only necessary for first time installations of Exago, after upgrading to Storage Management from a legacy storage mechanism and themes were not imported with one of the [transitioning utilities](https://devnet.logianalytics.com/hc/en-us/articles/5281647090839-Storage-Management-Transitioning-from-Legacy-Storage-Methods) or after adding new themes to the Themes directory (either by Exago or by customizing the application).

### Update Reports v2021.1+

The **associated\_reports** column of the Storage Management Content table is a comma separated list of content\_ids for each report that is associated with a particular content record. Reports become associated with others when they are components in a Composite Report such as Chained Report or Dashboard, or if an Advanced Report contains links to other reports (a.k.a. drilldowns).

This **Update Reports** function in the Admin Console reads the contents of a Storage Management database, parses the report file contents and generates the comma separated lists of associated\_reports where applicable.

Depending on the size of the Storage Management database, the Update Reports process may take several minutes to complete. Once finished, an Update All Reports dialog will appear with the results of the operation.

For more information, hover the mouse over the button to see the tooltip. Then click on the **Storage Management** link in the tooltip.

## Identity

The Storage Management Identity keys are used similar to the system-wide @userId@ and @companyId@ parameters but only affect content storage. Like @userId@ and @companyId@, they should be set each time an Exago session is created via the API.

The settings here can be used for testing and demonstration purposes. See [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction) and [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema).

### Class Id

Set a value for the **Class Id** identity key.

### Company Id

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This is similar to, but is not the same as the system-wide @companyId@ parameter.

Set a value for the **Company Id** identity key.

### User Id

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This is similar to, but is not the same as the system-wide @userId@ parameter.

Set a value for the **User Id** identity key.

When accessing Storage Management properties through the Admin Console (for example when viewing Role Folder Permissions) all access filters will be removed and all content will be available.

### Owner Id

Set the value for **Owner Id**. When the Owner Id of a content item matches the value of the Owner Id identity key, full access is granted to that content item automatically.

## Default Settings & Content Access Permissions

The default settings determine how permissions are configured for newly created content in the root.

Individual folders have their own inherit flag, default party type and default access flags properties. If for some reason individual folders do not have their own inherit flag, default party type or default access flags set (that is they are null or disabled) then the values here will be applied.

### Inherit Flag

Set the default value of the **Inherit Flag**.

If *True*, new folders created in the root will have their **inherit flag** set to *true*.  When a folder’s **inherit flag** is *true*, new content created in that folder will copy all of the access records from its parent.

If *False*, new folders created in the root will have their **inherit flag** set to *false.* When a folder’s **inherit flag** is *false*, new content created in that folder will have a single new content access record written with the **default party type** and **default access flags**.

Default value is *True*.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This setting determines the value of the **Inherit Flag** on child folders of the root. Folders created in the root do not copy the access records from the root folder. Instead, a single content access record with the **Default Party Type** will be written for new folders in the root.

### Party Type

Set the **default party type** for newly created folders in the root. Regardless of the value of **Party Type**, new folders created in the root will have their **default party type** set to this value.

When **Inherit Flag** is *True*, this dropdown is disabled as content access records will be inherited from the content’s parent and therefore will not have an effect.

### Access Flags v2020.1–v2021.1

### Default Access Permission v2021.1+

Set the **default access flags** that will be used for newly created content when not inheriting access from the parent objects. Choose from:

* *Full Access* — there will be no restriction on access to content
* *Read Only* — content is marked as read-only in a similar way to Roles. When content is read-only, it cannot be edited, saved or deleted. Read-only folders cannot have new content saved into them. Read-only reports can be duplicated into non-read-only folders.
* *Custom (pre-v2021.1)* — a different content access strategy can be implemented by manually editing the XML configuration file and providing a value in the `<default_access_flags>` node.
* *Custom (v2021.1+)* — a different content access strategy can be implemented by manually checking the corresponding permission checkboxes.

Each of the access flags are defined in [Access Flags v2021.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction#Access).

**CanView**, **CanSave** and **CanEdit** are implemented in *v2020.1*. The other flags are not yet active and will be implemented in *v2021.1*.

## Cache Settings

### Enable Report List Caching

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This setting was formerly located in ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Other Settings**.

Set to *True* to enable the folders and report list in the ![MainLeftPaneViewReports.png](https://devnet.logianalytics.com/hc/article_attachments/5432210088471/mainleftpaneviewreports.png)**Report Tree** to be cached, rather than querying the Storage Management database each time they are needed. Default value is *True*.

It is recommended to enable **Report List Caching**, even with a small timeout. Care should be taken when running Exago in a web farm environment, as the caches will become unsynchronized.

#### Timeout

If **Enable Report List Caching** is *True*, set the timeout in seconds that the folder and report list cache should expire. Default value is *30* seconds.

### Enable Report XML Caching

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This setting was formerly located in ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Other Settings**.

If *True*, the XML report definition content will be cached rather than being read from the database each time it is needed. Enabling this setting will reduce the number of calls to the Storage Management database and may help with performance. Default value is *True.*

It is recommended to enable **Report XML Caching**, even with a small timeout. Care should be taken when running Exago in a web farm environment, as the caches will become unsynchronized.

#### Timeout

If **Enable Report XML Caching** is *True*, set the timeout in seconds that the folder and report list cache should expire. Default value is *30* seconds.

### Theme List Caching Timeout

Set the timeout in seconds that the report and chart theme cache should expire. Default value is *30* seconds.

## Additional Resources

* [Admin Support Lab - Storage Management Overview](https://devnet.logianalytics.com/hc/en-us/articles/5281554383127-Storage-Management-Overview) (video)
* [Admin Training Series - Storage Management Permissioning and Setup](https://devnet.logianalytics.com/hc/en-us/articles/5281571962903-Storage-Management-Permissioning-and-Setup) (video)
