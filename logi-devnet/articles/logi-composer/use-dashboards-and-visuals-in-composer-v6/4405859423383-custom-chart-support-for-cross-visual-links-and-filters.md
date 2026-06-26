---
title: "Custom Chart Support for Cross-Visual Links and Filters"
id: 4405859423383
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859423383-Custom-Chart-Support-for-Cross-Visual-Links-and-Filters
updated_at: 2021-09-21T01:29:15Z
---

# Custom Chart Support for Cross-Visual Links and Filters

# Custom Chart Support for Cross-Visual Links and Filters

The `zd-chart` CLI supports the ability to publish and subscribe to cross-visual links. To implement publish/subscribe cross-visual filtering for custom charts, use the CLI to edit your charts and enable the controls for publish and subscribe. See [*Step 4. Enable Cross-Visual Filtering*](https://devnet.logianalytics.com/hc/en-us/articles/4405850977047-Part-4-Custom-Chart-Controls#Cross-vis).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Publish should only be enabled if the custom chart uses the radial menu and filtering.

Cross-source links and same-source links are automatically populated and supported on the **Cross-Visual Filtering** tab of the [Dashboard Interactions dialog](https://devnet.logianalytics.com/hc/en-us/articles/4405859426583-Understand-the-Cross-Visual-Filtering-Tab) for custom charts when they are added to a dashboard, in the following circumstances.

* When a custom chart has the **Filter** option in its radial menu, same-source links appear in the **Published filters** and **Subscribed filters** sections of the tab.
* When a custom chart does *not* have the **Filter** option in its radial menu, same-source links appear in the **Subscribed filters** section of the tab, but no **Published filters** section is shown.
* When two custom charts using different data sources are added to the dashboard and a cross-source link is added between their data sources, the cross-source link appears in the **Published filters** section for the chart that can publish the link (the chart using the first data source in the cross-source link) only. However, the cross-source link appears in the **Subscribed filters** section for both charts.
* Cross-visual filters are *automatically* applied to custom charts when they are added to a dashboard, in the following circumstances.

  + When two custom charts using the same data source are added to the dashboard, a cross-visual filter specified for the same-source link field on one custom chart is automatically applied to the other custom chart.
  + When two custom charts using different data sources are added to the dashboard and a cross-source link is added between their data sources, a cross-visual filter specified for the cross-source link field on one custom chart is automatically applied to the other custom chart.
