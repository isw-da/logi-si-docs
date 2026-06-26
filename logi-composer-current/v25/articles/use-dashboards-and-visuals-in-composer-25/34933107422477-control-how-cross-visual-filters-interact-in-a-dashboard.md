---
title: "Control How Cross-Visual Filters Interact in a Dashboard"
id: 34933107422477
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933107422477-Control-How-Cross-Visual-Filters-Interact-in-a-Dashboard
updated_at: 2026-05-26T22:07:51Z
---

# Control How Cross-Visual Filters Interact in a Dashboard

# Control How Cross-Visual Filters Interact in a Dashboard

You can control how cross-visual filters interact in a dashboard. Cross-visual filters are filters created using same-source and cross-source link fields established in the dashboard. You can control which same-source and cross-source link fields each dashboard visual can publish (apply cross-visual filters for) and which links each dashboard visual subscribes to (which cross-visual filters can be applied to the visual).

**Note:** 
When more than one dashboard is embedded in an application, the cross-visual filters that are published for a visual on one of the dashboards can be subscribed to by any visual on any of the embedded dashboards. However, this is not true unless the dashboards are embedded in the same application. Visuals in a dashboard open in one window or tab cannot subscribe to cross-visual filters published by visuals in a different window or tab.

Using the **Cross-Visual Filtering** tab of the Dashboard Interactions dialog, you can specify which links each dashboard visual publishes and which each visual subscribes to.

* When a visual publishes a link, that visual can apply cross-visual filters using the link field to other dashboard visuals that have subscribed to the link. Cross-visual filters can only be applied if the associated link is published. In addition, they can only be applied using the **Filter** option on the [context menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933236349453-Use-the-Context-Menu).
* When a visual subscribes to a link, the visual will be filtered by the link field if another visual creates a cross-visual filter for the same field.

Custom cross-visual filters can also be created in your Javascript code. See [Publish Custom Cross-Visual Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933105142797-Publish-Custom-Cross-Visual-Filters).

Dashboard links are created for a dashboard in two ways:

* Each visual in a dashboard automatically creates *same-source links* for each field (column) in the data source that it uses. Same-source link names have the format: `<source-name>.<field-name>`.

  When a visual is added to a dashboard, its same-source links are created and the links are published. In addition, the visual is automatically subscribed to its own same-source links.
* You can create *cross-source links* for common fields in different data sources used on the same dashboard. See [Use Cross-Source Links](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932758491405-Use-Cross-Source-Links). These links can also be published and subscribed in a dashboard.

See the following topics:

* [Understand the Cross-Visual Filtering Tab](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933116644621-Understand-the-Cross-Visual-Filtering-Tab)
* [Publish a Link](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933081250701-Publish-a-Link)
* [Mute a Published Link](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933081445773-Mute-a-Published-Link)
* [Revoke a Published Link](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933109232909-Revoke-a-Published-Link)
* [Subscribe a Visual to a Link](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933117410317-Subscribe-a-Visual-to-a-Link)
* [Mute a Subscribed Link for a Visual](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933107698573-Mute-a-Subscribed-Link-for-a-Visual)
* [Specify Cross-Visual Filters for Cross-Visual Links](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933095470861-Specify-Cross-Visual-Filters-for-Cross-Visual-Links)
* [Publish Custom Cross-Visual Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933105142797-Publish-Custom-Cross-Visual-Filters)
* [Subscribe to a Cross-Visual Filter](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933065274509-Subscribe-to-a-Cross-Visual-Filter)
* [Date-Time Formats in Cross-Visual Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933066060429-Date-Time-Formats-in-Cross-Visual-Filters)
* [Embed Cross-Visual Link Publish and Subscribe Settings Using JavaScript](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933125724685-Embed-Cross-Visual-Link-Publish-and-Subscribe-Settings-Using-JavaScript)
* [Custom Chart Support for Cross-Visual Links and Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933065927181-Custom-Chart-Support-for-Cross-Visual-Links-and-Filters)
