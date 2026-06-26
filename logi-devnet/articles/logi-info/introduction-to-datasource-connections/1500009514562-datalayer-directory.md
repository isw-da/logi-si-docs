---
title: "DataLayer.Directory"
id: 1500009514562
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514562-DataLayer-Directory
updated_at: 2021-06-17T01:58:10Z
---

# DataLayer.Directory

# DataLayer.Directory

The **DataLayer.Directory** element provides developers with information about the files and folders in a specified directory.

* Attributes
* [Working with DataLayer.Directory](#WorkingWith)

This element is only available in Logi Info; it is *not available* in Logi Report.

## Attributes

The DataLayer.Directory element has the following attributes:

|  |  |
| --- | --- |
| **Attribute** | **Description** |
| ID | (Required through v10.1.46) Unique element ID. |
| Directory Filter | Filters the results based on a complete filename or a filename that includes the standard "wild card" characters (\* and ?). Default: \*.\* |
| Directory Folder | Fully-qualified file path of folder to be read. Example: C:\Temp Defaults to your application's rdDataCache folder. |
| Directory Type | The type of entries to included in the returned data: FilesAndFolders = Include both files and folders (default). FilesOnly = Return only information about files. FoldersOnly = Return only information about folders. |

## Work with DataLayer.Directory

The datalayer reads the directory data for the specified folder, filters it based on the Directory Filter attribute value (if any), and caches it as rows and columns, with one row per file or folder. Data retrieved into the datalayer is cached in **XML** format.

The data retrieved with a datalayer is available using @Data **tokens**, in the format @Data.*ColumnName*~. The spelling of the column name is **case-sensitive**. The data is only available within the **scope** of the **parent** element of the datalayer, not throughout the entire report definition. The DataLayer.Linked element can be used to make the data reusable in another datalayer outside this scope.

Valid "column names" available through the @Data token are:

| Column | Description |
| --- | --- |
| Name | Simple name of the file or folder, with the file extension, e.g. *myFile.txt* |
| PhysicalName | The fully-qualified path and name of the file or folder, e.g. *c:\myFolder\myFile.txt* |
| Type | Item type, either *File* or *Folder* |
| Size | Item size, in bytes. Folders report 0. |
| DateModified | Timestamp indicating when the item was last modified, e.g. *3/8/2008 2:25:12 PM* |
| DateCreated | Timestamp indicating when the item was created, e.g. *3/8/2008 2:25:12 PM* |
| Extension | File extension, if any, with leading period, e.g. *.txt* |
| NameOnly | File or folder name without file extension, e.g. *myFile* |
| ParentFolder | Name of the folder which contains this file or folder. |

  
File access **permissions** may need to be granted to the account that your Logi application runs under on the web server in order to read data with DataLayer.Directory, especially if the files or folders are not within your application folder. In Windows environments, these will be either the local ASPNET or NETWORK SERVICE accounts.

The data retrieved into the datalayer can be viewed by turning on the **Debugging Link** in the \_settings definition (General element) and using the resulting link at the bottom of the report page to view the **Application Trace** page. A link on the Trace page will display the retrieved data.
