---
title: "Modify Permissions for a  Dashboard"
id: 43701013885709
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701013885709-Modify-Permissions-for-a-Dashboard
updated_at: 2026-05-29T14:08:04Z
---

# Modify Permissions for a  Dashboard

# Modify Permissions for a Dashboard

You can modify the dashboard permissions you granted to your tenant, to groups in your tenant, or to specific users in your tenant.

**Modify permissions for a dashboard**

1. Log into Composer as an administrator or a user belonging to a group that includes the **Administer Dashboards** or the **Manage Dashboard Permissions** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference).
2. Select **Library** on the [top-level navigation banner](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701115577869-The-Top-Level-Navigation-Banner) or the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu), or select the **Dashboards** box on the [Home page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page). The library displays the list of dashboards.
3. Locate the row for the dashboard in the list and select the permissions icon in the Permissions column. The Dashboard Permissions dialog appears, showing current rights for tenants, groups, and users.
4. If you want to add permissions for all users in your tenant or for additional groups or users in your tenant, select **Add** on the Dashboard Permissions dialog and then select **Groups**, **Users**, or **Tenant** from the drop-down menu.

   * If you select **Groups**, the Add Groups dialog appears, listing all the groups available in your tenant. The [supplied groups](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021357837-About-Supplied-Groups) are not shown; permissions can not be changed for those groups.
   * If you select **Users**, the Add Users dialog appears, listing all the users available in your tenant.
   * If you select **Tenant**, Read permission is selected for your tenant in the Dashboard Permissions dialog. When finished, select **Apply**.
   * Members of the Administrators group have read, write, and delete permissions for every dashboard in the tenant.
   * The user who created the dashboard is automatically selected and has **Read**, **Write**, and **Delete** permissions, although these permissions can be changed.
5. Modify the **Read**, **Write**, or **Delete** checkbox selections for the tenant or any of the users or groups on the Dashboard Permissions dialog to indicate what users in them can do with the dashboard.

   **Read** permission is assumed and is always selected. If you clear (uncheck) the **Read** box (revoke **Read** permission), permission for the entire dashboard is revoked for the tenant, group, or user after you save.
6. Select **Save**. The Save Details dialog appears, listing the changes that you made.
7. Review the changes and select **OK**. The dashboard permissions are set.
