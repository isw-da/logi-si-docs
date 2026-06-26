---
title: "Apply a Filter to Dashboard Visuals Using the Radial Menu"
id: 4405851061015
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851061015-Apply-a-Filter-to-Dashboard-Visuals-Using-the-Radial-Menu
updated_at: 2021-09-21T01:28:34Z
---

# Apply a Filter to Dashboard Visuals Using the Radial Menu

# Apply a Filter to Dashboard Visuals Using the Radial Menu

Visuals on your dashboard that are same-source or cross-source linked can be filtered simultaneously using the radial menu of one of the visuals if they are subscribed to the links. These are cross-visual filters. For more information about subscribing to dashboard links, see [*Subscribe a Visual to a Link*](https://devnet.logianalytics.com/hc/en-us/articles/4405851136151-Subscribe-a-Visual-to-a-Link).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Unlike row-level filters, cross-visual filters are not saved with the visual.

Here is an example:

* You have a bar chart, pie chart, and table that show data from the same product sales data source (same-source link) and they are all subscribed to the same-source link. In this scenario, you can use the radial menu to simultaneously filter the data in two of the three visuals by any field in the data source. The visual on which the filter is selected is not affected.
* In addition to the three visuals above, you add a donut chart on the same dashboard that uses data from a different sales data source. You have cross-source linked the two data sources by a field (for example, State) and all of the visuals have subscribed to the cross-source link. When you use the radial menu to filter one of the visuals by State, the subscribed visuals are all filtered. Only the visual on which the filter is selected is not affected.

Controls for use of filters by end users are provided using the interactivity sidebar. See [*Control How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405859573143-Control-How-Users-Interact-With-a-Visual).

To view the filters applied to a visual, see [*Viewing the Applied Filters for a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405851065623-Viewing-the-Applied-Filters-for-a-Visual).

To apply a radial menu filter to all dashboard visuals that subscribe to a same-source or cross-source link:

1. Open the dashboard and select one of the data points in one of the visuals. The radial menu appears.
2. Select **Filter** on the radial menu. The filter is applied to all of the visuals subscribed to the link. The visual on which the filter was selected is not affected.

   In addition, the **Filter** option on the radial menu is only available when the visual publishes a link for the field it is also using for its visual grouping. It is *not* available if the published cross-visual links for the visual are muted. See [*Mute a Published Link*](https://devnet.logianalytics.com/hc/en-us/articles/4405851129495-Mute-a-Published-Link).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) The radial menu is not available on arc gauges, histograms, KPI charts, maps, or tables of raw data.
