---
title: "Review and Apply a Keyset as a Visual Filter"
id: 43701120924045
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120924045-Review-and-Apply-a-Keyset-as-a-Visual-Filter
updated_at: 2026-05-29T14:10:40Z
---

# Review and Apply a Keyset as a Visual Filter

# Review and Apply a Keyset as a Visual Filter

You can review and apply a keyset as a visual filter to visuals that use the same or different data sources. Visuals are limited to records containing values stored in the keyset. You can update a keyset at any time by uploading new values for the keyset.

**Note:** 
To apply a keyset to a visual, the data source for the target visual must include a field storing the same data as the key field used for the keyset. The key field is defined when the keyset is created. See [Create a Keyset](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701135635213-Create-a-Keyset).

**Review and apply a keyset as a visual filter**

1. For the purposes of this procedure, suppose you want to list the planned sales for jewelry. Assuming you have a keyset containing a list of jewelry (see [Create a Keyset](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701135635213-Create-a-Keyset)), apply it to a bar chart showing planned sales by category.

   ![Shows your data as a bar chart](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242490592909 "Bar Chart visual")
2. Select the filter icon on the [visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701118671885-Apply-a-Row-Level-Filter-to-a-Visual-or-Filter-Snippet) or [dashboard](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701108132365-Apply-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the visual filter sidebar, select its filter icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243213685645)) or select **Settings** from the [visual menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu) (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243197417613)) and then select ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243197418253) on the [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243213692685)). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar appears showing any filters that have been applied.
3. Select **Add Filter**.
4. Locate the data field in the Filters sidebar list that contains the same kind of data as the data in the keyset you want to use. In our example, it is Category.

   The Filters sidebar displays three tabs:

   * The **Value** tab allows you to select values for the filter.
   * The **Wildcard** tab allows you to specify a row-level wildcard filter for the visual.
   * The **Keyset** tab allows you to select a keyset for the filter or to upload a CSV file as a keyset.

     **Note:** 
     This example uses a non-numeric filter. See [Set a Numeric Field Filter](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701133427085-Set-a-Numeric-Field-Filter).
5. Select the **Keyset** tab. The keysets and saved filters defined in your environment are listed.

   ![Define your keyset values here](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242490904077 "Select Values Keyset tab")
6. Select the keyset you want to apply. Details about the keyset appear on the Filters sidebar.

   ![Review and edit your keyset values](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243213693965 "Keyset Values Details")

   Sort the data in the keyset as needed by selecting the up and down arrows (![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242475727629)) in the Preview area. This sort has no effect on the visual result set when the keyset is applied.
7. When you are finished setting your filter values, select **Continue** and examine your updates. If they are correct, select **Apply**.

   The visual is filtered by the keyset data.

   ![Your filtered sales data ](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242491616781 "Sales Bar Chart, filtered")

   Select the **x** in the upper right corner of the Filters sidebar to close it.
