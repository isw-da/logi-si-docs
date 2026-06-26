---
title: "Moving Files Between Storage Management Databases"
id: 5281638646807
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281638646807-Moving-Files-Between-Storage-Management-Databases
updated_at: 2022-05-03T22:07:48Z
---

# Moving Files Between Storage Management Databases

# Moving Files Between Storage Management Databases

Exago recommends using a three-environment development, quality assurance and production paradigm. In this structure, it is often desirable to maintain unique Storage Management databases for each environment. Use the **ImportExportStorageMgmt** command line utility, available in *v2020.1.17+* and *v2021.1.5+,* to transition one SM database to another.

Unlike the [DatabaseToJson](https://devnet.logianalytics.com/hc/en-us/articles/5281647090839-Storage-Management-Transitioning-from-Legacy-Storage-Methods#Database) legacy transitioning utility, **ImportExportStorageMgmt** creates a JSON file **for each** content item in the database named with its content\_id. These files can then be easily backed up or version controlled.

As its name implies, **ImportExportStorageMgmt** supports two different operations:

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> **ImportExportStorageMgmt** requires that the primary keys from Exago’s factory implementation of Storage Management are in the database. If the primary keys have been changed, an alternate method of transitioning must be used.

* **Export** — read the contents of an existing Storage Management database and output a JSON file for each content item. Filters can be applied to include or exclude certain folders as desired. All columns, including custom columns will be exported.
* **Import** — read the contents of a directory of JSON files (created during an Export) and load each one into a target database. If an item already exists in the target, update it. Imports are completed in two steps: first for content table records, then for content access table records.
  > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
  >
  > The target database must be initialized before **ImportExportStorageMgmt** can import into it. Use the Admin Console’s **Prepare Database** button; execute the statements returned with the **Show Prepare Data** button; or call the **LoadReportsToDb** utility with the `-I` parameter to accomplish this.

## Configuration File

Before handling any data, **ImportExportStorageMgmt** must know how to access the source and target databases, where to store the JSON files and any filtering options desired. These settings are contained in a JSON **configuration** file.

There may be more than one configuration file created ahead of time, as ImportExportStorageMgmt allows specifying a configuration file at runtime.

### File Structure

A sample of a configuration file is below. Tables A and B below the sample define the different components.

```
{
    "SourceDb":
    {
        "DbType":"SQLite",
        "DbProvider":"SQLite",
        "ConnectionString":"DataSource=D:\ImportExport.sqlite",
        "TablePrefix":"dev_"
    },
     "TargetDb":
    {
        "DbType":"MySQL",
        "DbProvider":"devart.data.mysql",
        "ConnectionString":"Unicode=true; User ID=xxxxxx;Password=xxx;Host=xxx;Database=file system",
        "TablePrefix":"prod_"
    },
    "JsonDirectory":"c:\exago\export\Json",
    "BlockList" : [
        "Public",
        "Hidden"
    ],
    "AllowList" : null,
    "AutoMatch" : [
        "Public",
        "My Reports"
    ],
    "FieldSpecification": {
	"created_date" : "datetime",
	"modified_date" : "datetime",
	"bit_content" : "bytearray"
	}
}
```

Table A — **ImportExportStorageMgmt** Configuration File JSON Definition

| Name | Type | Description |
| --- | --- | --- |
| SourceDb | [Database Definition](#Table) | Source database from which to copy content during an Export operation. |
| TargetDb | [Database Definition](#Table) | Destination database where content is copied to during an import operation. |
| JSONDirectory | string | File system directory where the JSON files are exported (saved) to, and imported (read) from. |
| BlockList | array of string | List of root folders (those at the top level of the Report Tree) to exclude from an export operation. During export, content access records that refer to folders on the BlockList will not be written if that content only exists in a blocked folder. To block no folders, set to `null`. light bulb To import/export the entire Report Tree, leave both **BlockList** and **AllowList** as `null`. |
| AllowList | array of string | List of folders to include in the export operation. During export, content access records will be written only if content exists in one of the AllowList folders and the AllowList is not empty. To allow all folders, set to `null`. light bulb To import/export the entire Report Tree, leave both **BlockList** and **AllowList** as `null`. |
| AutoMatch | array of string | To match a root folder by *name* instead of *content ID*, provide the name of that folder in this list. The first folder in the target database with the same name in the source database will be assumed to be the same folder. |
| FieldSpecification | JSON object with key/value pairs | Use to identify the names of *datetime* or *bytearray* columns in the database. Use the column name as the key and the data type, either *datetime* or *bytearray* as the value.  Special handling for fields is performed when a field’s name matches one specified in the list. |

Table B — **Database Definition** JSON Definition

| Name | Type | Description |
| --- | --- | --- |
| ConnectionString | string | Connection string to connect to the database |
| DbType | string | The type of source database. Must be one of the following:  * *Sqlite* * *Mysql* * *SqlServer* — Microsoft SQL Server * *Oracle* * *PostgreSQL* |
| DbProvider | string | Driver to use for connection to the source database light bulb Use the applicable driver name from the **Admin Console** > **General** > **Database Settings**. |
| TablePrefix | string | Table prefix in the database, if applicable. If no prefix is needed, set to `null`. |

## Command Line

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

By default **ImportExportStorageMgmt** is located in `<WebApp>/bin`. Configuration files will be saved to the current directory.

### Structure

Optional command line parameters are enclosed in { braces }. The utility processes the command line parameters in the order they are entered, and may be combined into multiple actions with a single call. When combing actions, they must appear in the order presented below:

```
ImportExportStorageMgmt {-h} -f <configFile> {-E} {-I}
```

### Parameters

Table C — **ImportExportStorageMgmt** Command Line Parameter Definitions

| Parameter | Description/Usage |
| --- | --- |
| -f <configFile> | The name and path of the configuration file to use. If the file is not found, the utility will create a default configuration file at this location. |
| -E | Perform an export operation from the <configFile>’s `SourceDb` |
| -I | Perform an import operation to the <configFile>’s `TargetDb` |
| -h | Display help message with the command line structure |

### Common Usage Examples

**Create a new configuration file:** So long as the file name following the -f does not exist, the utility will create a sample configuration file with that name. This example will create a new configuration file named `Dev-to-Prod.json` in **ImportExportStorageMgmt**‘s installation directory.

```
ImportExportStorageMgmt.exe -f Dev-to-Prod.json
```

Sample Output

```
11:12:04 INFO  - ExportStorageMgmt -f Dev-to-Prod.json
11:12:04 ERROR - Specified configuration file not found - I'll try and create one for you
11:12:04 INFO  - Created Config File at Dev-to-Prod.json
```

**Transfer a single database from one to another:** The configuration defines a single source and a single target database.

```
ImportExportStorageMgmt.exe -f Dev-to-Prod.json -E -I
```

**Export multiple databases, import to a single database:** Define the separate source databases in different configuration files. They must reference the same **JSONDirectory**. Define the target database in the last configuration file. Perform an export operation on all databases, but only a single import on the last one. Since the import operation reads all of the contents of the **JSONDirectory** the contents of all previously exported databases will be imported.

```
ImportExportStorageMgmt.exe -f Dev-to-Prod.json -E -f QA-to-Prod.json -E -I
```

Sample Output

```
14:27:41 INFO  - ExportStorageMgmt -f Dev-to-Prod.json -E -f QA-to-Prod.json -E -I
14:27:41 INFO  - Starting Export
14:27:43 INFO  - Processing Complete, write 1534 records
14:27:43 INFO  - Exported 1136 records of type 0
14:27:43 INFO  - Exported  251 records of type 1
14:27:43 INFO  - Exported  132 records of type 2
14:27:43 INFO  - Exported   15 records of type 3
14:27:43 INFO  - Starting Export
14:27:45 INFO  - Processing Complete, write 860 records
14:27:45 INFO  - Exported  616 records of type 0
14:27:45 INFO  - Exported  124 records of type 1
14:27:45 INFO  - Exported  100 records of type 2
14:27:45 INFO  - Exported   20 records of type 3
14:27:45 INFO  - Starting Import
14:29:03 INFO  - AutoMatch for Public 7da64126-c96c-471d-a3c1-5f6060b2a812=>afe754e9-4439-459a-90ab-b6981ebf3825
14:30:10 INFO  - AutoMatch for Public e62df5d8-8228-4839-a87d-2000179f9ff0=>afe754e9-4439-459a-90ab-b6981ebf3825
14:30:18 INFO  - AutoMatch for My Reports f3d0dad0-9a5d-49d5-99b3-6c2de8285237=>843e95d0-74c0-414b-b4eb-5a1dfdd96bb7
14:30:19 INFO  - AutoMatch for My Reports f6aea47e-b24b-46ca-83ac-98a443c6c3c9=>843e95d0-74c0-414b-b4eb-5a1dfdd96bb7
14:30:23 INFO  - AutoMatch for My Reports fcf2b618-034c-417d-9688-6326b38d9632=>843e95d0-74c0-414b-b4eb-5a1dfdd96bb7
14:30:25 INFO  - Completed Loading Content Records: Inserted 2389 content records, and updated 0 content records
14:33:03 INFO  - Completed Loading Access Records: Inserted 2708 access records, and updated 0 access records
14:33:03 INFO  - No Orphan Records Located
```

## Troubleshooting

The `ImportExportStorageMgmt.log` log file is saved to **ImportExportStorageMgmt**‘s installation directory. Send this file to the Exago Support Team when asking for assistance in troubleshooting this utility. The log file contains additional DEBUG lines with SQL statements not included in the console.

A sample log is below, without the DEBUG lines:

```
08:42:27 INFO  - ExportStorageMgmt -f MySMConfigFile.json -E -I
08:42:27 INFO  - Starting Export
08:42:29 INFO  - Processing Complete, write 851 records
08:42:29 INFO  - Exported  608 records of type 0
08:42:29 INFO  - Exported  123 records of type 1
08:42:29 INFO  - Exported  100 records of type 2
08:42:29 INFO  - Exported   20 records of type 3
08:42:29 INFO  - Starting Import
08:43:27 INFO  - AutoMatch for My Reports f3d0dad0-9a5d-49d5-99b3-6c2de8285237=>f4fdd6d2-1c32-4bf9-bfbb-f13a1ecdc10b
08:43:30 INFO  - Completed Loading Content Records: Inserted 850 content records, and updated 0 content records
08:44:21 INFO  - Completed Loading Access Records: Inserted 859 access records, and updated 0 access records
08:44:21 INFO  - No Orphan Records Located
```

### Log File Contents

The **type** in each `Exported ___ records of type` line represents one of the Content Types from the [wrContentType enumeration](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#wrConten).

**AutoMatch** lines appear when a folder name in the AutoMatch list is matched, with the content ID of the folder in the source database and then the content ID of the folder in the target database.

**Completed** lines appear when each step of the import operation finishes. Inserts for new items are counted along with items that are updated.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
>
> Deleting content from the system doesn’t remove records from the database. Instead, either an update to the content or content access records will be made depending on who deleted the item. See [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction).

## JSON Files

The individual JSON files in the **JSONDirectory** represent a single record in the database’s content table. Each file is name with the record’s **content\_id**.

The file consists of two JSON components: one named **Content** and the other **Access** that correlate with the item’s content record and content\_access records. See [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema).

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The **Access** object has two additional properties not in the database: *parentname* and *contentname*. These are created by and for the use of the utility only.

### Sample Content Item JSON File

```
{
  "Content": {
    "content_id": "bcbac226-ded2-46ed-bc8b-62648c5ad0f1",
    "content_type": 0,
    "report_type": 2,
    "content_attribute": null,
    "name": "Executive Dashboard",
    "description": null,
    "text_content": "(the contents of a report WR file appears here)",
    "bit_content": null,
    "deleted_flag": false,
    "created_date": "2016-10-17T11:24:15",
    "created_by": "98871680-c7bc-421a-846a-cdcefaada47b",
    "modified_date": "2017-08-23T12:06:44",
    "modified_by": "98871680-c7bc-421a-846a-cdcefaada47b",
    "owner_id": "98871680-c7bc-421a-846a-cdcefaada47b",
    "exports_allowed": 0,
    "inherit_flag": false,
    "default_party_type_id": null,
    "extended_attributes": null,
    "default_access_flags": null,
    "default_export_type": null,
    "report_tree_shortcut_action": null,
    "use_cache_execution": null,
    "is_cache_valid": null,
    "associated_reports": null
  },
  "Access": [
    {
      "content_id": "bcbac226-ded2-46ed-bc8b-62648c5ad0f1",
      "parent_id": "b6d3f26a-0a58-4c7b-8616-9f670d43f9f7",
      "party_type_id": 1,
      "party_id": null,
      "sort_order": 0,
      "access_flags": 480,
      "child_inherits": false,
      "parentname": "Dashboards",
      "contentname": "Executive Dashboard"
    },
    {
      "content_id": "bcbac226-ded2-46ed-bc8b-62648c5ad0f1",
      "parent_id": "b6d3f26a-0a58-4c7b-8616-9f670d43f9f7",
      "party_type_id": 2,
      "party_id": "1",
      "sort_order": 0,
      "access_flags": 503,
      "child_inherits": false,
      "parentname": "Dashboards",
      "contentname": "Executive Dashboard"
    },
    {
      "content_id": "bcbac226-ded2-46ed-bc8b-62648c5ad0f1",
      "parent_id": "b6d3f26a-0a58-4c7b-8616-9f670d43f9f7",
      "party_type_id": 4,
      "party_id": "98871680-c7bc-421a-846a-cdcefaada47b",
      "sort_order": 0,
      "access_flags": 511,
      "child_inherits": false,
      "parentname": "Dashboards",
      "contentname": "Executive Dashboard"
    }
  ]
}
```
