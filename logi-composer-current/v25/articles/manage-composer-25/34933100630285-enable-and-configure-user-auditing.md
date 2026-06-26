---
title: "Enable and Configure User Auditing"
id: 34933100630285
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933100630285-Enable-and-Configure-User-Auditing
updated_at: 2026-05-26T22:07:53Z
---

# Enable and Configure User Auditing

# Enable and Configure User Auditing

Write your audit logs to the PostgreSQL database installed with Composer, or an alternative PostgreSQL database of your choice. Create the database, update the `zoomdata.properties` file, and restart Composer to begin capturing audit events.

**Note:**  If you expect a large number of user audit events, accumulating a significant amount of information over time, consider using a separate PostgreSQL database.

## Create a Database

Create the database for user auditing. There are two ways to do so:

**Note:**  PostgreSQL databases are the only supported database type.

1. Bootstrap creation. When you install or upgrade Composer using a `bootstrap-zoomdata` script, a user audit data table is created on the local PostrgreSQL instance. The user audit database is named `zoomdata-user-auditing`, and installed at the same location as the Logi metadata for your Composer instance.
2. Manual creation. To use a separate database or PostgreSQL instance from your Composer metadata database, edit the `zoomdata.properties` file to reflect the target parameters to use. Set the default value of `destination.params.password` to the same database password used in your default PostgreSQL database. Composer creates the collections automatically in that database as needed.

## Enable User Auditing

After you have created or linked your database, copy these properties into the `zoomdata.properties` file.

user-auditing.enabled=true
user-auditing.destination.name=PostgreSQL
user-auditing.destination.type=postgresql
user-auditing.destination.schema=public
user-auditing.destination.collection=audit\_records
user-auditing.destination.collection-per-account=false
user-auditing.destination.params.user\_name=${db.username:zoomdata}
user-auditing.destination.params.password=${db.password:}
user-auditing.destination.params.jdbc\_url=jdbc:postgresql://localhost:5432/zoomdata-user-auditing
user-auditing.tenant.attribute=

Required and optional properties include:

| Property | Default Value | Description |
| --- | --- | --- |
| enabled | false | Use to enable or disable user auditing. Default is false, to disable user auditing. To enable, set to true. Required. |
| destination.name | PostgreSQL | The name of the type of database. Only PostgreSQL is supported. |
| destination.type | postgresql | The database type. Only postgresql is supported. |
| destination.schema | public |  |
| destination.collection |  | The name of the collection of the user audit data. Use to separate data by accounts to prevent access to audit data by unauthorized users.  For example, `audit_records<Account ID>`. |
| destination.collection-per-account | fals | Default is false, to disable  To enable, set to true and include a field for Account ID in destination.collection. |
| destination.params.user\_name | zoomdata | The user name sent to the database to write audit data.  Required. |
| destination.params.password |  | The password sent to the database to write audit data. Required. Can be the same as your default PostgreSQL database. |
| destination.params.jdbc\_url | jdbc:postgresql://localhost:5432/zoomdata-user-auditing | The path to the audit data database. This can be the same database as the user audit schema as shown, or a separate database or partition, as needed.  Required. |
| tenant.attribute |  | Include any new or existing user attribute to support data capture by tenant customer users. Use in addition to account information that is always captured and retained in the database. |

## Restart Composer

Restart Composer to begin capturing audit events.

If you used the bootstrap script to install Composer and audit setup, the audit database table is created when the first event is logged. Test your setup by performing any of the event-triggering actions. See [User Audit Events](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933060626701-User-Audit-Events).

If you've set up your database manually, set up the [Data Writer microservice](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933071011725-Data-Writer-Microservice) to support the user audit processes.
