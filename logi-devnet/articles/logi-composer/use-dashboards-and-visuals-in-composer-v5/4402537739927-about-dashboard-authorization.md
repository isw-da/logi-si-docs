---
title: "About Dashboard Authorization"
id: 4402537739927
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537739927-About-Dashboard-Authorization
updated_at: 2021-09-15T02:20:52Z
---

# About Dashboard Authorization

# About Dashboard Authorization

Dashboard authorization allows you to permit your entire account, groups within your account, or users within your account to read, write, or delete a dashboard. This allows you to share a dashboard with other users.

If a user belongs to a group that has the **Can Administer Dashboards**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402537668503-Group-Privilege-Reference) enabled, the user can read, add, modify, or remove any dashboard in the Composer account. However, if the user does not belong to a group with this privilege enabled, the user can still be granted permission to read, write, or delete specific dashboards in the account using dashboard authorization. Dashboard authorization allows users in an account or group to read, write, or delete a dashboard, regardless of any group privilege settings that ordinarily limit their ability to do so.

![](https://devnet.logianalytics.com/hc/article_attachments/4406753437463/noteicon.jpg) To manage authorization of a dashboard, your Composer user definition must meet **one** of the following criteria:

* It must be an administrator, belonging to the [**Administrators** group](https://devnet.logianalytics.com/hc/en-us/articles/4402552704919-About-Supplied-Group-Definitions)
* It must belong to a group with the **Can Administer Dashboards** (ROLE\_ADMINISTER\_DASHBOARDS) [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402537668503-Group-Privilege-Reference) enabled.
* It must belong to a group with the **Can Manage Dashboard Permissions** (ROLE\_PERMISSION\_DASHBOARDS) [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402537668503-Group-Privilege-Reference) enabled. If your user definition has only this privilege (and *not* the **Can Administer Dashboards** privilege), you will only be able to manage authorization for the dashboards you can read.

Dashboard permissions are determined using a most permissive model. For more information, see [*How Dashboard Permissions Are Determined*](https://devnet.logianalytics.com/hc/en-us/articles/4402537739287-How-Dashboard-Permissions-Are-Determined).

Dashboard authorization specifications can also be made using the API endpoints `/api/dashboards/<dashboardid>/acls`, `/api/dashboards/<dashboardid>/acls/bulk`, `GET /api/user/permissions/dashboards/<dashboardid>`, and `GET /api/inventory/<type>/<id>`. API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.

For more information, see the following topics:

* [*Granting Permissions for a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402552769431-Granting-Permissions-for-a-Dashboard)
* [*Modifying Permissions for a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402537738647-Modifying-Permissions-for-a-Dashboard)
* [*Revoking Permissions for a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402552770455-Revoking-Permissions-for-a-Dashboard)
* [*How Dashboard Permissions Are Determined*](https://devnet.logianalytics.com/hc/en-us/articles/4402537739287-How-Dashboard-Permissions-Are-Determined)
