> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# How Dashboard and Self Service Report Permissions Are Determined

The creator of a dashboard or self service report always has permission to read, write, and delete the dashboard. If the user who created the dashboard is removed from the Self-Service Analytics environment, the dashboards and self service dashboard reports they created are retained.

If conflicting permissions are specified for a tenant, a group within that tenant, and a user within the tenant, the permissions granted to the users in both are determined using a most permissive model. Users are granted the highest level of permission specified for the tenant, group, and user.

For example, if the tenant is granted read and write permissions, but **Group A** is granted write and delete permissions, users in **Group A** will be able to read, write, and delete the dashboard. However, users in any other groups in the tenant will only be able to read and write the dashboard.

Here's another example. If the tenant is granted read, write, and delete permissions, but the groups are only granted read permissions, all users in the tenant will have read, write, and delete permissions.

**How source permissions affect dashboard and self service report use**

Users must have access to the data sources used in the dashboard or self service report to see the data from the data sources.

For example, assume your tenant is granted read, write, and delete permissions for a dashboard or report. If Linda (a user in the tenant) does not have access to the data source used by the dashboard or if Linda is not assigned to any group at all, Linda will be able to see the dashboard or report in the library and will be able to open the dashboard or report, but no data will be shown.

Now suppose a dashboard uses three data sources on different visuals in the dashboard, but Linda only has access to two of the data sources. Linda will be able to see only the visuals that use data from the two data sources to which she has access.

**Permissions for imported objects**

When you [import dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-import), associated resources such as visuals, sources, and connections are imported as well. You can quickly grant default access levels to all imported and associated objects in your tenants by enabling **Share Default Access With All Users** at import time. Users are granted Data access to sources and Read access to visuals and dashboards.

<h2 id="about-dashboard-and-self-service-report-permissions">
  About Dashboard and Self Service Report Permissions
</h2>

Dashboard and self service report permissions allow you to permit your entire tenant, groups within your tenant, or users within your tenant to read, write, or delete a dashboard or report. This allows you to share a dashboard or report with other users.

If a user belongs to a group that has the **Administer Dashboards** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) enabled, the user can read, add, modify, or remove any dashboard or report in the tenant. However, if the user does not belong to a group with this privilege enabled, the user can still be granted permission to read, write, or delete specific dashboards and reports in the tenant using dashboard permissions. Dashboard permissions allow users in an tenant or group to read, write, or delete a dashboard or report, regardless of any group privilege settings that ordinarily limit their ability to do so.

<Note>
  To manage permissions of a dashboard or self service report, a user must meet **one** of the following criteria:
</Note>

* Must be an administrator, belonging to the **[Administrators](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#administrators-group-system-admins)** group or **[Content Distributors](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#content-distributors-group)** group.

* Must belong to a group with the **Administer Dashboards** (ROLE\_ADMINISTER\_DASHBOARDS) [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) enabled.

* Must belong to a group with the **Manage Dashboard Permissions** (ROLE\_PERMISSION\_DASHBOARDS) [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) enabled. If your user definition has only this privilege (and *not* the **Administer Dashboards** privilege), you will only be able to manage permissions for the dashboards or reports for which you have `READ` permission.

  In addition, you may be restricted in which permissions you can assign. You can only assign permissions equivalent to your own. For example, if your user account has read permission for a dashboard or self service report, you can grant and revoke the read option available on the Permissions panel. If you have write permission for a dashboard or self service report, you can grant and revoke the write option on the Permissions panel.

  <Note>
    If your user account does not have read permission for a dashboard or self service report, you cannot see the dashboard or report in the appropriate Library.
  </Note>

Dashboard and self service report permissions are determined using a most permissive model. For more information, see How Dashboard and Self Service Report Permissions Are Determined.

These permissions can also be managed using the API endpoints `GET /api/dashboards/{dashboardId}/acls`, `PUT and PATCH /api/dashboards/{dashboardId}/acls/bulk`, `GET /api/inventory/DASHBOARD/{id}`, and `GET /api/user/permissions/dashboards/{dashboardId}`.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

* Users who have the [group privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) **Export Dashboards** (ROLE\_EXPORT\_DASHBOARDS) and READ for dashboards can export dashboards.
* Users who have [group privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) of **Manage Connections** (ROLE\_MANAGE\_CONNECTIONS), and **Administer Sources** (ROLE\_ADMINISTER\_SOURCES), and **Administer Visuals** (ROLE\_ADMINISTER\_VISUALS), and **Administer Dashboards** (ROLE\_ADMINISTER\_DASHBOARDS) can import dashboards.

## Grant Permissions for a Dashboard

You can grant read, write, or delete dashboard permissions for your tenant, groups in your tenant, or specific users in your tenant.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

**Grant permissions for a dashboard**

1. Log in as an administrator or a user belonging to a group that includes the **Administer Dashboards** or the **Manage Dashboard Permissions** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference). If you are logged in as a tenant admin, verify you're in or switch to the appropriate tenant.

2. Select the **Discovery Board** card on your home page or **Library** from the main menu. The dashboard library opens.

3. Locate the row for the dashboard in the list and select the permissions icon in the Permissions column. The Dashboard Permissions dialog appears.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/dashboards/dash-permit-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=13feee586fb7520d178af6352f09931d" alt="set permissions for users in this work area" width="647" height="631" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/dashboards/dash-permit-26-2.png" />

   Some columns in this work area can be resized or sorted as needed; select the column header break to resize, or select the column name to change the sort.

