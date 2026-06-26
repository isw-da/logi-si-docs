---
title: "Storage Management: Custom Implementation"
id: 5281646850327
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281646850327-Storage-Management-Custom-Implementation
updated_at: 2022-05-03T22:07:47Z
---

# Storage Management: Custom Implementation

# Storage Management: Custom Implementation

## Recommended Reading

The following topics provide background on Exago’s Storage Management system. It is highly recommended to review them before writing a custom implementation of Storage Management.

* [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction)
* [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema)

## Introduction

Clients may write their own implementation of the Storage Management assembly to replace Exago’s out-of-the-box implementation.

In *v2020.1*, a custom assembly must contain one class that implements the entire **[IStorageManagement Interface](#IStorage)**.

In *v2021.1+*, the [IStorageManagement Interface](#IStorage) methods have been virtualized, so clients need only implement the methods that will operate differently than Exago’s out-of-the-box behavior. Refer to the basic example at the end of this topic.

Clients looking to write their own Storage Management assembly may download Exago’s Storage Management implementation code as a Visual Studio project from the [Downloads page on Support Site](https://support.exagoinc.com/hc/en-us/categories/202053837). If you need more information, contact [Exago Support](https://help.insightsoftware.com/s/contactsupport?language=en_US "Exago support").

### SessionInfo

The **SessionInfo object** is not available in the Storage Management system. However, there is a dictionary of options passed around the Storage Management system that stores pertinent information for the database, but additional key-value pairs can be added as needed. This dictionary may be accessed with the .NET API, REST Web Service API and within the Storage Management assembly itself.

#### Example

This example modifies the constructor of Exago’s Storage Management example.

```
public StorageMgmtDatabase(StorageMgmtConfig config) {
 
 //set the value of the companyId identity key to Exago, Inc.
 config.SetIdentity("companyId", "Exago, Inc.");
 
 //set a Custom Option named userProfile
 config.SetOption("userProfile", "support_Administrator");
}
...
```

### Implementation

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

Once developed, move the finished library into a directory accessible to the Exago Web Application for example `<WebApp>/bin`, Scheduler Services for example `<Sched>/bin` (if applicable) and REST Web Service API for example `<WebSvc>/bin` (if applicable). Then set the **Admin Console** > **Storage Management** > **Assembly Location** and **Class Name** settings accordingly.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> Name the DLL file something other than `WebReports.ContentDatabase.dll` as not to overwrite the Exago provided library. This way, if troubleshooting is ever needed in the future, it is easy to change back to the factory provided implementation.

## ContentMetadata Class

The **ContentMetadata** class contains metadata about reports and other content. This data is saved to the Storage Management database, and is serializable as JSON.

**Namespace:** WebReports.Api.Common

### Properties

A **ContentMetaData** object has the following properties. Properties that appear as hyperlinks below require constants or enums which are documented in [Constants and Enumerators](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators).

Table A — ContentMetaData Class Properties

| Name | Type | Writable | Description |
| --- | --- | --- | --- |
| AccessFlags | [ContentPermission v2021.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#ContentP) | yes | Integer representation of bitmap of the access flags bitmap |
| Age | TimeSpan | no | The age of the object, used internally |
| AllowExportCsv | Boolean | yes | Whether this report object can be exported to CSV. |
| AllowExportExcel | Boolean | yes | Whether this report object can be exported as an Excel workbook. |
| AllowExportHtml | Boolean | yes | Whether this report object can be run in a Report Viewer |
| AllowExportPdf | Boolean | yes | Whether this report object can be exported as a PDF file. |
| AllowExportRtf | Boolean | yes | Whether this report object can be exported as an RTF file. |
| Attribute | string | yes | If this content is a theme, then this is theme type (that is Chart, CrossTab, Express, ExpressView, ExpressView\_v2, Map) |
| CacheKey | string | no | Returns the content ID of this object. |
| CanRename | Boolean | yes | This field is not implemented and is ignored. |
| CanShare | Boolean | yes | This field is not implemented and is ignored. |
| ClientData | string | yes | Content of the UDF metadata string from a custom folder management implementation. |
| ContentData | array of byte | yes | Holds the binary content of templates |
| ContentId | GUID | yes | The GUID which uniquely identifies this content item throughout the application |
| ContentType | [wrContentType v2020.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#wrConten) | yes | The type of content that this content item is |
| ContentXML | string | yes | Holds the text string for reports and themes |
| Description | string | yes | User supplied report description field |
| ExportFlags | integer | yes | Bitmap indicating the various permitted export types. From MSB to LSB: Excel, CSV, RTF, PDF, HTML. This property is for informational purposes only. Changing it will not affect the report’s output types. Output types are only controlled by the report. |
| ExtendedAttributes | string | yes | This field is reserved for use by Exago clients, for storing metadata about content as they see fit in their custom implementation. |
| ExtensionData | string | yes | This field is for future functionality and is not implemented yet. |
| Folder | string | yes | Relative folder path of this content item |
| FullName | string | yes | Folder path plus the report name **Example:** My Reports\Sales Report |
| IsFolder | Boolean | yes | Indicates if this content item is a folder as opposed to a report |
| IsOwner | Boolean | yes | Indicates if the current user is the owner of the content item |
| IsReadOnly | Boolean | yes | Determines if this item is considered to be read-only. |
| IsReport | Boolean | yes | Indicates if this content item is a report. *True* if it is a report, *False* is it is not a report. |
| Name | string | yes | Report name without the folder or file extension |
| ParentId | GUID | yes | The GUID that uniquely identifies the parent (folder) of this content item |
| ReportType | [wrReportType](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#wrReport) | yes | If the **ContentType** property is *wrContentType.Report*, this property indicates the report type it is |
| Timestamp | DateTime | yes | A DateTime representing the moment when this object was created. |
| DefaultExportType | [ExportFlag v2020.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#ExportFl) | yes | The report’s **Default Export Type** setting, represented by the [ExportFlag v2020.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#ExportFl) enumeration. |
| ReportTreeShortcutAction | [TreeShortcut](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#TreeShor) | yes | The report’s **Report Tree Shortcut** setting, using the [TreeShortcut](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#TreeShor) enumeration. |
| UseCacheExecution | Boolean | yes | If this content item is a report, this column is *True* if Execution Caching is enabled for this report, or *False* if Execution Caching is disabled. |
| IsCacheValid | Boolean | yes | This column is for future functionality and is not implemented yet. |
| AssociatedReports | List of GUID | yes | A list of **content\_id**s as GUIDs for each report that is associated with this one. Reports become associated with others when they are components in a **Composite Report** such as **Chained Report** or **Dashboard**, or if an **Advanced Report** contains linked reports.  * Chained Reports: Each component report in a chain is included. * Dashboards: Each Existing Report tile is included. * Advanced Report with linked report: a report is included for each cell that is linked. For example, if there are 4 cells that link to the same report, the same **content\_id** will appear in this list 4 times. |
| SourceId | GUID | yes | The content ID that this **ContentMetadata** object is based on. For newly created content or when saving a report with the same name this field will be `Guid.Empty`.  For duplicated reports or when saving an existing report with a new name, this field will be the content ID of the original report.  When exporting an ExpressView to an Advanced Report, this field will be the content ID of the ExpressView.  Based on the value of this field, it can be determined if an item is being saved for the first time, being duplicated in the user interface, or saved with either a new or existing location. |

### Constructors

#### `public ContentMetadata()`

|  |  |
| --- | --- |
| Description | Instantiate a new **ContentMetadata** object. **ContentMetadata**.**AccessFlags** will be set to full permissions. |

#### `public ContentMetadata(ContentMetadata other)`

|  |  |
| --- | --- |
| Description | Copy constructor: Instantiate a new **ContentMetadata** object and copy the properties of the passed object `other` to this one. The following properties are copied:  * ContentId * ParentId * ReportType * ContentType * Name * Folder * Description * IsReadOnly * ExportFlags * TimeStamp * ContentXML * ContentData * AccessFlags * ClientData * ExtendedAttributes * SortOrder * IsOwner * ReportTreeShortcutAction * DefaultExportType |
| Arguments | * `other`: the **ContentMetadata** object to copy into this new one |

### Methods

#### `string GetUdfJson()`

|  |  |
| --- | --- |
| Description | Serializes this content object as JSON. Includes metadata about the item. Properties included in the JSON:  * ContentId * ContentType * ReportType * AccessFlags * ClientData |
| Returns | A JSON encoded **String** of this object for use in the client |

#### `static ContentMetadata GetMetadataFromJson(string jsonStr)`

|  |  |
| --- | --- |
| Description | Return a **ContentMetadata** object from the supplied string, assumed to be a JSON serialized form of a **ContentMetadata** object. This method is static. |
| Arguments | * `jsonStr`: a JSON serialized form of a **ContentMetadata** object |
| Returns | A **ContentMetadata** object |

#### `void SetFullNamesFromFullName(string fullName)`

|  |  |
| --- | --- |
| Description | Set the report name (Name property) and folder (Folder property) from the specified FullName property string. |
| Arguments | * `fullName`: a string representing the **FullName** property of a content item. |

#### `string ToString()`

|  |  |
| --- | --- |
| Description | Return a string representation of the **ContentMetadata** object |
| Returns | A string in the following format:  ``` ReportMetadata Id: {contentId} Name: {name} Folder: {folder} Type: {report or content type} ```   Items in {braces} will be replaced by the object’s properties. Examples:   ``` ReportMetadata Id: 34952c9c-9b0c-869a-c850-3b623ba4005b Name: Current Product Listing Folder: General Reports Type: ExpressView ```  ``` ReportMetadata Id: 141f017a-e8c2-4a9a-baec-90826bab4d77 Name: SA Timesheet (blank).pdf Folder: NULL Type: Template ``` |

## IStorageManagement Interface

The IStorageManagement interface defines all of the necessary methods that will be called from ExagoBI to read and write content to the Storage Mechanism. All of the permissions logic, if applicable, can be built into the methods of this class.

WebReports.Api.Report.ReportProperties objects can be used for reading information about reports directly from their XML definition, without having to first load the report with `ReportObjectFactory.LoadFromRepository(string name)`.

**Namespace:** WebReports.Api.ReportMgmt

```
public interface IStorageManagement
 {
	wrContentType? GetContentType(Guid contentId)
 	IEnumerable<ContentMetadata> GetContentList(wrContentType contentType, bool includeContent = false);
 	ContentMetadata GetContent(ContentMetadata metadata);
 	string GetCacheKey();
	void RenameContent(ContentMetadata metadata, string newName, ContentMetadata parentMetadata);
	void DeleteContent(ContentMetadata metadata);
	void SaveContent(ContentMetadata metadata);
 	StorageMgmtResult ValidateContentName(string reportName, string udfData);
	void AddFolder(ContentMetadata metadata);
    void MoveFolder(ContentMetadata folder, ContentMetadata target, bool updatePermissions);
	IEnumerable<string> GetTemplateList();
	byte[] GetTemplate(string templateName);
	void SaveTemplate(string templateName, byte[] templateData)
	IEnumerable<ContentMetadata> GetThemeList(string themeType);
	bool ExistTheme(string themeType, string themeName);
	string GetTheme(string themeType, string themeName);
	void SaveTheme(string themeType, string themeName, string themeData);
	void ClearReportListCache();
    string TestConnection();
	string InitDb(string jsonSchemaFilePath, bool showSQL);
 }
```

### Methods

#### `wrContentType? GetContentType(Guid contentId);`

|  |  |
| --- | --- |
| Description | Return the content type (for example *report*, *folder*, *theme*, *template*) of the object whose ID is **contentId** light bulb This call ignores the user’s access permissions. |
| Arguments | * `contentId`: a GUID, the content ID in the database of the content whose type to retrieve |
| Returns | a value from the [wrContentType v2020.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#wrConten) enumeration representing the type of content (for example folder, report, theme, template) to return |

#### `IEnumerable<ContentMetadata> GetContentList(wrContentType contentType, bool includeContent)`

|  |  |
| --- | --- |
| Description | Return a collection of content items of the specified type as [ContentMetadata Class](#ContentM) objects. This method is called whenever a list of content is needed, such as by the Report Tree, in the Linked Report Wizard, the Name tab of the Report Wizard, the Duplicate Report dialog, the Role Folders dialog in the Admin Console. |
| Arguments | * `contentType`: a value from the [wrContentType v2020.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#wrConten) enumeration representing the type of content (for example folder, report, theme, template) to return * `includeContent`: Boolean value indicating whether or not the content item’s full content (either the text or binary content) will be returned in the ContentMetadata object. Set to *true* to return content, *false* to return metadata only. Default value is *false*. |
| Returns | A collection of ContentMetadata objects |

#### `ContentMetadata GetContent(ContentMetadata metadata)`

|  |  |
| --- | --- |
| Description | Return the metadata and content (text or binary) for the specified content item. This method is called whenever content needs to be retrieved from the Storage Management database. This includes opening a report to edit or execute, reading in template files or themes during report design or execution. This method is also called after clicking **Finish** in the Report Wizard to load the newly created report into the Designer, and when clicking on items in the Report Tree to load details about the item (for example export types). |
| Arguments | * `metadata`: a [ContentMetadata Class](#ContentM) object representing the content item to retrieve. |
| Returns | A **ContentMetadata** object that represents the content requested |

#### `string GetCacheKey()`

|  |  |
| --- | --- |
| Description | Return the report list cache key. This is generally user specific and is constructed from containing all the identity keys referenced in the party type table. Exago will compare the returned cache keys. If the cache key is different, the cache should be considered expired.  This method is called frequently to check if the cache has expired for a particular user, including the start of the session, starting the Report Designers or Report Wizards, and stepping through the Report Wizard. |
| Returns | A string with the cache key. |

#### `void RenameContent(ContentMetadata metadata, string newName, ContentMetadata parentMetadata)`

|  |  |
| --- | --- |
| Description | Renames or moves a content item. Move an item by specifying a different parent item. The content indicated by **metadata** has its name changed to **newName**. This method is called when moving or rename reports and when renaming folders. Folders are moved with the [void MoveFolder(ContentMetadata folder, ContentMetadata target, bool updatePermissions)](#void) method. |
| Arguments | * `metadata`: the [ContentMetadata Class](#ContentM) object to be renamed or moved. * `newname`: string with the new name for the content item * `parentMetadata`: a **ContentMetadata** object representing the parent of `metadata`. To move a content item to a new folder, specify a different parent object here. To keep the item in the same folder, specify the content item’s existing parent here. |

#### `void DeleteContent(ContentMetadata metadata)`

|  |  |
| --- | --- |
| Description | Delete the content in the **metadata** object. This method is called anytime a content item is deleted, after the user interface requests confirmation from the user the item should be deleted. |
| Arguments | * `metadata`: the **[ContentMetadata Class](#ContentM)** object to be deleted. |

#### `void SaveContent(ContentMetadata metadata)`

|  |  |
| --- | --- |
| Description | Save the content in the **metadata** object. This may be a new or updated content. This method is called when writing changes to content into the database. This could be a report, or a theme. Folders are added with the separate [void AddFolder(ContentMetadata metadata)](#void2) method. |
| Arguments | * `metadata`: the **ContentMetadata** object to be saved. |

#### `StorageMgmtResult ValidateContentName(string reportName, string udfData)`

|  |  |
| --- | --- |
| Description | Used to validate that a report name is legitimate and allowed in the database. The method should permit only valid report names to be saved in the database. In Exago’s implementation of the interface, this method simply returns `null` as report name validation is handled elsewhere in the application. |
| Arguments | * `reportName`: the report name to be validated * `udfData`: additional UDF report data |
| Returns | A **StorageMgmtResult** object that can be queried for a result code. |

#### `void AddFolder(ContentMetadata metadata)`

|  |  |
| --- | --- |
| Description | Add a new folder. The new folder’s parent is set in the **metadata** object. |
| Arguments | * `metadata`: a **ContentMetadata** object representing the folder to be added. |

#### `void MoveFolder(ContentMetadata folder, ContentMetadata target, bool updatePermissions)`

|  |  |
| --- | --- |
| Description | Move a folder into a new location, and optionally copy the permissions from the destination folder to content in the one being moved. This method is called whenever a folder is moved, by dragging it around the Report Tree or when choosing Move Folder to Root from the right-click menu. |
| Arguments | * `folder`: a **ContentMetadata** object representing the folder to be moved. * `target`: a **ContentMetadata** object representing the destination where **folder** will be moved to. * `updatePermissions`: *true* if the permissions of **target** should be copied to content in **folder** or *false* if the permissions should not be copied. The permissions will only be changed for content that the current user is the owner of. |

#### `IEnumerable<string> GetTemplateList()`

|  |  |
| --- | --- |
| Description | Return a collection of template names. This method is called when opening the **Template** dialog on the Report Designer’s Settings menu and after selecting a new Template file to upload with the **Upload** button. |
| Arguments | none |
| Returns | A collection of strings with names of the templates in the database. |

#### `byte[] GetTemplate(string templateName)`

|  |  |
| --- | --- |
| Description | Get the binary contents of a Microsoft Word, Microsoft Excel or PDF template file. This method is called when selecting a template from the dropdown list in the **Template** dialog, immediately after uploading a new template and after saving a report that includes a template. |
| Arguments | * `templateName`: the name from the Content table of the template file to read. |
| Returns | A byte array of the binary contents of the template file. |

#### `void SaveTemplate(string templateName, byte[] templateData)`

|  |  |
| --- | --- |
| Description | Save the binary contents of a Microsoft Word, Microsoft Excel or PDF template file to the database. This method is called to Upload a new template to the database from the Templates dialog in the Report Designer. |
| Arguments | * `templateName`: the name from the Content table of the template file to be saved. * `templateData`: a byte array of the binary contents of the template file. |

#### `IEnumerable<ContentMetadata> GetThemeList(string themeType)`

|  |  |
| --- | --- |
| Description | Retrieve a collection of theme names that match the specified theme type as **ContentMetadata** objects. This method will be called from the Report Designers when they are opened, and before calling [void SaveTheme(string themeType, string themeName, string themeData)](#void3). |
| Arguments | * `themeType`: the type of theme to retrieve (for example *ExpressView*, *Chart*, *Map*, *CrossTab*, *Express*) |
| Returns | An enumerable collection of **ContentMetadata** objects representing all of the available themes of the requested type. |

#### `bool ExistTheme(string themeType, string themeName)`

|  |  |
| --- | --- |
| Description | Check to see if a theme exists in the database. This method is called when saving a theme to see if it already exists. |
| Arguments | * `themeType`: the type of the theme to check for. * `themeName`: the name of the theme to check for. |
| Returns | *true* if the theme exists in the database, *false* if it does not |

#### `string GetTheme(string themeType, string themeName)`

|  |  |
| --- | --- |
| Description | Get the content of the theme. This method will be called by a Report Designer to retrieve the theme data to apply it to the report. |
| Arguments | * `themeType`: the type of the theme to read. * `themeName`: the name of the theme to read. |
| Returns | A string with the text content (XML, JSON or CSV) of the theme. |

#### `void SaveTheme(string themeType, string themeName, string themeData)`

|  |  |
| --- | --- |
| Description | Save new contents into a theme. If the theme exists, it will be overwritten. This method is called when a theme is saved from one of the Report Designers. |
| Arguments | * `themeType`: the type of theme that will be saved * `themeName`: the name of theme that will be saved * `themeData`: the XML, JSON or CSV content of the theme that will be saved |
| Example | ``` this.SaveTheme("Chart", "Crimson Mountain", "#F0433A,#C9283E,#820333,#540032,#2E112D") ``` |

#### `void ClearReportListCache()`

|  |  |
| --- | --- |
| Description | Clear the report list cache. This method should be called when saving or updating reports to make sure the Report Tree is up to date with the content changes. |

#### `string TestConnection()`

|  |  |
| --- | --- |
| Description | Check the connection to the Storage Management database specified in the configuration file is valid. This method is called when clicking the **Check Database Settings** button in the **Admin Console**. |
| Returns | A string containing any error message, otherwise `null` if the connection is successful. |

#### `string InitDb(string jsonSchemaFilePath, bool showSQL)`

|  |  |
| --- | --- |
| Description | Initialize a Storage Management database with the schema definition found in the provided JSON file. This method is called when clicking the **Initialize Database** or **Show Schema SQL** buttons in the **Admin Console**.  More information can be found in the [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema) topic.  light bulb Default location is `<WebApp>\Config\Other\StorageMgmtSchema.json` where `<WebApp>` is the installation directory of the Web Application. |
| Arguments | * `jsonSchemaFilePath`: full path to the schema definition JSON file. * `showSQL`: whether or not database initializing SQL statements should be returned |
| Returns | If `showSQL` is *true*, this method will return SQL statements that can be used to initialize a Storage Management database. If `showSQL` is *false*, this method will return *null*. |

## Virtualized Methods v2021.1+

Below is a basic example of a class that overrides only the **SaveContent** and **AddFolder** methods.

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using WebReports.Api.Common;
using WebReports.Api.ReportMgmt;
using WebReports.ContentDatabase;

namespace V_versions
{
 public class V_storage : StorageMgmtDatabase
 {
  private static readonly Logger logger = Log.GetLogger();

  /**
   * Provide a constructor
   */ 
  public V_storage(StorageMgmtConfig config) : base(config)
  {
  }

  /** 
   * Override the SaveContent method
   * <param name="metadata">the ContentMetadata object to be saved</param>  */ 
  public override void SaveContent(ContentMetadata metadata)
  {
   //Custom implementation of the method goes here
  }

  /**
   * Override the AddFolder method
   * <param name="metadata">a ContentMetadata object representing the folder to be added</param>  */ 
  public override void AddFolder(ContentMetadata metadata)
  {
   //Custom implementation of the method does here
  }
 }
}
```

Then, based on this example in the **Admin Console**, set the following:

* **Assembly Location** to the full path to the DLL produced by the project
* **Class Name** — `V_versions.V_storage`
