---
title: "Setting a Numeric Field Filter"
id: 4402537797399
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537797399-Setting-a-Numeric-Field-Filter
updated_at: 2021-09-15T02:21:37Z
---

# Setting a Numeric Field Filter

# Setting a Numeric Field Filter

You can filter visual data by the values in a numeric field.

To set a filter for a numeric field:

1. Select the filter icon on the [visual](https://devnet.logianalytics.com/hc/en-us/articles/4402537795351-Applying-a-Row-Level-Filter-to-a-Visual) or [dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4402552811415-Applying-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406753463191/filter-vis.png)) or select **Edit Visual** from the [visual menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406763902743/three-dots-menu_19x11.png)) and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753463447/sidebar-filter_20x21.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406763902999/filter-dash.png)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.
2. Select the Row tab. If the style of your visual is an arc gauge, KPI chart, raw data table, histogram, or map markers chart, the Group tab is available, but you cannot create a group filter because all filters for these visual styles are row-level filters. If you are using the dashboard filters sidebar, the Group tab is not available.

   The Saved tab shows saved filters that you can apply to a dashboard or visual. See [*Maintaining Saved Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4402552818327-Maintaining-Saved-Filters).
3. On the Row tab, select a numeric field you want to use from the list of available number fields. A second page with two tabs appears in the Filters sidebar: Range and Keyset.

   You can also select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753440151/add.png) to access the [*Derived Field Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4402552791703-Derived-Field-Editor) or the [*Custom Metrics Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4402552783255-Custom-Metrics-Editor) to create or modify derived fields and custom metrics to be used as filters. See [*Accessing the Derived Field Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4402537770263-Accessing-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [*Accessing the Custom Metrics Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4402537758743-Accessing-the-Custom-Metrics-Editor-from-the-Filters-Sidebar).

   | Tab | Description |
   | --- | --- |
   | Range | Select a relational comparison operator in the **Operator** selection box. Data is included in the visual when the data in the filter field meets the condition set by the relational operator and the numeric values you specify. Valid numeric operators are described in [*Operators*](https://devnet.logianalytics.com/hc/en-us/articles/4402552859159-Operators).  The Range tab initially shows the full range of values available. It provides an **Operator** selection box and **From** and **To** boxes for you to use to select the range of values. Use the arrows in the **From** and **To** boxes to increase and decrease the maximum and minimum values. |
   | Keyset | The Keyset tab allows you to select a keyset to apply as the filter (see [*Using Keysets*](https://devnet.logianalytics.com/hc/en-us/articles/4402537825175-Using-Keysets)). |
4. After the filter specifics have been specified, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753455127/apply1-btn_41x23.png). If you create the filter at the dashboard level, it is applied to all the visuals in the dashboard. Otherwise, it is applied only to the selected (active) visual.
