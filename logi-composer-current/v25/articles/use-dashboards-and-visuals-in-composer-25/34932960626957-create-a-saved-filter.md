---
title: "Create a Saved Filter"
id: 34932960626957
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932960626957-Create-a-Saved-Filter
updated_at: 2026-05-26T22:09:33Z
---

# Create a Saved Filter

# Create a Saved Filter

When you have created filters and applied them to a dashboard, they are listed under
**Active Filters** on the Filter dialog. You can save these filters to be applied later to visuals or filter snippets from the same data source. A saved filter can include the settings from one or more filters.

**Note:** 
Cross-visual filters that have been applied from same-source and cross-source links are not saved when filters are saved for a visual. Saved filters only include row-level filters for the visual.

**Save a filter**

1. Select the filter icon on the [visual](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932931145741-Apply-a-Row-Level-Filter-to-a-Visual-or-Filter-Snippet), filter snippet, or [dashboard](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932922987533-Apply-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the filter sidebar, select its filter icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167885651725)) or select **Settings** from the [menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu) (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167885652493)) and then select ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167875481101) on the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167875482125)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied. If no filters have been applied, create one that you want to save. See [Apply Row-Level Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932930630157-Apply-Row-Level-Filters), [Set a Numeric Field Filter](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932957895565-Set-a-Numeric-Field-Filter), and [Set a Time Field Filter](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932958685197-Set-a-Time-Field-Filter).
2. Select **Save Filters** on the Filters sidebar. The Save Filter Set dialog appears.
3. Supply a name for the saved filter in the **Name** field.
4. Optionally, provide a description for the saved filter in the **Description** field.
5. If you want to share this set with other users, select **Share Filter Set**.
6. Select **Apply**.

   The Save Filter Set dialog closes and the filter is saved. You can see the saved filter on the **Saved Filters** tab of the filters dialog in other visuals that use the same data source.
7. [Save](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932815496845-Save-a-Dashboard) the dashboard.

## Example

Suppose you want to create a saved filter for different jewelry sales.

1. On your sales visual, sales filter snippet, or sales dashboard (if all the visuals on the dashboard are using the same sales data source), open the Filters sidebar.
2. On the Filters sidebar, create and apply a filter for jewelry sales. See [Apply Row-Level Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932930630157-Apply-Row-Level-Filters).

   * Select the **Row** tab on the Filters sidebar.
   * Depending on how the data in your data source is organized, select whatever attribute you use to identify a jewelry sale (for example, Category).
   * On the next page of the Filters sidebar, select jewelry types in the possible attribute values (for example, for the Category attribute, you might select rings, earrings, pendants, and bracelets).
   * Select **Apply** to apply the filter. You visual, visuals linked to a filter snippet, (or dashboard) now shows all sales data for jewelry. The first page of the Filters sidebar appears again.
3. Select **Save Filter** on the Filters sidebar. The Save Filter Set dialog appears.
4. Enter a name for the saved filter (for example, Jewelry Sales) and, optionally, a description. If you want to share your filter, slide the **Share Filter Set** switch on (to the right). This shares the filter with other users when they view dashboards created using that same source.
5. Select **Apply** to save the Jewelry Sales filter.
