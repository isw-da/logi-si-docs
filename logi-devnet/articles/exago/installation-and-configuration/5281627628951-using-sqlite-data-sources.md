---
title: "Using SQLite Data Sources"
id: 5281627628951
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281627628951-Using-SQLite-Data-Sources
updated_at: 2023-04-03T17:52:19Z
---

# Using SQLite Data Sources

# Using SQLite Data Sources

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Beginning with *v2021.1.8+*, native ADO.NET support for SQLite is included. To add a SQLite Data Source in these versions, skip this topic and follow the instructions in [Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/5281617045911-Data-Sources) exclusively.

SQLite is a relational database system which stores data directly in local disk files. Many applications, including Exago, use SQLite in order to store local data. For example, the **Monitoring Service** and **Storage Management** system can uses a SQLite databases.

SQLite data files can be added to Exago as a data source. Exago uses Open Database Connectivity (ODBC) as a translation layer in order to read the files. Before adding a SQLite data source, a SQLite ODBC driver must be installed on the Exago server .

## Installing the SQLite ODBC Driver

There are several options for drivers, but the recommended one is a free and open source package by Christian Werner and other authors.

To install the SQLite ODBC Driver:

### Windows

1. Download the latest version of `sqliteodbc.exe` from [Christian Werner’s website](http://www.ch-werner.de/sqliteodbc/).
   * 64-bit Windows: Also download the latest version of `sqliteodbc_w64.exe`.
2. Run the installer(s) as an administrator to install the drivers.
   * Optional: On the Choose Components page, select **SQLite 2 Drivers**if you need to add a SQLite Version 2 data source.

## Adding a SQLite file as an ODBC data source

Once the SQLite ODBC Driver is installed, SQLite files can be added as ODBC data sources. Most operating systems include a graphical user interface to manage ODBC data sources. In Windows, this is called ODBC Data Source Administrator.

To add a SQLite file as an ODBC database:

### Windows

1. As an administrator, open the ODBC Data Source Administrator:
   1. Click **Start**>**Run**.
   2. Type `odbcad32`.
   3. Press Enter.
2. On the User DSN page, **Add** a new User Data Source.
3. Select the proper SQLite ODBC Driver for the data source:
   * SQLite ODBC Driver
   * SQLite3 ODBC Driver
   * SQLite ODBC (UTF-8) Driver
4. Click **Finish**. Then, in the Configuration window, enter the options for the data source:
   1. In the **Data Source Name** field, enter a name for the data source.
   2. In the **Database Name** field, enter the file path to the SQLite file, or click **Browse** and locate the file.
   3. Optional: Set the other fields according to the requirements of the data source.
5. Click **OK** to close the Configuration window. Then click **Apply** or **OK** to save the data source.

## Adding an ODBC data source to Exago

ODBC data sources are added to Exago in the same manner as other data sources. You can specify an optional Column Delimiter for an ODBC data source.

Either use the Admin Console or edit the Configuration File to add an ODBC data source to Exago:

### Option 1: Admin Console

1. Open the Admin Console by browsing to `http://.../{Exago}/Admin.aspx`
2. In the Contents pane on the left, select **Sources**. Then press the Add button to open a New Data Source window.
   * If you don’t see **Sources**, double-click **Data** to expand the Data menu.
3. In the New Data Source window, enter the options for the data source:
   1. Enter a **Name** for the data source.
   2. From the **Type** list, select **odbc**.
   3. Optional: Enter a **Column Delimiter(s)** and **Schema/Owner Name**.
   4. In the **Connection String** field, enter a connection string in the following format:`DRIVER=driver;Database=path;[LongNames=0|1];[Timeout=timeout];[NoTXN=0|1];[SyncPragma=NORMAL|OFF|FULL];[StepAPI=0|1];`

      where:  
      `DRIVER=driver` specifies the type of SQLite ODBC Driver.  
      `Database=path` specifies the file path to the SQLite file.

      #### Example

      ```
      DRIVER=SQLite3 ODBC Driver;Database=C:ExagodatabasesNorthwind.sqlite;LongNames=0;Timeout=1000;NoTXN=0;SyncPragma=NORMAL;StepAPI=0;
      ```
4. You can click the **Test** button to check whether the data source was configured correctly. If the connection is successful, click **Apply** or **OK** to save the data source.

### Option 2: Configuration File

1. Open the Configuration File in a text or xml editor.
2. Add a new `<datasource></datasource>` element in the `<webreports>` parent element.
3. In the `<datasource>` element add the following fields:
   * `<id>id</id>` where *id* is a unique integer identifier for the data source
   * `<name>name</name>` where *name* is a name for the data source
   * `<dbtype>odbc</dbtype>`
   * `<dataconnstring>connectionstring</dataconnstring>` where *connectionstring* is a formatted connection string (See “Admin Console” Step 3.4, above)
   * Optional: `<schema>schema</schema>` where *schema* is a Schema/Owner Name
   * Optional: `<odbcdelim>delim</odbcdelim>` where *delim* is a Column Delimiter(s)

   #### Example

   ```
   <webreports>
      ...
      <datasource>
         <id>1</id>
         <name>Northwind</name>
         <dbtype>odbc</dbtype>
         <dataconnstr>DRIVER=SQLite3 ODBC Driver;Database=C:ExagodatabasesNorthwind.sqlite;LongNames=0;Timeout=1000;NoTXN=0;SyncPragma=NORMAL;StepAPI=0;</dataconnstr>
      </datasource>
      ...
   </webreports>
   ```
4. Save the Configuration File.

After you add the data source, you must add the data objects and joins. See **[Data Objects](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects)** and **[Join Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281644535703-Join-Configuration)**.
