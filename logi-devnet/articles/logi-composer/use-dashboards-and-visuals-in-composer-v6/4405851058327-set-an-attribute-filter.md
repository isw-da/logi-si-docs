---
title: "Set an Attribute Filter"
id: 4405851058327
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851058327-Set-an-Attribute-Filter
updated_at: 2021-09-21T01:28:33Z
---

# Set an Attribute Filter

# Set an Attribute Filter

You can filter visual data by the values in an attribute.

To set a filter for an attribute:

1. Select the filter icon on the [visual](https://devnet.logianalytics.com/hc/en-us/articles/4405851057431-Apply-a-Row-Level-Filter-to-a-Visual) or [dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4405851056535-Apply-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406743754263/filter-vis.png)) or select **Edit Visual** from the [visual menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743718551/three-dots-menu_19x11.png)) and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743782935/sidebar-filter_20x21.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406743718807/filter-dash.png)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.
2. Select the Row tab. If the style of your visual is an arc gauge, KPI chart, table (raw data), histogram, or map markers chart, the Group tab is available, but you cannot create a group filter because all filters for these visual styles are row-level filters. If you are using the dashboard filters sidebar, the Group tab is not available.

   The Saved tab shows saved filters that you can apply to a dashboard or visual. See [*Maintain Saved Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4405851070359-Maintain-Saved-Filters).
3. On the Row tab, select the filter attribute you want to use from the list of available attributes. A second page with three tabs appears in the Filters sidebar.

   You can also select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743717271/add.png) to access the [*Derived Field Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4405851014551-Derived-Field-Editor) or the [*Custom Metrics Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4405859284119-Custom-Metrics-Editor) to create or modify derived fields and custom metrics to be used as filters. See [*Access the Derived Field Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4405859296663-Access-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [*Access the Custom Metrics Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4405851000727-Access-the-Custom-Metrics-Editor-from-the-Filters-Sidebar).

   | Tab | Description |
   | --- | --- |
   | Value | The Value tab allows you to select:  * A filter operator (**Include** or **Exclude**, depending on whether you want to include or exclude the value from the data). * An optional custom value. To create and select a custom value, enter the value in the **Customize** field and select **Add**. Your custom field is added and selected in the list of possible values. To remove the custom value, uncheck it in the list of possible values. It is removed from the filter and from the list of possible values for the filter. * One or more values from the list of available values for the attribute you selected. To select all values, select **Select All**. Use the search bar to quickly find a value. You can type the name of the value in the Search bar (or characters in the value name) to limit the list of values. A maximum of 1000 values are listed. If no values are listed or if you cannot find your value, type the exact name of the value (as stored in your data) into the Search bar and select  to select it. This will force Composer to use this value when sending the query to the data store.  See [*Apply Row-Level Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4405851055639-Apply-Row-Level-Filters). |
   | Wildcard | The Wildcard tab allows you to specify a wild card filter for the attribute. See [*Apply Wild Card Filters to a Visual or Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405851071383-Apply-Wild-Card-Filters-to-a-Visual-or-Dashboard). |
   | Keyset | The Keyset tab allows you to select a keyset filter for the attribute. See [*Use Keysets*](https://devnet.logianalytics.com/hc/en-us/articles/4405859392151-Use-Keysets) for instructions on using keysets in a filter. |
4. After the filter specifics have been specified, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743745559/apply1-btn_41x23.png). If you create the filter at the dashboard level, it is applied to all the visuals in the dashboard. Otherwise, it is applied only to the selected (active) visual.
