---
title: "Grant Permissions for a Visual"
id: 43701199414925
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701199414925-Grant-Permissions-for-a-Visual
updated_at: 2026-05-29T14:09:49Z
---

# Grant Permissions for a Visual

# Grant Permissions for a Visual

You can grant read, write, or delete visual permissions for your tenant, groups in your tenant, or specific users in your tenant.

**Grant permissions for a visual**

1. Log in as an administrator or a user belonging to a group that includes the **Administer Visuals** or the **Manage Visual Permissions** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference). If you are logged in as a tenant admin, verify you're in or switch to the appropriate tenant.
2. Access the Visual Permissions dialog. Select **Visual Gallery** on the [top-level navigation banner](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701115577869-The-Top-Level-Navigation-Banner) or the [UI menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Composer-UI-Menu), or select the **Visuals** box on the [Home page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page). The Visuals page appears.
3. Locate the row for the visual in the list and select the permissions icon in the **Permissions** column. The Visual Permissions dialog appears.

   Initially, this dialog is populated with the permissions for the visual creator.
4. Select **Add** on the Visual Permissions dialog and then select **Groups**, **Users**, or **Tenant** from the drop-down menu.

   * If you select **Groups**, the Add Groups dialog appears, listing all the groups available in your tenant. The [supplied groups](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021357837-About-Supplied-Groups) are not shown; permissions can not be changed for those groups.
   * If you select **Users**, the Add Users dialog appears, listing all the users available in your tenant.
   * If you select **Tenant**, Read permission is selected for your tenant on the Visual Permissions dialog.
   * Members of the Administrators group have read, write, and delete permissions for every visual in the tenant.
   * The user who created the visual is automatically selected and has **Read**, **Write**, and **Delete** permissions unless you revoke these permissions.
5. Select the tenant or any specific groups or users you want to permit to read, write, or delete the visual and select **Apply**. The Visual Permissions dialog lists your selections.
6. Select the **Read**, **Write**, or **Delete** checkboxes for the tenant, groups, or users to indicate what users in them can do with the visual. **Read** permission is assumed and is always selected. If you clear (uncheck) the **Read** box (revoke **Read** permission), permission for the entire visual is revoked for the tenant, group, or user after you save.
7. Select **Save**. The Save Details dialog appears, listing the changes that you made.
8. Review the changes and select **OK**. The visual permissions are set.

**Permissions for imported objects**

When you [import dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093507213-Import-Dashboards), associated resources such as visuals, sources, and connections are imported as well. You can quickly grant default access levels to all imported and associated objects in your tenants by enabling **Share Default Access With All Users** at import time. Users are granted Data access to sources and Read access to visuals and dashboards.
