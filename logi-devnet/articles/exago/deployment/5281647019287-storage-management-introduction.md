---
title: "Storage Management: Introduction"
id: 5281647019287
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction
updated_at: 2022-05-03T22:08:47Z
---

# Storage Management: Introduction

# Storage Management: Introduction

Exago’s **Storage Management** system replaces the legacy *file system*, *cloud storage*, *folder management* and *web service (SOAP)* storage methods with a relational database. All reports, templates, folders and themes are stored in this database. Microsoft SQL Server, MySQL, Oracle and PostgreSQL are supported out-of-the-box. Exago also supports a SQLite database for development, testing and demonstration purposes only.

As of *v2020.1,* all legacy storage methods are deprecated and are replaced with the Storage Management system. Storage Management enables a flexible folder and report permissions model and creates a future development platform for features such as collaboration, annotation, version control and more.

## Content Storage

All reports, folders, report template files, report themes, chart themes, and GeoChart themes are stored in a relational database. This content is stored in a table with some metadata for easy access (for example name, description, exports) and general object management (for example updated by, saved date).

Report definitions and themes are stored as plain-text in the database. Template files are stored as binary data.

### Default Folders

Two new folders will be available for each user in the system:

* **My Reports**: visible to all users, but content saved in it is only available to the current user.
* **Public**: visible to all users and any content saved in it is available to all other users of the system. This provides a basic way of sharing report content with other users.

