---
title: "Apply a Row-Level Filter to a Dashboard"
id: 43701108132365
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701108132365-Apply-a-Row-Level-Filter-to-a-Dashboard
updated_at: 2026-05-29T14:10:53Z
---

# Apply a Row-Level Filter to a Dashboard

# Apply a Row-Level Filter to a Dashboard

When all the visuals in a dashboard use data from the same data source, you can apply row-level filters to the data on all the visuals in the dashboard. When more than one filter is applied to a visual (either via a dashboard filter or via the [specific visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701118671885-Apply-a-Row-Level-Filter-to-a-Visual-or-Filter-Snippet)), the filter conditions are ANDed. In other words, both filter conditions must be met for the data to appear in the visual.

**Apply a row-level filter to a dashboard**

1. Select the filter icon ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243232853133) on the dashboard (to the left of the dashboard title). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Dashboard Filters sidebar appears showing any dashboard filters that have been applied.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242534514189)

   Two tabs are available on the Dashboard Filters sidebar, allowing you to create a row-level filter or a saved filter. If these tabs do not appear, select **Add Filter** to see them.

   | Tab | Description |
   | --- | --- |
   | **Row** | The **Row** tab allows you to create a row-level filter, as described in the rest of this topic. |
   | **Saved** | The **Saved** tab shows saved filters that you can apply to the dashboard or visual. See [Maintain Saved Filters](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701104098061-Maintain-Saved-Filters). |
2. Select the Row tab and then select the filter attribute, number, or time field you want to use from the list. The process of creating a row-level filter varies based on the type of field you select.

   * If you select an attribute field, see [Set an Attribute Filter](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701133345293-Set-an-Attribute-Filter).
   * If you select a numeric field, see [Set a Numeric Field Filter](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701133427085-Set-a-Numeric-Field-Filter).
   * If you select a time field, see [Set a Time Field Filter](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701087681293-Set-a-Time-Field-Filter).

   You can also select the add icon ![add icon](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243247564301 "add icon") to access the [Derived Field Editor](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701095677581-Derived-Field-Editor) or the [Custom Metrics Editor](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701082580237-Custom-Metrics-Editor) to create or modify derived fields and custom metrics to be used as filters. See [Access the Derived Field Editor from the Filters Sidebar](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701066934285-Access-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [Access the Custom Metrics Editor from the Filters Sidebar](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701015326349-Access-the-Custom-Metrics-Editor-from-the-Filters-Sidebar).
3. After the filter specifics have been defined, select **Continue**. The filter is applied to all the visuals in the dashboard. Note that a number appears in a green circle next to the filter icon on the visuals to which the filter has been applied. The number represents the number of filters applied to the visual. After confirming your changes, select **Apply**.
