---
title: "Logi Composer 25.2 Release Notes"
id: 37515110333197
section: "Logi Composer  25 Release Notes Overview"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515110333197-Logi-Composer-25-2-Release-Notes
updated_at: 2026-05-26T22:10:34Z
---

# Logi Composer 25.2 Release Notes

# Logi Composer 25.2 Release Notes

This topic describes feature enhancements, resolved issues, and important information for Composer 25.2.

To purchase this product, contact [insightsoftware Sales](mailto:loginewbusinessteam@insightsoftware.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "Sales email address.").

* [Feature Enhancements](#Feature "Feature Enahncements section")
* [API Updates](#API_Updates "API Updates section")
* [Resolved Issues](#Resolved)
* [Deprecated Features](#Deprecated_Features)
* [Removed Features](#Removed_Features)

See also [Important Notices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933115853197-Important-Notices), [Deprecated Features](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933137766029-Deprecated-Features), and [Logi Composer Version 25 Summary of Changes](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933145504013-Logi-Composer-Version-25-Summary-of-Changes).

Composer is offered on a quarterly release schedule. The current major release of Composer is v25.3.

**Important:** 
Composer v7, a passive support release, is supported with service packs that address only critical patches and security updates. Composer v7 is in passive support as of September 1, 2023. Security updates are not applicable to third-party dependencies. Changes to existing functionality, bug fixes, and workarounds are described in the Release Notes. Composer v7 is at end of life as of September 1, 2024. See [Logi Composer Release Vehicles and Third Party End of Life Policy](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/39993554687885-Logi-Composer-Release-Vehicles-and-Third-Party-End-of-Life-Policy).

## Feature Enhancements

| Title | Description |
| --- | --- |
| **25.2.10 Feature Enhancements** | |
| None. |  |
| **25.2.9 Feature Enhancements** | |
| None. |  |
| **25.2.8 Feature Enhancements** | |
| None. |  |
| **25.2.7 Feature Enhancements** | |
| None. |  |
| **25.2.6 Feature Enhancements** | |
| None. |  |
| **25.2.5 Feature Enhancements** | |
| None. |  |
| **25.2.4 Feature Enhancements** | |
| None. |  |
| **25.2.3 Feature Enhancements** | |
| None. |  |
| **25.2.2 Feature Enhancements** | |
| None. |  |
| **25.2.1 Feature Enhancements** | |
| None. |  |
| **25.2 Feature Enhancements** | |
| [Updated Connector Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#connect) | We have updated a number of connectors in this release. Updated connectors include: Oracle, PostgreSQL, the Real Time Sales (RTS) connector, Redshift, and the Snowflake connector. See their respective connector pages for more information. |
| [OpenSearch Connector Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#connect2) | We have added support for a new connector, OpenSearch. See [Manage the OpenSearch Connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515138873485-Manage-the-OpenSearch-Connector). |
| [Dashboard Filtering and Data Refresh Improvements](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#Dashboard) | We have added a way for you to enable or disable the auto refresh of data in your single source dashboards as needed.   * Dashboards that include filter snippets from a single source have a new setting, Published Filters. * When available, select the Published Filters icon on the dashboard and enable or disable the **Auto Apply Filters** toggle. * **Auto Apply Filters** is enabled by default: any changes you make to your filters are reflected immediately. * If you are working with several filter snippets and a large data set, you can disable **Auto Apply Filters** to prevent Composer from refreshing the data until you either enable **Auto Apply Filters** again, or select **Apply** in the **Published Filters Setting** work area.   For more information, see [Manage Auto Data Refresh](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149198733-Manage-Auto-Data-Refresh). |
| [Show and Hide Column Labels](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#Metric) | You now have the option to hide some or all of the metric function labels and time zone labels in your table visuals and pivot table visuals. Select relevant show/hide options for individual labels using the table context menu in the column header. |
| [Install / Upgrade Operating System Requirements](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#Install) | Composer v25.2 no longer supports CentOS 7 or Amazon Linux 7. Update your OS to a later version before upgrading to or installing Composer v25.2, or exclude the `sdk-service` during installation. |
| [Free-Form Widget Placement on Dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#Free-For) | You can now switch the layout of a dashboard between Responsive and Free-Form Layout.  When you enable Free-Form Layout instead of Responsive layout, you can adjust your dashboard layout with finer-grained control. Adjust your widget sizes and placement, then save your changes to the dashboard. |
| [Scheduled Dashboard Reports](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#Schedule) | You can now select a Delivery Method for your scheduled dashboard reports to include email and SFTP in environments where you allow external users to receive these scheduled deliveries.  SFTP file location delivery is disabled by default. To enable this option in your environment, contact Technical Support. |
| [Embedded Source Events](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#Embedded) | Use the event listener `composer-source-copied` to listen for and react to the event of copying a source in your embedded environment. |
| [Elasticsearch Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#elastic) | Elasticsearch now supports versions 8.1 to 8.17. |

## API Updates

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

| Endpoint | Method | Description |
| --- | --- | --- |
| **25.2.10 API Updates** | | |
| None. |  |  |
| **25.2.9 API Updates** | | |
| None. |  |  |
| **25.2.8 API Updates** | | |
| api/sources/odata/s\_{sourceid} | GET | A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.   * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option. * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.   Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests. |
| **25.2.7 API Updates** | | |
| None. |  |  |
| **25.2.6 API Updates** | | |
| None. |  |  |
| **25.2.5 API Updates** | | |
| None. |  |  |
| **25.2.4 API Updates** | | |
| None. |  |  |
| **25.2.3 API Updates** | | |
| None. |  |  |
| **25.2.2 API Updates** | | |
| None. |  |  |
| **25.2.1 API Updates** | | |
| None. |  |  |
| **25.2 API Updates** | | |
| /api/dashboards/{dashboard\_id}/reports/report\_id/  /api/dashboards/{dashboard\_id}/reports | PUT, POST | You can now add a `destinationType` of `EMAIL` or `FILE_DROP` to support SFTP and SMTP dispatch of scheduled dashboard reports. |

## Resolved Issues

| Title | Description |
| --- | --- |
| **25.2.10 Resolved Issues** | |
| Updates | This service pack includes various internal fixes. |
| **25.2.9 Resolved Issues** | |
| Dashboard & Visual Loading | Corrected an issue in Windows environments where the Edit Dashboard page returned an error when you refreshed or duplicated the browser tab. The dashboard editor now correctly persists its state across page refreshes and duplicate tabs. |
| Authentication Methods | Expanded the documentation provided with the Composer API to include more information about `basicAuth` and `trustedAccessAuth`. |
| Time Zone Display | Fixed an issue where the Time Bar's From and To values could display mismatched time zones in visuals. |
| **25.2.8 Resolved Issues** | |
| Large Data Value Handling in OData | A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.   * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option. * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.   Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests. |
| **25.2.7 Resolved Issues** | |
| Embed Visual Event Trigger | A new setting, `fireOnEveryChange`, is now available for embedded dashboards. Disabled by default, enabling this makes it easier for you to track and respond to all user interactions within a dashboard.  When enabled, dashboards send out change events (`dashboard-level`/`visual-level updates`) every time something is modified: sorting, filtering, visual settings, and more. This gives you more granular visibility into user actions.  When disabled, events were are only triggered once for `dashboard-level`/`visual-level changes`.  Enable in the embed SDK configuration. See [Embedded Events](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932937400973-Embedded-Events). |
| Consul Updates | Consol has been upgraded to version 1.22.1. |
| **25.2.6 Resolved Issues** | |
| Time Bar Settings | You can now enable an time bar option in your environment that allows the time bar slider to snap to the closest interval of the defined granularity for a specific source. This is disabled by default: enable the new server-level variable, **timebar-snap-to-interval** to use in your environment.  See [Server-Level Variables](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932636844045-Server-Level-Variables). |
| US Region Maps | Corrected an issue that prevented display of a US Region Map visual to which a new data column had been added. |
| **25.2.5 Resolved Issues** | |
| Updates | This service pack includes various internal fixes. |
| **25.2.4 Resolved Issues** | |
| Time Bar | By default, the Time Bar will display time information as presented in the associated data source with no offsets or bounds to the time field. If you are using UTC, this is indicated in the time bar. If the time is derived based on other settings, this is indicated in the time bar. |
| Source Selection - Creating Visuals | Corrected an issue that prevented display of source names during visual creation. |
| API Update | Corrected an issue that did not return multiple data type options for aggregation functions such as `LAST_VALUE` from `api/sources/<sourceid>/expression-syntax`. |
| **25.2.3 Resolved Issues** | |
| Dashboard Sharing - Tenants | Corrected an issue in multi-tenant environments that prevented users from sharing dashboards with groups they are not members of. |
| **25.2.2 Resolved Issues** | |
| Scheduled Dashboard Reports to SFTP | The ability to deliver scheduled dashboard reports to an SFTP file location is now disabled by default. [To enable](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932636844045-Server-Level-Variables) this option in your environment, contact Technical Support. |
| Dates in Bar Charts | Corrected an issue that displayed incorrect range dates for weeks as displayed in some bar chart visuals. |
| Importing Sources | Updated the workflows used to import sources to process imports more efficiently, preventing timeouts. |
| Exclude/NOTIN | Corrected an issue that incorrectly excluded records with NULL values instead of only excluding specified values. |
| Spark SQL Connector | Upgrading to this release corrects a driver issue related to connecting to a Databricks source. |
| **25.2.1 Resolved Issues** | |
| Scheduled Dashboard Reports | Corrected a browser issue that prevented scheduled dashboard reports (XLXS and PDF) from being generated due to memory leak under heavy load. |
| Upgraded External Library Files | We’ve upgraded `org.springframework:spring-webmv` from 5.3.26 to 5.3.39 in response to customer requests. |
| **25.2 Resolved Issues** | |
| None. |  |

## Deprecated Features

| Title | Description |
| --- | --- |
| **25.2.10 Deprecated Features** | |
| None. |  |
| **25.2.9 Deprecated Features** | |
| None. |  |
| **25.2.8 Deprecated Features** | |
| None. |  |
| **25.2.7 Deprecated Features** | |
| None. |  |
| **25.2.6 Deprecated Features** | |
| None. |  |
| **25.2.5 Deprecated Features** | |
| None. |  |
| **25.2.4 Deprecated Features** | |
| None. |  |
| **25.2.3 Deprecated Features** | |
| None. |  |
| **25.2.2 Deprecated Features** | |
| None. |  |
| **25.2.1 Deprecated Features** | |
| None. |  |
| **25.2 Deprecated Features** | |
| None. |  |

## Removed Features

| Title | Description |
| --- | --- |
| **25.2.10 Removed Features** | |
| None. |  |
| **25.2.9 Removed Features** | |
| None. |  |
| **25.2.8 Removed Features** | |
| None. |  |
| **25.2.7 Removed Features** | |
| None. |  |
| **25.2.6 Removed Features** | |
| None. |  |
| **25.2.5 Removed Features** | |
| None. |  |
| **25.2.4 Removed Features** | |
| None. |  |
| **25.2.3 Removed Features** | |
| None. |  |
| **25.2.2 Removed Features** | |
| None. |  |
| **25.2.1 Removed Features** | |
| None. |  |
| **25.2 Removed Features** | |
| None. |  |

## Known Issues

| Affected Releases | Description |
| --- | --- |
| **Logi Composer 25.2** and later | None. |
