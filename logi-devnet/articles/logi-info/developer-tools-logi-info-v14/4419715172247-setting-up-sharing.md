---
title: "Setting Up Sharing "
id: 4419715172247
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715172247-Setting-Up-Sharing
updated_at: 2022-07-17T02:24:54Z
---

# Setting Up Sharing 

# Setting Up Sharing

If the goAllowSharing constant described earlier has been set to *True*, users can choose at runtime to share their work with other users and/or user groups. To support this, you need to do two things:

First, if you want to share with groups of users, the security configuration must, of course, identify groups and the users that belong to them.

![](https://devnet.logianalytics.com/hc/article_attachments/7522847984407/cfginfogo125_15.png)

The example above shows a simple arrangement of security elements that uses a static datalayer to illustrate the assignment of roles, or "group membership", to users. It's through these elements, whether static or from other sources such as Active Directory, that a user is understood to "belong" to a group. We can see above that user "Roger" belongs to the group "Operations".

![](https://devnet.logianalytics.com/hc/article_attachments/7522854062103/cfginfogo125_16.png)

Second, you must configure the **Sharing List** element in the goBookmarkSharingUserlist definition, shown above. Out of the box, it includes an example based on a static datalayer. For sharing with individual users, that datalayer provides *username* and *department* data values and displays those values in two data table columns that appear in the user interface.

The SharingCollectionDisplayColumn property can be used to search for users by their first/last name. The default value is empty. Users can set the property value in goCustomizations.goBookmarkSharingUserlist.lgx. Once shared, the display name is saved in the bookmark and reflected in the Shared With list.

For sharing with groups, you need to include an additional column for the Sharing List data, as shown above, that's a "this user name is really a group name" flag. When this column value is blank, the username column will be understood to be the name of an individual user; when the column has any other value, such as "yes", the username column will be understood to be a group name. The name of the group name flag column is entered into the Sharing List element's **Group Identifier
Column** attribute. In the example
above, that would be "isGroup".

![](https://devnet.logianalytics.com/hc/article_attachments/7522755610135/sharing_dialog_box.png)

In the InfoGo application, a user will see the pop-up box shown above when they want to share bookmarks. The configuration of the Sharing List element directly affects the box contents.

A drop-down list allows you to filter the list of those with whom a user can share items. The list can be filtered to include People or Groups, or both.

![](https://devnet.logianalytics.com/hc/article_attachments/7522745474327/_newplus.jpg) New for 14.1 As a content creator, you can now manage access for content shared with other users at the bookmark level. Access types include "Read" or "Interactive". If you are sharing a report, selecting the "Interactive" permission allows the user you are sharing the report with to schedule the report. Granting an “Interactive” permission when sharing a Dashboard or Analysis allows the user to drill-to and apply filters to the shared content; however, they will not be able to save these changes to the original content, as this can only be done through specific security roles. Note that you must select at least one access type to share content. Selecting the "Interactive" permission automatically selects the "Read" check box, as well. You can edit these permissions by checking/unchecking the corresponding check boxes. Deselecting the "Read" check box will automatically uncheck the "Interactive" check box (if it was selected), and in this case, would unshare the content entirely. Schedules launched by the shared user will be removed if their permission changes to "Read". Likewise, if the report or folder is unshared with that user, schedules launches by the shared user will be removed.

As an administrator, you have the ability to disable/enable the sharing permission feature using a constant. To enable sharing, update the constant goSharePermissionEnable to "True". By default, this constant is set to "False".

![](https://devnet.logianalytics.com/hc/article_attachments/7522832156055/enabl_sharing_permission.png)

![](https://devnet.logianalytics.com/hc/article_attachments/7522755629847/noteicon.jpg)

* If you change the constant to "False" after someone has shared a schedule or bookmark using the Interactive permission, the permission will change back to Read-Only.

* The "Interactive" permission is different from edit, described below, as it does not support saving changes back to original bookmark.

For more information, see [InfoGo - Sharing Your Work](https://devnet.logianalytics.com/hc/en-us/articles/4419723216663-InfoGo-Sharing-Your-Work-).

## Editing Shared Items

By default, items that are shared with other users are presented in "read-only" mode to those other users. They can make a copy of them, but they cannot edit the original, shared items. However, other users who have been assigned the InfoGoReportManagersecurity Right, *can* edit the original shared items.

## Bookmark Storage in a Database

Bookmark, Gallery, and Save files are typically stored as XML files in
the web server file system. However, this may not be useful or practical
in some InfoGo deployments, so it's possible to store them
instead in a SQL database. Logi Studio includes a migration tool and a special **File To Database Mapping** element that
make it easy to transfer existing bookmark files into a database, and then use them from there.

For more information about migrating these files, see [Storing Bookmark, Gallery, and Save Files in a Database](https://devnet.logianalytics.com/hc/en-us/articles/4419707679255-Storing-Bookmark-Gallery-and-Save-Files-in-a-Database).
