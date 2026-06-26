---
title: "About Supplied Group Definitions"
id: 4402955414039
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955414039-About-Supplied-Group-Definitions
updated_at: 2021-08-07T17:29:01Z
---

# About Supplied Group Definitions

# About Supplied Group Definitions

The only non-deletable group supplied with Composer is the **Administrators** group. Users who are assigned to the **Administrators** group for an account are administrators of the account.

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) Management of the supplied **Administrators** group can only be performed by a member of that group or by a user in a group with *all* the following [privileges](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference): **Can Administer Users**, **Can Administer Groups**, and **Can Administer Dashboards**.

You cannot alter the permissions set for this group. However, administrators or users assigned the **Can Administer Groups**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference) can define additional groups with different privilege settings to define the authorization levels required by your organization. See [*Add Group Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4402962858903-Add-Group-Definitions). After the groups are defined, you can assign users to the groups, as appropriate.

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) Beginning with Composer 6.2, the **View All** group is no longer available for *new* Composer installations. If you have upgraded from a previous version, the description for the **View All** group has changed, indicating that the group is no longer a default system group and no longer gives users implicit read-only permissions to all sources in the account. Pre-existing data sources will still be accessible for View All group members, but new data sources will not.
