---
title: "Creating a Saved Filter"
id: 4402537801239
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537801239-Creating-a-Saved-Filter
updated_at: 2021-09-15T02:21:41Z
---

# Creating a Saved Filter

# Creating a Saved Filter

When you have created filters and applied them to a dashboard, they are listed under
**Active Filters** on the Filter dialog. You can save these filters to be applied later to visuals from the same data source. A saved filter can include the settings from one or more filters.

To save a filter:

1. Select the filter icon on the [visual](https://devnet.logianalytics.com/hc/en-us/articles/4402537795351-Applying-a-Row-Level-Filter-to-a-Visual) or [dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4402552811415-Applying-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406753463191/filter-vis.png)) or select **Edit Visual** from the [visual menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406763902743/three-dots-menu_19x11.png)) and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753463447/sidebar-filter_20x21.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406763902999/filter-dash.png)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied. If no filters have been applied, create one that you want to save. See [*Applying Row-Level Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4402537794711-Applying-Row-Level-Filters), [Setting a Numeric Field Filter](https://devnet.logianalytics.com/hc/en-us/articles/4402537797399-Setting-a-Numeric-Field-Filter), and [Setting a Time Field Filter](https://devnet.logianalytics.com/hc/en-us/articles/4402552813847-Setting-a-Time-Field-Filter).
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763975831/save-filters_64x21.png) on the Filters sidebar. The Save Filter Set dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763976087/save-filter-set_224x219.png)
3. Supply a name for the saved filter in the **Name** field.
4. Optionally, provide a description for the saved filter in the **Description** field.
5. If you want to share this set with other users, select **Share Filter Set**.
6. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763976343/apply1-btn_43x24.png).

   The Save Filter Set dialog closes and the filter is saved. You can see the saved filter on the **Saved Filters** tab of the filters dialog in other visuals that use the same data source.
7. [Save](https://devnet.logianalytics.com/hc/en-us/articles/4402537747863-Saving-a-Dashboard) the dashboard.

## Example

Suppose you want to create a saved filter for different jewelry sales.

1. On your sales visual or sales dashboard (if all of the visuals on the dashboard are using the same sales data source), open the Filters sidebar.
2. On the Filters sidebar, create and apply a filter for jewelry sales. See [Applying Row-Level Filters](https://devnet.logianalytics.com/hc/en-us/articles/4402537794711-Applying-Row-Level-Filters).

   * Select the **Row** tab on the Filters sidebar.
   * Depending on how the data in your data source is organized, select whatever attribute you use to identify a jewelry sale (for example, Category).
   * On the next page of the Filters sidebar, select jewelry types in the possible attribute values (for example, for the Category attribute, you might select rings, earrings, pendants, and bracelets).
   * Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753455127/apply1-btn_41x23.png) to apply the filter. You visual (or dashboard) now shows all sales data for jewelry. The first page of the Filters sidebar appears again.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753469719/save-filters_61x20.png) on the Filters sidebar. The Save Filter Set dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763976599/save-filter-set_226x221.png)
4. Enter a name for the saved filter (for example, Jewelry Sales) and, optionally, a description. If you want to share your filter, slide the **Share Filter Set** toggle on (to the right). This shares the filter with other users when they view dashboards created using that same source.
5. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763976343/apply1-btn_43x24.png) to save the Jewelry Sales filter.
