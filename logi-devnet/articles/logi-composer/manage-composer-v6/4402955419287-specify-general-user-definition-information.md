---
title: "Specify General User Definition Information"
id: 4402955419287
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955419287-Specify-General-User-Definition-Information
updated_at: 2021-08-07T17:29:06Z
---

# Specify General User Definition Information

# Specify General User Definition Information

When you add or modify a user definition, the following general information can be specified:

* The login name for the user definition
* The user's full name
* The user's email address
* The user's password
* Groups to which the user is assigned
* Whether the user definition is enabled or disabled.

This general information is managed on the **Info** tab of the user definition editor. To access the **Info** tab, see [*Add User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4402955417367-Add-User-Definitions) or [*Modify User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4402962864663-Modify-User-Definitions). For information on the user definition settings that can be changed on other tabs of the user definition editor, see:

* [*Assign and Remove Users in Composer Accounts*](https://devnet.logianalytics.com/hc/en-us/articles/4402962861335-Assign-and-Remove-Users-in-Composer-Accounts)
* [*Specify Custom User Attributes*](https://devnet.logianalytics.com/hc/en-us/articles/4402955418007-Specify-Custom-User-Attributes)
* [*Specify User Regional Settings*](https://devnet.logianalytics.com/hc/en-us/articles/4402955419927-Specify-User-Regional-Settings)
* [*Enable and Disable User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4402955418647-Enable-and-Disable-User-Definitions)

You can modify the general information for user definitions in a Composer account if you are logged in as a Composer account administrator, a Composer supervisor, or a user who is assigned to a group with [user management privileges](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference).

The following table describes all the information you can change on the **Info** tab. The **Required?** column indicates whether the information is required in a user definition.

| Tab Field | Required? | Default | Description |
| --- | --- | --- | --- |
| **Login Name** | Yes | --- | The login name for the user. This is also the name for the user definition. The login name must be unique in all accounts in the Composer instance. It must include at least one alphanumeric character.  The login name is used to log into Composer. See [*Log Into the Composer UI*](https://devnet.logianalytics.com/hc/en-us/articles/4402955424535-Log-Into-the-Composer-UI). |
| **Full Name** | No | --- | The full name of the user. Specify up to 40 characters of the user's given name. |
| **Email** | No | --- | The email address of the user. Specify up to 254 characters of the user's email. |
| **Change Password** | Yes | --- | Select the arrow in this box to expand the Info tab and see the **Password** and **Confirm Password** boxes. |
| **Password** | Yes | --- | The password associated with this user name. The password must contain at least nine characters and must include one lowercase, one uppercase, one numeric, and one special character. Special characters include these characters: !@#$%^&\*\*()-\_=+,.:;<> |
| **Confirm Password** | Yes | --- | The password associated with this user name. Use this text box to retype the password you specified in the **Password** text box when you initially create the user definition and when you change the password for the user. |
| **Require password change** | No | No | Use the **Require password change** switch to indicate whether the user should be prompted to change their password when they log on for the first time (or the first time after their password was set or changed).  When a supervisor creates a new user, the **Require password change** switch on the **Info** tab is always on (set to **Yes**) and cannot be altered. New users created by a supervisor are required to change their password when they first log into Composer. After the new user has been created, supervisors cannot reset or change the user password. Only Composer administrators can reset or change user passwords. |
|  | No | --- | Select this button to assign the user to one or more groups in the account. The Add Group(s) dialog appears.    If your user ID is not assigned the **Can Administer Groups** privilege or is not an administrator, you cannot assign groups to a user. In addition, only administrators can assign users to the **Administrators** group.  Use the search box at the top of the dialog to locate a group name in the list. You can also sort the group names in ascending or descending order using the **Sort By Name** arrows.  After selecting (checking) one or more groups for the user definition, select **Apply** to assign the user to the groups and close the Add Group(s) dialog. |
| **Disable User** | No | not checked | This option appears only for account administrators or account users who are assigned to a group with [user management privileges](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference). Use the **Disable User** checkbox to disable the user definition in the account. See [*Enable and Disable User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4402955418647-Enable-and-Disable-User-Definitions). |
