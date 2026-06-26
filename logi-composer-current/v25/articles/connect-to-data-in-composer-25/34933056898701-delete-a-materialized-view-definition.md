---
title: "Delete a Materialized View Definition"
id: 34933056898701
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933056898701-Delete-a-Materialized-View-Definition
updated_at: 2026-05-26T22:09:16Z
---

# Delete a Materialized View Definition

# Delete a Materialized View Definition

**Note:** 
Materialized view functionality is disabled by default. To enable, [contact technical support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) for assistance.
The [Materialized Views API](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932682254861-Materialized-Views-API-Experimental) is deprecated and will be removed in a future release.

**Important:** 
This is an experimental feature.

Deleting a materialized view does not affect the underlying pre-aggregated data. When that data is not used any more, it should be deleted manually from you external storage by the data owner.

**Delete a materialized view definition using the UI**

1. Make sure you are logged in as a user with the **Administer Sources**  [privilege](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932577846157-Group-Privilege-Reference) or that you have [**read**, **write**, and permission for the data source](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932915596173-About-Source-Permissions).
2. List the materialized views for the data source. See [List Materialized View Definitions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933057267725-List-Materialized-View-Definitions).

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167871954829)
3. Locate the materialized view definition you want to delete and select ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167882164621) in the Delete column for the definition.

   A warning dialog appears, prompting you to confirm the deletion.
4. Select **Delete** on the warning dialog.

   The definition is deleted.
