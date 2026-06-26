---
title: "Apply a Row-Level Filter to a Dashboard"
id: 4405851056535
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851056535-Apply-a-Row-Level-Filter-to-a-Dashboard
updated_at: 2021-09-21T01:28:33Z
---

# Apply a Row-Level Filter to a Dashboard

# Apply a Row-Level Filter to a Dashboard

When all the visuals in a dashboard use data from the same data source, you can apply row-level filters to the data on all the visuals in the dashboard. When more than one filter is applied to a visual (either via a dashboard filter or via the [specific visual](https://devnet.logianalytics.com/hc/en-us/articles/4405851057431-Apply-a-Row-Level-Filter-to-a-Visual)), the filter conditions are ANDed. In other words, both filter conditions must be met for the data to appear in the visual.

To apply a row-level filter to a dashboard:

1. Select the filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406743718807/filter-dash.png)) on the dashboard (to the left of the dashboard title). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Dashboard Filters sidebar appears showing any dashboard filters that have been applied.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747418519/dashboard-filters_288x471.png)

   Two tabs are available on the Dashboard Filters sidebar, allowing you to create a row-level filter or a saved filter. If these tabs do not appear, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743802391/add-filter-btn.png) to see them.

   | Tab | Description |
   | --- | --- |
   | **Row** | The **Row** tab allows you to create a row-level filter, as described in the rest of this topic. |
   | **Saved** | The **Saved** tab shows saved filters that you can apply to the dashboard or visual. See [*Maintain Saved Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4405851070359-Maintain-Saved-Filters). |
2. Select the Row tab and then select the filter attribute, number, or time field you want to use from the list. The process of creating a row-level filter varies based on the type of field you select.

   * If you select an attribute field, see [*Set an Attribute Filter*](https://devnet.logianalytics.com/hc/en-us/articles/4405851058327-Set-an-Attribute-Filter).
   * If you select a numeric field, see [*Set a Numeric Field Filter*](https://devnet.logianalytics.com/hc/en-us/articles/4405851060119-Set-a-Numeric-Field-Filter).
   * If you select a time field, see [*Set a Time Field Filter*](https://devnet.logianalytics.com/hc/en-us/articles/4405851063831-Set-a-Time-Field-Filter).

   You can also select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743717271/add.png) to access the [*Derived Field Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4405851014551-Derived-Field-Editor) or the [*Custom Metrics Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4405859284119-Custom-Metrics-Editor) to create or modify derived fields and custom metrics to be used as filters. See [*Access the Derived Field Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4405859296663-Access-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [*Access the Custom Metrics Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4405851000727-Access-the-Custom-Metrics-Editor-from-the-Filters-Sidebar).
3. After the filter specifics have been provided, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743745559/apply1-btn_41x23.png). The filter is applied to all the visuals in the dashboard. Note that a number appears in a green circle next to the filter icon on the visuals to which the filter has been applied. The number represents the number of filters applied to the visual.
