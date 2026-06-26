---
title: "Edit a Materialized View Definition"
id: 34933077573773
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933077573773-Edit-a-Materialized-View-Definition
updated_at: 2026-05-26T21:48:16Z
---

# Edit a Materialized View Definition

# Edit a Materialized View Definition

**Note:** 
Materialized view functionality is disabled by default. To enable, [contact technical support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) for assistance.
The [Materialized Views API](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932682254861-Materialized-Views-API-Experimental) is deprecated and will be removed in a future release.

**Important:** 
This is an experimental feature.

Edit a materialized view definition using the UI

1. Make sure you are logged in as a user with the **Administer Sources**  [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) or that you have [**read** and **write** permission for the data source](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions).
2. List the materialized views for the data source. See [List Materialized View Definitions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933057267725-List-Materialized-View-Definitions).

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167865748877)
3. Select the materialized view name in the list of materialized view definitions. The definition opens in a new dialog.
4. Modify any field in the definition. You can change the definition name, description and target settings. You can also add and remove metrics, groups, and filters from the definition. Remove metrics, group, and filter specifications by selecting ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167865750797) in the **Delete** column of the Metrics, Groups, and Filters tables.

   **Note:** 
   Materialized views only work if you specify the metrics and groups used by your visuals in the materialized view definition. For example, if you use Sales (SUM) as your metric and State as your group in a visual, be sure to add these metrics and groups to your materialized view definition. If they don't match, Composer will not use the materialized view to boost your visual rendering time.

   See [Add a Materialized View Definition](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933077179789-Add-a-Materialized-View-Definition) for explanations of each field in the definition.
5. Select **Save** to save the materialized view definition.
