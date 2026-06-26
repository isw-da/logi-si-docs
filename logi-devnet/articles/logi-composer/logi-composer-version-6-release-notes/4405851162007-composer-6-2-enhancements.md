---
title: "Composer 6.2 Enhancements"
id: 4405851162007
section: "Logi Composer Version 6 Release Notes"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851162007-Composer-6-2-Enhancements
updated_at: 2022-04-25T15:19:14Z
---

# Composer 6.2 Enhancements

# Composer 6.2 Enhancements

This topic describes the significant enhancements in Composer 6.2.

* [*Rebranding Updates*](#Migratio)
* [*Authorization Updates*](#Authoriz)
* [*New Dremio Connector*](#New)
* [*Data Source Changes*](#Data2)
* [*Data Source Row Security And Column Security Changes*](#Data)
* [*User Interface Changes*](#User)

Email [salesteam@logianalytics.com](mailto:salesteam@logianalytics.com?subject=Tell%20me%20about%20Composer%205) or [emea\_sales@logianalytics.com](mailto:emea_sales@logianalytics.com) to purchase Composer.

## Rebranding Updates

The name Zoomdata was replaced with Composer in error messages for source and dashboard imports as well as in several messages in log files.

## Authorization Updates

The user experience when saving, updating, or sharing a dashboard is now consistent whether you use the Composer user interface or its API. If your user account includes the **Can Administer Dashboards**[privilege](https://devnet.logianalytics.com/hc/en-us/articles/4405859114647-Group-Privilege-Reference) without access to all the data sources used by the visuals on the dashboard, you can now save the dashboard, update the dashboard, and share the dashboard link. In past versions, you could do this using the API, but not the user interface.

## New Dremio Connector

This release introduces a Dremio connector. This connector lets you access the data available in Dremio from supported versions of MySQL and MS SQL Server data stores using the Composer client. The Composer Dremio connector supports Dremio Community and Enterprise Editions version 4.1 through 4.8. See [*Manage the Dremio Connector*](https://devnet.logianalytics.com/hc/en-us/articles/4405859221911-Manage-the-Dremio-Connector) for more information.

## Data Source Changes

Data source configurations can no longer be disabled. Once they are enabled, they cannot be disabled by anyone. Data source configurations that are disabled when you upgrade to this version, remain disabled, until they are enabled. After they are enabled, they can never be disabled.

You can still control access to a data source configuration using [row](https://devnet.logianalytics.com/hc/en-us/articles/4405859333655-Restrict-Access-to-Data-Using-Row-Security) and [column](https://devnet.logianalytics.com/hc/en-us/articles/4405851034007-Restrict-Access-to-Fields-Using-Column-Security) data source restrictions, or by [deleting](https://devnet.logianalytics.com/hc/en-us/articles/4405859314967-Delete-a-Data-Source-Configuration) the data source from the system. For more information, see [*Enable a Data Source Configuration*](https://devnet.logianalytics.com/hc/en-us/articles/4405859316119-Enable-a-Data-Source-Configuration).

## Data Source Row Security And Column Security Changes

The row security and column security restrictions specified for a data source configuration can now reference the same field in the data source. In past releases this was not possible. For more information about row and column security, see [*Restrict Access to Fields Using Column Security*](https://devnet.logianalytics.com/hc/en-us/articles/4405851034007-Restrict-Access-to-Fields-Using-Column-Security) and [*Restrict Access to Data Using Row Security*](https://devnet.logianalytics.com/hc/en-us/articles/4405859333655-Restrict-Access-to-Data-Using-Row-Security).

## User Interface Changes

The following changes were made to the user interface in this release:

* Resolved LDAP errors that occurred when logging in as a user whose Composer account was changed since the LDAP user definitions were established.
* An error now appears if you try to import a dashboard that contains a visual that does not exist in Composer.
* Null values can now display as zeros in [line charts](https://devnet.logianalytics.com/hc/en-us/articles/4405851221911-Line-Charts) (including line & bar, multiple metric, and attribute line charts). A new **Display null as zero** checkbox has been added when you set the granularity for time fields on line charts. If **Include Blanks** is selected for the chart, you can select the **Display null as zero** option. By default, both options are not selected. See [*Even Time Intervals*](https://devnet.logianalytics.com/hc/en-us/articles/4405850992919-Even-Time-Intervals).
