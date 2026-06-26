---
title: "Composer 6.8 Enhancements"
id: 4405859455383
section: "Logi Composer Version 6 Release Notes"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859455383-Composer-6-8-Enhancements
updated_at: 2022-04-25T15:19:14Z
---

# Composer 6.8 Enhancements

# Composer 6.8 Enhancements

This topic describes the significant enhancements in Composer 6.8.

* [*Authorization Changes*](#Auth)
* [*New Dashboard Cross-Visual Filtering Controls*](#Dashboard)
* [*Radial Menu Changes*](#Radial)
* [*Cross-Source Link Changes*](#xSource)
* [*Filter Changes*](#Filter)
* [*Arc Gauge Changes*](#Arc)
* [*Table Enhancements*](#Table)
* [*Dashboard and Visual Export Changes*](#Export-Dash)
* [*Keyset Enhancements*](#Keyset)
* [*Visual Data Cache Changes*](#VisDataCache)
* [*Query Engine Enhancements*](#QueryEngine)
* [*User Interface Changes*](#User)

## Authorization Changes

Groups can no longer be transferred to a different account using the API. In past releases, they could.

## New Dashboard Cross-Visual Filtering Controls

This release introduces new dashboard cross-visual filtering controls. Using the **Cross-Visual Filtering** tab of the new Dashboard Interactions dialog, you can specify which cross-visual filter each dashboard visual publishes (which link fields it can apply cross-visual filtering for) and which cross-visual filter each visual subscribes to (which cross-visual filters can be applied to the visual). Cross-visual filters are filters created using same-source and cross-source link fields established in the dashboard.

See [*Control How Cross-Visual Filters Interact in a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405859431447-Control-How-Cross-Visual-Filters-Interact-in-a-Dashboard). A new Dashboard Interactions dialog is introduced in this release to support this feature. It is accessed from the dashboard icon bar using the ![](https://devnet.logianalytics.com/hc/article_attachments/4406747402135/dash-xsourcelink.png) icon. See [*Use the Dashboard Icon Bar*](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar).

Custom charts support cross-visual filtering controls if the chart supports the radial menu and filtering and if the appropriate publish and subscribe controls are enabled. See [*Custom Chart Support for Cross-Visual Links and Filters*](https://devnet.logianalytics.com/hc/en-us/articles/4405859423383-Custom-Chart-Support-for-Cross-Visual-Links-and-Filters).

Finally, you can specify cross-visual link publish and subscribe settings for an embedded dashboard using JavaScript. Two JavaScript methods are provided for the `Zoomdata` object: `publish` and `subscribe`. See [*Embed Cross-Visual Link Publish and Subscribe Settings Using JavaScript*](https://devnet.logianalytics.com/hc/en-us/articles/4405859425175-Embed-Cross-Visual-Link-Publish-and-Subscribe-Settings-Using-JavaScript).

## Radial Menu Changes

Use of the radial menu to apply cross-visual filters for cross-source links to other visuals in a dashboard has now been extended to also apply filters for same-source links, based on the publish and subscribe settings for the dashboard and its visuals. If a visual subscribes to a link field, a radial menu filter (cross-visual filter) for the field from a different visual in the same dashboard will also be applied to the first visual. For example, if Visuals A and B are both subscribed to a link for field Z, and you use the radial menu to apply a filter for field Z on Visual B, the filter will also be applied to Visual A.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Unlike row-level filters, cross-visual filters are not saved with the visual.

In addition, the **Filter** option on the radial menu is only available when the visual publishes a link for the field it is also using for its visual grouping. It is *not* available if the published cross-visual links for the visual are muted. See [*Mute a Published Link*](https://devnet.logianalytics.com/hc/en-us/articles/4405851129495-Mute-a-Published-Link).

See [*Use the Radial Menu*](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu).

## Cross-Source Link Changes

The cross-source links dialog has changed in this release. It is now available on a tab in the new Dashboard Interactions dialog that is also used to specify dashboard visual interaction controls. In addition, cross-source links can now be published and subscribed using the new dashboard link controls. See [*Use Cross-Source Links*](https://devnet.logianalytics.com/hc/en-us/articles/4405850967575-Use-Cross-Source-Links).

## Filter Changes

Cross-visual filters that have been applied from same-source and cross-source links are now listed separately on the Filters sidebar from filters that are applied from the Filters sidebar. In addition, you can now view them from a drop-down dialog when you select the filter icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406743754263/filter-vis.png)) on the visual.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Cross-visual filters are not saved when filters are saved for a visual. Saved filters only include row-level filters for the visual.

See [*Filter Data*](https://devnet.logianalytics.com/hc/en-us/articles/4405851066519-Filter-Data).

## Arc Gauge Changes

The following changes have been made to arc gauges in this release:

* The maximum value for the arc gauge can now be determined by a second metric. In other words, you can now plot a metric on an arc gauge as it relates to a second metric. In past releases, only the minimum and maximum values of the arc gauge metric could be used. A new **Static maximum value** switch has been added to the Rulers sidebar for arc gauges that you can use to specify whether or not a second metric is used. If the switch is off, you can select a second metric to use. For example, if the arc metric was the number of apples, you might select a second metric representing the total number of fruit. In this way, the arc gauge would plot the total number of apples as it relates to the total number of fruit.
* A new **Show Label Description** switch has been added to the Rulers sidebar for arc gauge. Use this switch to display a description for the label on the gauge. The label shows the value that is plotted, but the label description shows the calculation for the plotted value in the format `<actual value>/<maximum value>`. If the **Static maximum value** switch is off and the **Show Label Description** switch is on, the label description includes the field names and values used to calculate the plotted value. By default, the label description is not shown.
* Percentages can now be used for the arc gauge metric range. The plotted value can be shown as a percentage of the maximum value. A new **Show as percentage** switch has been added to the Rulers sidebar for arc gauges that you can use to activate this.
* Multiple changes have been introduced for the metric that determines the color of the arc gauge.

  + You can determine the maximum value of the color metric based on a different metric. A new **Static maximum value** switch has been added to the Rulers sidebar for arc gauges that you can use to specify whether or not a different metric is used.
  + Percentages can now be used for the color rules of the color metric on the Color sidebar for the gauge, if the new **Show as percentage** switch has been switched on for the color metric.

See [*Arc Gauges*](https://devnet.logianalytics.com/hc/en-us/articles/4405851211287-Arc-Gauges).

## Table Enhancements

You can now specify the **Rows per Fetch** for an individual table. In past releases, this could be set at the data source level, but not for an individual table. See [*Change Table Pagination*](https://devnet.logianalytics.com/hc/en-us/articles/4405851239447-Change-Table-Pagination).

## Dashboard and Visual Export Changes

Several changes have been made to dashboard and visual exporting.

* The icon you select on the [dashboard icon bar](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar) and the [visual menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) has changed. You now select the ![](https://devnet.logianalytics.com/hc/article_attachments/4406743754519/dash-export.png) icon to export a dashboard or a visual.
* When you select PNG format for a dashboard export, the PNG file is generated and automatically downloaded. No intermediate panel and step are required.
* When you select PDF format for a dashboard or visual export, the Export As PDF dialog has been redesigned to match current Composer standards.

See [*Export a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405850982935-Export-a-Dashboard).

## Keyset Enhancements

The following enhancements were made to keysets in this release:

* You can now update the values of a keyset from a CSV file. See [*Update Keyset Values From a CSV File Using the UI*](https://devnet.logianalytics.com/hc/en-us/articles/4405859393687-Update-Keyset-Values-From-a-CSV-File-Using-the-UI).
* The keyset details panel that appears in the filters sidebar has been updated visually.

## Visual Data Cache Changes

Visuals with some dynamic time ranges can now be cached. In past releases, visuals with dynamic time range filters were never cached. Now the data for the following dynamic time ranges are cached:

* Previous Month, Previous Day, Previous Quarter, and Previous Year (these time ranges end in the past).
* Custom dynamic time ranges, that are in the past and are not based on current time (NOW time preset).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) Data is not cached for some dynamic time ranges such as Previous Hour and Previous Minute because these time ranges are too small to be used.

See [*Preset Time Ranges*](https://devnet.logianalytics.com/hc/en-us/articles/4405851144983-Preset-Time-Ranges).

## Query Engine Enhancements

The INFO-level messages logged by the query engine have been enhanced to include more information about the request execution. The topology type, response type, response size, and connector requests are now included.

## User Interface Changes

The following changes were made to the user interface in this release:

* A new icon (![](https://devnet.logianalytics.com/hc/article_attachments/4406743754775/dash-interact.png)) is now added to visuals when they are subscribed to a dashboard cross-source or same-source link filter.
* The cross-source links dialog has changed in this release. It is now available on a tab in the new Dashboard Interactions dialog that is also used to specify dashboard visual interaction controls.
* The keyset details panel that appears in the filters sidebar has been updated visually.
* Cross-visual filters that have been applied from same-source and cross-source links are now listed separately on the Filters sidebar from filters that are applied from the Filters sidebar.
* The Export As PDF dialog has been redesigned to Composer's current standards. This dialog appears when you export a dashboard or visual. In addition, the icon you select to export a dashboard or visual has changed.
* All dashboard, visual, visual gallery, and dashboard library warning dialogs have been updated to a new style.
