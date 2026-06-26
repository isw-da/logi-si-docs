---
title: "About Supplied Groups"
id: 43701021357837
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021357837-About-Supplied-Groups
updated_at: 2026-05-29T14:07:05Z
---

# About Supplied Groups

# About Supplied Groups

Several default groups are supplied with Composer. Add users to these groups to allow them to perform specific tasks related to the tenant(s) they may belong to in your environment . You can't delete, rename, or edit the privileges of these default groups. Add users as needed to each group, or [add more groups](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005381517-Add-User-Groups) to accommodate your organization's needs.

* **Administrators** - Group members include the [default admin user](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups#The2), who is a system administrator assigned to the Visual Data Discovery tenant (formerly the *superaccount*). If your environment includes tenants, each tenant includes an administrators group: all tenant admins belong to that group.

  **Note:** Composer v23.4 and later does not include a supervisor user. Add users to the Supervisors group.
* **Supervisors** - Add users as group members to allow them to perform specific functions without giving them access to reserved administrator tasks. Only the supplied [admin user](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups#The2) or other system administrator can add users to this group.
* **Content Distributors** - Add users as group members to allow them to create, maintain, and distribute content to any tenant.

  **Important:** 
  If you use the Content Distributors group, add them to [another user group you define](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005381517-Add-User-Groups) to give them access to the features you designate beyond Content Distributors.

**Important:** 
The default tenant installed with Composer is the **Visual** Data Discovery tenant. If you do not add multiple tenants, all users belong to the **Visual** Data Discovery tenant by default. If your environment includes multiple tenants, users can be members of different groups in each tenant depending on your organization's needs.

## Administrators Group (System Admins)

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

See [Add Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051525645-Add-Users), [About Supplied Groups](#), [Group Privilege Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference), and[The Composer UI Menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu).

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

If you'd like a user to be a full system administrator, add them to this group and the Content Distributors group as well.

## Content Distributors Group

If you'd like a user to be a full system administrator, add them to this group and the Supervisors group as well.

The Content Distributors group is part of the Visual Data Discovery tenant. Members can create, maintain, and distribute content to all tenants in your environment. Members of the Content Distributors group can:

* Import and export sources directly, or as part of importing and exporting dashboards.
* Import and export local and visual gallery visuals when importing and exporting dashboards.
* Import and export visual gallery visuals.
* Import and export dashboards.
* Import and export connections.
