> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Authorize Self-Service Analytics Access for Users in Groups

Your users can access Self-Service Analytics after you have defined their user accounts, added users to groups, and optionally, added users to tenants to grant access to content creation, content management, content access, and content use.

Self-Service Analytics supports several approaches to authenticating users, including SAML and LDAP. Choose the best approach given your existing constraints and objectives. A complete list of authentication tools supported is provided in [Supported Authentication Tools](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/authorization-tools).

<Note>
  SAML and LDAP groups that are automatically created in Self-Service Analytics must be manually assigned group data source access and privileges.
</Note>

Once authenticated, users have authorization to perform Self-Service Analytics functions and access resources as defined by their [group](#manage-user-groups) membership.

Use the following features to define and provide product access and authorization in Self-Service Analytics.

* Self-Service Analytics tenants: Use to separate product resources as necessary. Assign users to multiple tenants to allow access to each tenant's resources. You can further set up different groups, data connections, data sources, dashboards, and visuals for each tenant. See [Manage Tenants](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/acct-manage).
* User accounts: Define access for individual users in Self-Service Analytics. Assign users to one or more groups to give them access to data sources and product features. Users can belong to multiple groups in multiple tenants.
* Groups: Use to assign [privileges](#group-privilege-reference) to groups of users. Groups are most useful when a number of users require the same access restrictions. Users can be assigned to multiple groups. See [Manage User Groups](#manage-user-groups).

<h2 id="manage-user-groups">
  Manage User Groups
</h2>

Use groups to assign [privileges](#group-privilege-reference) to groups of users. Groups are most useful when a number of users require the same access restrictions. Users can be assigned to multiple groups.

<Note>
  SAML and LDAP groups that are automatically created in Self-Service Analytics must be manually assigned privileges.
</Note>

A Self-Service Analytics system administrator, tenant administrator, or a user who has been assigned to a group with [group management privileges](#group-privilege-reference) can manage groups. They can:

* Add, edit, or remove groups
* Assign and remove users in a group
* Authorize users in the group to perform specific functions

If your user account is not assigned the **Administer Groups** privilege or is not an administrator, you cannot assign groups to a user. In addition, only administrators can assign users to the **Administrators** group.

For more info about managing users, see [Manage Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage).

<h2 id="add-user-groups">
  Add User Groups
</h2>

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases. If you are running an earlier release or your admin has not enabled the new interface, see [Add Groups (Earlier Releases)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005381517-Add-User-Groups#Add).
</Note>

### Add Groups

System administrators and users who are assigned to a group with [group management privileges](#group-privilege-reference) can add groups to your instance or a tenant.

1. Log in as a system administrator or a user who has been assigned to a group with [group management privileges](#group-privilege-reference).

   If the user name you log in with is also associated with other tenants, verify that the correct tenant is selected. See [Switch Tenants](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/acct-manage#switch-tenants).

2. Select **Groups** (formerly *Users and Groups*) from the Administration menu. The Groups work area appears, listing all defined groups for this tenant.

3. Select **New Group** to open a New Group work area, with three tabs: **General**,**Members**, and **Privileges**.

   <Note>
     Add a group name on the **General** tab, then save the new group to access the other tabs.
   </Note>

4. Specify a group name on the **General** tab in the **Group Name** field. Optionally provide a short description of the group in the **Description** field.

5. Select **Save** to save the new group. The group is now defined, but has no members and only default assigned privileges.

6. Select the **Members** tab and assign users to the group. See [Add and Remove Members of a Group](#add-and-remove-members-of-a-group) for more information.

7. Select the **Privileges** tab and select privileges for the group. Any you add here grant permissions to all members of the group to perform specific actions or access specific features. See [Group Privilege Reference](#group-privilege-reference).

8. When you're done adding members and setting privileges, select **Save** to save your changes to the group.

## Modify User Groups

System administrators and users who are assigned to a group with [group management privileges](#group-privilege-reference) can modify groups in a tenant.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases. If you are running an earlier release or your admin has not enabled the new interface, see [Modify a Group (Earlier Releases)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701051224461-Modify-User-Groups#Modify).
</Note>

<Note>
  Management of the [supplied **Administrators** group](#about-supplied-groups) can only be performed by a member of that group or by a user in a group with *all* the following [privileges](#group-privilege-reference): **Administer Users**, **Administer Groups**, and **Administer Dashboards**.
</Note>

### Modify a Group

1. Log in as a system administrator or a user who has been assigned to a group with [group management privileges](#group-privilege-reference).

   If the user name you log in with is also associated with other tenants, verify that the correct tenant is selected. See [Switch Tenants](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/acct-manage#switch-tenants).

2. Select **Groups** (formerly *Users and Groups*) from the Administration menu. The Groups work area appears, listing all defined groups for this tenant.

3. In the list of groups, locate the name of the group you want to modify. The group editor work area opens.

4. Select the **General** tab to change the group name in the **Group Name** box. Optionally update the description of the group in the **Description** box.

5. Select the **Members** tab and assign and remove users in the group. See [Add and Remove Members of a Group](#add-and-remove-members-of-a-group) for more information.

6. Select the **Privileges** tab and update the privileges for the group. Privileges allow the administrator to grant permission to perform specific functions to all members of a group. See [Group Privilege Reference](#group-privilege-reference) for more information.

7. After members and privileges have been updated for the group, select **Save** to save the group.

## Delete User Groups

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases. If you are running an earlier release or your admin has not enabled the new interface, see [Delete Groups (Earlier Releases)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700987514893-Delete-User-Groups#Delete).
</Note>

### Delete Groups

System administrators and users who are assigned to a group with [group management privileges](#group-privilege-reference) can delete groups in a tenant.

1. Log in as a system administrator or a user who has been assigned to a group with [group management privileges](#group-privilege-reference).

   If the user name you log in with is also associated with other tenants, verify that the correct tenant is selected. See [Switch Tenants](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/acct-manage#switch-tenants).

2. Select **Groups** (formerly *Users and Groups*) from the Administration menu. The Groups work area appears, listing all defined groups for this tenant.

3. In the list of groups, locate the name of the group you want to delete and select its associated remove (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-open.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=02c9cbe530b9f34bd9a73851fdf499e2" alt="" width="16" height="18" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '18px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-open.png" />) icon. A warning dialog appears that prompts you to confirm that you want to delete the group.

4. Select **Delete** on the warning dialog to remove the group.

## List and Review User Groups

You can list and review groups in a tenant when you are logged in as a system administrator or as a user who has been assigned to a group with [group management privileges](#group-privilege-reference).

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

1. Log in as an administrator or a user who has been assigned to a group with [group management privileges](#group-privilege-reference).

   If the user name you log in with is also associated with other tenants, verify that the correct tenant is selected. See [Switch Tenants](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/acct-manage#switch-tenants).

2. Select **Groups** (formerly *Users and Groups*) from the Administration menu. The Groups work area appears, listing all defined groups for this tenant.

3. In the list of groups, locate the name of the group view. A work area for this group opens with three tabs: **General**,**Members**, and **Privileges**.

<h2 id="add-and-remove-members-of-a-group">
  Add and Remove Members of a Group
</h2>

You can add, remove, or delete users from a group when you are logged in as a system administrator or as a user who has been assigned to a group with [group management privileges](#group-privilege-reference).

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases. If you are running an earlier release or your admin has not enabled the new interface, see [Add or Remove Members (Earlier Releases)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700987395981-Add-and-Remove-Members-of-a-Group#Add).
</Note>

### Add or Remove Members

<Note>
  Management of the [supplied **Administrators** group](#about-supplied-groups) can only be performed by a member of that group or by a user in a group with *all* the following [privileges](#group-privilege-reference): **Administer Users**, **Administer Groups**, and **Administer Dashboards**.
</Note>

1. Log in as a system administrator or a user who has been assigned to a group with [group management privileges](#group-privilege-reference).

   If the user name you log in with is also associated with other tenants, verify that the correct tenant is selected. See [Switch Tenants](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/acct-manage#switch-tenants).

2. Select **Groups** (formerly *Users and Groups*) from the Administration menu. The Groups work area appears, listing all defined groups for this tenant.

3. Select the group to which you want to add or remove members. The group editor work area opens.

4. Select the **Members** tab.

5. Select **Add Members**. An Add Member(s) work area appears.

6. Select (check) the names of the users you want to add to the group. To remove members, clear (uncheck) the checkboxes for the user names you want to remove from the group.

   If all users should be added or removed in the group, select the **Select All** option.

   You can sort the user list by name in ascending or descending order to help you locate the user names you need.

   Use the search bar to easily locate a specific user in longer lists.

7. After making your changes, select **Apply**. The selected user(s) are added or removed in the editor, but the group must still be saved.

   <Note>
     You can remove users from the group on this screen by selecting the remove (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-open.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=02c9cbe530b9f34bd9a73851fdf499e2" alt="" width="16" height="18" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '18px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-open.png" /> )icon next to a user name, and select **Delete** on the resulting confirmation dialog.
   </Note>

8. Select **Save** to save the group and the membership changes. The selected user(s) are added or removed to the group. A save confirmation message displays.

<h2 id="about-supplied-groups">
  About Supplied Groups
</h2>

Several default groups are supplied with Self-Service Analytics. Add users to these groups to allow them to perform specific tasks related to the tenant(s) they may belong to in your environment . You can not delete, rename, or edit the privileges of these default groups. Add users as needed to each group, or [add more groups](#add-user-groups) to accommodate your organization's needs.

* **Administrators** - Group members include the [default admin user](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user), who is a system administrator assigned to the **Visual Data Discovery** tenant. If your environment includes tenants, each tenant includes an Administrators group: all tenant admins belong to that group.

* **Supervisors** - Add users as group members to allow them to perform specific functions without giving them access to reserved administrator tasks. Only the supplied [admin user](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or other system administrator can add users to this group.

* **Content Distributors** - Add users as group members to allow them to create, maintain, and distribute content to any tenant.

  <Warning>
    If you use the Content Distributors group, add them to [another user group you define](#add-user-groups) to give them access to the features you designate beyond Content Distributors.
  </Warning>

<Warning>
  The default tenant installed with Self-Service Analytics is the **Visual Data Discovery** tenant. If you do not add multiple tenants, all users belong to the **Visual Data Discovery** tenant by default. If your environment includes multiple tenants, users can be members of different groups in each tenant, depending on your organization's needs.
</Warning>

<h3 id="administrators-group-system-admins">
  Administrators Group (System Admins)
</h3>

Administrators group members include the [default admin user](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user), who is a system administrator associated with the **Visual Data Discovery**tenant.

Assign users to the Administrators group to give them administrative privileges to perform actions such as:

* Create and manage users and groups.
* Manage connectors.
* Create and manage custom charts.
* Access actions.

<Note>
  The Administrators group is an integral part of Self-Service Analytics management. Users in the group can be system administrators, and tenant admins for one or more tenants.
</Note>

<Note>
  Management of the supplied **Administrators** group can only be performed by a member of that group or by a user in a group with *all* the following [privileges](#group-privilege-reference): **Administer Users**, **Administer Groups**, and **Administer Dashboards**.
</Note>

See [Add Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#add-users), Authorize Self-Service Analytics Access for Users in Groups, [Group Privilege Reference](#group-privilege-reference), and [The Main Menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-main-menu).

<h3 id="administrators-group-tenant-admins">
  Administrators Group (Tenant Admins)
</h3>

Administrators group members in tenants can:

* Create and manage users, groups, and content in their tenants.
* Define custom charts in their tenants.
* Perform Console and Actions related tasks.
* Self-Service Analytics users can be added as system admins and tenant admins in your environment.

### Supervisors Group

The Supervisors group is designed to give you a group of users who can perform specific functions without giving them access to all tasks members of the Administrators group can perform.

All system admins are automatically added to this group. No further actions related to this group are needed to create system admins. Add non-admin users to this group if needed.

Assign users to the Supervisors group to allow those users to:

* Manage tenants, including creating, removing, enabling, and disabling tenants. Except when initially creating a tenant, supervisors cannot change or assign administrators to the tenant.
* Manage the look and feel of data analytics environment.
* Manage product licenses.
* Manage connectors.
* Enable security privileges, and more.

If you would like a user to be a full system administrator, add them to this group and the Content Distributors group as well.

<h3 id="content-distributors-group">
  Content Distributors Group
</h3>

If you would like a user to be a full system administrator, add them to this group and the Supervisors group as well.

The Content Distributors group is part of the **Visual Data Discovery** tenant. Members can create, maintain, and distribute content to all tenants in your environment. Members of the Content Distributors group can:

* Import and export sources directly, or as part of importing and exporting dashboards.
* Import and export local and visual gallery visuals when importing and exporting dashboards.
* Import and export visual gallery visuals.
* Import and export dashboards.
* Import and export connections.

<h2 id="group-privilege-reference">
  Group Privilege Reference
</h2>

Group privileges are specified on the **Privileges** tab for a [group](#about-supplied-groups). Privileges allow a member of the Administrators group to grant permission to perform specific functions to all members of a group.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/auth/group-privileges-24-1.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=9a3d0ccf28d9ce0bcfdbaa60831733f6" alt="use this work area to set privileges for groups of users" width="444" height="463" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/auth/group-privileges-24-1.png" />

<table>
  <thead>
    <tr>
      <th>UI Privilege Name</th>
      <th>Assign this privilege to allow group members to...</th>
      <th>**Enabled by default in these groups:**</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Administer Visuals**

        <br />

        <br />

        <br />

        ROLE\_ADMINISTER\_VISUALS
      </td>

      <td>
        Create, read, update, and delete visuals from dashboards or from the Visual Gallery in the account.

        <br />

        <br />

        <br />

        When the **Administer Visuals Privilege** is granted, the privileges **Create Visuals**, **Export Visuals**, and **Managed Visual Permissions** are automatically granted.

        <br />

        <br />

        <br />

        In addition, users with the **Administer Visuals** privilege are automatically granted read, write, and delete permissions to all visuals in the account. However, if they do not also have [Data Access permission for the data source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-permissions) associated with a visual, they cannot see any data on the visual.
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Create Visuals**

        <br />

        <br />

        <br />

        ROLE\_CREATE\_VISUALS
      </td>

      <td>
        Create visuals. Users must also have Read permission for the data source selected for the visual.

        <br />

        <br />

        <br />

        When the **Administer Visuals** privilege is granted, this privilege is also granted.
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Export Visuals**

        <br />

        <br />

        <br />

        ROLE\_EXPORT\_VISUALS
      </td>

      <td>
        Import and export visuals. Users must also have Read permission for the data source selected for the visual.

        <br />

        <br />

        <br />

        When the **Administer Visuals** privilege is granted, this privilege is also granted.
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Manage Visual Permissions**

        <br />

        <br />

        <br />

        ROLE\_PERMISSION\_VISUALS
      </td>

      <td>
        Assign permissions to a visual. When the **Administer Visuals** privilege is granted, this privilege is also granted. If this privilege is *not* granted, the <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/permissions.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=85dac856f3efab89ddb9d150e2cf2099" alt="" width="15" height="15" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '15px', height: '15px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/permissions.png" /> icon and the Permissions column in the [Visual Gallery](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-gallery) do not appear in the UI.

        <br />

        <br />

        <br />

        See [About Visual Permissions](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/visual-auth).
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Administer Dashboards**

        <br />

        <br />

        <br />

        ROLE\_ADMINISTER\_DASHBOARDS
      </td>

      <td>
        Add, modify, or remove dashboards in the account, including dashboards created by other users.

        <br />

        <br />

        <br />

        When this privilege is granted, the **Create Dashboards**, **Export Dashboards**, and **Manage Dashboard Permissions** privileges are automatically granted.
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Create Dashboards**

        <br />

        <br />

        <br />

        ROLE\_CREATE\_DASHBOARDS
      </td>

      <td>
        Create dashboards and reports.

        <br />

        <br />

        <br />

        If this privilege is not granted, your users:

        <br />

        <br />

        <br />

        * **Add Dashboard** and **Add Report buttons** are not available in the [dashboard library](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-manage#use-the-library-for-dashboards) or [reports library](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/ssr-manage#use-the-self-service-reports-library).
        * Cannot import a dashboard or make of copy a dashboard using the Save As dialog.
        * Cannot make a copy of a report using the Save As dialog.

        <br />

        <br />

        <br />

        When the **Administer Dashboards** privilege is granted, the **Create Dashboards**privilege is automatically granted.
      </td>

      <td>
        * All groups, except Supervisors group
      </td>
    </tr>

    <tr>
      <td>
        **Export Dashboards**

        <br />

        <br />

        <br />

        ROLE\_EXPORT\_DASHBOARDS
      </td>

      <td>
        Export dashboard configuration JSON files.

        <br />

        <br />

        <br />

        If this privilege is not granted, users in the group can still export dashboards as screenshots (PNG) or PDF files, but they cannot export the dashboard configuration.

        <br />

        <br />

        <br />

        When the **Administer Dashboards** privilege is granted, this privilege is automatically granted.
      </td>

      <td>
        * Administrators group
        * Content Distributors group
      </td>
    </tr>

    <tr>
      <td>
        **Manage Dashboard Permissions**

        <br />

        <br />

        <br />

        ROLE\_PERMISSION\_DASHBOARDS
      </td>

      <td>
        Assign permissions to a dashboard.

        <br />

        <br />

        <br />

        If your user has the **Administer Dashboards** privilege, they automatically have this privilege as well.

        <br />

        <br />

        <br />

        If this privilege is not granted, the permissions (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/permissions.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=85dac856f3efab89ddb9d150e2cf2099" alt="" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/permissions.png" />) icon and the Permissions column on the Library page do not appear in the UI.

        <br />

        <br />

        <br />

        See [About Dashboard and Self Service Report Permissions](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-auth-permissions#about-dashboard-and-self-service-report-permissions).
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Administer Scheduled Reports**

        <br />

        <br />

        <br />

        ROLE\_ADMINISTER\_DASHBOARD\_REPORTS
      </td>

      <td>
        Create, edit, and delete all scheduled dashboard reports.

        <br />

        <br />

        <br />

        Grant Read access for dashboards to users who receive reports.
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Create Scheduled Reports**

        <br />

        <br />

        <br />

        ROLE\_CREATE\_DASHBOARD\_REPORTS
      </td>

      <td>Create, edit, and delete only your own scheduled dashboard reports.</td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Administer Tags**

        <br />

        <br />

        <br />

        ROLE\_ADMINISTER\_TAGS
      </td>

      <td>Create, assign, remove, and delete all content tags.</td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Create Tags**

        <br />

        <br />

        <br />

        ROLE\_CREATE\_TAGS
      </td>

      <td>Create, assign, and remove tags. Delete your own content tags.</td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Administer Sources**

        <br />

        <br />

        <br />

        ROLE\_ADMINISTER\_SOURCES
      </td>

      <td>
        Create, import, export, modify, review, and remove data source configurations in the account.

        <br />

        <br />

        <br />

        When this privilege is granted, the **Create New Data Sources**, **Manage Source Permissions** and **Edit Calculations** privilege are also granted.

        <br />

        <br />

        <br />

        In addition, users with the **Edit Calculations** privilege are automatically granted read, write, and delete permissions to all sources in the account.
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Create New Data Sources**

        <br />

        <br />

        <br />

        ROLE\_CREATE\_SOURCES
      </td>

      <td>
        Create new data source configurations.

        <br />

        <br />

        <br />

        When the **Administer Sources** privilege is granted, this privilege is also granted.
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Manage Source Permissions**

        <br />

        <br />

        <br />

        ROLE\_PERMISSION\_SOURCES
      </td>

      <td>
        Assign [permissions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-permissions) to a data source configuration and manage data source [row](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-security-row) and [column](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-security-row#restrict-access-to-fields-using-column-security) security filters.

        <br />

        <br />

        <br />

        If your user has the **Administer Sources** privilege, they automatically have this privilege as well.

        <br />

        <br />

        <br />

        If this privilege is *not* granted, the <img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/permissions.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=85dac856f3efab89ddb9d150e2cf2099" alt="" width="16" height="16" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '16px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/permissions.png" /> icon and the Permissions column on the Sources page do not appear in the UI. See [About Source Permissions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-permissions).
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Edit Calculations**

        <br />

        <br />

        <br />

        ROLE\_EDIT\_FORMULAS
      </td>

      <td>
        Add or edit custom metrics and derived fields.

        <br />

        <br />

        <br />

        Users with Read permission for a source and **Edit Calculations** can create and edit custom metrics and derived fields for the source.

        <br />

        <br />

        <br />

        Users with Write permission for a source can create and edit custom metrics and derived fields for the source.
      </td>

      <td>
        * All groups, except Supervisors group
      </td>
    </tr>

    <tr>
      <td>
        **Administer Folders**

        <br />

        <br />

        <br />

        ROLE\_ADMINISTER\_FOLDERS
      </td>

      <td>
        Add, modify, or remove folders, including folders created by other users.

        <br />

        <br />

        <br />

        When this privilege is granted, the **Create Folders** privilege is automatically granted.

        <br />

        <br />

        <br />

        Folders must be [enabled](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) to see this option.

        <Warning>
          This feature is considered to be released in beta for your testing purposes. Workflows and features may change before a production-ready version is released.
        </Warning>
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Create Folders**

        <br />

        <br />

        <br />

        ROLE\_CREATE\_FOLDERS
      </td>

      <td>
        Create folders.

        <br />

        <br />

        <br />

        When the **Administer Folders** privilege is granted, this privilege is also granted.

        <br />

        <br />

        <br />

        Folders must be [enabled](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) to see this option.

        <Warning>
          This feature is considered to be released in beta for your testing purposes. Workflows and features may change before a production-ready version is released.
        </Warning>
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Manage Folder Permissions**

        <br />

        <br />

        <br />

        ROLE\_PERMISSION\_FOLDERS
      </td>

      <td>
        Assign permissions to folders.

        <br />

        <br />

        <br />

        If your user has the **Administer Folders** privilege, they automatically have this privilege as well.

        <br />

        <br />

        <br />

        Folders must be [enabled](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) to see this option.

        <Warning>
          This feature is considered to be released in beta for your testing purposes. Workflows and features may change before a production-ready version is released.
        </Warning>
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Administer Alerts**

        <br />

        <br />

        <br />

        ROLE\_ADMINISTER\_ALERTS
      </td>

      <td>
        Add, modify, or remove alert definitions in the account, including alerts created by other users.

        <br />

        <br />

        <br />

        When this privilege is granted, the **Create Alerts** privilege is automatically granted.
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Create Alerts**

        <br />

        <br />

        <br />

        ROLE\_CREATE\_ALERTS
      </td>

      <td>
        Create alert definitions.

        <br />

        <br />

        <br />

        When the **Administer Alerts** privilege is granted, this privilege is also granted.
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Manage Connections**

        <br />

        <br />

        <br />

        ROLE\_MANAGE\_CONNECTIONS
      </td>

      <td>Add, modify, or remove the data store connection definitions used by connectors and the query engine to connect to your data stores.</td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Manage File Uploads**

        <br />

        <br />

        <br />

        ROLE\_MANAGE\_UPLOADS
      </td>

      <td>
        Remove unused files uploaded for a data source if they are not used by any other sources.

        <br />

        <br />

        <br />

        When the **Manage Connections** privilege is granted, this privilege is also granted.
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Manage Action Templates**

        <br />

        <br />

        <br />

        ROLE\_MANAGE\_ACTION\_TEMPLATES
      </td>

      <td>
        Add, modify, or remove the action templates required to integrate Self-Service Analytics visual and dashboard data into your third-party applications.

        <br />

        <br />

        <br />

        Action templates define your third-party application to Self-Service Analytics.
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Invoke Actions**

        <br />

        <br />

        <br />

        ROLE\_INVOKE\_ACTIONS
      </td>

      <td>Invoke an action template from a visual.</td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Administer Themes**

        <br />

        <br />

        <br />

        ROLE\_ADMINISTER\_THEMES
      </td>

      <td>Create, read, update, delete, list, activate, and otherwise manage themes for the UI.</td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Administer Users**

        <br />

        <br />

        <br />

        ROLE\_ADMINISTER\_USERS
      </td>

      <td>
        Administer other user definitions. When this privilege is granted, group users can:

        <br />

        <br />

        <br />

        * Add, disable, and remove user definitions
        * Reset user passwords
        * Define user custom attributes and regional settings

        <br />

        <br />

        <br />

        This privilege does not allow group members to update groups or the groups to which a user is assigned.

        <br />

        <br />

        <br />

        If your user ID is not assigned the **Administer Groups** privilege or is not an administrator, you cannot assign groups to a user.

        <br />

        <br />

        <br />

        In addition, only administrators can assign users to the **Administrators** group.
      </td>

      <td>
        * Administrators group
        * Supervisors group
      </td>
    </tr>

    <tr>
      <td>
        **Administer Groups**

        <br />

        <br />

        <br />

        ROLE\_ADMINISTER\_GROUPS
      </td>

      <td>
        Administer other group definitions. When this privilege is granted, group users can:

        <br />

        <br />

        <br />

        * Add or remove group definitions
        * Assign and remove users in a group definition
        * Authorize users in the group to perform specific functions

        <br />

        <br />

        <br />

        This privilege does not allow group members to add or otherwise maintain user definitions.
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Save Filters**

        <br />

        <br />

        <br />

        ROLE\_SAVE\_FILTERS
      </td>

      <td>
        Save (and share) filters created in visuals and dashboards.

        <br />

        <br />

        <br />

        When this privilege is not granted, the **Save Filter** privilege does not appear on Filter dialogs in the UI.
      </td>

      <td>
        * All groups, except Supervisors group
      </td>
    </tr>

    <tr>
      <td>
        **Manage Custom Charts**

        <br />

        <br />

        <br />

        ROLE\_MANAGE\_VISUALIZATION\_TYPES
      </td>

      <td>When you have this privilege, you can use the CLI to create custom charts, and manage custom charts using the Self-Service Analytics UI.</td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Generate Embed Code**

        <br />

        <br />

        <br />

        ROLE\_GENERATE\_EMBED\_CODE
      </td>

      <td>
        Generate an embeddable dashboard or visual gallery snippet for a dashboard in the dashboard library or the visual gallery.

        <br />

        <br />

        <br />

        See [Embed Components Into Your Application](/simba-embedded-analytics/docs/self-service-analytics/26.3/embed-and-extend/embed/dash-embed/dash-embed).
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Administer Initial Visuals**

        <br />

        <br />

        <br />

        ROLE\_ADMINISTER\_INITIAL\_VISUALS
      </td>

      <td>
        Users with this privilege have permission to update the list of available visualizations for a source.

        <br />

        <br />

        <br />

        See [Available Visual Types](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/visuals/available-visual-types).
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>
        **Administer Calendars**

        <br />

        <br />

        <br />

        ROLE\_ADMINISTER\_CALENDARS
      </td>

      <td>
        Users with this privilege can create, update, and delete alternative fiscal calendars.

        <br />

        <br />

        <br />

        See [Fiscal Calendars](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#fiscal-calendars).
      </td>

      <td>
        * Administrators group
      </td>
    </tr>

    <tr>
      <td>ROLE\_DISTRIBUTE\_CONTENT</td>
      <td>Users who belong to the Administrators group or Content Distributors group can make content available to your users and tenant users.</td>

      <td>
        * Administrators group
        * Content Distributors group
      </td>
    </tr>
  </tbody>
</table>

## Add and Remove Supervisors

<Note>
  The default **supervisor** user is no longer installed: add users to the **Supervisors** group instead. If you upgrade from an earlier version, the Supervisor user becomes a member of the Supervisors group in the *Visual Data Discovery* (formerly *superaccount*) tenant.
</Note>

After upgrading to Self-Service Analytics, the supplied [admin user](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) (System Administrator) or a member of the Administrators group can add or remove users in the Supervisors group.

Add any number of users to this group to allow them to perform specific functions without giving them access to all tasks members of the Administrators group can perform in the *Visual Data Discovery* tenant.

### Add a User to the Supervisors Group

1. Log in as the supplied [admin user](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Administrators group in *Visual Data Discovery*.

2. Select **Users** (formerly *Users and Groups*) from the Administration menu. The Users work area opens.

3. Select the user from the list of users you want to add to the Supervisors group. The account details for that user appear on the right side of the page.

4. On the **Info** tab, select **Add Group(s)**. The Select Account(s) dialog appears.

   <Note>
     If the user is already a member of the Supervisors group, this option is not shown.
   </Note>

5. Select (check) the group or groups you want to add this user to. When you add a user to the Supervisors group, they have full access to the supervisory functions. See [About the Supplied Self-Service Analytics Tenant](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/acct-manage#about-the-supplied-self-service-analytics-tenant).

6. Select **Apply** when finished.

7. Select **Save** to save the user.

The user is now a member of the Supervisors group.

### Remove a User from the Supervisors Group

You can remove a user from the Supervisors group by removing them from the Supervisors or by simply deleting their user account. See [Delete Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#delete-users) .

1. Log in as the supplied [admin user](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#admin-user) or a member of the Administrators group in *Visual Data Discovery*.
2. Select **Groups** (formerly *Users and Groups*) from the Administration menu. The Groups work area opens.
3. Select the Supervisors group from the list of groups. The details for that group appear on the right side of the page.
4. Select the **Members** tab. This tab lists all members of the Supervisors group.
5. Remove the user from the group by selecting the remove icon (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-open.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=02c9cbe530b9f34bd9a73851fdf499e2" alt="" width="16" height="18" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '16px', height: '18px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-open.png" />) next to the user's name. Confirm your deletion in the confirmation modal.
6. Select **Save** when finished. The list of users on the **Members** tab adjusts to show your changes.

## Disable the Supplied Supervisor User

<Note>
  The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
</Note>

<h3 id="disable-the-supplied-supervisor-user-disable-the-supplied">
  Disable the Supplied Supervisor User
</h3>

1. Log into Self-Service Analytics as a member of the Supervisors group who is not the supplied supervisor user (make sure you have selected the tenant **superaccount** or **Visual Data Discovery**).
2. On the left side of the page, select the **supervisor** user. The supervisor user information appears on the right side of the page.
3. Select (check) the **Disable User** checkbox at the bottom of the **Info** tab.
4. Select **Save** to save the supervisor definition.

## Change a Supervisor Password

<Note>
  The default **supervisor** user is no longer installed with Self-Service Analytics: add users to the **Supervisors** group instead. If you upgrade to Self-Service Analytics from an earlier version, the Supervisor user becomes a member of the Supervisors group in the *Visual Data Discovery* (formerly *superaccount*) tenant.
</Note>

Members of the Supervisors group can change their own passwords, or force a password change for other users the next time a selected user logs in. See [Change Passwords](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#change-passwords). A system administrator or users who are members of a group with [user management privileges](#group-privilege-reference) can change a password or force a password change for a member of the Supervisors group.

### Change a Password for Supervisor Group Members

<Note>
  Only a system administrator or users who are members of a group with [user management privileges](#group-privilege-reference) can change a password or force a password change for a member of the Supervisors group.
</Note>

**Change or reset password for Supervisors group members**

1. Log in as user who has been assigned to a group with [user management privileges](#group-privilege-reference).

2. Select **Users** (formerly *Users and Groups*) from the Administration menu. A work area opens you can use to add and manage users.

3. Select the user from the list of users whose password you want to reset. The account details for that user appear on the right side of the page.

4. On the **Info** tab, select **Change Password**.

5. Type the new password in the **Password** and **Confirm Password** boxes.

   <Note>
     Optionally, change the **Require password change** switch from the default **No** to **Yes**. If you change this to **Yes**, the user is prompted (and forced) to change their password when they next attempt to log in.
   </Note>

6. Select **Save** to save your changes.

7. The next time the user logs in, they can use the new password you set. They are prompted to change this password if **Require password change** was set to **Yes**.
