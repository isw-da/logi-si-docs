---
title: "Specify General User Information"
id: 43701005878797
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005878797-Specify-General-User-Information
updated_at: 2026-05-29T14:11:44Z
---

# Specify General User Information

# Specify General User Information

When you add or modify a user, you can specify the following general information:

* The login name for the user
* The user's full name
* The user's email address
* The user's password
* Groups to which the user is assigned
* Whether the user is enabled or disabled

This general information is managed on the **Info** tab of the user editor. To access the **Info** tab, see [Add Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051525645-Add-Users) or [Modify Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021873037-Modify-Users). For information on the user settings that can be changed on other tabs, see:

* [Assign and Remove Users in Tenants](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701035684493-Assign-and-Remove-Users-in-Tenants)
* [Specify Custom User Attributes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051547533-Specify-Custom-User-Attributes)
* [Specify A User's Regional Settings](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005924493-Specify-A-User-s-Regional-Settings)
* [Enable and Disable Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021648781-Enable-and-Disable-Users)

In v23.4 of Logi Composer and later, tasks formerly performed by the Supervisor user are now performed by the default system admin and members of the Supervisors group. Any user who belongs to the Supervisors group or to a group with [user management privileges](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) can make changes to the general information of a user's **Info** tab.

**Note:** 
The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.

The following table describes all the information you can change on the **Info** tab. The **Required?** column indicates whether the information is required in a user's definition.

| Tab Field | Required? | Default | Description |
| --- | --- | --- | --- |
| **Login Name** | Yes | --- | The login name for the user. This is also the name for the user definition. The login name must be unique in all accounts in the Composer instance. It must include at least one alphanumeric character.  The login name is used to log into Composer. See [Log Into the Logi Composer UI](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700988311437-Log-Into-the-Logi-Composer-UI) . |
| **Full Name** | No | --- | The full name of the user. Specify up to 40 characters of the user's given name. |
| **Email** | No | --- | The email address of the user. Specify up to 254 characters of the user's email. |
| **Change Password** | Yes | --- | Select the arrow in this box to expand the Info tab and see the **Password** and **Confirm Password** boxes. |
| **Password** | Yes | --- | The password associated with this user name. The password must contain at least nine characters and must include one lowercase, one uppercase, one numeric, and one special character. Special characters include these characters: !@#$%^&\*\*()-\_=+,.:;<> |
| **Confirm Password** | Yes | --- | The password associated with this user name. Use this text box to retype the password you specified in the **Password** text box when you initially create the user definition and when you change the password for the user. |
| **Require password change** | No | Yes | Use the **Require password change** switch to indicate whether the user should be prompted to change their password when they log on for the first time (or the first time after their password was set or changed).  When you create a new user, the **Require password change** switch on the **Info** tab is always on (set to **Yes**), but can be changed to **No**. |
| **Add Groups** | No | --- | Select this button to assign the user to one or more groups in the account. The Add Group(s) dialog appears.  add user to groups dialog  If your user ID is not assigned the **Administer Groups** privilege or is not an administrator, you cannot assign groups to a user. In addition, only administrators can assign users to the **Administrators** group.  Use the search box at the top of the dialog to locate a group name in the list. You can also sort the group names in ascending or descending order using the **Sort By Name** arrows.  After selecting (checking) one or more groups for the user definition, select **Apply** to assign the user to the groups and close the Add Group(s) dialog.  In v23.4 of Logi Composer and later, users who belong to the Supervisors group do not have this field on the Info tab. Update their group membership in the group directly. Navigate to the menu option **Users and Groups**, then select the Group tab to add or remove the user from a specific group in a specific tenant. |
| **Disable User** | No | not checked | This option appears only for administrators or users who are assigned to a group with [user management privileges](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference). Use the **Disable User** checkbox to disable the user.  See [Enable and Disable Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021648781-Enable-and-Disable-Users) . |
