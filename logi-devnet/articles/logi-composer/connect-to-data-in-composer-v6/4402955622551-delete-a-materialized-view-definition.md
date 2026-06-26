---
title: "Delete a Materialized View Definition"
id: 4402955622551
section: "Connect to Data in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955622551-Delete-a-Materialized-View-Definition
updated_at: 2021-08-07T17:31:29Z
---

# Delete a Materialized View Definition

# Delete a Materialized View Definition

![](https://devnet.logianalytics.com/hc/article_attachments/4404952805911/criticalicon.gif) This is an experimental feature.

Deleting a materialized view does not affect the underlying pre-aggregated data. When that data is not used any more, it should be deleted manually from you external storage by the data owner.

To delete a materialized view definition using the UI:

1. Make sure you are logged in as a Composer administrator or a user with the **Can Administer Sources** or the **Can Create new Data Sources**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4402955416087-Group-Privilege-Reference) and that you have [write permission for the data source](https://devnet.logianalytics.com/hc/en-us/articles/4402955557783-About-Data-Source-Permissions).
2. List the materialized views for the data source. See [*List Materialized View Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4402955623831-List-Materialized-View-Definitions).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404952829463/mat-view-list_576x447.png)
3. Locate the materialized view definition you want to delete and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952790039/trashcan.png) in the Delete column for the definition.

   A warning dialog appears, prompting you to confirm the deletion.
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952830871/delete-btn.png) on the warning dialog.

   The definition is deleted.
