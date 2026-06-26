---
title: "About Visual Permissions"
id: 4405851253271
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851253271-About-Visual-Permissions
updated_at: 2021-09-21T01:30:27Z
---

# About Visual Permissions

# About Visual Permissions

Visual permissions allow you to permit your entire account, groups within your account, or users within your account to read, write, or delete a visual. This allows you to share a visual with other users.

If a user belongs to a group that has the **Can Administer Visuals**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) enabled, the user can read, add, modify, or remove any visual in the Composer account. However, if the user does not belong to a group with this privilege enabled, the user can still be granted permission to read, write, or delete specific visuals in the account using visual permissions. Visual permissions allow users in an account or group to read, write, or delete a visual, regardless of any group privilege settings that ordinarily limit their ability to do so.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) To manage permissions of a visual, your Composer user definition must meet **one** of the following criteria:

* It must be an administrator, belonging to the [**Administrators** group](https://devnet.logianalytics.com/hc/en-us/articles/4405859110935-About-Supplied-Group-Definitions)
* It must belong to a group with the **Can Administer Visuals** (ROLE\_ADMINISTER\_VISUALS) [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) enabled.
* It must belong to a group with the **Can Manage Visual Permissions** (ROLE\_PERMISSION\_VISUALS) [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) enabled. If your user definition has only this privilege (and *not* the **Can Administer Visuals** privilege), you will only be able to manage permissions for the visuals you can read.

  In addition, you may be restricted in which permissions you can assign. You can only assign permissions equivalent to your own. For example, if your user account has read permission for a visual, you can grant and revoke the read option available on the Visual Permissions panel. If you have write permission for a visual, you can grant and revoke the write option on the Visual Permissions panel.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If your user definition does not have read permission for a visual, you cannot view the visual in the Visual Gallery. If your user definition does not have write permission for a visual, you cannot save the visual.

Visual permissions are determined using a most permissive model. For more information, see [*How Visual Permissions Are Determined*](https://devnet.logianalytics.com/hc/en-us/articles/4405851251479-How-Visual-Permissions-Are-Determined).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If you upgrade from a previous version to Composer 6.9, previously created visuals are automatically granted account, group, or user permissions for the visual based on their current permissions for the data source used by the visual.

Visual permission specifications can also be made using the API endpoints `GET api/visuals?includePermissions=true`, `PATCH /api/visuals/<visualId>/acls/bulk`, `GET /api/visuals/<visualId>/acls`, and `/api/user/permissions/visuals/<visualId>`. API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.

For more information, see the following topics:

* [*Grant Permissions for a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405859565207-Grant-Permissions-for-a-Visual)
* [*Modify Permissions for a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405859566231-Modify-Permissions-for-a-Visual)
* [*Revoke Permissions for a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405851252375-Revoke-Permissions-for-a-Visual)
* [*How Visual Permissions Are Determined*](https://devnet.logianalytics.com/hc/en-us/articles/4405851251479-How-Visual-Permissions-Are-Determined)
