---
title: "Logi Composer 25.4 Release Notes"
id: 41964668259853
section: "Logi Composer  25 Release Notes Overview"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/41964668259853-Logi-Composer-25-4-Release-Notes
updated_at: 2026-05-26T22:10:35Z
---

# Logi Composer 25.4 Release Notes

# Logi Composer 25.4 Release Notes

This topic describes feature enhancements, resolved issues, and important information for Composer 25.4.

To purchase this product, contact [insightsoftware Sales](mailto:loginewbusinessteam@insightsoftware.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "Sales email address.").

* [Feature Enhancements](#Feature "Feature Enahncements section")
* [Operating System Support](#OS)
* [API Updates](#API_Updates "API Updates section")
* [Resolved Issues](#Resolved)
* [Deprecated Features](#Deprecated_Features)
* [Removed Features](#Removed_Features)

See also [Important Notices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933115853197-Important-Notices), [Deprecated Features](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933137766029-Deprecated-Features), and [Logi Composer Version 25 Summary of Changes](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933145504013-Logi-Composer-Version-25-Summary-of-Changes).

Composer is offered on a quarterly release schedule. The current major release of Composer is v25.4.

## Feature Enhancements

| Title | Description |
| --- | --- |
| **25.4.4 Feature Enhancements** | |
| None. |  |
| **25.4.3 Feature Enhancements** | |
| None. |  |
| **25.4.2 Feature Enhancements** | |
| None. |  |
| **25.4.1 Feature Enhancements** | |
| None. |  |
| **25.4 Feature Enhancements** | |
| [Source Creation Redesign](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/41964693319821-Logi-Composer-25-4-Feature-Enhancements#Source) | Source creation is now easier than ever with drag and drop source creation. When you create a new source, simply drag the entity or entities you want to use from the Connections tab or Files tab directly onto the Source Creation work area.  Create joins quickly and easily using the visual interface. Select an entity and view its properties in the Properties panel as needed.  The Cache and Global Settings tabs have moved to the top of the work area; select these tabs to define and update your fields and settings at any time. Define a Custom SQL type entity creation directly in the work area.  See [Manage Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932941009037-Manage-Data-Sources) and [Define a Source](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932863719309-Define-a-Source). |
| [OData Updates](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/41964693319821-Logi-Composer-25-4-Feature-Enhancements#OData) | Call data using the OData API and return in column format when you use a custom query parameter that includes **response\_format=compact**. See API Updates. |
| [Dashboard and Source Tag Entities](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/41964693319821-Logi-Composer-25-4-Feature-Enhancements#Dashboar) | Use the `dashboardTag` and `sourceTag` entities to filter dashboard and source lists using the related API or in an embedded environment. You can filter using the operators `IN`, `NOT`, `!=`, `<>`, `AND`, and `OR`.  Use `dashboardTag` in conjunction with Dashboard Interactivity settings to serve and exclude appropriate dashboards to users based on your filter expressions. |
| [Composer Bill of Materials](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/41964693319821-Logi-Composer-25-4-Feature-Enhancements#Composer) | You can now access a bill of materials for current and previous releases of Logi Composer by navigating to [https://composer-index.logianalytics.com](https://composer-index.logianalytics.com/ "Logi Composer BOM reference link").  View a listing of all applicable libraries, versions, and associated licenses to help you complete security reviews, verify license compliance, or to understand the underlying technology stack of Composer. |
| [Expanded Aggregate Metric Function Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/41964693319821-Logi-Composer-25-4-Feature-Enhancements#Expanded) | We have expanded aggregate metric function support for all connectors. Use the **listagg** function, for example, as `Listagg(fieldname, 'delimiter')` to concatenate the fields values, separated by the defined delimiter.  Pushdown is supported for multiple connectors:  BigQuery, Impala, MySQL, MemSQL, Oracle, PostgreSQL, Redshift, Snowflake, and SparkSQL. |
| [Time Bar Settings](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/41964693319821-Logi-Composer-25-4-Feature-Enhancements#Time) | You can now enable a time bar option in your environment that allows the time bar slider to snap to the closest interval of the defined granularity for a specific source. This is disabled by default: enable the new server-level variable, **timebar-snap-to-interval** to use in your environment.  See [Server-Level Variables](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932636844045-Server-Level-Variables). |
| [Hierarchical Filter State Persistence](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/41964693319821-Logi-Composer-25-4-Feature-Enhancements#Hierarch) | Hierarchical filters now automatically save your filter configurations, preserving them across sessions.   * Expanded or collapsed nodes are now saved and restored when you return to the dashboard. * Admins and dashboard owners can set permanent filter selections and expansion states as the default view for all users. * Your non-owner users can explore filters freely and use "Save As" to create their own dashboard copy with customized settings. |

## Operating System Support

*List Updated: 01 December 2025*

**Important:** This information is provided to assist you in planning your future upgrade projects.

**Caution:** Running an older, unsupported operating system in your environment is done so at your own risk. Plan and upgrade to a supported operating system for full support and functionality.

* RHEL 9 (Red Hat)
* CentOS Stream 9

  **Note:** CentOS 7 & 8 are end of life (EOL) support. CentOS Stream 9 is supported for new instances of Logi Composer 25.4 and higher. Upgrade your operating system to CentOS Stream 9 before upgrading your Composer instance.
* Ubuntu 18.04, 20.04, and Ubuntu 22.04.

  **Note:** Ubuntu 16.04 is nearing end of life (EOL) support. Composer will support Ubuntu 16.04 through the release of Composer 25.3. Composer 25.4 and later will require an operating system upgrade before you upgrade your Composer instance.
* Windows Server versions 2016 and 2019 or higher.

For more information on current and future planned operating system support information, see [Operating System Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/39993525943181-Operating-System-Support).

## API Updates

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

| Endpoint | Method | Description |
| --- | --- | --- |
| **25.4.4 API Updates** | | |
| None. |  |  |
| **25.4.3 API Updates** | | |
| None. |  |  |
| **25.4.2 API Updates** | | |
| api/sources/odata/s\_{sourceid} | GET | A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.   * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option. * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.   Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests. |
| **25.4.1 API Updates** | | |
| None. |  |  |
| **25.4 API Updates** | | |
| api/sources/odata/s\_{sourceid} | GET | A new query parameter, **response\_format=compact**, has been added to the existing OData API endpoint: **/api/sources/odata/s\_{sourceid}?response\_format=compact**.  When you include this parameter in your query, the API returns data in a more efficient, compact JSON format. The reduced size of the response payload increases the speed of data transfer. |

## Resolved Issues

| Title | Description |
| --- | --- |
| **25.4.4 Resolved Issues** | |
| Updates | This service pack includes various internal fixes. |
| **25.4.3 Resolved Issues** | |
| Dashboard & Visual Loading | Corrected an issue in Windows environments where the Edit Dashboard page returned an error when you refreshed or duplicated the browser tab. The dashboard editor now correctly persists its state across page refreshes and duplicate tabs. |
| Authentication Methods | Expanded the documentation provided with the Composer API to include more information about `basicAuth` and `trustedAccessAuth`. |
| Time Zone Display | Fixed an issue where the Time Bar's From and To values could display mismatched time zones in visuals. |
| **25.4.2 Resolved Issues** | |
| Large Data Value Handling in OData | A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.   * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option. * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.   Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests. |
| **25.4.1 Resolved Issues** | |
| Embed Visual Event Trigger | A new setting, `fireOnEveryChange`, is now available for embedded dashboards. Disabled by default, enabling this makes it easier for you to track and respond to all user interactions within a dashboard.  When enabled, dashboards send out change events (`dashboard-level`/`visual-level updates`) every time something is modified: sorting, filtering, visual settings, and more. This gives you more granular visibility into user actions.  When disabled, events were are only triggered once for `dashboard-level`/`visual-level changes`.  Enable in the embed SDK configuration. See [Embedded Events](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932937400973-Embedded-Events). |
| DNS Name Change Configuration | When updating the Composer site DNS name, ensure the correct base URL is configured in:   * Zoomdata properties file (on-premise Linux) * Helm charts (Kubernetes) * Zoomdata properties file (on-premise Windows)   This resolves site errors that occur after DNS name changes. |
| Consul Updates | Consol has been upgraded to version 1.22.1. |
| **25.4 Resolved Issues** | |
| None. |  |

## Deprecated Features

| Title | Description |
| --- | --- |
| **25.4.4 Deprecated Features** | |
| None. |  |
| **25.4.3 Deprecated Features** | |
| None. |  |
| **25.4.2 Deprecated Features** | |
| None. |  |
| **25.4.1 Deprecated Features** | |
| None. |  |
| **25.4 Deprecated Features** | |
| None. |  |

## Removed Features

| Title | Description |
| --- | --- |
| **25.4.4 Removed Features** | |
| None. |  |
| **25.4.3 Removed Features** | |
| None. |  |
| **25.4.2 Removed Features** | |
| None. |  |
| **25.4.1 Removed Features** | |
| None. |  |
| **25.4 Removed Features** | |
| None. |  |

## Known Issues

| Affected Releases | Description |
| --- | --- |
| **Logi Composer 25.4** and later | * When you install Composer v25.3 or v25.4 in an Ubuntu 18 environment, the application does not deploy as expected. * When you attempt to upgrade Composer to v25.4, the Sources work area may not load in Windows server deployments or Linux RHEL 9 server deployments. To resolve the error, clear your browser’s cache and reload and access the resource again. * When you install Composer v25.4, entities may not be available in the Cloudera Search sources for new connections. |
