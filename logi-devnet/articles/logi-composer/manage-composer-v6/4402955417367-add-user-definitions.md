---
title: "Add User Definitions"
id: 4402955417367
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955417367-Add-User-Definitions
updated_at: 2021-08-07T17:29:05Z
---

# Add User Definitions

# Add User Definitions

Composer account administrators, a Composer supervisor, and account users who are assigned to a group with [user management privileges](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference) can add user definitions to a Composer account.

## When Logged In as a Supervisor

Supervisors can add new users to Composer, with the following caveats:

* The user is not assigned to any groups. Supervisors cannot specify or change a user's group assignments. Only an administrator of the account or a user who has been assigned to an account group with [user management privileges](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference) can assign groups to users in the account.
* When a supervisor creates a new user, the **Require password change** switch on the **Info** tab is always *on* (set to **Yes**) and cannot be altered. New users created by a supervisor are required to change their password when they first log into Composer.
* After a new user has been created, supervisors cannot reset or change the user password. Only administrators or a users who have been assigned to a group with [user management privileges](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference) can reset or change user passwords.

To add a user definition when logged in as a supervisor:

1. Log into Composer as a supervisor. The Manage Users page appears, listing all the user definitions in the Composer instance. If you move from this page, you can always access it by selecting **Users** on the [supervisor menu](https://devnet.logianalytics.com/hc/en-us/articles/4402955649943-The-Composer-Supervisor-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4404952783767/hamburger.png)).
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959577751/new-user-btn_70x21.png). The user definition editor appears on the right side of the page.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404952927767/user-new-supervisor-all_480x311.png)
3. On the **Info** tab, supply values for the user login name, full name, email, and initial password. See [*Specify General User Definition Information*](https://devnet.logianalytics.com/hc/en-us/articles/4402955419287-Specify-General-User-Definition-Information).
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959576599/save-blue-supervisor-btn.png) to save the new user definition. If you do not save the new definition, you cannot access the **Account(s)** and **Regional Settings** tabs for a new user definition.
5. On the **Account(s)** tab, assign the user to one or more Composer accounts and identify the user's primary account. See [*Assign and Remove Users in Composer Accounts*](https://devnet.logianalytics.com/hc/en-us/articles/4402962861335-Assign-and-Remove-Users-in-Composer-Accounts).
6. On the **Regional Settings** tab, select a regional language for the user definition. See [*Specify User Regional Settings*](https://devnet.logianalytics.com/hc/en-us/articles/4402955419927-Specify-User-Regional-Settings).
7. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959576599/save-blue-supervisor-btn.png) to save the user definition.

## When Logged In as an Administrator or a Group User with User Management Privileges

To add a user definition as an administrator or user with user management group privileges:

1. Log into Composer as a Composer administrator or a user who has been assigned to a group with [user management privileges](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference).

   If the user name you log in with is also associated with other Composer accounts, verify that the correct account is selected. See [*Switch Accounts*](https://devnet.logianalytics.com/hc/en-us/articles/4402955425175-Switch-Accounts).
2. Select **Users & Groups** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4402963040407-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4404952783767/hamburger.png)). The Users and Groups page appears. It consists of two sections: **Users** and **Groups**.
3. Select **Users** to see a list of all the user definitions that have been defined for the account.
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952928023/new-user-btn.png). The user definition editor appears on the right side of the page.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404952928279/user-new-supervisor-acct_480x255.png)
5. On the **Info** tab, supply values for the user login name, full name, email, password, and assigned groups. See [*Specify General User Definition Information*](https://devnet.logianalytics.com/hc/en-us/articles/4402955419287-Specify-General-User-Definition-Information). You can also use this tab to disable a user definition. See [*Enable and Disable User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4402955418647-Enable-and-Disable-User-Definitions).
6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959576599/save-blue-supervisor-btn.png) to save the new user definition. If you do not save the new definition, you cannot access the **Custom Attributes** and **Regional Settings** tabs for a new user definition.
7. On the **Custom Attributes** tab, specify custom attributes for the user. See [*Specify Custom User Attributes*](https://devnet.logianalytics.com/hc/en-us/articles/4402955418007-Specify-Custom-User-Attributes).
8. On the **Regional Settings** tab, select a regional language for the user definition. See [*Specify User Regional Settings*](https://devnet.logianalytics.com/hc/en-us/articles/4402955419927-Specify-User-Regional-Settings).
9. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959576599/save-blue-supervisor-btn.png) to save the user definition.
