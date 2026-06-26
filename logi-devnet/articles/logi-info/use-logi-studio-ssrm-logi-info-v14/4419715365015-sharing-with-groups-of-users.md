---
title: "Sharing with Groups of Users"
id: 4419715365015
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715365015-Sharing-with-Groups-of-Users
updated_at: 2022-07-17T02:24:06Z
---

# Sharing with Groups of Users

# Sharing with Groups of Users

Sharing bookmarks with *groups* of users works in a manner similar to the sharing mechanism we've already seen, with two important implementation differences. First, the security configuration must, of course, identify groups and the users that belong to them.

![](https://devnet.logianalytics.com/hc/article_attachments/7522822995351/introbm_25a.png)

The example above shows a simple arrangement of security elements that uses a static datalayer to illustrate the assignment of roles, or "group membership", to users. It's through these elements, whether static or from other sources such as Active Directory, that a user is understood to "belong" to a group. We can see above that user "Roger" belongs to the group "Operations".

![](https://devnet.logianalytics.com/hc/article_attachments/7522812438167/introbm_25b.png)

The second difference is that a Sharing List *must* be used and its configuration needs to include entries for groups, as shown above. ![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) These group names should match those in the security elements in the \_Settings definition.

Your should include a column as a "this user name is really a group name" flag. When this column value is blank, the username column will be understood to be the name of an individual user; when the column has any other value, such as "yes", the username column will be understood to be a group name. The name of the group name flag column is entered into the Sharing List element's **Group Identifier Column** attribute. In the example
above, that would be "isGroup".

![](https://devnet.logianalytics.com/hc/article_attachments/7522812442647/introbm_25c.png)

With groups included in the Sharing List configuration, the sharing pop-up will look like the example shown above, with special icons for groups.

As you might expect, when you share a bookmark with a group, it will be available to all of the users in that group.
