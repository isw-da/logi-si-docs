---
title: "Apply a Group Filter from a Metric"
id: 34932986213773
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932986213773-Apply-a-Group-Filter-from-a-Metric
updated_at: 2026-05-26T22:09:37Z
---

# Apply a Group Filter from a Metric

# Apply a Group Filter from a Metric

Suppose you want to find product sales greater than $200,000 for the last quarter within the greater Los Angeles area. You might create a group filter using the following steps. This example requires that you have already applied a row-level filter for the city of Los Angeles.

Group filters can only be applied from a specific visual or filter snippet. They cannot be applied to a dashboard.

**Create the group filter**

1. Select the filter icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167891115789)) or select **Settings** from the [menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu) (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167902505869)) and then select ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167902506509) on the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu).

   The Filters sidebar appears showing any filters that have been applied.
2. Select **Add Filter**. A work area opens for applying Row, Group, and Saved filters.
3. Select the Group tab and select the numeric field **Sales** on the tab.

   The Range tab appears in the Filters sidebar. By default, the Aggregation function is set to Sum. You can select other values from the drop-down list.
4. Select the **Greater Than** operator in the Operator selection box. This allows you to input a threshold value, rather than a value range.
5. Specify a threshold value of 200000 in the Value box.
6. Select **Apply**.
7. After the visual updates, select **Group** and then select **Product Category**. This displays all sales of products totally over $200,000.
8. Remember to [save your filter](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932976956941-Maintain-Saved-Filters).
