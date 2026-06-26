---
title: "Review and Apply a Keyset as a Visual Filter"
id: 4405859387543
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859387543-Review-and-Apply-a-Keyset-as-a-Visual-Filter
updated_at: 2021-09-21T01:28:59Z
---

# Review and Apply a Keyset as a Visual Filter

# Review and Apply a Keyset as a Visual Filter

You can review and apply a keyset as a visual filter to visuals that use the same or different data sources. The visuals will be limited to records containing values stored in the keyset.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) To apply a keyset to a visual, the data source for the target visual must include a field storing the same data as the key field used for the keyset. The key field is defined when the keyset is created. See [*Create a Keyset*](https://devnet.logianalytics.com/hc/en-us/articles/4405851103255-Create-a-Keyset).

Keysets can be applied to all the visuals on a dashboard only if the dashboard contains visuals that use the same data source.

To review and apply a keyset as a visual filter:

1. For the purposes of this procedure, suppose you want to list the planned sales for jewelry. Assuming you have previously created a keyset containing a list of jewelry (see [*Create a Keyset*](https://devnet.logianalytics.com/hc/en-us/articles/4405851103255-Create-a-Keyset)), we will apply it to a bar chart showing planned sales by category.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743785879/planned-sales-category_480x201.png)
2. Select the filter icon on the [visual](https://devnet.logianalytics.com/hc/en-us/articles/4405851057431-Apply-a-Row-Level-Filter-to-a-Visual) or [dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4405851056535-Apply-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406743754263/filter-vis.png)) or select **Edit Visual** from the [visual menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406743718551/three-dots-menu_19x11.png)) and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743782935/sidebar-filter_20x21.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859578391-Use-the-Visual-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406743718807/filter-dash.png)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743786391/add-filter-btn_91x21.png).
4. Locate the data field in the Filters sidebar list that contains the same kind of data as the data in the keyset you want to use. In our example, it would be Category.

   The Filters sidebar displays three tabs:

   * The **Value** tab allows you to select values for the filter.
   * The **Wildcard** tab allows you to specify a row-level wild card filter for the visual.
   * The **Keyset** tab allows you to select a keyset for the filter or to upload a CSV file as a keyset.
5. Select the **Keyset** tab. The keysets and saved filters defined in your environment are listed. In our example, the keyset VA Airports is listed.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743787287/sales-category_192x421.png)
6. Select the keyset you want to apply. Details about the keyset appear on the Filters sidebar.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743783447/keyset-details_192x417.png)

   You can sort the data in the keyset as needed by selecting the up and down arrows (![](https://devnet.logianalytics.com/hc/article_attachments/4406743787543/up-down-arrow.png)) in the Preview area. This sort has no effect on the visual result set when the keyset is applied.
7. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743745559/apply1-btn_41x23.png). The visual is filtered by the keyset data. In our example, it shows the canceled flights from Virginia airports.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747413271/jewelry-planned-sales_576x240.png)

   Select the **x** in the upper right corner of the Filters sidebar to close it.
