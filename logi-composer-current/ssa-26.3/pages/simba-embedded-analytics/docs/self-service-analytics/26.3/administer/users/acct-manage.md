> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Tenants

As a member of the Supervisors group or a system [admin user](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user), you can manage Self-Service Analytics tenants.

Use tenants to separate resources as necessary. Assign users to multiple tenants to allow access to each tenant's resources. You can further set up different groups, data connections, data sources, dashboards, and visuals for each tenant.

<Note>
  The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
</Note>

### How Tenants Differ from Groups

You can create and use [groups](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#manage-user-groups) in your environment in the default tenant, Visual Data Discovery, to give users different rights, privileges, and access to specific resources.

You can [create additional tenants](#add-and-remove-tenants) to further separate users and resources, and use [groups](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#manage-user-groups) within each tenant to give users different rights, privileges, and access to specific resources. Multiple tenant environments can be run within one organization for intentional user experience silos, or to support multiple, separate user experience silos across multiple organizations.

When a [system administrator](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a tenant administrator creates a user within a tenant, the Login Name is checked against the list of all users across all tenants in the instance. If a user account with that Login Name exists in the Visual Data Discovery tenant or any other tenant, an error message is returned indicating the user account cannot be created. Create the desired user account by selecting another Login Name.

<h2 id="switch-tenants">
  Switch Tenants
</h2>

If a user is assigned to multiple tenants, they can switch between tenants when working in Self-Service Analytics. Users can also be members of different groups on each tenant, with settings specific to each group in each tenant. To switch which tenant you are working in, select your profile from the [menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-main-menu), then select a tenant from the **Switch Tenant** menu.

While you do not have to maintain multiple tenants, Self-Service Analytics makes it easy to do so if you need to establish separate working areas for various groups in your organization.

* By default, users are assigned to the *Visual Data Discovery* tenant.
* After you have added more tenants, you can assign users to one or more tenants as needed. See [Assign and Remove Users in Tenants](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#assign-and-remove-users-in-tenants).
* If your environment has users who are assigned to multiple tenants, you can specify which tenant the user uses the next time they log in. See [Set the Current Tenant for a User](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#set-the-current-tenant-for-a-user).

<h2 id="add-and-remove-tenants">
  Add and Remove Tenants
</h2>

If you want to use tenants to manage access to resources and data, add them to your environment quickly and easily.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

### Create a New Tenant

1. Log in as the supplied [admin user](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user), a system administrator, or a member of the Supervisors group.

2. Select **Tenants** (formerly *Multi-Tenancy*) from the Administration menu. The Multi-Tenancy work area appears. This lists the defined tenants in your environment, including the default tenant, *Visual Data Discovery*.

3. To add a new tenant, select **Add Tenant** .

   The Create New Tenant work area opens.

4. Enter a name for the new tenant in the **Tenant Name** field. The name must be at least four characters long.

5. Assign at least one administrator. Select one of the following options:

   * Select **Assign Existing User As Admin** to select an existing user as the administrator for the tenant. Assign a user by choosing **Select Users**, then select one or more users from the list.

     Select **Apply** to confirm your choices. The users are added as tenant administrators to the Administrators group in this tenant when you complete tenant creation.

     <Warning>
       If you want the tenant admin to also be a user or admin in the Visual Data Discovery (default) tenant, you must create the user account in the Visual Data Discovery (default) tenant, and then add them as an admin during tenant creation or after you create the tenant account.
     </Warning>

   * Select **Create A New Admin User** to create a new user account as the administrator for the tenant. Supply a user name and password for the new user in the **Username**, **Password**, and **Confirm Password** fields.

     The new user is assigned to the new tenant account as a tenant administrator assigned to the Administrators group in this tenant when you complete tenant creation. They are not added to the **Visual Data Discovery** tenant, and cannot be added to the **Visual Data Discovery** tenant later.

     <Note>
       When you create a user within a tenant, the Login Name is checked against the list of all users across all tenants in the Composer Instance. If the Login Name is in use, you will see an error message. Select a different Login Name for that user.
     </Note>

   No other fields are required, but you can add **Custom Attributes** for the tenant as needed. See [Specify Custom Tenant Attributes](#specify-custom-tenant-attributes).

6. Select **Create Tenant**.

   The new tenant is created and is automatically enabled. The administrator you assigned is included as a tenant user (see [List and Review Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#list-and-review-users)) and member of the tenant's Administrators group.

   To disable the tenant, see [Enable or Disable Tenants](#enable-or-disable-tenants).

Only the Administrators group and no other user groups are part of the tenant until administrator users create more user groups. See [Manage User Groups](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#manage-user-groups).

You can use the Accounts API endpoints to see and define the reserved attributes for your tenants. This includes defining an `email.replyToAddress` and `email.senderDisplayName` for sharing dashboard reports and self service reports. See [Scheduled Self Service Reports and Dashboard Report Prerequisites](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-schedule#scheduled-self-service-reports-and-dashboard-report) and [Properties Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/properties-reference).

API documentation is provided in your environment at this link: `https://<Self-Service Analytics-URL>/composer/swagger-ui.html`.

### Remove Tenants

1. Log in as an [admin user](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) (System Administrator) or a member of the Supervisors group.

2. Select **Tenants** (formerly *Multi-Tenancy*) from the Administration menu. The Multi-Tenancy work area appears. This lists the defined tenants in your environment, including the default tenant, *Visual Data Discovery*.

3. In the list of tenants, locate the tenant you want to delete and select delete button for that tenant.

   A warning dialog appears that prompts you to confirm that you want to delete the tenant.

4. Select **Delete** on the warning dialog to remove the tenant. All users, data source configurations, data source connections, and custom dashboards that are not associated with other tenants are removed.

The default tenant, *Visual Data Discovery*, cannot be removed.

## Modify Tenants

### Modify an Existing Tenant

1. Log in as the supplied [admin user](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user), a system administrator, or a member of the Supervisors group.

2. Select **Tenants** (formerly *Multi-Tenancy*) from the Administration menu.

   The Multi-Tenancy work area appears, listing the existing tenants in your environment.

3. In the list of tenants, select the name of the tenant you want to modify. The Edit Tenant work area opens.

4. In this work area, you can change the tenant name in the **Tenant Name** field.

   Alternatively, disable or enable a tenant here. See [Enable or Disable Tenants](#enable-or-disable-tenants).

   If needed, add or remove Custom Attributes. See [Specify Custom Tenant Attributes](#specify-custom-tenant-attributes).

5. Select **Save** to save any changes you make.

## Modify Tenant Administrators

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases. If you are running an earlier release or your admin has not enabled the new interface, see [Add or Remove a Tenant Administrator (Earlier Releases)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701020850061-Modify-Tenant-Administrators#Add).
</Note>

When you create a tenant, you must assign an existing user as an administrator for the tenant or add a new user as an administrator of the tenant. The user is automatically added to the Administrators group for that tenant.

Thereafter, you can only modify the administrators of the tenant when you are logged in as an administrator of the tenant.

### Add or Remove a Tenant Administrator

1. Log in as an administrator for the tenant.

   If the system administrator user name you logged in with is also associated with other Self-Service Analytics tenants, verify that the correct tenant is selected. See [Switch Tenants](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#switch-tenants) .

2. Select **Users** from the menu. The Users work area appears, listing all users in the tenant.

3. Select the name of the existing user you want to add or remove as an administrator of the tenant from the user list. User details open to the right of the list.

4. Scroll to the **Groups** section of the **Info** tab in the selected user.

5. To make the user an administrator of the tenant, add the user to the **Administrators** group. Select **Add Groups** to bring up the Add Group(s) dialog.

   Select (check) the **Administrators** group in the dialog to add the user to this group and select **Apply**.

   To remove the user as an administrator of the tenant, clear (uncheck) the **Administrators** group in the dialog and select **Apply**.

6. Select **Save** to save the user updates.

## List and Review Tenants

### List Tenants

1. Log in as the supplied [admin user](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user), a system administrator, or a member of the Supervisors group.
2. Select **Tenants** (formerly *Multi-Tenancy*) from the Administration menu. The Multi-Tenancy work area appears. This lists the defined tenants in your environment, including the default tenant, *Visual Data Discovery*.
3. When you have reviewed the list of tenants in your environment, select **Add Tenant** to add a new tenant, or navigate away from this work area by selecting an option from the main menu.

### Review Tenants

1. Log in as the supplied [admin user](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user), a system administrator, or a member of the Supervisors group.

2. Select **Tenants** (formerly *Multi-Tenancy*) from the Administration menu. The Multi-Tenancy work area appears. This lists the defined tenants in your environment, including the default tenant, *Visual Data Discovery*.

3. To review a tenant, select its name in the list. The Edit Tenant work area appears. Select Cancel to return to the tenant list.

   If you want to see if a user is assigned to a tenant, see [List and Review Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#list-and-review-users).

4. When you have reviewed the tenants in your environment, navigate away from this work area by selecting an option from the main menu.

<h2 id="enable-or-disable-tenants">
  Enable or Disable Tenants
</h2>

Your tenants can be enabled and disabled. When you create tenant for the first time, it is automatically enabled.

### Disable a Tenant

<Note>
  The default tenant , *Visual Data Discovery,* can not be disabled.
</Note>

**Disable a tenant**

1. Log in as the supplied [admin user](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user), a system administrator, or a member of the Supervisors group.

2. Select **Tenants** (formerly *Multi-Tenancy*) from the Administration menu.

   The Multi-Tenancy work area appears, listing the existing tenants in your environment.

3. Select the name of the tenant you want to disable from the list.

   The Edit Tenant work area appears.

4. Select (check) the **Disabled** checkbox (formerly *Disable Tenant*) for the chosen tenant.

5. Select **Save** to save your changes to the tenant.

After a tenant is disabled, users assigned to it can no longer switch to that tenant. If this is the only tenant a user is assigned to, they are shown a message to contact their system administrator the next time they log in.

### Enable a Tenant

**Enable a tenant**

1. Log in as the supplied [admin user](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user), a system administrator, or a member of the Supervisors group.

2. Select **Tenants** (formerly *Multi-Tenancy*) from the Administration menu.

   The Multi-Tenancy work area appears, listing the existing tenants in your environment.

3. Select the name of the tenant you want to enable from the list.

   The Edit Tenant work area appears. If you want to edit a different tenant, select the tenant name and pick a different tenant to edit in the dialog.

4. Clear (uncheck) the **Disabled** checkbox (formerly *Disable Tenant*) for the chosen tenant.

5. Select **Save** to save your changes to the tenant.

After a tenant is enabled, users that assigned to it can now switch to it while they are logged into other tenants to which they are assigned.

<h2 id="about-the-supplied-self-service-analytics-tenant">
  About the Supplied Self-Service Analytics Tenant
</h2>

One unique Self-Service Analytics tenant is created during the installation process: *Visual Data Discovery*.

* The *Visual Data Discovery* tenant is a dedicated and permanent tenant that cannot be deleted. The [supplied admin user](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) and other system admin users can maintain tenants and perform system administrator-level functions.
* Members of the Supervisors group have full access to Self-Service Analytics Supervisors group actions, permissions, and specific supervisory functions that can be performed in the *Visual Data Discovery* tenant.
* Other users can be assigned as admins of any tenant. Simply add them to the **Administrators** group for the desired tenants.

<h2 id="specify-custom-tenant-attributes">
  Specify Custom Tenant Attributes
</h2>

You can define and manage custom tenant attributes when you create or edit a tenant account. This article covers updating tenant attributes.

### Supplied Context Variables

The following reserved context variables are available for use. You do not need to create custom tenant attributes for these attributes. Use these supplied context variables instead.

* sftp.host
* sftp.password
* sftp.port
* sftp.remoteDirectory
* sftp.strictHostKeyChecking
* sftp.user
* email.replyToAddress
* email.senderDisplayName

### Add A Custom Attribute for a Tenant

**Add a custom attribute for a tenant**

1. Access the Custom Attributes work area for the tenant.

2. Select **Add Custom Attribute**. A blank line is added to the Custom Attributes tab.

3. Supply values for the attribute, as described in the following table:

   | Tab Field | Description |
   | - | - |
   | Key | Specify the name of the custom attribute. The name cannot include braces. |
   | Value | Specify one or more values for the custom attribute. See below for more options. |
   | Usage | Shows how the attribute appears in the text entry fields of the application. |
   | Secure | Select this checkbox if you want to encrypt the custom attribute values. |
   | Delete | Select the delete button to remove the attribute. |

4. When you have specified all values, select **Save** to save the changes to your tenant.

### Remove a Custom Attribute from a Tenant

**Remove a custom attribute from a Tenant**

1. Access the Custom Attributes work area for the tenant.
2. Select the delete icon for the attribute you want to remove.
3. When are done removing your specific attributes, select **Save** to save the changes to your tenant.
