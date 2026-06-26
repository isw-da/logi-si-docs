---
title: "Reviewing and Applying a Keyset as a Visual Filter"
id: 4402552841111
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402552841111-Reviewing-and-Applying-a-Keyset-as-a-Visual-Filter
updated_at: 2021-09-15T02:22:02Z
---

# Reviewing and Applying a Keyset as a Visual Filter

# Reviewing and Applying a Keyset as a Visual Filter

You can review and apply a keyset as a visual filter to visuals that use the same or different data sources. The visuals will be limited to records containing values stored in the keyset.

![](https://devnet.logianalytics.com/hc/article_attachments/4406753437463/noteicon.jpg) To apply a keyset to a visual, the data source for the target visual must include a field storing the same data as the key field used for the keyset. The key field is defined when the keyset is created. See [*Creating a Keyset*](https://devnet.logianalytics.com/hc/en-us/articles/4402537823639-Creating-a-Keyset).

Keysets can be applied to all the visuals on a dashboard only if the dashboard contains visuals that use the same data source.

To review and apply a keyset as a visual filter:

1. For the purposes of this procedure, suppose you want to list the canceled flights from Virginia airports. Assuming you have previously created a keyset containing a list of airport codes, (see [*Creating a Keyset*](https://devnet.logianalytics.com/hc/en-us/articles/4402537823639-Creating-a-Keyset)), we will apply it to a bar chart showing canceled flights nationwide:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763958295/canceled-flights_576x224.png)
2. Select the filter icon on the [visual](https://devnet.logianalytics.com/hc/en-us/articles/4402537795351-Applying-a-Row-Level-Filter-to-a-Visual) or [dashboard](https://devnet.logianalytics.com/hc/en-us/articles/4402552811415-Applying-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406753463191/filter-vis.png)) or select **Edit Visual** from the [visual menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu) (![](https://devnet.logianalytics.com/hc/article_attachments/4406763902743/three-dots-menu_19x11.png)) and then select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753463447/sidebar-filter_20x21.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406763902999/filter-dash.png)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406763958551/add-filter-btn.png).
4. Locate the data field in the Filters sidebar list that contains the same kind of data as the data in the keyset you want to use. In our example, it would be Origin Airport Code.

   The Filters sidebar displays filter options that can be applied for the selected data field.
5. Select the **Keysets** tab. The keysets and saved filters defined in your environment are listed. In our example, the keyset Virginia Airport Codes is listed.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763958807/keyset-selection1_192x312.png)
6. Select the keyset you want to apply. Details about the keyset appear on the Filters sidebar.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406753464599/keyset-details1_192x310.png)

   You can sort the data in the keyset as needed by selecting the up and down arrows (![](https://devnet.logianalytics.com/hc/article_attachments/4406763959575/up-down-arrow.png)) in the Preview area. This sort has no effect on the visual result set when the keyset is applied.
7. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753455127/apply1-btn_41x23.png). The visual is filtered by the keyset data. In our example, it shows the canceled flights from Virginia airports.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406753465111/canceled-flights-keyset_576x223.png)

   Select the **x** in the upper right corner of the Filters sidebar to close it.
