---
title: "Storing Bookmark, Gallery, and Save Files in a Database"
id: 4419707679255
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707679255-Storing-Bookmark-Gallery-and-Save-Files-in-a-Database
updated_at: 2022-07-17T02:24:06Z
---

# Storing Bookmark, Gallery, and Save Files in a Database

# Storing Bookmark, Gallery, and Save Files in a Database

Bookmark, Gallery, and Save files are usually stored as XML files in the web server file system. However, this may not be useful or practical in some Logi application deployments, so it's now possible to store them instead in a SQL database.

Some of the benefits of this approach include making backups easier and eliminating the need for network shares and "sticky" sessions. Logi Studio includes a migration tool that makes it easy to transfer existing bookmark files into a database, and then use them from there.

You can store the following (which we'll collectively call "bookmark files" in this topic)...

* Bookmark Collection files
* Bookmark files
* Gallery files
* Gallery thumbnail files
* Files uploaded with Report Author

...in these databases:

* Microsoft SQL Server 2005+
* MySQL
* Oracle
* PostgreSQL

## Requirements

These are the requirements for migrating and using database bookmark storage. In your \_Settings definition:

1. If one doesn't already exist, add a **Connection** element for the database where your bookmarks will be stored. *Ensure that the account used in the Connection element has sufficient rights to read from, and **write** to, the database*.
2. If not already in use, add and enable the **Security** element and enter a user name in its **Development Username** attribute. For the duration of the bookmark migration operation, grant the *rdBookmarksAdmin* right or role to that user.
3. If you're using Logi **SecureKey** security, set your Security element's **SecureKey Database Connection** attribute to the connection for your bookmark database.
4. Add a **File To Database Mapping** element under the root of your \_Settings definition. When your application needs to read or save a bookmark, this element will "redirect" the command to a database table created for this purpose.

The migration takes place entirely within the context of the application currently open in Logi Studio, you can't use it to migrate files in other Logi applications.

![](https://devnet.logianalytics.com/hc/article_attachments/7522808766103/introbm_42.png)

As shown above, the Mapping element is added in the \_Settings definition.

Its **Folder** attribute is set to a file folder that has been previously configured to store bookmark files. For example, to store bookmarks in the database, this attribute and the **General** element's **Bookmark Folder Location** attribute would be the same, *as long as you do not have any dynamic subfolders* in the BookMark Folder location.. The @Function.AppPhysicalPath~ token can be used in this attribute but other tokens are not allowed.

If you DO have dynamic subfolders(such as in SSRM), then you need to specify it in this way (for example) if:

BookmarkLocation="@Function.AppPhysicalPath~\goBookmarks\UserName@Function.UserName~"

Then your mapping would look like this:

<FileToDatabaseMapping Folder="@Function.AppPhysicalPath~\goBookmarks"

The **Table Name** attribute specifies the database table to be used; if it doesn't exist, it will be created by the migration tool using this value. At a minimum, we recommend that you use a *different* table for each Logi application. Tokens cannot be used here.

The **Connection ID** specifies the database connection to be used. If left blank, the first Connection element found will be used.

The Mapping element's attributes now support tokens.

If you have multiple folders where bookmark files are stored, then add multiple File to Database Mapping elements to include them, and migrate them all to the same database table.

## Migrating Existing Files into the Database

Once the requirements listed above have been met, you need to run Logi Studio's migration tool to create the database table and insert existing bookmark files into it. The migration of existing bookmark files into the database is something you'll do once, to create the table(s) and migrate any existing bookmark files, and won't need to do again.

**Important:** Before you begin this operation, you will have to disable your Security element in the \_Settings.lgx file. Find where security enabled = True, and reset it to **False**, and then save the settings file. Once you have completed the migration, set security enabled back to **True**.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) The migration is a one-way operation: once bookmarks have been stored in the database and used, it's very difficult to accurately revert them back to being stored in files.

![](https://devnet.logianalytics.com/hc/article_attachments/7522839557399/introbm_43.png)

The migration tool is launched from Logi Studio's Tools menu, as shown above, by clicking the Bookmark Storage menu item. Click **Next** to start the migration.

![](https://devnet.logianalytics.com/hc/article_attachments/7522808794007/introbm_44.png)

A gauge and bookmark item counter will display progress as the migration proceeds. Click **Next**, then **Finish** when the migration is complete.

![](https://devnet.logianalytics.com/hc/article_attachments/7522797832855/introbm_45.png)

If you examine your database table, as shown above, you'll see that the files have been copied into it.

If it's not otherwise useful, delete the user name you set in the Security element's **Development Username** attribute and remove the *rdBookmarksAdmin* right/role assignment.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Migration tool can be run without using Studio, using http://<Logi App URI/URL>/rdPage.aspx?rdDebugSession=True&rdForWizard=True&rdReport=rdTemplate/rdMigration URL pattern. Note that same rules for Security, as defined for Studio driven wizard, apply. Please contact [Customer Service](mailto:CustomerService@LogiAnalytics.com) for additional information.

Subsequent new bookmarks and changes to existing bookmarks will now be automatically applied to the table. Requests for the bookmark data will result in a query of the table. Bookmark files are *not* automatically deleted by the migration process, but you may delete them manually if you'd like, as they'll no longer be read or updated.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) It's not recommended but if you do re-run the migration tool later, it will update all of the existing table rows with whatever is in the (possibly "stale") bookmark files and then add any new files. This could result in overwriting newer bookmark table data with the old bookmark file data.
