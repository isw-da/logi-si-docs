---
title: "Understanding The Tenant-Role-User Relationship"
id: 4415492693015
section: "Introduction"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/4415492693015-Understanding-The-Tenant-Role-User-Relationship
updated_at: 2021-12-10T03:08:02Z
---

# Understanding The Tenant-Role-User Relationship

# Understanding The Tenant-Role-User Relationship

## Tenants, Roles, and Users

Within Izenda, users fit into categories that define their relationships
with other users. Izenda utilizes these relationships to define access
rights of features, data, reports, and dashboards.

[![../_images/tru_single_tenant.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415511713559/tru_single_tenant_960x540.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492445719/tru_single_tenant.png)

### Users

A user is the elemental classification of an entity within Izenda.

* Users have a user name and token to grant access to various parts of
  Izenda
* A user does not have to have a defined tenant or a defined role
  + A user either has a tenant/role or the user is a System
    Administrator. Within your User Setup, you will able to toggle a
    user to be an Administrator.
  + System Administrators can impersonate tenant views to navigate the
    platform with a tenant’s access.
* A user can belong to more than one role

For more on User Setup, please see the [User Setup](https://devnet.logianalytics.com/hc/en-us/articles/4415512108183-User-Setup).

### Roles

A role is a classification within a tenant and are used to define
natural distinctions between users. For instance, your company man have
an IT Department that is interested in bug reports and a Sales
Department that is interested in quarterly sales. Roles will allow you
to filter the data available for each role so that they only see
relevant information.
- Roles can overlap each other but roles cannot be subsets of each other

For more on Role Setup, please see the [Role Setup](https://devnet.logianalytics.com/hc/en-us/articles/4415512104471-Role-Setup).

### Tenants

Tenants are the largest user classification available. A tenant is
generally used to define one definite entity with a broad access to
features, data, reports, and dashboards.
- Users and roles can only belong to 1 tenant

### Tenant System Modes

* Izenda is built to support two main system configuration modes:

#### Single Tenant

Single tenant allows you to set up Izenda for a single client scenario.

[![../_images/tru_single_tenant.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415511713559/tru_single_tenant_960x540.png)](https://devnet.logianalytics.com/hc/article_attachments/4415492445719/tru_single_tenant.png)

#### Multi-Tenant

Multi-Tenant provides an easy management of multiple clients on the same instance of Izenda.

* If you use multi-tenant mode, you can choose to allow duplicated User IDs where an ID can be used in multiple tenants. These User IDs do not reference the same user.
* Roles can mirror each other in each tenant but roles cannot exist between tenants.
* Users can mirror each other in each tenant but users, other than a System Administrator, cannot exist between tenants.

[![../_images/tru_multi_tenant.PNG](https://devnet.logianalytics.com/hc/article_attachments/4415504343063/tru_multi_tenant_960x540.png)](https://devnet.logianalytics.com/hc/article_attachments/4415511713815/tru_multi_tenant.png)

For more on Multi-Tenant Setup, please see the [Tenant Setup](https://devnet.logianalytics.com/hc/en-us/articles/4415504854935-Tenant-Setup).
