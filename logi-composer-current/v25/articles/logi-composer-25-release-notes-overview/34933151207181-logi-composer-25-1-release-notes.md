---
title: "Logi Composer 25.1 Release Notes"
id: 34933151207181
section: "Logi Composer  25 Release Notes Overview"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933151207181-Logi-Composer-25-1-Release-Notes
updated_at: 2026-05-26T22:08:34Z
---

# Logi Composer 25.1 Release Notes

# Logi Composer 25.1 Release Notes

This topic describes feature enhancements, resolved issues, and important information for Composer 25.1.

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
| **25.1.11 Feature Enhancements** | |
| None. |  |
| **25.1.10 Feature Enhancements** | |
| None. |  |
| **25.1.9 Feature Enhancements** | |
| None. |  |
| **25.1.8 Feature Enhancements** | |
| None. |  |
| **25.1.7 Feature Enhancements** | |
| None. |  |
| **25.1.6 Feature Enhancements** | |
| None. |  |
| **25.1.5 Feature Enhancements** | |
| None. |  |
| **25.1.4 Feature Enhancements** | |
| None. |  |
| **25.1.3 Feature Enhancements** | |
| None. |  |
| **25.1.2 Feature Enhancements** | |
| None. |  |
| **25.1.1 Feature Enhancements** | |
| None. |  |
| **25.1 Feature Enhancements** | |
| [User Interface Simplification and Updates](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933122669837-Logi-Composer-25-1-Feature-Enhancements#User) | We have added a number of user interface updates to simplify the use of Composer for you. These include changes to the interface to allow you to engage with your environment more easily, improved navigation with accessibility updates, and more.  When you use the UI menu to select an option in Composer, your cursor focus shifts to the section or component you selected and the menu is closed. |
| [Data Zoom Scroll Options for Visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933122669837-Logi-Composer-25-1-Feature-Enhancements#Data) | You can now enable scroll options for visuals that previously did not include axis or zoom  options. Depending on the visual type, the Data Zoom options may include horizontal, vertical, or both scroll options. This includes:   * Line Trend: Attribute Value Charts and Multiple Metric Charts * Bar Charts * Box Plot * Combo Chart * Donut * Floating Bubbles * Heat Map * Pie * Waterfall   Enable or disable as needed in the Data Zoom section of the Settings sidebar menu. Changes to the ruler used in a visual will reset the scroll settings, and the minimum and maximums are not saved. |
| [OData Enhancements](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933122669837-Logi-Composer-25-1-Feature-Enhancements#OData) | We have added support for the `cast` function in OData API filters. You can now cast numeric fields (integers, longs, doubles, decimals) to strings in filter queries, enabling string-based operations such as `eq`, `startswith`, and `contains`. |
| [Dashboard Authors](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933122669837-Logi-Composer-25-1-Feature-Enhancements#Dashboard) | Tenant administrators can now select and change the author for a dashboard in the [Dashboard Library](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932842461581-Use-the-Library-for-Dashboards). The new author must have appropriate permissions for the dashboard to be able to access the dashboard. |

## API Updates

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

| Endpoint | Method | Description |
| --- | --- | --- |
| **25.1.11 API Updates** | | |
| api/sources/odata/s\_{sourceid} | GET | A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.   * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option. * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.   Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests. |
| **25.1.10 API Updates** | | |
| None. |  |  |
| **25.1.9 API Updates** | | |
| None. |  |  |
| **25.1.8 API Updates** | | |
| None. |  |  |
| **25.1.7 API Updates** | | |
| None. |  |  |
| **25.1.6 API Updates** | | |
| None. |  |  |
| **25.1.5 API Updates** | | |
| None. |  |  |
| **25.1.4 API Updates** | | |
| None. |  |  |
| **25.1.3 API Updates** | | |
| None. |  |  |
| **25.1.2 API Updates** | | |
| None. |  |  |
| **25.1.1 API Updates** | | |
| None. |  |  |
| **25.1 API Updates** | | |
| None. |  |  |

## Resolved Issues

| Title | Description |
| --- | --- |
| **25.1.11 Resolved Issues** | |
| Large Data Value Handling in OData | A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.   * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option. * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.   Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests. |
| **25.1.10 Resolved Issues** | |
| Embed Visual Event Trigger | A new setting, `fireOnEveryChange`, is now available for embedded dashboards. Disabled by default, enabling this makes it easier for you to track and respond to all user interactions within a dashboard.  When enabled, dashboards send out change events (`dashboard-level`/`visual-level updates`) every time something is modified: sorting, filtering, visual settings, and more. This gives you more granular visibility into user actions.  When disabled, events were are only triggered once for `dashboard-level`/`visual-level changes`.  Enable in the embed SDK configuration. See [Embedded Events](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932937400973-Embedded-Events). |
| Consul Updates | Consol has been upgraded to version 1.22.1. |
| **25.1.9 Resolved Issues** | |
| Time Bar Settings | You can now enable an time bar option in your environment that allows the time bar slider to snap to the closest interval of the defined granularity for a specific source. This is disabled by default: enable the new server-level variable, **timebar-snap-to-interval** to use in your environment.  See [Server-Level Variables](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932636844045-Server-Level-Variables). |
| US Region Maps | Corrected an issue that prevented display of a US Region Map visual to which a new data column had been added. |
| **25.1.8 Resolved Issues** | |
| Updates | This service pack includes various internal fixes. |
| **25.1.7 Resolved Issues** | |
| Time Bar | By default, the Time Bar will display time information as presented in the associated data source with no offsets or bounds to the time field. If you are using UTC, this is indicated in the time bar. If the time is derived based on other settings, this is indicated in the time bar. |
| Source Selection - Creating Visuals | Corrected an issue that prevented display of source names during visual creation. |
| API Update | Corrected an issue that did not return multiple data type options for aggregation functions such as `LAST_VALUE` from `api/sources/<sourceid>/expression-syntax`. |
| **25.1.6 Resolved Issues** | |
| Dashboard Sharing - Tenants | Corrected an issue in multi-tenant environments that prevented users from sharing dashboards with groups they are not members of. |
| **25.1.5 Resolved Issues** | |
| Dates in Bar Charts | Corrected an issue that displayed incorrect range dates for weeks as displayed in some bar chart visuals. |
| Importing Sources | Updated the workflows used to import sources to process imports more efficiently, preventing timeouts. |
| Exclude/NOTIN | Corrected an issue that incorrectly excluded records with NULL values instead of only excluding specified values. |
| Spark SQL Connector | Upgrading to this release corrects a driver issue related to connecting to a Databricks source. |
| **25.1.4 Resolved Issues** | |
| Cross-Source Linking | When you import dashboards and visuals into your instance, all cross-source links are now appropriately imported and linked. |
| Scheduled Dashboard Reports | Corrected a browser issue that prevented scheduled dashboard reports (XLXS and PDF) from being generated due to memory leak under heavy load. |
| Upgraded External Library Files | We’ve upgraded `org.springframework:spring-webmv` from 5.3.26 to 5.3.39 in response to customer requests. |
| **25.1.3 Resolved Issues** | |
| Scheduled Dashboard Reports | Corrected a browser driver issue that prevented scheduled dashboard reports from being generated due to memory leak under heavy load. |
| SQL Editor | Fixed a user interface layout responsiveness issue, ensuring smooth functionality without affecting other components. |
| Filter Snippets | Corrected an issue that prevented the use of some filter snippets that filter hierarchical data. |
| **25.1.2 Resolved Issues** | |
| Embed Updates | Updated the embed bundle to address various deployment issues. |
| Deployment Updates | The deployment package for Composer has been updated to remove MD5 references to allow for greater flexibility of deployment options in your environment. |
| **25.1.1 Resolved Issues** | |
| Embedded Components | Corrected an issue that returned an error when using a customized inventory table in an embedded environment. |
| Resizing Widgets | Adjusted the behavior of resized widgets to allow them to utilize the full available area. Visuals now expand properly for improved layout and user experience and do not limit element placement. |
| User Interface | In this service pack, we've upgraded the AG Grid version used for the user interface. While this may cause some alignment issues on certain content library pages, the functionality remains unaffected. These issues will be resolved in an upcoming service pack. |
| Embedded Dashboards | Resolved an issue that previously restricted the full visibility of accessing the contextual menus located at the bottom of the embedded dashboards. |
| **25.1 Resolved Issues** | |
| None. |  |

## Deprecated Features

| Title | Description |
| --- | --- |
| **25.1.11 Deprecated Features** | |
| None. |  |
| **25.1.10 Deprecated Features** | |
| None. |  |
| **25.1.9 Deprecated Features** | |
| None. |  |
| **25.1.8 Deprecated Features** | |
| None. |  |
| **25.1.7 Deprecated Features** | |
| None. |  |
| **25.1.6 Deprecated Features** | |
| None. |  |
| **25.1.5 Deprecated Features** | |
| None. |  |
| **25.1.4 Deprecated Features** | |
| None. |  |
| **25.1.3 Deprecated Features** | |
| None. |  |
| **25.1.2 Deprecated Features** | |
| None. |  |
| **25.1.1 Deprecated Features** | |
| None. |  |
| **25.1 Deprecated Features** | |
| None. |  |

## Removed Features

| Title | Description |
| --- | --- |
| **25.1.11 Removed Features** | |
| None. |  |
| **25.1.10 Removed Features** | |
| None. |  |
| **25.1.9 Removed Features** | |
| None. |  |
| **25.1.8 Removed Features** | |
| None. |  |
| **25.1.7 Removed Features** | |
| None. |  |
| **25.1.6 Removed Features** | |
| None. |  |
| **25.1.5 Removed Features** | |
| None. |  |
| **25.1.4 Removed Features** | |
| None. |  |
| **25.1.3 Removed Features** | |
| None. |  |
| **25.1.2 Removed Features** | |
| None. |  |
| **25.1.1 Removed Features** | |
| None. |  |
| **25.1 Removed Features** | |
| None. |  |

## Known Issues

| Affected Releases | Description |
| --- | --- |
| **Logi Composer 25.1** and later | None. |
