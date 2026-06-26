---
title: "Control How Cross-Visual Filters Interact in a Dashboard"
id: 4402963028631
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402963028631-Control-How-Cross-Visual-Filters-Interact-in-a-Dashboard
updated_at: 2021-08-07T17:32:33Z
---

# Control How Cross-Visual Filters Interact in a Dashboard

# Control How Cross-Visual Filters Interact in a Dashboard

You can control how cross-visual filters interact in a dashboard. Cross-visual filters are filters created using same-source and cross-source link fields established in the dashboard. You can control which same-source and cross-source link fields each dashboard visual can publish (apply cross-visual filters for) and which links each dashboard visual subscribes to(which cross-visual filters can be applied to the visual).

![](https://devnet.logianalytics.com/hc/article_attachments/4404959473559/noteicon.jpg) When more than one dashboard is embedded in application, the cross-visual filters that are published for a visual on one of the dashboards can be subscribed to by any visual on any of the embedded dashboards. However, this is not true unless the dashboards are embedded in the same application. Visuals in a dashboard open in one window or tab cannot subscribe to cross-visual filters published by visuals in a different window or tab.

Using the **Cross-Visual Filtering** tab of the Dashboard Interactions dialog, you can specify which links each dashboard visual publishes and which each visual subscribes to.

* When a visual publishes a link, that visual can apply cross-visual filters using the link field to other dashboard visuals that have subscribed to the link. Cross-visual filters can only be applied if the associated link is published. In addition, they can only be applied using the **Filter** option on the [radial menu](https://devnet.logianalytics.com/hc/en-us/articles/4402963090199-Use-the-Radial-Menu).
* When a visual subscribes to a link, the visual will be filtered by the link field if another visual creates a cross-visual filter for the same field.

Custom cross-visual filters can also be created in your Javascript code. See [*Publish Custom Cross-Visual Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4404952935831-Publish-Custom-Cross-Visual-Filters).

Dashboard links are created for a dashboard in two ways:

* Each visual in a dashboard automatically creates *same-source links* for each field (column) in the data source that it uses. Same-source link names have the format: `<source-name>.<field-name>`.

  When a visual is added to a dashboard, its same-source links are created and the links are published. In addition, the visual is automatically subscribed to its own same-source links.
* You can create *cross-source links* for common fields in different data sources used on the same dashboard. See [*Use Cross-Source Links*](https://devnet.logianalytics.com/hc/en-us/articles/4402962929047-Use-Cross-Source-Links). These links can also be published and subscribed in a dashboard.

See the following topics:

* [*Understand the Cross-Visual Filtering Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4402955639447-Understand-the-Cross-Visual-Filtering-Tab)
* [*Publish a Link*](https://devnet.logianalytics.com/hc/en-us/articles/4402955636759-Publish-a-Link)
* [*Mute a Published Link*](https://devnet.logianalytics.com/hc/en-us/articles/4402955637399-Mute-a-Published-Link)
* [*Revoke a Published Link*](https://devnet.logianalytics.com/hc/en-us/articles/4402955638039-Revoke-a-Published-Link)
* [*Subscribe a Visual to a Link*](https://devnet.logianalytics.com/hc/en-us/articles/4402963029399-Subscribe-a-Visual-to-a-Link)
* [*Mute a Subscribed Link for a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4402963030167-Mute-a-Subscribed-Link-for-a-Visual)
* [*Specify Cross-Visual Filters for Cross-Visual Links*](https://devnet.logianalytics.com/hc/en-us/articles/4402955640087-Specify-Cross-Visual-Filters-for-Cross-Visual-Links)
* [*Embed Cross-Visual Link Publish and Subscribe Settings Using JavaScript*](https://devnet.logianalytics.com/hc/en-us/articles/4402963025687-Embed-Cross-Visual-Link-Publish-and-Subscribe-Settings-Using-JavaScript)
* [*Custom Chart Support for Cross-Visual Links and Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4402955638807-Custom-Chart-Support-for-Cross-Visual-Links-and-Filters)