4. Select **Add** on the Dashboard Permissions dialog and then select **Groups**, **Users**, or **Tenant** from the drop-down menu.

   * If you select **Groups**, the Add Groups dialog appears, listing all the groups available in your tenant. The [supplied groups](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#about-supplied-groups) are not shown; permissions can not be changed for those groups.
   * If you select **Users**, the Add Users dialog appears, listing all the users available in your tenant.
   * If you select **Tenant**, Read permission is selected for your tenant on the Source Permissions dialog.
   * Members of the Administrators group have data access, read, write, and delete permissions for every data source in the tenant.
   * The user who creates a data source is automatically selected and has **Data Access**, **Read**, **Write**, and **Delete** permissions unless you revoke these permissions.

5. Select tenants or any specific groups or users you want to permit to read, write, or delete the dashboard and select **Apply**. The Dashboard Permissions dialog lists your selections.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/dashboards/dash-permit-26-2-02.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=05904dbd3393f41c81b1c725be77b31e" alt="set dashboard permissions dialog" width="649" height="636" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/dashboards/dash-permit-26-2-02.png" />

6. Select the **Read**, **Comment**, **Write**, or **Delete** checkboxes for a tenant, groups, or users to indicate what they can do with the dashboard. **Read** permission is assumed and is always selected. If you clear (uncheck) the **Read** box (revoke **Read** permission), permission for the entire dashboard is revoked for the tenant, group, or user after you save.

7. Select **Save**. The Save Details dialog appears, listing the changes that you made.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/dashboards/dash-permit-26-2-03.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=b533778d9eb40dbf124e12ff357b8177" alt="confirm your changes and save" width="649" height="637" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/dashboards/dash-permit-26-2-03.png" />

8. Review the changes and select **OK**. The dashboard permissions are set.

**Permissions for imported objects**

When you [import dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-import), associated resources such as visuals, sources, and connections are imported as well. You can quickly grant default access levels to all imported and associated objects in your tenants by enabling **Share Default Access With All Users** at import time. Users are granted Data access to sources and Read access to visuals and dashboards.

<h2 id="modify-permissions-for-a-dashboard">
  Modify Permissions for a Dashboard
</h2>

You can modify the dashboard permissions you granted to your tenant, to groups in your tenant, or to specific users in your tenant.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

**Modify permissions for a dashboard**

1. Log into Self-Service Analytics as an administrator or a user belonging to a group that includes the **Administer Dashboards** or the **Manage Dashboard Permissions** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Select the **Discovery Board** card on your home page or **Library** from the main menu. The dashboard library opens.

   <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/dashboards/dash-lib-26-2.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=810bb5aec71b6976d9198168f687bd8f" alt="use to manage your dashboards" width="1417" height="541" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/dashboards/dash-lib-26-2.png" />

3. Locate the row for the dashboard in the list and select the permissions icon in the Permissions column. The Dashboard Permissions dialog appears, showing current rights for tenants, groups, and users.

   Some columns in this work area can be resized or sorted as needed; select the column header break to resize, or select the column name to change the sort.

4. If you want to add permissions for all users in your tenant or for additional groups or users in your tenant, select **Add** on the Dashboard Permissions dialog and then select **Groups**, **Users**, or **Tenant** from the drop-down menu.

   * If you select **Groups**, the Add Groups dialog appears, listing all the groups available in your tenant. The [supplied groups](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#about-supplied-groups) are not shown; permissions can not be changed for those groups.
   * If you select **Users**, the Add Users dialog appears, listing all the users available in your tenant.
   * If you select **Tenant**, Read permission is selected for your tenant in the Dashboard Permissions dialog. When finished, select **Apply**.
   * Members of the Administrators group have read, write, and delete permissions for every dashboard in the tenant.
   * The user who created the dashboard is automatically selected and has **Read**, **Write**, and **Delete** permissions, although these permissions can be changed.

5. Modify the **Read**, **Write**, or **Delete** checkbox selections for the tenant or any of the users or groups on the Dashboard Permissions dialog to indicate what users in them can do with the dashboard.

   **Read** permission is assumed and is always selected. If you clear (uncheck) the **Read** box (revoke **Read** permission), permission for the entire dashboard is revoked for the tenant, group, or user after you save.

6. Select **Save**. The Save Details dialog appears, listing the changes that you made.

7. Review the changes and select **OK**. The dashboard permissions are set.

## Revoke Permissions for a Dashboard

You can revoke the dashboard permissions you previously granted to your tenant, to groups in your tenant, or to specific users in your tenant.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

**Revoke permissions for a dashboard**

1. Log into Self-Service Analytics as an administrator or a user belonging to a group that includes the **Administer Dashboards** or the **Manage Dashboard Permissions** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Select the **Discovery Board** card on your home page or **Library** from the main menu. The dashboard library opens.

3. Locate the row for the dashboard in the list and select icon in its Permissions column. The Dashboard Permissions dialog appears.

   Some columns in this work area can be resized or sorted as needed; select the column header break to resize, or select the column name to change the sort.

4. To completely revoke all dashboard permissions for the tenant or for a group or user, locate the row for the tenant, group or user on the Dashboard Permissions dialog and select the delete icon. The tenant, group, or user is removed from the dialog.

   You can also revoke specific permissions by changing the checkbox selections for the tenant or group on the Dashboard Permissions dialog. If you clear (uncheck) the **Read** box (revoke **Read** permission), permission for the entire dashboard is revoked for the tenant, group, or user after you save. See [Modify Permissions for a Dashboard](#modify-permissions-for-a-dashboard).

5. Select **Save**. The Save Details dialog appears, listing the changes that you made.

6. Review the changes and select **OK**. The dashboard permissions are set.
