---
title: "Apply a Row-Level Filter to a Visual or\u00a0Filter Snippet"
id: 34932931145741
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932931145741-Apply-a-Row-Level-Filter-to-a-Visual-or-Filter-Snippet
updated_at: 2026-05-26T22:09:39Z
---

# Apply a Row-Level Filter to a Visual or Filter Snippet

# Apply a Row-Level Filter to a Visual or Filter Snippet

You can apply row-level filters for the data in a visual or filter snippet. When more than one filter is applied (either via the visual or filter snippet itself or via a [dashboard filter](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932922987533-Apply-a-Row-Level-Filter-to-a-Dashboard)), the filter conditions are ANDed. In other words, both filter conditions must be met for the data to appear in the visual or filter snippet.

**Apply a row-level filter to a visual or filter snippet**

1. To access the filter sidebar, select its filter icon ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167903055373) or select **Settings** from the [menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu) (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167891681037)) and then select ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167891681805) on the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu).

   The Filters sidebar appears showing any filters that have been applied.
2. Three tabs are appear on the Filters sidebar, allowing you to create a row-level filter, a group filter, or a saved filter. If these tabs do not appear, select **Add Filter** to see them.

   | Tab | Description |
   | --- | --- |
   | **Row** | The **Row** tab allows you to create a row-level filter, as described in the rest of this topic. |
   | **Group** | The **Group** tab allows you to create and use a group filter. See [Apply Group Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932955067661-Apply-Group-Filters).  If you are using a KPI, raw data, histogram, or map markers visual, the **Group** tab is not available because all filters on these visuals are row-level filters. |
   | **Saved** | The **Saved** tab shows saved filters that you can apply to the dashboard, filter snippet, or visual. See [Maintain Saved Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932976956941-Maintain-Saved-Filters). |
3. Select the Row tab and then select the filter attribute, number, or time field you want to use from the list. The process of creating a row-level filter varies based on the type of field you select.

   * If you select an attribute field, see [Set an Attribute Filter](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932939064717-Set-an-Attribute-Filter).
   * If you select a numeric field, see [Set a Numeric Field Filter](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932957895565-Set-a-Numeric-Field-Filter).
   * If you select a time field, see [Set a Time Field Filter](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932958685197-Set-a-Time-Field-Filter).

   You can also select the add icon ![add icon](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167903058701 "add icon") to access the [Derived Field Editor](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932882620813-Derived-Field-Editor) or the [Custom Metrics Editor](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932820475405-Custom-Metrics-Editor) to create or modify derived fields and custom metrics to be used as filters. See [Access the Derived Field Editor from the Filters Sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932881853581-Access-the-Derived-Field-Editor-from-the-Filters-Sidebar) and [Access the Custom Metrics Editor from the Filters Sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932813600525-Access-the-Custom-Metrics-Editor-from-the-Filters-Sidebar).
4. After the filter specifics have been defined, select **Continue**. The filter is applied to the selected (active) visual or filter snippet. Note that a number appears in a green circle next to the filter icon on the visuals to which the filter has been applied. The number represents the number of filters applied to the visual.

To view the filters applied, see [Viewing the Applied Filters for a Visual or Filter Snippet](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932954339341-Viewing-the-Applied-Filters-for-a-Visual-or-Filter-Snippet).

## Example

Suppose you want to learn what the planned sales are for different product categories for male customers in San Francisco. You might apply a series of row-level filters using the following steps.

1. On your sales visual, select **Group** (x-axis) and then select **Product Category** from the list.
   The visual data is grouped by product category purchases.
2. On your sales visual, select **Planned Sales** for the **Metric** (y-axis). Your visual might look like this:

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167189130509)
3. Select the filter icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167903059597)) on the visual.
4. Select **Add Filter**, then on the Row tab, select **City**.
5. On the next page, select the **Value** tab and ensure **Include** is selected on the tab. Then locate and select **San Francisco** from the list of available attribute values.
6. Select **Continue**, then **Apply**. Your filter is now displayed on the Filters sidebar and is applied to your visual. The visual shows all planned purchases in San Francisco by category.
7. In the Filters sidebar, select **Add Filter** again.
8. Select the **Gender** attribute on the Row tab.
9. On the next page, select the **Value** tab and ensure **Include** is selected. Then select **Male** from the list of available attribute values.
10. Select **Continue**, then **Apply**. The Filters sidebar shows both filters you have applied to your visual. The visual shows all planned purchases in San Francisco by men. The purchases are grouped by category and might look like this:

    ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167205000845)
11. Filters are not saved automatically. To save your filter, select **Save Filters** on the Filters sidebar. The Save Filter Set dialog appears.

    Enter a name for the saved filter and, optionally, a description. If you want to share your filter, slide the **Share Filter Set** switch on (to the right). This shares the filter with other users when they view dashboards created using that same source.
