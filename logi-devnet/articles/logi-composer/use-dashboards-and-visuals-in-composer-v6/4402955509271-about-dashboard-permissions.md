---
title: "About Dashboard Permissions"
id: 4402955509271
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955509271-About-Dashboard-Permissions
updated_at: 2021-08-07T17:32:36Z
---

# About Dashboard Permissions

# About Dashboard Permissions

Dashboard permissions allow you to permit your entire account, groups within your account, or users within your account to read, write, or delete a dashboard. This allows you to share a dashboard with other users.

If a user belongs to a group that has the **Can Administer Dashboards**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference) enabled, the user can read, add, modify, or remove any dashboard in the Composer account. However, if the user does not belong to a group with this privilege enabled, the user can still be granted permission to read, write, or delete specific dashboards in the account using dashboard permissions. Dashboard permissions allow users in an account or group to read, write, or delete a dashboard, regardless of any group privilege settings that ordinarily limit their ability to do so.

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) To manage permissions of a dashboard, your Composer user definition must meet **one** of the following criteria:

* It must be an administrator, belonging to the [**Administrators** group](https://devnet.logianalytics.com/hc/en-us/articles/4402955414039-About-Supplied-Group-Definitions)
* It must belong to a group with the **Can Administer Dashboards** (ROLE\_ADMINISTER\_DASHBOARDS) [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference) enabled.
* It must belong to a group with the **Can Manage Dashboard Permissions** (ROLE\_PERMISSION\_DASHBOARDS) [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference) enabled. If your user definition has only this privilege (and *not* the **Can Administer Dashboards** privilege), you will only be able to manage permissions for the dashboards you can read.

  In addition, you may be restricted in which permissions you can assign. You can only assign permissions equivalent to your own. For example, if your user account has read permission for a dashboard, you can grant and revoke the read option available on the Dashboard Permissions panel. If you have write permission for a dashboard, you can grant and revoke the write option on the Dashboard Permissions panel.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) If your user account does not have read permission for a dashboard, you cannot see the dashboard on the Library page.

Dashboard permissions are determined using a most permissive model. For more information, see [*How Dashboard Permissions Are Determined*](https://devnet.logianalytics.com/hc/en-us/articles/4402955507991-How-Dashboard-Permissions-Are-Determined).

Dashboard permission specifications can also be made using the API endpoints `/api/dashboards/<dashboardid>/acls`, `/api/dashboards/<dashboardid>/acls/bulk`, `GET /api/user/permissions/dashboards/<dashboardid>`, and `GET /api/inventory/<type>/<id>`. API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.

For more information, see the following topics:

* [*Grant Permissions for a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402955506711-Grant-Permissions-for-a-Dashboard)
* [*Modify Permissions for a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402955507351-Modify-Permissions-for-a-Dashboard)
* [*Revoke Permissions for a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402955508631-Revoke-Permissions-for-a-Dashboard)
* [*How Dashboard Permissions Are Determined*](https://devnet.logianalytics.com/hc/en-us/articles/4402955507991-How-Dashboard-Permissions-Are-Determined)
