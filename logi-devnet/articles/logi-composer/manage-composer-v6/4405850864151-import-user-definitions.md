---
title: "Import User Definitions"
id: 4405850864151
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850864151-Import-User-Definitions
updated_at: 2021-09-21T01:26:33Z
---

# Import User Definitions

# Import User Definitions

You can import users from Lightweight Directory Access Protocol (LDAP) or Active Directory if either protocol has been set up. Authorized users created and stored in these directories can be imported into Composer. You can import all users or select specific ones to add to Composer.

Composer can connect to an organization’s Active Directory (AD) and OpenLDAP directory services using configured LDAP settings. See [*Use Lightweight Directory Access Protocol (LDAP) With Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859462551-Use-Lightweight-Directory-Access-Protocol-LDAP-With-Composer).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Composer supports the auto-provisioning of users via the SAML single sign-on protocol. When auto-provisioning is set up, the user is automatically added when they first log into Composer. For instructions on automatic provisioning of users and groups via SAML, see [*Configure Composer to Support SAML*](https://devnet.logianalytics.com/hc/en-us/articles/4405851175831-Configure-Composer-to-Support-SAML).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg)When a user is imported from Active Directory or if user provisioning is enabled and a new Active Directory user is added, the corresponding Composer user definition is automatically added. However, when a user is removed from Active Directory, the corresponding Composer user definition is not automatically removed. Composer authentication does not occur for the removed user, but you will need to manually remove the Composer user definition. See [*Delete User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405850863255-Delete-User-Definitions).

To import user definitions into Composer from LDAP or Active Directory:

1. Log into Composer as a supervisor and verify that LDAP or Active Directory have been set up. See [*Use Lightweight Directory Access Protocol (LDAP) With Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859462551-Use-Lightweight-Directory-Access-Protocol-LDAP-With-Composer). Be sure to save the settings. Then log out.
2. Log into Composer as a Composer administrator or a user who has been assigned to a group with [user management privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).

   If the user name you log in with is also associated with other Composer accounts, verify that the correct account is selected. See [*Switch Accounts*](https://devnet.logianalytics.com/hc/en-us/articles/4405850869015-Switch-Accounts).
3. Select **Users & Groups** on the [UI menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859444119-The-Composer-UI-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743720343/hamburger.png)). The Users and Groups page appears. It consists of two sections: **Users** and **Groups**.
4. Select the **Users** section to see a list of all the user definitions that have been defined for the account.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743752855/import-users-btn.png). Upon successful access to your organization’s secure directory, a new tab appears listing all the available users that can be imported into Composer. You have the option to either select all users or individual users.
6. On the Import Users tab, select the users to be imported into Composer.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747459351/import-users_480x312.png)
7. Select **Import**. When the import completes, you will see the users added to the user list.
8. On the **Info** tab of the user definition editor, select groups for each user. See [*Specify General User Definition Information*](https://devnet.logianalytics.com/hc/en-us/articles/4405850865047-Specify-General-User-Definition-Information).

   Do **not** change the user login name as this may cause conflicts when reconnections to the LDAP or Active Directory are attempted.

   If you have enabled the auto-creation of groups, Composer creates the groups that user is assigned to if they do not already exist.
9. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747459607/save-blue-supervisor-btn.png) to save the user definition.
