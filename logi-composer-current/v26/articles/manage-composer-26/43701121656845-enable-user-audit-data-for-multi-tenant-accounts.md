---
title: "Enable User Audit Data for Multi Tenant Accounts"
id: 43701121656845
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701121656845-Enable-User-Audit-Data-for-Multi-Tenant-Accounts
updated_at: 2026-05-29T14:08:59Z
---

# Enable User Audit Data for Multi Tenant Accounts

# Enable User Audit Data for Multi Tenant Accounts

Configure user auditing for tenants to restrict access to user audit data to their own user tenant data. Composer system administrators can see aggregated data for all tenants in the Composer account.

You can define this level of separation in the database in one of several ways, depending on tenant connection creation privileges.

**Important:** 
Database tables that contain user audit data are created automatically when you first trigger an [audit event](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136325645-User-Audit-Events#User). Trigger table creation with user auditing enabled and properly configured before you create a data source for the tables or apply access controls at the database level.

## Tenants Without Connection Creation Permissions

In environments where tenants don't have permission to create connections, you can set up and use user attribute value, such as `${User.tenant}` define row level filters to limit access to user audit data.

1. Set up an attribute for each user, such as `${User.tenant}`, to identify the tenant for each user.
2. Add the attribute name to the `zoomdata.properties` file. In this example, add `tenant`: `user-auditing.tenant.attribute=tenant`.
3. Generate an audit event for any account to trigger audit data table creation.
4. As a system administrator, create connection and data sources for the audit data in Composer.
5. Add a row level filter to the data source. Compare the column tenant with the user attribute you created. In this example, `tenant=${User.tenant}`

## Tenants With Connection Creation Permissions

If your tenants do have permission to create connections, there are two ways to restrict user audit data access: by setting up views at the tenant level, or applying row level security. Use the features of your database to control access to the data, once attributes are defined and applied.

### Views Per Tenant

1. Set up an attribute for each user, such as `${User.tenant}`, to identify the tenant for each user.
2. Add the attribute name to the `zoomdata.properties` file. In this example, add `tenant`: `user-auditing.tenant.attribute=tenant`.
3. Generate an audit event for any account to trigger audit data table creation.
4. Create a view for each tenant that filters the audit data table, using a condition such as `tenant='<Tenant>'`.
5. Create user database accounts for each tenant. Define access rights for account user to query only their own tenant audit data table.
6. Create connections to the audit database using each user database account.

### Row Level Security

1. Set up an attribute for each user, such as `${User.tenant}`, to identify the tenant for each user.
2. Add the attribute name to the `zoomdata.properties` file. In this example, add `tenant`: `user-auditing.tenant.attribute=tenant`.
3. Generate an audit event for any account to trigger audit data table creation.
4. Create a separate database user for each tenant, and configure row level security for each account user to query only their own tenant audit data table, using a condition such as `tenant='<Tenant>'`
5. Create connections to the audit database using each user database account.
