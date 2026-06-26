---
title: "Apply a Row-Level Filter to a Visual"
id: 4405851057431
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851057431-Apply-a-Row-Level-Filter-to-a-Visual
updated_at: 2021-09-21T01:28:32Z
---

# Apply a Row-Level Filter to a Visual

# Apply a Row-Level Filter to a Visual

You can apply row-level filters for the data in a visual. When more than one filter is applied to a visual (either via the visual itself or via a [dashboard filter](https://devnet.logianalytics.com/hc/en-us/articles/4405851056535-Apply-a-Row-Level-Filter-to-a-Dashboard)), the filter conditions are ANDed. In other words, both filter conditions must be met for the data to appear in the visual.

To apply a row-level filter to a visual:

1. Select the filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406743754263/filter-vis.png)) on the visual or select **Edit Visual** from the [visual menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743718551/three-dots-menu_19x11.png)) and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743782935/sidebar-filter_20x21.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu).

   The Filters sidebar appears showing any filters that have been applied.
2. Three tabs are appear on the Filters sidebar, allowing you to create a row-level filter, a group filter, or a saved filter. If these tabs do not appear, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743802391/add-filter-btn.png) to see them.

   | Tab | Description |
   | --- | --- |
   | **Row** | The **Row** tab allows you to create a row-level filter, as described in the rest of this topic. |
   | **Group** | The **Group** tab allows you to create and use a group filter. See [*Apply Group Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4405851068567-Apply-Group-Filters). If you are using a KPI, raw data, histogram, or map markers visual, the **Group** tab is not available because all filters on these visuals are row-level filters. |
   | **Saved** | The **Saved** tab shows saved filters that you can apply to the dashboard or visual. See [*Maintain Saved Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4405851070359-Maintain-Saved-Filters). |
3. Select the Row tab and then select the filter attribute, number, or time field you want to use from the list. The process of creating a row-level filter varies based on the type of field you select.

   * If you select an attribute field, see [*Set an Attribute Filter*](https://devnet.logianalytics.com/hc/en-us/articles/4405851058327-Set-an-Attribute-Filter).
   * If you select a numeric field, see [*Set a Numeric Field Filter*](https://devnet.logianalytics.com/hc/en-us/articles/4405851060119-Set-a-Numeric-Field-Filter).
   * If you select a time field, see [*Set a Time Field Filter*](https://devnet.logianalytics.com/hc/en-us/articles/4405851063831-Set-a-Time-Field-Filter).

   You can also select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743717271/add.png) to access the [*Derived Field Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4405851014551-Derived-Field-Editor) or the [*Custom Metrics Editor*](https://devnet.logianalytics.com/hc/en-us/articles/4405859284119-Custom-Metrics-Editor) to create or modify derived fields and custom metrics to be used as filters.See [*Access the Derived Field Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4405859296663-Access-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [*Access the Custom Metrics Editor from the Filters Sidebar*](https://devnet.logianalytics.com/hc/en-us/articles/4405851000727-Access-the-Custom-Metrics-Editor-from-the-Filters-Sidebar).
4. After the filter specifics have been provided, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743745559/apply1-btn_41x23.png). The filter is applied to the selected (active) visual. Note that a number appears in a green circle next to the filter icon on the visuals to which the filter has been applied. The number represents the number of filters applied to the visual.

To view the filters applied to a visual, see [*Viewing the Applied Filters for a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405851065623-Viewing-the-Applied-Filters-for-a-Visual).

## Example

Suppose you want to learn what the planned sales are for different product categories for male customers in San Francisco. You might apply a series of row-level filters using the following steps.

1. On your sales visual, select **Group** (x-axis) and then select **Product Category** from the list.
   The visual data is grouped by product category purchases.
2. On your sales visual, select **Planned Sales** for the **Metric** (y-axis). Your visual might look like this:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743802647/planned-sales3_576x237.png)
3. Select the filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406743754263/filter-vis.png)) on the visual.
4. On the Row tab, select **City**.
5. On the next page, select the **Value** tab and ensure **Include** is selected on the tab. Then locate and select **San Francisco** from the list of available attribute values.
6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743745559/apply1-btn_41x23.png). Your filter is now displayed on the Filters sidebar and is applied to your visual. The visual shows all planned purchases in San Francisco by category.
7. In the Filters sidebar, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743802391/add-filter-btn.png) again.
8. Select the **Gender** attribute on the Row tab.
9. On the next page, select the **Value** tab and ensure **Include** is selected. Then select **Male** from the list of available attribute values.
10. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743745559/apply1-btn_41x23.png). The Filters sidebar shows both filters you have applied to your visual. The visual shows all planned purchases in San Francisco by men. The purchases are grouped by category and might look like this:

    ![](https://devnet.logianalytics.com/hc/article_attachments/4406743803031/planned-sales4_576x236.png)
11. Filters are not saved automatically. To save your filter, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743796759/save-filters_61x20.png) on the Filters sidebar. The Save Filter Set dialog appears.

    ![](https://devnet.logianalytics.com/hc/article_attachments/4406743797015/save-filter-set_226x221.png)

    Enter a name for the saved filter and, optionally, a description. If you want to share your filter, slide the **Share Filter Set** switch on (to the right). This shares the filter with other users when they view dashboards created using that same source.
