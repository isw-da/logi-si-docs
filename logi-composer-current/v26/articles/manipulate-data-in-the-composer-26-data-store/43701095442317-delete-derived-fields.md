---
title: "Delete Derived Fields"
id: 43701095442317
section: "Manipulate Data In The Composer 26 Data Store"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701095442317-Delete-Derived-Fields
updated_at: 2026-05-29T14:11:08Z
---

# Delete Derived Fields

# Delete Derived Fields

You can delete derived fields from a data source on the [Fields tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields), or by deleting the source entirely.

**Important:** 
If you delete a source, your derived field can't be used by associated visuals, materialized views, actions, or chart defaults.

**Note:** 
If you try to delete a visual, filter snippet, dashboard, dashboard link, source, or source field, Composer displays an error message naming any objects dependent on the item you’re trying to delete. You can delete the item after you’ve removed the association from the dependent object.
See[Fields Usage](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701095792013-Fields-Usage).

**Delete derived fields from a data source while editing the data source configuration**

1. Edit the data source configuration in the UI. See [Edit a Data Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116405261-Edit-a-Data-Source).
2. Select the **Fields** tab.
3. Locate the derived field in the Fields table that you would like to remove.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242634496653)
4. Select the delete icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242634591885)) in the Actions column.
5. Select **Delete** in the pop-up confirmation dialog. The derived field is deleted if it is not in use.
