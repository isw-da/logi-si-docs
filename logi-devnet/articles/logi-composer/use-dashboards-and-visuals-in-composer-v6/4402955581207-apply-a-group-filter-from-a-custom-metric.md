---
title: "Apply a Group Filter from a Custom Metric"
id: 4402955581207
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955581207-Apply-a-Group-Filter-from-a-Custom-Metric
updated_at: 2021-08-07T17:33:26Z
---

# Apply a Group Filter from a Custom Metric

# Apply a Group Filter from a Custom Metric

Suppose you want to find product purchases made by males within certain areas of Los Angeles, while also comparing their income levels. Specifically, you are interested in men whose sales average more than $100,000. You might create a filter using the following steps. This example requires that you have already applied a row-level filter for the city of Los Angeles.

Since you do not have a custom metric created yet for average sales, one needs to be created.

To create the custom metric:

1. Select the filter icon on the [visual](https://devnet.logianalytics.com/hc/en-us/articles/4402962986263-Apply-a-Row-Level-Filter-to-a-Visual) or [dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4402955577239-Apply-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4404952816151/filter-vis.png)) or select **Edit Visual** from the [visual menu](https://devnet.logianalytics.com/hc/en-us/articles/4402955730967-Use-the-Visual-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4404952780951/three-dots-menu_19x11.png)) and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959519383/sidebar-filter_20x21.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402955735319-Use-the-Visual-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4404952781207/filter-dash.png)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952855191/add-filter-btn_76x21.png).
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959479319/add.png) and select **Add Custom Metric** from the resulting menu. The Custom Metrics Editor appears.
4. In the Function Library, double-select **AVG(field)**.
5. In Attributes & Metrics, select **Sales**.
6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952855447/run-btn_32x23.png) to see a preview of the results.
7. Name your custom metric and select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959502359/save-blue-btn.png).
8. Close the Custom Metrics Editor.

Now that you have created and successfully saved the custom metric you want to use, you can apply it to the visual or dashboard.

To filter your data by the aggregated field:

1. Select the filter icon on the [visual](https://devnet.logianalytics.com/hc/en-us/articles/4402962986263-Apply-a-Row-Level-Filter-to-a-Visual) or [dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4402955577239-Apply-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4404952816151/filter-vis.png)) or select **Edit Visual** from the [visual menu](https://devnet.logianalytics.com/hc/en-us/articles/4402955730967-Use-the-Visual-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4404952780951/three-dots-menu_19x11.png)) and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959519383/sidebar-filter_20x21.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402955735319-Use-the-Visual-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4404952781207/filter-dash.png)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952855191/add-filter-btn_76x21.png).
3. Ensure that the row-level filter for males in Los Angeles is applied.
4. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952855191/add-filter-btn_76x21.png).
5. From the list of available attributes, select **Zipcode**.
6. Choose the zip codes you want to include in your results. For example, all the 900 zip codes or 90211, 90305, and 90701.
7. Select **Apply**.
8. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952855191/add-filter-btn_76x21.png).
9. Select the **Group** tab.
10. Select your saved custom metric from the list of available custom metrics for use.
11. Select the **Operator** tab and then select the greater-than (>)operator.
12. In the value field, enter 100 and then select **Apply**.
    In the Filters sidebar , you can see all the filters you have applied thus far.
13. On the visual canvas, select **Group** and ensure **Product Category** is selected for an attribute.
14. To view the differences in average sales for products, simply filter on different income brackets. For example, apply a filter for incomes between $100 to $1000.
