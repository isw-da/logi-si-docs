---
title: "Setting a Time Field Filter"
id: 4402552813847
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402552813847-Setting-a-Time-Field-Filter
updated_at: 2021-09-15T02:21:39Z
---

# Setting a Time Field Filter

# Setting a Time Field Filter

When you select a time attribute for a visual, you can filter the time range displayed on the visual.

To set a time range for a time field filter:

1. Select the filter icon on the [visual](https://devnet.logianalytics.com/hc/en-us/articles/4402537795351-Applying-a-Row-Level-Filter-to-a-Visual) or [dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4402552811415-Applying-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406753463191/filter-vis.png)) or select **Edit Visual** from the [visual menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406763902743/three-dots-menu_19x11.png)) and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753463447/sidebar-filter_20x21.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406763902999/filter-dash.png)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.
2. Select the Row tab. If the style of your visual is an arc gauge, KPI chart, raw data table, histogram, or map markers chart, the Group tab is available, but you cannot create a group filter because all filters for these visual styles are row-level filters. If you are using the dashboard filters sidebar, the Group tab is not available.

   The Saved tab shows saved filters that you can apply to a dashboard or visual. See [*Maintaining Saved Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4402552818327-Maintaining-Saved-Filters)
3. On the Row tab, select a time field you want to use from the list of available time fields. A second page with two tabs appears in the Filters sidebar: Range and Keyset.

   You can also select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753440151/add.png) to access the [*Derived Field Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4402552791703-Derived-Field-Editor) or the [*Custom Metrics Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4402552783255-Custom-Metrics-Editor) to create or modify derived fields and custom metrics to be used as filters. See [*Accessing the Derived Field Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4402537770263-Accessing-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [*Accessing the Custom Metrics Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4402537758743-Accessing-the-Custom-Metrics-Editor-from-the-Filters-Sidebar).
4. On the Range tab, use the **From** and **To** boxes to specify the time range for the filter. You can set the range in static time or dynamic time, or use preset ranges provided with Composer.

   * Select **Static Time** or **Dynamic Time** in the **fx** drop-down menu.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406763977111/time-bar-range-types1_250x150.png)

     If you select **Static Time**, the **From** and **To** boxes are filled with default dates and times. Use the boxes to select specific from and to times:

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406763977495/filter-time-range-static1_150x254.png)

     If you select **Dynamic Time**, the **From** and **To** boxes are filled with **Start of Data Set** and **End of Data Set** automatically. Use the **Condition** boxes to select different dynamic from and to times:

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406763978007/filter-time-range-dynamic1_139x260.png)
   * Alternatively, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763978263/presets-btn1_66x22.png) to fill the **From** and **To** boxes with predefined time ranges provided by Composer.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406753470359/time-bar-presets_122x216.png)

     Use the filter box at the top of the presets list to locate the preset setting you want. Descriptions of each of the preset options are provided in [*Preset Time Ranges*](https://devnet.logianalytics.com/hc/en-us/articles/4402552860055-Preset-Time-Ranges).
5. Alternatively, select a keyset on the **Keysets** tab to use for the filter. See [*Using Keysets*](https://devnet.logianalytics.com/hc/en-us/articles/4402537825175-Using-Keysets).
6. After the filter specifics have been specified, select **Apply**. If you create the filter at the dashboard level, it is applied to all the visuals in the dashboard. Otherwise, it is applied only to the selected (active) visual.
