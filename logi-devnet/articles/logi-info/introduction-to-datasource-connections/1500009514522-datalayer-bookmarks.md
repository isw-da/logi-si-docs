---
title: "DataLayer.Bookmarks"
id: 1500009514522
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514522-DataLayer-Bookmarks
updated_at: 2021-06-17T01:58:09Z
---

# DataLayer.Bookmarks

# DataLayer.Bookmarks

The **DataLayer.Bookmarks** element is used specifically to retrieve saved bookmark information.

* Attributes
* [Work with DataLayer.XML File](#WorkingWith)

For more information about bookmarks, see . Bookmark implementation examples can be found in our [Bookmarks Sample Application](https://devnet.logianalytics.com/rdPage.aspx?rdReport=SampleApps&dnPage=3).

## Attributes

The DataLayer.Bookmarks element has the following attributes:

| Attribute | Description |
| --- | --- |
| ID | (Required, through v10.1.46) Unique element ID. |
| Bookmark Collection | (Required) Bookmarks are stored in XML data files, called a Bookmark Collection. These are located in a folder specified in the Bookmark Location attribute of the Settings definition's General element. This attribute sets the name of the collection; only the file name, without an extension, is entered here.  A value is *not* required here if the General element's Bookmark Collection Default has been specified in the \_Settings definition. |

## Work with DataLayer.Bookmarks

This datalayer connects directly to the bookmark collection via the file system. Unlike most datalayer elements, this one requires **no connection
element**. Bookmark information is retrieved and cached as rows and columns, with
one row per bookmark. Data retrieved into the datalayer is cached in **XML**
format.

The data retrieved with a datalayer is available using @Data **tokens**,
in the format @Data.*ColumnName*~. The spelling of the column name is
**case-sensitive**. The data is only available within the **scope** of the
**parent** element of the datalayer, not throughout the entire report
definition. The DataLayer.Linked element can be used to make the data reusable
in another datalayer outside this scope.

A "bookmark" consists of a record in an .xml file, similar to this (format may vary depending on Logi Info version):

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778705687/dlbookmarks_01.png)

Bookmark data is retrieved into the datalayer in columns with the following names:

|  |  |
| --- | --- |
| **Column Name** | **Contains** |
| BookmarkCollection | The name of the bookmark collection this bookmark belongs to. |
| BookmarkID | A unique, system-assigned GUID value identifying the bookmark. |
| BookmarkUserName | The name of the user who created this bookmark. |
| CustomColumn1 | An optional value provided by the developer for customization purposes. |
| CustomColumn2 | An optional value provided by the developer for customization purposes. |
| Description | An arbitrary text description given to the bookmark by the user. |
| ExtraFile | A GUID-based file name for a super-element bookmark. |
| FolderID | A unique, system-assigned GUID value identifying the logical folder containing this bookmark. |
| IsShared | A flag indicating whether this bookmark is shared. |
| Name | An arbitrary name given to the bookmark. |
| Report | The name of the report associated with the bookmark. |
| SaveTime | The bookmark creation timestamp, in ISO 8601 format (e.g. "2014-06-23T09:32:11-04:00"). |

The data retrieved into the datalayer can be viewed during development by setting **General** element's **Debugger Style** attribute in the \_Settings definition and using
the resulting link at the bottom of the report page to view the **Debugger Trace** page. A link on the Trace page will display the retrieved data.
