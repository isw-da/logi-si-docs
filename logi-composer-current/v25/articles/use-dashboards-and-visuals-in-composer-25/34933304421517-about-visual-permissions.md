---
title: "About Visual Permissions"
id: 34933304421517
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933304421517-About-Visual-Permissions
updated_at: 2026-05-26T22:08:38Z
---

# About Visual Permissions

# About Visual Permissions

Visual permissions allow you to permit your entire tenant, groups within your tenant, or users within your tenant to read, write, or delete a visual. This allows you to share a visual with other users.

If a user belongs to a group that has the **Administer Visuals** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) enabled, the user can read, add, modify, or remove any visual in Composer. However, if the user does not belong to a group with this privilege enabled, the user can still be granted permission to read, write, or delete specific visuals using visual permissions. Visual permissions allow users in a tenant or group to read, write, or delete a visual, regardless of any group privilege settings that ordinarily limit their ability to do so.

**Note:** 
To manage permissions of a visual, your Composer user must meet **one** of the following criteria:

* Must be an administrator, belonging to the [**Administrators** group](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932609516941-About-Supplied-Groups)
* Must belong to a group with the **Administer Visuals** (ROLE\_ADMINISTER\_VISUALS) [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) enabled.
* Must belong to a group with the **Manage Visual Permissions** (ROLE\_PERMISSION\_VISUALS) [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) enabled. If your user has only this privilege (and *not* the **Administer Visuals** privilege), you will only be able to manage permissions for the visuals you can read.

  In addition, you may be restricted in which permissions you can assign. You can only assign permissions equivalent to your own. For example, if your user account has read permission for a visual, you can grant and revoke the read option available on the Visual Permissions panel. If you have write permission for a visual, you can grant and revoke the write option on the Visual Permissions panel.

  **Note:** 
  If your user does not have read permission for a visual, you cannot view the visual in the Visual Gallery. If your user definition does not have write permission for a visual, you cannot save the visual.

Visual permissions are determined using a most permissive model. For more information, see [How Visual Permissions Are Determined](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933279573645-How-Visual-Permissions-Are-Determined).

Visual permission specifications can also be made using the API endpoints `GET api/visuals?includePermissions=true`, `PATCH /api/visuals/<visualId>/acls/bulk`, `GET /api/visuals/<visualId>/acls`, and `/api/user/permissions/visuals/<visualId>`.

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

**Permissions for imported objects**

When you [import dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932814514061-Import-Dashboards), associated resources such as visuals, sources, and connections are imported as well. You can quickly grant default access levels to all imported and associated objects in your tenants by enabling **Share Default Access With All Users** at import time. Users are granted Data Access to Sources and Read access to Visuals and Dashboards.

For more information, see the following topics:

* [Grant Permissions for a Visual](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933273320845-Grant-Permissions-for-a-Visual)
* [Modify Permissions for a Visual](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933263646221-Modify-Permissions-for-a-Visual)
* [Revoke Permissions for a Visual](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933263870733-Revoke-Permissions-for-a-Visual)
* [How Visual Permissions Are Determined](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933279573645-How-Visual-Permissions-Are-Determined)
