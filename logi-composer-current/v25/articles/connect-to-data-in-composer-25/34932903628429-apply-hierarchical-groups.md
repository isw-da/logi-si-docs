---
title: "Apply Hierarchical Groups"
id: 34932903628429
section: "Connect to Data in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932903628429-Apply-Hierarchical-Groups
updated_at: 2026-05-26T22:09:49Z
---

# Apply Hierarchical Groups

# Apply Hierarchical Groups

**Note:** 
Hierarchical fields are enabled by default at the server level. Work with [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) to disable.

## Use a Hierarchical Group in a Pivot Table

1. Create a pivot table visual from your hierarchical data source.
2. Select the Settings sidebar menu, then select **Edit Row Groups** (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167939494797)).

   ![Select a hierarchy group](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167289025805 "Edit row groups work area")
3. Select a hierarchical field to use, then select **Continue** to define column groups and metrics for your visual.

   **Note:** 
   You can't use other fields in row groups if you have selected a hierarchical field. The hierarchical field will be the only row in the rows dimension.
4. Optionally, select **Edit Column Group** (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167939494797)) to add a field or fields to column groups.
5. Select metrics to use in your pivot table. Optionally, enable **Rollup** for the metrics, if supported. This shows the rolled up value of all child values at each hierarchy level.
6. Select **Apply** to apply your changes. You can now expand and collapse the hierarchical data you defined in your visual.

   **Note:** 
   Not all data in your sources may display in your visual due to rows per page settings. The default display of rows is 200, including the parents and root node. Adjust the **Rows per Page** in the Display Settings.
