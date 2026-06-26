---
title: "Team Development Features"
id: 4406818016535
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818016535-Team-Development-Features
updated_at: 2022-04-06T06:09:40Z
---

# Team Development Features

# Team Development Features

Note: This feature is not supported in Info 12.7.

Logi Studio includes two features for use in a **team development** environment, where multiple developers are working on the same Logi application. **File Locking** prevents multiple developers from inadvertently working on the same file at the same time and blocking or overwriting each other's modifications. **File History** retains a copy of each file revision and current versions can be "rolled back" to earlier versions.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575483287/usingstudio_64.png)

As shown above, these features are enabled by adding a **Team Development** element to the application's **\_Settings** definition. The two features, File History and File Locking, are enabled by setting their respective attributes.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575483415/usingstudio_65.png)

When you Save the \_Settings definition, the Team Development features will become enabled. Definitions in the Application panel, including the \_Settings definition, will be shown with a "padlocked" icon, indicating that the files have been locked. Hovering your mouse over the definitions will cause a "File Locked" tooltip to appear. Attributes and their values for elements in those definitions will be shown with gray text, indicating that they cannot be edited.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575483799/usingstudio_66.png)

Individual files can be unlocked, opened, closed, or locked using the pop-up menu options, shown above, that are now available when a file is right-clicked. The file icons will change to reflect a file's locked or unlocked state. Locking applies to text-based **support files** as well as definition
files.

Team Development uses a **source control system** approach, where to unlock a file is to "check it out" and to lock it is to "check it in". This means:

* When no one is working on any file, they are all locked (checked-in) and available to be unlocked (checked-out) by anyone.
* When you unlock (check-out) and open a file, you can edit it, but everyone else is prevented from working with it.
* When you save and/or re-lock (check-in) the file, then it's available to be unlocked by anyone again.

When a file has been unlocked by a user, other users attempting to unlock it will see an "in-use" icon next to the entry in Studio and a tooltip that indicates who's working with this file, when they hover their mouse over it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The initial locked state is *also* applied to the **\_Settings** definition, and you must now unlock it if you want to modify it.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583659287/usingstudio_67.png)

If they've been enabled in the \_Settings definition, File Locking and File History information can be viewed by clicking the **Team Development** menu item, shown above, in the Tools tab.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563009559/usingstudio_68.png)

When the toolbar icon is clicked, the **Team Development**  dialog box opens, as shown above. **File Locking** details are displayed in the first tab, allowing development team members to determine which files are locked, who locked them, and when.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583659543/usingstudio_69.png)

**File History** details are displayed in the second tab. Revision information and the actual revised data are presented. If a particular file is double-clicked, an individual file history dialog box is displayed and it includes a *Rollback...* button, which can be used to replace the current file contents with the selected version's contents.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575484183/usingstudio_70.png)

The Team Development features use a **local****database** file located under the folder "TeamDevelopment", shown above, in the Logi application folder. The folder and database file are automatically created when the Team Development features are enabled

The **Pack Team Development Database**  feature helps to maintain performance. Clicking the appropriate button in the Application History tab will present a prompt for confirmation. Clicking **Yes** will start a process that makes a backup of the Team Development database and then packs and shrinks it. All developers should close the application in Studio before a packing operation is started. You should pack the database whenever you feel that **File History** retrieval is taking
a long time.

These features allow team developers to work together on an application, without getting in each other's way, and provide a useful audit trail of modifications.

## System Configuration

A commonly-used approach for team development is to set up a centralized "development server" where the Logi application files can be accessed, using a shared network folder, by all members of the development team. Logi Info Server is installed on that server, along with a web server and all necessary supporting files. A Logi Info license is required for that server.

Developers who can "map" a local drive to the shared folder on the development server must be given *Read*, *Write*, *Modify*, and *Delete* file access permissions. Developers must also have Logi Info or, at the very least, Logi Studio installed and licensed on their own machines. They then "open" the Logi application on the development server and apply the Team Development settings as outlined above.

In the \_Settings definition, the Path element's **Application Path** attribute should be set to the URL of the Logi app on the development server, rather than to the usual http://localhost/yourApp. Do *not* set the **Alternative Definition Folder** attribute, which is not relevant for this situation.
