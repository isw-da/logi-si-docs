---
title: "Group and Ungroup Table Data"
id: 43701183802381
section: "Use Dashboards, Reports  and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701183802381-Group-and-Ungroup-Table-Data
updated_at: 2026-08-31T04:13:55Z
---

# Group and Ungroup Table Data

# Group and Ungroup Table Data

You can group and ungroup table data by one or more fields while you are viewing the table. Summarized totals are provided for numeric fields in each group. The fields used for grouping are automatically moved to the leftmost columns of the table.

Grouping can be set on the table itself using the column heading context menus and using the Table Settings sidebar (a new Group area has been added). In addition, group default settings can be specified for tables in data source configurations.

In environments where [self service reports](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46982003580173-Manage-Self-Service-Reports) are enabled, the table visual is the primary visual used to generate a report. It supports up to 15 columns of exported data and up to 10 columns of grouped data.

**Note:** 
End users will only be able to group table data if the **Group** interactivity setting is enabled. See [Control How Users Interact With a Visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701185104653-Control-How-Users-Interact-With-a-Visual).

**Note:** 
Live mode and historical playback do not work for tables when the table is grouped.

**Note:** 
If a table has been grouped, you cannot [export](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701214516365-Export-Visuals) its raw or visual data.

This topic covers grouping and ungrouping data using the table context menu and settings sidebar menu.

## Group and Ungroup Table Data - Table Context Menu

If a field is selected for grouping, it is automatically selected for the table and cannot be specifically selected as a table column.

When you group table data, summarized totals are provided for numeric fields in each group. The fields used for grouping are automatically moved to the leftmost columns of the table.

### Group Table Data - Table Context Menu

1. View the table visual in a dashboard, in the Visual Gallery, or in a report. Determine which field you want to use to group the data. For example, you might want to group sales data by state.
2. Locate the field in the table and select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48528037201549) next to its column heading to access the table context menu.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48527827520525)
3. Select **Group by <field>** on the context menu.

   The table is grouped by that field.
4. Optionally, select an aggregation level for the group field from the **Aggregation** list. The **Aggregation** list is only available for fields that have aggregation enabled in the data source and if the group field is not the first group field for the table. Optionally, select relevant show/hide options for individual metric labels using the table context menu in the column header.
5. You might want to group the table data by more than one field. For example you might want the sales data that has already been grouped by state to also be grouped by city.

   If you want to group by an additional field, locate the field in the table and select **Group by <field>** on its context menu.

   The table is grouped by that field within the grouping of any previously selected groups.
6. Save the dashboard, visual, or report.

### Ungroup Table Data - Table Context Menu

1. View the table visual in a dashboard, in the Visual Gallery, or in a report. Determine which field you want to remove from grouping.
2. Locate the field in the table and select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48528037201549) next to its column heading to access the table context menu.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48527827566221)
3. Select **Ungroup by <field>** on the context menu.

   The table is ungrouped by that field.
4. Save the dashboard, visual, or report.

# Group and Ungroup Table Data - Table Settings Sidebar

If a field is selected for grouping, it is automatically selected for the table and cannot be specifically selected as a table column.

When you group table data, summarized totals are provided for numeric fields in each group. The fields used for grouping are automatically moved to the leftmost columns of the table.

### Group Table Data - Table Settings sidebar

1. If you are editing the visual in a dashboard or report, select **Settings** from the [visual drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Drop-Down-Menu). The [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) for the table appears.

   If you are editing the table from the Visual Gallery or in a report, the sidebar appears to the right of the table.
2. Select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48528037201677) on the [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu). The Table Settings sidebar for the table appears.
3. Select and drag the field by which you want the table grouped from the **Columns** section of the Table Settings sidebar to the **Groups** section.

   The **Groups** section of the Table Settings sidebar lists the columns by which the table is grouped, in order of that grouping. In the following example, the sales data is grouped first by state, then by city within the state, and then by product category.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48527827605133)
4. Optionally, select an aggregation level for the group field from the **Aggregation** list. The **Aggregation** list is only available for fields that have aggregation enabled in the data source and only if the group field is not the first group field for the table.
5. Select **Apply** to apply your changes to the table. The grouping selections are applied to the table.
6. Save the dashboard, visual, or report.

### Ungroup Table Data - Table Settings sidebar

1. If you are editing the visual in a dashboard or report, select **Settings** from the [visual drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Drop-Down-Menu). The [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) for the table appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
2. Select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48528037201677) on the [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu). The Table Settings sidebar for the visual appears.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48527827605133)
3. You can remove a field from grouping in several ways:

   1. Select and drag the field from the **Groups** section of the Table Settings sidebar to the **Columns** section.
   2. In the **Groups** section of the sidebar, select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48528013041165) corresponding to the field you want removed from grouping.
   3. Select the edit icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/48527837157261)) for **Edit Groups** on the sidebar menu. The Table Settings sidebar changes and only the fields included are listed. Clear the checkbox of the field you want to remove from grouping. Note that this also removes the field from the table and you must manually add it back if you want its column shown in the table. Select **Continue** when you have completed your changes.
4. Select **Apply** to apply your changes to the table.
5. Save the dashboard, visual, or report.
