> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Users

Self-Service Analytics provides the account management controls necessary to create users and manage user access of Self-Service Analytics. Authorization for users to use product features and functions is controlled by the [groups](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#manage-user-groups) to which the users are assigned.

<Note>
  User management is performed by Self-Service Analytics system administrators, users with the **Administer Users** group [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), and members of the Supervisors group. Group assignment is managed by administrators (or users with the **Administer Groups** group [privilege](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference)).
</Note>

User definitions can be manually created or [imported](#import-users) via the LDAP security protocol. In addition, if using SAML single sign-on protocol, users and groups may be automatically provisioned in Self-Service Analytics (account level synchronization). For more information, see [Supported Authentication Tools](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/authorization-tools).

<h2 id="add-users">
  Add Users
</h2>

The system [admin users](#admin-user) or a user who has been assigned to a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) can add users to your environment. If you use tenants to manage access to resources and data, the supplied [admin user](#admin-user) and users belonging to the Supervisor group can add users to one or more tenants during user creation as well.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

### When Logged In as Member of the Supervisors Group

Members of the Supervisors group can add new users to your environment, with the following caveats:

* The new user is not assigned to any groups. Only the supplied [admin user](#admin-user) or a user who has been assigned to a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) can assign groups to users. If you use tenants to manage access to resources and data, a tenant admin or a user who has been assigned to a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) can assign groups to users in the tenant.
* The **Require password change** switch on the **Info** tab is always *on* (set to **Yes**) to require users to change their password when they first log into Self-Service Analytics. Change to **No** if needed.
* If you use tenants to manage access to resources and data, new users are created in your environment with no tenant membership. Members of the Supervisors group or any system [admin user](#admin-user) can add new users to tenants as required.

**Add a user (Supervisor group members)**

1. Log in as a system [admin user](#admin-user) or a member of the Supervisors group. Select **Users** from the Administration menu (formerly *System Users*) to open the Users work area and list all users in your environment.

   In environments where the [enhanced-experience](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) toggle has been enabled, the menu option **System Users** has been removed from the main menu UI. Users with appropriate privileges can instead access users using the **User** menu option, and groups using the **Groups** menu option.

2. Select **New User**. A New User work area opens with three tabs: **Info**, **Tenant(s)**, and **Regional Settings**.

3. On the **Info** tab, enter the user login name, full name, email, and password values. Adjust the **Require password change** switch (**Yes** by default) as needed. See [Specify General User Information](#specify-general-user-information).

4. Select **Save** to save the new user. Until you save the user, you can not access the **Tenants(s)** and **Regional Settings** tabs for this user.

5. Select the user you just created from the user list. Assign the user to one or more tenants on the Tenant(s) tab, and optionally select a **Current Tenant** if they are assigned to multiple tenants. See [Assign and Remove Users in Tenants](#assign-and-remove-users-in-tenants).

6. On the **Regional Settings** tab, select a regional language for the user definition. See [Specify A User's Regional Settings](#specify-a-user-s-regional-settings).

7. Select **Save** to save the user.

<h3 id="when-logged-in-as-an-administrator-or-a-group-user-with-user">
  When Logged In as an Administrator or a Group User with User Management Privileges
</h3>

**Add a user (admin user or user with user management group privileges)**

1. Log in as an administrator or a user who has been assigned to a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

   If the user name you log in with is also associated with other Self-Service Analytics tenants, verify that the correct tenant is selected. See [Switch Tenants](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/acct-manage#switch-tenants).

2. Select **Users** from the Administration menu (formerly *Users and Groups*). The Users work area appears, listing all defined users in this tenant.

3. Select **New User**. A New User work area opens with three tabs: **Info**, **Custom Attributes**, and **Regional Settings**.

4. On the **Info** tab, enter the user login name, full name, email, and password values.

   Optionally, adjust the **Require password change** switch (**Yes** by default) as needed. See [Specify General User Information](#specify-general-user-information).

   Optionally, add the user to available groups.

5. Select **Save** to save the new user. Until you save the user, you can not access the **Custom Attributes** and **Regional Settings** tabs for this user.

6. On the **Custom Attributes** tab, specify custom attributes for the user. See [Specify Custom User Attributes](#specify-custom-user-attributes).

7. On the **Regional Settings** tab, select a regional language for the user definition. See [Specify A User's Regional Settings](#specify-a-user-s-regional-settings).

8. Select **Save** to save the user.

<h2 id="modify-users">
  Modify Users
</h2>

Self-Service Analytics administrators, tenant administrators, or a user who has been assigned to a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) can modify user accounts.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

<h3 id="modify-a-user-supervisors-group-members">
  Modify a User (Supervisors Group Members)
</h3>

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.
</Note>

1. Log in as the supplied [admin user](#admin-user) or a user in the Supervisors group. Select **Users** from the Administration menu (formerly *System Users*) to open the Users work area and list all users in your environment. If you are logged in as a tenant admin, verify you're in or switch to the appropriate tenant.

   <Note>
     In environments where the [enhanced-experience](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) toggle has been enabled, the menu option **System Users** has been removed from the main menu UI. Users with appropriate privileges can instead access users using the **User** menu option, and groups using the **Groups** menu option.
   </Note>

2. On the left side of the Users work area, select the name of the user you want to modify. The user information appears on the right side of the work area.

3. On the **Info** tab, modify the values for the user login name, full name, email, and password, as needed. See [Specify General User Information](#specify-general-user-information) and [Change Passwords](#change-passwords).

   <Note>
     You cannot change the groups to which a user is assigned. Groups can only be assigned by tenant administrators or tenant users who have been assigned to groups with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).
   </Note>

4. On the **Tenant(s)** tab, adjust the tenants to which the user is assigned or change the user's current tenant, as needed. See [Assign and Remove Users in Tenants](#assign-and-remove-users-in-tenants).

5. On the **Regional Settings** tab, change the regional language for the user as needed. See [Specify A User's Regional Settings](#specify-a-user-s-regional-settings).

6. Select **Save** to save the user.

<h3 id="modify-a-user-administrator-group-members-group-members-with">
  Modify a User (Administrator Group Members, Group Members with User Management Privileges)
</h3>

1. Log in as an administrator or a user who has been assigned to a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference). If you are logged in as a tenant admin, verify you're in or switch to the appropriate tenant.

   If the user name you log in with is also associated with other tenants, verify that the correct tenant is selected. See [Switch Tenants](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/acct-manage#switch-tenants).

2. Select **Users** from the Administration menu (formerly *Users and Groups*) to open the Users work area and list all users in your environment. If you are logged in as a tenant admin, verify you're in or switch to the appropriate tenant.

   <Note>
     In environments where the [enhanced-experience](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) toggle has been enabled, the menu option **System Users** has been removed from the main menu UI. Users with appropriate privileges can instead access users using the **User** menu option, and groups using the **Groups** menu option.
   </Note>

3. On the left side of the work area, select the name of the user you want to modify. The user information appears on the right side of the work area.

4. On the **Info** tab, supply values for the user login name, full name, email, password, and assigned groups, as needed. See [Specify General User Information](#specify-general-user-information). You can also use this tab to disable a user definition in the account. See [Enable and Disable Users](#enable-and-disable-users) .

5. On the **Custom Attributes** tab, specify or change custom attributes for the user as needed. See [Specify Custom User Attributes](#specify-custom-user-attributes).

6. On the **Regional Settings** tab, change the regional language for the user as needed. See [Specify A User's Regional Settings](#specify-a-user-s-regional-settings).

7. Select **Save** to save the user.

<h2 id="delete-users">
  Delete Users
</h2>

Administrators or a user who has been assigned to a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) can delete users in your environment or individual tenants.

<Note>
  In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases. If you are running an earlier release or your admin has not enabled the new interface, see [Delete a User (Previous Releases)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021605645-Delete-Users#PR).
</Note>

### Delete a User

**Applies to: Supplied Admin user or Supervisors Group member**

1. Log in as the supplied [admin user](#admin-user) (System Administrator) or a member of the Supervisors group.

2. Select **Users** (formerly *Users and Groups*) from the Administration section of the [main menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-main-menu). A Users work area opens, listing all users defined for your environment (single tenant environment) or the tenant you have selected to work in (multiple tenant environment).

3. Select the name of the user you want to delete and select its delete (-) icon. A warning dialog opens.

4. Select **Delete** to remove the user.

   The user is removed from your instance. See also [Assign and Remove Users in Tenants](#assign-and-remove-users-in-tenants).

### Modify a User

**Applies to: Admin Group members, Group members with User Management privileges**

1. Log in as an administrator or a user who has been assigned to a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Select **Users** from the Administration section of the [main menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-main-menu). A Users work area opens, listing all users defined for the tenant.

3. Select the name of the user you want to delete and select its delete (-) icon. A warning dialog opens.

4. Select **Delete** to remove the user.

   The user is removed from your instance. See also [Assign and Remove Users in Tenants](#assign-and-remove-users-in-tenants).

<h2 id="list-and-review-users">
  List and Review Users
</h2>

A system [admin user](#admin-user) and users who are assigned to a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) can review users in Self-Service Analytics and tenants.

<h3 id="list-and-review-all-users-in-your-environment-supervisors-group">
  List and Review All Users in Your Environment (Supervisors Group Members)
</h3>

1. Log in as a member of the Supervisors group, and select **Users** (formerly *System Users*) from the Administration menu. The Users work area opens, listing all users in your environment, from all tenants.

   In environments where the [enhanced-experience](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) toggle has been enabled, the menu option **System Users** has been removed from the main menu UI. Users with appropriate privileges can instead access users using the **User** menu option, and groups using the **Groups** menu option.

2. Select a user name on the left side of the page. A work area opens that includes three tabs of user details you can edit as needed.

   You can:

   * Modify the user information on the **Info** tab. See [Specify General User Information](#specify-general-user-information).
   * Review and assign the user to specific Self-Service Analytics tenants and select a primary tenant for this user on the **Tenants(s)** tab. See [Assign and Remove Users in Tenants](#assign-and-remove-users-in-tenants).
   * Specify regional settings for the user on the **Regional Settings** tab. See [Specify A User's Regional Settings](#specify-a-user-s-regional-settings).

3. Select any of the tabs in the work area to review the user settings.

<h3 id="list-and-review-all-users-in-your-environment-system">
  List and Review all Users in Your Environment (System Administrator or a User with User Management Privileges)
</h3>

1. Log in as a user who has been assigned to a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

   If the user name you log in with is also associated with other Self-Service Analytics tenants, verify you are using the *Visual Data Discovery* tenant to see all users, or a specific tenant to see only the users in that tenant. See [Switch Tenants](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/acct-manage#switch-tenants).

2. Select **Users** (formerly *Users and Groups*) from the Administration menu. The Users work area opens, listing all users in your environment, from all tenants.

3. Select a user name on the left side of the page. A work area opens that includes three tabs of user details you can edit as needed.

   You can:

   * Modify the user information on the **Info** tab. See [Specify General User Information](#specify-general-user-information).
   * Review and assign the user to specific Self-Service Analytics tenant and select a primary tenant for this user on the **Tenants(s)** tab. See [Assign and Remove Users in Tenants](#assign-and-remove-users-in-tenants).
   * Specify regional settings for the user on the **Regional Settings** tab. See [Specify A User's Regional Settings](#specify-a-user-s-regional-settings).

4. Select any of the tabs in the work area to review the user settings.

<h2 id="import-users">
  Import Users
</h2>

You can import users from Lightweight Directory Access Protocol (LDAP) or Active Directory if either protocol has been set up. Authorized users created and stored in these directories can be imported into your environment. You can import all users or select specific ones to add.

Self-Service Analytics can connect to an organization’s Active Directory (AD) and OpenLDAP directory services using configured LDAP settings. See [Use Lightweight Directory Access Protocol (LDAP)](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/authorization-tools#use-lightweight-directory-access-protocol-ldap).

<Note>
  Self-Service Analytics supports the auto-provisioning of users via the SAML single sign-on protocol. When auto-provisioning is set up, the user is automatically added when they first log in. For instructions on automatic provisioning of users and groups via SAML, see [Configure Self-Service Analytics to Support SAML](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/authorization-tools#configure-self-service-analytics-to-support-saml).
</Note>

<Note>
  When a user is imported from Active Directory or if user provisioning is enabled and a new Active Directory user is added, the corresponding user definition is automatically added. However, when a user is removed from Active Directory, the corresponding user is not automatically removed. Authentication does not occur for the removed user, but you will need to manually remove the user. See [Delete Users](#delete-users) .
</Note>

<h3 id="import-user-definitions-into-self-service-analytics-from-ldap">
  Import User Definitions into Self-Service Analytics from LDAP or Active Directory
</h3>

1. Log into Self-Service Analytics as a system admin, or member of the Supervisors group and verify that LDAP or Active Directory have been set up. See [Use Lightweight Directory Access Protocol (LDAP)](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/authorization-tools#use-lightweight-directory-access-protocol-ldap). Save the settings, then log out.

2. Log in as an administrator or a user who has been assigned to a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

   If the user name you log in with is also associated with other tenants, verify that the correct tenant is selected. See [Switch Tenants](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/acct-manage#switch-tenants).

3. Select **Users** (formerly *Users and Groups*) from the Administration section of the [main menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-main-menu). A Users work area opens, listing all users defined for your environment (single tenant environment) or the tenant you have selected to work in (multiple tenant environment).

4. Select **Import Users**. Upon successful access to your organization’s secure directory, a new tab appears listing all the available users that can be imported. You have the option to either select all users or individual users.

5. On the Import Users tab, select the users to be imported.

   <img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/auth/import-users.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=70d45758c203031aa3c13cd175f43b1d" alt="" width="703" height="457" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/auth/import-users.png" />

6. Select **Import**. When the import completes, you will see the users added to the user list.

7. On the **Info** tab of the user editor, select groups for each user. See [Specify General User Information](#specify-general-user-information).

   Do **not** change the user login name as this may cause conflicts when reconnecting to the LDAP or Active Directory are attempted.

   If you have enabled the auto-creation of groups, Self-Service Analytics creates the groups that user is assigned to if they do not already exist.

8. Select **Save** to save the user.

<h2 id="enable-and-disable-users">
  Enable and Disable Users
</h2>

You can enable or disable a user when you add a new user or modify an existing user. New users are enabled by default.

When you disable a user, the user is not removed from Self-Service Analytics, but the user no longer has access to the tenant in which they were disabled. If a user belongs to more than one tenant, they can still log into , but only to the tenants in which their user account is enabled. If their user account is disabled in all tenants, they can no longer log into Self-Service Analytics.

Enable or disable a user on the **Info** tab of the user.

Enable and disable users in a tenant if you are logged in as an administrator for the tenant or as a user who is assigned to a group in the tenant with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

### Disable a User

1. Access the **Info** tab for a user as a member of a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference). See [Add Users](#add-users) or [Modify Users](#modify-users).
2. Select (check) the **Disable User** checkbox at the bottom of the tab.
3. Select **Save** to save the user.

### Enable a User

1. Access the **Info** tab for a user as a member of a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference). See [Add Users](#add-users) or [Modify Users](#modify-users).
2. Clear (uncheck) the **Disable User** checkbox at the bottom of the tab.
3. Select **Save** to save the user.

<h2 id="specify-general-user-information">
  Specify General User Information
</h2>

When you add or modify a user, you can specify the following general information:

* The login name for the user
* The user's full name
* The user's email address
* The user's password
* Groups to which the user is assigned
* Whether the user is enabled or disabled

This general information is managed on the **Info** tab of the user editor. To access the **Info** tab, see [Add Users](#add-users) or [Modify Users](#modify-users). For information on the user settings that can be changed on other tabs, see:

* [Assign and Remove Users in Tenants](#assign-and-remove-users-in-tenants)
* [Specify Custom User Attributes](#specify-custom-user-attributes)
* [Specify A User's Regional Settings](#specify-a-user-s-regional-settings)
* [Enable and Disable Users](#enable-and-disable-users)

Tasks formerly performed by the Supervisor user are now performed by the default system admin and members of the Supervisors group. Any user who belongs to the Supervisors group or to a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference) can make changes to the general information of a user's **Info** tab.

<Note>
  The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
</Note>

The following table describes all the information you can change on the **Info** tab. The **Required?** column indicates whether the information is required in a user's definition.

<table>
  <thead>
    <tr>
      <th>Tab Field</th>
      <th>Required?</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>**Login Name**</td>
      <td>Yes</td>
      <td>---</td>

      <td>
        The login name for the user. This is also the name for the user definition. The login name must be unique in all accounts in the Self-Service Analytics instance. It must include at least one alphanumeric character.

        <br />

        The login name is used to log into Self-Service Analytics. See [Log Into the User Interface](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#log-into-the-user-interface).
      </td>
    </tr>

    <tr>
      <td>**Full Name**</td>
      <td>No</td>
      <td>---</td>
      <td>The full name of the user. Specify up to 40 characters of the user's given name.</td>
    </tr>

    <tr>
      <td>**Email**</td>
      <td>No</td>
      <td>---</td>
      <td>The email address of the user. Specify up to 254 characters of the user's email.</td>
    </tr>

    <tr>
      <td>**Change Password**</td>
      <td>Yes</td>
      <td>---</td>
      <td>Select to expand the Info tab and see the **Password** and **Confirm Password** fields.</td>
    </tr>

    <tr>
      <td>**Password**</td>
      <td>Yes</td>
      <td>---</td>
      <td>The password associated with this user name. The password must contain at least nine characters and must include one lowercase, one uppercase, one numeric, and one special character. Special characters include these characters: `!@#$%^&**()-_=+,.:;<>`</td>
    </tr>

    <tr>
      <td>**Confirm Password**</td>
      <td>Yes</td>
      <td>---</td>
      <td>The password associated with this user name. Use this text box to retype the password you specified in the **Password** text box when you initially create the user definition and when you change the password for the user.</td>
    </tr>

    <tr>
      <td>**Require password change**</td>
      <td>No</td>
      <td>Yes</td>

      <td>
        Use the **Require password change** switch to indicate whether the user should be prompted to change their password when they log on for the first time (or the first time after their password was set or changed).

        <br />

        When you create a new user, the **Require password change** switch on the **Info** tab is always on (set to **Yes**), but can be changed to **No**.
      </td>
    </tr>

    <tr>
      <td>**Add Groups**</td>
      <td>No</td>
      <td>---</td>

      <td>
        Select this button to assign the user to one or more groups in the account. The Add Group(s) dialog appears.

        <br />

        <img src="https://mintcdn.com/insightsoftware/1fCfZrK84x8KmAw8/simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/admin/add-groups-default-263.png?fit=max&auto=format&n=1fCfZrK84x8KmAw8&q=85&s=a2d43b06d9e7c0a4dc9b1ade6624f169" alt="add user to groups dialog" width="355" height="299" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/v26/work-areas/admin/add-groups-default-263.png" />

        <br />

        If your user ID is not assigned the **Administer Groups** privilege or is not an administrator, you cannot add users to a group.

        <br />

        <Note>
          Only administrators can assign users to the **Administrators** group.
        </Note>

        <br />

        Use the search box at the top of the dialog to locate a group name in the list. You can also sort the group names in ascending or descending order using the **Sort By Name** arrows.

        <br />

        After selecting (checking) one or more groups for the user definition, select **Apply** to assign the user to the groups and close the Add Group(s) dialog.

        <br />

        Users who belong to the Supervisors group do not have this field on the Info tab. Update their group membership in the group directly. Navigate to the menu option **Groups**, then select the Members tab to add or remove the user from a specific group in a specific tenant.
      </td>
    </tr>

    <tr>
      <td>**Disable User**</td>
      <td>No</td>
      <td>not checked</td>

      <td>
        This option appears only for administrators or users who are assigned to a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference). Use the **Disable User** checkbox to disable the user.

        <br />

        See [Enable and Disable Users](#enable-and-disable-users) .
      </td>
    </tr>
  </tbody>
</table>

<h2 id="specify-a-user-s-regional-settings">
  Specify A User's Regional Settings
</h2>

Set regional settings for a user to determine the language of each user and the format of numeric fields in a data source. For example, a user based in the United States sees number fields formatted for Italian currency differently than a user based in Italy. See [Number Formatting for Data Sources](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting) for more information.

These settings can be changed by an administrator or a user who has been assigned to a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

The user locale can be set using the **Regional Settings** tab, as well.

To access the **Regional Settings** tab, see [Add Users](#add-users) or [Modify Users](#modify-users). For information on the user settings that can be changed on other tabs for a user, see:

* [Assign and Remove Users in Tenants](#assign-and-remove-users-in-tenants)
* [Specify General User Information](#specify-general-user-information)
* [Specify Custom User Attributes](#specify-custom-user-attributes)
* [Enable and Disable Users](#enable-and-disable-users)

### Set the User Locale for a User

1. Navigate to the **Regional Settings** tab for a user. See [Add Users](#add-users) or [Modify Users](#modify-users).
2. Select the location for the user in the drop-down list of the **Regional Presets** box.
3. When all values have been specified, select **Save** to save the user.

<h2 id="assign-and-remove-users-in-tenants">
  Assign and Remove Users in Tenants
</h2>

You can assign or remove users in Self-Service Analytics tenants as a system [admin user](#admin-user) or a user in the Supervisors group.

### Assign a User to a Tenant

1. Log in as a [system administrator](#administrators-group) or a member of the Supervisors group.
2. On the left side of the Manage Users work area, select the name of the user you want to modify. The user information appears on the right side of the work area.
3. Select the **Tenant(s)** tab. This tab lists all the tenants to which the user is assigned and the number of groups to which the user is assigned in each tenant.
4. Select **Add Tenant(s)**. The Select Tenants(s) dialog appears.
5. Select (check) the tenants to assign the user to those tenants. If you clear (uncheck) the checkbox associated with a tenant here, user is removed from the tenant.
6. Select **Apply** when finished. The list of tenants on the **Tenant(s)** tab updates to reflect your changes.
7. Optionally, select a tenant for the user to use the next time they log in from available tenants in the **Current Tenant** field. See [Set the Current Tenant for a User](#set-the-current-tenant-for-a-user).
8. Select **Save** to save the user.

### Remove a User from a Tenant

1. Log in as a [system administrator](#administrators-group) or a member of the Supervisors group.

2. On the left side of the Manage Users work area, select the name of the user you want to modify. The user information appears on the right side of the work area.

3. Select the **Tenant(s)** tab. This tab lists all the tenants to which the user is assigned and the number of groups to which the user is assigned in each tenant.

4. You can remove the user from tenants in one of two ways:

   * Select the remove (<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-grey.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=b5cae506ca0133d74de0b5c2feb623ea" alt="" width="17" height="17" noZoom style={{display: 'inline', verticalAlign: 'middle', width: '17px', height: '17px', margin: '0 2px'}} data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/icons/delete-grey.png" />) icon next to the tenant you want to remove the user from. Select **Delete** when prompted to remove the user from this tenant.
   * Select **Add Tenant(s)**. The Select Tenants(s) dialog appears. Clear (uncheck) the checkbox associated with a tenant here, user is removed from the tenant. Select **Apply**: the list of tenants on the **Tenant(s)** tab updates to reflect your changes.

5. Optionally, select a tenant for the user to use the next time they log in from available tenants in the **Current Tenant** field. See [Set the Current Tenant for a User](#set-the-current-tenant-for-a-user).

6. Select **Save** to save the user.

<h2 id="set-the-current-tenant-for-a-user">
  Set the Current Tenant for a User
</h2>

If a user has access to multiple Self-Service Analytics tenants, you can specify the tenant they should use the next time they log in. After logging in, they can [switch tenants](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/acct-manage#switch-tenants), as needed.

After a user switches tenants, the most recent tenant they worked in is remembered and used the next time they log in. If a user is assigned to only one tenant, that tenant is always the current tenant.

<Note>
  The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.
</Note>

<h3 id="set-the-current-tenant-for-a-user-set-the-current-tenant-for-a">
  Set the Current Tenant for a User
</h3>

1. Log in as a system [admin user](#admin-user) or a user in the Supervisors group. Select **Users** from the Administration menu (formerly *System Users*) to open the Users work area and list all users in your environment.

   <Note>
     In environments where the [enhanced-experience](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) toggle has been enabled, the menu option **System Users** has been removed from the main menu UI. Users with appropriate privileges can instead access users using the **User** menu option, and groups using the **Groups** menu option.
   </Note>

2. On the left side of the Users work area, select the name of the user whose tenants you want to modify. The user information appears on the right side of the work area.

3. Select the **Tenant(s)** tab. This tab lists all the tenants to which the user is assigned and the number of groups to which the user is assigned in each tenant.

4. Select a tenant for the user to use the next time they log in from available tenants in the **Current Tenant** field.

5. Select **Save** to save the user.

<h2 id="change-passwords">
  Change Passwords
</h2>

<Note>
  Only users who are members of the Administrators group or the Supervisors group, or belong to a group that includes the **Administer Users** privilege can change an existing user's password or require them to change their password the next time they log in.
</Note>

### Change or Reset a Password

1. Log in as user who has been assigned to a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

2. Select **Users** (formerly *Users and Groups*) from the Administration menu. A work area opens you can use to add and manage users.

3. Select the user from the list of users whose password you want to reset. The account details for that user appear on the right side of the page.

4. On the **Info** tab, select **Change Password**.

5. Type the new password in the **Password** and **Confirm Password** boxes.

   <Note>
     Optionally, change the **Require password change** switch from the default **No** to **Yes**. If you change this to **Yes**, the user is prompted (and forced) to change their password when they next attempt to log in.
   </Note>

6. Select **Save** to save your changes.

7. The next time the user logs in, they can use the new password you set. They are prompted to change this password if **Require password change** was set to **Yes**.

<h2 id="supplied-users-and-user-groups">
  Supplied Users and User Groups
</h2>

Self-Service Analytics supplies one user: **[admin](#admin-user)**. The admin is the default system administrator, who can define other users and tenants, enable security features, and define user groups and privileges. To add more system administrators, create or add users to the Administrators group, Supervisors group, and Content Distributors group. When they belong to all three groups, they can perform all of the same functions as the default system admin.

After you have install and deployed Self-Service Analytics in your operating environment, access the application as the admin user from a web browser (see [System Requirements](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#system-requirements) for details).

<h3 id="admin-user">
  admin User
</h3>

The supplied **admin** user is defined as a system administrator and is a member of the Administrators group, the Supervisors group, and the Content Distributors group for the [supplied tenant](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/acct-manage#about-the-supplied-self-service-analytics-tenant). The **admin** user cannot be deleted.

The first time you log into the UI as the **admin** user, you are prompted to change the **admin** user password. Thereafter, you can change the password for the **admin** user only if you are logged into the UI as an administrator. See [Change Passwords](#change-passwords).

Other users can be defined as administrators or can be assigned to groups with some administrator privileges. See [Add Users](#add-users), [About Supplied Groups](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#about-supplied-groups), and [Group Privilege Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

<h3 id="administrators-group">
  Administrators Group
</h3>

Administrators group members include the [default admin user](#admin-user), who is a system administrator associated with the *Visual Data Discovery* tenant (formerly the *superaccount*).

Assign users to the Administrators group to give them administrative privileges to perform actions such as:

* Create and manage users and groups.
* Manage connectors.
* Create and manage custom charts.
* Access actions.

<Note>
  The Administrators group is an integral part of Self-Service Analytics management. Users in the group can be system administrators, and tenant admins for one or more tenants.
</Note>

<Note>
  Management of the supplied **Administrators** group can only be performed by a member of that group or by a user in a group with *all* the following [privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference): **Administer Users**, **Administer Groups**, and **Administer Dashboards**.
</Note>

See [Add Users](#add-users), [About Supplied Groups](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#about-supplied-groups), [Group Privilege Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference), and [The Main Menu](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access#the-main-menu).

<h3 id="administrators-group-tenant-admins">
  Administrators Group (Tenant Admins)
</h3>

Administrators group members in tenants can:

* Create and manage users, groups, and content in their tenants.
* Define custom charts in their tenants.
* Perform Console and Actions related tasks.
* Self-Service Analytics users can be added as system admins and tenant admins in your environment.

### Supervisors Group

The Supervisors group is designed to give you a group of users who can perform specific functions without giving them access to all tasks members of the Administrators group can perform in Self-Service Analytics.

Assign users to the Supervisors group to allow those users to:

* Manage tenants, including creating, removing, enabling, and disabling tenants. Except when initially creating a tenant, supervisors cannot change or assign administrators to the tenant.
* Manage the look and feel of your software environment.
* Manage product licenses.
* Manage connectors.
* Enable security privileges, and more.

If you would like a user to be a full system admin, add them to this group and the Content Distributors group as well. See [About Supplied Groups.](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#about-supplied-groups)

### Content Distributors Group

All system admins are automatically added to this group. No further action is needed.

The Content Distributors group is part of the *Visual Data Discovery* tenant. Members can create, maintain, and distribute content and objects such as sources and connections to all tenants in your environment.

If you would like a user to be a full system admin, add them to this group and the Supervisors group as well. See [About Supplied Groups.](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#about-supplied-groups)

<h2 id="why-can-not-i-recreate-users-that-previously-existed">
  Why can not I Recreate Users that Previously Existed?
</h2>

Users may notice that if they delete a user while logged in as an administrator, they cannot recreate users with the same username. When you delete users while logged in as an administrator, the user is not completely removed from the system. Instead, it is no longer assigned to the account. This happens to ensure that we do not delete a user who has been assigned several accounts by an administrator who has no authority to see the other accounts. So, the user remains in the system and cannot be recreated.

To completely delete a user, log in as the supervisor and delete the user there. The user will be completely removed from the system and you can then create a user with the same user name. See Manage Users.

<h2 id="specify-custom-user-attributes">
  Specify Custom User Attributes
</h2>

You can define custom attributes for a user's definition if you are logged in as a Self-Service Analytics system administrator, tenant administrator, or a user who is assigned to a group with [user management privileges](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/aaa-ov#group-privilege-reference).

Use custom attributes to store values that can be used as [parameters](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#use-user-attributes-for-connection-parameters), or variables, in [connection definitions](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connections-managing#use-user-attributes-for-connection-parameters), data source [row security filters](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/ds-security-row#insert-variables-for-row-security-restriction-filters), and in [custom SQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-source-creation-tab#custom-sql).

A primary use of custom attributes is for user credential pass-through. Add credentials to a user's custom attributes so users with access to a particular data source connected to your instance can use these saved credentials to maintain access privileges for that source within Self-Service Analytics.

<Note>
  User attributes set for users via the UI or using LDAP user definitions are encrypted when stored in metadata. To specify the encryption modes, see [Encryption](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/changing-encryption-mode).
</Note>

Custom attributes are defined using the **Custom Attributes** tab when you edit the user.

When you reference custom attributes in connection definitions, action URLs, attribute definitions, or a data source's custom SQL, they take the form of `${User.<custom-attribute-name>}`.

This section covers the following topics:

* [Supplied Context Variables](#supplied-context-variables)
* [Add A Custom Attribute for a User](#add-a-custom-attribute-for-a-user)
* [Remove a Custom Attribute from a User](#remove-a-custom-attribute-from-a-user)
* [Specify Multivalue (Array) Custom Attributes](#specify-multivalue-array-custom-attributes)
* [Specify Numeric Values in Custom Attributes](#specify-numeric-values-in-custom-attributes)
* [Specify Time Values in Custom Attributes](#specify-time-values-in-custom-attributes)

<h3 id="supplied-context-variables">
  Supplied Context Variables
</h3>

The following context variables are provided with Self-Service Analytics.

* `${User.composerUserName}`: include to insert the name of the user who is currently logged in.
* `${User.accountId}`: include to insert the user account ID of the user who is currently logged in.
* `${User.credentials}`: include to pass the session ID or trusted access token (in embedded environments) of the user.

You do not need to create custom user attributes for the user name or account ID. Use these supplied context variables instead.

<h3 id="add-a-custom-attribute-for-a-user">
  Add A Custom Attribute for a User
</h3>

**Add a custom attribute for a user**

1. Access the Custom Attributes tab for the user. See [Add Users](#add-users) or [Modify Users](#modify-users).

2. Select Add Custom Attribute. A blank line is added to the Custom Attributes tab.

3. Supply values for the attribute, as described in the following table:

   | Tab Field | Description |
   | - | - |
   | Key | Specify the name of the custom attribute. The name cannot include braces. |
   | Value | Specify one or more values for the custom attribute. See below for more options. |
   | Usage | Shows how the attribute appears in the text entry fields of the application. |
   | Secure | Select this checkbox if you want to encrypt the custom attribute values. |
   | Delete | Select the delete button to remove the attribute. |

4. When you have specified all values, select **Save** to save the user.

<h3 id="remove-a-custom-attribute-from-a-user">
  Remove a Custom Attribute from a User
</h3>

**Remove a custom attribute from a user**

1. Access the Custom Attributes tab for the user. See [Add Users](#add-users) or [Modify Users](#modify-users). The defined custom attributes are listed.
2. Select the delete button corresponding to the attribute you want to remove.
3. When are done removing your specific attributes, select **Save** to save the user.

<h3 id="specify-multivalue-array-custom-attributes">
  Specify Multivalue (Array) Custom Attributes
</h3>

For multivalue user attributes (arrays), the elements must be comma-separated and contain no redundant white spaces between elements. These multivalue custom attributes should only be used as arrays in INCLUDE and EXCLUDE filter operations. With all other filter operations, the custom attribute values are used as-is.

For example, an INCLUDE or EXCLUDE row security filter that uses a multivalue custom attribute containing the array (`["apples", "oranges", "bananas"]`) will interpret the values as three separate values, splitting the values on commas.

However, an EQUAL or NOT EQUAL row security filter using the same multivalue custom attribute would interpret the array values as a single value (`"apples,oranges,bananas"`).

Null values in multivalue custom attributes are processed as a special text marker - `[Null]`.

<h3 id="specify-numeric-values-in-custom-attributes">
  Specify Numeric Values in Custom Attributes
</h3>

Numeric value in custom attributes are supported as integers or floating-point values represented as text.

<h3 id="specify-time-values-in-custom-attributes">
  Specify Time Values in Custom Attributes
</h3>

For date-time values, the following formats are supported:

* ISO-8601 format with optional milliseconds (but no timezone): `yyyy-MM-ddTHH:mm:ss[.SSS]`
* Self-Service Analytics's default API time format: `yyyy-MM-dd HH:mm:ss.SSS`, milliseconds required.

Unix time stamp format (seconds/milliseconds) is not supported for date-time values.

The BETWEEN filter operator expects an array with two elements.

When you use a time-value custom attribute as a filter variable for a filter using BETWEEN, two explicit elements must be specified (for example `start_date` and `end_date`). The dates can be specified as static date-time values, dynamic time patterns, or single-value user attributes.

Specifications such as `[${User.date_array}]`, with the `date_array` attribute containing two elements are not supported.
