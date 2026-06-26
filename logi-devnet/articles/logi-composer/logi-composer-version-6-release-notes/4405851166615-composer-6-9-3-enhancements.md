---
title: "Composer 6.9.3 Enhancements"
id: 4405851166615
section: "Logi Composer Version 6 Release Notes"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851166615-Composer-6-9-3-Enhancements
updated_at: 2022-04-25T15:19:14Z
---

# Composer 6.9.3 Enhancements

# Composer 6.9.3 Enhancements

This topic describes the significant enhancements in Composer 6.9.3.

* [*Dashboard Import Overwrite Permission Updates*](#DashImport)

## Dashboard Import Overwrite Permission Updates

The overwrite policy behavior for imported dashboards now honors the write permissions for all the dashboard components: the dashboard itself, its visuals, and the data sources used by its visuals. To update an existing dashboard, the user attempting the import must now have write permission for all of these components. Otherwise, the update will fail.

For more information about requesting the dashboard import overwrite policy and its behavior, see [*Overwrite Policy Behavior*](https://devnet.logianalytics.com/hc/en-us/articles/4405850983831-Import-a-Dashboard#overwrite). For information about component permissions, see [*About Dashboard Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859259159-About-Dashboard-Permissions), [*About Visual Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851253271-About-Visual-Permissions), and [*About Data Source Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions).
