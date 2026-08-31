---
title: "Grant Permissions for a  Source"
id: 43701101299981
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701101299981-Grant-Permissions-for-a-Source
updated_at: 2026-08-31T04:15:55Z
---

# Grant Permissions for a  Source

# Grant Permissions for a Source

You can grant read, write, or delete data source configuration permissions for your tenant, groups in your tenant, or specific users in your tenant.

**Note:** In this release, when your admin enables the Enhanced Experience user interface, you will see changes to workflows you may have used in previous releases.

**Grant permissions for a data source**

1. Log in as an administrator or a user belonging to a group that includes the **Administer Sources** or the **Manage Source Permissions** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference). If you are logged in as a tenant admin, verify you're in or switch to the appropriate tenant.
2. Select the **Sources** card on your home page or **Data Sources** from the main menu.. The Sources work area opens.

   Some columns in this work area can be resized or sorted as needed; select the column header break to resize, or select the column name to change the sort.
3. Locate the row for the data source configuration in the list and select icon in its **Permissions** column. The Source Permissions dialog appears.

   Initially, this dialog lists only the creator of the data source.
4. Select **Add** on the Source Permissions dialog and then select **Groups**, **Users**, or **Tenant** from the drop-down menu.

   * If you select **Groups**, the Add Groups dialog appears, listing all the groups available in your tenant. The [supplied groups](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021357837-About-Supplied-Groups) are not shown; permissions can not be changed for those groups.
   * If you select **Users**, the Add Users dialog appears, listing all the users available in your tenant.
   * If you select **Tenant**, Read permission is selected for your tenant on the Source Permissions dialog.
5. Select the tenant or any specific groups or users you want to permit to read, write, or delete the data source and select **Apply**. The Source Permissions dialog lists your selections.

   ![use this work area to add or remove specific source permissions](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48527948434701 "Source Permissions work area")

   * Members of the Administrators group have data access, read, write, and delete permissions for every data source in the tenant.
   * The user who creates a data source is automatically selected and has **Data Access**, **Read**, **Write**, and **Delete** permissions.
6. Select the **Data Access**, **Read**, **Write**, or **Delete** checkboxes for the tenant, groups, or users to indicate what users in them can do with the data source. **Data Access** permission is assumed and is always selected. If you clear (uncheck) the check box (revoke **Data Access** permission), permission for the entire data source is revoked for the tenant, group, or user after you save.
7. Select **Save**. The Save Details dialog appears, listing the changes that you made.

   ![confirm your selections before saving](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48527909996813 "review your changes before saving")![review your changes before saving](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48527917347469 "Save Details for Source Permissions work area")
8. Review the changes and select **OK**. The source authorization permissions are set.

**Permissions for imported objects**

When you [import dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093507213-Import-Dashboards), associated resources such as visuals, sources, and connections are imported as well. You can quickly grant default access levels to all imported and associated objects in your tenants by enabling **Share Default Access With All Users** at import time. Users are granted Data access to sources and Read access to visuals and dashboards.
