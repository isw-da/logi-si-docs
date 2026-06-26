---
title: "Storage Management: Transitioning from Legacy Storage Methods"
id: 5281647090839
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281647090839-Storage-Management-Transitioning-from-Legacy-Storage-Methods
updated_at: 2022-05-03T22:08:47Z
---

# Storage Management: Transitioning from Legacy Storage Methods

# Storage Management: Transitioning from Legacy Storage Methods

Exago’s **Storage Management** system replaces the legacy *file system*, *cloud storage*, *folder management* and *web service (SOAP)* storage methods with a relational database. All reports, templates, folders and themes are stored in this database. Microsoft SQL Server, MySQL, Oracle and PostgreSQL are supported out-of-the-box. Exago also supports a SQLite database for development, testing and demonstration.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Exago recommends using the included SQLite database for development, testing and demonstration purposes only. Use MSSQL, MySQL, Oracle or PostgreSQL in a production environment.

Review the [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema) topic to gain an understanding of the structure and implementation of this database. The [Storage Management Migration](https://devnet.logianalytics.com/hc/en-us/articles/5281547914775-Storage-Management-Migration) support lab includes a narrative walk through and demonstration of the migration process.

## General Procedure

To upgrade from legacy file system, cloud storage or Exago’s reference example of Folder Management to relational **Storage Management** the general procedure is as follows. Clients implementing custom Folder Management or SOAP Web Services should contact their Customer Success Manager for further information.

1. Identify the legacy storage method in use (either *file system*, *cloud storage*, *folder management* or *SOAP* *web service*).
2. Make a backup of the contents of the legacy storage method.
3. Read the contents of the legacy storage method into an intermediate JSON file with one of the Exago provided [transitioning utilities](#Transiti). This intermediate JSON file saves a copy of the legacy storage method’s contents, and allows manual editing of it if desired before import.
4. *Not typical:* Make any changes to the [intermediate JSON file](#Intermed) to suit the destination database environment or access permissions required.
5. Initialize the destination Storage Management database.
6. Load the contents of the intermediate JSON file into the destination database with one of the Exago provided [transitioning utilities](#Transiti).
7. Configure the Exago Web Application to connect to the Storage Management database. Information for this and the following steps can be found in the sections at the end of this topic: [Upgrading from File System or Cloud Storage](#Upgradin), [Upgrading from Folder Management](#Upgradin2) or [Upgrading from Web Service (SOAP) Storage](#Upgradin3).
8. Update any API integration code to set the identity keys each time a new session is created.

### Transitioning Utilities

Exago provides several utilities for completing the above steps, described in **Table A** below.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic references `<WebApp>/`,
> `<WebSvc>/` and `<Sched>/`as a placeholder
> for the Web Application, Web Service API and Scheduler Service's install
> location respectively. The default install location is
> `C:\Program Files\Exago\ExagoWeb\` (`/opt/Exago/` on Linux),
> `C:\Program Files\Exago\ExagoWebApi\` ( `/opt/Exago/WebServiceApi/` on Linux) or
> `C:\Program Files\Exago\ExagoScheduler\` (`/opt/Exago/Scheduler/` on Linux); however, these directories
> can be changed during installation.

These utilities can be found in `<WebApp>\bin`

Table A — Storage Management Transition Utilities

| Step | Utility | Legacy Method(s) | Function/Purpose |
| --- | --- | --- | --- |
| 2 | [CloudToJson](#CloudToJ) | cloud storage | Reads an existing *cloud storage* implementation and translates it to an intermediate JSON file. |
| 2 | [DatabaseToJson](#Database) | folder management | Reads an existing database storage implementation and translates it to an intermediate JSON file. Typically used by legacy *folder management* environments implementing the Exago example. |
| 2 | [FileSystemToJson](#FileSyst) | file system | Reads an existing *file system* implementation and translates it to an intermediate JSON file. |
| 4, 5 | [LoadReportsToDb](#LoadRepo) | all | This utility can change its function depending on command line arguments to either:   * *Initialize* the destination Storage Management database with the schema. * *Load* the contents of an intermediate JSON file into the destination database, or load the contents from a file system or cloud stroage repository directly into the destination database. * *Read* the contents of the Storage Management database and display it in a format similar to the `tree` console command. |

Regardless of legacy storage implementation, the transition utilities are non-destructive. The legacy content is only *read* during this process. It is prudent to make a backup of the legacy content store before any system upgrade.

They will run on Windows and Linux. On Windows, they should be run with Administrator privileges.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> When running the transition utilities on Linux, make sure the execute permission bit is set on the utility’s .exe file.

For each of the utilities below, optional command line parameters are enclosed in { braces }. If a parameter has a defined set of possible values, they are enclosed in [ brackets ]. Default values are **bold**. The utilities process the command line parameters in the order they are entered, and may be combined into multiple actions with a single call.

* [CloudToJson](#CloudToJ)
* [DatabaseToJson](#Database)
* [FileSystemToJson](#FileSyst)
* [LoadReportsToDb](#LoadRepo)

#### CloudToJson

**CloudToJson** is used to read one or more directories on a cloud storage repository and generate an intermediate JSON file describing the contents of that repository. If required, modifications can be made to this JSON file before loading content into the Storage Management database. JSON file will be created in `<WebApp>binCloudToJson.json`.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> If customizing the JSON file is not necessary, [LoadReportsToDb](#LoadRepo) can read from a cloud repository directly without first having to create an intermediate JSON file.

##### Command Line Structure

```
CloudToJson.exe <cloudspec>
```

##### Command Line Parameters

Table B — **CloudToJson** Command Line Parameter Definitions

| Parameter | Description/Usage |
| --- | --- |
| <cloudspec> | The string defining the connection to the cloud repository. Typically, this is Exago’s **Report Path**. |

##### Common Usage Examples

**Create JSON file in default directory**: Read the contents of a file system report repository. JSON file will be created in `<WebApp>\bin\CloudToJson.json`.

```
CloudToJson.exe "pathtype=s3;region='myRegion';accesskey='myAccessKey';secretkey='mySecretKey';bucketname='myBucketName'"
```

##### Manually Editing the Intermediate JSON File

In some circumstances, customizing the intermediate JSON file may be desirable or needed to properly set permissions on the content in the destination database. The contents of the JSON file and an explanation of each element can be found in the [Intermediate JSON File](#Intermed) section of this topic.

##### Access Flags

In a cloud storage mechanism, all users have access to all content without restriction. Access controls are determined by use of Roles. **CloudToJson** will accordingly grant all access to all content.

By default **CloudToJson** will set:

* **AccessFlags** to *1111111111111111* granting all access permissions.
* **ReportAccessList** to be empty.

Learn more in Review [Intermediate JSON File](#Intermed) and [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction).

##### Troubleshooting

A log file named `CloudToJson.log` is saved to **CloudToJson**‘s installation directory, typically `<WebApp>\bin`Send this file to the Exago Support Dept when asking for assistance in troubleshooting this utility.

#### DatabaseToJson

**DatabaseToJson** is used to read the report content and access permissions information from a source database to an intermediate JSON file. It is designed for transitioning implementations of Exago’s folder management example to Storage Management. It can also be used to transition from Exago’s included SQLite database to a production database after testing is completed.

Access permissions from the source database will be transferred to an intermediate JSON file for importing into the Storage Management database. Orphaned reports will be imported into an *Orphaned Reports* folder.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> An *Orphaned Report* is one not attached to any folder (including the root); or attached to a folder that cannot be traced from the root. This typically happens if there is a missing record in the legacy folder management database’s `access` table. Likewise, folders not traceable to the root will not be imported into the Storage Management database.
>
> Orphaned reports will be visible to all users with all access flags set to true.

##### Command Line Structure

**DatabaseToJson** needs to know how to connect to and read the data from the legacy database. This information is conveyed to **DatabaseToJson** in one of two ways:

* If no command line parameter is specified, **DatabaseToJson** will read the information from the `<applicationSettings><DatabaseToJson.Properties.Settings>` nodes of the **`DatabaseToJson.exe.config`** file. These values must be configured before running **DatabaseToJson** the first time. Review **Table D** below for information on each setting.
* An optional command line parameter can be specified to choose a predefined configuration from a `DatabaseToJson.config.json` file in **DatabaseToJson**‘s installation directory. The DatabaseToJson.config.json file may describe one or more database configurations to read from. It must be created before running **DatabaseToJson** the first time. The contents of the file are described in **Table D** below.

```
DatabaseToJson.exe {<configuration>}
```

##### Command Line Parameters

Table C — **DatabaseToJson** Command Line Parameter Definitions

| Parameter | Description/Usage |
| --- | --- |
| <configuration> | The name of the configuration from the optional DatabaseToJson.config.json file to use.  If no configuration parameter is provided, **DatabaseToJson** will read the connection data from DatabaseToJson.exe.config instead. |

A sample of the `DatabaseToJson.config.json` file is below. This file defines two configurations, one named *default* and the other *sqlite*.

```
{
    "default": {
    "DbType": "SqlServer",
    "DbProvider": "System.Data.SqlClient",
    "ConnectionString": "Server=mydbserver;Database=thedatabase;uid=dblogin;pwd=dbpassword",
    "ContentSql": "SELECT id, name, CASE WHEN leaf_flag=1 THEN 0 WHEN leaf_flag=0 THEN 1 WHEN type=1 THEN 3 WHEN type=2 THEN 2 ELSE NULL END AS content_type, ReportType AS report_type, isDeleted AS deleted_flag, dateCreated AS created_date, createdByUserId AS created_by, dateLastModified AS modified_date, lastModifiedByUserId AS modified_by, OwnerId AS owner_id, themeType AS content_attribute, bit_content as bit_content, content AS text_content FROM Reports ORDER BY dateCreated",
    "AccessSql": "SELECT ReportId AS id, ParentId AS parent_id, PartyType+1 AS party_type_id, CASE WHEN PartyType=0 THEN NULL ELSE PartyId END AS party_id, Sortorder AS sort_order, CASE WHEN ReportAccess.ReadOnly=1 THEN 0 ELSE 1 END as edit_access, CASE WHEN ReportAccess.ReadOnly=1 THEN 0 ELSE 1 END as save_access, CASE WHEN ReportAccess.CanRename=1 THEN 1 ELSE 0 END as rename_access, CASE WHEN ReportAccess.CanShare=1 THEN 1 ELSE 0 END as share_access, CASE WHEN ReportAccess.ReadOnly=1 THEN 0 ELSE 1 END as delete_access, 1 as execute_access, 1 as copy_access, 1 as download_access, 1 as export_access, CASE WHEN ReportAccess.ReadOnly=1 THEN 0 ELSE 1 END as remove_access, 1 as view_access, 1 as share_access FROM ReportAccess ",
"OutputFile":"DatabaseToJson.json"
  },
"sqlite": {
	"DbType": "SQLite",
	"DbProvider": "SQLite",
	"ConnectionString": "Data Source=C:\Program Files\Exago\ExagoWeb\Config\StorageManagement.sqlite",
	"ContentSql": "SELECT content_id as id, name, content_type, report_type, deleted_flag, created_date, created_by, modified_date, modified_by, owner_id, content_attribute, bit_content, text_content FROM content WHERE content_id != '00000000-0000-0000-0000-000000000000' ",
	"AccessSql": "SELECT content_id AS id, parent_id, party_type_id, party_id, sort_order, access_flags & 0x0001 as edit_access, access_flags & 0x0002 as save_access, access_flags & 0x0004 as rename_access, access_flags & 0x0008 as share_access, access_flags & 0x0010 as delete_access, access_flags & 0x0020 as execute_access, access_flags & 0x0040 as copy_access, access_flags & 0x0080 as download_access, access_flags & 0x0100 as view_access, access_flags FROM content_access ",
	"OutputFile":"SQLiteToJson.json"
	}
}
```

Table D — **DatabaseToJson.config.json** Definition

| Name | Type | Description |
| --- | --- | --- |
| ConnectionString | string | Connection string to connect to the legacy storage source database. |
| DbType | string | The type of source database. Must be one of the following:   * *Sqlite* * *Mysql* * *SqlServer* — Microsoft SQL Server * *Oracle* * *PostgreSQL* |
| DbProvider | string | Driver to use for connection to the source database  light bulb Use the applicable driver name from the **Admin Console** > TreeGeneral.png**General** > TreeGeneralNode.png**Database Settings**. |
| contentSQL | string | SQL statement to read content from the source database.  Modify the names of the applicable columns in the source database.  See [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema). |
| accessSQL | string | SQL statement to read access rights from the source database.  Modify the names of the applicable columns in the SQL statement to match those in the source database.  See [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema). |
| outputFile | string | The fully qualified file name of the intermediate JSON file that will be output.  If there is no path, the file will be saved in the directory where DatabaseToJson is run from. |

##### Access Flags

Learn more in Review [Intermediate JSON File](#Intermed) and [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction).

##### Manually Editing the Intermediate JSON File

In some circumstances, customizing the intermediate JSON file may be desirable or needed to properly set permissions on the content in the destination database. The contents of the JSON file and an explanation of each element can be found in the [Intermediate JSON File](#Intermed) section of this topic.

##### Troubleshooting

A log file named `DatabaseToJson.log` is saved to **DatabasetoJson**‘s installation directory, typically `<WebApp>\bin.`Send this file to the Exago Support Dept when asking for assistance in troubleshooting this utility.

#### FileSystemToJson

**FileSystemToJson** is used to read one or more directories on a local file system and generate an intermediate JSON file describing the contents of those directories. If required, modifications can be made to this JSON file before loading content into the Storage Management database.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> If customizing the JSON file is not necessary, [LoadReportsToDb](#LoadRepo) can read from a file system repository directly without first having to create an intermediate JSON file.

##### Command Line Structure

If the last parameter is not an existing directory it is assumed to be the path to the output file.

```
FileSystemToJson.exe <directory> {<directory> ..} {outputfile}
```

##### Command Line Parameters

Table E — **FileSystemToJson** Command Line Parameter Definitions

| Parameter | Description/Usage |
| --- | --- |
| <directory> | At least one directory must be specified for FileSystemToJson to read. Typically, this is Exago’s **Report Path** and the Themes directory.  Additional directories may be specified by separating them with a space. |
| <outputfile> | An optional path and file name to give the JSON file the utility will generate.  If not specified here, the file will be named `FileSystem.json` in the directory **FileSystemToJson** is in. |

##### Common Usage Examples

**Create JSON file in default directory**: Read the contents of a file system report repository located at `C:\ExagoReports` and any themes located in `C:\ExagoThemes`. JSON file will be created in `<WebApp>\bin\FileSystem.json`.

```
FileSystemToJson.exe C:\ExagoReports C:\ExagoThemes
```

Sample output:

```
12:00:39 INFO - Export Starts
12:00:40 INFO - from:'C:\ExagoReports'
12:00:40 INFO - to:c:\Exago\bin\FileSystem.json
12:00:40 INFO - Loading from C:\ExagoReports
12:00:40 INFO - Loading from C:\ExagoThemes
```

**Create JSON file in specified directory**: Read the contents of a file system report repository located in `C:\ExagoReports`, any templates at `C:\ExagoTemplates` and any themes located in `C:\ExagoThemes`. JSON file will be created in `D:\MyContent.json`.

```
FileSystemToJson.exe C:\ExagoReports C:\ExagoTemplates C:\ExagoThemes D:\MyContent.json
```

Sample output:

```
12:02:39 INFO - Export Starts
12:02:39 INFO - from:'C:\ExagoReports'
12:02:39 INFO - to:D:\MyContent.json
12:02:39 INFO - Loading from C:\ExagoReports
12:02:39 INFO - Loading from C:\ExagoTemplates
12:02:39 INFO - Loading from C:\ExagoThemes
```

##### Manually Editing the Intermediate JSON File

In some circumstances, customizing the intermediate JSON file may be desirable or needed to properly set permissions on the content in the destination database. The contents of the JSON file and an explanation of each element can be found in the [Intermediate JSON File](#Intermed) section of this topic.

##### Access Flags

In a file system storage mechanism, all users have access to all content without restriction. Access controls are determined by use of Roles. **FileSystemToJson** will accordingly grant all access to all content.

By default **FileSystemToJson** will set:

* **AccessFlags** to *1111111111111111* granting all access permissions.
* **ReportAccessList** to be empty.

Learn more in Review [Intermediate JSON File](#Intermed) and [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction).

##### Troubleshooting

A log file named `FileSystemToJson.log` is saved to **FileSystemToJson**‘s installation directory, typically `<WebApp>\bin.` Send this file to the Exago Support Dept when asking for assistance in troubleshooting this utility.

#### LoadReportsToDb

**LoadReportsToDb** is used for three different operations: *initialize*, *load* and *read*.

1. *Initialize* sets up the Storage Management database with the schema and default party types. It should be the first operation run on a new database.
2. *Load* interprets the contents of either an intermediate JSON file, a file system directory or cloud storage repository and loads their contents into the Storage Management database.
3. *Read* verifies a *Load* operation by reading the contents of the Storage Management database and displaying it in a hierarchical directory structure. Can also be called at any time to review the database’s content and default party types.

##### Command Line Structure

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The command line parameters need to be called in the order they are documented below.

```
LoadReportsToDb.exe {-t [Sqlite|Mysql|SqlServer|Oracle|Postgresql]} -c <connection string> {-d <driver name|Sqlite>} {-p <table-prefix>} {-o <timeout_in_seconds> } {-I} {-L <jsonFile>} {-D <directory>} {-W <cloudspec>} {-R}
```

##### Command Line Parameters

Table F — **LoadReportsToDb** Command Line Parameter Definitions

| Parameter | Description/Usage |
| --- | --- |
| -t <**Sqlite** | Mysql | SqlServer | Oracle | Postgresql> | Storage Management database type  Choose one of the following:   * ***Sqlite*** (default) * *Mysql* * *SqlServer* — Microsoft SQL Server * *Oracle* * *PostgreSQL* |
| -c <connection\_string> | Connection string to the Storage Management database. For SQLite, only the path and file name of the database file are required.  When connecting to a PostgreSQL Storage Management database, include `Unicode=true` in the connection string.  This parameter is required for all use of **LoadReportsToDb** |
| -d <driver\_name | **Sqlite**> | Driver to use for connection to the Storage Management database  Defaults to *SQLite* for SQLite (-t Sqlite). If not using SQLite, must be explicitly specified.  light bulb Use the applicable driver name from the **Admin Console** > TreeGeneral.png**General** > TreeGeneralNode.png**Database Settings**. |
| -p <prefix\_or\_schema> | An optional prefix for all Storage Management database tables. Review the [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema) topic for information.  This option can be used to add a table name prefix or a schema if it exists.  **Examples**:   1. `-p test_` will result in tables named *test\_content*, *test\_party\_type*, *test\_content\_access* and *test\_storage\_meta* 2. `-p dbo.` will result in tables named *dbo.content*, *dbo.party\_type*, *dbo.content\_access* and *dbo.storage\_meta* |
| -o <timeout\_in\_seconds> v2020.1.12+ | An optional integer value to be passed along to the database driver’s `CommandTimeout` property. It is up to the driver what to do with this value. It is important to note that each individual driver may implement the handling of this value differently. Therefore, its consequences may vary. The value must be greater than 0. |
| -I | Initialize operation Create the tables, load the default party types and setup the base configuration in the Storage Management database.  Initialize will create two new folders in the file structure: **Public** with *Everyone* permissions and **My Reports** with *User* permissions.  If **-t** is *Sqlite*, and the SQLite file does not exist at the connection string specified by **-c**, the file will be created. |
| -R | Read operation Read the “file structure” of the Storage Management database, and display it in a hierarchical format, similar to the operating system command `tree`.  Useful for verifying the contents of the database after a JSON load (-L), directory load (-D) or web load (-W) operation. |
| -L <path\_to\_json\_file> | Load operation (JSON) Read an intermediate JSON file created by **DatabaseToJson** or **FileSystemtoJson** and load its contents into the Storage Management database. Reports with duplicate IDs will be assigned new IDs and a [warning will be displayed](#Duplicat) to that affect. |
| -D <directory> | Load operation (Directory)  Read the report and other contents of the specified *directory* and load it into the Storage Management database. Bypasses the manual creation of the intermediate JSON file and reads the directory directly into the database.  Do not include the trailing slash at the end of the directory path.  light bulb If converting from File System storage, specify the **Report Path** here to directly load reports into the database from the legacy file system.  The Themes directory can also be read with the -D parameter.  Each directory to be imported must be prefixed with it’s own -D.  Reports with duplicate IDs will be assigned new IDs and a [warning will be displayed](#Duplicat) to that affect. |
| -W <cloudspec> | Load operation (Cloud/Web) Read the report and other contents of the cloud storage repository referenced by *cloudspec* and load it into the Storage Management Database. Bypasses the manual creation of the intermediate JSON file and reads the contents directly into the database.  light bulb If converting from Cloud storage, specify the [**Report Path**](https://devnet.logianalytics.com/hc/en-us/articles/5281644565527-Main-Settings#Report) here to directly load reports into the database from the cloud repository.  Reports with duplicate IDs will be assigned new IDs and a warning will be displayed to that effect. |

##### Common Usage Examples

**Upgrading to Storage Management in a test environment:** Initialize a SQLite database located at `D:\StorageMgmt.sqlite`, read the contents of a file system report repository located at `C:\ExagoReports` and any themes located in `C:\ExagoThemes` then load it into the SQLite database.

```
LoadReportsToDb.exe -c D:StorageMgmt.sqlite -I -D C:\ExagoReports -D C:\ExagoThemes
```

Sample output:

```
20:31:07 INFO  - LoadReportsToDb -c D:\StorageMgmt.sqlite -D C:\ExagoReports C:\ExagoThemes
20:31:07 INFO  - We are in 32bit mode
20:31:07 INFO  - Loading from C:\ExagoReports
20:31:16 WARN  - Duplicate Id found, e8382e37-53ae-4bcc-a804-11cbf448a9be, for Report 'General Reports\Dashboard', new id will be created
20:31:34 INFO  - Load Completed:Folder:17 Report:159 Template:1
20:31:34 INFO  - Execution Completed
```

**Upgrading to Storage Management from a cloud storage repository:** Initialize an Oracle database with default table names, read the contents of an Amazon S3 repository and load it into the database.

```
LoadReportsToDb.exe -t Oracle -d Oracle.DataAccess.Client -c "Data Source=(DESCRIPTION=(ADDRESS_LIST=(ADDRESS=(PROTOCOL=TCP)(HOST=myOracleServer)(PORT=1521)))(CONNECT_DATA=(SERVER=DEDICATED)(SERVICE_NAME=ORCL))); User Id=ORACLE_DB; Password=ORACLE_PASSWORD;"
 -W "pathtype=s3;region='myRegion';accesskey='myAccessKey';secretkey='mySecretKey';bucketname='myBucketName'"
```

**Upgrading to Storage Management with a MySQL database and different table names:** Initialize a MySQL database with table **prefix** *dukane*; read the contents of a file system report repository located at `C:\ExagoReports` and any themes located in `C:\ExagoThemes` then load it into the MySQL database.

```
LoadReportsToDb.exe -t Mysql -d Devart.Data.Mysql -c "Server=myServerAddress;Database=myDataBase;Uid=myUsername;Pwd=myPassword;" -p dukane_ -I -D C:\ExagoReports -D C:\ExagoThemes
```

Sample output:

```
11:05:29 INFO  - We are in 32bit mode
11:05:29 INFO  - Found Schema File at 'c:\Exago\Config\Other\StorageMgmtSchema.json'
11:05:29 WARN  - [ContentDatabase.DbQuery.GetFactory] Getting DbProviderFactory for 'Devart.Data.Mysql'
11:05:31 INFO  - Loading from C:\ExagoReports
11:05:32 WARN  - [ContentDatabase.DbQuery.GetFactory] Getting DbProviderFactory for 'Devart.Data.Mysql'
11:05:43 WARN  - Duplicate Id found, e8382e37-53ae-4bcc-a804-11cbf448a9be, for Report 'General Reports\Dashboard', new id will be created
11:06:11 WARN  - Duplicate Id found, fdfd25ea-8ea2-4205-a891-830ab8e449d5, for Report 'Reports\Sales Figures', new id will be created
11:06:23 INFO  - Load Completed:Folder:17 Report:159 Template:1
11:06:23 INFO  - Loading from C:\ExagoThemes
11:06:23 WARN  - [ContentDatabase.DbQuery.GetFactory] Getting DbProviderFactory for 'Devart.Data.Mysql'
11:06:36 INFO  - Load Completed:Theme:57
11:06:36 INFO  - Execution Completed
```

**Load an intermediate JSON file into an existing Storage Management database:** Load an intermediate JSON file created by **FileSystemToJson** located at `<WebApp>\bin\FileSystem.json` to a Microsoft SQL Server database that has already been initialized.

```
LoadReportsToDb -t SqlServer -d System.Data.SqlClient -c "Server=myServerAddress;Database=myDataBase;User Id=myUsername;Password=myPassword;" -L FileSystem.json
```

**Verify the contents of an intermediate JSON file has been loaded correctly into a MySQL database:**

```
LoadReportsToDb -t Mysql -d Devart.Data.Mysql -c "Server=myServerAddress;Database=myDataBase;Uid=myUsername;Pwd=myPassword;" -R
```

Sample output:

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Standard Reports are the legacy name for Advanced Reports. CrossTabs are also considered Advanced Reports.

```
11:48:05 INFO  - LoadReportsToDb -c D:StorageMgmt.sqlite -R
11:48:05 INFO  - We are in 32bit mode
11:48:05 INFO  - Report Contents of Database

Advanced Reports (Inherit:False DefaultPartyType:Everyone)
|--Advanced Report (Blank) (Standard, Everyone)
|--Advanced Report (Blank) (Standard, User)
|--Advanced Report 1 (Standard, Everyone)
|--Advanced Report 1 (Standard, User)
|--Exports (Inherit:True DefaultPartyType:User)
|  |--onlyExportToAllExceptPDF (Advanced, User)
|  |--onlyExportToCSV (Standard, User)
|  |--onlyExportToPDF (Standard, User)
|  |--onlyExportToRTF (Standard, User)
|  |--onlyExportToXLS (Standard, User)
Chained Reports (Inherit:False DefaultPartyType:Everyone)
|--Chained Report With Prompt (Chained, Everyone)
|--For Exports (Inherit:True DefaultPartyType:User)
|  |--exportTypeAllExceptPDF (Chained, User)
|  |--exportTypeCSVOnly (Chained, User)
|  |--exportTypePDFOnly (Chained, User)
|  |--exportTypeRTFOnly (Chained, User)
|  |--exportTypeXLSOnly (Chained, User)
Chart Tests (Inherit:True DefaultPartyType:User)
|--Charting (Inherit:False DefaultPartyType:Everyone)
|  |--4+ Charts (Standard, Everyone)
|  |--Bar Chart (Standard, Everyone)
|  |--Bubble Chart (Standard, Everyone)
|  |--Revenue by Employee by Month (Standard, Everyone)
|  |--YTD (Standard, Everyone)
|--Geocharts (Inherit:False DefaultPartyType:Everyone)
|  |--Geocharts Report (Standard, Everyone)
|  |--Geocharts Report No Map (Standard, Everyone)
|--Google Map (Inherit:False DefaultPartyType:Everyone)
|  |--Google Map Report 1 (Standard, Everyone)
|  |--Google Map Report with Custom Aggregates (Standard, Everyone)
Charting (Inherit:False DefaultPartyType:Everyone)
|--4+ Charts (Standard, Everyone)
|--Bar Chart (Standard, Everyone)
|--Bubble Chart (Standard, Everyone)
|--Charting Report (Standard, Everyone)
|--Column Chart (Standard, Everyone)
|--Line Chart (Standard, Everyone)
|--MinimumGauge (Standard, Everyone)
|--MultiAxis Chart (Standard, Everyone)
|--Multi-Series Pie Chart (Standard, Everyone)
|--Pseudo CrossTab Chart (Standard, Everyone)
|--Revenue by Employee by Month (Standard, Everyone)
|--YTD (Standard, Everyone)
```

##### Duplicate ID Warning

If during the loading operation duplicate report IDs are found, the **LoadReportsToDb** will display a warning similar to the one below:

```
20:31:16 WARN - Duplicate Id found, e8382e37-53ae-4bcc-a804-11cbf448a9be, for Report 'General Reports\Dashboard', new id will be created
```

While not an indication of failure,  duplicate IDs could cause **Scheduler Services** to lose track of the report. This would mean the next time a report is saved, the change will not be pushed to all of the Scheduler Services, or the wrong report will be pushed to them.

To remedy this:

1. Search for and delete the duplicate GUIDs from each Scheduler Service’s working directory.
2. Re-schedule the report in the application.

The location of the working directory can be found in the Scheduler Service’s configuration file. See [Scheduler Service Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281627554583-Scheduler-Service-Configuration).

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Re-scheduling is only required when warnings about duplicated IDs appear, not for every report schedule in a system.

##### Troubleshooting

A log file named `LoadReportsToDb.log` is saved to **LoadReportToDb**‘s installation directory, typically `<WebApp>\bin.` Send this file to the Exago Support Dept when asking for assistance in troubleshooting this utility.

## Upgrading from File System or Cloud Storage

![Storage_Management_Graphic_Integration_Cloud_Repository__1_.png](https://devnet.logianalytics.com/hc/article_attachments/5432175742487/storage_management_graphic_integration_cloud_repository__1_.png)

or

![File_System_Storage_Quick_Integration.png](https://devnet.logianalytics.com/hc/article_attachments/5432227890711/file_system_storage_quick_integration.png)

or

![Cloud_Storage_Storage_Quick_Integration.png](https://devnet.logianalytics.com/hc/article_attachments/5432209846423/cloud_storage_storage_quick_integration.png)

This section will describe a generic step-by-step process to upgrade an existing legacy file system or cloud storage implementation to Exago’s Storage Management system.

Access rights will be imported with global (everyone) access.

1. Identify the location of the Reports, Themes and Templates.
2. Backup the contents of the legacy storage mechanism.
3. Create the destination Storage Management database. User permissions can be found in the [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema) topic. If using SQLite, skip this step.
4. Run [**LoadReportsToDb**](#LoadRepo) with the applicable command line parameters as described above. To load report and chart themes, be sure to include the path to the themes directories.
5. Verify the load operation completed correctly by running `LoadReportsToDb -R` (along with any database specific parameters as applicable). The output will show the directory structure stored in the database.
6. Navigate to ![TreeStorageMgmt.png](https://devnet.logianalytics.com/hc/article_attachments/5432175848087/treestoragemgmt.png)**Storage Management** within the **Admin Console**. Refer to [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management) for an explanation of what each of these settings is and what values to provide.
   1. Set the **Database Type**, **Database Provider** and **Database Connection**.
   2. Set the **Tables** names.
   3. Click the **Check Database Settings** button to make sure Exago can connect to the Storage Management database and that the schema is correct.
   4. Set the values of the four **Identity** keys if desired. Since **FileSystemToJson** or **LoadReportsToDb -D** will use `system` for the owner ID during import, we suggest using `system` as the value for **Owner ID** in the Admin Console for file system replacements.
   5. Set the **Default Settings** for access rights if desired. To emulate the previous file system behavior, review the suggestions in the [Emulating a Legacy Storage Mechanism](https://devnet.logianalytics.com/hc/en-us/articles/5281653081111-Storage-Management-Getting-Started#Emulatin).
   6. Set the **Cache Settings** if desired.
7. Update any API integration code to account for the Storage Management identity keys as the application is entered.
8. Load the Exago Web Application to verify that it loads without errors and that:
   * users are seeing the correct folders and reports
   * users are *not* seeing folders and reports that they should not have access to
   * themes are available to the ExpressView Designer, Advanced Report Designer, CrossTab Designer, Charts and GeoCharts
   * template files are available to their corresponding reports

Transition to Storage Management is now complete.

## Upgrading from Folder Management

This section will describe a generic step-by-step process to upgrade an existing folder management implementation using Exago’s folder management example to the new Storage Management system.

If you need more product information, including new purchases and upgrades, contact your Exago Customer Success Manager.

Access rights will be imported to match the folder management implementation.

1. Backup the existing folder management database.
2. Create or edit the `<WebApp>\bin\DatabaseToJson.config.json` file with the parameters to match the source database schema.
3. Run [**DatabaseToJson**](#Database) to generate an intermediate JSON file.
4. Create the destination Storage Management database. User access permissions can be found in [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema). If using SQLite, skip this step.
5. Run [**LoadReportsToDb**](#LoadRepo) with the applicable command line parameters as described above. To load report and chart themes, be sure to include the path to the themes directories.
6. Verify the load operation completed correctly by running `LoadReportsToDb -R` (along with any database specific parameters as applicable). The output will show the directory structure stored in the database.Configure Exago to use the Storage Management database with the **Admin Console**. Navigate to **Storage Management** within the Admin Console. Refer to the Storage Management topic in the Admin Console section for an explanation of what each of these settings is and what values to provide.
   1. Set the **Database Type**, **Database Provider** and **Database Connection**.
   2. Set the **Tables** names.
   3. Click the **Check Database Settings** button to make sure Exago can connect to the Storage Management database and that the schema is correct.
   4. Set the values of the four **Identity** keys if desired.
   5. Set the **Default Settings** for access rights if desired. To emulate the previous Folder Management behavior, review the suggestions in [Emulating a Legacy Storage Mechanism](https://devnet.logianalytics.com/hc/en-us/articles/5281653081111-Storage-Management-Getting-Started#Emulatin)
   6. Set the **Cache Settings** if desired.
7. Update any API integration code to account for the Storage Management identity keys as the application is entered.
8. Load the Exago Web Application to verify that it loads without errors and that:
   * users are seeing the correct folders and reports
   * users are *not* seeing folders and reports that they should not have access to
   * themes are available to the ExpressView Designer, Advanced Report Designer, CrossTab Designer, Charts and GeoCharts
   * template files are available to their corresponding reports

Transition to Storage Management is now complete.

## Upgrading from Web Service (SOAP) Storage

If you need more product information, including new purchases and upgrades, contact your Exago Customer Success Manager.

## Piecemeal Transition

To transition a small number of reports (for example one at a time), use the **Download** and **Upload** capability in the Report Tree of the Web Application user interface.

1. Enable **Admin Console** > **General** > **Feature/UI Settings** > **Show Report Upload/Download Options** in both the legacy version and the *v2020.1+* version.
2. In the legacy installation, right-click the report and choose ![Download.png](https://devnet.logianalytics.com/hc/article_attachments/5432193118615/download.png)**Download** to save the report definition to the local computer.
3. In the *v2020.1+* installation, right-click the desired destination folder and choose ![Upload.png](https://devnet.logianalytics.com/hc/article_attachments/5432174691991/upload.png)**Upload** to upload the report definition to the application.

## Intermediate JSON File

The **CloudToJson**, **FileSystemToJson** and **DatabaseToJson** utilities create an intermediate JSON file defining the contents of their respective source storage mechanism. A sample JSON file generated by **FileSystemToJson** defining a single folder named “My Folder” containing a single report named “test” is shown below. A Microsoft Excel template file is also included.

Editing of this file may be necessary to customize permissions or other parameters before loading into the database. The file’s location is determined by the utility used. Review the sections above for details.

A definition of the structure of the file is detailed in [Structure](#Structur)

```
[
  {
    "OwnerId": null,
    "CreatedBy": null,
    "ModifiedBy": null,
    "CreatedDate": "2020-02-21T11:18:36.0473673-05:00",
    "ModifiedDate": "2020-02-21T11:19:20.3949126-05:00",
    "IsDeleted": false,
    "Metadata": {
      "SortOrder": null,
      "ContentXML": null,
      "ContentData": null,
      "AccessFlags": 65535,
      "ExtendedAttributes": null,
      "FullName": "My Folder",
      "ContentId": "c242735e-34d5-40ab-901c-9849d1790998",
      "ParentId": "00000000-0000-0000-0000-000000000000",
      "IsFolder": true,
      "IsReport": false,
      "ReportType": 0,
      "ContentType": 1,
      "Name": "My Folder",
      "Attribute": null,
      "Folder": "",
      "Description": null,
      "Path": "C:\ExagoReports\Reports\My Folder",
      "AllowedOutputTypes": 0,
      "ClientData": null,
      "ExtensionData": null,
      "AllowOutputHtml": false,
      "AllowOutputPdf": false,
      "AllowOutputCsv": false,
      "AllowOutputExcel": false,
      "AllowOutputRtf": false,
      "CanRename": true,
      "CanShare": true,
      "IsReadOnly": false
    },
    "ReportAccessList": [],
    "Children": [
      {
        "OwnerId": null,
        "CreatedBy": null,
        "ModifiedBy": null,
        "CreatedDate": "2020-02-21T11:17:07.8474847-05:00",
        "ModifiedDate": "2019-10-08T14:52:07.8892432-04:00",
        "IsDeleted": false,
        "Metadata": {
          "SortOrder": null,
          "ContentXML": "==REPORT XML DEFINITION TEXT APPEARS HERE==",
          "ContentData": null,
          "AccessFlags": 65535,
          "ExtendedAttributes": null,
          "FullName": "My Folder\test",
          "ContentId": "784b1167-c0f9-42f8-8045-a2b690cf9d9a",
          "ParentId": "c242735e-34d5-40ab-901c-9849d1790998",
          "IsFolder": false,
          "IsReport": true,
          "ReportType": 0,
          "ContentType": 0,
          "Name": "test",
          "Attribute": null,
          "Folder": "My Folder",
          "Description": "",
          "Path": "C:\ExagoReports\Reports\My Folder\test.wr",
          "AllowedOutputTypes": 31,
          "ClientData": null,
          "ExtensionData": null,
          "AllowOutputHtml": true,
          "AllowOutputPdf": true,
          "AllowOutputCsv": true,
          "AllowOutputExcel": true,
          "AllowOutputRtf": true,
          "CanRename": true,
          "CanShare": true,
          "IsReadOnly": false
        },
        "ReportAccessList": [],
        "Children": [],
        "OriginalId": null
      }
    ],
    "OriginalId": null
  },
  {
    "OwnerId": null,
    "CreatedBy": null,
    "ModifiedBy": null,
    "CreatedDate": "2020-02-20T13:20:31.5527279-05:00",
    "ModifiedDate": "2020-02-20T13:20:31.5527279-05:00",
    "IsDeleted": false,
    "Metadata": {
      "SortOrder": null,
      "ContentXML": null,
      "ContentData": "==BINARY TEMPLATE FILE CONTENT APPEARS HERE==",
      "AccessFlags": 65535,
      "ExtendedAttributes": null,
      "FullName": "MyTemplate8.xlsx",
      "ContentId": "7d2f0719-c12e-41d9-9804-c4e18e7b65d6",
      "ParentId": "00000000-0000-0000-0000-000000000000",
      "IsFolder": false,
      "IsReport": false,
      "ReportType": 0,
      "ContentType": 3,
      "Name": "MyTemplate8.xlsx",
      "Attribute": null,
      "Folder": "",
      "Description": null,
      "Path": "C:\ExagoReports\Reports\MyTemplate8.xlsx",
      "AllowedOutputTypes": 0,
      "ClientData": null,
      "ExtensionData": null,
      "AllowOutputHtml": false,
      "AllowOutputPdf": false,
      "AllowOutputCsv": false,
      "AllowOutputExcel": false,
      "AllowOutputRtf": false,
      "CanRename": true,
      "CanShare": true,
      "IsReadOnly": false
    },
    "ReportAccessList": [],
    "Children": [],
    "OriginalId": null
  }
]
```

### Structure

The intermediate JSON file contains an array of **Content** objects.

#### Content JSON

Table G — Content JSON Structure

| Name | Type | Description |
| --- | --- | --- |
| OwnerID | string | The user ID of the user who is the owner of this content item. The value of this column is read from a folder management database. For file system and cloud imports, this value will be `null`. |
| CreatedBy | string | The user ID of the user who created this content item. The value of this column is read from a folder management database. For file system and cloud imports, this value will be `null`. |
| ModifiedBy | string | The user ID of the user who last saved modified this content item. The value of this column is read from a folder management database. For file system and cloud imports, this value will be `null`. |
| CreatedDate | string | Timestamp indicating the date, time and time zone offset when **CreatedBy** created this content item. |
| ModifiedDate | string | Timestamp indicating the date, time and time zone offset when **ModifiedBy** modified this content item. |
| IsDeleted | Boolean | Indicates whether or not this item is to be marked as deleted for all users. For file system and cloud imports, this value will be always be `false`. |
| MetaData | [MetaData](#MetaData) | A JSON object that represents the metadata for this content item. See **Table H** below. |
| ReportAccessList | array of [ReportAccessItem](#ReportAc) objects | An array of **ReportAccessItem** JSON objects which set the accessibility of this content item. See **Table I** below. |
| Children | array of [Content](#Content) objects | If this content item is a container for other items (that is it is a folder), this is an array of the **Content** JSON items that are contained in the folder. |
| OriginalId | String | The ID of this content item as referred to by the legacy storage system. For file system and cloud imports, this value will be `null`. |

#### MetaData JSON

The contents of this JSON object closely mimic the fields in the Storage Management database’s [Content](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema#Content) and [Content Access](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema#Content2) tables.

Table H — MetaData JSON Structure

| Name | Type | Description |
| --- | --- | --- |
| SortOrder | string | This field is for future use and is not yet implemented. Value will always be `null`. |
| ContentXML | string | If this content item is a report or a theme, then its XML content will be stored as text in this column. |
| ContentData | string | If this content item is a template file or other binary object, an ASCII representation of the file contents will be stored in this field. |
| AccessFlags | integer | If **ReportAccessList** is empty, a bitmap indicating which access permissions are allowed for the content item, where *1* indicates the action is permitted and *0* indicates the action is not permitted.  If **ReportAccessList** is not empty, then the AccessFlags of each **ReportAccessItem** object will determine permissions.  See [access\_flags v2021.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema#access_f) for more information and examples. |
| ExtendedAttributes | string | This field is reserved for use by Exago clients, for storing metadata about content as they see fit in their custom implementation. Value will always be `null`. |
| FullName | string | The name of the content item, including it’s path from the root.  For example, for a report named *test* in a folder named *My Folder*, this field would be “*My Folder\test*“ |
| ContentId | string | A GUID representing this content item in the destination Storage Management database. |
| ParentId | string | If **ReportAccessList** is empty, a GUID representing the ContentId field of this item’s parent. For example, for a report this would be the GUID of the folder containing it.  If *00000000-0000-0000-0000-000000000000*, this item is in the root.  If **ReportAccessList** is not empty and this content item is a report, this field is ignored. |
| IsFolder | Boolean | Indicates if this content item represents a folder. *True* if it is a folder, *False* if it is not. |
| IsReport | Boolean | Indicates if this content item is a report. *True* if it is a report, *False* if it is not. |
| ReportType | [wrReportType](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#wrReport) | If **IsReport** is *True*, this value represents the type of report this item is. |
| ContentType | integer | The type of content this item represents. See [Storage Management: Database Schema, content Table, content\_type Column](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema#content_) for more information and examples. |
| Name | string | The name of this content item. For example, for a report named *test* in a contained folder named *My Folder*, this column would be “*test*“ |
| Attribute | string | If this content item represents a chart or report theme, this column describes the type of chart or report that it applies to. For example, *Map* or *CrossTab*. |
| Folder | string | The name of the folder this content item is contained in. For example, for a report named *test* in a contained folder named *My Folder*, this column would be “*My Folder*“ |
| Description | string | The description text assigned to a report when it is saved. |
| Path | string | The absolute file system location pointing to this content item prior to import.  For example, for a report named *test* contained in a folder named *My Folder*, this column would be “*C:\ExagoReports\My Folder\test.wr”* |
| AllowedOutputTypes | integer | A bitmap indicating which export types are allowed for the content item, where *1* indicates an export type is permitted and *0* indicates an export type is not permitted.  See [Storage Management: Database Schema, content Table, exports\_allowed Column](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema#exports_) for more information. |
| ClientData | String | Content of the UDF metadata string from a custom folder management implementation. |
| ExtensionData | String | This field is for future functionality and is not implemented yet. |
| AllowOutputHtml | Boolean | Deprecated. This column will not be read during the import process. Instead, set access permissions with the **AllowedOutputTypes**. |
| AllowOutpoutPdf | Boolean | Deprecated. This column will not be read during the import process. Instead, set access permissions with the **AllowedOutputTypes**. |
| AllowOutputCsv | Boolean | Deprecated. This column will not be read during the import process. Instead, set access permissions with the **AllowedOutputTypes**. |
| AllowOutputExcel | Boolean | Deprecated. This column will not be read during the import process. Instead, set access permissions with the **AllowedOutputTypes**. |
| AllowOutputRtf | Boolean | Deprecated. This column will not be read during the import process. Instead, set access permissions with the **AllowedOutputTypes**. |
| CanRename | Boolean | Deprecated. This column will not be read during the import process. Instead, set access permissions with the **AccessFlags**. |
| CanShare | Boolean | Deprecated. This column will not be read during the import process. Instead, set access permissions with the **AccessFlags**. |
| IsReadOnly | Boolean | Deprecated. This column will not be read during the import process. Instead, set access permissions with the **AccessFlags**. |

#### ReportAccessItem JSON

**LoadReportsToDb** will generate Content Access table entries based on these ReportAccessItems.

Table I — ReportAccessItem JSON Structure

| Name | Type | Description |
| --- | --- | --- |
| Parent | string | Id of the content item that this item appears as a child to. |
| PartyTypeId | integer | Refer to [Storage Management: Database Schema Table D](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema#Party). |
| PartyId | string | The value of the corresponding identity key that this **ReportAccessItem** controls.  For example, if **PartyTypeId** is *4*, this is the value of UserId for which the **AccessFlags** will apply. |
| SortOrder | string | Content is sorted first by the value in this column, then by name (case in-sensitive). |
| AccessFlags | integer | A bitmap indicating which access permissions are allowed for the content item, where *1* indicates the action is permitted and *0* indicates the action is not permitted.  See [Storage Management: Database Schema, content\_access Table, access\_flags Column](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema#Content2) for more information and examples. |