Review [Permissions](#Permissi) below to learn more about access controls with Storage Management.

If these folders already exist in the environment before upgrading, new ones will not be created. These folders can optionally be deleted if not desired.

### Supported Database Types

Exago’s Storage Management implementation support the following database types for content storage:

* Microsoft SQL Server
* MySQL
* Oracle
* PostgreSQL
* SQLite

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Exago recommends using the included SQLite database for development, testing and demonstration purposes only. Use MSSQL, MySQL, Oracle or PostgreSQL in a production environment.

## Permissions

Content permissions are based on pools of users called **parties**. The most specific is an individual user, the least is “everyone”. In between are various levels of control based on [Identity Keys](#Identity). For example, company level access can be granted based on the value of the companyId key. These keys are discussed in more detail in the [Identity Keys](#Identity) section below and in [Storage Management Permissioning](https://devnet.logianalytics.com/hc/en-us/articles/5281540440983-Storage-Management-Permissioning).

![Upside down funnell showing the precedence of identiy keys](https://devnet.logianalytics.com/hc/article_attachments/5432209948567/keyfunnel.png)

Identity keys work in a hierarchical structure that moves from less specific to more specific

When a user attempts to access content (for example a report), all of the access records that match the provided keys are sorted according to their priority. The first record from that set (the highest priority) provides the effective access to the content. That access may allow execution, editing, viewing, downloading or no access at all. If there are two content access records that apply to the same user (for example there is a match on their **companyId** and on their **userId** values) for a content item, the record with higher priority (**userId**) will apply over the other.

In the figure below, everyone except for user “Nicole” will be able to see “Tim’s Report” in their Report Tree. Only user “Tim” can read, write, rename or share “Tim’s Report”. Anyone in the same “Exago” company (“Travis”, “Tim” and “Alex”) can also write to it as well. Any user (except “Nicole” who is explicitly restricted from it), including those outside of “Exago”, can see the report.

This illustration provides a simplistic way of visualizing Storage Management access. In the actual implementation, access control flags such as “read\_access” are bit flags in a single column. More information about these access flags follows.

![Demonstration of different identityy keys applied to content](https://devnet.logianalytics.com/hc/article_attachments/5432123055511/userpermissions_together.png)

For simplicity, each access flag is shown in it’s own column in this figure. In practice, access flags are expressed as a bitmap in a single access\_flags column. Review the Storage Management: Database Schema topic for more information.

### Identity Keys

A new set of variables called **identity keys** are used to identify ownership and access rights to content in the Storage Management system. These keys are similar in purpose to Exago’s system parameters @userId@ and @companyId@ but are specific to the Storage Management mechanism.

Each time an Exago session is created via the API, values for both the system parameters and any Storage Management identity keys should be set. Values for the keys may be set with .NET API calls and through a [new REST Web Service API endpoint](https://devnet.logianalytics.com/hc/en-us/articles/5281630668311-REST-Storage-Management). Values are case-sensitive, and should be unique across organizations.

Setting the identity keys is not mandatory. However, the Storage Management system will still process access rules with `null` as the value for any unset key. Therefore, it is strongly recommended all identity keys are given values when accessing the application.

Four identity keys are implemented out of the box: **User Id**, **Company Id**, **Class Id** and **Owner Id**. Additional identity keys may be added by editing the configuration file and making appropriate changes to the Party Type table in the database.

For example, consider an employee named “Astro Boy” who works in the “Report Building” department of the company “Exago, Inc.” in Kingston, NY.

#### User Id

A unique identifier for a specific user of the application. For example, “Astro Boy” or “aboy”.

#### Company Id

A unique identifier for the organization or company that the User Id belongs to. This key has second priority in the hierarchy above the User Id. For example, “Exago, Inc.” or “Kingston”.

#### Class Id

A unique identifier for the user’s class. This key has third priority in the hierarchy above the User Id. For example, “administrator” or “report-builder”.

#### Owner Id

When a report or folder is created, the owner of that content is assigned to the value of the creator’s **Owner Id**. For example,  “Astro Boy” or “aboy”.

When the Owner Id column of a content item matches the value of the **Owner Id** identity key, full permission (all access flags are set to *true*) is granted to that content item automatically.

In most cases **Owner Id** will have the same value as the **User Id** key, so that users have ownership of (and therefore full access rights to) content they create. This value doesn’t necessarily need to be an individual user. A company or class can also own content, and so those values are also valid.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> If the **Owner Id** is not set when content is created, Exago will use the value for **User Id** in its place.

Owners of content will see the **Owner**![TreeReportOwned.png](https://devnet.logianalytics.com/hc/article_attachments/5432210012695/treereportowned.png) icon next to the content in their ![MainLeftPaneViewReports.png](https://devnet.logianalytics.com/hc/article_attachments/5432210088471/mainleftpaneviewreports.png)**Report Tree**.

### Access Flags

**Access Flags** assigned to each content item enable or restrict functionality in the application. In *v2020.1*, only the **CanView**, **CanSave** and **CanEdit** flags have been implemented. Setting the other flags will not have any affect at this time, however they are implemented in *v2021.1* and it is best practice to begin setting them now.

### Access Flags v2021.1+

* **Can Edit** — whether or not content may be edited/saved in its respective Report Designer. If *false*, content cannot be opened in a Report Designer, child folders cannot be added, the ![Upload.png](https://devnet.logianalytics.com/hc/article_attachments/5432174691991/upload.png)**Upload** option is not available, content may not be moved to the folder and content cannot be moved out of a folder. The **Run/Stop** button in the ExpressView Designer will be hidden and locked in the **Run** mode.
* **Can Rename** — whether or not content may be renamed. If *false*, the ability to change a content item’s name is unavailable, even though it may be moved to a different location (if **Can****Edit** and **Can Move** permit that change).
* **Can Share** — this flag is for future functionality and is not implemented yet
* **Can Delete** — whether or not content may be deleted. When *false*, delete options are disabled for folders and reports. When *true*, folders must be empty for all users to be deleted.
* **Can Copy** — whether or not content may be duplicated or downloaded. When false, the **Duplicate** and ![Download.png](https://devnet.logianalytics.com/hc/article_attachments/5432193118615/download.png)**Download** options are not available. Setting this flag *false* will also prevent ExpressViews from being exported to Advanced Reports, and will disable the **Save Changes as New Report** option in the **Advanced Report Viewer**.
* **Can View** — whether or not the content is visible in the **Report Tree** or not. When false, the content item is hidden from view. This is useful for hiding components of **Chained Reports** or **Dashboards** from end users.
* **Can Schedule** — whether or not content may be scheduled. When false, the ![ScheduleAddSmall.png](https://devnet.logianalytics.com/hc/article_attachments/5432210118551/scheduleaddsmall.png)**Schedule Report** and **![EmailReportSmall.png](https://devnet.logianalytics.com/hc/article_attachments/5432210153367/emailreportsmall.png)Email Report** options are not available. Has no effect on existing schedules, the **Schedule Wizard** or ![MainLeftPaneScheduleManager.png](https://devnet.logianalytics.com/hc/article_attachments/5432206444439/mainleftpaneschedulemanager.png)**Schedule Manager**.
* **Can Move** — whether or not content may be moved to a different location. In order to move a report, both the target and origin folders must have **Can Edit** set to *true.*

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Content that has the **Can Rename**, **Can Move**, **Can Delete** and **Can Edit** permissions all set to *false* will be considered read-only and marked with the read-only ![padlock icon](https://devnet.logianalytics.com/hc/article_attachments/5432176031767/treereportlock.png) icon. Folders and reports need the **Can View** permission to appear in the ![MainLeftPaneViewReports.png](https://devnet.logianalytics.com/hc/article_attachments/5432210088471/mainleftpaneviewreports.png)Report Tree.

### Access Flags v2020.1–v2021.1

* **Can View** — whether or not the content is visible in the **Report Tree**
* **Can Download** — if **Show Report Upload/Download Options** in the Admin Console is *True*, this value determines if the content can be downloaded. Has no effect if **Show Report Upload/Download Options** is *False*.
* **Can Copy** — the content can be duplicated
* **Can Execute** — the report can be run
* **Can Delete** — the content can be deleted
* **Can Share** — this flag is for future functionality and is not implemented yet
* **Can Rename** — the content can be renamed
* **Can Save** — the report can be saved, or a folder can be saved into
* **Can Edit** — the report can be opened in the Report Designer, or a folder may be edited

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Folders and reports need both **Can Edit** and **Can Save** permissions or they will be read-only and marked with the read-only ![padlock icon](https://devnet.logianalytics.com/hc/article_attachments/5432176031767/treereportlock.png)icon. Folders and reports need the **Can View** permission to appear in the ![report page icon](https://devnet.logianalytics.com/hc/article_attachments/5432210088471/mainleftpaneviewreports.png)Report Tree.

When content is created, access permissions are either inherited from their parent; or a single content access record is written based on the parent’s default party type and access flag settings. If the parent’s access flags are all disabled (or missing) then the new content will use the **Default Access Flags** from the system configuration.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> For the best user experience, keep the number of items in the Report Tree less than 1000.

### Inheritance

A new concept for permissions management has been introduced with Storage Management, called **inheritance**. Functionally, inheritance allows content to “emulate” roles without actually needing to use them. This is meant to provide a migration path away from roles for clients migrating from file system or cloud storage, who want to preserve file system behavior. However, clients migrating from folder management may want to turn inheritance off, as this behavior is not present in that system.

If a folder’s **inherit flag** is *true*, when new content is saved into the folder that content will be assigned all of the same permissions as the folder. All of the content access records assigned to the parent folder will be copied to the new content item.

If a folder’s **inherit flag** is *false*, new content in a folder will not inherit the permissions from the parent. Instead of all of the content access records being copied from parent to the new content, a new single content access record will be written with the default access flags and the default party type.

#### Examples of Inheritance

##### Example 1 — Default Folders

The new Default Folders**Public** and **My Reports** have the inherit\_flag set to *false*.

* **My Reports**
  + **Inherit Flag**: *false*
  + **Default Party Type Id**: *4* (user)
* **Public**
  + **Inherit Flag**: *false*
  + **Default Party Type Id**: *1* (everyone)

When new content is created in the **My Reports** folder since the **inherit flag** is false, any content access records on the **My Reports** folder will not be copied to reports saved there. Instead, reports saved to the **My Reports** folder will have a single *user* level content access record written. The value of the **User Id** identity key will be saved into this access record, there by granting access to the content only to the current user.

When new content is created in the **Public** folder since the **inherit flag** is false, any content access records on the **Public** folder will not be copied to reports saved there. Instead, reports saved to the **Public** folder will have a single *everyone* level content access record written. *Everyone* access records apply to all users of the system, and therefore the access record will set access for all users.

If either folder’s **inherit flag** were *true*, then any content access record on the respective folder would be copied to reports saved in them. This could for example, grant access to another user of a report that should only be visible to a single user in the **My Reports** folder.

##### Example 2 — A Departmental Folder

Consider a fictional folder for the “Sales Department” in a company. A simplified version of the content access records are shown in Table A to demonstrate how they work.

* **Sales Department**
  + **Inherit Flag**: *true*

Table A — Content Access Records for Sales Department folder

| Content | Party Type | Party Value | Access Flags | Parent |
| --- | --- | --- | --- | --- |
| Sales Department | 2 (company) | Sales Dept | 508 | root |
| Sales Department | 4 (user) | Mike B | 511 | root |

When a new report, for example, *Quarterly Report* is saved to the **Sales Department** folder, all of the content access records in Table A would be copied on to the new report. Therefore, the resulting content access table looks like Table B below:

Table B — Content Access Records for Sales Department folder and Quarterly Report

| Content | Party Type | Party Value | Access Flags | Parent |
| --- | --- | --- | --- | --- |
| Sales Department | 2 (company) | Sales Dept | 508 | root |
| Sales Department | 4 (user) | Mike B | 511 | root |
| Quarterly Report | 2 (company) | Sales Dept | 508 | Sales Department |
| Quarterly Report | 4 (user) | Mike B | 511 | Sales Department |

### Query Tool

Exago provides a database query tool called the **Storage Management Utility** that can read from the Storage Management database and display the content access records, access flags and inheritance on content in the system.

For *v2020.1–v2021.1*, the utility is included with the Exago installer. Documentation of the utility can be found in [Storage Management: Utility (v2020.1)](https://devnet.logianalytics.com/hc/en-us/articles/5281631176983-Storage-Management-Utility-v2020-1-).

In *v2021.1+*, the utility is a separate download on the Support Site Downloads page. Documentation for this version can be found in [Storage Management: Utility (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281647115927-Storage-Management-Utility-v2021-1-).

### Roles

The access controls built into Roles essentially sit on top of the Storage Management access flags. This means that Roles can be made more restrictive than the Storage Management mechanism but not less.

If a folder is marked read-only with a Role, a user will not be able to edit, save, delete or rename content in the folder regardless of the access flags or ownership.

Exago recommends choosing one permission model: either Roles or the Storage Management permissions system and not use both at the same time.

### Report Management

Content paths are determined by the access records, thus content can be in different locations for different parties.

Content names in the Storage Management system are case-sensitive.

If the parent’s access flags are all disabled, then the new content will use the **Default Access Flags** from the system configuration.

#### Creating a New Report or Folder

Creating new content requires it be saved into a folder. Folders may be saved in the top-most level called the root or may be children of other folders. Reports may only be saved into folders where the **Can Save** flag is true for that party.

Depending on system configuration, new content can either **inherit** permissions from their parent folder or **default permissions** can be set by the system administrator on a folder-by-folder basis.

#### Moving a Report or Folder To a Different Folder

Moving a content item is essentially the same as creating it in the new location. Content will pick up permissions based on that container’s settings. The existing access records for the content item will be removed, and new records will be written based on the new parent’s settings. Review [Creating a New Report or Folder](#Creating) above.

If someone **other than the owner** of a content item moves it from one folder to another, the item is moved only for that user. A new user-specific access record is added for the content, with the new location.

If the **owner** of the content item moves it, it is moved for all users. The owner’s permissions are “sticky” for that item. The owner will retain the same level of permission they had before the item was moved. If the **owner** moves a folder to one where the permissions are different than its current location, they will be prompted how to handle the permissions after the move:

![KDROYjndVu.png](https://devnet.logianalytics.com/hc/article_attachments/5432176062999/kdroyjndvu.png)

Folder Move confirmation prompt

These changes only affect content that the current user owns:

* **Apply New Permissions** — apply the access permissions of the destination folder to content you own.  
  Example: if moving *My Reports* to *Public*, any user of the system will gain access to the content in *My Reports* you own. The permissions don’t change for content other users own.
* **Keep Existing Permissions** — do not apply the access permissions of the destination folder, retain the permissions the content currently has.  
  Example: if moving *My Reports* to *Public*, only the current user will have access to the items in *My Reports*.
* **Cancel Move** — do not move the folder and leave it in its current location

#### Deleting a Folder

Folders may only be deleted if they are empty.

If someone **other than the owner** deletes a folder, the folder is only deleted for that particular user. This is accomplished by adding a Content Access record that restricts that user’s access to the item.

If the **owner** deletes a folder, it must be first empty for all users of the application. The folder will then by marked deleted for all users.

In both scenarios, the content item remains in the Storage Management database but becomes invisible to certain or all users.

#### Deleting a Report

If someone **other than the owner** of a report deletes it, the item is deleted only for that user. Essentially, it becomes invisible for that user while still remaining available for others.

If the **owner** of the report deletes it, it is removed for all users.

In both scenarios, the content item remains in the Storage Management database but becomes invisible to certain or all users.

## Caching

The Storage Management system can cache the **Report Tree**, the **Report Definition XML** and the **Theme List**. Exago recommends that all three be enabled to reduce the load on the Storage Management database.

## Security Considerations

Information about Database Permissions required for Exago to access the Storage Management database can be found in the [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema) topic.

Information about controlling access to content can be found in the [Permissions](#Permissi) section of this topic.

## Transitioning to Storage Management

Exago has developed several tools for the transition of content from legacy storage mechanisms to Storage Management. The transitioning process and tools are documented in the [Storage Management: Transitioning from Legacy Storage Methods](https://devnet.logianalytics.com/hc/en-us/articles/5281647090839-Storage-Management-Transitioning-from-Legacy-Storage-Methods) topic and in Admin Support Lab — Storage Management Migration.

To migrate from one Storage Management database to another, use the **ImportExportStorageMgmt** command line utility, documented in the [Moving Files Between Storage Management Databases](https://devnet.logianalytics.com/hc/en-us/articles/5281638646807-Moving-Files-Between-Storage-Management-Databases).

## Getting Started

To get up and running quickly with Storage Management, review [Storage Management: Getting Started](https://devnet.logianalytics.com/hc/en-us/articles/5281653081111-Storage-Management-Getting-Started)

## Customization

In addition to Exago’s out-of-the-box implementation clients may write their own implementation of the Storage Management assembly.

Full details are outlined in the [Storage Management: Customization](https://devnet.logianalytics.com/hc/en-us/articles/5281646850327-Storage-Management-Custom-Implementation) topic and in Admin Support Lab — Storage Management Customization.

## Additional Resources

### Support Lab Videos

* Admin Support Lab — Storage Management Overview
* Admin Support Lab — Storage Management Migration
* Admin Support Lab — Storage Management Permissioning
* Admin Support Lab — Storage Management Customization

### Topics

* [Storage Management: Transitioning from Legacy Storage Methods](https://devnet.logianalytics.com/hc/en-us/articles/5281647090839-Storage-Management-Transitioning-from-Legacy-Storage-Methods)
* [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema)
* [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management)
* [Storage Management: Custom Implementation](https://devnet.logianalytics.com/hc/en-us/articles/5281646850327-Storage-Management-Custom-Implementation)
* [REST — Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281630668311-REST-Storage-Management)
* [User Identification](https://devnet.logianalytics.com/hc/en-us/articles/5281619919255-User-Identification)
