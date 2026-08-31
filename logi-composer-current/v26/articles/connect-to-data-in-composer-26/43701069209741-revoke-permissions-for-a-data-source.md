---
title: "Revoke Permissions for a Data Source"
id: 43701069209741
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701069209741-Revoke-Permissions-for-a-Data-Source
updated_at: 2026-08-31T04:13:21Z
---

# Revoke Permissions for a Data Source

# Revoke Permissions for a Data Source

You can revoke the data source permissions you previously granted to your tenant, to groups in your tenant, or to specific users in your tenant.

**Note:** In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.

**Revoke permissions for a data source**

1. Log in as an administrator or a user belonging to a group that includes the **Administer Sources** or the **Manage Source Permissions** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference). If you are logged in as a tenant admin, verify you're in or switch to the appropriate tenant.
2. Select the **Sources** card on your home page or **Data Sources** from the main menu.. The Sources work area opens.

   Some columns in this work area can be resized or sorted as needed; select the column header break to resize, or select the column name to change the sort.
3. Locate the row for the data source configuration in the list and select the permissions icon in the **Permissions** column. The Source Permissions dialog opens.
4. To completely revoke all source permissions for the tenant or for a group or user, locate the row for the tenant, group or user on the Source Permissions dialog and select the delete icon. The tenant , group, or user is removed from the dialog.

   You can also revoke specific permissions by changing the checkbox selections for the tenant or group on the Source Permissions dialog. If you clear (uncheck) the **Data Access** box (revoke **Data Access** permission), permission for the entire data source is revoked for the tenant, group, or user after you save. See [Modify Permissions for a Data Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080721037-Modify-Permissions-for-a-Data-Source).
5. Select **Save**. The Save Details dialog appears, listing the changes that you made.
6. Review the changes and select **OK**. The source authorization permissions are set.
