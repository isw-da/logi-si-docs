---
title: "Tenant Setup for Multi-tenant Architectures"
id: 12528299950103
section: "Administrator Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528299950103-Tenant-Setup-for-Multi-tenant-Architectures
updated_at: 2023-02-23T14:59:37Z
---

# Tenant Setup for Multi-tenant Architectures

# Tenant Setup for Multi-tenant Architectures

New in version 2.0.0: Global Report feature can be used to share system reports among all tenants, see [Global Report Setup Guide](https://devnet.logianalytics.com/hc/en-us/articles/12528284237719-Global-Report-Setup-Guide).

In multi-tenant systems, tenant data is stored in similar database structures placed in

* different databases - Separate Database Architecture
* different schemas in the same database - Separate Schema Architecture
* same tables, schemas and databases - Shared Schema Architecture

## Separate Database Architecture

Each tenant data is stored in a separate database with identical structure.

[![../_images/TicketDesk_-_Separate_Database_Architecture.png](https://devnet.logianalytics.com/hc/article_attachments/12528205348375/ticketdesk_-_separate_database_architecture.png)](https://devnet.logianalytics.com/hc/article_attachments/12528205348375/ticketdesk_-_separate_database_architecture.png)

1. Add connections to each tenant database at that tenant level.

   > In this sample, create 4 tenants each having one connection to its database.
2. Data model and other settings should be set up for one tenant, then copied to other tenants using a Copy Management setting similar to the following:

   [![../_images/Copy_Management_-_Separate_Database_Architecture.png](https://devnet.logianalytics.com/hc/article_attachments/12528205362583/copy_management_-_separate_database_architecture_900x488.png)](https://devnet.logianalytics.com/hc/article_attachments/12528221167511/copy_management_-_separate_database_architecture.png)

## Separate Schema Architecture

Each tenant data is stored in a separate schema in the same database.

1. Add connections to the shared database at that each tenant level.
2. Set up data model for one source tenant only.

   [![../_images/MultiTenantCase2_T1_Data_Model.png](https://devnet.logianalytics.com/hc/article_attachments/12528205369239/multitenantcase2_t1_data_model_556x544.png)](https://devnet.logianalytics.com/hc/article_attachments/12528221174679/multitenantcase2_t1_data_model.png)
3. Skip data model for other tenants (Just add the connection, test then save it).

   [![../_images/MultiTenantCase2_T2_Connection.png](https://devnet.logianalytics.com/hc/article_attachments/12528221253655/multitenantcase2_t2_connection_557x208.png)](https://devnet.logianalytics.com/hc/article_attachments/12528221236759/multitenantcase2_t2_connection.png)
4. Copy data model to other tenants using a Copy Management setting similar to the following:

   [![../_images/Copy_Management_-_Separate_Schema_Architecture.png](https://devnet.logianalytics.com/hc/article_attachments/12528205411223/copy_management_-_separate_schema_architecture_900x438.png)](https://devnet.logianalytics.com/hc/article_attachments/12528221267735/copy_management_-_separate_schema_architecture.png)
5. The data model was successfully copied to other tenants.

   [![../_images/MultiTenantCase2_T2_After_Copy.png](https://devnet.logianalytics.com/hc/article_attachments/12528221298455/multitenantcase2_t2_after_copy_540x544.png)](https://devnet.logianalytics.com/hc/article_attachments/12528205423895/multitenantcase2_t2_after_copy.png)

## Shared Schema Architecture

Each tenant data is stored in the same tables, schema and database, identified by different values in a “TenantID” field in every table.

1. Add connections to the shared database at that each tenant level.
2. Set up data model for one source tenant only.

   [![../_images/MultiTenantCase3_T1_Data_Model.png](https://devnet.logianalytics.com/hc/article_attachments/12528221314071/multitenantcase3_t1_data_model_567x516.png)](https://devnet.logianalytics.com/hc/article_attachments/12528221307543/multitenantcase3_t1_data_model.png)
3. Skip data model for other tenants (Just add the connection, test then save it).

   [![../_images/MultiTenantCase3_T2_Connection.png](https://devnet.logianalytics.com/hc/article_attachments/12528221351319/multitenantcase3_t2_connection_568x212.png)](https://devnet.logianalytics.com/hc/article_attachments/12528205458455/multitenantcase3_t2_connection.png)
4. Copy data model to other tenants using a Copy Management setting similar to the following:

   [![../_images/Copy_Management_-_Shared_Schema_Architecture.png](https://devnet.logianalytics.com/hc/article_attachments/12528205475479/copy_management_-_shared_schema_architecture_900x492.png)](https://devnet.logianalytics.com/hc/article_attachments/12528205470359/copy_management_-_shared_schema_architecture.png)
5. Specify this specific “TenantID” field in the “Tenant Field” advanced setting to automatically restrict report data to that of the tenant of the current logged-in user.

   > (This setting basically adds a filter condition “TenantID” = <value of the tenant id of the current logged-in user> to every query sources used in report)

   Note: Please note that the field must be wrapped in brackets when set. For example: TenantID should be set as [TenantID]

   [![../_images/Tenant_Field_advanced_setting.png](https://devnet.logianalytics.com/hc/article_attachments/12528221405975/tenant_field_advanced_setting_650x251.png)](https://devnet.logianalytics.com/hc/article_attachments/12528205479575/tenant_field_advanced_setting.png)
