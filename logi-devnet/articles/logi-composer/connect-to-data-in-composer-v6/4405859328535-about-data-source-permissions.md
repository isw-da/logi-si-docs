---
title: "About Data Source Permissions"
id: 4405859328535
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions
updated_at: 2021-09-21T01:28:20Z
---

# About Data Source Permissions

# About Data Source Permissions

As a Composer administrator or a user assigned to a group with the **Can Administer Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) or with the **Can Manage Source Permissions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference), you can provide the ability for users to read, write, or delete a data source configuration.

If a user created a data source configuration, they can always modify or remove it. If the user belongs to a group that has the **Can Administer Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) enabled, the user can read, add, modify, or remove any data source configuration in the Composer account. However, if the user does not belong to a group with this privilege enabled, the user can still be granted permission to read, write, or delete specific data sources in the account using source permissions. Data source permissions allow users to read, write, or delete a data source configuration, regardless of any group privilege settings that ordinarily limit their ability to do so.

#### Privilege Considerations

To manage permission settings for a data source, the Composer user must meet **one** of the following criteria:

* The user is an administrator, belonging to the [**Administrators** group](https://devnet.logianalytics.com/hc/en-us/articles/4405859110935-About-Supplied-Group-Definitions).
* The user belongs to a group with the **Can Administer Sources** (ROLE\_ADMINISTER\_SOURCES) [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) enabled.
* The user belongs to a group with the **Can Manage Source Permissions** (ROLE\_PERMISSION\_SOURCES) [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) enabled. If a user only has this privilege (and *not* the **Can Administer Sources** privilege), they can only manage permissions for data source configurations they can read.

  In addition, you may be restricted in which permissions you can assign. You can only assign permissions equivalent to your own. For example, if your user account has read permission for a data source, you can grant and revoke the read option available on the Source Permissions panel. If you have write permission for a data source, you can grant and revoke the write option on the Source Permissions panel.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If your user account does not have read permission for a data source, you cannot see the data source on the Sources page.

Data source permissions are determined using a most permissive model. For more information, see [*How Data Source Permissions Are Determined*](https://devnet.logianalytics.com/hc/en-us/articles/4405851030423-How-Data-Source-Permissions-Are-Determined).

#### Data Store Connection Considerations

Users with write permissions for a data source are automatically able to read the [connection definitions](https://devnet.logianalytics.com/hc/en-us/articles/4405850909079-Manage-Data-Store-Connections) for a data source. However, connection definitions can only be maintained by Composer administrators or users belonging to groups that have been granted the **Can Manage Connections**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference).

#### Fused Data Source Considerations

When you grant any permission to a fused data source, read permission to the parent data sources is granted as well. You should see a warning about this after saving the fused source permissions. If a user is not granted read permission for one of the data sources that comprise a fused source, only the General tab of the data source configuration wizard will be available to that user when they edit the fused data source.

In addition, fused data sources continue to respect the row security and permissions established for the underlying data sources that are joined in the fused data source.

#### Row and Column Security Considerations

Row and column security filters can be maintained for a data source by a:

* Composer administrator
* User in a group that has been granted the **Can Administer Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference)
* User in a group that has been granted the **Can Manage Source Permissions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) who also has **read** [permission](#) for the data source.

Security filters will not be applied to users with the privileges mentioned above. Source administrators can manage security filters for regular users but not for other source administrators.

For specific information about source permissions, see the following topics:

* [*Grant Permissions for a Data Source*](https://devnet.logianalytics.com/hc/en-us/articles/4405851029399-Grant-Permissions-for-a-Data-Source)
* [*Modify Permissions for a Data Source*](https://devnet.logianalytics.com/hc/en-us/articles/4405851031319-Modify-Permissions-for-a-Data-Source)
* [*Revoke Permissions for a Data Source*](https://devnet.logianalytics.com/hc/en-us/articles/4405859327255-Revoke-Permissions-for-a-Data-Source)
* [*How Data Source Permissions Are Determined*](https://devnet.logianalytics.com/hc/en-us/articles/4405851030423-How-Data-Source-Permissions-Are-Determined)

Data source permission specifications can also be made using the API endpoints `GET /api/user/permissions/sources`, `GET /api/user/permissions/sources/<sourceid>`, `GET /api/user/permissions/sources/<sourceid>`, `GET /api/sources/<sourceid>/acls`, and `PUT /api/sources/<sourceid>/acls/bulk`.

When you use the `GET /api/sources/<sourceid>/acls` endpoint, you can restrict the list to specific users, groups, or accounts using the `sidTypes` parameter. In addition, you can use the `returnSids` parameter to restrict the list so it retrieves only users, groups, or accounts with access to the data sources or to only users, groups, or accounts without access.

API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.
