---
title: "Grant Permissions for a  Dashboard"
id: 43701093007629
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093007629-Grant-Permissions-for-a-Dashboard
updated_at: 2026-05-29T14:11:20Z
---

# Grant Permissions for a  Dashboard

# Grant Permissions for a Dashboard

You can grant read, write, or delete dashboard permissions for your tenant, groups in your tenant, or specific users in your tenant.

**Grant permissions for a dashboard**

1. Log in as an administrator or a user belonging to a group that includes the **Administer Dashboards** or the **Manage Dashboard Permissions** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference). If you are logged in as a tenant admin, verify you're in or switch to the appropriate tenant.
2. Select **Library** on the [top-level navigation banner](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701115577869-The-Top-Level-Navigation-Banner) or the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu), or select the **Dashboards** box on the [Home page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page) The library displays the list of dashboards.
3. Locate the row for the dashboard in the list and select the permissions icon in the Permissions column. The Dashboard Permissions dialog appears.

   ![set permissions for users in this work area](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242684233869 "Dashboard Permissions work area")
4. Select **Add** on the Dashboard Permissions dialog and then select **Groups**, **Users**, or **Tenant** from the drop-down menu.

   * If you select **Groups**, the Add Groups dialog appears, listing all the groups available in your tenant. The [supplied groups](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021357837-About-Supplied-Groups) are not shown; permissions can not be changed for those groups.
   * If you select **Users**, the Add Users dialog appears, listing all the users available in your tenant.
   * If you select **Tenant**, Read permission is selected for your tenant on the Source Permissions dialog.
   * Members of the Administrators group have data access, read, write, and delete permissions for every data source in the tenant.
   * The user who creates a data source is automatically selected and has **Data Access**, **Read**, **Write**, and **Delete** permissions unless you revoke these permissions.
5. Select tenants or any specific groups or users you want to permit to read, write, or delete the dashboard and select **Apply**. The Dashboard Permissions dialog lists your selections.

   ![set dashboard permissions dialog](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242695348621 "set dashboard permissions dialog")
6. Select the **Read**, **Comment**, **Write**, or **Delete** checkboxes for a tenant, groups, or users to indicate what they can do with the dashboard. **Read** permission is assumed and is always selected. If you clear (uncheck) the **Read** box (revoke **Read** permission), permission for the entire dashboard is revoked for the tenant, group, or user after you save.
7. Select **Save**. The Save Details dialog appears, listing the changes that you made.

   ![confirm your changes and save](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242679304589 "Save Details for permissions dialog")
8. Review the changes and select **OK**. The dashboard permissions are set.

**Permissions for imported objects**

When you [import dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093507213-Import-Dashboards), associated resources such as visuals, sources, and connections are imported as well. You can quickly grant default access levels to all imported and associated objects in your tenants by enabling **Share Default Access With All Users** at import time. Users are granted Data access to sources and Read access to visuals and dashboards.
