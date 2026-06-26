---
title: "How  Dashboard Permissions Are Determined"
id: 43701076359437
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701076359437-How-Dashboard-Permissions-Are-Determined
updated_at: 2026-05-29T14:08:05Z
---

# How  Dashboard Permissions Are Determined

# How Dashboard Permissions Are Determined

The creator of a dashboard always has permission to read, write, and delete the dashboard. If the user who created the dashboard is removed from the Composer environment, the dashboards they created are retained.

If conflicting dashboard permissions are specified for the tenant, the group within the tenant, and the user within the tenant, the permissions granted to the users in both are determined using a most permissive model. The users are granted the highest level of permission specified for the tenant, group, and user.

For example, if the tenant is granted read and write permissions, but **Group A** is granted write and delete permissions, users in **Group A** will be able to read, write, and delete the dashboard. However, users in any other groups in the tenant will only be able to read and write the dashboard.

Here's another example. If the tenant is granted read, write, and delete permissions, but the groups are only granted read permissions, all users in the tenant will have read, write, and delete permissions.

**How source permissions affect dashboard use**

Users must have access to the data sources used on the dashboard to see the data from the data sources.

For example, assume your tenant is granted read, write, and delete permissions for a dashboard. If Linda (a user in the tenant) does not have access to the data source used by the dashboard or if Linda is not assigned to any group at all, Linda will be able to see the dashboard in the library and will be able to open the dashboard, but no data will be shown.

Now suppose the dashboard uses three data sources on different visuals in the dashboard, but Linda only has access to two of the data sources. Linda will be able to see only the visuals that use data from the two data sources to which she has access.

**Permissions for imported objects**

When you [import dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093507213-Import-Dashboards), associated resources such as visuals, sources, and connections are imported as well. You can quickly grant default access levels to all imported and associated objects in your tenants by enabling **Share Default Access With All Users** at import time. Users are granted Data access to sources and Read access to visuals and dashboards.
