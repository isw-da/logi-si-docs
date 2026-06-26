---
title: "Storage Management: Utility (v2020.1)"
id: 5281631176983
section: "Deployment"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281631176983-Storage-Management-Utility-v2020-1
updated_at: 2022-05-03T22:08:47Z
---

# Storage Management: Utility (v2020.1)

# Storage Management: Utility (*v2020.1*)

Exago provides the **Storage Management Utility** (**SMU**) to view and manage the content access records and permissions on content items. It is a WPF application and will only run on the Windows family of operating systems. It is only available in English language. The SMU can be downloaded from the Downloads page on our Support Site.

![Hpi0k8o4Ig.png](https://devnet.logianalytics.com/hc/article_attachments/5432207578263/hpi0k8o4ig.png)

The main SMU window

### Recommended Reading

The following topics on the Exago Support Site provide background information for the Storage Management system:

* [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction)
* [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema)
* [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management)

## Configuration

### Initial Setup

When first launched, the **Storage Management Utility** must be configured to connect to the Storage Management database.

1. On the menu bar, click on **Config** to open the **Options** dialog.
2. In the list of profiles on the left, click on *Default* to load the default profile.
3. In the **Database Connection** section on the right, enter in the details to connect to the Storage Management database. These values can be found in the Exago **Admin Console** > **Storage Management** section.
   * **Name** — enter a friendly name to reference this profile, or leave as *Default*
   * **Type** — select the type of database either *Microsoft SQL Server*, *MySQL*, *SQLite*, *Oracle* or *PostgreSQL*
   * **Driver** — enter the database provider (driver) to use to connect to the database
   * **Connection** — enter the connection string
   * **Content** — enter the name of the content table
   * **Access** — enter the name of the content access table
   * **Party Type** — enter the name of the party type table
   * **Meta** — enter the name of the storage meta table
4. Click **Save** to save the profile to the configuration.
5. Click **Ok** to choose the profile and close the Options dialog.

The configuration file is saved to `%APPDATA%\Exago\StorageMgmtQuery.json`, where `%APPDATA%` represents the Windows environment variable with the current user’s AppData directory path. For example, `C:\Users\Astro Boy\AppData\Roaming\Exago`.

### Managing Profiles

Any number of database profiles may be saved in the configuration and recalled at a later time.

#### Creating a New Profile

1. On the menu bar, click on **Config** to open the **Options** dialog.
2. Click **New** to create a new profile.
3. Resume from Step 3 in the [Initial Setup](#Initial).

#### Editing a Profile

1. On the menu bar, click on **Config** to open the **Options** dialog.
2. Select a profile from the list by clicking on it. The currently active profile always appears at the top of the list.  
   ![q1yMrtgPmP.png](https://devnet.logianalytics.com/hc/article_attachments/5432159415575/q1ymrtgpmp.png)
3. Make changes as desired.
4. Click **Save** to save the changes to the profile.

#### Deleting a Profile

1. On the menu bar, click on **Config** to open the **Options** dialog.
2. Select a profile from the list by clicking on it.
3. Click **Remove**.

## User Interface

### Menu Bar

![CGxwsVVPJj.png](https://devnet.logianalytics.com/hc/article_attachments/5432207712407/cgxwsvvpjj.png)

The Title and Menu bars at the top of the window

The **Menu Bar** contains four selectable options to control the application:

* **Reload** — connect to the Storage Management database and refresh the **Content Tree** with its content
* **Config** — open the **Options** dialog to create, edit or view configuration profiles
* **Filter** — filter the items in the **Content Tree** by name, content ID, content type, report type, deleted or empty status. See [Filtering the Content Tree](#Filterin) for more information.
* **Help** — open Help content (display this topic)

### Content Tree

![mstsc_TU33GmVhBt.png](https://devnet.logianalytics.com/hc/article_attachments/5432180518551/mstsc_tu33gmvhbt.png)

Content tree in the SMU showing several folders, reports and some deleted items

The left side of the SMU window is the **Content Tree**. The Content Tree lists all of the content items in the database’s **content** table in alphabetical order.  The tree is refreshed when the **Reload** item is clicked on the menu bar.

Content in the tree is identified by icons:

* ![TreeFolder.png](https://devnet.logianalytics.com/hc/article_attachments/5432207849111/treefolder.png) — this item is a folder
* ![TreeAdvancedReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432192105239/treeadvancedreport.png) — this item is an **Advanced Report** or a **CrossTab**
* ![TreeChainedReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432180048407/treechainedreport.png) — this item is a **Chained Report**
* ![TreeDashboardReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432192292631/treedashboardreport.png) — this item is a **Dashboard**
* ![TreeExpressReport.png](https://devnet.logianalytics.com/hc/article_attachments/5432173711639/treeexpressreport.png) — this item is an **Express Report**
* ![TreeExpressView.png](https://devnet.logianalytics.com/hc/article_attachments/5432206928151/treeexpressview.png) — this item is an **ExpressView**
* ![SettingsMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432122354839/settingsmenu.png) — this item is either a theme or a template
* ![TreeCustomOptionNumeric.png](https://devnet.logianalytics.com/hc/article_attachments/5432174475799/treecustomoptionnumeric.png) — this item has multiple content access records

Items that appear with strike-through text have been deleted by the content owner (the deleted flag is *true*).

The top of the **Content Tree** will always have a folder name ROOT, which is the parent of all other content items in the system. Clicking on any item in the **Content Tree** except for the ROOT will load the details for that content item into the **Detail Pane** on the right side of the window.

Themes and template files will appear in “pseudo folders”, named [Themes] and [Templates] respectively. These folders do not actually exist, they only appear in the Storage Management Utility for organization purposes. Themes and templates are actually stored in the root directory in the Storage Management database.

#### Filtering the Content Tree

To filter the items displayed in the **Content Tree:**

![MD2Nr7mnm3.png](https://devnet.logianalytics.com/hc/article_attachments/5432159574679/md2nr7mnm3.png)

Filter Criteria dialog

1. Click **Filter** in the Title and Menu Bar to open the **Filter Criteria** dialog.
2. Enter one or more criteria to filter by:
   * **Name** — the name of the item as it appears in the Exago BI application
   * **Content Id** — the GUID that uniquely identifies this content item in the system
   * **Content Type** — the type of content to show either *Folder*, *Report*, *Theme,**Template* or *All*
   * **Report Type** — the type of report to show either *Chained*, *Dashboard*, *Express*, *ExpressView* or *Advanced* or *Visualization*. Only applicable if **Content Type** is *Report* or *All*. *Visualization* is not a currently supported report type in the system and should not be selected.
   * **Hide Deleted** — check this checkbox to hide any content items that have been marked deleted by the content owner (that is the item’s deleted flag is true). Items individually deleted by non-owners will still appear as content access records.
   * **Hide Empty Folders** — check this checkbox to hide folders that appear empty in the Content Tree. A folder is considered empty if it contains no content or if other filter criteria hides any content.
3. Click the **Filter** button to apply the filters to the content tree, or click **Cancel** to erase the changes to the dialog. The dialog will close.

##### Clearing Filters

To clear filters and show the entire Content Tree again:

1. Click **Filter** in the Title and Menu Bar to open the **Filter Criteria** dialog.
2. Click the **Clear** button. The filters will be removed and the dialog will close.

### Detail Pane

The right side of the SMU window is the **Detail Pane**. The Detail Pane allows viewing and editing of the  access records for content items. It is divided into two tabs: **Details** and **Report Contents**.

![tipunmyL9b.png](https://devnet.logianalytics.com/hc/article_attachments/5432174588823/tipunmyl9b.png)

**Details** and **Report Contents** tabs at the top of the Detail Pane

#### Report Contents tab

The **Report Contents** tab will display the XML report definition content when a report is selected in the Content Tree. It will appear blank if any other content type is selected.

With an XML report definition displayed, the three buttons along the top of the tab become active:

![FN96ISlph1.png](https://devnet.logianalytics.com/hc/article_attachments/5432180760343/fn96islph1.png)

Report Contents buttons

* **Save** — save any changes made to the XML back to the Storage Management database
* **Write To** — save the displayed XML content to a local disk file (similar to the **Download ![Download.png](https://devnet.logianalytics.com/hc/article_attachments/5432193118615/download.png)** function in the Exago Web Application)
* **Load From** — read an XML report definition from a local disk file into the tab (similar to the **Upload ![Upload.png](https://devnet.logianalytics.com/hc/article_attachments/5432174691991/upload.png)** function in the Exago Web Application)

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> Remember to click **Save** after loading content with the **Load From** function to save the content to the database.

#### Details tab

The **Details** tab displays content item information.  It is further divided into four panels:

![detail-numbered.png](https://devnet.logianalytics.com/hc/article_attachments/5432122517015/detail-numbered.png)

Anatomy of the SMU Detail Pane Details tab

1. **Selected Item** — displays the content metadata for the selected item, loads the content access records into the **4. Access Records** panel
2. **Parent** — displays the content metadata for the selected item’s parent item (that is the folder this content item is stored in) based on the currently selected **4. Access Record**
3. **Access Rights** — works in conjunction with the **4. Access Records** panel to display the access rights for the currently selected access record
4. **Access Records** — displays all of the content access records on the selected content item

##### 1. Selected Item

The **Selected Item** panel displays metadata saved in the Storage Management system’s content table for the currently selected item in the **Content Tree**.

* **Name** — the name of the item as it appears in the Exago BI application
* **Content Id** — the GUID that uniquely identifies this content item in the system
* **Content Type** — the type of content this item is, either *Folder*, *Report*, *Theme* or *Template*
* **Report Type** — only displayed when **Content Type** is *Report*. Displays the type of report this content item is. Either *Chained*, *Dashboard*, *Express*, *ExpressView* or *Advanced*.  
  > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
  >
  > CrossTabs are considered Advanced Reports.
* **Owner** — the value of the **Owner Id** identity key when this content item was created
* **Attribute** — only displayed when **Content Type** is *Theme.*Displays the component in the application the theme applies to. Either *ExpressView*, ExpressView\_v2, *Express Report*, *CrossTab*, *Chart*or *Map*.
* **Default Access Rights** — only displayed for folders. Displays the value for each of the Access Flags that will be applied to new content created in the folder.
* **Default Party Type** — only displayed for folders. Displays the default party type that will be applied to new content created in the folder. Can be changed by selecting a different value from the dropdown.
* **Additional Flags** — only displayed for folders and reports (although **Deleted** will appear for templates and themes). Displays or sets the values of certain flags on the content item:
  + **Inherit Access** — only displayed for folders. Displays the value of the folder’s **inherit flag** which determines if content access records are copied from the folder to new content created in the folder. Can be changed by checking/unchecking the checkbox.
  + **Deleted** — Displays the value of the item’s **deleted flag** which indicates the item was deleted by the content owner and should not be visible to any user of the system. Can be changed by checking/unchecking the checkbox.
* **Description** — only displayed for Reports. Displays the description field for a report
* **Created By** — only displayed for Reports. The value of the **User Id** identity key when this report was created
* **Created Date** — only displayed for Reports. The UTC timestamp at the instant when this report was created
* **Modified By** — only displayed for Reports. The value of the **User Id** identity key when this report was last saved
* **Modified Date** — only displayed for Reports. The UTC timestamp at the instant when this report was last saved

If the **Access Flags**, **Default Party Type** or **Additional Flags** are changed, the word **Changes** will appear in red at the top of the panel. Changes can be saved by clicking on the **Save** button in the top right corner. Doing so will write the changes to the Storage Management database immediately.

##### 2. Parent

The **Parent** panel displays metadata saved in the Storage Management system’s content table for the currently selected item’s parent in the **Content Tree**.

* **Name** — the name of the item as it appears in the Exago BI application
* **Content Id** — the GUID that uniquely identifies this content item in the system
* **Content Type** — the type of content this item is, either *Folder*, *Report*, *Theme* or *Template*
* **Owner** — the value of the **Owner Id** identity key when this content item was created
* **Default Access Rights** — only displayed for folders. Displays the value for each of the Access Flags that will be applied to new content created in the folder.
* **Default Party Type** — only displayed for folders. Displays the default party type that will be applied to new content created in the folder. Can be changed by selecting a different value from the dropdown.
* **Additional Flags** — only displayed for folders and reports. Displays or sets the values of certain flags on the content item:
  + **Inherit Access** — only displayed for folders. Displays the value of the folder’s **inherit flag** which determines if content access records are copied from the folder to new content created in that folder.
  + **Deleted** — Displays the value of the item’s **deleted flag** which indicates the item was deleted by the content owner and should not be visible to any user of the system.

##### 3. Access Rights

![ZYRgytC3yu.png](https://devnet.logianalytics.com/hc/article_attachments/5432193235863/zyrgytc3yu.png)

Access Rights panel in Detail Pane

The **Access Rights** panel displays the **party type**, **party id**, **sort order** and **access flags** of the currently selected item in the 4. Access Records panel.

* **Party Type** — displays the access record’s party type. Can be changed by selecting a different value from the dropdown.
* **Party Id** — displays the access record’s party id. This is the value of the **Party Type** that this record applies to. Can be changed by entering a new value into the text box.
* **Sort Order** — displays the access record’s sort order value. Can be changed by entering a new value into the text box.
* **Access Flags** — displays the access flags as a hexadecimal value. Can be changed by altering the nine checkboxes.
* **Checkboxes** — set or unset the various access flags.

Whenever changes are made, the word **Changes** will appear in red at the top of the panel. Changes can be saved by clicking on the **Save** button in the top right corner, doing so will write the changes to the Storage Management database immediately.

![rLVfFKJbnX.png](https://devnet.logianalytics.com/hc/article_attachments/5432122567063/rlvffkjbnx.png)

Pending changes in the Access Rights panel

##### 4. Access Records

![yd460J0lyk.png](https://devnet.logianalytics.com/hc/article_attachments/5432208513559/yd460j0lyk.png)

The Access Records panel in this figure is displaying four **Class** level records and one **User** level record

The **Access Records** panel displays all of the content access records that exist for a particular content item, based on the content’s **content id**.

Clicking on any of the records in the panel will update the 3. Access Rights panel with that record’s information, as well as highlighting the location of the content item in the Content Tree. Since content can appear in different folders for different parties, it may be in different locations in the tree for different records.

* **Party Type** — the party type name from the party type table that this content access record applies to
* **Party Id** — the value of the identity key that correlates with the **Party Type** that this content access record applies to
* **Access Flags** — displays the access flags as a hexadecimal value.
* **Parent** — the content ID of the parent that contains this content item for this particular party
* **Parent** — the name of the parent that contains this content item for this particular party

### Status Bar

The **Status Bar** at the bottom of the SMU window displays information about the utility’s communication with the Storage Management database and the local file system, the loaded configuration and the version number of the utility.

![VfCnNuIyuD.png](https://devnet.logianalytics.com/hc/article_attachments/5432181038359/vfcnnuiyud.png)

Status bar message indicating the Content Tree was last refreshed at 8:45:28 PM

The status bar is broken up into three zones:

1. Messages
2. The name of the currently loaded configuration profile. In the figure above, the currently loaded profile is named *My SM Test Environment*.
3. The version number of the Storage Management Utility

Messages in the status bar are always accompanied with a timestamp indicating when the operation was completed.

* **Reload** — the Content Tree has been refreshed with content from the Storage Management database
* **Save contents to <local path>** — XML report definition has been saved to a local disk file. <local path> will be replaced with the actual path and name of the saved file.
* **Loaded contents from <local path>** — XML report definition has been loaded from a local disk file. <local path> represents the path and name of the file that was loaded from the local file system.
* **Saved Report Specification for <report name>** — the XML report definition has been saved to the Storage Management database. <report name> represents the name of the report in the Content Tree that was saved.
* **Saved Access Data for <report type> for parent <content id>** — changes made in the 4. Access Records panel have been saved to the Storage Management database. <report type> and <content id> will be replaced with the type of report and the parent’s content ID respectively.
* **Saved Content Data for <report type>** — changes made in the 1. Selected Item panel have been saved to the Storage Management database. <report type> will be replaced with type of report that was changed.

[![Concept Link Icon](https://devnet.logianalytics.com/hc/article_attachments/5432159914263/transparent.gif)See Also](javascript:void(0);)
