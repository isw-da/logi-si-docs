---
title: "Authorize Composer Access"
id: 34932639906445
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932639906445-Authorize-Composer-Access
updated_at: 2026-05-26T22:06:03Z
---

# Authorize Composer Access

# Authorize Composer Access

Your users can access Composer, after you've defined their user accounts, added users to groups, and optionally, added users to tenants to grant access to content creation, content management, content access, and use.

Composer supports several approaches to authenticating users, including SAML and LDAP. Choose the best approach given your existing constraints and objectives. A complete list of authentication tools supported by Composer is provided in [Supported Authentication Tools](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933146499341-Supported-Authentication-Tools).

**Note:** 
SAML and LDAP groups that are automatically created in Composer must be manually assigned group data source access and privileges.

Once authenticated, users have authorization to perform Composer functions and access Composer resources as defined by their [group](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932593467277-Manage-User-Groups) membership.

Use the following features to define and provide product access and authorization in Composer.

* Composer tenants: Use to separate Composer product resources as necessary. Assign users to multiple tenants to allow access to each tenant's resources. You can further set up different groups, data connections, data sources, dashboards, and visuals for each tenant. See [Manage Composer Tenants](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932649111693-Manage-Composer-Tenants).
* User accounts: Define access for individual users in Composer. Assign users to one or more groups to give them access to Composer data sources and product features. Users can belong to multiple groups in multiple tenants.
* Groups: Use to assign [privileges](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) to groups of users. Groups are most useful when a number of Composer users require the same access restrictions. Users can be assigned to multiple groups. See [Manage User Groups](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932593467277-Manage-User-Groups).
