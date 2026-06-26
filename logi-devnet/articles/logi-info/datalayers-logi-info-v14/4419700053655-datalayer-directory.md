---
title: "DataLayer.Directory"
id: 4419700053655
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419700053655-DataLayer-Directory
updated_at: 2022-07-17T02:03:51Z
---

# DataLayer.Directory

# DataLayer.Directory

The **DataLayer.Directory** element provides developers with information about the files and folders in a specified directory.

The following sections are covered in this topic:

* About DataLayer.Directory
* [Attributes](#Attributes)
* [Working with DataLayer.Directory](#WorkingWith)

  

## About DataLayer.Directory

DataLayer.Directory provides the directory information for a specific folder and/or its contents. The results, in the usual datalayer tabular format, includes information such as file name, type, size, and creation date.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) This datalayer returns the directory information stored in the file system for a single folder; it does not *search* folders for files nor traverse sub-folders.

To get the information for multiple sub-folders, you can use several of these elements together under a Data Table, for example, and their results will be automatically joined together (Union) to produce a single data set. This is useful when the names of the sub-folders to be examined are known in advance.

## Attributes

The DataLayer.Directory element has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | Specifies an optional element ID. Recommended for easier identification when debugging. |
| Directory Filter | Specifies a filters for the results, based on a complete filename or a filename that includes the standard "wild card" characters (\* and ?). The default value is: \*.\* |
| Directory Folder | Specifies a fully-qualified file path for a folder to be read. Tokens may be used here. Examples:   C:\inetpub\wwwroot\yourLogiApp\\_Themes @Function.AppPhysicalPath~\\_Definitions\\_Reports The asterisk wild card character ("\*") may be used here to specify folder names. The default value is your application's rdDataCache folder. |
| Directory Type | Specifies the type of directory information to return:  *FilesAndFolders* = (Default) Returns information about both files and folders. *FilesOnly* = Returns information about files only. *FoldersOnly* = Returns information about folders only. |

  

## Working with DataLayer.Directory

The datalayer reads the file system directory information for the specified folder, filters it based on the **Directory Filter** attribute value (if any), and caches it as rows and columns, with one row per file or folder. Data retrieved into the datalayer is cached in XML format.

The data retrieved with a datalayer is available using @Data tokens, in the format @Data.*ColumnName*~. The spelling of column names are *case-sensitive*.

The data retrieved is only available within the scope of the parent element of the datalayer, not throughout the entire report definition. The DataLayer.Linked element can be used to make the data reusable in another datalayer outside this scope.

The datalayer will be populated with these column names, for use with @Data tokens:

| Column | Description |
| --- | --- |
| Name | The simple name of the file or folder, with the file extension. Example:  *myFile.xml* |
| PhysicalName | The fully-qualified path and name of the file or folder. Example: *C:\inetpub\wwwroot\myLogiApp\\_SupportFiles\myFile.xml* |
| Type | The item type, either *File* or *Folder* |
| Size | The item size, in bytes. Folders report a value of *0*. |
| DateModified | The time stamp indicating when the item was last modified. Example: *6/8/2016 2:25:12 PM* |
| DateCreated | The time stamp indicating when the item was created.  Example: *6/8/2016 2:25:12 PM* |
| Extension | The file extension, if any, with leading period. Example: *.xml* |
| NameOnly | The file or folder name without file extension. Example: *myFile* |
| ParentFolder | The name of the folder thatcontains this file or folder. |

File access permissions may need to be granted to the account that your Logi application runs under on the web server in order to read data with DataLayer.Directory, especially if the files or folders are not within your Logi application folder.

The data retrieved into the datalayer can be viewed by turning on the Debugger in the \_Settings definition (General element) and using the resulting icon at the bottom of the report page to view the **Application Trace** page. A link on the Trace page will display the retrieved data.
