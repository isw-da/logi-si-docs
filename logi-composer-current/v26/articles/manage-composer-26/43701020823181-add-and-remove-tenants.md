---
title: "Add and Remove  Tenants "
id: 43701020823181
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701020823181-Add-and-Remove-Tenants
updated_at: 2026-05-29T14:07:03Z
---

# Add and Remove  Tenants 

# Add and Remove Tenants

If you want to use tenants to manage access to resources and data, add them to your environment quickly and easily.

## Create a New Tenant

1. Log in as the supplied [admin user](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups#The2), a system administrator, or a member of the Supervisors group.
2. Select **Tenants** on the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701139705997-The-Composer-Supervisor-Menu). The Multi-Tenancy work area appears. This lists the defined tenants in your environment, including the default tenant, *Visual Data Discovery*.
3. To add a new tenant, select **Add Tenant** .

   The Create New Tenant work area opens.
4. Enter a name for the new tenant in the **Tenant name** box. The name must be at least four characters long.
5. Every tenant must have at least one administrator. Select one of the following options:

   * Select **Assign Existing User As Admin** to select an existing user as the administrator for the account. After selecting this option, select **Select Users**, then select a user from the list that opens. After you select one or more users, select **Apply**.
   * Select **Create A New Admin User** to create a new user account to use as the administrator for the account. Supply the user name and password for the new user in the **User name**, **Password**, and **Confirm Password** boxes. The new user is assigned to the new account as a tenant administrator assigned to that tenant's Administrator's group.
6. Select **Create Tenant**.

   The new tenant is created and is automatically enabled. The administrator you assigned is included as a tenant user (see [List and Review Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701006052237-List-and-Review-Users)).

   To disable the tenant, see [Enable or Disable Tenants](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701020896141-Enable-or-Disable-Tenants).
7. Optionally, define custom attributes for this tenant in the **Custom attributes** work area.

Only the Administrators group and no other user groups are part of the tenant until administrator users create user groups. See [Manage User Groups](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701035505293-Manage-User-Groups).

You can use the Accounts API endpoints to see and define the reserved attributes for your tenants. This includes defining an `email.replyToAddress` and `email.senderDisplayName` for sharing dashboard reports. See [Scheduled Dashboard Report Prerequisites](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047328013-Scheduled-Dashboard-Report-Prerequisites) and [zoomdata.properties Properties](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054421133-zoomdata-properties-Properties).

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

## Remove Tenants

1. Log in as an [admin user](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups#The2) (System Administrator) or a member of the Supervisors group.
2. Select the UI menu then select **Multi-Tenancy**.

   The Manage Tenants page appears. It lists the tenants that have been defined.
3. In the list of tenants, locate the tenant you want to delete and select delete button in the **Delete** column.

   A warning dialog appears that prompts you to confirm that you want to delete the tenant.
4. Select **Delete** on the warning dialog to remove the tenant. All users, data source configurations, data source connections, and custom dashboards that are not associated with other tenants are removed.

The default tenant, *Visual Data Discovery*, cannot be removed.
