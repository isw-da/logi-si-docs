---
title: "Composer 6.1 Enhancements"
id: 4405851161111
section: "Logi Composer Version 6 Release Notes"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851161111-Composer-6-1-Enhancements
updated_at: 2022-04-25T15:19:14Z
---

# Composer 6.1 Enhancements

# Composer 6.1 Enhancements

This topic describes the significant enhancements in Composer 6.1.

* [*Query Engine Changes*](#Query)
* [*Data Source Configuration Changes*](#Data)
* [*Row Security Changes*](#Row)
* [*User Interface Changes*](#User)

Email [salesteam@logianalytics.com](mailto:salesteam@logianalytics.com?subject=Tell%20me%20about%20Composer%205) or [emea\_sales@logianalytics.com](mailto:emea_sales@logianalytics.com) to purchase Composer.

## Query Engine Changes

A new property for the query engine was introduced in this release: `qe.max.rows.during.execution`. Use this property in the query engine properties file (`/etc/zoomdata/query-engine.properties`) to limit the number of rows of data that can be processed for a single query. This property is introduced to prevent an individual complicated query from consuming all the resources available to Composer.

The value specified for `qe.max.rows.during.execution` must be at least slightly greater than the value specified for the `qe.zengine.edc.rows.limit` property. The default for this new property is 5 million (5000000) rows of data (the default for `qe.zengine.edc.rows.limit` is 1 million rows). If you increase the value of `qe.zengine.edc.rows.limit`, consider increasing the value of this property.

When a query exceeds the `qe.max.rows.during.execution` limit, a `Resource limit is reached during query execution` message appears. See [*Query Engine Properties*](https://devnet.logianalytics.com/hc/en-us/articles/4405859160727-Query-Engine-Properties).

## Data Source Configuration Changes

You can now insert variables in the custom SQL of a data source configuration and specify defaults for those variables. See [*Tables/Indices Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859323287-Tables-Indices-Tab) and [*Specify Custom User Attributes*](https://devnet.logianalytics.com/hc/en-us/articles/4405850862359-Specify-Custom-User-Attributes).

## Row Security Changes

Row security has been enhanced in this release to allow you to use filters to restrict data source data for specific users or accounts. In past releases you could only restrict the data for specific groups. This change involves changes to the row security dialogs as well as to the API call for row security (see [*API Updates*](https://devnet.logianalytics.com/hc/en-us/articles/4405859449111-Logi-Composer-Version-6-Release-Notes#API)). For more information about row security, see [*Restrict Access to Data Using Row Security*](https://devnet.logianalytics.com/hc/en-us/articles/4405859333655-Restrict-Access-to-Data-Using-Row-Security).

## User Interface Changes

The following changes were made to the user interface in this release:

* The **Default** option on the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4405851254295-Use-the-Visual-Menu) has been removed in this release. You can still specify the default settings for a visual style in a data source using the Visuals tab in the data source configuration wizard. In addition, the **Defaults** interaction setting has also been removed from the interactivity sidebar. See [*Visuals Tab*](https://devnet.logianalytics.com/hc/en-us/articles/4405859325591-Visuals-Tab) and [*Control How Users Interact With a Visual*](https://devnet.logianalytics.com/hc/en-us/articles/4405859573143-Control-How-Users-Interact-With-a-Visual).
* The Clear Cache button (![](https://devnet.logianalytics.com/hc/article_attachments/4406743755543/clear-cache-btn.png)) on the Sources page has moved from its own column to the Actions column. In addition, the icon used for the Clear Cache button has changed. See [*Sources Page*](https://devnet.logianalytics.com/hc/en-us/articles/4405851037719-Sources-Page).
* The dashboard library has been modified to match the look of the Sources and Connections pages as well as the Visual Gallery. The side menu has been removed and the options on the side menu have been converted to buttons at the top of the page. See [*Use the Dashboard Library*](https://devnet.logianalytics.com/hc/en-us/articles/4405859273751-Use-the-Dashboard-Library).
* This release introduces pagination mode for viewing raw data tables. You can now use a new pagination bar at the bottom of a raw data table to page through and view the fetched data. The number of pages of data available to display before more data is fetched from the data store is determined by the size of the visual widget on the dashboard. In past releases, only infinite scrolling was available for viewing raw data tables.

  To support pagination, you can now select **Pagination** mode at the bottom of the Settings sidebar for a raw data table visual. Two modes are offered: **Infinite Scroll** and **Pagination**. The default is **Infinite Scrolling**. For complete information about how data is fetched for a raw data table and how pagination and infinite scrolling work, see [*Change Table Pagination*](https://devnet.logianalytics.com/hc/en-us/articles/4405851239447-Change-Table-Pagination).
