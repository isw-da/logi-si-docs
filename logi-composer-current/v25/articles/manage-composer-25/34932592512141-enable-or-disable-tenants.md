---
title: "Enable or Disable  Tenants"
id: 34932592512141
section: "Manage Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932592512141-Enable-or-Disable-Tenants
updated_at: 2026-05-26T22:10:30Z
---

# Enable or Disable  Tenants

# Enable or Disable Tenants

Your tenants can be enabled and disabled. When you create tenant for the first time, it is automatically enabled.

## Disable a Tenant

**Note:** 
The default tenant , *Visual Data Discovery,* can't be disabled.

**Disable a tenant**

1. Log in as the supplied [admin user](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932621360909-Supplied-Users-and-User-Groups#The2), a system administrator, or a member of the Supervisors group.
2. Select the UI menu (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46168007221645)) then select **Multi-Tenancy**.

   The Multi-Tenancy work area appears. It lists the defined tenants in your environment.
3. Select the name of the tenant you want to disable from the list.

   The Edit Tenant work area appears. If you want to edit a different tenant, select the tenant name and pick a different tenant to edit in the dialog.
4. Select (check) the **Disable Tenant** checkbox for the chosen tenant.
5. Select **Save** to save your changes to the tenant.

After a tenant is disabled, users assigned to it can no longer switch to that tenant. If this is the only tenant a user is assigned to, they are shown a message to contact their system administrator the next time they log into Composer.

## Enable a Tenant

**Enable a tenant**

1. Log in as the supplied [admin user](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932621360909-Supplied-Users-and-User-Groups#The2), a system administrator, or a member of the Supervisors group.
2. Select the UI menu (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46168007221645)) then select **Multi-Tenancy**.

   The Multi-Tenancy work area appears. It lists the defined tenants in your environment.
3. Select the name of the tenant you want to enable from the list.

   The Edit Tenant work area appears. If you want to edit a different tenant, select the tenant name and pick a different tenant to edit in the dialog.
4. Clear (uncheck) the **Disable Tenant** checkbox for the chosen tenant.
5. Select **Save** to save your changes to the tenant.

After a tenant is enabled, users that assigned to it can now switch to it while they are logged into other tenants to which they are assigned.
