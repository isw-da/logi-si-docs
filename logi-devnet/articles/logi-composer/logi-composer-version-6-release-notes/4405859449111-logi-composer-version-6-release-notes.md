---
title: "Logi Composer Version 6 Release Notes"
id: 4405859449111
section: "Logi Composer Version 6 Release Notes"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859449111-Logi-Composer-Version-6-Release-Notes
updated_at: 2022-11-28T17:38:44Z
---

# Logi Composer Version 6 Release Notes

# Logi Composer Version 6 Release Notes

This topic describes feature enhancements, resolved issues, and important information for Composer 6.

To purchase this product, contact [US Sales](mailto:salesteam@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "US Sales email address.") or [UK Sales](mailto:emea_sales@logianalytics.com?subject=I%20am%20interested%20in%20purchasing%20this%20product.%20Please%20contact%20me. "Email address for UK sales team.").

* [*Important Notices*](#Importan)
* [*Feature Enhancements*](#Feature)
* [*API Updates*](#API)
* [*Resolved Issues*](#Resolved)
* [*Deprecated Features*](#Deprecat)
* [*Removed Features*](#Removed)

To review a summary of the major changes made from Composer 5 to Composer 6, see [*Logi Composer Version 6 Summary of Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851159959-Logi-Composer-Version-6-Summary-of-Changes).

### Log4j and Log4net Vulnerabilities Update

In the second week of December 2021, a Log4j vulnerability was announced that may affect some customers using our products. Resolving/mitigating this issue is a high priority! We will continue to issue information to help you with this vulnerability. For more information see [*Statement on Log4j and Log4net Vulnerabilities*](https://devnet.logianalytics.com/hc/en-us/articles/4415781801751-Statement-on-Log4j-and-Log4net-Vulnerabilities).

## Important Notices

![](https://devnet.logianalytics.com/hc/article_attachments/4409070299415/criticalicon.gif) Support for Composer 5.9 ends on June 27, 2022. Composer 6.9 will soon enter the Passive Support phase. Our Passive Support release receives only critical patches and security updates until its end-of-life date. We describe critical patches in the Passive Support Release Notes page at the discretion of Product Management. Security updates are not applicable to the third-party dependencies. If you are using Composer 5.9, you should contact [Sales](mailto:salesteam@logianalytics.com?subject=Upgrading%20Composer) and upgrade to the most current LTS release. We no longer publish documentation for any Composer products prior to version 6.9. Contact [Customer Support](https://devnet.logianalytics.com/hc/en-us/requests/new) if you need content for an unsupported release.

![](https://devnet.logianalytics.com/hc/article_attachments/4409070299415/criticalicon.gif)**IMPORTANT:** Older license keys are not compatible with Composer 6.9. If you are upgrading from any older Composer or Zoomdata release, a new license must be requested. See [*Request and Apply a New License Key*](https://devnet.logianalytics.com/hc/en-us/articles/4405851108247-Request-and-Apply-a-New-License-Key).

![](https://devnet.logianalytics.com/hc/article_attachments/4409070299415/criticalicon.gif) Support for Zoomdata 4.9 will end on September 25, 2021. With the release of Composer 6.9 LTS, Zoomdata 4.9 entered Passive Support. Our LTS Passive Support release receives only critical patches and security updates until its end-of-life date. Security updates are not applicable to the third-party dependencies. We encourage you to migrate to our most current LTS release. The documentation for the LTS Passive Support release is updated only when necessary. If there are changes to existing functionality or workarounds that you need to be aware of, you can find the information you need in the Release Notes.

For more information about the supported Logi Composer and Logi Zoomdata releases, see [*Logi Composer (Zoomdata) Release Vehicles*](https://devnet.logianalytics.com/hc/en-us/articles/4405851109143-Logi-Composer-Zoomdata-Release-Vehicles).

#### Upgrade and Migration Considerations

* In general, you can upgrade directly to the latest version of Composer from a prior version.
* If you are upgrading to a newer version of Composer and you also want to change your encryption mode, perform the upgrade first and then complete the steps described in [*Change the Encryption Mode*](https://devnet.logianalytics.com/hc/en-us/articles/4405859459351-Change-the-Encryption-Mode).
* Manually upgrading Composer no longer provides the Java Runtime Environment (JRE) needed for Composer to start. Make sure you have Java 11.0.5 or later installed before you manually install or manually upgrade to Composer 5.8 or later. If you do not, Composer will not start.

For information about Composer's end-of-life policy for third-party software, see [*Composer's Third-Party End-of-Life Policy*](https://devnet.logianalytics.com/hc/en-us/articles/4405859458071-Composer-s-Third-Party-End-of-Life-Policy).

[![](https://devnet.logianalytics.com/hc/article_attachments/4409070301079/totop.png)Back to top](#top "Click to go to the top")

## Feature Enhancements

| Title | Description |
| --- | --- |
| **6.9.29 Enhancements** | |
| None. |  |
| **6.9.28 Enhancements** | |
| None. |  |
| **6.9.27 Enhancements** | |
| None. |  |
| **6.9.26 Enhancements** | |
| None. |  |
| **6.9.25 Enhancements** | |
| None. |  |
| **6.9.24 Enhancements** | |
| None. |  |
| **6.9.23 Enhancements** | |
| None. |  |
| **6.9.22 Enhancements** | |
| None. |  |
| **6.9.21 Enhancements** | |
| None. |  |
| **6.9.20 Enhancements** | |
| None. |  |
| **6.9.19 Enhancements** | |
| [Extended OpenStreetMap Support](https://devnet.logianalytics.com/hc/en-us/articles/5667569640471) | You can now create map visuals using a custom URL that points to a local or other specific instance of OpenStreetMap. Enter the URL in the **Provider URL** field, available after selecting OpenStreetMap as the Tile Provider for a visual in Composer. |
| **6.9.18 Enhancements** | |
| None. |  |
| **6.9.17 Enhancements** | |
| [Time Bar](https://devnet.logianalytics.com/hc/en-us/articles/5152308220695#time-bar) | The time bar and Data Details work area in Composer now display time at the same level of granularity you define for your visual at the source level. |
| [Loading Times](https://devnet.logianalytics.com/hc/en-us/articles/5152308220695#loading-times) | Composer now returns lists of users more efficiently when called in the user interface or using the API. User Name and User ID information are provided: select an individual user to return that user’s full information. |
| **6.9.16 Enhancements** | |
| None. |  |
| **6.9.15 Enhancements** | |
| [Modified Date Display](https://devnet.logianalytics.com/hc/en-us/articles/4421572928535#date) | Composer now displays the modified date and time for sources, visuals, and dashboards in your local date and time. |
| **6.9.14 Enhancements** | |
| None. |  |
| **6.9.13 Enhancements** | |
| None. |  |
| **6.9.12 Enhancements** | |
| None. |  |
| **6.9.11 Enhancements** | |
| None. |  |
| **6.9.10 Enhancements** | |
| [Null/Zero Conversion for KPI Charts](https://devnet.logianalytics.com/hc/en-us/articles/4414070304663-Composer-6-9-10-Enhancements) | A new toggle "Display Null as Zero" is now available for KPI Charts, enabling you to change the display from 'Null' to '0' in cases where there is no data. |
| **6.9.9 Enhancements** | |
| None. |  |
| **6.9.8 Enhancements** | |
| None. |  |
| **6.9.7 Enhancements** | |
| None. |  |
| **6.9.6 Enhancements** | |
| None. |  |
| **6.9.5 Enhancements** | |
| Keyset Exclude Filter with CSV Upload | You can now exclude keyset values uploaded via CSV files in your filter. |
| **6.9.4 Enhancements** | |
| None. |  |
| **6.9.3 Enhancements** | |
| [*Dashboard Import Overwrite Permission Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405851166615-Composer-6-9-3-Enhancements#DashImport) | The overwrite policy behavior for imported dashboards now honors the write permissions for all the dashboard components: the dashboard itself, its visuals, and the data sources used by its visuals. |
| **6.9.2 Enhancements** | |
| [*Custom Metric Date and Time Aggregation Function Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859456535-Composer-6-9-2-Enhancements#CustomMetrics) | Custom metrics now support the `now()` and `time_add` functions used by row-level expressions. The original custom metric `DATE()`, `DateADD`, and `DateSUB` functions still work but should no longer be used. They are deprecated in this release and will be removed in a future release. Instead, use the `now()` and `time_add` functions. |
| [*Dashboard Import Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859456535-Composer-6-9-2-Enhancements#DashImport) | You can now use the API to import a dashboard using a new overwrite policy, so that dashboards with the same name are overwritten instead of being imported with a slightly altered name. |
| **6.9.1 Enhancements** | |
| None. |  |
| **6.9 Enhancements** | |
| [*License Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#License) | This release implements a new license file structure.  **IMPORTANT:** Older license keys are not compatible with Composer 6.9. If you are upgrading from any older Composer or Zoomdata release, a new license must be requested.  See [*Request and Apply a New License Key*](https://devnet.logianalytics.com/hc/en-us/articles/4405851108247-Request-and-Apply-a-New-License-Key). |
| [*Authorization Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#Auth) | Two new privileges, **Can Create Visuals** and **Can Manage Visual Permissions** are introduced in this release to support the updates made for visual permissions.  If a user is granted the **Can Administer Visuals** privilege, they are now automatically granted both the **Can Create Visuals** and **Can Manage Visual Permissions** privileges as well.  A non-administrative user must have the **Can Create Visuals** or **Can Administer Visuals** [group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) to add a visual.  Finally, a non-administrative user must also have the **Can Create Visuals** (or **Can Administer Visuals** [group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) to import a dashboard. In prior releases, they only needed the **Can Create new Data Sources** and **Can Create Dashboards** [group privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference). |
| [*Security Key Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#Security) | Security keys are deprecated in this release and will be removed from the product in a future release. Use Trusted Access instead for all embedded workflows. See [*Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access).  However, while Composer still supports security keys, it's previous method of authorizing the use of visuals using new security keys changed due to the introduction of visual permissions in this release. |
| [*Connector Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#Connector) | The Elasticsearch 6 connector now supports Elasticsearch versions up to 6.8. In past Composer releases, the maximum supported Elasticsearch 6 version was 6.7. |
| The Elasticsearch 7 connector now supports Elasticsearch versions up to 7.12. In past Composer releases, the maximum supported Elasticsearch 7 version was 7.6. |
| The MySQL connector now supports MySQL versions 5.6 through 8.0. In past Composer releases, the only supported MySQL version was 5.6. |
| [*New Visual Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#VisPerm) | This release introduces visual permissions. Visual permissions allow you to permit your entire account, groups within your account, or users within your account to read, write, or delete a visual. This allows you to share a visual with other users. API updates have been made to support this new functionality. See [*API Updates*](#API). |
| In past releases, if a user had Read permissions for a data source, they also had Read permission to any visuals created using the data source. However, with the introduction of visual permissions in this release, this is no longer true. With this release, authorization for visuals is now controlled by visual permissions. |
| [*Dashboard Save Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#DashboardSave) | Saving dashboards has changed to support visual permissions. |
| The Save and Save As options that were available from a drop-down menu off of the dashboard icon bar have been separated. With this release, two icons on the dashboard icon bar are now provided: one for Save and one for Save As. |
| Dashboard save processing and dashboard copy processing have been improved and the Save Options and the Save As Options dialogs have changed to reflect the improvements. |
| Pre-existing visuals are no longer automatically saved when you save a dashboard (new visuals are automatically saved). You must explicitly elect to save pre-existing visuals on the dashboard Save Options dialog. |
| [*Dashboard Link Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#DashboardLink) | Dashboard link information is no longer stored with visual definitions, but with the dashboard definitions. When you upgrade to Composer 6.9, the dashboard link information is automatically upgraded for you. |
| [*Dashboard Javascript Embed Update*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#Embed) | A new `composer-dashboard-failed` event has been added to the product and can be used in your Javascript embed code to control what happens when a dashboard fails to load. |
| [*New Dashboard Interactivity Setting*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#InteractDash) | A new dashboard interactivity setting is introduced in this release: **Share Filter Sets**. |
| [*Visual Save Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#VisualSave) | The option to **Save** a visual with its current name has been removed from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu). Instead, the  icon appears at the top of visuals that need to be saved. This icon allows you to save the visual with its current name. To save it using a new name, use the new **Save As** option. |
| [*New Visual Save As Support*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#VisualSaveAs) | A new **Save As** option on the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) when a visual is edited in a dashboard, a new  icon on the visual when edited in the Visual Gallery, and a new Save As Options dialog have been added. Use these to save a visual with a new visual name. The original visual still exists with its original name in the system. |
| [*Visual Name Uniqueness*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#VisualNameUnique) | Visual name uniqueness is now enforced with this release. |
| [*New List Filter Visual Style*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#List) | A new visual style called a list filter has been added to the product. A list filter visual can be used to list values of a data source field in a visual. You can select one or more of the field values in the list to quickly apply a filter to other visuals in the dashboard that subscribe to a [cross-visual filter](https://devnet.logianalytics.com/hc/en-us/articles/4405859431447-Control-How-Cross-Visual-Filters-Interact-in-a-Dashboard) for the field. |
| [*New Stacked Area Chart Options*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#Stacked) | New **Display as stacked** and **Stacking Style** options on [Line Trend: Attribute Value](https://devnet.logianalytics.com/hc/en-us/articles/4405859525143-Line-Trend-Attribute-Value-Charts) visuals allow you to create stacked area charts. |
| [*Table Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#Table) | If a table has been grouped, the options to export its raw or visual data are no longer available. You cannot export raw and visual table data after it has been grouped. |
| [*New Visual Interactivity Settings*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#Interactivity) | Three new visual interactivity settings are introduced in this release: **Maximize**, **Rename**, and **Show Time Bar Panel**. |
| [*Experimental Materialized View Enhancements*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#MatView) | You can now create materialized view definitions using the Composer UI. In past releases, they could only be created using the API. This is an experimental feature.  This is an experimental feature. |
| [*New Experimental Alerting API Functionality*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#Alerts) | This release introduces new API endpoints that you can use to alert your end users when a metric reaches a specified threshold.  This is an experimental feature. |
| [*Keyset Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405851165591-Composer-6-9-Enhancements#Keyset) | An error now displays when an attempt to upload keyset values uses a keyset upload file that contains more records than are allowed by the Composer environment configuration. |
| **6.8 Enhancements** | |
| [*Query Engine Enhancements*](https://devnet.logianalytics.com/hc/en-us/articles/4405859455383-Composer-6-8-Enhancements#QueryEngine) | The INFO-level messages logged by the query engine are enhanced to include more information about the request execution. |
| [*Visual Data Cache Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859455383-Composer-6-8-Enhancements#VisDataCache) | Visuals with some dynamic time ranges can now be cached. In past releases, visuals with dynamic time range filters were never cached. |
| [*Authorization Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859455383-Composer-6-8-Enhancements#Auth) | Groups can no longer be transferred to a different account using the API. |
| [*New Dashboard Cross-Visual Filtering Controls*](https://devnet.logianalytics.com/hc/en-us/articles/4405859455383-Composer-6-8-Enhancements#Dashboard) | New dashboard cross-visual filtering controls are introduced in this release. You can now specify which cross-visual filter each dashboard visual publishes (which link fields it can apply cross-visual filtering for) and which cross-visual filter each visual subscribes to (which cross-visual filters can be applied to the visual). Cross-visual filters are filters created using same-source and cross-source link fields established in the dashboard.  Custom charts support cross-visual filtering controls if the chart supports the radial menu and filtering and if the appropriate publish and subscribe controls are enabled.  Cross-visual link publish and subscribe settings for a dashboard can be specified for embedded dashboards using JavaScript. Two JavaScript methods are provided with the `Zoomdata` object: `publish` and `subscribe`. |
| [*Radial Menu Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859455383-Composer-6-8-Enhancements#Radial) | Use of the radial menu to apply cross-visual filters for cross-source links to other visuals in a dashboard has now been extended to also apply filters for same-source links, based on the publish and subscribe settings for the dashboard and its visuals. |
| [*Cross-Source Link Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859455383-Composer-6-8-Enhancements#xSource) | The cross-source links dialog has changed in this release. In addition, cross-source links can now be published and subscribed using the new dashboard link controls. |
| [*Filter Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859455383-Composer-6-8-Enhancements#Filter) | Cross-visual filters that are applied from same-source and cross-source links are now listed separately on the Filters sidebar from filters that are applied from the Filters sidebar. In addition, you can now view them from a drop-down dialog when you select the filter icon () on the visual. |
| [*API Updates*](#API) | The Composer API specification is now generated in OpenAPI 3.0 format. |
| [*Arc Gauge Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859455383-Composer-6-8-Enhancements#Arc) | The maximum value for the arc gauge can now be determined by a second metric. A new **Static maximum value** switch is added to the Rulers sidebar for arc gauges that you can use to specify whether or not a second metric is used. |
| A new **Show Label Description** switch is added to the Rulers sidebar for arc gauge. Use this switch to display a description for the label on the gauge. |
| Percentages can now be used for the arc gauge metric range. A new **Show as percentage** switch is added to the Rulers sidebar for arc gauges that you can use to activate this. |
| You can now determine the maximum value of the color metric based on a different metric. A new **Static maximum value** switch is added to the Rulers sidebar for arc gauges that you can use to specify whether or not a second metric is used. |
| Percentages can now be used for the color rules of the color metric on the Color sidebar for the gauge, if the new **Show as percentage** switch is switched on for the color metric. |
| [*Table Enhancements*](https://devnet.logianalytics.com/hc/en-us/articles/4405859455383-Composer-6-8-Enhancements#Table) | You can now specify the **Rows per Fetch** for an individual table. In past releases, this could be set at the data source level, but not for an individual table. |
| [*Dashboard and Visual Export Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859455383-Composer-6-8-Enhancements#Export-Dash) | The icon you select to export a dashboard or a visual has changed and the Export As PDF dialog is redesigned. In addition, when you export a dashboard to a PNG file, the PNG file is created and downloaded without an intermediate step. |
| [*Keyset Enhancements*](https://devnet.logianalytics.com/hc/en-us/articles/4405859455383-Composer-6-8-Enhancements#Keyset) | You can now update the values of a keyset from a CSV file. |
| The keyset details panel that appears in the filters sidebar is updated visually. |
| [*User Interface Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859455383-Composer-6-8-Enhancements#User) | A new icon () is now added to visuals when they are subscribed to a dashboard cross-source or same-source link filter. |
| The cross-source links dialog has changed in this release. It is now available on a tab in the new Dashboard Interactions dialog that is also used to specify dashboard visual interaction controls. |
| Cross-visual filters that are applied from same-source and cross-source links are now listed separately on the Filters sidebar from filters that are applied from the Filters sidebar. |
| The Export As PDF dialog is redesigned to Composer's current standards. This dialog appears when you export a dashboard. In addition, the dashboard icon you select to export a dashboard has changed. |
| All dashboard, visual, visual gallery, and dashboard library warning dialogs are updated to a new style. |
| **6.7 Enhancements** | |
| [*Permission Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851164695-Composer-6-7-Enhancements#Permissions) | Data source and dashboard permissions have some additional restrictions added in this release. You now can only assign dashboard or data source permissions equivalent to your own. |
| Read, write, and delete permissions for a visual are now controlled by the permissions assigned the data source used by the visual in combination with the user's group [privileges](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference). The creator of a visual is automatically granted read, write, and delete for the visual in the Visual Gallery, but when they are removed from the system, the supervisor is assigned ownership for the visual. |
| [*Connector Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405851164695-Composer-6-7-Enhancements#Connector) | The MongoDB connector now supports MongoDB versions up to 4.4. |
| [*New Dashboard Interactivity*](https://devnet.logianalytics.com/hc/en-us/articles/4405851164695-Composer-6-7-Enhancements#Dashint) | This release introduces new dashboard interactivity settings you can use to control how users can interact with a dashboard after it is embedded. Dashboard interactivity settings allow you to control whether users can change the layout, add visuals to the dashboard, delete the dashboard, save the dashboard, filter the dashboard, rename the dashboard, add the dashboard to favorites, set up or change dashboard links, set up or change cross-source links, refresh the dashboard, export the dashboard to PNG or PDF format, or export the dashboard configuration. They also allow you to override the individual visual interactivity settings for the visuals in the dashboard. |
| [*Visual Interactivity Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851164695-Composer-6-7-Enhancements#VisualInt) | With the introduction of dashboard interactivity, visual interactivity is removed from the visual sidebar menu when you edit a visual in a dashboard. Visual interactivity settings are still available for visuals when you edit the visual in the Visual Gallery.  In addition, a new **Preview Interactivity Settings** switch allows you to test the visual interactivity settings when you edit visual interactivity in the Visual Gallery. |
| [*Embedded Dashboard Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851164695-Composer-6-7-Enhancements#Embedded) | Embedded dashboards can now be controlled by dashboard interactivity settings. Several new properties and a new object for the Javascript `createComponent` method used to embed dashboards are added in this release to support dashboard interactivity. |
| [*New Embedded Visual Authoring*](https://devnet.logianalytics.com/hc/en-us/articles/4405851164695-Composer-6-7-Enhancements#Visbuild) | This release introduces the ability to embed Composer's visual authoring experience in your applications using JavaScript. This allows your users to add and maintain the visuals embedded in a dashboard. |
| [*New Combo Chart Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405851164695-Composer-6-7-Enhancements#Combo) | A new combo chart visual is added to Composer in this release. In addition, a new interactive legend is introduced for combo charts; the legend used by other visuals is not supported. |
| [*Arc Gauge Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851164695-Composer-6-7-Enhancements#Arc) | You can now specify the minimum and maximum values of the metric that determines the color of the arc gauge on the Rulers sidebar. |
| The maximum value for the arc gauge can now be determined by a second metric. |
| Percentages can now be shown for an arc gauge metric. |
| You can determine the maximum value of the color metric based on a different metric. |
| Percentages can now be used for the color metric on the Rulers sidebar and used in the color rules for the metric on the Color sidebar for the gauge. |
| You can now view the raw values for the arc gauge metric and identify the metric used to determine the maximum value. |
| [*Keyset Enhancements*](https://devnet.logianalytics.com/hc/en-us/articles/4405851164695-Composer-6-7-Enhancements#Keyset) | An administrator can now remove keysets they did not create. |
| You can now upload a keyset from a CSV file using the API. See [*API Updates*](#API). |
| A new **Upload Keyset Values** button on the Keyset tab of the Filters sidebar allows you to select a CSV file containing keyset values and save the value list with a new keyset name. |
| [*New Quarter Granularity Option*](https://devnet.logianalytics.com/hc/en-us/articles/4405851164695-Composer-6-7-Enhancements#quarter) | This release introduces the quarter granularity option for date and time fields. |
| [*Fused Data Source Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851164695-Composer-6-7-Enhancements#Fused) | Text fields can now be joined in fused data sources. |
| [*Distinct Value Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405851164695-Composer-6-7-Enhancements#Distinct) | When custom ranges or list values are requested for a field, full data scans are no longer performed. |
| [*Radial Menu Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405851164695-Composer-6-7-Enhancements#Radial) | Null values can now be removed from a visual using the radial menu **Remove** option. |
| [*User Interface Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851164695-Composer-6-7-Enhancements#User) | The dashboard icon bar has changed. Cross-source links now have their own icon option and are split out from dashboard linking. |
| A new Dashboard Interactivity panel is introduced in the UI to support dashboard interactivity. |
| With the introduction of dashboard interactivity, visual interactivity is removed from the visual sidebar menu when you edit a visual in a dashboard. Visual interactivity settings are still available for visuals when you edit the visual in the Visual Gallery. |
| You can now edit a visual when it is maximized in a dashboard. |
| **6.6 Enhancements** | |
| [*Authorization Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859454231-Composer-6-6-Enhancements#Authoriz) | The group privilege **Can Manage Visuals** was renamed to **Can Administer Visuals** in this release. The corresponding API privilege **ROLE\_MANAGE\_VISUALS** was also renamed to **ROLE\_ADMINISTER\_VISUALS**. Customers who use the API to manage groups must manually make this change wherever **ROLE\_MANAGE\_VISUALS** is currently used; if you use the Composer user interface (UI) to manage groups, the change will happen automatically. |
| In addition, to alter and save an individual visual in a dashboard now, you must either be assigned to a group with the **Can Administer Visuals** (**ROLE\_ADMINISTER\_VISUALS**) privilege or be the creator of the visual. |
| [*Connector Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405859454231-Composer-6-6-Enhancements#Connecto) | The maximum version of Spark SQL data stores supported by the Composer Spark SQL connector is now version 3.0. |
| [*COALESCE Function Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859454231-Composer-6-6-Enhancements#COALESCE) | The [COALESCE function](https://devnet.logianalytics.com/hc/en-us/articles/4405851017239-Conditional-Functions) now supports aggregate metrics with complex calculations using arithmetic functions (for example `COALESCE(max(sales) * 1.3, 0)`), so a default value can be used if null values are returned. |
| [*Performance Improvements*](https://devnet.logianalytics.com/hc/en-us/articles/4405859454231-Composer-6-6-Enhancements#Performa) | Improved server start times by 15 percent. |
| [*User Interface Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859454231-Composer-6-6-Enhancements#User) | Labels on bar charts are upgraded to take into account the bar color as well as the background color of the UI. |
| Table data can now be aggregated by group field if the group field is not the first group field for the table and the data source indicates that the group field can be aggregated. |
| **6.5 Enhancements** | |
| [*New Trusted Access Authorization Introduced*](https://devnet.logianalytics.com/hc/en-us/articles/4405851163799-Composer-6-5-Enhancements#New) | Composer now provides its own security methodology that allows for machine-to-machine authorization of Composer resources when embedded in your application (the “parent” application). This is a form of “delegated” authorization where the parent application can determine, on demand, how and when to authorize any given embedded Composer component to an end-user logged into the parent application. This methodology is called *Trusted Access*.  Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) for all embed-related workflows. |
| [*Embedded Dashboard Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851163799-Composer-6-5-Enhancements#Embedded) | Significant changes were made to how dashboards can be embedded in your applications. Primarily, while your existing embedded dashboard HTML snippets will continue to work, this release introduces the ability to embed dashboards using JavaScript code. This is more powerful than the HTML script snippet provided in previous releases because it provides you with more tailoring options for the dashboards in your application.  Logi Analytics recommends using [Trusted Access](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) for all embed-related workflows. |
| [*User Interface Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851163799-Composer-6-5-Enhancements#User) | The Advanced options (**Root**, **Embed ID**, **Show Banner**, **Show Header**, **Show Logo**, **Show Title**, **Show Breadcrumbs**, and **Show Actions**) previously available on the Embed Code dialog that produces an embeddable HTML script snippet are removed. |
| The **OAUTH** option on the [Security page](https://devnet.logianalytics.com/hc/en-us/articles/4405859465111-Enable-Trusted-Access-and-OAuth-2-0) of the Supervisor UI is renamed **Trusted Access & OAUTH**. |
| **6.4 Enhancements** | |
| [*Raw Data Table Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851162903-Composer-6-4-Enhancements#Raw) | Multiple changes were made to raw data tables, including:   * UI references to "raw data tables" or "raw data table" are changed to simply "tables" or "table." * A context menu is added to table column headings. * You can now group tables. * You can aggregate metrics in a table. * You can set even time intervals in a table. * You can alter the granularity of a time field in a table. |
| [*Data Source Configuration Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851162903-Composer-6-4-Enhancements#Data) | A new "Data Unavailable" message now appears when an error occurs obtaining data from a data source for a row security filter. In addition, if a row security filter returns no results, a new "No search results" message appears. |
| The default settings available for tables in a data source configuration have changed. |
| [*Caching Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851162903-Composer-6-4-Enhancements#Caching) | A new metadata cache to cache field statistics and improve overall metadata caching performance is introduced. |
| **6.3 Enhancements** | |
| [*Installation Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859452695-Composer-6-3-Enhancements#Installa) | CentOS 6 is no longer supported and the special installation Bootstrap procedure (`bootstrap-zoomdata-centos6.run`) is no longer provided with this product. CentOS 6 is no longer supported by Red Hat Linux (RHEL). Use CentOS 7 or 8 instead. |
| Red Hat Linux 6 and Scientific Linux are no longer supported. |
| [*Rebranding Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405859452695-Composer-6-3-Enhancements#Migratio) | The `Content-Type` header `vnd.zoomdata.v2+json` is no longer supported in version 5.9.1 and later and can no longer be used as the `Content-Type` for API routes. It is removed from the product. Use `vnd.composer.v2+json` as the `Content-Type` for API routes instead. |
| [*Custom Chart CLI Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859452695-Composer-6-3-Enhancements#Custom) | A new version 5 of the custom chart CLI is introduced in this release. |
| [*Elasticsearch Connector Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859452695-Composer-6-3-Enhancements#Elastics) | Support for Composer Elasticsearch 6 and 7 indices with a disabled `_source` field or with a `_source` field with exclusions is introduced. In past releases, only Elasticsearch data stores with the `_source` field enabled and with no exclusions were supported. |
| A new `elasticsearch.inner-hits.size property` is introduced for Elasticsearch 6 and 7 connectors. |
| [*Data Source Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859452695-Composer-6-3-Enhancements#Data) | This release introduces source permissions, the ability to permit your account or specific groups or users in your account to read, write, or delete a data source configuration.  As a result of the introduction of data source permissions in version 6.3, the ability to restrict data sources within group definitions is removed. Use data source permissions instead. |
| [*Column Security Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405859452695-Composer-6-3-Enhancements#Column) | This release introduces support for multiple groups in a data source column security filter. In past releases, only a single group could be selected for a column security filter. |
| [*Authorization Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405859452695-Composer-6-3-Enhancements#Authoriz) | A new **Can Manage Source Permissions** privilege is added. |
| A new **Can Administer Sources** privilege is added. |
| The **Can Export Dashboards & Data Sources** privilege is renamed to simply **Can Export Dashboards** in this release. |
| The API privileges ROLE\_DELETE\_ALL\_SOURCES, ROLE\_MANAGE\_ALL\_SOURCES, ROLE\_VIEW\_ALL\_SOURCES, and ROLE\_MANAGE\_SOME\_SOURCES are removed from the product. |
| [*User Interface Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859452695-Composer-6-3-Enhancements#User) | A new Permissions column is added to the Sources page. |
| The Column Security dialog is changed to support multiple group column security filters. A new Add Groups button is provided that activates a new Add Groups dialog. |
| **6.2 Enhancements** | |
| [*Rebranding Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405851162007-Composer-6-2-Enhancements#Migratio) | The name Zoomdata was replaced with Composer in error messages for source and dashboard imports as well as in several messages in log files. |
| [*Authorization Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405851162007-Composer-6-2-Enhancements#Authoriz) | The user experience when saving, updating, or sharing a dashboard is now consistent whether you use the Composer user interface or its API. |
| [*New Dremio Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405851162007-Composer-6-2-Enhancements#New) | A new Dremio connector is introduced in this release. |
| [*Data Source Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851162007-Composer-6-2-Enhancements#Data2) | Data source configurations can no longer be disabled. Once they are enabled, they cannot be disabled by anyone. |
| [*Data Source Row Security And Column Security Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851162007-Composer-6-2-Enhancements#Data) | The row security and column security restrictions specified for a data source configuration can now reference the same field in the data source. In past releases this was not possible. |
| [*User Interface Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851162007-Composer-6-2-Enhancements#User) | LDAP errors that occurred when logging in as a user whose Composer account was changed since the LDAP user definitions were established are resolved. |
| An error now appears if you try to import a dashboard that contains a visual that does not exist in Composer. |
| Null values can now display as zeros in [line charts](https://devnet.logianalytics.com/hc/en-us/articles/4405851221911-Line-Charts) (including line & bar, multiple metric, and attribute line charts). A new **Display null as zero** checkbox is added when you set the granularity for time fields on line charts. |
| **6.1 Enhancements** | |
| [*Query Engine Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851161111-Composer-6-1-Enhancements#Query) | A new property for the query engine was introduced in this release: `qe.max.rows.during.execution`. Use this property in the query engine properties file (`/etc/zoomdata/query-engine.properties`) to limit the number of rows of data that can be processed for a single query. |
| [*Data Source Configuration Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851161111-Composer-6-1-Enhancements#Data) | You can now insert variables in the custom SQL of a data source configuration and specify defaults for those variables. |
| [*Row Security Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851161111-Composer-6-1-Enhancements#Row) | Row security is enhanced in this release to allow you to use filters to restrict data source data for specific users or accounts. In past releases you could only restrict the data for specific groups. |
| [*User Interface Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405851161111-Composer-6-1-Enhancements#User) | The **Default** option on the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) is removed in this release. You can still specify the default settings for a visual style in a data source using the Visuals tab in the data source configuration wizard. |
| The Clear Cache button () on the Sources page has moved from its own column to the Actions column. In addition, the icon used for the Clear Cache button has changed. |
| The dashboard library is modified to match the look of the Sources and Connections pages as well as the Visual Gallery. The side menu is removed and the options on the side menu are converted to buttons at the top of the page. |
| Pagination mode is introduced for viewing raw data tables. You can now use a new pagination bar at the bottom of a raw data table to page through and view the fetched data. |
| **6.0 Enhancements** | |
| [*Migration Considerations*](https://devnet.logianalytics.com/hc/en-us/articles/4405859451415-Composer-6-0-Enhancements#Migratio) | With this release, you can no longer use `<hostname>:8080/zoomdata/api/version`. This is no longer supported. Use `<hostname>:8080/composer/api/version` instead. |
| The `server.multiple-context-path.primary` and `server.multiple-context-path.secondary` properties in the `zoomdata.properties` file are deprecated. |
| If your installation uses Kerberos, the default behavior for unauthenticated users has also changed. From a browser, unauthenticated users are now redirected to the Composer login page. For API calls, links in the format `<hostname>:8080/api/version` or `<hostname>:8080/zoomdata/api/version` now return an unauthorized 401 error. To resolve the error, use `<hostname>:8080/composer/api/version`. |
| [*Rebranding Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405859451415-Composer-6-0-Enhancements#Rebrandi) | The Service Monitor was rebranded. |
| Error messages in the UI were rebranded. |
| The word "chart" was changed to "visual," where appropriate, in the translation file used for internationalization. |
| [*Derived Field Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859451415-Composer-6-0-Enhancements#Derived) | You can now use the `NOW()` function in a derived field definition to obtain the current date and time. However, `NOW()` functionality is not enabled by default. |
| [*User Interface Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859451415-Composer-6-0-Enhancements#User) | The color of the **Add Filter** button on the Row Security dialog and on the Column Security dialog was adjusted to align with the color of other buttons in the UI (it is now blue) and the button was moved from the left side of the dialogs to the right. |
| A row security filter can now be assigned to more than one Composer group. In past releases, it could only be assigned to one group. |
| If a user belongs to more than one group, each with separate row security filters for the same data source, an error message now appears when the user tries to view a dashboard using the data source. |
| You can now use derived fields (row-level expressions) in row security filters. |
| Color palette names can now be translated using the translation file. |
| When a dashboard is embedded in an application, its sidebar now becomes a pop-up dialog (instead of a sidebar) when it is opened. |
| The maximum length of dashboard and chart descriptions has increased from 255 characters to 750 characters. |

## API Updates

| Endpoint | Method | Description |
| --- | --- | --- |
| **6.9.29 API Updates** | | |
| None. |  |  |
| **6.9.28 API Updates** | | |
| None. |  |  |
| **6.9.27 API Updates** | | |
| None. |  |  |
| **6.9.26 API Updates** | | |
| None. |  |  |
| **6.9.25 API Updates** | | |
| None. |  |  |
| **6.9.24 API Updates** | | |
| None. |  |  |
| **6.9.23 API Updates** | | |
| None. |  |  |
| **6.9.22 API Updates** | | |
| None. |  |  |
| **6.9.21 API Updates** | | |
| None. |  |  |
| **6.9.20 API Updates** | | |
| None. |  |  |
| **6.9.19 API Updates** | | |
| None. |  |  |
| **6.9.18 API Updates** | | |
| None. |  |  |
| **6.9.17 API Updates** | | |
| None. |  |  |
| **6.9.16 API Updates** | | |
| None. |  |  |
| **6.9.15 API Updates** | | |
| None. |  |  |
| **6.9.14 API Updates** | | |
| None. |  |  |
| **6.9.13 API Updates** | | |
| None. |  |  |
| **6.9.12 API Updates** | | |
| `/api/sources/{id}` | POST/PUT | You can no longer manually set the "version": {integer} of a source object when using PUT api/sources/{id} OR POST api/sources. Version is a system controlled variable which cannot be set manually. |
| **6.9.11 API Updates** | | |
| None. |  |  |
| **6.9.10 API Updates** | | |
| None. |  |  |
| **6.9.9 API Updates** | | |
| `/api/connections/{id}` | PUT | Create a connection using a predefined object ID. |
| `/api/sources/{id}` | PUT | New endpoint.  Use to upload sources using the object's ID while retaining the object ID when migrating from one environment to another.  You must have the `CanCreate{Object}` privilege. |
| `/api/visuals/{id}` | PUT | Use to create a visual using a predefined object ID.  You must have the `CanCreate{Object}` privilege. |
| `/api/dashboards/{id}` | PUT | Use to create a dashboard using a predefined object ID.  You must have the `CanCreate{Object}` privilege. |
| **6.9.8 API Updates** | | |
| None. |  |  |
| **6.9.7 API Updates** | | |
| None. |  |  |
| **6.9.6 API Updates** | | |
| None. |  |  |
| **6.9.5 API Updates** | | |
| None. |  |  |
| **6.9.4 API Updates** | | |
| None. |  |  |
| **6.9.3 API Updates** | | |
| `/api/sources` | DELETE GET PATCH POST PUT | This endpoint is deprecated and will be removed in a future release. |
| `/api/upload` | DELETE POST | This endpoint is deprecated and will be removed in a future release |
| **6.9.2 API Updates** | | |
| `/api/dashboards/import` | POST | A new query parameter, `strategy`, has been added for this endpoint. Valid values can be `OVERWRITE` or `USE_EXISTING_OR_CREATE`.   * Specify `OVERWRITE` to implement the new overwrite import policy. * Specify `USE_EXISTING_OR_CREATE` to continue to use the existing import policy (importing the dashboard with a slightly altered name). This is the default value and will be used if `strategy` is not specified. |
| **6.9.1 API Updates** | | |
| `/api/materialized-views` | GET | A new, optional parameter, `sourceId={<data-source-id>}`, has been added in this release. Use this parameter to obtain a list of materialized views for a specific data source. |
| **6.9 API Updates** | | |
| `application/vnd.composer.v3+json` media type | --- | A new media type, `application/vnd.composer.v3+json` is introduced in this release. The media type `application/vnd.composer.v2+json` is deprecated and will be removed in a future release. Logi Analytics recommends using the `application/vnd.composer.v3+json` media type for all API calls.  The difference between the two media types is primarily in the response of listing endpoints. |
| `/api` ( `/composer/api`) | GET | This API endpoint is now deprecated and will be removed from the product in a future release. |
| `/api/alerts` | GET PUT DELETE PATCH POST | A new, experimental, API is introduced in this release that can be used to alert your end users when a metric reaches a specified threshold. No UI support for this feature is provided at this time. See [*Manage Alerts*](https://devnet.logianalytics.com/hc/en-us/articles/4405859133079-Manage-Alerts). |
| `/api/upload` | DELETE POST | This API endpoint has been deprecated and will be removed in a future release. |
| `/api/visuals/<visualId>` | GET PUT DELETE | The visual permissions for a user are now verified when this API endpoint is used to retrieve, update, or delete a visual. |
| `/api/visuals/<visualId>/acls` | GET | This new endpoint can be used to list the users and groups for which visual permissions have been defined. |
| `/api/visuals/<visualId>/acls/bulk` | PATCH | This endpoint can now be used to grant or revoke visual permissions. However, the `ownerType=Source` property can no longer be specified because permissions to view or manage a visual are no longer tied to your permissions for its data source. However, read permissions for the visual's data source are required to see data in the visual. |
| `/api/visuals` | GET | The following fields in the response payload are deprecated and will be removed in a future release.   * `enabled` * `ownerType` * `name` (use `visualName` instead) * `dashboardLinks` (this field is now defined and stored in the new dashboard API response payload) |
| PUT DELETE POST | The following fields in the response payload of all other `/api/visuals` endpoints are deprecated and will be removed in a future release.   * `enabled` * `ownerType` * `lastModified` (use `lastModifiedDate` instead) * `ownerSourceId` (use `source.sourceId` instead) * `name` (use `visualName` instead) * `dashboardLinks` ((this field is now defined and stored in the new dashboard API response payload) |
| `description` property | --- | A new property called `description` is added to the visual payload. |
| `/api/visuals/source/<sourceId>/summary` | GET | This API endpoint now checks for READ permission to the data source when reading a summary of all the visual defaults. |
| `/api/user/permissions/visuals/<visualId>` | GET | This new endpoint can be used to retrieve a user's permissions for a visual. |
| `/api/visdefs/<sourceId>` | -- | This API endpoint has now been removed from the product. It was deprecated in a previous release. |
| `/api/visdefs/default/<sourceId>` | -- | This API endpoint has now been removed from the product. It was deprecated in a previous release. |
| `/api/visdefs/default/<sourceId>/<visualId>` | GET | This API endpoint now checks for READ permission to the data source when generating a single visual default. |
| `/api/dashboards/*` | DELETE GET POST PUT | This endpoint in the v1 version of the API (`application/vnd.composer.dashboard.v1+json`) is deprecated and will be removed in a future release. Use the new version of the endpoint in the v2 version of the API (`application/vnd.composer.dashboard.v2+json`) instead. |
| DELETE GET PUT | The new `/api/dashboards` API endpoint no longer relies on visuals. Instead, it uses widgets.   * The `visualizations` container is renamed to `widgets`. * The new `widgets` array contains `widget` objects, which contain only widget-specific information: `id`, `name`, `description`, `layout`, `visualId`, and `dashboardLink`.   In addition, the `bookmarksMap` object returned in the response when using the v3 version of the Composer API (`application/vnd.composer.v3+json`) has been renamed `content`.  The `/api/dashboard` family of API endpoints were updated with a new payload in this release. To use `vnd.composer.dashboards.v1+json` for backward compatibility, including the use of the `bookmarksMap` object (instead of the new `content` object), turn on the `dashboard-v1-api` variable on the Server-Level Variables page (only a Composer supervisor can make this change). See [*Server-Level Variables*](https://devnet.logianalytics.com/hc/en-us/articles/4405850889495-Server-Level-Variables). |
| `/api/visualizations/libs/*` | DELETE GET POST PUT | The `/api/visualizations/libs` endpoint is deprecated and will be removed in a future release. Use the custom chart CLI instead. See [*Maintain Custom Charts Using the Custom Chart CLI*](https://devnet.logianalytics.com/hc/en-us/articles/4405859247127-Maintain-Custom-Charts-Using-the-Custom-Chart-CLI). |
| `/api/sources/<id>/key` | GET | These security-related endpoints are deprecated and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See [*Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) and [*Embed Composer Components Using JavaScript and Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405859346967-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access). |
| `/api/sources/remove/<id>` | DELETE |
| `/api/sources/key` | GET |
| `/api/screenshot/*` | GET POST PUT | The screenshot-related endpoints are deprecated and will be removed in a future release. |
| `/oauth/authorize` | GET | This endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See [*Trusted Access API Endpoints*](https://devnet.logianalytics.com/hc/en-us/articles/4405851180439-Trusted-Access-API-Endpoints). |
| `/oauth2/client` | DELETE GET POST PUT | This endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See [*Trusted Access API Endpoints*](https://devnet.logianalytics.com/hc/en-us/articles/4405851180439-Trusted-Access-API-Endpoints). |
| `/oauth2/token` | DELETE GET POST | This endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See [*Trusted Access API Endpoints*](https://devnet.logianalytics.com/hc/en-us/articles/4405851180439-Trusted-Access-API-Endpoints). |
| **6.8 API Updates** | | |
| OpenAPI Updates | --- | The Composer API specification is now generated in OpenAPI 3.0 format. |
| Group Updates | --- | Groups can no longer be transferred to a different account using the API. |
| `/api/export/generate/rawdata` | --- | This endpoint is deprecated and will be removed in a future release. Use `/api/export/csv/raw` instead. |
| **6.7 API Updates** | | |
| `/api/keysets/upload` | POST | This new endpoint creates a keyset from a CSV file. See [*Upload Keyset Data From a CSV File Using the API*](https://devnet.logianalytics.com/hc/en-us/articles/4405851106327-Upload-Keyset-Data-From-a-CSV-File-Using-the-API). |
| `/api/keysets/upload/<keyset-id>` | PUT | This new endpoint updates a keyset from a CSV file. See [*Update Keyset Values From a CSV File Using the API*](https://devnet.logianalytics.com/hc/en-us/articles/4405851105431-Update-Keyset-Values-From-a-CSV-File-Using-the-API). |
| `/api/dashboards/<dashboard-ID>/interactivity` | GET | This new endpoint returns the dashboard's interactivity profile. If you do not have authorization for a dashboard, errors are returned. |
| PUT | This new endpoint saves a dashboard's interactivity profile. |
| DELETE | This new endpoint deletes a dashboard's interactivity profile. |
| /`api/dashboards/interactivity` | GET | This new endpoint lists the existing dashboard interactivity profiles. |
| `/api/dashboard/<dashboard-ID>?interactivityProfile={linked | readonly | interactive}` | GET | This new endpoint returns the dashboard payload with one of the following three profile names:   * `linked`: Uses the [dashboard interactivity profile](https://devnet.logianalytics.com/hc/en-us/articles/4405859265303-Control-How-Users-Interact-With-a-Dashboard) set for the dashboard. * `readonly`: Overrides the [dashboard interactivity profile](https://devnet.logianalytics.com/hc/en-us/articles/4405859265303-Control-How-Users-Interact-With-a-Dashboard), setting all visual interactivity settings to `false`, so users can view the dashboard and its visuals, but not interact with them. * `interactive`: Overrides the [dashboard interactivity profile](https://devnet.logianalytics.com/hc/en-us/articles/4405859265303-Control-How-Users-Interact-With-a-Dashboard) and all visual interativity settings to `true`, so users can view and interact with the dashboard and its visuals. This is the opposite of `readonly`. |
| `/api/sources/<source-ID>/fields/meta` | GET | This new endpoint is an experimental endpoint that returns information about all the fields and metrics in a data source. |
| **6.6 API Updates** | | |
| Group privilege renamed | The API privilege **ROLE\_MANAGE\_VISUALS** was renamed to **ROLE\_ADMINISTER\_VISUALS**. Customers who use the API to manage groups must manually make this change wherever **ROLE\_MANAGE\_VISUALS** is currently used. See [*Authorization Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859454231-Composer-6-6-Enhancements#Authoriz). | |
| `/api/dashboards/<dashboard-id>/acls/bulk` | PATCH | This new endpoint assigns permissions for a dashboard to a list of security identities (groups, users, accounts). |
| `/api/sources/<source-id>/acls/bulk` | PATCH | This new endpoint assigns permissions for a data source to a list of security identities (groups, users, accounts). |
| `/api/user/permissions/visuals/<visual-id>` | GET | This new endpoint retrieves the permissions for a visual for the currently logged in user. |
| `/api/visuals` | GET | The payload from this API now can include permission information for the visual, if the query parameter `includePermissions=true` is included, enabling this capability. |
| **6.5 API Updates** | | |
| `/api/trusted-access/clients` | GET | Returns all the Trusted Access client information in the metadata. Included with this information is the access token validity time (in seconds), client ID, client name, client secret expiration time (in seconds), and the token authentication method. For a description of these, see [*Trusted Access Client Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405859468951-Trusted-Access-Client-Properties). |
| `/api/trusted-access/clients` | POST | Creates a Trusted Access client. The request must specify the number of seconds for which the access token is valid and the client name. The client name must be unique. When you create the client, the client ID, client secret, secret expiration time, and the token authentication method are automatically generated. |
| `/api/trusted-access/clients/<id>` | GET | Returns the Trusted Access client information for a specific client. The request must specify the client ID. |
| `/api/trusted-access/clients/<id>` | DELETE | Deletes a specific Trusted Access client. The request must specify the client ID. |
| `/api/trusted-access/clients/<id>` | PATCH | Updates the Trusted Access client information for a specific client. The request must specify the client ID and the number of seconds for which the access token is valid. |
| `/api/trusted-access/token` | POST | Generates a new access token for a user. The request must specify the Composer user name. The user must already exist, and have an active Composer user account (unless you are using LDAP with automatic provisioning for Composer). |
| **6.4 API Updates** | | |
| `/api/sources/<source-id>/cache/visdata` | DELETE | Clears the visual data cache. |
| `/api/sources/<source-id>/cache/metadata` | DELETE | Clears the metadata cache. |
| `/api/sources/<source-id>/cache` | DELETE | Clears both the visual and metadata caches. |
| Source definition endpoints | --- | A new boolean `cacheableMetadata` property indicates whether metadata caching is enabled for a data source. The existing `cacheable` property indicates whether caching, in general, is enabled for the data source. |
| --- | A new `statsCached` property allows you to control metadata (field statistics) caching on a per-field basis. This property can be used to configure the field statistics look-up via materialized views (ignoring internal caches and redirecting the requests from the original source) and to improve the performance of statistics requests when precreated statistics data exists. Please contact your Technical Support representative to get guidance on how to configure this. |
| `/api/visdefs/<source-id>` | --- | This endpoint is deprecated. It is replaced by a new `/api/visuals/source/<sourcid>/summary` endpoint. The response produced by the new endpoint has also changed to include a new `visualId` setting. |
| `/api/visuals/source/<source-id>/summary` | GET | This endpoint obtains the default visual definitions for a data source configuration. |
| **6.3 API Updates** | | |
| `/api/user/permissions/sources` | GET | Lists the permission levels for the logged in user for all data source configurations in the system. |
| `/api/user/permissions/sources/<sourceid>` | GET | Retrieves the currently logged in user's source permissions for a data source. |
| `/api/sources/<sourceid>/acls` | GET | Retrieves a list of access rights for a data source. You can restrict the list to specific users, groups, or accounts using the `sidTypes` parameter. In addition, you can use the `returnSids` parameter to restrict the list so it retrieves only users, groups, or accounts with access to the data sources or to only users, groups, or accounts without access. |
| `/api/sources/<sourceid>/acls/bulk` | PUT | Grants or revokes permissions to a data source configuration a list of groups, users, or accounts. |
| `/api/sources/<source-id>/security/attributes` | --- | These endpoints now support the specification of multiple groups for a data source column security filter. |
| `/api/sources/<source-id>/security/attributes/<id>` | --- |
| **6.2 API Updates** | | |
| Visual placement | --- | An error is now produced when you try to place the same visual on a dashboard twice. |
| `/api/groups` |  | The `sources` field is deprecated and will be removed in a future release. |
|  | The `configType` field is deprecated and will be removed in a future release. |
| **6.1 API Updates** | | |
| `/api/sources/<source-id>/security/filters` | --- | This endpoint is enhanced to support account and user security identifiers. In past releases, only group security identifiers were supported. |
| `/api/security/sids` | --- | This new endpoint is introduced to retrieve security ID information. The `sidTypes` parameter can be specified with this new endpoint to limit the type of security ID information retrieved. Valid values for `sidTypes` are `GROUP`, `USER`, `ACCOUNT`, or `ALL` (the default). |
| **6.0 API Updates** | | |
| With this release, you can no longer use `<hostname>:8080/zoomdata/api/version`. This is no longer supported. Use `<hostname>:8080/composer/api/version` instead. | | |

API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`.

## Resolved Issues

| Title | Description |
| --- | --- |
| **6.9.29 Resolved Issues** | |
| Scheduled Reports | Corrected an issue for scheduled reports that generated and included system messages unrelated to the data presented in the PDF output. |
| **6.9.28 Resolved Issues** | |
| Heat Map Visuals | Corrected an issue that prevented you from setting color thresholds for number values that include decimal places. |
| Dashboard Links | Corrected an issue that prevented dashboard to dashboard links from transferring a filter if the group label included an ampersand (**&**). |
| Composer Events | Corrected an issue that may trigger Composer events before Composer is in a state that is ready to respond to the events. |
| Export Pivot Table Data | Corrected an issue that prevented the export of data to CSV format for pivot tables that include a numeric group column with high-precision numbers. |
| Visualization Loading | Composer now loads linked grouped and individual table visuals appropriately. |
| **6.9.27 Resolved Issues** | |
| Display Values | Composer now correctly displays metric labels appropriately in visuals that include negative values. |
| **6.9.26 Resolved Issues** | |
| Fonts for Visuals | Composer now applies font customization styling to all labels associated with a customized visual. |
| PDF Export | Composer now includes uncropped visuals when exporting to a PDF. |
| **6.9.25 Resolved Issues** | |
| Time Presets Support | Several of Composer’s time presets have been updated to provide more consistent time range information. See *[Preset Time Ranges](https://devnet.logianalytics.com/hc/en-us/articles/4405851144983)*for more information. |
| **6.9.24 Resolved Issues** | |
| Embedding Multiple Dashboards | Improvements were made to the loading and rendering of pages that include multiple dashboards in Composer to speed up load time and improve performance. |
| **6.9.23 Resolved Issues** | |
| None. |  |
| **6.9.22 Resolved Issues** | |
| Heat Map Visual Color Mode | When you switch between adjusting the colors for a heat map visual manually and using Gradient options, Composer now correctly applies manual color thresholds when undoing the Auto Color Metric change. |
| **6.9.21 Resolved Issues** | |
| Pivot Tables Update | The time granularity label (minutes, hours, seconds) has been removed from the row and column group labels of pivot tables. |
| **6.9.20 Resolved Issues** | |
| Visual Data Export (CSV) | Composer no longer returns an error when exporting visual data in CSV format for some dashboards that contain pivot tables. |
| Log4j Updates | Even though Composer does not use log4j for any normal workflows, the .jar files were included in a normal installation package for third party use. These .jar files are no longer included in Composer installation packages, to help mitigate any log4j vulnerabilities. |
| **6.9.19 Resolved Issues** | |
| None. |  |
| **6.9.18 Resolved Issues** | |
| Extended Filter Attributes | Composer now correctly displays selectable check box selections in Firefox browsers for extended length filter attribute names. |
| Radial Menu | Composer now displays the radial menu associated with the current visual, after switching between visuals. |
| **6.9.17 Resolved Issues** | |
| logi-composer.js | Composer now loads, renders, and operates standard visuals and custom visuals without using unsafe evaluations that may not comply with some organizations' CSPs. |
| **6.9.16 Resolved Issues** | |
| Custom Charts | Composer no longer returns an error when adding a custom chart to a new source. |
| **6.9.15 Resolved Issues** | |
| Playback for KPI Charts | Composer no longer returns an error when playback is enabled on a KPI chart with some types of Custom Metrics. |
| **6.9.14 Resolved Issues** | |
| Unified Timebar | Composer now displays the correct time range in milliseconds in the time bar when unlinking a visual. |
| **6.9.13 Resolved Issues** | |
| Modal Popups | Composer now displays field pickers for modal popups appropriate to the picker location. |
| **6.9.12 Resolved Issues** | |
| Embedded Dashboards | You can now resize, and drag and drop the Details dialog in embedded dashboards. You can now export raw data from a dashboard Details dialog. |
| **6.9.11 Resolved Issues** | |
| None. |  |
| **6.9.10 Resolved Issues** | |
| Menus for Embedded Visuals | Composer now correctly displays the More menu for visuals embedded using bootstrap@5.0.2. |
| **6.9.9 Resolved Issues** |  |
| Sub-Group Search | Composer now returns consistent results when you search Sub-Groups by Attribute search terms. |
| CSS Styles for Table Visuals | The CSS styles of embedded Composer table visuals are now independent of CSS styles used by your parent application. |
| List Filter Widget | List filter visuals that contain multiple selections from data sources now expand to an appropriate navigable height. |
| Null Values | In the Line Trend: Attributes Visual, Logi Composer now displays groupings with null values. |
| **6.9.8 Resolved Issues** | |
| Multiple Pivot Tables | Composer now displays pivot tables correctly after you have created and edited a dashboard containing multiple pivot tables. |
| Dashboard Display | When opening an embedded dashboard, Composer now displays the top of the dashboard instead of scrolling to the last active visual. |
| Fusion Data Scheduled Reports | Composer now properly produces visuals and images for scheduled report PDF files generated using Fusion data. |
| Data Variance | Composer now correctly calculates and returns the results of 1 Mth YoY data to accommodate leap years. |
| **6.9.7 Resolved Issues** | |
| Hive Datasource | Composer now properly handles invisible fields in the Hive datasource when customers upgrade from Composer 5.9 to 6.9. |
| **6.9.6 Resolved Issues** | |
| Large Dashboard Scheduling | Customers can now schedule and transmit large dashboards without getting a DataBufferLimitException error code. |
| 6.9.5 Resolved Issues | |
| None. |  |
| 6.9.4 Resolved Issues | |
| Amazon S3 Connector | Improvements were made to the Amazon S3 error messages and log entries in Composer. |
| Dashboard Links | The **Link** option on the radial menu no longer appears if a user does not have read permission for the dashboard that is linked. |
| **6.9.3 Resolved Issues** | |
| Field Conversion & Data Sources | An error is no longer produced when saving a data source after converting multiple integer fields to numbers. |
| Invisible Fields & Data Sources | You can no longer save a data source with an invisible field, if the invisible field is referenced in a visual (charted or used in filters and keysets). |
| Filters | Aggregations are now pushed down correctly when excluding many values in a filter. |
| Custom Metrics | The help dialog (available in the Function Library section of the Custom Metrics Editor) now appears for a dashboard embedded using Bootstrap version 3.3.7. |
| List Filter Widget | Values now appear on a list filter widget after it is maximized or minimized. |
| **6.9.2 Resolved Issues** | |
| [*Custom Metric Date and Time Aggregation Function Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859456535-Composer-6-9-2-Enhancements#CustomMetrics) | Custom metrics now support the `now()` and `time_add` functions used by row-level expressions. The original custom metric `DATE()`, `DateADD`, and `DateSUB` functions still work but should no longer be used. They are deprecated in this release and will be removed in a future release. Instead, use the `now()` and `time_add` functions. |
| [*Dashboard Import Changes*](https://devnet.logianalytics.com/hc/en-us/articles/4405859456535-Composer-6-9-2-Enhancements#DashImport) | You can now use the API to import a dashboard using a new overwrite policy, so that dashboards with the same name are overwritten instead of being imported with a slightly altered name. |
| Materialized Views | You can now create a materialized view definition when the Volume metric has been renamed. |
| 6.9.1 Resolved Issues | |
| Dashboard Import | A problem importing dashboards from the same Composer version has been resolved. |
| Composer 6.9 Resolved Issues | |
| Cross-source Linked Dashboard Visual Filters | Filters now work correctly for dashboard visuals that are cross-source linked when the dashboard is linked by URL from an application. |
| UI errors | The scroll bar no longer disappears when scrolling through a long list of filter values. |
| Axes Colors | The colors of axes lines for visuals are now retained correctly after an upgrade. |
| Custom Charts | Resolved an issue with custom charts that broke with the removal of internal JavaScript libraries that were being used as dependencies. |
| 6.8 Resolved Issues | |
| Data Sources | Changes to the Tables/Indices tab of a data source configuration (or the custom SQL specified there) no longer reset the custom labels and settings on the Fields tab of the data source or its global settings. |
| Connections | Connection attributes no longer appear broken when a system override is specified. |
| Calculated Value Appearance | When a dashboard loads, values that take a moment to be calculated are shown as a waiting (loading) using this image: |
| Dashboard Refreshes | Corrected a problem in which table data was not refreshed when the dashboard refresh button was selected. |
| Histograms | Corrected a problem in which histograms were not retaining their bar interval settings under specific circumstances. |
| Migration | Resolved a problem in which migration failed because the data source had no Volume Metric selected. |
| Embed Code | Composer no longer uses `hammer.js`. |
| Tables | Corrected a problem in which tables were not updated during playback. |
| 6.7 Resolved Issues | |
| Visuals | Corrected a problem in which **Undo Changes** did not work for a visual while the visual sidebar was open. |
| Data Sources | Corrected a problem in which visuals were not honoring the Group By global default setting in the data source. |
| Radial Menu | Corrected a problem in which undoing a trend request (Trend option on the radial menu) produced errors. |
| 6.6 Resolved Issues | |
| COALESCE Function Changes | The [COALESCE function](https://devnet.logianalytics.com/hc/en-us/articles/4405851017239-Conditional-Functions) now supports aggregate metrics with complex calculations using arithmetic functions (for example `COALESCE(max(sales) * 1.3, 0)`), so a default value can be used if null values are returned. |
| Pivot Tables | Pivot table performance is improved for a Postgres data source that uses custom SQL. |
| Elasticsearch Connectors | Elasticsearch connectors now provide error messages when a Last Value metric cannot be computed correctly. See [*Elasticsearch Last Value Processing*](https://devnet.logianalytics.com/hc/en-us/articles/4405850951063-Elasticsearch-Last-Value-Processing). |
| Line Trend Visuals | Improved performance of line trend visuals. |
| Performance | Java memory performance on live dashboards is improved. |
| API/SDK | It is no longer possible to create two visuals with the same `controlsCfg` ID using the API. |
| An incorrect call for the `removeEventListener` function is corrected. |
| Importing Dashboards | Resolved a problem in which an attempt to import a dashboard failed when the dashboard included a visual shared with another dashboard that had already been imported. |
| Embedded Dashboards | Dashboards are now embedded successfully when they contain no visuals. |
| 6.5 Resolved Issues | |
| MSSQL Connections | Resolved a problem in which some MSSQL connections no longer worked for visuals and dashboards after an upgrade from 4.9 to 5.9. |
| Embedded Dashboards | Line and bar trend visuals now work in embedded scenarios. |
| Dashboards & Visuals | Corrected a problem in which leaving a dashboard or visual while the Settings sidebar is open caused the visual or dashboard to go blank. |
| 6.4 Resolved Issues | |
| Embedded Dashboards | You can now remove a visual from an embedded dashboard. A new **Remove Visual** option is added to the embedded dashboard drop-down menu. |
| Numeric Data Exports | All numeric data in an exported CSV file is now exported in decimal form. In past releases, some numbers were exported using scientific notation. |
| Window Aggregation Functions | Window aggregation functions now support derived fields as partitioning arguments. See [*Window Aggregation Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851016343-Window-Aggregation-Functions). |
| 6.3 Resolved Issues | |
| Embedded Dashboards | Dialog elements now appear correctly for iFrameless embedded dashboards. |
| Filtering | Corrected a filter problem that occurred when drilling down (zooming) on a particular attribute. |
| Amazon S3 Connector | Corrected a problem in which the Amazon S3 connector sporadically failed to detect a file delimiter. |
| 6.2 Resolved Issues | |
| LDAP | Resolved LDAP errors that occurred when logging in as a user whose Composer account was changed since the LDAP user definitions were established. |
| Embedded Dashboards | Unnecessary pop-up dialogs no longer appear in an embedded dashboard when the visual style is switched. |
| Time Bar | The initial load of a dashboard no longer hides the time bar. |
| Dashboards | The top of a long dashboard link list is now viewable when you scroll down the list. |
| An error now appears if you try to import a dashboard that contains a visual that does not exist in Composer. |
| Themes | Dark themes now work correctly with line charts. |
| 6.1 Resolved Issues | |
| Jquery Support | Composer updated the version of `jquery` it uses to version 3.5.0 or later. |
| Map Visuals | The OpenMapSurfer tile provider for maps is no longer supported. When you upgrade to this version of Composer, all visuals that use OpenMapSurfer are upgraded to use OpenStreetMap instead. |
| Snowflake Connector | Problems creating a Snowflake data source from a Snowflake table that contained a numeric or date field are resolved. |
| Performance | Performance was improved for the sort and limit feature in visuals. |
| 6.0 Resolved Issues | |
| Connectors | Connectors correctly start now when the `config-server.enabled=true` option is set in the `edc.properties` file in an HA environment. |
| Security | Improved security in enterprise data connectors. |
| Kerberos | If you have Kerberos enabled, you must use a static context path for the Composer login URL. Multiple or dynamic context paths are not supported at this time. |

## Deprecated Features

The following deprecated features will be removed in a future release.

| Title | Description |
| --- | --- |
| 6.9.29 Deprecated Features | |
| None. |  |
| 6.9.28 Deprecated Features | |
| None. |  |
| 6.9.27 Deprecated Features | |
| None. |  |
| 6.9.26 Deprecated Features | |
| None. |  |
| 6.9.25 Deprecated Features | |
| None. |  |
| 6.9.24 Deprecated Features | |
| None. |  |
| 6.9.23 Deprecated Features | |
| None. |  |
| 6.9.22 Deprecated Features | |
| None. |  |
| 6.9.21 Deprecated Features | |
| None. |  |
| 6.9.20 Deprecated Features | |
| None. |  |
| 6.9.19 Deprecated Features | |
| None. |  |
| 6.9.18 Deprecated Features | |
| None. |  |
| 6.9.17 Deprecated Features | |
| None. |  |
| 6.9.16 Deprecated Features | |
| None. |  |
| 6.9.15 Deprecated Features | |
| None. |  |
| 6.9.14 Deprecated Features | |
| None. |  |
| 6.9.13 Deprecated Features | |
| None. |  |
| 6.9.12 Deprecated Features | |
| None. |  |
| 6.9.11 Deprecated Features | |
| None. |  |
| 6.9.10 Deprecated Features | |
| None. |  |
| 6.9.9 Deprecated Features | |
| None. |  |
| 6.9.8 Deprecated Features | |
| None. |  |
| 6.9.7 Deprecated Features | |
| None. |  |
| 6.9.5 Deprecated Features | |
| None. |  |
| 6.9.4 Deprecated Features | |
| None. |  |
| 6.9.3 Deprecated Features | |
| API | The `/api/sources` and `/api/upload` endpoints are deprecated and will be removed in a future release. |
| 6.9.2 Deprecated Features | |
| Custom Metric Date and Time Aggregation Functions | The custom metric `DATE()`, `DateADD`, and `DateSUB` functions still work but should no longer be used. They are deprecated in this release and will be removed in a future release. Instead, use the `now()` and `time_add` functions. See [*Date and Time Filter Aggregation Functions*](https://devnet.logianalytics.com/hc/en-us/articles/4405851015447-Date-and-Time-Filter-Aggregation-Functions). |
| **6.9 Deprecated Features** | |
| API | The media type `application/vnd.composer.v2+json` is deprecated and will be removed in a future release. Use the `application/vnd.composer.v3+json` media type instead. If you must use |
| The `GET /api` (`/composer/api`) endpoint is now deprecated and will be removed from the product in a future release. |
| The `/api/dashboards/*` endpoint used in the v1 version of the API (`application/vnd.composer.dashboard.v1+json`) is deprecated and will be removed in a future release. Use the new version of the endpoint in the v2 version of the API (`application/vnd.composer.dashboard.v2+json`) or `application/vnd.composer.v2` instead. Errors will result if you attempt to use `application/vnd.composer.dashboard.v1+json`.  Contact Customer Support to use `vnd.composer.dashboards.v1+json` for backward compatibility, including the use of the `bookmarksMap` object (instead of the new `content` object).  When no `content-type` header is specified, Composer defaults to using `application/vnd.composer.dashboard.v1+json`. |
| The `/api/upload` endpoint is deprecated and will be removed in a future release. |
| The `/api/visualizations/lib/*` endpoint is deprecated and will be removed in a future release. Use the custom chart CLI instead. See [*Maintain Custom Charts Using the Custom Chart CLI*](https://devnet.logianalytics.com/hc/en-us/articles/4405859247127-Maintain-Custom-Charts-Using-the-Custom-Chart-CLI). |
| The `/api/sources` endpoint is deprecated and will be replaced in a future release. |
| The `GET /api/sources/<id>/key` endpoint is now deprecated and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See [*Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) and [*Embed Composer Components Using JavaScript and Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405859346967-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access). |
| The `DELETE /api/sources/remove/<id>` endpoint is now deprecated and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See [*Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) and [*Embed Composer Components Using JavaScript and Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405859346967-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access). |
| The `GET /api/sources/key` endpoint is now deprecated and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See [*Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access) and [*Embed Composer Components Using JavaScript and Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405859346967-Embed-Composer-Components-Using-JavaScript-and-Trusted-Access). |
| The `/api/screenshot/*` endpoint and `/api/screenshot-management` endpoint are deprecated and will be removed in a future release. |
| The `GET /oauth/authorize` endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See [*Trusted Access API Endpoints*](https://devnet.logianalytics.com/hc/en-us/articles/4405851180439-Trusted-Access-API-Endpoints). |
| The `/oauth2/client` endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See [*Trusted Access API Endpoints*](https://devnet.logianalytics.com/hc/en-us/articles/4405851180439-Trusted-Access-API-Endpoints). |
| The `/oauth2/token` endpoint is deprecated and will be removed in a future release. Use Trusted Access instead. See [*Trusted Access API Endpoints*](https://devnet.logianalytics.com/hc/en-us/articles/4405851180439-Trusted-Access-API-Endpoints). |
| The following fields in the response payload of the `GET /api/visuals` endpoint are deprecated and will be removed in a future release.   * `enabled` * `ownerType` * `name` (use `visualName` instead) * `dashboardLinks` ((this field is now defined and stored in the new dashboard API response payload) |
| The following fields in the response payload of all other `/api/visuals` endpoints are deprecated and will be removed in a future release.   * `enabled` * `ownerType` * `lastModified` (use `lastModifiedDate` instead) * `ownerSourceId` (use `source.sourceId` instead) * `name` (use `visualName` instead) * `dashboardLinks` ((this field is now defined and stored in the new dashboard API response payload) |
| Data Sources | The **Enabled** column on the Sources page of the UI is deprecated and will be removed in a future release. You can no longer disable data source configuration definitions, so when the column is removed, all disabled data sources will automatically be enabled. If you do not want the data sources disabled, you should [delete](https://devnet.logianalytics.com/hc/en-us/articles/4405859314967-Delete-a-Data-Source-Configuration) them. You can control access to a data source configuration using data source [permissions](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions), as well as [row](https://devnet.logianalytics.com/hc/en-us/articles/4405859333655-Restrict-Access-to-Data-Using-Row-Security) and [column](https://devnet.logianalytics.com/hc/en-us/articles/4405851034007-Restrict-Access-to-Fields-Using-Column-Security) data source restrictions. See [*Enable a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405859316119-Enable-a-Data-Source-Configuration). |
| The import and export JSON definition functions for data source configurations are deprecated and will be removed in a future release. Plans are underway to replace this functionality with an improved option in a future release. |
| Dashboards | The import and export JSON definition functions for dashboard configurations are deprecated and will be removed in a future release. Plans are underway to replace this functionality with an improved option in a future release. |
| OAuth Security | The OAuth Authentication Service is deprecated and will be removed in a future release. Use Trusted Access instead. See [*Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access). |
| Security Keys | Security keys are deprecated in this release and will be removed in a future release. Use Trusted Access instead for all embedded workflows. See [*Trusted Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405851181463-Trusted-Access). |
| Older Dashboard Embed Structure | Support for the iFrameless dashboard embed structure used in Composer 5.9 and older versions is deprecated in this release and will be removed in a future release. Use the new embed structure and methodology documented in [*Embed Composer Components Into Your Application*](https://devnet.logianalytics.com/hc/en-us/articles/4405859263895-Embed-Composer-Components-Into-Your-Application) instead. |
| **6.8 Deprecated Features** | |
| API | The `/api/export/generate/rawdata` endpoint is deprecated and will be removed in a future release. Use `/api/export/csv/raw` instead. |
| Custom Chart CLI | The following custom chart CLI libraries are deprecated: `nvd3.multiline.js`, `fabric.js`, `require/require.js`. |
| 6.7 Deprecated Features | |
| Embedded Dashboards | The `mode` property of the `createComponent` Javascript method used when embedding dashboards is deprecated. Use dashboard interactivity instead. See [*Control How Users Interact With a Dashboard*](https://devnet.logianalytics.com/hc/en-us/articles/4405859265303-Control-How-Users-Interact-With-a-Dashboard). |
| 6.6 Deprecated Features | |
| None | |
| 6.5 Deprecated Features | |
| JavaScript properties | The `application.banner` and `application.logo` JavaScript properties are deprecated. See [*Embedded Dashboard Properties and Objects*](https://devnet.logianalytics.com/hc/en-us/articles/4405851050647-Supported-Embedded-Dashboard-Properties-and-Objects). |
| 6.2 Deprecated Features | |
| API | The `sources` field in the `/api/groups` endpoint is deprecated and will be removed in a future release. |
| The `configType` field in the `/api/groups` endpoint is deprecated and will be removed in a future release. |
| 6.0 Deprecated Features | |
| Properties | The `server.multiple-context-path.primary` and `server.multiple-context-path.secondary` properties in the `zoomdata.properties` file are deprecated. This release does not support multiple context paths. |
| API | You can no longer use `<hostname>:8080/zoomdata/api/version`. Use `<hostname>:8080/composer/api/version` instead. |
| 5.9.1 Deprecated Features | |
| API | The `/api/security/attributes` endpoint is replaced with the new `/api/sources/<source-id>/security/attributes` endpoint, used for column security. |
| The `/api/filters` endpoint is replaced with the new `/api/sources/<source-id>/security/filters` endpoint, used for row security. |
| The `/api/dashboards/<dashboard-id>/key` endpoint. When removed, you will no longer be able to share a dashboard by generating a public link. |
| 5.9 Deprecated Features | |
| Authorization | The UI privilege **Can Share Visuals & Dashboards** (API privilege ROLE\_SHARE\_DASHBOARDS) associated with sharing a dashboard via a dashboard link is renamed **Can Generate Dashboard Public Link** (same API privilege), but is officially deprecated in release 5.9. |

## Removed Features

| Title | Description |
| --- | --- |
| **6.9 Removed Features** | |
| API | The `GET /api/visdefs/<sourceid>/<visid>` API endpoint is now removed from the product. It was deprecated in a previous release. |
| The `PUT /api/visdefs/<sourceid>/<visid>` API endpoint is now removed from the product. It was deprecated in a previous release. |
| The `POST /api/visdefs/<sourceid>/<visid>` API endpoint is now removed from the product. It was deprecated in a previous release. |
| The `DELETE /api/visdefs/<sourceid>/<visid>` API endpoint is now removed from the product. It was deprecated in a previous release. |
| The `GET /api/visdefs/<sourceid>`API endpoint is now removed from the product. It was deprecated in a previous release. |
| The `POST /api/visdefs/default/<sourceid>/<visid>` API endpoint is now removed from the product. |
| The `PUT /api/visdefs/default/<sourceid>/<visid>` API endpoint is now removed from the product. |
| Licensing | In support of the new license structure, the following license properties have been removed from the `api/license`endpoint response: `type` and `enforcementLevel`. |
| Context Variables | The `${User.zoomdataUserName}` context variable is removed from the product. You can no longer use this variable in new connection, data source, or forced filter definitions. Existing definitions that use this context variable will continue to work. For new definitions, use the `${User.composerUserName}` context variable instead. |
| 6.8 Removed Features | |
| None. | |
| 6.7 Removed Features | |
| None. | |
| 6.6 Removed Features | |
| None. | |
| 6.5 Removed Features | |
| None. | |
| 6.4 Removed Features | |
| Fields | * `com.zoomdata.resource.GroupAclResource#bookmarks` * `com.zoomdata.resource.GroupAclResource#connections` * `com.zoomdata.resource.InventoryItemResource#ownerFullName` * `com.zoomdata.resource.InventoryItemResource#ownerUserId` * `com.zoomdata.resource.dashboard.DashboardResource#userId` * `com.zoomdata.resource.dashboard.DashboardResource#shareState` * `com.zoomdata.resource.dashboard.DashboardResource#ownerName` |
| Sorting Option | The `com.zoomdata.web.controller.InventoryController.SortableField#OWNER` sorting option that relied on the OWNER field that was deprecated in 5.9 is removed from the code. |
| Authorization | The API privilege ROLE\_SAVE\_DASHBOARDS, deprecated in 5.9, is removed from the code. Use ROLE\_CREATE\_DASHBOARDS instead. All existing groups that had the ROLE\_SAVE\_DASHBOARDS privilege granted are automatically migrated to ROLE\_CREATE\_DASHBOARDS. However, if your organization has integrated Composer API calls into third-party software, you will need to manually change all references of ROLE\_SAVE\_DASHBOARDS to ROLE\_CREATE\_DASHBOARDS. See [*Group Privilege Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference). |
| API | The `visualizations` container in the response from a GET or PATCH `/api/sources/<id>` request was deprecated in 5.9 and support for it is removed from the Composer code. |
| 6.3 Removed Features | |
| Linux | CentOS 6 is no longer supported and the special installation Bootstrap procedure (`bootstrap-zoomdata-centos6.run`) is no longer provided with this product. CentOS 6 is no longer supported by Red Hat Linux (RHEL). Use CentOS 7 or 8 instead. |
| Red Hat Linux 6 and Scientific Linux are no longer supported. |
| JSON | The `Content-Type` header `vnd.zoomdata.v2+json` is no longer supported in version 6.3 and later and can no longer be used as the `Content-Type` for API routes. It is removed from the product. Use `vnd.composer.v2+json` as the `Content-Type` for API routes instead. |
| Group Definitions | As a result of the introduction of data source permissions in version 6.3, the ability to restrict data sources within group definitions is removed. See [*Manage Group Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405850856599-Manage-Group-Definitions). Use data source permissions instead. For information about data source permissions, see [*About Data Source Permissions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859328535-About-Data-Source-Permissions). |
| Custom Chart CLI | Support for Version 3 of the custom chart CLI is now removed because it only supported Zoomdata version 3 and earlier and support for those Zoomdata versions is dropped. Use version 4 or the new version 5 of the custom chart CLI instead. See [*Supported Custom Chart CLI Versions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859246103-Supported-Custom-Chart-CLI-Versions). |
| Authorization | The API privileges ROLE\_DELETE\_ALL\_SOURCES, ROLE\_MANAGE\_ALL\_SOURCES, ROLE\_VIEW\_ALL\_SOURCES, and ROLE\_MANAGE\_SOME\_SOURCES are removed from the product. When you upgrade, groups with these roles will be automatically upgraded with new source privilege settings as follows:   * Groups with the ROLE\_VIEW\_ALL\_SOURCES privilege are automatically granted read permissions for all data sources. * Groups with the ROLE\_MANAGE\_ALL\_SOURCES privilege are automatically granted write permissions for all data sources. * Groups with the ROLE\_DELETE\_ALL\_SOURCES privilege are automatically granted delete permissions for all data sources. |
| 6.2 Removed Features | |
| API | The `accountId` parameter, which was deprecated in Composer 5.9, has now been removed from the following API endpoints:   * `GET /api/actions` * `DELETE /api/actions/{id}` * `POST /api/actions/{id}/invoke` * `GET /api/dashboards/export` * `GET /api/groups` * `GET /api/inventory` * `GET /api/sources/name/{name}` * `GET /api/sources` * `POST /api/upload/{sourceId}` * `DELETE /api/upload/{sourceId}` * `GET /api/preferences` * `GET /api/users` * `GET /api/visuals` |
| Authorization | The supplied **View All** group, which was officially deprecated in Composer 5.9, has now been removed from *new* installations of the product. See [*About Supplied Group Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859110935-About-Supplied-Group-Definitions).  If you are upgrading to this release, the description provided for the **View All** group has changed, indicating that the group is no longer a default system group and no longer gives users implicit read-only permissions to all sources in the account. Pre-existing data sources will still be accessible for **View All** group members; new data sources will not. |
| 6.1 Removed Features | |
| None. | |
| 6.0 Removed Features | |
| None. | |
