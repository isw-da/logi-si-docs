---
title: "Use Cross-Visual Links for Cross-Visual Filtering"
id: 34932951587853
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932951587853-Use-Cross-Visual-Links-for-Cross-Visual-Filtering
updated_at: 2026-05-26T22:09:40Z
---

# Use Cross-Visual Links for Cross-Visual Filtering

# Use Cross-Visual Links for Cross-Visual Filtering

After you have defined cross-source or same-source links for a dashboard, you can use them in cross-visual filtering. Cross-visual filtering allows you to simultaneously apply the same filter across all visuals in your dashboard that use the linked fields. Cross-visual filters must be applied from a visual's context menu or from the time bar.

**Note:** 
Unlike row-level filters, cross-visual filters are not saved with the visual.

Cross-source link must be defined on a dashboard before you can use them in cross-visual filtering. However, same-source links are created automatically and can be automatically used in cross-visual filtering. In addition, cross-visual filters are only applied to a dashboard visual if the visual subscribes to its associated cross-visual link. See [Define Cross-Source Links](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932758167821-Define-Cross-Source-Links), [Publish a Link](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933081250701-Publish-a-Link), and [Subscribe a Visual to a Link](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933117410317-Subscribe-a-Visual-to-a-Link).

This section includes the following topics.

* [Apply Cross-Visual Filtering to Dashboard Visuals](#Apply)
* [Apply Cross-Visual Filtering From the Time Bar](#Xsource)

To view the filters applied to a visual, see [Viewing the Applied Filters for a Visual or Filter Snippet](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932954339341-Viewing-the-Applied-Filters-for-a-Visual-or-Filter-Snippet).

## Apply Cross-Visual Filtering to Dashboard Visuals

**Apply a cross-visual filter from a visual to the dashboard visuals**

1. After cross-visual links are created, select an area of the visual that uses a linked field. The [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu) for that area of the visual displays:

   ![Select to filter your data](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167234597133 "The context menu with filter option")

   **Note:** 
   Filters for cross-source and same-source links must be defined using the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu). You cannot create a link filter from the [Filters sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932968609677-The-Filters-Sidebar). Filters created from the sidebar apply only to the selected visual. Filters for cross-source and same-source links are called *cross-visual filters* and are listed in the [Filters sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932968609677-The-Filters-Sidebar) separately from filters that are applied from the Filters sidebar.
2. Select **Filter** on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu).

   The filter is automatically applied to all of the visuals that are subscribed to the link. For more information about published and subscribed links, see [Control How Cross-Visual Filters Interact in a Dashboard](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933107422477-Control-How-Cross-Visual-Filters-Interact-in-a-Dashboard).
3. [Save](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932815496845-Save-a-Dashboard) the dashboard.

## Apply Cross-Visual Filtering From the Time Bar

To apply a cross-visual filter from the time bar, a same-source or cross-source link for time fields in the data sources must first be created.

**Apply a cross-visual filter to the dashboard using a time field from the time bar**

1. After cross-visual links are created, select the time field in the time bar. The Time Bar dialog appears.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167217260941)
2. Select the linked time field you have defined in the **Time Attribute** section of the Time Bar dialog.
3. Select the visuals to which you want the time filter applied in the **Applies to** section. The **Applies to** section lists all the visuals in the dashboard that use data from:

   * The same data source with a same-source link subscribed for the linked time field.
   * Different data sources with a linked time field for the data you have selected.
4. Adjust the time bar minimum or maximum to filter the visuals. See [Use the Time Bar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933204115725-Use-the-Time-Bar).
