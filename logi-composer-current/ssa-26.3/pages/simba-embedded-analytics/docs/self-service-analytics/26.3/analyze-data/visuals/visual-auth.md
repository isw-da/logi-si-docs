> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# About Visual Permissions

Visual permissions allow you to permit your entire tenant, groups within your tenant, or users within your tenant to read, write, or delete a visual. This allows you to share a visual with other users.

If a user belongs to a group that has the **Administer Visuals** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) enabled, the user can read, add, modify, or remove any visual in Self-Service Analytics. However, if the user does not belong to a group with this privilege enabled, the user can still be granted permission to read, write, or delete specific visuals using visual permissions. Visual permissions allow users in a tenant or group to read, write, or delete a visual, regardless of any group privilege settings that ordinarily limit their ability to do so.

<Note>
  To manage permissions of a visual, your user must meet **one** of the following criteria:
</Note>

* Must be an administrator, belonging to the [**Administrators** group](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#about-supplied-groups)

* Must belong to a group with the **Administer Visuals** (ROLE\_ADMINISTER\_VISUALS) [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) enabled.

* Must belong to a group with the **Manage Visual Permissions** (ROLE\_PERMISSION\_VISUALS) [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) enabled. If your user has only this privilege (and *not* the **Administer Visuals** privilege), you will only be able to manage permissions for the visuals you can read.

  In addition, you may be restricted in which permissions you can assign. You can only assign permissions equivalent to your own. For example, if your user account has read permission for a visual, you can grant and revoke the read option available on the Visual Permissions panel. If you have write permission for a visual, you can grant and revoke the write option on the Visual Permissions panel.

  <Note>
    If your user does not have read permission for a visual, you cannot view the visual in the Visual Gallery. If your user definition does not have write permission for a visual, you cannot save the visual.
  </Note>

Visual permissions are determined using a most permissive model. For more information, see [How Visual Permissions Are Determined](#how-visual-permissions-are-determined).

Visual permission specifications can also be made using the API endpoints `GET api/visuals?includePermissions=true`, `PATCH /api/visuals/<visualId>/acls/bulk`, `GET /api/visuals/<visualId>/acls`, and `/api/user/permissions/visuals/<visualId>`.

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

**Permissions for imported objects**

When you [import dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-import), associated resources such as visuals, sources, and connections are imported as well. You can quickly grant default access levels to all imported and associated objects in your tenants by enabling **Share Default Access With All Users** at import time. Users are granted Data access to sources and Read access to visuals and dashboards.

For more information, see the following topics:

* [Grant Permissions for a Visual](#grant-permissions-for-a-visual)
* [Modify Permissions for a Visual](#modify-permissions-for-a-visual)
* [Revoke Permissions for a Visual](#revoke-permissions-for-a-visual)
* [How Visual Permissions Are Determined](#how-visual-permissions-are-determined)

<h2 id="how-visual-permissions-are-determined">
  How Visual Permissions Are Determined
</h2>

The creator of a visual always has permission to read, write, and delete the visual. If the creating user is removed from the Self-Service Analytics environment, the visuals created by the user are retained and the [supplied `supervisor` user](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#supplied-users-and-user-groups) becomes the creator of these orphaned visuals.

If conflicting visual permissions are specified for the account, the group within the account, and the user within the account, the permissions granted to the users in both are determined using a most permissive model. The users are granted the highest level of permission specified for the account, group, and user. For example, if the account is granted read and write permissions, but Group A is granted write and delete permissions, users in Group A will be able to read, write, and delete the visual. However, users in any other groups in the account will only be able to read and write the visual.

Here's another example. If the account is granted read, write, and delete permissions, but the groups are only granted read permissions, all users in the account will have read, write, and delete permissions.

### How Data Source Permissions Affect Visual Use

Users must have access to the data sources used for the visual to see the data from the data sources.

For example, assume your account is granted read, write, and delete permissions for a visual. If Chris (a user in the account) does not have access to the data source used by the visual or if Chris is not assigned to any group at all, Chris will be able to see the visual in the Visual Gallery and will be able to open the visual, but no data will be shown.

**Permissions for imported objects**

When you [import dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-import), associated resources such as visuals, sources, and connections are imported as well. You can quickly grant default access levels to all imported and associated objects in your tenants by enabling **Share Default Access With All Users** at import time. Users are granted Data access to sources and Read access to visuals and dashboards.

<h2 id="grant-permissions-for-a-visual">
  Grant Permissions for a Visual
</h2>

You can grant read, write, or delete visual permissions for your tenant, groups in your tenant, or specific users in your tenant.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

**Grant permissions for a visual**

1. Log in as an administrator or a user belonging to a group that includes the **Administer Visuals** or the **Manage Visual Permissions** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference). If you are logged in as a tenant admin, verify you're in or switch to the appropriate tenant.

2. Access the Visual Permissions dialog. Select **Visual Gallery** from the main menu.. The Visuals library appears.

3. Locate the row for the visual in the list and select the permissions icon in the **Permissions** column. The Visual Permissions dialog appears.

   Initially, this dialog is populated with the permissions for the visual creator. Some columns in this work area can be resized or sorted as needed; select the column header break to resize, or select the column name to change the sort.

4. Select **Add** on the Visual Permissions dialog and then select **Groups**, **Users**, or **Tenant** from the drop-down menu.

   * If you select **Groups**, the Add Groups dialog appears, listing all the groups available in your tenant. The [supplied groups](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#about-supplied-groups) are not shown; permissions can not be changed for those groups.
   * If you select **Users**, the Add Users dialog appears, listing all the users available in your tenant.
   * If you select **Tenant**, Read permission is selected for your tenant on the Visual Permissions dialog.
   * Members of the Administrators group have read, write, and delete permissions for every visual in the tenant.
   * The user who created the visual is automatically selected and has **Read**, **Write**, and **Delete** permissions unless you revoke these permissions.

5. Select the tenant or any specific groups or users you want to permit to read, write, or delete the visual and select **Apply**. The Visual Permissions dialog lists your selections.

6. Select the **Read**, **Write**, or **Delete** checkboxes for the tenant, groups, or users to indicate what users in them can do with the visual. **Read** permission is assumed and is always selected. If you clear (uncheck) the **Read** box (revoke **Read** permission), permission for the entire visual is revoked for the tenant, group, or user after you save.

7. Select **Save**. The Save Details dialog appears, listing the changes that you made.

8. Review the changes and select **OK**. The visual permissions are set.

**Permissions for imported objects**

When you [import dashboards](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-import), associated resources such as visuals, sources, and connections are imported as well. You can quickly grant default access levels to all imported and associated objects in your tenants by enabling **Share Default Access With All Users** at import time. Users are granted Data access to sources and Read access to visuals and dashboards.

<h2 id="modify-permissions-for-a-visual">
  Modify Permissions for a Visual
</h2>

You can modify the visual permissions you granted to your tenant, to groups in your tenant, or to specific users in your tenant.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

**Modify permissions for a visual**

1. Log in as an administrator or a user belonging to a group that includes the **Administer Visuals** or the **Manage Visual Permissions** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Access the Visual Permissions dialog. Select the **Visual Gallery** option from the menu. The Visuals library appears.

3. Locate the row for the visual in the list and select the permissions icon in the **Permissions** column. The Visual Permissions dialog appears.

   Initially, this dialog is populated with the permissions for the visual creator.

4. If you want to add permissions for all users in your tenant or for additional groups or users in your tenant, select **Add** on the Visual Permissions dialog and then select **Groups**, **Users**, or **Tenant** from the drop-down menu.

   * If you select **Groups**, the Add Groups dialog appears, listing all the groups available in your tenant. The [supplied groups](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#about-supplied-groups) are not shown; permissions can not be changed for those groups.
   * If you select **Users**, the Add Users dialog appears, listing all the users available in your tenant.
   * If you select **Tenant**, Read permission is selected for your tenant on the Visual Permissions dialog.
   * Members of the Administrators group have read, write, and delete permissions for every visual in the tenant.
   * The user who created the visual is automatically selected and has **Read**, **Write**, and **Delete** permissions unless you revoke these permissions.

5. Modify the **Read**, **Write**, or **Delete** checkbox selections for the tenants or any of the users or groups on the Visual Permissions dialog to indicate what users in them can do with the visual. **Read** permission is assumed and is always selected. If you clear (uncheck) the **Read** box (revoke **Read** permission), permission for the entire visual is revoked for the tenant , group, or user after you save.

6. Select **Save**. The Save Details dialog appears, listing the changes that you made.

7. Review the changes and select **OK**. The visual permissions are set.

<h2 id="revoke-permissions-for-a-visual">
  Revoke Permissions for a Visual
</h2>

You can revoke the visual permissions you previously granted to your tenant, to groups in your tenant, or to specific users in your tenant.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

**Revoke permissions for a visual**

1. Log in as an administrator or a user belonging to a group that includes the **Administer Visuals** or the **Manage Visual Permissions** [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Access the Visual Permissions dialog. Select **Visual Gallery** from the main menu. The Visuals library appears.

3. Locate the row for the visual in the list and select the permissions icon in the **Permissions** column. The Visual Permissions dialog appears.

   Initially, this dialog is populated with the permissions for the visual creator.

4. To completely revoke all visual permissions for the account or for a group or user, locate the row for the tenant, group or user on the Visual Permissions dialog and select the delete icon. The tenant, group, or user is removed from the dialog.

   You can also revoke specific permissions by changing the checkbox selections for the tenant or group on the Visual Permissions dialog. If you clear (uncheck) the **Read** box (revoke **Read** permission), permission for the entire visual is revoked for the tenant, group, or user after you save. See [Modify Permissions for a Visual](#modify-permissions-for-a-visual).

5. Select **Save**. The Save Details dialog appears, listing the changes that you made.

6. Review the changes and select **OK**. The visual permissions are set.
