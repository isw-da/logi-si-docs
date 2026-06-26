---
title: "Apply a Group Filter from a Metric"
id: 4405859351703
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859351703-Apply-a-Group-Filter-from-a-Metric
updated_at: 2021-09-21T01:28:37Z
---

# Apply a Group Filter from a Metric

# Apply a Group Filter from a Metric

Suppose you want to find product sales greater than $200,000 for the last quarter within the greater Los Angeles area. You might create a group filter using the following steps. This example requires that you have already applied a row-level filter for the city of Los Angeles.

Group filters can only be applied from a specific visual. They cannot be applied to a dashboard.

To create the group filter:

1. Select the visual's filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406743754263/filter-vis.png)) or select **Edit Visual** from the [visual menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743718551/three-dots-menu_19x11.png)) and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743782935/sidebar-filter_20x21.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu).

   The Filters sidebar appears showing any filters that have been applied.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406747415959/add-filter-btn_76x21.png).
3. Select the Group tab and select the numeric field **Sales** on the tab.

   The Range tab appears in the Filters sidebar. By default, the Aggregation function is set to Sum. You can select other values from the drop-down list.
4. Select the **Greater Than** operator in the Operator selection box. This allows you to input a threshold value, rather than a value range.
5. Specify a threshold value of 200000 in the Value box.
6. Select **Apply**.
7. After the visual updates, select **Group** and then select **Product Category**. This displays all sales of products totally over $200,000.
8. Remember to [save your filter](https://devnet.logianalytics.com/hc/en-us/articles/4405851070359-Maintain-Saved-Filters).
