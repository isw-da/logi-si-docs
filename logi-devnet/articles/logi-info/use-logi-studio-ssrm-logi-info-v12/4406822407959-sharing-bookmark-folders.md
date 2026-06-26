---
title: "Sharing Bookmark Folders"
id: 4406822407959
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822407959-Sharing-Bookmark-Folders
updated_at: 2022-04-06T06:07:05Z
---

# Sharing Bookmark Folders

# Sharing Bookmark Folders

Entire bookmark folders can also be shared with other users:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563203095/introbm_19.png)

When sharing is enabled and you hover your mouse over sub-folders in the Bookmark Organizer, you'll see the built-in sharing icon, as shown above. The icon color indicates whether the folder has been shared with anyone.

A special *Shared with Me* folder will appear containing the folders, if any, that others have shared with you. Click the **shared folders** to see their contents and run the bookmarks. You can hover your mouse over them to see who shared them with you.

Clicking a sub-folder's green or black **sharing icon** will display the same Share pop-up panel used when sharing bookmarks. In it, you can see who you've shared the folder with, share the folder with others, and revoke sharing. The *My Items* personal folder cannot be shared.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png) If your application has been configured for it, you will receive a notification on the SSRM Home Page when an item is shared/unshared with you:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563202199/new_bell_icon_1244x181.png)

Selecting this notification will display information about the author and shared folder. Select the **shared item** to access the folder:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575628823/actionable_notification_folder_share.png)

## Shared Folder Shortcuts

Suppose a folder shared with you is many levels of sub-folders deep and it's a nuisance to have to drill-down to it every time you need to use its bookmarks. The *shared folder shortcut* can make life easier for you in this case. This is created by drilling-down to the shared folder you want and then dragging it onto one of your personal folders:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563203223/introbm_22.png)

This action creates the folder shortcut, as shown above. ![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The shortcut has a special "shared folder" icon and that, by clicking its gear icon, you can rename it or remove it.

## Implementation

Assuming you've already implemented the Bookmark Organizer, here's how to implement bookmark sharing:

1. Ensure that some variety of **Logi Security** is being used.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575629079/introbm_23.png)

2. Set your **Bookmark Organizer** element's **Allow Sharing** attribute to *True* (tokens may be used here), as shown above.  
     
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417583853207/introbm_24.png)

3. Next, decide if you want to provide users with a pick-list of other users with whom they can share folders. This is determined by the addition of the **Sharing List** element beneath Bookmark Organizer. Referring to the images shown above:  
     
   *Without* the Sharing List element, user names can be typed-in and will be compared to the names associated with all of the existing personal bookmark collections. A type-ahead feature helps filter the available names.  
     
   *With* the Sharing List element, user names are displayed in an embedded table, as shown above right, and the names come from a datalayer. If a user in the table doesn't have a personal bookmark collection yet, one will be created for her automatically if a folder is shared with her.  
     
     
     
   ![](https://devnet.logianalytics.com/hc/article_attachments/4417563203735/introbm_25.png)  
     
   The example above shows the **Sharing List** element in use. As a special type of data table, it gives developers some control over the contents and formatting of the list. Any type of datalayer can be used and users are selected by clicking table rows. The Share pop-up panel will automatically expand to fit the width of the table. Specify the name of the datalayer column containing the user names in the Sharing List element's **Sharing Collection Column**
   attribute.

Your bookmark folder sharing functionality is now ready for use. Here's a testing tip:

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) In your \_Settings definition, use the **Security** element's **Development Username** attribute to run the application as different users in order to see that individual bookmark folders are created and shared correctly.
