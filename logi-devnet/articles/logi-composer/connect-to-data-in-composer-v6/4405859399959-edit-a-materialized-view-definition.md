---
title: "Edit a Materialized View Definition"
id: 4405859399959
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859399959-Edit-a-Materialized-View-Definition
updated_at: 2021-09-21T01:29:04Z
---

# Edit a Materialized View Definition

# Edit a Materialized View Definition

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) This is an experimental feature.

To edit a materialized view definition using the UI:

1. Make sure you are logged in as a Composer administrator or a user with the **Can Administer Sources** or the **Can Create new Data Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) and that you have [write permission for the data source](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions).
2. List the materialized views for the data source. See [*List Materialized View Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851113751-List-Materialized-View-Definitions).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743777815/mat-view-list_576x447.png)
3. Select the materialized view name in the list of materialized view definitions. The definition opens in a new dialog.
4. Modify any field in the definition. You can change the definition name, description and target settings. You can also add and remove metrics, groups, and filters from the definition. Remove metrics, group, and filter specifications by selecting ![](https://devnet.logianalytics.com/hc/article_attachments/4406743726743/delete-open.png) in the **Delete** column of the Metrics, Groups, and Filters tables.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Materialized views only work if you specify the metrics and groups used by your visuals in the materialized view definition. For example, if you use Sales (SUM) as your metric and State as your group in a visual, be sure to add these metrics and groups to your materialized view definition. If they don't match, Composer will not use the materialized view to boost your visual rendering time.

   See [*Add a Materialized View Definition*](https://devnet.logianalytics.com/hc/en-us/articles/4405859398807-Add-a-Materialized-View-Definition) for explanations of each field in the definition.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747400087/save-blue-btn.png) to save the materialized view definition.
