---
title: "Use Cross-Visual Links for Cross-Visual Filtering"
id: 4405859347991
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859347991-Use-Cross-Visual-Links-for-Cross-Visual-Filtering
updated_at: 2021-09-21T01:28:31Z
---

# Use Cross-Visual Links for Cross-Visual Filtering

# Use Cross-Visual Links for Cross-Visual Filtering

After you have defined cross-source or same-source links for a dashboard, you can use them in cross-visual filtering. Cross-visual filtering allows you to simultaneously apply the same filter across all visuals in your dashboard that use the linked fields. Cross-visual filters must be applied from a visual's radial menu or from the time bar.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Unlike row-level filters, cross-visual filters are not saved with the visual.

Cross-source link must be defined on a dashboard before you can use them in cross-visual filtering. However, same-source links are created automatically and can be automatically used in cross-visual filtering. In addition, cross-visual filters are only applied to a dashboard visual if the visual subscribes to its associated cross-visual link. See [*Define Cross-Source Links*](https://devnet.logianalytics.com/hc/en-us/articles/4405859236887-Define-Cross-Source-Links), [*Publish a Link*](https://devnet.logianalytics.com/hc/en-us/articles/4405859420823-Publish-a-Link), and [*Subscribe a Visual to a Link*](https://devnet.logianalytics.com/hc/en-us/articles/4405851136151-Subscribe-a-Visual-to-a-Link).

This section includes the following topics.

* [*Apply Cross-Visual Filtering to Dashboard Visuals*](#Apply)
* [*Apply Cross-Visual Filtering From the Time Bar*](#Xsource)

To view the filters applied to a visual, see [*Viewing the Applied Filters for a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405851065623-Viewing-the-Applied-Filters-for-a-Visual).

## Apply Cross-Visual Filtering to Dashboard Visuals

To apply a cross-visual filter from a visual to the dashboard visuals:

1. After cross-visual links are created, select an area of the visual that uses a linked field. The [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu) for that area of the visual displays:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743803287/radial-menu_96x96.png)

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Filters for cross-source and same-source links must be defined using the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu). You cannot create a link filter from the [Filters sidebar](https://devnet.logianalytics.com/hc/en-us/articles/4405851062807-The-Filters-Sidebar). Filters created from the sidebar apply only to the selected visual. Filters for cross-source and same-source links are called *cross-visual filters* and are listed in the [Filters sidebar](https://devnet.logianalytics.com/hc/en-us/articles/4405851062807-The-Filters-Sidebar) separately from filters that are applied from the Filters sidebar.
2. Select **Filter** on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu).

   The filter is automatically applied to all of the visuals that are subscribed to the link. For more information about published and subscribed links, see [*Control How Cross-Visual Filters Interact in a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405859431447-Control-How-Cross-Visual-Filters-Interact-in-a-Dashboard).
3. [Save](https://devnet.logianalytics.com/hc/en-us/articles/4405850986647-Save-a-Dashboard) the dashboard.

## Apply Cross-Visual Filtering From the Time Bar

To apply a cross-visual filter from the time bar, a same-source or cross-source link for time fields in the data sources must first be created.

To apply a cross-visual filter to the dashboard using a time field from the time bar:

1. After cross-visual links are created, select the time field in the time bar. The Time Bar dialog appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743803543/time-bar_150x239.png)
2. Select the linked time field you have defined in the **Time Attribute** section of the Time Bar dialog.
3. Select the visuals to which you want the time filter applied in the **Applies to** section. The **Applies to** section lists all the visuals in the dashboard that use data from:

   * The same data source with a same-source link subscribed for the linked time field.
   * Different data sources with a linked time field for the data you have selected.
4. Adjust the time bar minimum or maximum to filter the visuals. See [*Use the Time Bar*](https://devnet.logianalytics.com/hc/en-us/articles/4405851196695-Use-the-Time-Bar).
