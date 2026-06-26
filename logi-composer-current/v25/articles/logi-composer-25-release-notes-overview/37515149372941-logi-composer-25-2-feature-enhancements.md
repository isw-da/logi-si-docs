---
title: "Logi Composer 25.2 Feature Enhancements"
id: 37515149372941
section: "Logi Composer  25 Release Notes Overview"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements
updated_at: 2026-05-26T22:08:33Z
---

# Logi Composer 25.2 Feature Enhancements

# Logi Composer 25.2 Feature Enhancements

This topic provides details about the enhancements in Logi Composer 25.2.

To purchase this product, contact [insightsoftware Sales](mailto:loginewbusinessteam@insightsoftware.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "Sales email address.").

* [Updated Connector Support](#connect)
* [OpenSearch Connector Support](#connect2)
* [Dashboard Filtering and Data Refresh Improvements](#Dashboard)
* [Show and Hide Column Labels](#Metric)
* [Install / Upgrade Operating System Requirements](#Install)
* [Free-Form Widget Placement on Dashboards](#Free-For)
* [Scheduled Dashboard Reports](#Schedule)
* [Embedded Source Events](#Embedded)
* [Elasticsearch Support](#elastic)

To purchase this product, contact [insightsoftware Sales](mailto:loginewbusinessteam@insightsoftware.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "Sales email address.").

## Updated Connector Support

We have updated a number of connectors in this release. Updated connectors include: Oracle, PostgreSQL, the Real Time Sales (RTS) connector, Redshift, and the Snowflake connector. See their respective connector pages for more information.

## OpenSearch Connector Support

We have added support for a new connector, OpenSearch. See [Manage the OpenSearch Connector](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515138873485-Manage-the-OpenSearch-Connector).

## Dashboard Filtering and Data Refresh Improvements

We have added a way for you to enable or disable the auto refresh of data in your single source dashboards as needed.

* Dashboards that include filter snippets from a single source have a new setting, Published Filters.
* When available, select the Published Filters icon on the dashboard and enable or disable the **Auto Apply Filters** toggle.
* **Auto Apply Filters** is enabled by default: any changes you make to your filters are reflected immediately.
* If you are working with several filter snippets and a large data set, you can disable **Auto Apply Filters** to prevent Composer from refreshing the data until you either enable **Auto Apply Filters** again, or select **Apply** in the **Published Filters Setting** work area.

For more information, see [Manage Auto Data Refresh](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149198733-Manage-Auto-Data-Refresh).

## Show and Hide Column Labels

You now have the option to hide some or all of the metric function labels and time zone labels in your table visuals and pivot table visuals. Select relevant show/hide options for individual labels using the table context menu in the column header.

## Install / Upgrade Operating System Requirements

Composer v25.2 no longer supports CentOS 7 or Amazon Linux 7. Update your OS to a later version before upgrading to or installing Composer v25.2, or exclude the `sdk-service` during installation.

## Free-Form Widget Placement on Dashboards

You can now switch the layout of a dashboard between Responsive and Free-Form Layout.

When you enable Free-Form Layout instead of Responsive layout, you can adjust your dashboard layout with finer-grained control. Adjust your widget sizes and placement, then save your changes to the dashboard.

## Scheduled Dashboard Reports

You can now select a Delivery Method for your scheduled dashboard reports to include email and SFTP in environments where you allow external users to receive these scheduled deliveries.

SFTP file location delivery is disabled by default. To enable this option in your environment, contact Technical Support.

## Embedded Source Events

Use the event listener `composer-source-copied` to listen for and react to the event of copying a source in your embedded environment.

## Elasticsearch Support

Elasticsearch now supports versions 8.1 to 8.17.
