---
title: "About Source Permissions"
id: 34932915596173
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions
updated_at: 2026-05-26T22:07:11Z
---

# About Source Permissions

# About Source Permissions

As a Composer user assigned to a group with the **Administer Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) or with the **Manage Source Permissions** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference), you can enable users to work with data sources by enabling **Data Access**, **Read**, **Write**, and **Delete** permissions for sources.

**Note:** 
If you try to delete a visual, filter snippet, dashboard, dashboard link, source, or source field, Composer displays an error message naming any objects dependent on the item you’re trying to delete. You can delete the item after you’ve removed the association from the dependent object.
See[Fields Usage](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932867958541-Fields-Usage).

Users who create a data source can always modify or remove it, unless their permissions are revoked. Users who belong to a group with the **Administer Sources** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) enabled have **Data Access**, **Read**, **Write**, and **Delete** permissions for any source in Composer.

You can grant data source access to users who do not belong to a group with [privileges](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) enabled by defining **Data Access**, **Read**, **Write**, and **Delete** permissions for individual sources.

**Data Access** is a separate permission for sources. It can be set directly on sources for users, groups, and tenants, and is enabled for users, groups, and tenants when you assign **Read** permission for a visual that uses that source. Unless they are granted Read permission to the source as well, they can't see the source listed on the Source page, or select the source to create a new visual (for users with the **Create Visuals** or **Administer Visuals** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference)).

#### Privilege Considerations

To manage permission settings for a source, a Composer user must meet **one** of the following criteria:

* The user is an administrator, belonging to the [**Administrators** group](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932609516941-About-Supplied-Groups).
* The user belongs to a group with the **Administer Sources** (ROLE\_ADMINISTER\_SOURCES) [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) enabled.
* The user belongs to a group with the **Manage Source Permissions** (ROLE\_PERMISSION\_SOURCES) [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) enabled. If a user only has this privilege (and *not* the **Administer Sources** privilege), they can only manage permissions for sources they can read.

  In addition, you may be restricted in which permissions you can assign. You can only assign permissions equivalent to your own. For example, if your user account has read permission for a source, you can grant and revoke the read option available on the Source Permissions panel. If you have write permission for a source, you can grant and revoke the write option on the Source Permissions panel.

  **Note:** 
  If your user account does not have read permission for a source, you can't see the source on the Sources page.

Source permissions are determined using a most permissive model. For more information, see [How Source Permissions Are Determined](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932923718157-How-Source-Permissions-Are-Determined).

#### Data Store Connection Considerations

Users with write permissions for a data source are automatically able to read the [connection definitions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932706697357-Manage-Data-Store-Connections) for a data source. However, connection definitions can only be maintained by Composer administrators or users belonging to groups that have been granted the **Manage Connections** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference).

#### Row and Column Security Considerations

Row and column security filters can be maintained for a data source by:

* an administrator.
* User in a group that has been granted the **Administer Sources** [privilege.](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference)
* User in a group that has been granted the **Manage Source Permissions** [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) who also has **read** [permission](#) for the data source.

Security filters will not be applied to users with the privileges mentioned above. Source administrators can manage security filters for regular users but not for other source administrators.

For specific information about source permissions, see the following topics:

* [Grant Permissions for a Source](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932880234765-Grant-Permissions-for-a-Source)
* [Modify Permissions for a Data Source](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932892540045-Modify-Permissions-for-a-Data-Source)
* [Revoke Permissions for a Data Source](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915496589-Revoke-Permissions-for-a-Data-Source)
* [How Source Permissions Are Determined](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932923718157-How-Source-Permissions-Are-Determined)

Data source permissions can also be managed using the API endpoints `GET /api/sources/{sourceId}/acls`, `PATCH and PUT /api/sources/{sourceId}/acls/bulk`, `GET /api/user/permissions/sources/{sourceId}`, `GET /api/user/permissions/sources`, and `GET /api/inventory/SOURCE/{id}`.

When you use the `GET /api/sources/{sourceId}/acls` endpoint, you can read the source data. Use `PATCH` and `PUT` to restrict the list to specific users, groups, or tenants using the `sidTypes` parameter. In addition, you can use the `returnSids` parameter to restrict the list so it retrieves only users, groups, or tenants with access to the sources or to only users, groups, or tenants without access.

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

**Permissions for imported objects**

When you [import dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932814514061-Import-Dashboards), associated resources such as visuals, sources, and connections are imported as well. You can quickly grant default access levels to all imported and associated objects in your tenants by enabling **Share Default Access With All Users** at import time. Users are granted Data Access to Sources and Read access to Visuals and Dashboards.
