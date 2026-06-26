---
title: "Modify Permissions for a Data Source"
id: 34932892540045
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932892540045-Modify-Permissions-for-a-Data-Source
updated_at: 2026-05-26T22:07:06Z
---

# Modify Permissions for a Data Source

# Modify Permissions for a Data Source

You can modify the data source permissions you granted to your tenant, to groups in your tenant, or to specific users in your tenant.

**Modify permissions for a data source**

1. Log into Composer as an administrator or a user belonging to a group that includes the **Administer Sources** or the **Manage Source Permissions** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference). If you are logged in as a tenant admin, verify you're in or switch to the appropriate tenant.
2. Select **Sources** on the [top-level navigation banner](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933120256397-The-Top-Level-Navigation-Banner) or the [UI menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143886477-The-Composer-UI-Menu), or select the **Sources** box on the [Home page](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933063528717-Home-Page). The Sources work area opens.
3. Locate the row for the data source in the list and select the permissions icon in the **Permissions** column. The Source Permissions dialog appears.
4. If you want to add permissions for all users in your tenant or for additional groups or users in your tenant, select **Add** on the Source Permissions dialog and then select **Groups**, **Users**, or **Tenant** from the drop-down menu.

   * If you select **Groups**, the Add Groups dialog appears, listing all the groups available in your tenant. The [supplied groups](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932609516941-About-Supplied-Groups) are not shown; permissions can not be changed for those groups.
   * If you select **Users**, the Add Users dialog appears, listing all the users available in your tenant.
   * If you select **Tenant**, Read permission is selected for your tenant on the Source Permissions dialog.
   * Members of the Administrators group have read, write, and delete permissions for every source in the tenant.
   * The user who created the source is automatically selected and has**Data Access**, **Read**, **Write**, and **Delete** permissions unless you revoke these permissions.
5. Select the **Data Access**, **Read**, **Write**, or **Delete** checkboxes for the tenant, groups, or users to indicate what users in them can do with the data source. **Data Access** permission is assumed and is always selected. If you clear (uncheck) the check box (revoke **Data Access** permission), permission for the entire data source is revoked for the tenant , group, or user after you save.
6. Select **Save**. The Save Details dialog appears, listing the changes that you made.
7. Review the changes and select **OK**. The source authorization permissions are set.
