---
title: "Apply Hierarchical Groups"
id: 43701032076813
section: "Connect to Data in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701032076813-Apply-Hierarchical-Groups
updated_at: 2026-05-29T14:11:05Z
---

# Apply Hierarchical Groups

# Apply Hierarchical Groups

**Note:** 
Hierarchical fields are enabled by default at the server level. Work with [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) to disable.

## Use a Hierarchical Group in a Pivot Table

1. Create a pivot table visual from your hierarchical data source.
2. Select the Settings sidebar menu, then select **Edit Row Groups** (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243264805517)).

   ![Select a hierarchy group](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242649165581 "Edit row groups work area")
3. Select a hierarchical field to use, then select **Continue** to define column groups and metrics for your visual.

   **Note:** 
   You can't use other fields in row groups if you have selected a hierarchical field. The hierarchical field will be the only row in the rows dimension.
4. Optionally, select **Edit Column Group** (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243264805517)) to add a field or fields to column groups.
5. Select metrics to use in your pivot table. Optionally, enable **Rollup** for the metrics, if supported. This shows the rolled up value of all child values at each hierarchy level.
6. Select **Apply** to apply your changes. You can now expand and collapse the hierarchical data you defined in your visual.

   **Note:** 
   Not all data in your sources may display in your visual due to rows per page settings. The default display of rows is 200, including the parents and root node. Adjust the **Rows per Page** in the Display Settings.
