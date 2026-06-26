---
title: "How Source Permissions Are Determined"
id: 43701097731725
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701097731725-How-Source-Permissions-Are-Determined
updated_at: 2026-05-29T14:08:26Z
---

# How Source Permissions Are Determined

# How Source Permissions Are Determined

By default, the creator of a source configuration always has **Data Access**, **Read**, **Write**, and **Delete** permissions until those permissions are changed by an administrator or someone with appropriate authorization to change source permissions. If a user is removed from your software environment, sources created by that user are retained. The system admin becomes the creator of these orphaned data sources.

**Note:** 
The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.

Data Access is a separate permission for sources. It can be set directly on sources for users, groups, and accounts, and is enabled for users, groups, and accounts when you assign **Read** permission for a visual that uses that source. Unless they are granted Read permission to the source as well, they can't see the source listed on the Source page, or select the source to create a new visual (for users with the **Create Visuals** or **Administer Visuals**[privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference)).

If conflicting source permissions are specified for a tenant, the group within a tenant, and the user within a tenant, the permissions granted to the users are determined using a most permissive model. Users are granted the highest level of permission specified for the tenant, group, and user. For example, if the tenant is granted read and write permissions, but Group A is granted write and delete permissions, users in Group A will be able to read, write, and delete the source. However, users in any other groups in the tenant will only be able to read and write the data source.

Here's another example. If the tenant is granted data access, read, write, and delete permissions, but the groups in the tenant are only granted data access permissions, all users in the tenant will have data access, read, write, and delete permissions for the data source.

**Note:** 
If you try to delete a visual, filter snippet, dashboard, dashboard link, source, or source field, Composer displays an error message naming any objects dependent on the item you’re trying to delete. You can delete the item after you’ve removed the association from the dependent object.
See[Fields Usage](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701095792013-Fields-Usage).

**Permissions for imported objects**

When you [import dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093507213-Import-Dashboards), associated resources such as visuals, sources, and connections are imported as well. You can quickly grant default access levels to all imported and associated objects in your tenants by enabling **Share Default Access With All Users** at import time. Users are granted Data access to sources and Read access to visuals and dashboards.
