---
title: "How Data Source Permissions Are Determined"
id: 4405851030423
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851030423-How-Data-Source-Permissions-Are-Determined
updated_at: 2021-09-21T01:28:19Z
---

# How Data Source Permissions Are Determined

# How Data Source Permissions Are Determined

By default, the creator of a data source configuration always has permission to read, write, and delete the data source, until those permissions are changed by an administrator or someone with appropriate authorization to change source permissions. If the creating user is removed from the Composer environment, the data sources created by the user are retained and the [supplied Supervisor user](https://devnet.logianalytics.com/hc/en-us/articles/4405859125911-Supplied-User-Definitions) becomes the creator of these orphaned data sources.

If conflicting data sources permissions are specified for the account, the group within the account, and the user within the account, the permissions granted to the users are determined using a most permissive model. The users are granted the highest level of permission specified for the account, group, and user. For example, if the account is granted read and write permissions, but Group A is granted write and delete permissions, users in Group A will be able to read, write, and delete the data source. However, users in any other groups in the account will only be able to read and write the data source.

Here's another example. If the account is granted read, write, and delete permissions, but the groups are only granted read permissions, all users in the account will have read, write, and delete permissions for the data source.
