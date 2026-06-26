---
title: "How Visual Permissions Are Determined"
id: 43701184610701
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184610701-How-Visual-Permissions-Are-Determined
updated_at: 2026-05-29T14:09:50Z
---

# How Visual Permissions Are Determined

# How Visual Permissions Are Determined

The creator of a visual always has permission to read, write, and delete the visual. If the creating user is removed from the Composer environment, the visuals created by the user are retained and the [supplied `supervisor` user](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups) becomes the creator of these orphaned visuals.

If conflicting visual permissions are specified for the account, the group within the account, and the user within the account, the permissions granted to the users in both are determined using a most permissive model. The users are granted the highest level of permission specified for the account, group, and user. For example, if the account is granted read and write permissions, but Group A is granted write and delete permissions, users in Group A will be able to read, write, and delete the visual. However, users in any other groups in the account will only be able to read and write the visual.

Here's another example. If the account is granted read, write, and delete permissions, but the groups are only granted read permissions, all users in the account will have read, write, and delete permissions.

## How Data Source Permissions Affect Visual Use

Users must have access to the data sources used for the visual to see the data from the data sources.

For example, assume your account is granted read, write, and delete permissions for a visual. If Chris (a user in the account) does not have access to the data source used by the visual or if Chris is not assigned to any group at all, Chris will be able to see the visual in the Visual Gallery and will be able to open the visual, but no data will be shown.

**Permissions for imported objects**

When you [import dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093507213-Import-Dashboards), associated resources such as visuals, sources, and connections are imported as well. You can quickly grant default access levels to all imported and associated objects in your tenants by enabling **Share Default Access With All Users** at import time. Users are granted Data access to sources and Read access to visuals and dashboards.
