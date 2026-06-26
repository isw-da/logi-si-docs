---
title: "Apply a Group Filter from a Custom Metric"
id: 43701119033101
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119033101-Apply-a-Group-Filter-from-a-Custom-Metric
updated_at: 2026-05-29T14:10:49Z
---

# Apply a Group Filter from a Custom Metric

# Apply a Group Filter from a Custom Metric

Suppose you want to find product purchases made by males within certain areas of Los Angeles, while also comparing their income levels. Specifically, you are interested in men whose sales average more than $100,000. You might create a filter using the following steps. This example requires that you have already applied a row-level filter for the city of Los Angeles.

Since you do not have a custom metric created yet for average sales, one needs to be created.

**Create the custom metric**

1. Select the filter icon on the [visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701118671885-Apply-a-Row-Level-Filter-to-a-Visual-or-Filter-Snippet), [filter snippet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701104342925-Manage-Filter-Snippets), or [dashboard](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701108132365-Apply-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the filter sidebar, select its filter icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243232183181)) or select **Settings** from the [menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243246882829)) and then select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243246883341) on the [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243246883725)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.
2. Select **Add Filter**. A work area opens for applying Row, Group, and Saved filters.
3. Select an add icon ![add icon](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243246884365 "add icon") and select **Add Custom Metric** from the resulting menu. The Custom Metrics Editor appears.
4. In the Function Library, double-select **AVG(field)**.
5. In Fields, select **Sales**.
6. Select **Run** to see a preview of the results.
7. Name your custom metric and select **Save**.
8. Close the Custom Metrics Editor.

Now that you have created and successfully saved the custom metric you want to use, you can apply it to the visual, filter snippet, or dashboard.

**Filter your data by the aggregated field**

1. Select the filter icon on the [visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701118671885-Apply-a-Row-Level-Filter-to-a-Visual-or-Filter-Snippet), [filter snippet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701104342925-Manage-Filter-Snippets), or [dashboard](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701108132365-Apply-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the filter sidebar, select its filter icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243232183181)) or select **Settings** from the [menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243246882829)) and then select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243246883341) on the [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243246883725)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.
2. Select **Add Filter**.
3. Ensure that the row-level filter for males in Los Angeles is applied.
4. Select **Add Filter**.
5. From the list of available attributes, select **Zipcode**.
6. Choose the zip codes you want to include in your results. For example, all the 900 zip codes or 90211, 90305, and 90701.
7. Select **Apply**.
8. Select **Add Filter**.
9. Select the **Group** tab.
10. Select your saved custom metric from the list of available custom metrics for use.
11. Select the **Operator** tab and then select the greater-than (>)operator.
12. In the value field, enter 100 and then select **Apply**.
    In the Filters sidebar , you can see all the filters you have applied thus far.
13. On the visual canvas, select **Group** and ensure **Product Category** is selected for an attribute.
14. To view the differences in average sales for products, simply filter on different income brackets. For example, apply a filter for incomes between $100 to $1000.
