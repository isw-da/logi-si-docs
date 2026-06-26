---
title: "Delete Custom Metrics"
id: 34932819677837
section: "Manipulate Data In The Composer 25 Data Store"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932819677837-Delete-Custom-Metrics
updated_at: 2026-05-26T22:10:07Z
---

# Delete Custom Metrics

# Delete Custom Metrics

You can delete custom metrics from a data source in the [Custom Metrics](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932906721933-Manage-Fields#Custom) tab on the Fields tab, or by deleting the source entirely.

**Important:** 
If you delete a source, your custom metric can't be used by associated visuals, materialized views, actions, or chart defaults.

**Note:** 
If you try to delete a visual, filter snippet, dashboard, dashboard link, source, or source field, Composer displays an error message naming any objects dependent on the item you’re trying to delete. You can delete the item after you’ve removed the association from the dependent object.
See[Fields Usage](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932867958541-Fields-Usage).

**Delete custom metrics from a data source while editing the data source configuration**

1. Edit the data source configuration in the UI. See [Edit a Data Source](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932890384781-Edit-a-Data-Source).
2. Select the **Fields** tab.
3. Select **Custom Metrics** to open the Custom Metrics tab.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167907543437)
4. Locate the custom metric in the Custom Metrics table that you would like to remove.
5. Select the delete icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167907544845)) in the Actions column.
6. Select **Delete** in the pop-up confirmation dialog. The custom metric is deleted if it is not in use.
