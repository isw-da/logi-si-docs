---
title: "Setting Up Sharing"
id: 4406817205143
section: "Developer Tools - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817205143-Setting-Up-Sharing
updated_at: 2022-04-06T06:04:37Z
---

# Setting Up Sharing

# Setting Up Sharing

If the goAllowSharing constant described earlier has been set to *True*, users can choose at runtime to share their work with other users and/or user groups. To support this, you need to do two things:

First, if you want to share with groups of users, the security configuration must, of course, identify groups and the users that belong to them.

![](https://devnet.logianalytics.com/hc/article_attachments/4417584080791/cfginfogo125_15.png)

The example above shows a simple arrangement of security elements that uses a static datalayer to illustrate the assignment of roles, or "group membership", to users. It's through these elements, whether static or from other sources such as Active Directory, that a user is understood to "belong" to a group. We can see above that user "Roger" belongs to the group "Operations".

![](https://devnet.logianalytics.com/hc/article_attachments/4417584081047/cfginfogo125_16.png)

Second, you must configure the **Sharing List** element in the goBookmarkSharingUserlist definition, shown above. Out of the box, it includes an example based on a static datalayer. For sharing with individual users, that datalayer provides *username* and *department* data values and displays those values in two data table columns that appear in the user interface.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png)The SharingCollectionDisplayColumn property can be used to search for users by their first/last name. The default value is empty. Users can set the property value in goCustomizations.goBookmarkSharingUserlist.lgx. Once shared, the display name is saved in the bookmark and reflected in the Shared With list.

For sharing with groups, you need to include an additional column for the Sharing List data, as shown above, that's a "this user name is really a group name" flag. When this column value is blank, the username column will be understood to be the name of an individual user; when the column has any other value, such as "yes", the username column will be understood to be a group name. The name of the group name flag column is entered into the Sharing List element's **Group Identifier
Column** attribute. In the example
above, that would be "isGroup".

![](https://devnet.logianalytics.com/hc/article_attachments/4417584081175/cfginfogo125_17_498x398.png)

In the InfoGo application, a user will see the pop-up box shown above when they want to share bookmarks. The configuration of the Sharing List element directly affects the box contents.

A drop-down list allows you to filter the list of those with whom a user can share items. The list can be filtered to include People or Groups, or both.

## Editing Shared Items

By default, items that are shared with other users are presented in "read-only" mode to those other users. They can make a copy of them, but they cannot edit the original, shared items. However, other users who have been assigned the InfoGoReportManager security Right, *can* edit the original shared items.

## Bookmark Storage in a Database

Bookmark, Gallery, and Save files are typically stored as XML files in
the web server file system. However, this may not be useful or practical
in some InfoGo deployments, so it's possible to store them
instead in a SQL database. Logi Studio includes a migration tool and a special **File To Database Mapping** element that
make it easy to transfer existing bookmark files into a database, and then use them from there.

For more information about migrating these files, see [Storing Bookmark, Gallery, and Save Files in a Database](https://devnet.logianalytics.com/hc/en-us/articles/4406817598487-Storing-Bookmark-Gallery-and-Save-Files-in-a-Database).
