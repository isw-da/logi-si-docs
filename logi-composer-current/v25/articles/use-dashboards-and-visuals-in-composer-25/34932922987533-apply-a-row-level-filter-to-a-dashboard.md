---
title: "Apply a Row-Level Filter to a Dashboard"
id: 34932922987533
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932922987533-Apply-a-Row-Level-Filter-to-a-Dashboard
updated_at: 2026-05-26T22:09:30Z
---

# Apply a Row-Level Filter to a Dashboard

# Apply a Row-Level Filter to a Dashboard

When all the visuals in a dashboard use data from the same data source, you can apply row-level filters to the data on all the visuals in the dashboard. When more than one filter is applied to a visual (either via a dashboard filter or via the [specific visual](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932931145741-Apply-a-Row-Level-Filter-to-a-Visual-or-Filter-Snippet)), the filter conditions are ANDed. In other words, both filter conditions must be met for the data to appear in the visual.

**Apply a row-level filter to a dashboard**

1. Select the filter icon ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167891734285) on the dashboard (to the left of the dashboard title). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Dashboard Filters sidebar appears showing any dashboard filters that have been applied.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167215350285)

   Two tabs are available on the Dashboard Filters sidebar, allowing you to create a row-level filter or a saved filter. If these tabs do not appear, select **Add Filter** to see them.

   | Tab | Description |
   | --- | --- |
   | **Row** | The **Row** tab allows you to create a row-level filter, as described in the rest of this topic. |
   | **Saved** | The **Saved** tab shows saved filters that you can apply to the dashboard or visual. See [Maintain Saved Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932976956941-Maintain-Saved-Filters). |
2. Select the Row tab and then select the filter attribute, number, or time field you want to use from the list. The process of creating a row-level filter varies based on the type of field you select.

   * If you select an attribute field, see [Set an Attribute Filter](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932939064717-Set-an-Attribute-Filter).
   * If you select a numeric field, see [Set a Numeric Field Filter](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932957895565-Set-a-Numeric-Field-Filter).
   * If you select a time field, see [Set a Time Field Filter](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932958685197-Set-a-Time-Field-Filter).

   You can also select the add icon ![add icon](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167903098765 "add icon") to access the [Derived Field Editor](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932882620813-Derived-Field-Editor) or the [Custom Metrics Editor](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932820475405-Custom-Metrics-Editor) to create or modify derived fields and custom metrics to be used as filters. See [Access the Derived Field Editor from the Filters Sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932881853581-Access-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [Access the Custom Metrics Editor from the Filters Sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932813600525-Access-the-Custom-Metrics-Editor-from-the-Filters-Sidebar).
3. After the filter specifics have been defined, select **Continue**. The filter is applied to all the visuals in the dashboard. Note that a number appears in a green circle next to the filter icon on the visuals to which the filter has been applied. The number represents the number of filters applied to the visual. After confirming your changes, select **Apply**.
