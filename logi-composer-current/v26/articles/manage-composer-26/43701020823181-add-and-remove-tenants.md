---
title: "Add and Remove  Tenants "
id: 43701020823181
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701020823181-Add-and-Remove-Tenants
updated_at: 2026-08-31T04:15:25Z
---

# Add and Remove  Tenants 

# Add and Remove Tenants

If you want to use tenants to manage access to resources and data, add them to your environment quickly and easily.

**Note:** In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.

## Create a New Tenant

1. Log in as the supplied [admin user](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups#The2), a system administrator, or a member of the Supervisors group.
2. Select **Tenants** (formerly *Multi-Tenancy*) from the Administration menu. The Multi-Tenancy work area appears. This lists the defined tenants in your environment, including the default tenant, *Visual Data Discovery*.
3. To add a new tenant, select **Add Tenant** .

   The Create New Tenant work area opens.
4. Enter a name for the new tenant in the **Tenant Name** field. The name must be at least four characters long.
5. Assign at least one administrator. Select one of the following options:

   * Select **Assign Existing User As Admin** to select an existing user as the administrator for the tenant. Assign a user by choosing **Select Users**, then select one or more users from the list.

     Select **Apply** to confirm your choices. The users are added as tenant administrators to the Administrators group in this tenant when you complete tenant creation.

     **Important:** If you want the tenant admin to also be a user or admin in the Visual Data Discovery (default) tenant, you must create the user account in the Visual Data Discovery (default) tenant, and then add them as an admin during tenant creation or after you create the tenant account.
   * Select **Create A New Admin User** to create a new user account as the administrator for the tenant. Supply a user name and password for the new user in the **Username**, **Password**, and **Confirm Password** fields.

     The new user is assigned to the new tenant account as a tenant administrator assigned to the Administrators group in this tenant when you complete tenant creation. They are not added to the **Visual Data Discovery** tenant, and cannot be added to the **Visual Data Discovery** tenant later.

     **Note:** When you create a user within a tenant, the Login Name is checked against the list of all users across all tenants in the Composer Instance. If the Login Name is in use, you will see an error message. Select a different Login Name for that user.

   No other fields are required, but you can add **Custom Attributes** for the tenant as needed. See [Specify Custom Tenant Attributes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/48418039150349-Specify-Custom-Tenant-Attributes).
6. Select **Create Tenant**.

   The new tenant is created and is automatically enabled. The administrator you assigned is included as a tenant user (see [List and Review Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701006052237-List-and-Review-Users)) and member of the tenant's Administrators group.

   To disable the tenant, see [Enable or Disable Tenants](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701020896141-Enable-or-Disable-Tenants).

Only the Administrators group and no other user groups are part of the tenant until administrator users create more user groups. See [Manage User Groups](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701035505293-Manage-User-Groups).

You can use the Accounts API endpoints to see and define the reserved attributes for your tenants. This includes defining an `email.replyToAddress` and `email.senderDisplayName` for sharing dashboard reports and self service reports. See [Scheduled Self Service Reports and Dashboard Report Prerequisites](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047328013-Scheduled-Self-Service-Reports-and-Dashboard-Report-Prerequisites) and [zoomdata.properties Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054421133-zoomdata-properties-Properties).

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

## Remove Tenants

1. Log in as an [admin user](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups#The2) (System Administrator) or a member of the Supervisors group.
2. Select **Tenants** (formerly *Multi-Tenancy*) from the Administration menu. The Multi-Tenancy work area appears. This lists the defined tenants in your environment, including the default tenant, *Visual Data Discovery*.
3. In the list of tenants, locate the tenant you want to delete and select delete button for that tenant.

   A warning dialog appears that prompts you to confirm that you want to delete the tenant.
4. Select **Delete** on the warning dialog to remove the tenant. All users, data source configurations, data source connections, and custom dashboards that are not associated with other tenants are removed.

The default tenant, *Visual Data Discovery*, cannot be removed.
