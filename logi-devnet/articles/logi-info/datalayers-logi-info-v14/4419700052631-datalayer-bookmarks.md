---
title: "DataLayer.Bookmarks"
id: 4419700052631
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419700052631-DataLayer-Bookmarks
updated_at: 2022-07-17T02:03:52Z
---

# DataLayer.Bookmarks

# DataLayer.Bookmarks

The **DataLayer.Bookmarks** element is used specifically to retrieve saved bookmark information.

The following sections are covered in this topic:

* Attributes
* [Working with DataLayer.Bookmarks](#WorkingWith)

For more information, see [Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4419707675287-Bookmarks). Bookmark implementation examples can be found in our [Bookmarks Sample Application](https://devnet.logianalytics.com/hc/en-us/articles/360049424954-Bookmarks-Sample-Application).

## Attributes

The DataLayer.Bookmarks element has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | An optional element ID. Recommended for easier identification when debugging. |
| Bookmark Collection | (Required) Bookmarks are stored in XML data files, called a Bookmark Collection. These are located in a folder specified in the Bookmark Location attribute of the Settings definition's General element. This attribute sets the name of the collection; only the file name, without an extension, is entered here. Bookmarks can also be stored in a database. For more information, see the Storing Bookmark, Gallery, and SaveFiles in a Database section of [Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4419707675287-Bookmarks). A value is *not* required here if the General element's Bookmark Collection Default has been specified in the \_Settings definition. |

## Working with DataLayer.Bookmarks

This datalayer connects directly to the bookmark collection via the file system or, optionally in v12.5+, by querying a database. Unlike most datalayer elements, this one *does not* require aConnection
element. Bookmark information is retrieved and cached as rows and columns, with
one row per bookmark. Data retrieved into the datalayer is cached in XML
format.
The data retrieved with a datalayer is available using @Data tokens,
in the format @Data.*ColumnName*~ and the spelling of the column name is
case-sensitive. The data is only available within the scope of the
parent element of the datalayer, not throughout the entire report
definition. The DataLayer.Linked element can be used to make the data reusable
in another datalayer outside this scope.

A "bookmark" consists of a record in an .xml file, similar to this (format may vary depending on Logi Info version):

![](https://devnet.logianalytics.com/hc/article_attachments/4419699505303/dlbookmarks_01.png)

Bookmark data is retrieved into the datalayer in columns with the following names:  

| Column Name | Contains |
| --- | --- |
| BookmarkCollection | The name of the bookmark collection this bookmark belongs to. |
| BookmarkID | Aunique, system-assigned GUID value identifying the bookmark. |
| BookmarkUserName | The name of the user who created this bookmark. |
| CustomColumn1 | An optional value provided by the developer for customization purposes. |
| CustomColumn2 | An optional value provided by the developer for customization purposes. |
| Description | An arbitrary text description given to the bookmark by the user. |
| ExtraFile | A GUID-based file namefor asuper-element bookmark. |
| FolderID | Aunique, system-assigned GUID value identifying the logical folder containing this bookmark. |
| IsShared | A flag indicating whether this bookmark is shared. |
| Name | An arbitrary name given to the bookmark. |
| Report | The name of the report associated with the bookmark. |
| SaveTime | The bookmark creation timestamp, in ISO 8601 format (e.g. "2014-06-23T09:32:11-04:00"). |

The data retrieved into the datalayer can be viewed during development by setting **General** element's **Debugger Style** attribute in the \_Settings definition and using
the resulting link at the bottom of the report page to view the Debugger Trace page. A link on the Trace page will display the retrieved data.
