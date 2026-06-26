---
title: "Application Folders and Files"
id: 4406818002839
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818002839-Application-Folders-and-Files
updated_at: 2022-04-06T06:09:34Z
---

# Application Folders and Files

# Application Folders and Files

A Logi application is made up of a number of **files** that reside in an application folder group with a specific hierarchy.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563021847/usingstudio_02.png)

The physical folder structure that contains source files is displayed within Logi Studio in the **Application** panel, as shown above left. Standard folders are colored red and cannot be deleted. Files can be *right-clicked* and copied, renamed, and deleted, as shown above right.

Files that are deleted in Studio are placed in the Recycle Bin and can be restored, if desired.

Report definitions can also be designated as the *default* report for an application (this can useful to temporarily make a report the default during development, to avoid having to navigate to it through other reports when testing).

![](https://devnet.logianalytics.com/hc/article_attachments/4417583670039/usingstudio_03.png)

Files can be **added** to the application via the New File toolbar icon or, as shown above, by selecting and right-clicking the destination folder in the Application panel. Right-clicking the folder presents you with the option add a new file or an existing file to the application. If you select *Existing Definition*..., a **copy** of the file will be placed in your application; the original file is left untouched.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583670295/usingstudio_04.png)

You can also **drag** files into, or out of, Studio from, or to, the operating system (from Windows Explorer or the Desktop, for example) or another Studio instance.

In Studio, files are dragged from or dropped onto the file/folder tree in the Application panel. When dropping files, if you don't explicitly drop them onto a folder in the tree, Studio will attempt to place them in the correct folders based on their file extensions. Files can be dragged and dropped within other folders in the file tree.

##### 

Studio also supports a hierarchy of "pseudo folders" for additional file organization purposes. Folders are created by right-clicking any folder, as shown above, and selecting **Add**![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)**New Folder**.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563022359/usingstudio_03b.png)

Creating folders in this manner and then creating or dragging files into them produces the kind of file names shown in the example above. As you can see, no actual folders are created in the file system and the pseudo folders are represented by files that have an .fld extension. In Studio, entire folders can be dragged into other folders to reorganize them.

The following types of files are found in a Logi application:

* **\_Settings** - [The \_Settings Definition](https://devnet.logianalytics.com/hc/en-us/articles/4406817850903-The-Settings-Definition) file provides application-wide configuration information. Paths, constants, data connections, diagnostic settings, etc. are all configured here.

* **Reports** - Report definitions are the basic source code files of a Logi application, with each report definition usually equating to one web page. Individual files, with an .LGX extension, are enumerated here; double-clicking a definition will open it in the definition editor in the Workspace panel. A Master Report, introduced in v12.1 and created using a wizard on the main menu Design tab, is a
  report template that other reports can incorporate. For more information, see [Master Reports](https://devnet.logianalytics.com/hc/en-us/articles/4406817761559-Master-Reports).

* **Mobile Reports** - These are report definitions specifically designed for creating reports for mobile devices.

* **Processes** - Process definitions are a special category of non-presentation source files containing code that executes on the web server. They can contain code for conditional and unattended processing and provide flexibility and coding depth not available in Report definitions.

* **Data** - Data definitions can be used to create an application that retrieves data from a variety of sources and then streams it out as JSON data, to Logi apps, non-Logi apps, and browser clients. See [Data Definitions](https://devnet.logianalytics.com/hc/en-us/articles/4406822229527-Data-Definitions) for more information.

* **Support Files** - These are the files that support the report and process definition files and include style sheets, images, data files, HTML files, and more. See [Support Files Management](https://devnet.logianalytics.com/hc/en-us/articles/4406816928791-Support-Files-Management) for more information.

* **Widgets, Templates** - These folders contain files that are for special purposes.

To edit most files, double-click their name and they'll open in an appropriate editor in the Workspace panel. If you try to open and edit files in proprietary formats, such Excel spreadsheets, they'll open instead in the external application they're associated with in your computer's file system.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583670935/usingstudio_05.png)

In the file system, a basic Logi application looks like the example shown above. All of the files for a single application are contained in one folder, called the "Application folder", which makes deploying the app easy.

In the example above, the bin folder and folders beginning with "rd" are system folders and must be present. Their contents should not be directly edited. The two folders highlighted above are created automatically when the app runs, so don't be concerned if you create a brand new app and don't see them at first. Other folders may also be created on-the-fly, based on
features in your application.

Studio doesn't keep track of application files in a database or repository, so you can directly manage files in the Windows file system by copying, moving, renaming, or deleting them without causing any damage (or course, internal references to specific files may need to be updated). You can always update Studio's list of files by right-clicking any folder and selecting **Refresh Application**.

## Editing Files

Logi Studio includes file type-aware editors for viewing and editing application files.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563022743/usingstudio_06.png)

As shown above, when files are opened they're added to the **Workspace** panel as tabbed panels. The editor for each tab panel is appropriate for its file's type. Features include:

* Tabs can be reordered by dragging them left or right.
* Editors may, depending of file format, include line numbering, color coding, and collapsible regions.
* Elements and text can easily be copied and pasted between files in different tab panels.
* Copying an element also copies all of its child elements.
* Intelligent completion of element names and HTML tags is provided when typing.
* Undo-Redo (Ctrl-Z, Ctrl-Y) is available for all changes made since the last Save.
* The **Preview** panel for definitions includes Forward, Back, Refresh, and Stop buttons.
* Multiple elements that are hierarchical peers in the element tree can be selected at once, then moved or copied as a group.
* Elements have their valid child elements available for selection directly from their (right-click) context menus and from the Element Toolbox panel.

Files are closed, and their tabbed panel removed, by clicking the **X icon** in the tab by the file name. You'll be prompted to save any changes that may have been made.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563022871/usingstudio_07.png)

Tab **context menus**, available by right-clicking, are available, as shown above. The menu options vary based on the type of file being edited in the tab panel.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583671447/usingstudio_08.png)

At the bottom of the Workspace panel are several tabs that appear when editing a *definition*. The **Source** tab provides a view of the definition's underlying XML source code. If an element is selected in the definition when the Source tab is clicked, its corresponding XML tag will be highlighted in the source code, as shown above. Skilled developers can edit or copy-and-paste source directly here if necessary.

Copying the XML source is an easy way to send all or part of the definition to someone else; for example, to another developer or to Logi Support in an email. In fact, just selecting and copying an element right in the element tree itself and then pasting it into a email or another application will result in its XML source code being pasted.
