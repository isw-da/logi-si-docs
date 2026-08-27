---
title: "Set the Current  Tenant for a User"
id: 43701021523469
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021523469-Set-the-Current-Tenant-for-a-User
updated_at: 2026-08-26T07:11:47Z
---

# Set the Current  Tenant for a User

# Set the Current Tenant for a User

If a user has access to multiple Composer tenants, you can specify the tenant they should use the next time they log in. After logging in, they can [switch tenants](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701052090125-Switch-Tenants), as needed.

After a user switches tenants, the most recent tenant they worked in is remembered and used the next time they log in. If a user is assigned to only one tenant, that tenant is always the current tenant.

**Note:** 
The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.

## Set the Current Tenant for a User

1. Log in as a system [admin user](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups#The2) or a user in the Supervisors group. Select **Users** from the Administration menu (formerly *System Users*) to open the Users work area and list all users in your environment.

   **Note:**

   In environments where the [enhanced-experience](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables#ui-toggle "enhanced-experience link") toggle has been enabled, the menu option **System Users** has been removed from the main menu UI. Users with appropriate privileges can instead access users using the **User** menu option, and groups using the **Groups** menu option.
2. On the left side of the Users work area, select the name of the user whose tenants you want to modify. The user information appears on the right side of the work area.
3. Select the **Tenant(s)** tab. This tab lists all the tenants to which the user is assigned and the number of groups to which the user is assigned in each tenant.
4. Select a tenant for the user to use the next time they log in from available tenants in the **Current Tenant** field.
5. Select **Save** to save the user.
