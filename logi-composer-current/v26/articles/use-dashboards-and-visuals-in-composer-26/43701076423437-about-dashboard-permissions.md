---
title: "About Dashboard Permissions"
id: 43701076423437
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076423437-About-Dashboard-Permissions
updated_at: 2026-05-29T14:08:04Z
---

# About Dashboard Permissions

# About Dashboard Permissions

Dashboard permissions allow you to permit your entire tenant, groups within your tenant, or users within your tenant to read, write, or delete a dashboard. This allows you to share a dashboard with other users.

If a user belongs to a group that has the **Administer Dashboards** [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) enabled, the user can read, add, modify, or remove any dashboard in the tenant. However, if the user does not belong to a group with this privilege enabled, the user can still be granted permission to read, write, or delete specific dashboards in the tenant using dashboard permissions. Dashboard permissions allow users in an tenant or group to read, write, or delete a dashboard, regardless of any group privilege settings that ordinarily limit their ability to do so.

**Note:** 
To manage permissions of a dashboard, a user must meet **one** of the following criteria:

* Must be an administrator, belonging to the **[Administrators](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021357837-About-Supplied-Groups#AdminGrp)** group or **[Content Distributors](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701021357837-About-Supplied-Groups#CDGrp)** group.
* Must belong to a group with the **Administer Dashboards** (ROLE\_ADMINISTER\_DASHBOARDS) [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) enabled.
* Must belong to a group with the **Manage Dashboard Permissions** (ROLE\_PERMISSION\_DASHBOARDS) [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) enabled. If your user definition has only this privilege (and *not* the **Administer Dashboards** privilege), you will only be able to manage permissions for the dashboards for which you have `READ` permission.

  In addition, you may be restricted in which permissions you can assign. You can only assign permissions equivalent to your own. For example, if your user account has read permission for a dashboard, you can grant and revoke the read option available on the Dashboard Permissions panel. If you have write permission for a dashboard, you can grant and revoke the write option on the Dashboard Permissions panel.

  **Note:** 
  If your user account does not have read permission for a dashboard, you cannot see the dashboard on the Library page.

Dashboard permissions are determined using a most permissive model. For more information, see [How Dashboard Permissions Are Determined](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076359437-How-Dashboard-Permissions-Are-Determined).

Dashboard permissions can also be managed using the API endpoints `GET /api/dashboards/{dashboardId}/acls`, `PUT and PATCH /api/dashboards/{dashboardId}/acls/bulk`, `GET /api/inventory/DASHBOARD/{id}`, and `GET /api/user/permissions/dashboards/{dashboardId}`.

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

* Users who have the [group privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) **Export Dashboards** (ROLE\_EXPORT\_DASHBOARDS) and READ for dashboards can export dashboards.
* Users who have [group privileges](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) of **Manage Connections** (ROLE\_MANAGE\_CONNECTIONS), and **Administer Sources** (ROLE\_ADMINISTER\_SOURCES), and **Administer Visuals** (ROLE\_ADMINISTER\_VISUALS), and **Administer Dashboards** (ROLE\_ADMINISTER\_DASHBOARDS) can import dashboards.

For more information, see the following topics:

* [Export Dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076601229-Export-Dashboards)
* [Import Dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093507213-Import-Dashboards)
* [Grant Permissions for a Dashboard](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093007629-Grant-Permissions-for-a-Dashboard)
* [Modify Permissions for a Dashboard](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701013885709-Modify-Permissions-for-a-Dashboard)
* [Revoke Permissions for a Dashboard](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701046743181-Revoke-Permissions-for-a-Dashboard)
* [How Dashboard Permissions Are Determined](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076359437-How-Dashboard-Permissions-Are-Determined)
