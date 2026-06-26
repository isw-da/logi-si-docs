---
title: "Applying Wild Card Filters to a Visual or Dashboard"
id: 4402537802519
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537802519-Applying-Wild-Card-Filters-to-a-Visual-or-Dashboard
updated_at: 2021-09-15T02:21:42Z
---

# Applying Wild Card Filters to a Visual or Dashboard

# Applying Wild Card Filters to a Visual or Dashboard

Wild card filters are row-level filters you can use to filter the data on your dashboard visuals. Wild card filters allow you to filter and analyze the data in a visual that matches specific combinations of character patterns.

![](https://devnet.logianalytics.com/hc/article_attachments/4406753437463/noteicon.jpg) When working with multiple filter types on the same visual, row-level filters (including wild card filters) are applied first to a visual, keyset filters are applied second, and group filters are applied last on the aggregated result set.

To apply a wild card filter to a visual or dashboard:

1. Select the filter icon on the [visual](https://devnet.logianalytics.com/hc/en-us/articles/4402537795351-Applying-a-Row-Level-Filter-to-a-Visual) or [dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4402552811415-Applying-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406753463191/filter-vis.png)) or select **Edit Visual** from the [visual menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406763902743/three-dots-menu_19x11.png)) and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753463447/sidebar-filter_20x21.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406763902999/filter-dash.png)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.
2. Select the Row tab. If the style of your visual is an arc gauge, KPI chart, raw data table, histogram, or map markers chart, the Group tab is available, but you cannot create a group filter because all filters for these visual styles are row-level filters. If you are using the dashboard filters sidebar, the Group tab is not available.

   The Saved tab shows saved filters that you can apply to a dashboard or visual. See [*Maintaining Saved Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4402552818327-Maintaining-Saved-Filters).
3. On the Row tab, select the filter attribute you want to use from the list of available attributes. A second page with three tabs appears in the Filters sidebar.

   * The Value tab allows you to select a filter value for the attribute. See [*Applying Row-Level Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4402537794711-Applying-Row-Level-Filters) for instructions on using a regular row-level filter.
   * The Wildcard tab allows you to specify a wild card filter for the attribute. Continue following the steps in these instructions.
   * The Keyset tab allows you to select a keyset filter for the attribute. See [*Using Keysets*](https://devnet.logianalytics.com/hc/en-us/articles/4402537825175-Using-Keysets) for instructions on using keysets in a filter.

   You can also select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753440151/add.png) to access the [*Derived Field Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4402552791703-Derived-Field-Editor) or the [*Custom Metrics Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4402552783255-Custom-Metrics-Editor) to create or modify derived fields and custom metrics to be used as filters. See [*Accessing the Derived Field Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4402537770263-Accessing-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [*Accessing the Custom Metrics Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4402537758743-Accessing-the-Custom-Metrics-Editor-from-the-Filters-Sidebar).
4. Select the Wildcard tab to create a row-level wild card filter.
5. Select an operator from the drop-down menu for the **Operator** box on the **Wildcard** tab.

   | Operator | Data is included in the visual... |
   | --- | --- |
   | Contains | When the data in the filter attribute you selected contains the wild card string you will specify in the next step. |
   | Does Not Contain | When the data in the filter attribute you selected does *not* contain the wild card string you will specify in the next step. |
   | Begins With | When the data in the filter attribute you selected begins with the wild card string you will specify in the next step. |
   | Does Not Begin With | When the data in the filter attribute you selected does **not** begin with the wild card string you will specify in the next step. |
   | Ends With | When the data in the filter attribute you selected ends with the wild card string you will specify in the next step. |
   | Does Not End With | When the data in the filter attribute you selected does **not** end with the wild card string you will specify in the next step. |
6. In the **Value** box, type a string of characters that represents the wild card string for the filter. Data is included in the visual when the data in the filter field meets the condition set by this operator and the wild card string you specify.
7. By default the **Case Sensitive** slider is on (selected). When this option is selected, the wild card filter includes data in the visual only if the filter attribute data exactly matches both the value of the wild card string and the case of the wild card string value. Slide the option off if you do not care if the visual data exactly matches the case of the wild card string.
8. If you want to specify another wild card value, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753440151/add.png) next to the **Values** title on the Wildcard tab. Then repeat Steps 5-7 above for the new wild card value. Multiple wild card values are treated as OR operations. A record can meet the filter criteria specified by any of the wildcard values to be selected for filter processing.
9. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763975191/apply1-btn_48x27.png). If you create the filter at the dashboard level, it is applied to all the visuals in the dashboard. Otherwise, it is applied only to the selected (active) visual.
10. Optionally, repeat these steps to apply additional filters to the visual or dashboard.

See [*Removing a Filter from a Visual or Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402537798039-Removing-a-Filter-from-a-Visual-or-Dashboard) for information on removing a wild card filter from a visual or dashboard.
