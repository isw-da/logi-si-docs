---
title: "User Auditing for Multi Tenancy Environments"
id: 43701111414413
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701111414413-User-Auditing-for-Multi-Tenancy-Environments
updated_at: 2026-05-29T14:08:57Z
---

# User Auditing for Multi Tenancy Environments

# User Auditing for Multi Tenancy Environments

Composer supports two different levels of separation for user audit data. By default, user audit data is separated between accounts. If needed, you can further separate user audit data within a Composer account by adding and using a custom attribute to separate the data.

Use Composer to write audit data to a single table in your database or multiple tables to suit your organization's needs.

**Important:** 
Database tables that contain user audit data are created automatically when you first trigger an [audit event](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136325645-User-Audit-Events#User). Trigger table creation with user auditing enabled and properly configured before you create a data source for the tables or apply access controls at the database level.

## Separation Between Composer Tenant Accounts

Audit data for Composer users, including administrators, are not visible to other tenant accounts. You define this level of separation in the database in one of three ways:

* Tables: Configure Composerto collect and write user audit data to different tables, then give users database access only to their own audit data table.
* Views: Disable user auditing by account, then give users access to their own audit data, using specific views and database access rights.
* Row level security: Disable user auditing by account, then configure row level security, limiting access for each user to their own data.

See [Enable User Audit Data for Composer User Accounts](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074091149-Enable-User-Audit-Data-for-Composer-User-Accounts#Enable).

## Separation Between Tenants

Configure user auditing for tenants to restrict access to user audit data to their own user tenant data. Composer system administrators can see aggregated data for all tenants in the Composer tenant account.

You can define this level of separation in the database in one of several ways, depending on tenant connection creation privileges.

* If tenant users don't have permission to create new connections, add a user attribute value, then make the data available by applying the appropriate row level filter to that value.
* If tenant users do have permission to create new connections, you must set up database-level access control mechanisms.

  + Views per tenant: Define a tenant attribute, then define what user audit data users can access, using specific views and database access rights.
  + Database level row level security: Define a tenant attribute, then configure row level security for the audit table data, allowing users access to appropriate user audit data through individual user database accounts.

See [Enable User Audit Data for Multi Tenant Accounts](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701121656845-Enable-User-Audit-Data-for-Multi-Tenant-Accounts#Enable).
