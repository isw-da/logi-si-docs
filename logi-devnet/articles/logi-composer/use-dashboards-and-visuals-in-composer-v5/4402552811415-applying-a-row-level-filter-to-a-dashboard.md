---
title: "Applying a Row-Level Filter to a Dashboard"
id: 4402552811415
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402552811415-Applying-a-Row-Level-Filter-to-a-Dashboard
updated_at: 2021-09-15T02:21:35Z
---

# Applying a Row-Level Filter to a Dashboard

# Applying a Row-Level Filter to a Dashboard

When all the visuals in a dashboard use data from the same data source, you can apply row-level filters to the data on all the visuals in the dashboard. When more than one filter is applied to a visual (either via a dashboard filter or via the [specific visual](https://devnet.logianalytics.com/hc/en-us/articles/4402537795351-Applying-a-Row-Level-Filter-to-a-Visual)), the filter conditions are ANDed. In other words, both filter conditions must be met for the data to appear in the visual.

To apply a row-level filter to a dashboard:

1. Select the filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406763902999/filter-dash.png)) on the dashboard (to the left of the dashboard title). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Dashboard Filters sidebar appears showing any dashboard filters that have been applied.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763982999/dashboard-filters_288x471.png)

   Two tabs are available on the Dashboard Filters sidebar, allowing you to create a row-level filter or a saved filter. If these tabs do not appear, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763958551/add-filter-btn.png) to see them.

   | Tab | Description |
   | --- | --- |
   | **Row** | The **Row** tab allows you to create a row-level filter, as described in the rest of this topic. |
   | **Saved** | The **Saved** tab shows saved filters that you can apply to the dashboard or visual. See [*Maintaining Saved Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4402552818327-Maintaining-Saved-Filters). |
2. Select the Row tab and then select the filter attribute, number, or time field you want to use from the list. The process of creating a row-level filter varies based on the type of field you select.

   * If you select an attribute field, see [*Setting an Attribute Filter*](https://devnet.logianalytics.com/hc/en-us/articles/4402537796119-Setting-an-Attribute-Filter).
   * If you select a numeric field, see [*Setting a Numeric Field Filter*](https://devnet.logianalytics.com/hc/en-us/articles/4402537797399-Setting-a-Numeric-Field-Filter).
   * If you select a time field, see [*Setting a Time Field Filter*](https://devnet.logianalytics.com/hc/en-us/articles/4402552813847-Setting-a-Time-Field-Filter).

   You can also select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753440151/add.png) to access the [*Derived Field Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4402552791703-Derived-Field-Editor) or the [*Custom Metrics Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4402552783255-Custom-Metrics-Editor) to create or modify derived fields and custom metrics to be used as filters. See [*Accessing the Derived Field Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4402537770263-Accessing-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [*Accessing the Custom Metrics Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4402537758743-Accessing-the-Custom-Metrics-Editor-from-the-Filters-Sidebar).
3. After the filter specifics have been provided, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753455127/apply1-btn_41x23.png). The filter is applied to all the visuals in the dashboard. Note that the dashboard filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406763983255/filter-dash-set_16x20.png)) appears as green when a dashboard filter is applied.
