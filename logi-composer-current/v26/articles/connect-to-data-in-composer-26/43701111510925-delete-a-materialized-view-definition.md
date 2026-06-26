---
title: "Delete a Materialized View Definition"
id: 43701111510925
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701111510925-Delete-a-Materialized-View-Definition
updated_at: 2026-05-29T14:10:38Z
---

# Delete a Materialized View Definition

# Delete a Materialized View Definition

**Note:** 
Materialized view functionality is disabled by default. To enable, [contact technical support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) for assistance.
The [Materialized Views API](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701023039373-Materialized-Views-API-Experimental) is deprecated and will be removed in a future release.

**Important:** 
This is an experimental feature.

Deleting a materialized view does not affect the underlying pre-aggregated data. When that data is not used any more, it should be deleted manually from you external storage by the data owner.

**Delete a materialized view definition using the UI**

1. Make sure you are logged in as a user with the **Administer Sources**  [privilege](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701005611789-Group-Privilege-Reference) or that you have [**read**, **write**, and permission for the data source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701101615373-About-Source-Permissions).
2. List the materialized views for the data source. See [List Materialized View Definitions](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701111671949-List-Materialized-View-Definitions).

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243196138381)
3. Locate the materialized view definition you want to delete and select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243196139533) in the Delete column for the definition.

   A warning dialog appears, prompting you to confirm the deletion.
4. Select **Delete** on the warning dialog.

   The definition is deleted.
