---
title: "Supplied Users and User Groups"
id: 43701036219149
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups
updated_at: 2026-05-29T14:07:07Z
---

# Supplied Users and User Groups

# Supplied Users and User Groups

Composer supplies one user: **[admin](#The2)**. The admin is the default system administrator, who can define other users and tenants, enable security features, and define user groups and privileges. To add more system administrators, create or add users to the Administrators group, Supervisors group, and Content Distributors group. When they belong to all three groups, they can perform all of the same functions as the default system admin.

**Note:** 
If you are installing or upgrading to v23.4 or later, the default admin user (system administrator) can perform all functions the former supervisor user previously performed, and provide authentication for embedded use cases.

After you've install and deployed Composer in your operating environment, access the application as the admin user from a web browser (see [System Requirements](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105740685-System-Requirements) for details).

## admin User

The supplied **admin** user is defined as a system administrator and is a member of the Administrators group, the Supervisors group, and the Content Distributors group for the [supplied tenant](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021083277-About-the-Supplied-Composer-Tenant). The **admin** user cannot be deleted.

The first time you log into the UI as the **admin** user, you are prompted to change the **admin** user password. Thereafter, you can change the password for the **admin** user only if you are logged into the UI as an administrator. See [Change Passwords](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005569933-Change-Passwords).

Other users can be defined as administrators or can be assigned to groups with some administrator privileges. See [Add Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051525645-Add-Users), [About Supplied Groups](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021357837-About-Supplied-Groups), and [Group Privilege Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).

## Administrators Group

Administrators group members include the [default admin user](#The2), who is a system administrator associated with the *Visual* Data Discovery tenant (formerly the *superaccount*).

Assign users to the Administrators group to give them administrative privileges to perform actions such as:

* Create and manage users and groups.
* Manage connectors.
* Create and manage custom charts.
* Access actions.

**Note:** 
The Administrators group is an integral part of Composer management. Users in the group can be system administrators, and tenant admins for one or more tenants.

**Note:** 
Management of the supplied **Administrators** group can only be performed by a member of that group or by a user in a group with *all* the following [privileges](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference): **Administer Users**, **Administer Groups**, and **Administer Dashboards**.

See [Add Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051525645-Add-Users), [About Supplied Groups](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021357837-About-Supplied-Groups), [Group Privilege Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), and[The Composer UI Menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu).

## Administrators Group (Tenant Admins)

Administrators group members in tenants can:

* Create and manage users, groups, and content in their tenants.
* Define custom charts in their tenants.
* Perform Console and Actions related tasks.
* Logi Composer users can be added as system admins and tenant admins in your environment.

## Supervisors Group

The Supervisors group is designed to give you a group of users who can perform specific functions without giving them access to all tasks members of the Administrators group can perform in.

Assign users to the Supervisors group to allow those users to:

* Manage tenants, including creating, removing, enabling, and disabling tenants. Except when initially creating a tenant, supervisors cannot change or assign administrators to the tenant.
* Manage the look and feel of your software environment.
* Manage product licenses.
* Manage connectors.
* Enable security privileges, and more.

If you'd like a user to be a full system admin, add them to this group and the Content Distributors group as well. See [About Supplied Groups.](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021357837-About-Supplied-Groups)

## Content Distributors Group

The Content Distributors group is part of the Visual Data Discovery tenant. Members can create, maintain, and distribute content and objects such as sources and connections to all tenants in your environment.

If you'd like a user to be a full system admin, add them to this group and the Supervisors group as well. See [About Supplied Groups.](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021357837-About-Supplied-Groups)

See [About Supplied Groups.](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021357837-About-Supplied-Groups)
