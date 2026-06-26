---
title: "Supplied User Definitions"
id: 4405859125911
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859125911-Supplied-User-Definitions
updated_at: 2021-09-21T01:26:34Z
---

# Supplied User Definitions

# Supplied User Definitions

Composer supplies two user definitions: **supervisor** and **admin**. Use these two users to define other users and Composer accounts and to enable security features and define user groups and privileges. These supplied user definitions cannot be deleted.

After Composer has been installed and deployed in your operating environment, a Composer administrator accesses the application from a WebSocket-supported web browser (see [System Requirements](https://devnet.logianalytics.com/hc/en-us/articles/4405859384727-System-Requirements) for details). When you initially access the product, Composer prompts you to change the passwords for the **supervisor** and **admin** users.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743936535/login-initial_138x212.png)

## The `admin` User

The supplied **admin** user is defined as a Composer administrator (in the [**Administrators** group](https://devnet.logianalytics.com/hc/en-us/articles/4405859110935-About-Supplied-Group-Definitions)) for the [supplied Composer company account](https://devnet.logianalytics.com/hc/en-us/articles/4405859102999-About-the-Supplied-Composer-Accounts). The supplied **admin** user cannot be deleted.

The first time you log into the Composer UI as the **admin** user, you are prompted to change the **admin** user password. Thereafter, you can change the password for the **admin** user only if you are logged into the Composer UI as an administrator. See [*Change Passwords*](https://devnet.logianalytics.com/hc/en-us/articles/4405859113623-Change-Passwords).

Other users can be defined as Composer administrators or can be assigned to groups with some administrator privileges. See [*Add User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405850861463-Add-User-Definitions), [*About Supplied Group Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859110935-About-Supplied-Group-Definitions), and [*Group Privilege Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).

## The `supervisor` User

Your Composer installation (whether stand-alone or scale-out) provides one supervisor user. This user definition is permanent and cannot be deleted. However, it can be disabled (see [*Enable and Disable the Supplied Supervisor User*](https://devnet.logianalytics.com/hc/en-us/articles/4405859124759-Enable-and-Disable-the-Supplied-Supervisor-User)).

Other users can be defined as Composer supervisors. See [*Add and Remove Supervisors*](https://devnet.logianalytics.com/hc/en-us/articles/4405859123479-Add-and-Remove-Supervisors).

Supervisors should be used to make account-level changes to Composer (such as configuring SAML). Limit the availability of this access level to personnel responsible for managing Composer.

Supervisors can:

* Manage users, their regional definitions, and the accounts to which they are assigned. They cannot assign users to groups. User definitions created by a supervisor are not assigned to any groups, by default.

  When a supervisor creates a new user, the **Require password change** switch on the **Info** tab is always *on* (set to **Yes**) and cannot be altered. New users created by a supervisor are required to change their password when they first log into Composer. After the new user is created, supervisors cannot change or reset the user password.
* Manage Composer accounts, including creating, removing, enabling, and disabling accounts. Except when initially creating an account, supervisors cannot change or assign administrators to the account.
* Customize the Composer interface
* Configure security settings
* Manage connectors
* Manage Composer licenses

The supplied **supervisor** user can only be assigned to the [Composer superaccount](https://devnet.logianalytics.com/hc/en-us/articles/4405859102999-About-the-Supplied-Composer-Accounts). It cannot be assigned to any other Composer accounts.
Supervisor users you create can be assigned to the superaccount as well as other accounts.

The first time you log into the Composer UI as the supplied **supervisor** user, you are prompted to change the **supervisor** password. Thereafter, you can change the password for the **supervisor** user only if you are logged into Composer as the **supervisor**. See [*Change a Supervisor Password*](https://devnet.logianalytics.com/hc/en-us/articles/4405859111959-Change-a-Supervisor-Password).
