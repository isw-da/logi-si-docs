---
title: "Modify Permissions for a Data Source"
id: 43701080721037
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080721037-Modify-Permissions-for-a-Data-Source
updated_at: 2026-08-26T07:09:46Z
---

# Modify Permissions for a Data Source

# Modify Permissions for a Data Source

You can modify the data source permissions you granted to your tenant, to groups in your tenant, or to specific users in your tenant.

**Note:** In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.

**Modify permissions for a data source**

1. Log in as an administrator or a user belonging to a group that includes the **Administer Sources** or the **Manage Source Permissions** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference). If you are logged in as a tenant admin, verify you're in or switch to the appropriate tenant.
2. Select the **Sources** card on your home page or **Data Sources** from the main menu.. The Sources work area opens.

   Some columns in this work area can be resized or sorted as needed; select the column header break to resize, or select the column name to change the sort.
3. Locate the row for the data source in the list and select the permissions icon in the **Permissions** column. The Source Permissions dialog appears.
4. If you want to add permissions for all users in your tenant or for additional groups or users in your tenant, select **Add** on the Source Permissions dialog and then select **Groups**, **Users**, or **Tenant** from the drop-down menu.

   * If you select **Groups**, the Add Groups dialog appears, listing all the groups available in your tenant. The [supplied groups](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021357837-About-Supplied-Groups) are not shown; permissions can not be changed for those groups.
   * If you select **Users**, the Add Users dialog appears, listing all the users available in your tenant.
   * If you select **Tenant**, Read permission is selected for your tenant on the Source Permissions dialog.
   * Members of the Administrators group have read, write, and delete permissions for every source in the tenant.
   * The user who created the source is automatically selected and has**Data Access**, **Read**, **Write**, and **Delete** permissions unless you revoke these permissions.
5. Select the **Data Access**, **Read**, **Write**, or **Delete** checkboxes for the tenant, groups, or users to indicate what users in them can do with the data source. **Data Access** permission is assumed and is always selected. If you clear (uncheck) the check box (revoke **Data Access** permission), permission for the entire data source is revoked for the tenant , group, or user after you save.
6. Select **Save**. The Save Details dialog appears, listing the changes that you made.
7. Review the changes and select **OK**. The source authorization permissions are set.
