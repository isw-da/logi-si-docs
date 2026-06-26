---
title: "Authorize Composer Access"
id: 4405850851607
section: "Manage Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850851607-Authorize-Composer-Access
updated_at: 2021-09-21T01:26:25Z
---

# Authorize Composer Access

# Authorize Composer Access

User, group, and account definitions are required to grant users access to the Composer application.

Users can be authorized for access to specific accounts and product features. See [*Manage User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859120023-Manage-User-Definitions).

Composer supports several approaches to authenticating users, including SAML, OAuth, and LDAP. Your organization must choose the best approach given your existing constraints and objectives. A complete list of authentication tools supported by Composer is provided in [*Supported Authentication Tools*](https://devnet.logianalytics.com/hc/en-us/articles/4405851167639-Supported-Authentication-Tools).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) SAML and LDAP groups that are automatically created in Composer must be manually assigned group data source access and privileges.

After a user is authenticated for access to Composer, authorization to perform Composer functions and access Composer resources is controlled using [groups](https://devnet.logianalytics.com/hc/en-us/articles/4405850856599-Manage-Group-Definitions).

The following definitions can be specified to provide product access and authorization in Composer.

* Composer accounts can be used to separate Composer product resources, as necessary. Users can be assigned to multiple accounts. However, group definitions, data source configurations, data store connections, and dashboards and visuals are only available in the Composer accounts in which they are defined. See [*Manage Composer Account Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405850854423-Manage-Composer-Account-Definitions).
* User definitions identify individual users of Composer. See [*Manage User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859120023-Manage-User-Definitions). Users must be assigned to groups to use Composer data sources and product features. They may be assigned to more than one group.
* Group definitions assign [privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) to groups of users. Groups are most useful when a number of Composer users require the same access restrictions. Users can be assigned to multiple groups. See [*Manage Group Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405850856599-Manage-Group-Definitions).
