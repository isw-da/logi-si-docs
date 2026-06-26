---
title: "Storage Management: Database Schema"
id: 5281630919319
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema
updated_at: 2022-05-03T22:08:47Z
---

# Storage Management: Database Schema

# Storage Management: Database Schema

Exago’s Storage Management implementation defines several tables: **Content**, **Party Type**, **Content Access**, **Config\_File** and **StorageMeta**. At a very high level, the basic relationship between these tables is depicted by the following diagram:

![Storage_Management_Graphic_Blue.png](https://devnet.logianalytics.com/hc/article_attachments/5432228320023/storage_management_graphic_blue.png)

Storage Management table relationship

### Database Requirements

#### Permissions

Exago must be able to **INSERT**, **UPDATE**, **SELECT** and **DELETE** on the Storage Management database. If Exago is used to initialize the database (either through the Admin Console or one of the transitioning utilities), Exago must also be able to **CREATE TABLE**.

#### MySQL

If using MySQL for the Storage Management database, increase MySQL’s `max_allowed_packet` parameter to greater than the largest report or template file before using the transitioning utilities.

Symbols Used in this topic

* 🔑 indicates a **primary key**
* 🏷️ indicates a **foreign key**

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> The current Storage Management data schema version is *1.1*.

## Content Table

Each report, folder, theme or template is represented by a row in the **Content** table. A GUID is used as a unique identifier throughout the database and application to reference the content.

Table A — Storage Management **Content** Table Schema

| Column | Description |
| --- | --- |
| 🔑 content\_id | ID which uniquely identifies this content item |
| content\_type | The type of content this item represents, using the [wrContentType v2020.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#wrConten) enumeration (for example folder, report, theme, template) |
| report\_type | The type of report this row represents, using the [wrReportType](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#wrReport) enumeration.  If the **content\_type** is not *0* (that is this row does not represent a report), this column is ignored. |
| content\_attribute | The component of the application that this item is associated with. Used when **content\_type** is *2* to associate chart types with their respective themes.  Will be one of the following values:   * Chart * CrossTab * Express * ExpressView * ExpressView\_v2 * Map — theme for GeoChart   If the **content\_type** is not *2* (that is this row does not represent a theme)*,* this column is null and is ignored. |
| name | The name of the content item. |
| description | The description of the content item. For reports, this is the **Description** field provided when the report is saved. |
| text\_content | Plain text contents of the content item.  Report definitions and themes are stored in this column. |
| bit\_content | Binary contents of the content item.  Template files are stored in this column. |
| deleted\_flag | Indicates if the content owner has deleted this item. When an item is deleted by the owner, it is no longer visible to any user. *1* represents *True* (item has been deleted), *0* represents *False* (item has not been deleted). |
| created\_date | UTC timestamp when this content item was created. |
| created\_by | The value of the **User Id** identity key that created this content item. |
| modified\_date | UTC timestamp when this content was last saved. |
| modified\_by | The value of the **User Id** identity key that last saved this content item. |
| owner\_id | The value of the **Owner Id** identity key that owns this content. If the session’s **Owner Id** identity key matches this column’s value, that party will be given full permissions to the content item. |
| exports\_allowed | A bitmap indicating which export types the content item allows, where *1* indicates an export type is permitted and *0* indicates an export type is not permitted.  This column is used for informational, sorting and filtering purposes only. These flags have no affect on the export types allowed for a report, which is still controlled by the report itself. When content is saved, this column will be updated to match the export type saved in the report definition.  From MSB to LSB: *Excel*, *CSV*, *RTF*, *PDF*, *HTML*.  Examples:   * 00001 = 1 = HTML only. No file exports. * 00011 = 3 = HTML and PDF only * 11001 = 25 = HTML (report viewer), Excel Workbook and CSV exports * 11111 = 31 = All file types allowed |
| inherit\_flag | *True* if all of this content item’s content access records should be copied to new child content when it’s created. If *False*, a new content access record will be written for new child content with the **default\_party\_type\_id** and **default\_access\_flags.** If *null,* the value in the system configuration will be used. |
| 🏷️ default\_party\_type\_id | If **inherit\_flag** is *False*, a content access record with this party type and **default\_access\_flags** will be written for new content that is a child of this item.  If the new content is a folder, this value will always be copied from the parent folder whether or not **inherit\_flag** is true. |
| default\_access\_flags | If **inherit\_flag** is *False*, a content access record with the **default\_party\_type\_id** and these access flags will be written for new content that is a child of this item. For more information, see the access\_flags column in Table E below.  If the new content is a folder, this value will always be copied from the parent folder whether or not **inherit\_flag** is true.  These flags will be implemented in *v2020.2* of the application. |
| extended\_attributes | This field is reserved for use by Exago clients, for storing metadata about content as they see fit in their custom implementation. |
| default\_export\_type | This column is used for informational, sorting and filtering purposes only. This flag have no affect on the default export type allowed for a report, which is still controlled by the report itself. When content is saved, this column will be updated to match the default export type saved in the report definition.  The report’s **Default Export Type** setting, represented by the [ExportFlag v2020.1+](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#ExportFl) enumeration. |
| report\_tree\_shortcut\_action | This column is used for informational, sorting and filtering purposes only. This flag have no affect on the report tree shortcut for a report, which is still controlled by the report itself. When content is saved, this column will be updated to match the report tree shortcut saved in the report definition.  The report’s **Report Tree Shortcut** setting, using the [TreeShortcut](https://devnet.logianalytics.com/hc/en-us/articles/5281610137879-Constants-and-Enumerators#TreeShor) enumeration. |
| use\_cache\_execution | This column is used for informational, sorting and filtering purposes only. This flag have no affect on enabling or disabling Execution Caching for a report, which is still controlled by the report itself. When content is saved, this column will be updated to match the execution cache settings saved in the report definition.  If this content item is a report (**content\_type** = *0*), this column is *True* if Execution Caching is enabled for this report, or *False* if Execution Caching is disabled. |
| is\_cache\_valid | This column is for future functionality and is not implemented yet. |
| associated\_reports | A comma separated list of **content\_id**s for each report that is associated with this one. Reports become associated with others when they are components in a **Composite Report** such as **Chained Report** or **Dashboard**, or if an **Advanced Report** contains linked reports.   * Chained Reports: Each component report in a chain is included. * Dashboards: Each Existing Report tile is included. * Advanced Report with linked report: a report is included for each cell that is linked. For example, if there are 4 cells that link to the same report, the same **content\_id** will appear in this list 4 times. |

## Party Type Table

The **Party Type** defines groups of users. A party could be an individual user or all users, or anywhere in between.

Table B — Storage Management **Party Type** Table Schema

| Column | Description |
| --- | --- |
| 🔑 party\_type\_id | Unique key identifying this party type. |
| priority | Defines the priority level of the access. A larger number increases priority of this party type. See [Priority Levels](#Priority) below for additional information. |
| name | Name of this **party\_type**. |
| parameter | The name of the Storage Management identity key that will be compared to see if the user has access to this content. Out-of-the-box these values are:   * *classId* * *companyId* * *userId*   but any identity key name defined in the configuration may be used. |
| description | A long format user friendly description of this party type. |

### Priority Levels

The party type priorities determine in which scope the associated content access record applies. They are called *priorities* because higher values override lower ones.

For example if there are two content access records that apply to the same user for a content item, the record with the numerically greater **value** will apply over the other.

For more information, review the [Permissions](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction#Permissi) section of the Storage Management: Introduction topic.

Table C — Party Type Table **priority** Values

| Value | Name | Description |
| --- | --- | --- |
| 1 | Everyone | Everyone has access to this item. |
| 2 | Class | Users based on the their role in the organization.  Exago will compare the value of the *classId* key against **content\_access.party\_id** for all records associated with the **content\_id** to determine if the record applies. |
| 3 | Company | Users based on their role in the company.  Exago will compare the value of the *companyId* key against **content\_access.party\_id** for all records associated with the **content\_id** to determine if the record applies. |
| 4 | User | Individual user access.  Exago will compare the value of the *userId* key against **content\_access.party\_id** for all records associated with the **content\_id** to determine if the record applies. |

### Default Party Type Values

When one of the Transition Utilities is used, or the **Initialize Database** button is clicked in the **Admin Console**, Exago will create the Storage Management database tables and load the following default party types into it:

Table D — Default Party Type Values

| party\_type\_id | priority | name | parameter | description |
| --- | --- | --- | --- | --- |
| 1 | 0 | Everyone |  | All users belong to this party |
| 2 | 1 | Class | classId | Users based on their role in the organization, for example an admin or user |
| 3 | 2 | Company | companyId | Users that belong to a specific company |
| 4 | 3 | User | userId | Individual users |

## Content Access Table

The relationship between **content** and **party\_type** is defined in the **content\_access** table. Each content access record defines permissions available for each content item. The content access table also establishes a parent-child relationship between content items.

Table E — Storage Management **Content Access** Table Schema

| Column | Description |
| --- | --- |
| 🏷️ content\_id | Foreign key referencing the **content\_id** in the **content** table that this record relates to. |
| 🏷️ party\_type\_id | Foreign key referencing the **party\_type\_id** in the **party\_type** table, establishing the party for which this access record applies. |
| party\_id | The value of the Storage Management identity key specified by **party\_type\_id** that this content access record applies to. Sets the identity of the user group for which this access record applies.  Example with default party types:   Table F — Examples  | If **party\_type\_id** is… | And **party\_id** is… | These users are affected by this content access record… | | --- | --- | --- | | 1 | n/a | All users | | 2 | report-builder | Any user whose *classId* key value is also report-builder*.* | | 3 | Exago, Inc. | Any user whose *companyId* key value is also *Exago, Inc.*, regardless of their *classId* key. | | 4 | Astro Boy | Only the user whose *userId* key value is *Astro Boy*, regardless of their *companyId* or *classId* keys. | |
| sort\_order | Content is sorted first by the value in this column, then by name (case in-sensitive). Larger values appear at the top of the sorted list).  For example:   | Name | sort\_order | | --- | --- | | Nick | 99 | | emma | 99 | | Tim | 0 | | alex | 0 | | Bailey | 0 |   the sorted list would be: emma, Nick, alex, Bailey, Tim |
| access\_flags v2020.1–v2021.1 | A bitmap indicating what access is permitted by this record, where *1* indicates a user in the party can complete the action and *0* indicates that they cannot.  **CanView**, **CanSave** and **CanEdit** are currently implemented. The other flags are not yet active and will be implemented in a future release. All flags should be set as content is created to insure expected behavior when they are made active.  From MSB to LSB:   * **Reserved** — this bit is reserved for future use * **Reserved** — this bit is reserved for future use * **Reserved** — this bit is reserved for future use * **Reserved** — this bit is reserved for future use * **Reserved** — this bit is reserved for future use * **Reserved** — this bit is reserved for future use * **Reserved** — this bit is reserved for future use * **CanView** — the content item is visible in the Report Tree * **CanDownload** — if **Show Report Upload/Download Options** in the Admin Console is *True*, this value determines if the content can be downloaded. Has no effect if **Show Report Upload/Download Options** is *False*, or if the content is set as read-only by a Role. * **CanCopy** — the content can be duplicated * **CanExecute** — the report can be run * **CanDelete** — the content can be deleted * **CanShare** — for future functionality and is not implemented yet * **CanRename** — the content can be renamed * **CanSave** — the report can be saved * **CanEdit** — the report can be opened in the Report Designer   Examples:   * 1111111111111111 = 65535 = All permissions available * 0000000100100000 = 288 = Report appears in the report tree and can be run, but no other permissions. * 0000000100100011 = 291 = Report may only be run, edited and saved and will appear in the report tree. * 0000000111100000 = 480 = Report appears in the report tree, and can be downloaded, duplicated and run. Otherwise no other permissions.  light bulb This is the same behavior as the **Read Only** option in Roles. |
| access\_flags v2021.1+ | A bitmap indicating what access is permitted by this record, where *1* indicates a user in the party can complete the action and *0* indicates that they cannot.  From MSB to LSB:   * **Reserved** — this bit is reserved for future use * **Reserved** — this bit is reserved for future use * **Reserved** — this bit is reserved for future use * **Reserved** — this bit is reserved for future use * **Reserved** — this bit is reserved for future use * **CanMove** — the item can be moved to a different location * **CanSchedule** — the item can be scheduled or emailed * **CanView** — the content item is visible in the Report Tree * **Reserved** — this bit is reserved for future use * **CanCopy** — the item may be duplicated or downloaded * **Reserved** — this bit is reserved for future use * **CanDelete** — the item can be deleted * **CanShare** — for future functionality and is not implemented yet * **CanRename** — the content can be renamed * **Reserved** — this bit is reserved for future use * **CanEdit** — the item can be opened in a designer   Examples:   * 1111111111111111 = 65535 = All permissions available * 0000010100000001 = 1281 = item may be edited in the designer, moved to a different folder and seen in the report tree only * 0000000100000000 = 256 = item is visible in the Report Tree, but no new content may be saved and it may not open in the Designer.  light bulb This is the same behavior as marking items as **Read Only** with a Role. The **Read Only**TreeReportLock.png icon will appear for items that do not have the **Can Rename**, **Can Move**, **Can Delete** and **Can Edit** permissions. |
| 🏷️ parent\_id | Foreign key referencing the **content\_id** in the **content** table for the parent of this item. For a report, this would be the folder the report is stored in. For a folder, this would be the parent folder.  If *00000000-0000-0000-0000-000000000000*, this item is in the root of the hierarchy (it has no parent). |
| child\_inherits | This column is for future functionality and is not implemented yet. |

## StorageMeta

Metadata pertaining to the Storage Management system is stored in this table as name-value pairs. It is used internally by Exago’s Storage Management implementation.

Table G — Storage Management **StorageMeta** Table Schema

| Column | Data Type | Description |
| --- | --- | --- |
| 🔑 name | string | The name of the name-value pair. |
| value | string | The value of the name-value pair. |

The **StorageMeta** table will be loaded with some initial name-value pairs when the Storage Management database is initialized. They are:

Table H — **StorageMeta** Key-Value Pairs

| name | value Data Type | value Description |
| --- | --- | --- |
| CREATED | string | A timestamp representing the instant the database was initialized (created). For example: `2020-01-23T10:35:22` |
| SCHEMA\_VERSION | string | The Storage Management data schema version currently employed by this implementation. For example: `1.1` |

## Schema JSON

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

The schema defined above is also detailed in the following JSON file. This file is located in `<WebApp>\Config\Other\StorageMgmtSchema.json`. It is read by the transitioning utilities and the Web Application when initializing a new database.

In a custom Storage Management implementation, it is possible to add tables, columns and have Exago’s tools create them when executed.
