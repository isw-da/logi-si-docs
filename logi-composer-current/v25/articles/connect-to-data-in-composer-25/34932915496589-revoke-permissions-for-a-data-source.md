---
title: "Revoke Permissions for a Data Source"
id: 34932915496589
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915496589-Revoke-Permissions-for-a-Data-Source
updated_at: 2026-05-26T22:07:12Z
---

# Revoke Permissions for a Data Source

# Revoke Permissions for a Data Source

You can revoke the data source permissions you previously granted to your tenant, to groups in your tenant, or to specific users in your tenant.

**Revoke permissions for a data source**

1. Log into Composer as an administrator or a user belonging to a group that includes the **Administer Sources** or the **Manage Source Permissions** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference).
2. Select **Sources** on the [top-level navigation banner](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933120256397-The-Top-Level-Navigation-Banner) or the [UI menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143886477-The-Composer-UI-Menu), or select the **Sources** box on the [Home page](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933063528717-Home-Page). The Sources work area opens.
3. Locate the row for the data source configuration in the list and select the permissions icon in the **Permissions** column. The Source Permissions dialog opens.
4. To completely revoke all source permissions for the tenant or for a group or user, locate the row for the tenant, group or user on the Source Permissions dialog and select the delete icon. The tenant , group, or user is removed from the dialog.

   You can also revoke specific permissions by changing the checkbox selections for the tenant or group on the Source Permissions dialog. If you clear (uncheck) the **Data Access** box (revoke **Data Access** permission), permission for the entire data source is revoked for the tenant, group, or user after you save. See [Modify Permissions for a Data Source](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932892540045-Modify-Permissions-for-a-Data-Source).
5. Select **Save**. The Save Details dialog appears, listing the changes that you made.
6. Review the changes and select **OK**. The source authorization permissions are set.
