---
title: "Logi Composer 25.4 Feature Enhancements"
id: 41964693319821
section: "Logi Composer  25 Release Notes Overview"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/41964693319821-Logi-Composer-25-4-Feature-Enhancements
updated_at: 2026-05-26T22:05:58Z
---

# Logi Composer 25.4 Feature Enhancements

# Logi Composer 25.4 Feature Enhancements

This topic provides details about the enhancements in Logi Composer 25.4.

To purchase this product, contact [insightsoftware Sales](mailto:loginewbusinessteam@insightsoftware.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "Sales email address.").

* [Source Creation Redesign](#Source)
* [OData Updates](#OData)
* [Dashboard and Source Tag Entities](#Dashboar)
* [Composer Bill of Materials](#Composer)
* [Expanded Aggregate Metric Function Support](#Expanded)
* [Time Bar Settings](#Time)
* [Hierarchical Filter State Persistence](#Hierarch)

To purchase this product, contact [insightsoftware Sales](mailto:loginewbusinessteam@insightsoftware.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "Sales email address.").

## Source Creation Redesign

Source creation is now easier than ever with drag and drop source creation. When you create a new source, simply drag the entity or entities you want to use from the Connections tab or Files tab directly onto the Source Creation work area.

Create joins quickly and easily using the visual interface. Select an entity and view its properties in the Properties panel as needed.

The Cache and Global Settings tabs have moved to the top of the work area; select these tabs to define and update your fields and settings at any time. Define a Custom SQL type entity creation directly in the work area.

See [Manage Data Sources](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932941009037-Manage-Data-Sources) and [Define a Source](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932863719309-Define-a-Source).

## OData Updates

Call data using the OData API and return in column format when you use a custom query parameter that includes **response\_format=compact**. See [API Updates](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/41964668259853-Logi-Composer-25-4-Release-Notes#API_Updates).

## Dashboard and Source Tag Entities

Use the `dashboardTag` and `sourceTag` entities to filter dashboard and source lists using the related API or in an embedded environment. You can filter using the operators `IN`, `NOT`, `!=`, `<>`, `AND`, and `OR`.

Use `dashboardTag` in conjunction with Dashboard Interactivity settings to serve and exclude appropriate dashboards to users based on your filter expressions.

## Composer Bill of Materials

You can now access a bill of materials for current and previous releases of Logi Composer by navigating to [https://composer-index.logianalytics.com](https://composer-index.logianalytics.com/ "Logi Composer BOM reference link").

View a listing of all applicable libraries, versions, and associated licenses to help you complete security reviews, verify license compliance, or to understand the underlying technology stack of Composer.

## Expanded Aggregate Metric Function Support

We have expanded aggregate metric function support for all connectors. Use the **listagg** function, for example, as `Listagg(fieldname, 'delimiter')` to concatenate the fields values, separated by the defined delimiter.

Pushdown is supported for multiple connectors:

BigQuery, Impala, MySQL, MemSQL, Oracle, PostgreSQL, Redshift, Snowflake, and SparkSQL.

## Time Bar Settings

You can now enable a time bar option in your environment that allows the time bar slider to snap to the closest interval of the defined granularity for a specific source. This is disabled by default: enable the new server-level variable, **timebar-snap-to-interval** to use in your environment.

See [Server-Level Variables](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932636844045-Server-Level-Variables).

## Hierarchical Filter State Persistence

Hierarchical filters now automatically save your filter configurations, preserving them across sessions.

* Expanded or collapsed nodes are now saved and restored when you return to the dashboard.
* Admins and dashboard owners can set permanent filter selections and expansion states as the default view for all users.
* Your non-owner users can explore filters freely and use "Save As" to create their own dashboard copy with customized settings.
