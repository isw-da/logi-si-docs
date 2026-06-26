---
title: "Enable User Audit Data for Composer User Accounts"
id: 43701074091149
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074091149-Enable-User-Audit-Data-for-Composer-User-Accounts
updated_at: 2026-05-29T14:08:59Z
---

# Enable User Audit Data for Composer User Accounts

# Enable User Audit Data for Composer User Accounts

Audit data for Composer users, including administrators, are not visible to other Composer accounts. You define this level of separation in the database in one of three ways:

* [Tables](#Tables): Configure Composer to collect and write user audit data to different tables, then give users database access only to their own audit data table.
* [Views](#Views): Disable user auditing by account, then give users access to their own audit data, using specific views and database access rights.
* [Row level security](#Row): Disable user auditing by account, then configure row level security, limiting access for each user to their own data.

**Important:** 
Database tables that contain user audit data are created automatically when you first trigger an [audit event](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136325645-User-Audit-Events#User). Trigger table creation with user auditing enabled and properly configured before you create a data source for the tables or apply access controls at the database level.

## Tables for a Composer Account

1. Use separate collections for accounts by defining `user-auditing.destination.collection-per-account=true` in the `zoomdata.properties` file.
2. Generate an audit event for all accounts to trigger audit data table creation.
3. Create user database accounts for each user. Define user access rights for each user to query only their own account's audit data table.
4. Create connections to the audit database using each account.

## Views by Composer Account

1. Disable use of separate collections for accounts by defining `user-auditing.destination.collection-per-account=false` in the `zoomdata.properties` file.
2. Generate an audit event for any account to trigger audit data table creation.
3. Create a view for each account that filters the audit data table, using a condition such as `accountID='<Account ID>'`.
4. Create user database accounts for each user. Define user access rights for each user to query only their own account's audit data view.
5. Create connections to the audit database using each account.

## Row Level Security in the Database

1. Enable user auditing by defining `user-auditing.destination.collection-per-account=false` in the `zoomdata.properties` file.
2. Generate an audit event for any account to trigger audit data table creation.
3. Create user database accounts for each user, and configure row level security for the audit data table to limit users to their own data. For example, use a filter such as `accountID='<Account ID>`.
4. Create connections to the audit database using each account.
