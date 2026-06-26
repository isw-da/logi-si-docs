---
title: "Setting an Attribute Filter"
id: 4402537796119
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537796119-Setting-an-Attribute-Filter
updated_at: 2021-09-15T02:21:36Z
---

# Setting an Attribute Filter

# Setting an Attribute Filter

You can filter visual data by the values in an attribute.

To set a filter for an attribute:

1. Select the filter icon on the [visual](https://devnet.logianalytics.com/hc/en-us/articles/4402537795351-Applying-a-Row-Level-Filter-to-a-Visual) or [dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4402552811415-Applying-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406753463191/filter-vis.png)) or select **Edit Visual** from the [visual menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406763902743/three-dots-menu_19x11.png)) and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753463447/sidebar-filter_20x21.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406763902999/filter-dash.png)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.
2. Select the Row tab. If the style of your visual is an arc gauge, KPI chart, raw data table, histogram, or map markers chart, the Group tab is available, but you cannot create a group filter because all filters for these visual styles are row-level filters. If you are using the dashboard filters sidebar, the Group tab is not available.

   The Saved tab shows saved filters that you can apply to a dashboard or visual. See [*Maintaining Saved Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4402552818327-Maintaining-Saved-Filters)
3. On the Row tab, select the filter attribute you want to use from the list of available attributes. A second page with three tabs appears in the Filters sidebar.

   You can also select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753440151/add.png) to access the [*Derived Field Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4402552791703-Derived-Field-Editor) or the [*Custom Metrics Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4402552783255-Custom-Metrics-Editor) to create or modify derived fields and custom metrics to be used as filters. See [*Accessing the Derived Field Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4402537770263-Accessing-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [*Accessing the Custom Metrics Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4402537758743-Accessing-the-Custom-Metrics-Editor-from-the-Filters-Sidebar).

   | Tab | Description |
   | --- | --- |
   | Value | The Value tab allows you to select:  * A filter operator (**Include** or **Exclude**, depending on whether you want to include or exclude the value from the data). * An optional custom value. To create and select a custom value, enter the value in the **Customize** field and select **Add**. Your custom field is added and selected in the list of possible values. To remove the custom value, uncheck it in the list of possible values. It is removed from the filter and from the list of possible values for the filter. * One or more values from the list of available values for the attribute you selected. To select all values, select **Select All**. Use the search bar to quickly find a value. You can type the name of the value in the Search bar (or characters in the value name) to limit the list of values. A maximum of 1000 values are listed. If no values are listed or if you cannot find your value, type the exact name of the value (as stored in your data) into the Search bar and select  to select it. This will force Composer to use this value when sending the query to the data store.  See [*Applying Row-Level Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4402537794711-Applying-Row-Level-Filters). |
   | Wildcard | The Wildcard tab allows you to specify a wild card filter for the attribute. See [*Applying Wild Card Filters to a Visual or Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4402537802519-Applying-Wild-Card-Filters-to-a-Visual-or-Dashboard). |
   | Keyset | The Keyset tab allows you to select a keyset filter for the attribute. See [*Using Keysets*](https://devnet.logianalytics.com/hc/en-us/articles/4402537825175-Using-Keysets) for instructions on using keysets in a filter. |
4. After the filter specifics have been specified, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753455127/apply1-btn_41x23.png). If you create the filter at the dashboard level, it is applied to all the visuals in the dashboard. Otherwise, it is applied only to the selected (active) visual.
