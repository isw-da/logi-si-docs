---
title: "Manage Support Files"
id: 1500009531901
section: "Info v11 Overview"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531901-Manage-Support-Files
updated_at: 2021-06-17T01:58:38Z
---

# Manage Support Files

# Manage Support Files

In Logi applications, "Support Files" are defined as files that are part of an application that are not **Report**, **Process**, or other definition files. This topic discusses support files and their management within an application and provides important information about how files are handled in Studio. These files generally include:

* Images (.gif, .jpg, .jpeg, .png, .bmp, .wmf, .xbm, .art)
* Style Sheets (.css)
* Script files (.js)
* Data files (.csv, .mdb, .xls, xlsx, .xml)
* HTML files (.htm, .html)

Definitions for Templates and Widgets cannot be included in this category of files. Logi Studio and the support files concept are designed to make managing these files as easy as possible.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771611159/suppfiles_01.png)

In Logi Studio, support files are managed in the **Application** Panel. The panel displays standard **organizational****folders** for each category of file in an application, including Support Files. The default manner in which support files are displayed is shown above left, with all support files shown together.

Right-clicking the Support Files folder icon produces a pop-up menu, as shown above right. Note that adding an existing file *copies* the existing file to your project folder; the original file is left untouched.

The Application Panel displays the files that are included in the application; there are no Registry entries, tables, or other data concerning the files maintained by Studio as part of an application. This allows you to move, rename, or delete files *outside* of Studio without causing havoc.

Adding a large number of support files from within Studio could be time-consuming. To save time in this situation, files can be copied outside of Studio, using file system tools, directly into the appropriate folder. The files will automatically appear in Studio the next time the application is refreshed (using the pop-up menu option), or the application is closed and re-opened.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771611415/suppfiles_02.png)

The image above shows a typical collection of files and folders for a basic Logi application, as they exist in the file system. The top two folders, highlighted in yellow, correspond to the **Reports** and **Support Files** folders shown in Studio's Application panel. Other empty folders shown in Studio, such as Templates, will be physically created in the file system automatically when they're given some contents in Studio.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771611671/suppfiles_03.png)

Studio is equipped with editors in the **Workspace** panel for all support files except images. Double-clicking these files in the Application panel will open them in the Workspace panel for editing. Developers can also manage the files (copy, delete, rename, etc.) from within Studio by right-clicking them, as shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778510231/suppfiles_04.png)

If you wish to further organize your support files, you can do so by creating a new "folder", as shown above. This is a logical folder and does not appear in the file system as a separate folder. Here's how this works: when you create a new logical folder, you can give it a name, such as "dataXMLs".

Files that you add to that folder from within Studio will appear in the file system with the folder name prepended to their name, with a dot separator. Or, if you're working directly in the file
system, to get files to appear in that folder, you rename them to begin with the folder name and a period.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778510487/suppfiles_05.png)

So, for example, renaming sampleTopics.xml to dataXMLs.sampleTopics.xml in the file system will cause it to appear in Studio "inside" the new folder you created.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  You're *not* required to manage support files from within Studio, but by doing so you ensure that all necessary files are included in the project folder, simplifying deployment. In addition, specifying the location of files within your report definitions is simplified as the standard support file folders are "known" to Logi applications.
