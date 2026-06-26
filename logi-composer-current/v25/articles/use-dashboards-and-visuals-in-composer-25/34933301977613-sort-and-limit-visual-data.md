---
title: "Sort and Limit Visual Data"
id: 34933301977613
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933301977613-Sort-and-Limit-Visual-Data
updated_at: 2026-05-26T22:08:48Z
---

# Sort and Limit Visual Data

# Sort and Limit Visual Data

You can sort the data within a visual by the available metrics or attributes for most visuals. You can also limit the amount of data that is displayed to show a more detailed view of your data.

Some of the options and settings vary based on the **Sort by** field that is selected. In addition, these settings may appear multiple times on the Sort & Limit sidebar if more than one sort field can be specified for a visual style.

Sorting and limiting data is not available for all visual styles. The visual styles for which you cannot sort and limit data are arcs, histograms, KPI charts, pivot tables, tables of raw data, and maps. Pivot table and raw table data can be sorted, but not in the manner described here. See [Pivot Tables](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933216706189-Pivot-Tables) and [Tables](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933270449037-Tables). For information on how this functionality works in visuals that use two attribute group-bys, such as floating bubble charts and heat maps, see [Sort & Limit Processing for Visuals With Two Attribute Group-By Fields](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933272043277-Sort-Limit-Processing-for-Visuals-With-Two-Attribute-Group-By-Fields).

Administrators and users with editing rights to data source configurations can also set the default sort order and limits in data source configurations.
For additional information, see [Manage Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932941009037-Manage-Data-Sources).

**Sort or limit your visual data on a dashboard**

1. Select the visual in the Visual Gallery or on a dashboard.
2. If you selected the visual on a dashboard, select **Settings** on the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu) to access the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) for the visual.
3. Select the sort and limit option (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167828843661)) on the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) for the visual. The Sort & Limit sidebar opens.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46166920980877)
4. Select a field to sort by from the drop-down menu in the **Sort by** box. If more than one sort field is used for a visual style, more than one **Sort by** box appears on the sidebar.
5. For numeric **Sort by** fields:

   * Indicate how the data should be aggregated for the visual by selecting an **Aggregation** option. These include: SUM, AVG, MIN, MAX, or LAST VALUE, Count, and Distinct Count. For explanations, see [Metric Aggregation Functions](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932872742029-Metric-Aggregation-Functions).
   * The option **No Aggregation** is available if you group and sort by the same field. When you use No Aggregation, you can select the sort Order of as Alphabetical (A-Z) or Reverse Alphabetical (Z-A).
6. For attribute **Sort by** fields:

   * If you're sorting by the same attribute field used in groups, you can select an **Aggregation** option of No Aggregation, Count, or Distinct Count.
   * If you are sorting by a field not used in groups, you can select an **Aggregation** option of Count, or Distinct Count.
7. Select a sorting option from the drop-down menu in the **Order** box (for example, **Descending** or **Ascending**). Different sorting options are available, depending on the **Sort by** field you select. If the selected **Sort by** field is a metric, you can sort the data in ascending or descending order. If the selected **Sort by** field is an attribute, you can sort the data in alphabetical or reverse-alphabetical order. For time attribute-based visuals, you can sort in chronological or reverse-chronological order.
8. To limit the amount of data displayed in the visual, enter or specify a number in the **Limit** box. This number is the number of data points shown on the visual. (For example, for bar charts, this represents the number of bars.) Valid values range from 1 to 999999999. If this setting is set too large, browser performance may be affected and the visual may not be able to render the data effectively.
9. Select **Apply** to apply your changes to the visual.
