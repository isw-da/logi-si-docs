---
title: "How Dashboard Permissions Are Determined"
id: 4402955507991
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955507991-How-Dashboard-Permissions-Are-Determined
updated_at: 2021-08-07T17:32:55Z
---

# How Dashboard Permissions Are Determined

# How Dashboard Permissions Are Determined

The creator of a dashboard always has permission to read, write, and delete the dashboard. If the creating user is removed from the Composer environment, the dashboards created by the user are retained and the [supplied `supervisor` user](https://devnet.logianalytics.com/hc/en-us/articles/4402955423255-Supplied-User-Definitions) becomes the creator of these orphaned dashboards.

If conflicting dashboard permissions are specified for the account, the group within the account, and the user within the account, the permissions granted to the users in both are determined using a most permissive model. The users are granted the highest level of permission specified for the account, group, and user. For example, if the account is granted read and write permissions, but Group A is granted write and delete permissions, users in Group A will be able to read, write, and delete the dashboard. However, users in any other groups in the account will only be able to read and write the dashboard.

Here's another example. If the account is granted read, write, and delete permissions, but the groups are only granted read permissions, all users in the account will have read, write, and delete permissions.

#### How Data Source Permissions Affect Dashboard Use

Users must have access to the data sources used on the dashboard to see the data from the data sources.

For example, assume your account is granted read, write, and delete permissions for a dashboard. If Chris (a user in the account) does not have access to the data source used by the dashboard or if Chris is not assigned to any group at all, Chris will be able to see the dashboard in the dashboard library and will be able to open the dashboard, but no data will be shown.

Now suppose the dashboard uses three data sources on different visuals in the dashboard, but Chris only has access to two of the data sources. Chris will be able to see only the visuals that use data from the two data sources to which he has access.
