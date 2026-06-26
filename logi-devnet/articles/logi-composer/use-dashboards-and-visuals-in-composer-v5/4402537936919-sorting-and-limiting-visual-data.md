---
title: "Sorting and Limiting Visual Data"
id: 4402537936919
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537936919-Sorting-and-Limiting-Visual-Data
updated_at: 2021-09-15T02:23:07Z
---

# Sorting and Limiting Visual Data

# Sorting and Limiting Visual Data

You can sort the data within a visual by the available metrics or attributes for most visuals. You can also limit the amount of data that is displayed to show a more detailed view of your data.

Some of the options and settings vary based on the **Sort by** field that is selected. In addition, these settings may appear multiple times on the Sort & Limit sidebar if more than one sort field can be specified for a visual style.

Sorting and limiting data is not available for all visual styles. The visual styles for which you cannot sort and limit data are arcs, histograms, KPI charts, pivot tables, raw data tables, and maps. Pivot table and raw table data can be sorted, but not in the manner described here. See [*Pivot Tables*](https://devnet.logianalytics.com/hc/en-us/articles/4402537933719-Pivot-Tables) and [*Raw Data Tables (RDT)*](https://devnet.logianalytics.com/hc/en-us/articles/4402537935639-Raw-Data-Tables-RDT-). For information on how this functionality works in visuals that use two attribute group-bys, such as floating bubble charts and heat maps, see [*Sort & Limit Processing for Visuals With Two Attribute Group-By Fields*](https://devnet.logianalytics.com/hc/en-us/articles/4402537937687-Sort-Limit-Processing-for-Visuals-With-Two-Attribute-Group-By-Fields).

Administrators and users with editing rights to data source configurations can also set the default sort order and limits in data source configurations.
For additional information, see [*Manage Data Source Configurations*](https://devnet.logianalytics.com/hc/en-us/articles/4402552802199-Manage-Data-Source-Configurations).

To sort or limit your visual data on a dashboard:

1. Select the visual in the Visual Gallery or on a dashboard.
2. If you selected the visual on a dashboard, select **Edit Visual** on the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu) to access the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) for the visual.
3. Select the sort and limit option (![](https://devnet.logianalytics.com/hc/article_attachments/4406753438999/sidebar-sort.png)) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) for the visual. The Sort & Limit sidebar opens.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763908375/sidebar-sortlimit_192x356.png)
4. Select a field to sort by from the drop-down menu in the **Sort by** box. If more than one sort field is used for a visual style, more than one **Sort by** box appears on the sidebar.
5. For numeric **Sort by** fields, you can indicate how the data should be aggregated for the visual using the **Aggregation** box. Options include: SUM, AVG, MIN, MAX, or LAST VALUE. For explanations, see [*Available Metric Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4402537777687-Available-Metric-Functions).
6. Select a sorting option from the drop-down menu in the **Order** box (for example, **Descending** or **Ascending**). Different sorting options are available, depending on the **Sort by** field you select. If the selected **Sort by** field is a metric, you can sort the data in ascending or descending order. f the selected **Sort by** field is an attribute, you can sort the data in alphabetical or reverse-alphabetical order. For time attribute-based visuals, you can sort in chronological or reverse-chronological order.
7. To limit the amount of data displayed in the visual, enter or specify a number in the **Limit** box. This number is the number of data points shown on the visual. (For example, for bar charts, this represents the number of bars.) Valid values range from 1 to 999999999. If this setting is set too large, browser performance may be affected and the visual may not be able to render the data effectively.
8. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763908631/apply-btn_58x19.png) to apply your changes to the visual.
