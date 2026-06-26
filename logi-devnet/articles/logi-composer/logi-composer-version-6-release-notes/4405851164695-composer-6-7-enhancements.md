---
title: "Composer 6.7 Enhancements"
id: 4405851164695
section: "Logi Composer Version 6 Release Notes"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851164695-Composer-6-7-Enhancements
updated_at: 2022-04-25T15:19:14Z
---

# Composer 6.7 Enhancements

# Composer 6.7 Enhancements

This topic describes the significant enhancements in Composer 6.6.

* [*Permission Changes*](#Permissions)
* [*Connector Updates*](#Connector)
* [*New Dashboard Interactivity*](#Dashint)
* [*Visual Interactivity Changes*](#VisualInt)
* [*Embedded Dashboard Changes*](#Embedded)
* [*New Combo Chart Visual*](#Combo)
* [*Arc Gauge Changes*](#Arc)
* [*Keyset Enhancements*](#Keyset)
* [*New Embedded Visual Authoring*](#Visbuild)
* [*New Quarter Granularity Option*](#quarter)
* [*Fused Data Source Changes*](#Fused)
* [*Distinct Value Updates*](#Distinct)
* [*Radial Menu Updates*](#Radial)
* [*User Interface Changes*](#User)

## Permission Changes

The following read, write, and delete permission changes were made in this release.

* Data source and dashboard permissions have some additional restrictions added in this release. If your user account belongs to a group that has been granted the **Can Manage Dashboard Permissions** or **Can Manage Source Permissions**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference), you now can only assign dashboard or data source permissions equivalent to your own. For example, if your user account has read permission for a dashboard, you can grant and revoke the read option available on the Dashboard Permissions panel. If you have write permission for a data source, you can grant and revoke the write option on the Source Permissions panel.

  ![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg) If your user account belongs to a group that has been granted the **Can Administer Dashboards** or **Can Administer Sources** [privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference), you can grant and revoke all options on the Dashboard Permissions or the Source Permissions panels. Also, if your user account does not have read permission for a dashboard or data source, you cannot see the dashboard or data source on the Library or Sources page.

  See [*About Dashboard Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859259159-About-Dashboard-Permissions) and [*About Data Source Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions).
* Read, write, and delete permissions for a visual are now controlled by the permissions assigned the data source used by the visual in combination with the user's group [privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference). The creator of a visual is automatically granted read, write, and delete permissions for the visual in the Visual Gallery. When they are removed from the system, the supervisor is assigned ownership for the visual.

## Connector Updates

The MongoDB connector now supports MongoDB versions up to 4.4. In past releases, it only supported MongoDB versions up to 4.2. See [*Manage the MongoDB Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405850957591-Manage-the-MongoDB-Connector).

## New Dashboard Interactivity

This release introduces new dashboard interactivity settings you can use to control how users can interact with a dashboard. When a dashboard is embedded, dashboard interactivity settings are used to control how the user interacts with the embedded dashboard.

A new Dashboard Interactivity panel has been introduced in the UI. It contains two tabs: **Dashboard** and **Visuals**.

* Use the **Dashboard** tab to control whether users can change the layout, add visuals to the dashboard, delete the dashboard, save the dashboard, filter the dashboard, rename the dashboard, add the dashboard to favorites, set up or change dashboard links, set up or change cross-source links, refresh the dashboard, export the dashboard to PNG or PDF format, or export the dashboard configuration.
* Use the **Visuals** tab to override the [individual visual interactivity settings](https://devnet.logianalytics.com/hc/en-us/articles/4405859573143-Control-How-Users-Interact-With-a-Visual) for all visuals in this dashboard. This tab includes a switch called **Override Visual Interactivity**. When the switch is turned on, the individual visual interactivity settings for each visual on the dashboard are overridden and ignored. Instead, the visual interactivity settings set for the dashboard are used for all of the visuals in the dashboard.

  These settings are only applied to the visuals when they are used in this dashboard and not universally. The interactivity settings for the visuals themselves are not affected when used elsewhere. In other words, if a visual is used in one dashboard (Dashboard A) with **Override Visual Interactivity** turned on and is also used in a second dashboard (Dashboard B) with **Override Visual Interactivity** turned off, the individual visual interactivity settings are not honored in Dashboard A, but are honored in Dashboard B.

A **Preview Interactivity Settings** switch allows you to test the dashboard and visual interactivity settings on the dashboard. When this switch is turned on, the dashboard and visuals behave as they will when the dashboard is embedded, based on the dashboard and visual interactivity settings. The visual interactivity behavior may be set by the visual itself or by the dashboard interactivity override settings for all visuals on the dashboard. The **Preview Interactivity Settings** switch is a temporary switch: by default it is off each time you access the dashboard. It is not saved with the dashboard; so if you turn it on and save the dashboard, it will still be off the next time you edit the dashboard.

When you save a dashboard (Save option), the dashboard interactivity settings are also saved (if there are any). If there are no dashboard interactivity settings or if they have not been changed, they are not saved. When you save a dashboard with a new name (Save As option), the dashboard interactivity settings are saved to the new dashboard, but the interactivity settings for the original dashboard remain unchanged.

For complete information about the Dashboard Interactivity panel, see [*Control How Users Interact With a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405859265303-Control-How-Users-Interact-With-a-Dashboard).

Dashboard interactivity settings are exported with other dashboard settings when you export the dashboard to a JSON file. This ensures that the exported dashboard can be imported with the same interactivity profile. See [*Export a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405850982935-Export-a-Dashboard).

Several new properties for the Javascript `createComponent` method used to embed dashboards have been added in this release to support dashboard interactivity. In addition, the mode property is deprecated in this release. See [*Embedded Dashboard Changes*](#Embedded).

Finally, new API endpoints were introduced and others were altered to support dashboard interactivity. See [*API Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405859449111-Logi-Composer-Version-6-Release-Notes#API).

## Visual Interactivity Changes

With the introduction of dashboard interactivity, visual interactivity has been removed from the visual sidebar menu when you edit a visual in a dashboard. Visual interactivity settings are still available for visuals when you edit the visual in the Visual Gallery. See [*Control How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405859573143-Control-How-Users-Interact-With-a-Visual). This was done to eliminate confusion between the visual interactivity settings set for an individual visual and the visual interactivity override settings set in dashboard interactivity settings.

In addition, a new **Preview Interactivity Settings** switch allows you to test the visual interactivity settings when you edit visual interactivity in the Visual Gallery. When this switch is turned on, the visual behaves as it will when the visual is embedded, based on its interactivity settings. The **Preview Interactivity Settings** switch is a temporary switch: by default it is off each time you access the visual. It is not saved with the visual; so if you turn it on and save the visual, it will still be off the next time you edit the visual.

## Embedded Dashboard Changes

Embedded dashboards can now be controlled by dashboard interactivity settings. See [*Control How Users Interact With a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405859265303-Control-How-Users-Interact-With-a-Dashboard) and [*New Dashboard Interactivity*](#Dashint).

Several new properties and a new object for the Javascript `createComponent` method used to embed dashboards have been added in this release to support dashboard interactivity.

* A new `interactivityOverrides` object allows you to set interactivity settings for a dashboard in the Javascript. See [*Interactivity Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405851049623-Supported-Interactivity-Properties).
* A new `interactivityProfileName` property provides the interactivity profile name for the embedded dashboard. If the profile specified does not exist, the dashboard is embedded with the default system interactivity profile. If this parameter is not specified, the dashboard is embedded with a linked interactivity profile. When an interactivity profile is specified, any `mode` parameter specified for the `createComponent` method is ignored. See [*Embedded Dashboard Properties and Objects*](https://devnet.logianalytics.com/hc/en-us/articles/4405851050647-Supported-Embedded-Dashboard-Properties-and-Objects).

In addition, the `mode` property is deprecated in this release. See [*Embedded Dashboard Properties and Objects*](https://devnet.logianalytics.com/hc/en-us/articles/4405851050647-Supported-Embedded-Dashboard-Properties-and-Objects).

## New Embedded Visual Authoring

This releases introduces the ability to embed Composer's visual authoring experience in your applications using JavaScript. This allows your users to add and maintain the visuals embedded in a dashboard. Restrictions that control what a user can do using the embedded visual authoring experience is described in [*Embedded Composer Component Controls*](https://devnet.logianalytics.com/hc/en-us/articles/4405851048727-Embedded-Composer-Component-Controls).

In support of embedded visual authoring, the following enhancements were made.

* A new `visual-builder` parameter value is now supported for the `createComponent` method of the `EmbedManager` class. When `visual-builder` is specified, a new set of visual authoring properties for the visual authoring experience must be specified.

  In addition, the `removeComponent` and `refreshComponent` methods support visual authoring component IDs and can be used to remove and refresh visual authoring instances. See [*EmbedManager Methods*](https://devnet.logianalytics.com/hc/en-us/articles/4405859341847-Supported-EmbedManager-Methods).
* New visual authoring properties have been added to the `createComponent` method. They allow you to specify settings for an embedded visual authoring instance. See [*Embedded Visual Authoring Properties and Objects*](https://devnet.logianalytics.com/hc/en-us/articles/4405851051543-Supported-Embedded-Visual-Authoring-Properties-and-Objects).
* New Composer embedded events have been added that you can use in your JavaScript to better tailor how visual authoring behaves in your application. See [*Embedded Events*](https://devnet.logianalytics.com/hc/en-us/articles/4405851052695-Supported-Composer-v6-Embedded-Events).

![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg)Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) for all embed-related workflows.

For complete information about embedding visual authoring, see [*Embed Composer Components Into Your Application*](https://devnet.logianalytics.com/hc/en-us/articles/4405859263895-Embed-Composer-Components-Into-Your-Application). A JavaScript example embedding a visual authoring instance is provided in [*Embedded Visual Authoring JavaScript Example*](https://devnet.logianalytics.com/hc/en-us/articles/4405851054615-Embedded-Visual-Authoring-JavaScript-Example).

## New Combo Chart Visual

A new combo chart visual has been added to Composer in this release. Combo charts are based on a single independent variable (usually the x-axis) and up to four dependent variables (usually the y-axes). The dependent variables can be plotted using either bar or line visual styles.

In addition, a new style of legend has been introduced for combo charts; the legend used by other visuals is not supported on combo charts. The new legend is interactive, allowing you to show or hide different plots on the chart. See [*Combo Charts*](https://devnet.logianalytics.com/hc/en-us/articles/4405851217047-Combo-Charts).

## Arc Gauge Changes

You can now specify the minimum and maximum values of the metric that determines the color of the arc gauge on the Rulers sidebar. In past versions, this was not possible. See [*Adjust Arc Gauge Color Metric Value Range*](https://devnet.logianalytics.com/hc/en-us/articles/4405851211287-Arc-Gauges#ColorMax).

## Keyset Enhancements

The following enhancements were made to keysets in this release:

* A Composer user assigned to a group with **Can Administer Dashboard**[privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) can now remove keysets they did not create. In past releases, this was not possible. Other users still can only remove keysets they created.
* A new **Upload Keyset Values** button on the Keyset tab of the Filters sidebar allows you to select a CSV file containing keyset values and save the value list with a new keyset name. The CSV file must be a single-column, UTF-8-formatted CSV file with a maximum size of 1000 rows. See [*Create a Keyset From a CSV File*](https://devnet.logianalytics.com/hc/en-us/articles/4405859388567-Create-a-Keyset-From-a-CSV-File).

## New Quarter Granularity Option

In past releases, you could group data that included a date by millisecond, second, minute, hour, day, week, month or year. This release introduces the ability to group data by quarter. This change affects the granularity options available to you in the user interface and when using the API, including the Fields tab of your data source configuration and in the default settings for visuals in the data source configuration.

## Fused Data Source Changes

Text fields can now be joined in fused data sources. See [*Fuse Data Sources*](https://devnet.logianalytics.com/hc/en-us/articles/4405851072279-Fuse-Data-Sources).

## Distinct Value Updates

When custom ranges or list values are requested for a field, full data scans are no longer performed. See [*Fast Distinct Values*](https://devnet.logianalytics.com/hc/en-us/articles/4405850912279-Fast-Distinct-Values).

## Radial Menu Updates

Null values can now be removed from a visual using the radial menu **Remove** option. See [*Use the Radial Menu*](https://devnet.logianalytics.com/hc/en-us/articles/4405859536151-Use-the-Radial-Menu)

## User Interface Changes

The following changes were made to the user interface in this release:

* The dashboard icon bar has changed. Cross-source links now have their own icon option and have been split out from dashboard linking. In past versions, when you selected the ![](https://devnet.logianalytics.com/hc/article_attachments/4409070300567/dash-link.png) icon on the dashboard icon bar, you could select dashboard linking or cross-source linking. Now each option has its own icon on the icon bar. Use the ![](https://devnet.logianalytics.com/hc/article_attachments/4409070300567/dash-link.png) icon to perform [dashboard linking](https://devnet.logianalytics.com/hc/en-us/articles/4405859277463-Link-a-Dashboard). Use a new ![](https://devnet.logianalytics.com/hc/article_attachments/4409054856983/dash-xsourcelink.png) dashboard icon to perform [cross-source linking](https://devnet.logianalytics.com/hc/en-us/articles/4405850967575-Use-Cross-Source-Links). See [*Use the Dashboard Icon Bar*](https://devnet.logianalytics.com/hc/en-us/articles/4405850991127-Use-the-Dashboard-Icon-Bar).
* A new Dashboard Interactivity panel has been introduced in the UI to support dashboard interactivity. See [*Control How Users Interact With a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405859265303-Control-How-Users-Interact-With-a-Dashboard).
* With the introduction of dashboard interactivity, visual interactivity has been removed from the visual sidebar menu when you edit a visual in a dashboard. Visual interactivity settings are still available for visuals when you edit the visual in the Visual Gallery. See [*Visual Interactivity Changes*](#VisualInt).
* A new **Preview Interactivity Settings** switch allows you to test the visual interactivity settings when you edit visual interactivity in the Visual Gallery. See [*Visual Interactivity Changes*](#VisualInt).
* A new **Upload Keyset Values** button on the Keyset tab of the Filters sidebar allows you to select a CSV file containing keyset values and save the value list with a new keyset name. See [*Create a Keyset From a CSV File*](https://devnet.logianalytics.com/hc/en-us/articles/4405859388567-Create-a-Keyset-From-a-CSV-File).
* You can now edit a visual when it has been maximized in a dashboard. See [*Edit Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4405859570839-Edit-Visuals).
