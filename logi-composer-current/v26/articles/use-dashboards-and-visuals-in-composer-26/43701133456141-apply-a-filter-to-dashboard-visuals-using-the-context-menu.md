---
title: "Apply a Filter to Dashboard Visuals Using the Context Menu"
id: 43701133456141
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701133456141-Apply-a-Filter-to-Dashboard-Visuals-Using-the-Context-Menu
updated_at: 2026-05-29T14:08:36Z
---

# Apply a Filter to Dashboard Visuals Using the Context Menu

# Apply a Filter to Dashboard Visuals Using the Context Menu

You can filter visuals on a dashboard that use the same source or linked cross source simultaneously using the context menu of one of the visuals when the visuals are subscribed to the links. These filters are cross-visual filters. See [Subscribe a Visual to a Link](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701123075085-Subscribe-a-Visual-to-a-Link) ror more information about subscribing to dashboard links.

**Note:** 
Unlike row-level filters, cross-visual filters are not saved with the visual.

Example:

* You have a bar chart, pie chart, and table that show data from the same product sales data source (same source link) and are all subscribed to the same source link. In this scenario, you can use the context menu to simultaneously filter the data in two of the three visuals by any field in the data source. The visual you use to select the filter is not affected.
* You add a donut chart to the three visuals above in the same dashboard, but the donut chart uses data from a different sales data source. Cross-source link the two data sources by a field (for example, State) to subscribe all of the visuals to the cross-source link. When you use the context menu to filter one of the visuals by State, the subscribed visuals are all filtered. The visual you use to select the filter is not affected.

Controls for use of filters by end users are provided using the interactivity sidebar. See [Control How Users Interact With a Visual](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701185104653-Control-How-Users-Interact-With-a-Visual).

To view the filters applied to a visual, see [Viewing the Applied Filters for a Visual or Filter Snippet](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701133601549-Viewing-the-Applied-Filters-for-a-Visual-or-Filter-Snippet).

### Apply A Context Menu Filter

**Apply a context menu filter to all dashboard visuals that subscribe to a same source or cross-source link**

1. Open the dashboard and select one of the data points in one of the visuals. The context menu appears.
2. Select **Filter** on the context menu. The filter is applied to all of the visuals subscribed to the link. The visual you use to select the filter is not affected.

   The **Filter** option on the context menu is only available when the visual publishes a link for the field it is also using for its visual grouping. It is *not* available if the published cross-visual links for the visual are muted. See [Mute a Published Link](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701158070285-Mute-a-Published-Link).
