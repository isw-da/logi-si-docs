---
title: "Support Files Management"
id: 4419700075415
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419700075415-Support-Files-Management
updated_at: 2022-07-17T02:03:11Z
---

# Support Files Management

# Support Files Management

In Logi applications, "Support Files" are defined as files that
are part of an application that are not **Report**, **Process**, or
other definition files. This topic discusses support files and their
management within an application and provides important information about
how files are handled in Studio. Support files generally include:

* Images (.gif, .jpg, .jpeg, .png, .bmp, .wmf, .xbm, .art)
* Style Sheets (.css)
* Script files (.js)
* Data files (.csv, .json, .mdb, .xls, xlsx, .xml)
* HTML files (.htm, .html)

Logi Studio is designed to make managing these files as easy as possible.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706618903/suppfiles_01.png)

In Logi Studio, support files are managed in the **Application** Panel.
The panel displays standard organizational folders for each
category of file in an application, including Support Files. The default
manner in which support files are displayed is shown above left, with all
support files shown together.

In addition to the file types mentioned earlier, you're free to store
other files of other types there, such as .pdf or .docx, if it's
convenient for you.

Right-clicking the Support Files folder title in Studio produces a pop-up
menu, as shown above, right. ![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) Adding an existing file
*copies* the existing file to your project folder; the original file
is left untouched.

The Application Panel displays the files that are included in the
application; there are no Registry entries, tables, or other data
concerning the files maintained by Studio as part of an application. This
lets you move, rename, or delete files *outside* of Studio if you
want to, without causing havoc.

Adding a large number of support files from within Studio could be
time-consuming. To save time in this situation, files can be copied
outside of Studio, using file system tools, directly into the appropriate
folder. The files will automatically appear in Studio the next time the
application is refreshed (using the pop-up menu option), or the
application is closed and re-opened.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714628759/suppfiles_02.png)  

The image above shows a typical collection of files and folders for a
basic Logi application, as they exist in the file system. The top two
folders, highlighted in yellow, correspond to the **Reports** and
**Support Files** folders shown in Studio's Application panel. Other
empty folders shown in Studio, such as Templates, will be physically
created in the file system automatically when they're given some contents
in Studio.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706619159/suppfiles_03.png)

Studio is equipped with special editors in the **Workspace** panel for
the text-based support file types (.css, .js, .json, .xml, .htm, and
.html). Double-clicking these files in the Application panel will open
them in the Workspace panel for editing. If you double-click a non-text
file type, such as .xlsx, it will open in the external application (in
this case Excel) associated with it in the file system.

You can also manage any file (copy, delete, rename, etc.) from within
Studio by right-clicking it, as shown above.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706619415/suppfiles_04.png)

If you wish to further organize your support files, you can do so by
creating a new "folder", as shown above. This is a logical
folder and does not appear in the file system as a separate folder. Here's
how this works: when you create a new logical folder, you can give it a
name, such as "dataXMLs".

Files that you add to that folder from within Studio will appear in the
file system with the folder name pre-pended to their name, with a period
separator. Or, if you're working directly in the file system, to get files
to appear in that folder, just rename them to begin with the folder name
and a period.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699523607/suppfiles_05.png)

So, for example, renaming
sampleTopics.xml
to
dataXMLs.sampleTopics.xml
in the file system will cause it to appear in Studio "inside"
the new dataXMLs folder you created.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png) You're *not* required to manage support files from
within Studio, but by doing so you ensure that all necessary files are
included in the project folder with the proper access permissions,
simplifying deployment. In addition, specifying the location of files
within your report definitions is simplified as the standard support file
folders are "known" to Logi applications.
