---
title: "Software Updates Through Composer 26 "
id: 43701147670285
section: "Logi Composer  26 Release Notes Overview"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701147670285-Software-Updates-Through-Composer-26
updated_at: 2026-05-29T14:09:20Z
---

# Software Updates Through Composer 26 

# Software Updates Through Composer 26

Changes made over time to Logi Composer are included here to help you plan upgrades from older releases.

**Caution:** Running an older, unsupported operating system in your environment is done so at your own risk. Plan and upgrade to a supported operating system for full support and functionality. For information on operating system and environment support, see [Operating System Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136004365-Operating-System-Support).

To purchase this product, contact [insightsoftware Sales](mailto:loginewbusinessteam@insightsoftware.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "Sales email address.").

* [Feature Enhancements](#Feature)

  + [Composer v26](#v26)
  + [Composer v25](#v25)
  + [Composer v24](#v24)
  + [Composer v23](#v23)
  + [Composer v22](#v22)
  + [Composer v8.4 and Earlier](#v8)
  + [Composer v7.10 and Earlier](#v7)
  + [Composer v6.9 and Earlier](#v6)
* [Resolved Issues](#Resolved)

  + [Composer v26](#v263)
  + [Composer v25](#v253)
  + [Composer v24](#v243)
  + [Composer v23](#v233)
  + [Composer v22](#v223)
  + [Composer v8.4 and Earlier](#v843)
  + [Composer v7.10 and Earlier](#v7103)
  + [Composer v6.9 and Earlier](#v693)

## Feature Enhancements

### Composer v26

| Title | Description |
| --- | --- |
| Composer **26.1.2 Feature Enhancements** | |
| None. |  |
| **Composer** **26.1.1 Feature Enhancements** | |
| None. |  |
| **Composer** **26.1 Feature Enhancements** | |
| [Source Creation Updates](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#Source) | Source creation work area updates make it easier for you to add derived fields, hierarchies, upload translation files, and update field capabilities. Select an output node in the Source Creation canvas, and expand the Options menu to select and perform your task. |
| [Tenant Management Updates](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#Tenant) | The workflow for tenant creation and updates has been expanded and extended for easy management and maintenance.  Set up the **Reply-To Email** and **Sender Display Name** in this expanded work area as a tenant attribute if needed for sharing dashboard reports and self service reports.  Additionally, you can return reserved tenant attributes using the new endpoint, `api/account-attributes/reserved/`. |
| [Interactivity Overrides](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#Interact) | Interactivity overrides have been updated to accommodate the updated source creation workflow. |
| [Mapbox Style & Satellite Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#Mapbox) | You can now enter a [supported style ID](https://docs.mapbox.com/api/maps/styles/ "supported style ID") when you define MapBox as a Tile Provider in a source for map visuals.  An additional option for display of map visuals, satellite mode, is available for supported map tile providers. |
| [Numeric Ratios](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#Numeric) | A new Ratio format is now available in the numeric format selector. Decimal values are expressed as a normalized ratio against one. For example, 0.5 renders as 1:2, 0.3333… as 1:3. This format is supported across all visuals that accept a numeric field. |
| [PDF Generation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#PDF) | The underlying component we use to generate PDFs, jspdf, has been updated from 2.5.2 to 3.0.1. This upgrade is compatible with most current browsers, excluding Internet Explorer. |
| [UI Improvements](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#UI) | Adjust your columns of truncated fields in the Visual Gallery, the dashboards Library, and the Sources work areas. Select to drag and resize the width of the Name, Tags, and Data Source columns as you navigate among your resources. |
| [Dependency & Tooling Upgrades](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#Dependen) | Upgraded core dependencies for improved performance and security:   * Node.js to 20.12.0 * Yarn to 4.9.2 (Berry/Corepack) * npm to10.5.0 * TypeScript to 5.4.0 * Jest-circus to 29.7.0 (replaces deprecated Jasmine) |
| [Spring Boot Updates](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#Spring) | We have upgraded the underlying Spring Boot framework to 3.5.5 across the platform. This infrastructure update provides enhanced security compliance and compatibility with modern development standards. |

[Return to top](#top "return to top")

### Composer v25

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
| Source Creation Redesign | Source creation is now easier than ever with drag and drop source creation. When you create a new source, simply drag the entity or entities you want to use from the Connections tab or Files tab directly onto the Source Creation work area.  Create joins quickly and easily using the visual interface. Select an entity and view its properties in the Properties panel as needed.  The Cache and Global Settings tabs have moved to the top of the work area; select these tabs to define and update your fields and settings at any time. Define a Custom SQL type entity creation directly in the work area.  See [Manage Data Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068934669-Manage-Data-Sources) and [Define a Source](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080450061-Define-a-Source). |
| OData Updates | Call data using the OData API and return in column format when you use a custom query parameter that includes **response\_format=compact**. See API Updates. |
| Dashboard and Source Tag Entities | Use the `dashboardTag` and `sourceTag` entities to filter dashboard and source lists using the related API or in an embedded environment. You can filter using the operators `IN`, `NOT`, `!=`, `<>`, `AND`, and `OR`.  Use `dashboardTag` in conjunction with Dashboard Interactivity settings to serve and exclude appropriate dashboards to users based on your filter expressions. |
| Composer Bill of Materials | You can now access a bill of materials for current and previous releases of Logi Composer by navigating to [https://composer-index.logianalytics.com](https://composer-index.logianalytics.com/ "Logi Composer BOM reference link").  View a listing of all applicable libraries, versions, and associated licenses to help you complete security reviews, verify license compliance, or to understand the underlying technology stack of Composer. |
| Expanded Aggregate Metric Function Support | We have expanded aggregate metric function support for all connectors. Use the **listagg** function, for example, as `Listagg(fieldname, 'delimiter')` to concatenate the fields values, separated by the defined delimiter.  Pushdown is supported for multiple connectors:  BigQuery, Impala, MySQL, MemSQL, Oracle, PostgreSQL, Redshift, Snowflake, and SparkSQL. |
| Time Bar Settings | You can now enable a time bar option in your environment that allows the time bar slider to snap to the closest interval of the defined granularity for a specific source. This is disabled by default: enable the new server-level variable, **timebar-snap-to-interval** to use in your environment.  See [Server-Level Variables](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables). |
| Hierarchical Filter State Persistence | Hierarchical filters now automatically save your filter configurations, preserving them across sessions.   * Expanded or collapsed nodes are now saved and restored when you return to the dashboard. * Admins and dashboard owners can set permanent filter selections and expansion states as the default view for all users. * Your non-owner users can explore filters freely and use "Save As" to create their own dashboard copy with customized settings. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **25.3.7 Feature Enhancements** | |
| None. |  |
| **25.3.6 Feature Enhancements** | |
| None. |  |
| **25.3.5 Feature Enhancements** | |
| None. |  |
| **25.3.4 Feature Enhancements** | |
| None. |  |
| **25.3.3 Feature Enhancements** | |
| None. |  |
| **25.3.2 Feature Enhancements** | |
| None. |  |
| **25.3.1 Feature Enhancements** | |
| None. |  |
| **25.3 Feature Enhancements** | |
| Scheduled Dashboard Reports - Tenants | Users with appropriate permissions can specify a "Reply-To" and "Sender Display Name" for the emails generated for your scheduled dashboard reports.  This flexibility allows you to direct replies to your selected recipient and include a user-friendly sender display name for ease of use by your end users. If not defined, this defaults to the system values.  Additionally, the Accounts API has been updated so you can retrieve and define all tenant configuration information, including SFTP file drop and STMP details.  See API Updates. |
| User Interface Flexibility | We have introduced a number of flexible improvements to the user interface. When you work in some pop-up modals, you can resize some common columns to see more of the information about the resources you are using. Use your cursor to grab a column header break to adjust as needed.  These pop-ups include Dashboard Alerts, Dashboard Sharing, and Permissions for Sources, Visuals, and Dashboards. |
| Customize Label Color | You can now customize the label color for the combo chart visual in Composer if you do not want to use the themed color. Disable **Inherit from theme** in the Colors sidebar menu, then select the color you wish to use. |

[Return to top](#top "return to top")

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
| Updated Connector Support | We have updated a number of connectors in this release. Updated connectors include: Oracle, PostgreSQL, the Real Time Sales (RTS) connector, Redshift, and the Snowflake connector. See their respective connector pages for more information. |
| OpenSearch Connector Support | We have added support for a new connector, OpenSearch. See [Manage the OpenSearch Connector](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074183053-Manage-the-OpenSearch-Connector). |
| Dashboard Filtering and Data Refresh Improvements | We have added a way for you to enable or disable the auto refresh of data in your single source dashboards as needed.   * Dashboards that include filter snippets from a single source have a new setting, Published Filters. * When available, select the Published Filters icon on the dashboard and enable or disable the **Auto Apply Filters** toggle. * **Auto Apply Filters** is enabled by default: any changes you make to your filters are reflected immediately. * If you are working with several filter snippets and a large data set, you can disable **Auto Apply Filters** to prevent Composer from refreshing the data until you either enable **Auto Apply Filters** again, or select **Apply** in the **Published Filters Setting** work area.   For more information, see [Manage Auto Data Refresh](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701133177101-Manage-Auto-Data-Refresh). |
| Show and Hide Column Labels | You now have the option to hide some or all of the metric function labels and time zone labels in your table visuals and pivot table visuals. Select relevant show/hide options for individual labels using the table context menu in the column header. |
| Install / Upgrade Operating System Requirements | Composer v25.2 no longer supports CentOS 7 or Amazon Linux 7. Update your OS to a later version before upgrading to or installing Composer v25.2, or exclude the `sdk-service` during installation. |
| Free-Form Widget Placement on Dashboards | You can now switch the layout of a dashboard between Responsive and Free-Form Layout.  When you enable Free-Form Layout instead of Responsive layout, you can adjust your dashboard layout with finer-grained control. Adjust your widget sizes and placement, then save your changes to the dashboard. |
| Scheduled Dashboard Reports | You can now select a Delivery Method for your scheduled dashboard reports to include email and SFTP in environments where you allow external users to receive these scheduled deliveries.  SFTP file location delivery is disabled by default. To enable this option in your environment, contact Technical Support. |
| Embedded Source Events | Use the event listener `composer-source-copied` to listen for and react to the event of copying a source in your embedded environment. |
| Elasticsearch Support | Elasticsearch now supports versions 8.1 to 8.17. |

[Return to top](#top "return to top")

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
| User Interface Simplification and Updates | We have added a number of user interface updates to simplify the use of Composer for you. These include changes to the interface to allow you to engage with your environment more easily, improved navigation with accessibility updates, and more.  When you use the UI menu to select an option in Composer, your cursor focus shifts to the section or component you selected and the menu is closed. |
| Data Zoom Scroll Options for Visuals | You can now enable scroll options for visuals that previously did not include axis or zoom  options. Depending on the visual type, the Data Zoom options may include horizontal, vertical, or both scroll options. This includes:   * Line Trend: Attribute Value Charts and Multiple Metric Charts * Bar Charts * Box Plot * Combo Chart * Donut * Floating Bubbles * Heat Map * Pie * Waterfall   Enable or disable as needed in the Data Zoom section of the Settings sidebar menu. Changes to the ruler used in a visual will reset the scroll settings, and the minimum and maximums are not saved. |
| OData Enhancements | We have added support for the `cast` function in OData API filters. You can now cast numeric fields (integers, longs, doubles, decimals) to strings in filter queries, enabling string-based operations such as `eq`, `startswith`, and `contains`. |
| Dashboard Authors | Tenant administrators can now select and change the author for a dashboard in the [Dashboard Library](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047640717-Use-the-Library-for-Dashboards). The new author must have appropriate permissions for the dashboard to be able to access the dashboard. |

[Return to top](#top "return to top")

### Composer v24

| Title | Description |
| --- | --- |
| **Composer 24.4.15 Feature Enhancements** | |
| None. |  |
| **Composer 24.4.14 Feature Enhancements** | |
| None. |  |
| **Composer 24.4.13 Feature Enhancements** | |
| None. |  |
| **Composer 24.4.12 Feature Enhancements** | |
| None. |  |
| **Composer 24.4.11 Feature Enhancements** | |
| None. |  |
| **Composer 24.4.10 Feature Enhancements** | |
| None. |  |
| **Composer 24.4.9 Feature Enhancements** | |
| None. |  |
| **Composer 24.4.8 Feature Enhancements** | |
| None. |  |
| **Composer 24.4.7 Feature Enhancements** | |
| None. |  |
| **Composer 24.4.6 Feature Enhancements** | |
| None. |  |
| **Composer 24.4.5 Feature Enhancements** | |
| None. |  |
| **Composer 24.4.4 Feature Enhancements** | |
| None. |  |
| **Composer 24.4.3 Feature Enhancements** | |
| None. |  |
| **Composer 24.4.2 Feature Enhancements** | |
| None. |  |
| **Composer 24.4.1 Feature Enhancements** | |
| None. |  |
| **Composer 24.4 Feature Enhancements** | |
| Improved Hierarchical Filter Management | We have improved your experience and expanded the capabilities of hierarchical filters, making data sets of all sizes more easily navigable.   * Use the expand and collapse icons to more readily find parent and child nodes. * Select and deselect items and nodes easily. * The new **Expand All** option allows you to expand and collapse the entire data set quickly to make or review changes. |
| Updated Data Connector Support | Several new data connectors are available or have been updated to allow your users to connect to a wider range of sources.   * Amazon Simple Storage Service Connector (S3) now supports the S3A protocol. See [Manage the Amazon S3 Connector](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701009509517-Manage-the-Amazon-S3-Connector). * You can now add the IBM DB2 Connector in your Composer environment. * We have added support for the Business Central Connector. See [Manage the Business Central Jet Connector](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701057330957-Manage-the-Business-Central-Jet-Connector). |
| Table Visuals Update | Define the columns you want to include in a table visual when you create the visual. After you have selected your source and the table visual type, select to include one or more columns quickly and easily. Select **Create Visual** to generate your visual. If you select no columns, all columns are included by default.  See [Tables](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701131849357-Tables). |
| Export Dates in ISO 8601 Format | You now have the option to export and share dates as an ISO 8601 date in XLSX format. This preserves any formatting have applied to your data while allowing Excel users to recognize and manipulate the exported dates as dates in Excel.  See [Export Raw Data in CSV or XLSX Format](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701214677901-Export-Raw-Data-in-CSV-or-XLSX-Format) and [Schedule a Dashboard Report](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093791245-Schedule-a-Dashboard-Report). |
| Scheduled Reports Frequency | A new frequency option for sending scheduled dashboard reports, **Days**, allows you to schedule a report for generation and sharing on more than one day a week with a few simple selections. Create a new schedule or edit an existing schedule to meet your needs.  See [Schedule a Dashboard Report](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093791245-Schedule-a-Dashboard-Report). |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 24.3.10 Feature Enhancements** | |
| None. |  |
| **Composer 24.3.9 Feature Enhancements** | |
| None. |  |
| **Composer 24.3.8 Feature Enhancements** | |
| None. |  |
| **Composer 24.3.7 Feature Enhancements** | |
| None. |  |
| **Composer 24.3.6 Feature Enhancements** | |
| None. |  |
| **Composer 24.3.5 Feature Enhancements** | |
| None. |  |
| **Composer 24.3.4 Feature Enhancements** | |
| None. |  |
| **Composer 24.3.3 Feature Enhancements** | |
| None. |  |
| **Composer 24.3.2 Feature Enhancements** | |
| None. |  |
| **Composer 24.3.1 Feature Enhancements** | |
| None. |  |
| **Composer 24.3 Feature Enhancements** | |
| Expanded Dashboard Sharing | We have made it easier to share your dashboards with your users in Composer . Now you can optionally share dashboards with established groups and users in your tenant at once, making the objects available to users within those groups and tenants easily.  For more information see [Share a Dashboard with Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701077162637-Share-a-Dashboard-with-Users). |
| CentOS / Red Hat Linux Support | Composer now supports installation to CentOS Stream 9. CentOS 7 and CentOS 8, which have reached end of life, are no longer supported. Contact technical support for assistance in upgrading your environment to run on CentOS Stream 9 or other supported version of Red Hat Enterprise Linux. |
| Regional Setting - Australia | You can now select Australia as a regional preset when you define regional settings for your users. |
| PostgreSQL Support | Composer now uses PostgreSQL 16 by default for new installations. You can now upgrade to this version in existing installations as needed. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 24.2.12 Feature Enhancements** | |
| None. |  |
| **Composer 24.2.11 Feature Enhancements** | |
| None. |  |
| **Composer 24.2.10 Feature Enhancements** | |
| None. |  |
| **Composer 24.2.9 Feature Enhancements** | |
| None. |  |
| **Composer 24.2.8 Feature Enhancements** | |
| None. |  |
| **Composer 24.2.7 Feature Enhancements** | |
| None. |  |
| **Composer 24.2.6 Feature Enhancements** | |
| None. |  |
| **Composer 24.2.5 Feature Enhancements** | |
| None. |  |
| **Composer 24.2.4 Feature Enhancements** | |
| None. |  |
| **Composer 24.2.3 Feature Enhancements** | |
| None. |  |
| **Composer 24.2.2 Feature Enhancements** | |
| None. |  |
| **Composer 24.2.1 Feature Enhancements** | |
| None. |  |
| **Composer 24.2 Feature Enhancements** | |
| Source Creation Enhancements | We have enhanced the user experience for source creation by introducing visualization of data relationships for schemas.   * Navigate to the **Relationship** tab for a specific connection, then select a schema from the available schemas to view or edit the relationships for each. * Select a schema and view the relationships in read only mode for your data sources in the Entity Details work area for that data source. * When you are working with joins, view available joins and create new joins as needed. Recommended joins and joins you add are visible in the join relationship visualization; from there you can draw new joins according to your specific needs. * Visualization is available for multiple connection types. For Postgres connections, Composer provides tables and default database relationship data from the connection.   For more information, see [Visualize Schemas and Joins](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701038666125-Visualize-Schemas-and-Joins), [Source Creation Tab](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701080568205-Source-Creation-Tab), and [Visualize Joins](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072201741-Create-a-Fusion-Source#Visualiz). |
| Export Numeric Fields and Dates | Exporting raw or visual data from visuals created in Composer to XLSX format now outputs numeric and date fields in number and date format. |
| Breaking Changes Management | We have expanded change management for breaking changes by adding your warning tags to sources or other objects, even if there are no other top level dependencies to that object.  See [Import or Export Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701098185613-Import-or-Export-Sources). |
| Import Matching Strategy Improvements | When you migrate and import objects into your environment, you can define a matching strategy that uses multiple approaches to reviewing objects to determine how to handle them in conjunction with your selected insertion strategy.  Matching strategies are processed in order, proceeding to the next and the next if a strategy fails.  If all strategies fail, the object is imported and tagged with your selected tags to help you find affected objects and manage any issues.  These attributes are used to define the matching strategy and warning tags to use for import.  See [Import Dashboards](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093507213-Import-Dashboards), [Import Visual Gallery Visuals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701214789517-Import-Visual-Gallery-Visuals), and [Import or Export Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701098185613-Import-or-Export-Sources). |
| Improved Line Chart Performance | The data display of line charts in Composer now supports rendering of large data sets more quickly by halting the calculation of values and percentages for data lengths over 130,000.  When this threshold is reached, the **Display as stacked** option is disabled. Work with Support if you need to change the setting of `data-threshold` from the default of 130,000. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **24.1.12 Feature Enhancements** | |
| None. |  |
| **24.1.11 Feature Enhancements** | |
| None. |  |
| **24.1.10 Feature Enhancements** | |
| None. |  |
| **24.1.9 Feature Enhancements** | |
| None. |  |
| **24.1.8 Feature Enhancements** | |
| None. |  |
| **24.1.7 Feature Enhancements** | |
| None. |  |
| **24.1.6 Feature Enhancements** | |
| None. |  |
| **24.1.5 Feature Enhancements** | |
| None. |  |
| **24.1.4 Feature Enhancements** | |
| None. |  |
| **24.1.3 Feature Enhancements** | |
| None. |  |
| **24.1.2 Feature Enhancements** | |
| SAP S/4HANA Support | Composer now includes an SAP S/4HANA connector. See [Manage the SAP S/4HANA Connector](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700996045069-Manage-the-SAP-S-4HANA-Connector). |
| **24.1.1 Feature Enhancements** | |
| None. |  |
| **24.1 Feature Enhancements** | |
| Enhanced Filter Security Capabilities | We have expanded the filter capabilities to present data more securely to your users. Filter values can be shown in masked format if you want to filter based on confidential data.   * To enable, disable **Filtering** for fields in a data source for one or more data columns on the **Fields** tab of that data source. * Next, set the Value and Display fields in your filter snippets based on your needs. * When you view tool tips or hover over fields that have Filtering disabled, you will not see the actual values. Instead, you will see a generic reference, such as a count of "filter values" or a series of asterisks `******`.   **Important:** Applied filter values that later have **Filtering** disabled to not automatically mask or hide those fields. You must recreate the filter that uses these values.  You can now set and apply filters to filter snippets. Select a source to apply the filter in the filter snippet.  See [Filter Data With Masked Fields](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701108947981-Filter-Data-With-Masked-Fields). |
| Lite Dashboard for Self-Service Environments | We have added a simplified lite dashboard to your Composer environment. You can now embed a lite dashboard complete with its own interactivity settings, designed to get your users up and running quickly and easily.  Users can create dashboards with the default visual format as a table visual. Once created, users can:   * Edit the visual's fields and settings, and optionally change the visual type to an available visual type. * Select an available visual type if the data source does not support a table visual, then edit the visual as needed.   Available visual types include: Table (default), Bars, Bars:Multiple Metrics, Donut, KPI, Packed Bubbles, Pie. Customize this list further in your embed code as needed to add or remove other visual types. |
| Suppress Time Zone Labels | You can now opt to suppress time zone labels in the Composer user interface.  After upgrading to this version, you can [update the Data Details](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701116424973-Manage-Fields#Settings) of your time fields in a data source and suppress the labels. Select **Not Specified** instead of a time zone to hide time zone information in the user interface and when users export data. |
| Content Migration Flow Improvements and Breaking Changes Management Expansion | * You can now import and export visuals directly in the Visual Gallery user interface. Import and export one or more visuals in bulk. Import and Export includes any supporting objects the visuals are dependent on, such as data sources and connections. * When you import dashboards, visuals, and sources, Content Distributor group members and other users with appropriate privileges can enable **Share Default Access With All Users**. When enabled, in the UI or as an API option, users in the tenants you selected for import can access to these resources immediately based on default access levels. * View improved real-time import validation results, address errors, and suppress warnings for later handling with more options to correct issues in your environment. * The import process now considers an `origin.id` when importing objects: it is stored for every imported object on the target system.    + When you import using the API, you can select a matching strategy for reusing and updating objects. * When you select **Ignore Warnings** during import, a Tags field is added to the Import work area. Add or create tags to apply to objects that do not import cleanly.    + If errors occur during import, Composer adds the tags you select to affected objects.   + Use these tags to find the dashboards, visuals, filter snippets, or sources you need to fix. * You can also create or add tags for items that do not import cleanly when you import via API. |

[Return to top](#top "return to top")

### Composer v23

| Title | Description |
| --- | --- |
| **23.4.13 Feature Enhancements** | |
| Export Dates in ISO 8601 Format | You now have the option to export and share dates as an ISO 8601 date in XLSX format. |
| **23.4.12 Feature Enhancements** | |
| None. |  |
| **23.4.11 Feature Enhancements** | |
| None. |  |
| **23.4.10 Feature Enhancements** | |
| None. |  |
| **23.4.9 Feature Enhancements** | |
| None. |  |
| **23.4.8 Feature Enhancements** | |
| None. |  |
| **23.4.7 Feature Enhancements** | |
| None. |  |
| **23.4.6 Feature Enhancements** | |
| None. |  |
| **23.4.5 Feature Enhancements** | |
| None. |  |
| **23.4.4 Feature Enhancements** | |
| Extended Elasticsearch Support | Composer now supports Elasticsearch versions 8.1 through 8.11. |
| **23.4.3 Feature Enhancements** | |
| None. |  |
| **23.4.2 Feature Enhancements** | |
| None. |  |
| **23.4.1 Feature Enhancements** | |
| Prebuilt User Credentials - ${User.credentials} | Use the new user attribute, `${User.credentials}`, to pass the Composer session ID (when working in Composer directly) or trusted access token (in embedded environments) through a connection to a data source.  If this attribute is found on upgrade, the existing attribute is renamed to `${User.Custom_Credentials}`, allowing use of `${User.credentials}` as designed. |
| **23.4 Feature Enhancements** | |
| Tenant Administration and Content Creation/Distribution Enhancements | With this release, Composer transforms your approach to tenant administration and content creation and distribution among different Composer tenants. Leverage the power of a centralized hub system administrators and content distributors use to push content to your supported tenants.  **Key Features:**   1. A unified content area allows your content creators to create and distribute new content to multiple tenants easily. Create, modify, and effortlessly push dashboards and visualizations to different tenants. Seamlessly update existing content by pushing the changes where needed. If no additional tenants are added, the default tenant `Visual Data Discovery` is used. `Visual Data Discovery` replaces the `company` tenant. 2. **Multi-tenancy enhancement**. Streamlined tenant creation and content management means you can create tenants directly, then push the content you want them to see all from one place. 3. **Updated Group Roles**. You can now easily add users in a tenant to specific groups that allow these users to manage and create, share, and maintain content as needed.     * Members of the **Content Distributors** group can create, maintain, and distribute content to any tenants. 4. **Unified Administration**. A new default user account, the system administrator wields the combined supervisor and admin capabilities. The system administrator can perform all tasks necessary to Composer management. This change means:     * The **superaccount** work area is renamed to **Visual Data Discovery**.    * The company tenant is no longer created by Composer for new installations, existing company tenants remain unchanged.    * The default admin user is now the **system administrator** and has all supervisor user privileges, as a member of the **Visual Data Discovery** tenant.    * The default **supervisor** user is no longer installed; add users to the **Supervisors** group instead.    * Tenant Accounts are now known as Tenants in the user interface. |
| Enhanced Content Migration Flow | Streamline your content migration flow with the enhanced objects Export and Import Process:   * Benefit from the bulk import and export of dashboards and sources; select tenants to include at import. * Choose an import strategy per object class — create a new version of the object, reuse the object, or update the existing version on the target environment while preserving permissions and IDs. * View real-time import validation results, address errors, and suppress warnings for later handling. |
| Breaking Changes Management | Composer now offers more robust breaking changes management when working with changes to data types and sources for fields or schemas in use by dashboards, visuals, and filter snippets.  When you make changes to a data source in use such as:   * Changing the data type of a source field, derived field, or custom metric * Removing fields from inclusion in a data source * Changing the schema in use in a data source   Composer returns a verbose series of warnings about making such breaking changes. Review the returned list of affected visuals and filter snippets, and then decide to abort the change or proceed by selecting **Ignore Warnings**. Once you have saved your changes, navigate to the affected visuals and filter snippets to update the field used by each.  This works with conditional formatting, and when changing between all data types. |
| Data Gateway Service | Use the Data Gateway service to connect to your on-premise data sources from an instance of Composer running in the cloud. Install Data Gateway on your local network and by configuring Composer allow connection to the on-premise data sources of your choice. |
| Azure SQL Data Warehouse (Azure Synapse) | Offset is now supported when you connect to the Azure SQL Data Warehouse (Azure Synapse) using the Microsoft SQL Server connector. |
| Expanded Search Options for Managing and Adding Visuals | More search and select options are available when you add an existing Visual Gallery visual to your dashboards. Expanded search options means you can:   * Search for visuals by Type, Name, Description, Data Source, Tags, or Author. * Narrow the visuals shown or returned in search by selecting a filter option: All, Favorites, My Items, or Shared with Me. * If you search by tags, type, or data source, you can include multiple items in your search, returning all visuals that include at least one matching result. |
| Descriptions for Visuals | Use the analytics capabilities of Composer to generate descriptions of your visuals to dashboards with a few simple selections.  Quickly insert a visual description in a rich text snippet widget that summarizes the data shown in your visual. You can add multiple visual descriptions in individual widgets, or combine multiple visual descriptions in one or more widgets.  Edit the snippet to change the format, edit the contents of the generated description, edit description variables, insert images, links, and more. |
| Add URLs and Images to Table Visuals | Table visuals now support the inclusion of links to URLs or images in a table column. Select the option **Format {field name} as URL** to include a link to a URL or image by adding a URL with an interpolated value, such as `http://www.website.com/${value}`.   * If you link to a URL, the destination URL opens in a new browser tab when the user selects the field. * If you link to an image, the interpolated image is shown in the table cell. Define height and width of the image as needed. * Clear the image or URL by selecting the **None** option in the **Format as URL** work area. |
| Hierarchical Fields in Filter Snippets | Create filter snippets to filter by Hierarchy data type for the hierarchical data included in your dashboards. Select a hierarchical field to add to the filter snippet, then select an operator: equals or descendants of or includes to build the conditions for filtering the data.   * **Equals or descendants of**: Selecting the parent node selects all child nodes of the parent. Child nodes cannot be deselected. * **Include**: Selecting the parent node selects all child nodes of the parent. Child nodes can be deselected as needed.   As with all filter snippets, you can search your hierarchical content defined in the Value Column to help you select and deselect the content to include. |
| Content Tags for Visuals, Sorting, Filtering | We have expanded the use of content tags in Composer. You can now add tags to visuals, and use them to sort and organize content as you do with tags for dashboards and sources. Add a tag when you save or edit a visual in the Visual Gallery, or convert and add from a local visual from a dashboard to the Visual Gallery.   * When you import and export dashboards, sources, and shared visuals to the Visual Gallery using the UI or API, any associated tags are included. * Sort and filter dashboards, sources, and shared visuals in the Visual Gallery using your tags; filter in specifically tagged items, or items with no tags to help you organize your content. * Extend the use of content tags, filtering, and sorting to users working with embedded instances of Composer. |
| Multi-Grouping for Box Plot Visuals | Box plot visuals can now include groups and subgroups: add a subgroup to expand the depth of the information you provide in this visual type. |
| Sunburst Visuals | Use the new visual type, Sunburst, to display hierarchical data in a circle format. Display up to three levels of data, starting with the topmost hierarchical data in the center of the sunburst, with the secondary and tertiary levels shown in levels further from the center. |
| Export Multiple Sources and Copy Sources | You can now easily export multiple sources and copy individual sources in your environment as needed.   * **Export multiple sources**: Select the sources you want to export in the **Source** work area, then select **Export Selected Items**. All selected sources are downloaded to your browser, exported as one JSON file. * **Copy a source**: Open a source for editing, then select **Copy Source**. Enter a new **Name** for the copy of the source, and optionally a **Description** and **Tags**, then select **Copy**. The newly-named copy of your source is added to your data sources inventory, and you can continue editing your original source if needed.   Use the Sources API to send export requests for multiple sources, or copy requests for sources. |
| Other Bucket Grouping Options | A new feature, **Show Other**, allows you show or hide data in several visual types normally hidden when you define a limit for your data.  For example, enable **Show Other** for a pie chart of data sorted into twenty five counties, with a Limit of ten. Eleven slices are shown: the fifteen other counties are grouped as a single slice, comprising the remaining data succinctly. Disable **Show Other** in the sidebar menu, or by selecting **Remove** from the context menu of that data point.  This feature is available in the Sort & Limit sidebar menu of several visuals:   * Bar charts * Donut (single group) * Pie (single group) * Packed bubbles * Scatter plot * Tree map * Heatmap (single group) |
| Improved Analytical Capabilities | This release brings extensive updates to custom metrics. We have added time and time conversion functions, as well as a number of string manipulation functions to expand the range of possible calculations you can use in your environment. |
| Toggle Static Legends | You can now enable static legends for individual visuals as needed. If a static legend is available for a visual, enable or disable it in the Color sidebar menu. In embedded environments, this is configured at the dashboard level on a per-dashboard basis. |
| Refresh Data in Embedded Environments | Use the `EmbedManager` method `component.refreshData()` to refresh the data in an embedded dashboard. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 23.3.14 Feature Enhancements** | |
| None. |  |
| **Composer 23.3.13 Feature Enhancements** | |
| None. |  |
| **Composer 23.3.12 Feature Enhancements** | |
| None. |  |
| **Composer 23.3.11 Feature Enhancements** | |
| None. |  |
| **Composer 23.3.10 Feature Enhancements** | |
| None. |  |
| **Composer 23.3.9 Feature Enhancements** | |
| None. |  |
| **Composer 23.3.8 Feature Enhancements** | |
| None. |  |
| **Composer 23.3.7 Feature Enhancements** | |
| None. |  |
| **Composer 23.3.6 Feature Enhancements** | |
| None. |  |
| **Composer 23.3.5 Feature Enhancements** | |
| None. |  |
| **Composer 23.3.4 Feature Enhancements** | |
| None. |  |
| **Composer 23.3.3 Feature Enhancements** | |
| None. |  |
| **Composer 23.3.2 Feature Enhancements** | |
| None. |  |
| **Composer 23.3.1 Feature Enhancements** | |
| None. |  |
| **Composer 23.3 Feature Enhancements** | |
| Fiscal Calendars | Composer supports the use of fiscal calendars in your environment. Define one or more fiscal calendars in your Account to use in your data sources.  Once defined, users can select fiscal calendars to use on a per-source basis using the options available on the Global Settings tab of a data source.  Users can select a specific data field from a source on the Fields tab and create a new derived field using one of the available fiscal calendars.  If you are upgrading to this release, existing sources use the default Composer calendar. |
| Interpolation in Expressions | We have expanded the use of interpolation to allow you to include user attributes in derived fields and custom metrics such as in filters and Custom SQL expressions. Use interpolation in your expressions in the format `${attribute_name|default_value}`. You cannot use interpolation with secure attributes. |
| Display Source Data in Users' Custom Timezones | Display the source data in dashboards and visualizations in the timezone of each individual user instead of the default timezone stored at the source. Alternatively, convert a `dateTime` field to a custom timezone. Apply to selected data sources. |
| Support for OAuth 2.0 connections to BigQuery and Snowflake | Leverage existing authorization rules of BigQuery and Snowflake data sources by enabling OAuth for these connectors in Composer. Your users can authorize using personalized credentials. Access to the data follows the security rules of the data source. |
| Dashboard and Source Tags | Categorize your Composer inventory and create themed groups of content using dashboard and source tags. Create an overarching themed content structure for your users, or use tagging to improve your object migration flow. Users can tag content to create groupings for everyone in the organization for ease of use. |
| Expanded Map Visual Functionality | We have made a number of improvements to map visuals:   * You can now define settings for all map visuals for **Start Zoom** and **Max Zoom**. * Coordinates on the Map: Markers visual are now shown by default as a tooltip when a user hovers over a marker point. Disable **Show Coordinates In Tooltip** in the Settings sidebar menu to hide the coordinates on hover. * Disable the **Limit** property on Map: Markers to allow processing of all available data instead of limiting the rows processed to a user-defined number. * The **County** and **Zip** fields for US Maps are no longer a required field. You can hide these values by selecting **None** for these fields in the Settings sidebar menu. * We’ve expanded the Country name formats accepted by Map: World Countries visuals to support the ISO-3166 standard. * The initial map center definition can now include **Start Latitude** and **Start Longitude** coordinates. When used in combination with the **Start Zoom** setting, it’s easier than ever to define a specific initial view for map visuals. |
| Cloudmade for Map Visuals | Cloudmade’s tile support is no longer available, and has been removed from map visuals.  Existing visuals that use the Cloudmade Tile Provider are migrated to Open Street Maps when you upgrade to this release or later. |
| Hierarchical Pivot Improvements | You now have greater control over your hierarchical groups; when you select a hierarchical field as a row group, you can now define the number of levels to expand in your pivot table in the sidebar menu. When you select the column header menu for your field, new options are available:   * Collapse all rows - visible if your rows are expanded; select to collapse * Expand all rows - visible if your rows are collapsed; select to expand * Levels to expand - visible if Expand all rows is unchecked; provide a numeric value to define a default number of levels to be expanded.   For greater visibility, the root level of each hierarchical field is now presented in bold type. |
| Improved Object Deletion | Composer now displays the names of dependent objects when you try to delete a visual, dashboard, dashboard link, connection, data source, or data source field. |
| Security for Connection Types | Supervisor users can add access restrictions to connection types on a per Account basis in the UI or by appropriate APIs.   * When a connection type has no restrictions, users with appropriate permissions in all Accounts can add new connections of that type, and edit existing connections of that type. * When you add Accounts to the list of Allowed accounts for a specific connection type:    + Users in allowed Accounts can add and edit connections of that type   + Users in other Accounts cannot add or edit existing connections of that type |
| Filter Snippet Expanded Options | We have made a number of improvements to filter snippets.   * New options for Operators include **Contains** and **Does Not Contain** for more flexible filtering. * Simplify cross-source filtering when your data contains mismatched field names. Select a source for the filter snippet, then select a field to use as a **Value Column**. Next, select a different field, as needed, as a **Display Column**.    + If you prefer to use your value as the display, enable the **Use Value Column as Display Column** toggle.   + The new options, Value Column and Display Column, replace the Field column used in previous releases. * Simplify cross-source filtering when your data contains mismatched field names. Select a source for the filter snippet, then select a field to use as a **Value Column**. Next, select a different field, as needed, as a **Display Column**.    + If you prefer to use your value as the display, enable the **Use Value Column as Display Column** toggle.   + The new options, **Value Column** and **Display Column**, replace the Field column used in previous releases. * You can now sort the data in your filter, based on your **Display Column** selection. After selecting a Source and Display Column field, you can select sort options based on the field type: **A-Z** and **Z-A** orders, **Chronological**, or **Ascending** and **Descending**.    + Any values you add manually are not affected by this sort order.   + If you select an order, Static Overrides for a field won’t be applied. * Set a display option for Time fields: **Fixed List**, **Dropdown List**, and **Range**. If you select Range, you can give users the option to use static and dynamic time, or disable mode switching to require them to use static or dynamic time. * Connect multiple widgets from the same source quickly and easily. Select a **Widget Name** and **Field**, then select the **Copy** icon to add a new entry based on the same widget and field, then select a new field as needed. Repeat until all desired fields are included. * **Min** and **Max** ranges for date fields have been removed to make the filter snippet more compact. |
| Improved Data Types Conversion in the Python Connector | In this release of Composer, data types resolution in Python connector has changed. All values returned from public functions are implicitly converted to the [Pandas Dataframe](https://pandas.pydata.org/docs/reference/frame.html "Pandas dataframe link"). |
| Restrict Dashboard Report Scheduling to External Users | Control your users' ability to schedule dashboards reports to users without Composer accounts and prevent your users from report scheduling to external emails. Work with your Technical Support to disable this capability via server-level variable. |
| Restrict Dashboard Report Scheduling to External Users | The previous limit of a maximum of 4,000 symbols in an LDAP query has been removed, and now you can add LDAP queries with the unlimited amount of symbols as needed. |
| Arc Gauge Improvements | You can now display your percentage numbers in an arc gauge visual rounded to a whole number. |
| Extended Sources API Validation Response Payload and Introduced `suppressWarnings` | We have updated the validation error response payload for Sources API endpoints (code 400, “Bad Request”) and introduced `ERROR` and `WARNING` levels of validation issues. The APIs have been expanded with an optional query parameter, `suppressWarnings`, to force source creation or update omitting the warnings. |
| Delete File Uploads | Users with the new group privilege **Manage File Uploads** can delete unneeded files uploaded for a data source if they are not used by any sources. |
| Mobile-Friendly User Interface Updates | Mobile users can now touch and long touch a visual to access its Context menu and the visual's tooltip.  Touch and long-touch events behaviors are configurable for embedded dashboards.  All Visual settings are now available on mobile devices. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 23.2.15 Feature Enhancements** | |
| None. |  |
| **Composer 23.2.14 Feature Enhancements** | |
| None. |  |
| **Composer 23.2.13 Enhancements** | |
| None. |  |
| **Composer 23.2.12 Feature Enhancements** | |
| None. |  |
| **Composer 23.2.11 Feature Enhancements** | |
| None. |  |
| **Composer 23.2.10 Feature Enhancements** | |
| None. |  |
| **Composer 23.2.9 Feature Enhancements** | |
| None. |  |
| **Composer 23.2.8 Feature Enhancements** | |
| None. |  |
| **Composer 23.2.7 Feature Enhancements** | |
| Embedded Dashboard Events | Use the event listeners `composer-dashboard-pristine` and `composer-dashboard-dirty` to track the state of your embedded dashboards. |
| **Composer 23.2.6 Feature Enhancements** | |
| None. |  |
| **Composer 23.2.5 Feature Enhancements** | |
| None. |  |
| **Composer 23.2.4 Feature Enhancements** | |
| None. |  |
| **Composer 23.2.3 Feature Enhancements** | |
| None. |  |
| **Composer 23.2.2 Feature Enhancements** | |
| None. |  |
| **Composer 23.2.1 Feature Enhancements** | |
| None. |  |
| **Composer 23.2 Feature Enhancements** | |
| Python Connector Support | You can now connect your data in Composer using a Python script. Access information exposed by APIs, or other data generated by calculation or prediction models. |
| Accessibility Support (WCAG) | This release of Composer extends support for WCAG accessibility features. This expansion includes standardized semantic markup for text elements, acceptance of keyboard input for available elements, as well as improved accessibility of panels, menus, and pickers.  Page traversal updates include use of a defined focus order, optimized inventory navigation, along with auto focus and adjust focus selection on dashboards and panels.  The Calculation Editor now supports focus capture and escape in the formula text editor. |
| Services Memory Updates | With this release, service memory configuration recommendations have been reviewed and unified across all native operating system and container-based deployment options.   * These changes will help you avoid out of memory issues, unpredictable service stability, and memory overallocation. This includes a general recommendation to use the new default for Java: Xms=Xmx. * Our review and update of default memory allocation, based on internal performance testing, means that services are better configured for a general production load after you have completed installation. |
| Widget Level Comments | Users can now create and read comments for individual widgets included in their dashboards in both standalone and embedded environments.  Users with an Editor role can assign a new role for a user’s dashboard access, Commenter.   * Commenter users can create, edit, format, and delete their own comments, as well as view all available comments associated with a widget. * Viewer users can view all available comments associated with a widget. * Editor users can create and edit their own comments, as well as delete other user’s comments and view all available comments associated with a widget.   A new interactivity profile setting, Comments, supports this feature in embedded environments. |
| Improved Analytical Capabilities | We have improved analytical capabilities to support aggregate functions in custom metrics.   * Added Median, Variance, and Standard Deviations. * Included CASE to express conditions in your calculations. * Expanded support for multiple arithmetic functions, such as POWER, MOD, SQRT, and more. * Support for FIRST and LAST values. |
| Data Source Import and Export | Users can now export and import data source configurations including connection information in your environment if they have appropriate access rights and privileges.   * To export a data source, you must have read access for the connection and data source configuration. * To import a data source, you must have the **Create New Data Sources** privilege. |
| Java 17 Support | Composer v23.2 now runs on Java 17. When you perform a straightforward upgrade to this release, Java is updated automatically. To update manually, see Manually Install OpenJDK.  Composer v23.1 and earlier continue to run on Java 11. |
| Embedded Source Inventory List | Source management in is now supported in embedded environments. You can embed a list of sources, define which columns to view in what order, and define what controls are available by enabling and disabling interactivity settings. Users can filter and add sources to favorites. |
| Raw Data Field Capability | You can now control the visibility of the raw data for your fields. Select Update Field Capabilities to enable or disable access to raw data for one or more fields and remove them from raw data export files. Raw data access is enabled by default for all fields in your source. |
| Export Dashboards to XSLX | You can now export dashboards in Excel (.xlsx) format, including the information for each widget in its own named tab, with data provided as visual data or raw data for the visuals. |
| Send Scheduled Dashboard Reports in XLSX | Scheduled dashboard reports can now be sent in Excel (.xlsx) format, providing regular updates in the timeframe and frequency you define. Create or update a scheduled dashboard report to use Excel format as needed.  A new interactivity profile setting, Data Export, supports this feature in embedded environments. |
| Filter Snippet Improvements | We’ve expanded the functionality of filter snippets in several ways:   * Connect multiple filter snippets together to more flexibly filter your visual data. * The selected values for each filter snippet are saved when you save your dashboard. * Create filter snippets that are based on the Time field; connect to visual or snippets to filter data. |
| Conditional Formatting for KPI Visuals | You can now define conditional formatting for your KPI visuals to control labels, background, and arrows appearance. Color Settings have been expanded into Color Rules you can modify to suit your data presentation for new and existing visuals.  A default color palette and rules are applied to KPI visuals; select and edit any rule in the color sidebar menu to modify. Optimize the contrast of text against the background, and apply expanded and conditional formatting options such as bold and italics.  Color settings for your existing KPIs will be automatically migrated to new Conditional formatting. |
| Dashboard Layout Improvements | We’ve extended the flexibility of dashboard layouts in this release with a number of improvements:   * Converted dashboard widgets are now presented in the responsive layout format in the same row and columnar layouts as in their previous configuration. * You can now convert dashboards to responsive layout by API. * Expanded theme options allow you to set up gaps between widgets and the border radius. * By setting minimum widget height and width settings, you can define the appropriate values for widgets' sizes on your dashboard. You can also adjust the position and padding of content in widgets. * Drag and drop zones for moving widgets are easier to manipulate. * You can configure your dashboard to hide widgets for unavailable visuals from Viewer users: available widgets adjust to fit the dashboard, replacing unavailable visuals. |
| Mobile Friendly Dashboard Layout | Dashboards are now more responsive and flexible for viewing on mobile and tablet devices: widgets and layouts resize and adjust to the available screen size and orientation for your users. Task-based work areas, such as dashboard report scheduling and menus are also sized appropriately for use.  Use touch actions to get more information about a widget: a short touch brings up the context menu, while a long touch surfaces tooltips and dashboard layout options. |
| Interactivity Profiles Expansion | **Dashboards:** Dashboard interactivity profile settings have been updated and expanded so you can further fine tune the access your users have to specific settings.   * Export options have been expanded: control users' ability to export data in addition to exporting dashboards as a PDF or PNG, and exporting configurations. * You can more finely control users' ability to add snippets: enable or disable their ability to add text snippets, filter snippets, or both. * A new interactivity setting, Info, can be disabled to prevent users from seeing the info sidebar menu panel or modal for visuals. * Enable and disable users' ability to update the description of a dashboard. * Enable and disable users' ability to provide and read comments associated with widgets in your dashboard. |
| **Visuals:** Visual interactivity profile settings have been updated and expanded to fine tune the user experience.   * Control a user’s ability to see the info sidebar menu panel. * The Export interactivity option for visuals is now split into three settings, control users' ability to export to CSV, XLSX, and PDF/PNG. |
| Commenter Access for Dashboards | A new access role, Commenter, has been added to dashboards. Commenter users can create, edit, format, and delete their own comments on a widget, and view available comments associated with a widget.  Users with Editor or higher access can share a dashboard and assign this role to users within their organization. |
| Search by Description | Descriptions provided for dashboards, data sources, and visual gallery visuals are now searchable in their respective work areas.  Any dashboard, data source, or visual gallery visual with a description is indicated by an info icon in the table of available items.  Control access to this functionality using interactivity overrides. |
| Expanded Ubuntu Support | Composer now supports installation in Ubuntu 22 environments. |
| Extended Microsoft SQL Connections | Composer now supports connecting to Microsoft SQL v16.0 (SQL Server 2022). |
| Pivot Table Improvements | You can now select the option **Autosize All Columns** from the menu of a pivot table header to expand the width of the column data to display fully in your pivot table.  A new option, **Span Duplicate Rows**, groups repeating data values in the same row. On by default for new pivot tables, enable for existing pivot tables by selecting **Span Duplicate Rows** when editing row groups.  The display settings for pivot tables now include fine granularity controls you can use to show some of your data (when enabled) or all of your table data (when disabled).  Expand and collapse hierarchical fields by selecting Expand All Rows or Collapse All Rows from the menu of a hierarchical pivot table column.  Show or hide rollup options for your hierarchical columns by enabling or disabling **Show Rollup Labels** in the settings sidebar. |
| Table Visual Improvements | * It’s now easier to add custom metrics and derived fields to your table visuals. Select the add icon while editing columns included in the visual to add a derived field or custom metric as needed. * Review unique data in your table visuals by enabling **Show Distinct Rows** in the settings menu of your visual. |
| Data Upload Enhancements | You can now optionally prevent auto-detection of time fields for files uploaded in CSV or JSON format. Select **Disable Integer to Time Auto Detection** at file upload. |
| Embed Manager NPM Package | In environments where you use Typescript for your client side code, you can use Embed Manager as an npm package. See <https://www.npmjs.com/package/logi-embed>. |
| Configure Data Schemas for Connectors | You can now control which data source schemas are treated as internal by Composer and are not disclosed to users for the source creation. Add the `system.schemas` property to the properties file of a connector to specify the internal schemas and hide the data. |
| Extended Integer to Datetime Conversion in Timezone Offsets | You can now convert integer fields to datetime fields with milliseconds granularity when using timezone offsets for PostgreSQL and Impala. Use the new properties `datasource.timestamp-millis-fields-names` and `datasource.timestamp-millis-fields-pattern` to specify the offset field. |
| Convert Dashboards to Responsive Layout - API | You can now convert your dashboards to the responsive layout using the endpoint `api/dashboards/convert-layout/`.  **Important:**  This endpoint is experimental. |
| Embedded Visual Events | You can now use an event listener to track and log events related to cursor movements for visuals. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 23.1.14 Feature Enhancements** | |
| None. |  |
| **Composer 23.1.13 Feature Enhancements** | |
| None. |  |
| **Composer 23.1.12 Feature Enhancements** | |
| None. |  |
| **Composer 23.1.11 Feature Enhancements** | |
| Embedded Dashboard Events | Use the event listeners `composer-dashboard-pristine` and `composer-dashboard-dirty` to track the state of your embedded dashboards. |
| **Composer 23.1.10 Feature Enhancements** | |
| None. |  |
| **Composer 23.1.9 Feature Enhancements** | |
| None. |  |
| **Composer 23.1.8 Feature Enhancements** | |
| None. |  |
| **Composer 23.1.7 Feature Enhancements** | |
| None. |  |
| **Composer 23.1.6 Feature Enhancements** | |
| None. |  |
| **Composer 23.1.5 Feature Enhancements** | |
| None. |  |
| **Composer 23.1.4 Feature Enhancements** | |
| None. |  |
| **Composer 23.1.3 Feature Enhancements** | |
| None. |  |
| **Composer 23.1.2 Feature Enhancements** | |
| None. |  |
| **Composer 23.1.1 Feature Enhancements** | |
| Shared Dashboards and Visuals Updates | When you add or create one or more visuals added to the Visual Gallery in a dashboard previously shared with other users, the visual is available to those users once you have saved your changes to the dashboard. |
| Visual Builder Update | Composer now supports defining placement of the visual settings menu in an embedded environment.  editor: { placement: 'modals | dockRight' } |
| **Composer 23.1 Feature Enhancements** | |
| Simplified Product Evaluation | Simplify your evaluation of Composer 23.1 by downloading docker images insightsoftware has made available on <https://hub.docker.com/>. Try the docker Composer based solution <https://github.com/LogiComposer/Try>, or publicly available Helm charts for Kubernetes deployments. |
| Scalable Kubernetes Support | Composer now officially supports Kubernetes. Deploy your application to Kubernetes clusters to ensure high availability and fault tolerance. This solution includes horizontal autoscaling for your application microservices as needed, based on their load. |
| Structured Logging Support | Composer now supports structured logging you can enable as part of the bootstrap installation. |
| Dashboard View Mode | Composer dashboards now include a new View mode for both standalone and embedded environments. View mode is applied automatically to a dashboard for all users with Viewer access. The dashboard has a restricted feature set, defined by applied interactivity profiles.  Dashboards are opened, by default, in Edit mode for all Owners and Editors. These users can edit the dash board, define interactivity settings, and toggle between Edit and View modes to generally see what users with Viewer access see.  For both standalone and embedded environments:   * You can define preferred interactivity settings * Interactivity profile settings are applied   For embedded environments, define the preferred embed configuration:   * Define the default mode for Editors * Enable or disable access to interactivity settings for Editors |
| Self Service Sharing Updates | Collaborate with other Composer users by granting Editor permissions for your dashboards. Editors can edit the dashboard, share the dashboard and its visuals with other users, and change the permissions for existing users with access to the dashboard. |
| Local Visuals | Composer now supports two kinds of visuals: Local visuals and Visual Gallery visuals. Local visuals are exclusive to individual dashboards and not stored by default in the Visual Gallery. Select **Add New Visual** to create and edit local visuals to adjust, tweak, and experiment with scenarios you need. After you create a local visual, you can add it to the Visual Gallery for reuse in this and other dashboards. Local visuals use the dashboard’s permission set and don’t require any individual permissions or privileges for creation.  Select **Add Existing Visual** to add a Visual Gallery visual to a dashboard. Convert it to a local visual to adjust, tweak, and experiment with this local copy and not affect the Visual Gallery visual in other dashboards. |
| New and Responsive Dashboard Layouts | Composer dashboards have been redesigned to provide easy to use layout controls and support different resolutions. You can now reshape, resize, lock, swap, and align widgets quickly and easily to be visually appealing on a variety of user devices, from large screens through to mobile devices. Use column and row locking when you would like to fix a widget’s place and size.  All new dashboards are created with new and responsive layouts. You can easily convert non-responsive dashboards to responsive as needed. |
| Dashboard Export/Import Enhancements | You can now import dashboards more flexibly as you upgrade between Composer environments.   * Dashboards exported from Composer 7.10 and later can be imported to Composer versions 7.10.x, 8.1 – 8.4, 22.4.x, and 23.1.x. * Dashboards exported from Composer 7.9 and earlier can only be imported to the same major Composer version.   We’ve updated the dashboard export and import APIs to include source cache settings for the data and statistics caches in the payload. |
| Data Export in XLSX Format | You can now export your visual data and raw data for your visuals in XLSX format. Update file name and choose filters that you would like to be added as a string to the exported file. Define the number of records to export, and sort based on available attributes for Raw Data Export. |
| Localization Support for Source Metadata | Provide localization support for data source field labels and metrics labels by uploading metadata dictionaries. Upload a translation file in CSV format for each data source you create to support a broader range of users in their preferred language. |
| Schedule Dashboard Reports for Non-Composer Users | You can now schedule and send dashboard reports to users who do not have Composer accounts. The contents and permissions for these reports are determined by the settings on your account for the report, including interpolation, security for row and column data, as well as filtering. |
| Group Labels Position | Composer now offers you control over label positions for several visuals: Bars, Bars: Multiple Metric, and Combo Chart.  Select from horizontal (default), vertical, or diagonal to suit your visual layout needs. Control how to display labels in Bars visual: inside or outside the bars. |
| Expanded Combo Chart Label Settings | Combo chart label options have been expanded to allow you adjust the position of group labels, and show or hide more information about your data points.  Select to show or hide metric labels, absolute values, and relative values for the Y-axis bars in your visual. |
| Show and Hide Axis Pickers for Visuals | Declutter your visuals by controlling the availability of axis pickers for visuals in a dashboard. Axis pickers are shown by default; use the Widget settings sidebar to hide the pickers, or make only specific pickers available. |
| Dynamic Legends | This version of Composer introduces dynamic legends for many visuals. Depending on the color style used in a visual (distinct or gradient) you can temporarily adjust what data is shown in the visual by selecting a data point to turn on or off, or adjust the gradient slider. |
| Visual Date and Number Formatting | Define preferred formatting settings for date and number fields at the visual level, overriding the formatting defined at the source level.   * Reset visual formatting to return to the default source level formatting. * The formatting is now supported in grouped data. |
| Context Menu Updates | Composer 's context menu has several updates available in this release:   * The context menu is now available for all Composer visuals. * The Settings option has been added to the context menu. Select **Settings** to open the visual sidebar menu. * The **Remove** option in the context menu is now supported on Time fields. * You can now define right and left click actions for the context menu on Pivot table visuals. * VisualAPI is now available for visual-clicked, visual-right-clicked, series-clicked, and series-right-clicked events. You can also use VisualAPI API in custom options in the context menu. |
| Jira and Salesforce Connectors | Composer now supports a connection to Jira and Salesforce using Simba drivers. To obtain connector servers, see Obtain Additional Connector Servers.  For more setup information, see Manage the Jira Connector and Manage the Salesforce Connector. |
| Dashboard Filter Snippet | Filter visuals on your dashboard quicker and easier with a new Filter Snippet. Add your own custom values or select a field to have a predefined list of values. Connect visuals from one or different data sources to filter them. |
| InitialFilters for Dashboards | The functionality of the `initialFilters` object has been expanded. Use the `applyFiltersStrategy` property and the value `overrideSamePath` to override existing filters along the same path, or the value `replaceExisting` to remove all filters and use only defined `initialFilters`. Pass an object to the `path` if needed. |
| Expanded Visuals Interactivity Settings | You can now control **Save** and **Save as** options for availability for visuals using visual interactivity settings. |
| Expanded Dashboard Interactivity Settings | You can now enable and disable the **Save** as option for dashboards using dashboard interactivity settings. |
| Interactivity Updates | Control the Format interactivity option to enable or disable date and number formatting at the visual level. |
| Embedded Events Updates | Composer now provides a `componentInstanceId` as a part of event details for dashboard, source and visual events. |
| Distributed Tracing | All Composer microservices now support distributed tracing using the OpenTelemetry (OTel) specification.  This replaces the Composer Tracing Microservice (`zoomdata-tracing-server`), deprecated in a previous release, and is now removed. |
| License Key Provisioning | With this release of Composer, you can now supply license keys via configuration properties. |
| Hierarchy Support Update | Hierarchical field support is now enabled by default in Composer. Work with technical support to enable or disable as needed. |

[Return to top](#top "return to top")

### Composer v22

| Title | Description |
| --- | --- |
| **Composer 22.4.14 Feature Enhancements** | |
| None. |  |
| **Composer 22.4.13 Feature Enhancements** | |
| None. |  |
| **Composer 22.4.12 Feature Enhancements** | |
| None. |  |
| **Composer 22.4.11 Feature Enhancements** | |
| None. |  |
| **Composer 22.4.10 Feature Enhancements** | |
| None. |  |
| **Composer 22.4.9 Feature Enhancements** | |
| None. |  |
| **Composer 22.4.8 Feature Enhancements** | |
| None. |  |
| **Composer 22.4.7 Feature Enhancements** | |
| None. |  |
| **Composer 22.4.6 Feature Enhancements** | |
| None. |  |
| **Composer 22.4.5 Feature Enhancements** | |
| Hierarchy Support Update | Hierarchical field support is now enabled by default in Composer. Work with technical support to enable or disable as needed. |
| Context Menu Updates | VisualAPI is now available for visual-clicked, visual-right-clicked, series-clicked, and series-right-clicked events. You can also use VisualAPI API in custom options in the context menu. |
| InitialFilters for Dashboards | The functionality of the `initialFilters` object has been expanded. Use the `applyFiltersStrategy` property and the value `overrideSamePath` to override existing filters along the same path, or the value `replaceExisting` to remove all filters and use only defined `initialFilters`. |
| **Composer 22.4.4 Feature Enhancements** | |
| None. |  |
| **Composer 22.4.3 Feature Enhancements** | |
| None. |  |
| **Composer 22.4.2 Feature Enhancements** | |
| None. |  |
| **Composer 22.4.1 Feature Enhancements** | |
| None. |  |
| **Composer 22.4 Feature Enhancements** | |
| Hierarchies Support for Pivot Tables | Composer now supports common hierarchical structures you can use to visualize and organize your data. Hierarchies create parent-child tree-based, and field-level hierarchical structures using your source data. Transform your data further by applying hierarchical row filters to your data.  When you organize your data in Composer in hierarchies, it is easier to access for analytical processing, for data traversal, and keyword searching. To view your data in a hierarchical format, create a data source that defines a adjacency list hierarchy, add one or more hierarchy fields to your data source, then optionally define hierarchical groups or filters to apply to pivot table visuals, or hierarchical filters to your other visuals. |
| Self Service Sharing of Dashboards | You can now allow your users to share dashboards more easily among themselves in a user-friendly manner that does not require a complex process of defining granular permissions. Your users can now grant and revoke `VIEWER` access level to a dashboard, along with its underlying visuals and sources.  Control the visibility of this feature in Composer Embed mode by enabling or disabling **Share Dashboard** in Dashboard Interactivity Settings. |
| Widget Settings | Use Composer's Widget Settings sidebar menu to manage the appearance of your visuals and rich text snippets on a dashboard. Access by selecting **Settings** gear icon from the **More** menu, then changing the **Display Name**, **Description** text, or **Header** options.  The **More** menu option **Edit Visual** is renamed **Settings** for visuals and rich text snippets. |
| Rich Text Snippet Support | You can now add Rich Text Snippet snippets to your Composer dashboards. Annotate your dashboard, describe data on your dashboard in context, and link external resources, such as user guides, or images. Add during dashboard creation, or at any time using the Composer UI, or using the dashboard API. |
| Alerts Updates | Alerts are no longer an experimental feature of Composer. Create alert definitions, determine a schedule to evaluate the alert condition, and define how notifications are handled when an alert condition is met. You can use the API or Composer UI to define and update these conditions, so you can alert your users when a metric reaches a specific threshold. |
| Context Menu | The Context Menu provides your users a way to view more information about specific data points in visuals. This menu replaces the functionality of the radial menu, providing streamlined options for working with data.  Define how to embed the context menu in your Composer instance by specifying default options for right and left mouse selection. If needed, you can also add custom controls to the context menu for embedded visuals. |
| Bulk Update Field Capabilities | You can now update field capabilities for fields at the source level in bulk. Select **Update Field Capabilities** in the Fields tab to open the Bulk Update Field Capabilities work area. Search and sort fields as needed, then optionally enable or disable settings for one or more fields. Enable or disable **Details**, **Filtering**, **Grouping**, **Metrics**, and **Playing**. |
| Conditional Formatting Options for Pivot Tables | You can now format Pivot Table visuals by adding color and text formats based on conditional rules. |
| Stored Procedure Support For Microsoft SQL | You can now create Microsoft SQL sources that include the use of stored procedures. Use `exec` or `execute` in your custom SQL during source creation, with or without parameters. Supported stored procedures return raw data only. |
| Fields Statistics Update | You can now use an additional subordinate field of `statistics`, `lookup`, in the Fields API to set dynamic filter values overrides for a specific field. |
| Elasticsearch Updates | Composer includes expanded support for several Elasticsearch features.   * Elasticsearch 7 and 8 connectors recognize the numeric field types `scaled_float`, `half_float`, and `unsigned_long` for use in visuals. * Multi valued fields detection: When enabled, Composer uses automated field type detection to mark nested fields as `multi_valued` fields. Add the property `elasticsearch.describe.mark-all-nested-fields-as-multi-valued` to your Elasticsearch configuration files to treat all nested fields as `multi_valued` fields, then create a new source to connect to your data. Recreate existing sources to use multi valued fields. * Elasticsearch connectors work with GeoPoint field types, supporting the use of location fields as `location.latitude` and `location.longitude` in map visuals. |
| KPI Chart Label Positions | You can now adjust the position of labels in KPI Chart visuals. Use the options in the Position section of the Settings sidebar menu to rename your labels and adjust the position of the labels as needed. |
| Filter Values Entity Support | Composer now supports filter values entities you can use to provide an alternative source of metadata values. Use these entities in a dynamic override on Filter Values Tab in Fields to improve the filter experience of heavy data entities.  Control the interactivity by adding Filter Values Entity and Filter Values tab for your users as needed. |
| Composer Web Graceful Shutdown Support | Composer Web now includes a graceful shutdown option to close the active web sockets. The default shutdown period is 25 seconds, encompassing a 5 second propagation and 20 seconds to shutdown active tasks. |
| Tracing Improvements | Composer now supports tracing for Zoomdata-Web and Query Engine combined in the same trace ID. All requests to connectors are traced using a common trace ID.   * Zoomdata-Web supports tracing of: the REST API, Spring service, DAO service calls, and WebSocket messages. * Query Engine supports tracing of: REST API calls and WebSocket Messages. |
| Date and Time Format | You can now format your time fields at the source to show or hide the day of the week. By default, Composer hides the day of the week field. |

[Return to top](#top "return to top")

### Composer v8.4 and Earlier

| Title | Description |
| --- | --- |
| **Composer 8.4.1 Feature Enhancements** | |
| None. |  |
| **Composer 8.4 Feature Enhancements** | |
| Embedded Source Editor | You can now embed a source editor for your users. Use configuration to define your desired tabs and make specific components available and customize their source editor work flow.  Subscribe to events to track operations related to user activity for sources, fields, and custom metrics. |
| Custom Values and Custom Ranges Support | You can now apply a static override to a field to define custom values and ranges for data at the new Filter Values Tab in Fields. This applies to Attribute, Number, and Time data types.  The Fields Tab option **Only allow custom values** has been removed from the user interface. You can replicate this functionality for Attributes and Numbers by applying Static Override to a field and enabling Custom Values. You can now define custom values at the source level. |
| Fields API Updates | Composer supports an expanded statistics override option for `NUMBER` data fields. In addition to the existing `min` and `max` values, you can now define `distinctValues` as well.  API documentation is provided with your Composer installation at this link: `https://<composer-URL>/composer/swagger-ui.html`. |
| Format Dates on Visuals | Composer now supports date formatting for individual Table visuals. You can change the date formatting for a visual without affecting the underlying source date formatting, or revert to the date formatting defined at the source level as needed. |
| Logging Updates | Composer now provides unified logback configurations for all microservices, and unified log properties to provide centralized microservices configuration.  The logback.zoomdata property, previously used to control the log level of some loggers, has been removed. Use a standard spring boot approach to specify appropriate properties.  Several logging properties were renamed. See Log File Migration Reference. |
| Connect to Amazon OpenSearch | Composer now supports connections to the Amazon OpenSearch data store versions 1.x and higher. Connect using the Elasticsearch 7 data connector. |
| Field and Custom Metric Labels Updates | Composer now supports use of non-unique labels for fields and custom metrics. Underlying names for these fields remain unique, created by Composer or set using the API at field creation. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 8.3 Feature Enhancements** | |
| Schedule Reports From the Dashboard | On upgrade, Composer may make the **Schedule Report** button available in existing embedded dashboards by default.  Control visibility by enabling or disabling **Schedule Report** in the Dashboard Interactivity Settings menu for users with appropriate privileges. |
| Expanded Time and Date Options | Composer now enables you to define time formats at the source level to include specific **Week** options, such as **range**, **narrow**, **numeric**, **weekStart**, and **weekEnd**, and specific **Quarter** options, such as **range**, **narrow**, and **numeric**. These new options are usable in visuals, time bars, and filters throughout your environment. |
| Conditional Formatting Options for Tables | You can now format Table visuals by adding color and text formats based on conditional information. |
| Configuration Updates | The configuration property, `-Dlog.console.level=OFF`, has been moved from **application.jvm** to **application.properties** for the following microservices: Composer Web, Query Engine, Connectors, Screenshot Service, Data Writer, Admin Server, and Config Server. Change this property as needed using the environment variables for each microservice.  The configuration property `-Dlog.console.level=OFF` is no longer in the **application.jvm** files. |
| Raw Data Table Sorting | You can now multi sort columns in a raw data table without using the Shift key. Select each column in turn to enable multi sorting by those columns. |
| Initial Filters for Dashboards | You can pass initial filters to dashboards using the `initialFilters` object. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 8.2 Feature Enhancements** | |
| Composer Logging To Console | Composer v8.2 now supports log destination configuration and allows microservices logs to be written to files, `stdout`, or both. |
| Log File Name Updates | The log file names for the Config server and the Consul have changed:   * Config server log file: `config-server.log` * Consul log file: `zoomdata-consul-{unixTimestamp}.log` |
| Waterfall Visual | A new visual type, waterfall, is now available for use in your environment. |
| Format Numbers on Visuals | Composer now supports number formatting for individual Table visuals. You can change the number formatting for a visual without affecting the underlying source number formatting, or revert to the number formatting defined at the source level as needed. |
| Pivot Table Sorting Updates | Composer now supports pivot table data sorting by one or more column or row groups. |
| Null Values in Time Groups | You can now control the inclusion of NULL values in the time groups in your visuals. By default, NULL values are included. Add a filter to either exclude NULL values from a visual or to display only NULL values in a visual. |
| Visual Gallery Updates | The Visual Gallery now supports advanced search and favorites. You can also filter what visuals you see by favorite status, ownership, and shared status. The visuals list now includes a Favorites column and Data Source column.  The Usage column has been removed. |
| Visual and Display Name Updates | The field **Default Title** has been removed from the Info sidebar menu of stand alone visuals.  The field **Visual Title** has been renamed to **Display Name** for visuals included in a dashboard, and will display as the visual’s name when included in a dashboard. |
| Visual Rendering Updates | When you make changes to an underlying custom metric or derived field, associated visuals are re-rendered to reflect the changed source data. |
| Locale-Dependent Date and Time Formatting | Composer now presents date and time formats appropriate to a user’s locale for both source and visual data, complementing the options available in Configure Date and Time Formatting. |
| Modified Date Updates | Composer now updates the Modified Date field for sources when objects within a source are updated, including fields, custom metrics, cache settings, and global settings. |
| Import and Export Dashboard Updates | When you export a dashboard, empty arrays for `connections`, `sources`, `visuals`, and `visualTypes` are no longer contained in the payload. |
| Visual Interactivity Menu Parameters | A new parameter, `CREATE_VISUALS`, has been added to allow you to control how users interact with options to add new and existing visuals to a dashboard in embedded environments. Use `CREATE_VISUALS` to allow users with appropriate privileges to add new visuals, and `ADD_VISUALS` to allow users to add only existing visuals. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 8.1 Feature Enhancements** |  |
| Report Scheduler Updates | The dashboard report scheduler has been updated and streamlined to make reports easier to schedule for yourself and other users. The **Send to me** toggle is removed, replaced by a field to add report recipients, prepopulated with the current user’s information. |
| Group Privilege Update | You can now assign a new Group Privilege, **Administer Scheduled Reports** to your users. Users with both Read access to a dashboard and the Administer Scheduled Reports privilege can edit and delete all scheduled reports for those dashboards, even if created by another user. |
| Visual Gallery Embed Actions | You can now specify and use predefined actions in embedded visuals, including navigating to a link when you pass an item ID to the link, such as `https://visuals.company.com/edit/${inventoryItemId}`. |
| Visual Gallery Favorites | Composer now supports selecting and deselecting visuals as favorites when embedded in your application, and using the API. |
| Visual Gallery Embedding | You can now generate an embeddable HTML snippet for a visual using the UI. |
| Expanded Inventory Support | Composer now supports advanced search by field for embedded Visual Galleries, embedded Libraries, and the Library. Search All fields, or by specific fields such as Type, Name, Author, or Usage. |
| Expanded Date and Time Format Support | Composer includes expanded date and time formatting options that you can set at the source level. Select a time field on the Fields tab of your source creation, then select edit **Format** to control the specifics of the field to suit your needs. |
| Scheduled Reports API Updates | The behavior of the attribute `sendOnlyToOwner` is changed. When the attribute is set to `true`, the current user is now added to the list of `users`, and `sendOnlyToOwner` is reset by Composer to `false`. The attribute `sendOnlyToOwner` is deprecated, and will be removed in a future release. |
| Extend API to Support URL Format for Attribute, Number, Time | We have extended our API to support URL formatting for Attribute, Number, and Time. |
| Expanded Fields API Endpoints | Use the Composer API to remove a field or change a field type for a field in your source if it is not in use by a global filter. API documentation is provided with your installation at this link: `https://<composer-URL>/composer/swagger-ui.html`. |
| API Interpolation Support | Use the new endpoint `/api/user/interpolate` to send custom attribute names and get custom attribute values. API documentation is provided with your installation at this link: `https://<composer-URL>/composer/swagger-ui.html`. |
| Presto / Trino Support Update | Composer now supports Trino (rebranded from Presto) versions 351 - 390, and continues to support Presto version 319. For more information about the Trino connector, see Manage the Trino Connector. |
| Microsoft SQL Server Support Updates | The minimum Microsoft SQL Server version supported by Composer is now 12.0 (SQL Server 2014). |
| Elasticsearch Support Updates | Composer now supports Elasticsearch 8.1 - 8.3. When upgrading to version 8 of the Elasticsearch connector, previously defined connections that use the Transport client must be updated to use HTTP or HTTPS. Update your connection string as needed, for example, replace `transport://1.1.1.1:9300,2.2.2.2:9300` with `https://localhost:9200`. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 8.0 Feature Enhancements** | |
| Composer Custom Chart CLI | Composer’s Custom Chart Command Line Interface (CLI) v1.0 is now available to support Composer v7.10 and later. This tool allows developers to create, manage, and delete custom charts without being connected to the client application. See [Composer Chart CLI on NPM](https://www.npmjs.com/package/composer-chart-cli "Composer Chart CLI on NPM") and [Manage Custom Charts](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701046331405-Manage-Custom-Charts). |
| Dashboard Report Updates | Composer now supports interpolation for scheduled reports, so the recipients of the reports can now receive the data defined by their custom attributes in connection definitions, data source row security filters, visual and dashboard level filters, or custom SQL in data queries. |
| Cumulative Sum Option for Visuals | You can now enable a new setting, Cumulative Sum, for two visual types, Line Trend: Multiple Metric and Bars. When enabled, Composer updates the visual to add the previous value to the next value, and both the original and cumulative value for selected items are displayed as a tool tip.  In Bar visuals, this feature is only available when data is grouped by a Time field, and when the Enable Subgroup setting is disabled. |
| Expanded List Settings in Dashboards | Composer now allows you, when editing a list visual in a dashboard, to modify the Selection Behavior in the visual’s Settings sidebar menu. For single selections, you can customize the text of the **No Selection Label**; leave it as None, or add your own option.  For multiple selections, you can Filter Values when they Change, or allow the user to select their options and not display the results until they select the Submit button. You can customize the text of the **Submit Button Text**; leave it as Submit or add your own option. |
| Subtotals for Pivot Tables | You can now add metric subtotals to columns or rows of your pivot tables. Select Rows or Columns in **Show Metrics as** in the Settings sidebar menu, then enable **Show Metric Subtotals** to display the subtotals for your selection. |
| Inventory Visual API Support | Composer now supports a new endpoint, `api/inventory?type=VISUAL`, that returns information about visuals for which the user has READ permission. |
| Elasticsearch Support Update | Composer now supports Elasticsearch 8.1 - 8.3 in addition to 7.0 - 7.17. |

[Return to top](#top "return to top")

### Composer v7.10 and Earlier

| Title | Description |
| --- | --- |
| **Composer 7.10.23 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.22 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.21 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.20 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.19 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.18 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.17 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.16 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.15 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.14 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.13 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.12 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.11 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.10 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.9 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.8 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.7 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.6 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.5 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.4 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.3 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.2 Feature Enhancements** | |
| None. |  |
| **Composer 7.10.1 Feature Enhancements** | |
| None. |  |
| **Composer 7.10 Feature Enhancements** | |
| Windows Support | Composer v7.10 and higher can now be installed on Windows Server versions 2012 R2, 2016, and 2019 using a bootstrap script. |
| Source Creation Updates | Composer v7.10 includes a redesigned source creation process to allow for more flexibility in adding, updating, and working with data sources. The source creation wizard has been removed, replaced with an expanded work area that you can use to update and access your data and data sources. |
| Source Creation API Updates | A new endpoint, `/api/sources/`, is now available to create and manage a single table source, or multiple entities as a fused source. Requires the ROLE\_CREATE\_SOURCES privilege. |
| Source Management API Updates | Use the new endpoint `/api/uploads/` to manage data for file uploads. |
| Global Settings API Update | Use the extended endpoint `/api/sources/{sourceID}/global-settings` to read (GET) and update (PUT) the global settings for a specified source. You can set `defaultVisualFilters` using this endpoint: any new visual created from this source will use the filters you’ve defined. |
| Interpolation For Filters | Composer now supports interpolation for Global Filters at the Source level and Visual/Dashboard level filters. Attribute and Number fields support interpolation with `Include` and `Exclude` operators, and Time filters support interpolation for the Variable(s) option. Tooltips are visible to users for applicable operators, and you can still define custom values. |
| Visual and Dashboard Updates | Composer now allows you to access and re-render visuals created using columns that you may not have access to, due to column security or hidden fields.  When you open a visual that uses columns restricted by column security or uses hidden fields in the field picker, grouping field picker, metric field picker, multi-metric field picker, or in a filter, Composer displays a message indicating which fields are restricted. You can now select the available column and re-render the visual. |
| Visual and Dashboard Link Updates | The dashboard links work area has been updated for easier linking for visuals and dashboards. Additionally, when you navigate to a child dashboard using a dashboard link from a parent dashboard, you can return to the previous dashboard by selecting **Back**. |
| Visual Types Updates | You can now, with appropriate permissions, manage Available Visual Types from the Actions menu for a specific source. Enable and disable Available Visual Types for a source as needed without affecting existing visuals for that source.  For example, disable Bar visual types for a source to prevent users from creating Bar visual types from that source. Existing Bar visuals from that source remain unchanged. |
| Live Mode and Playback Updates | You can now use expanded playback speeds for your data: 30 days, 90 days, 180 days, and 365 days. Depending on the field granularity you select, the appropriate options are shown, for example, if your granularity is set to month, you can select 30, 90, 180, or 365, but if set to a year, you can select 365. |
| Custom Metric and Derived Field Updates | You can now edit the names of custom metrics and derived fields in several places:   * Edit the Label field in the Settings panel of a selected metric or derived field when creating or updating a source. * Edit the label shown in the breadcrumb of the Custom Metrics or Derived Field editors. |
| List Widget Sorting | Use the Sort & Limit sidebar to change the sort order of items in the current display column in the list widget. Sort by ascending or descending for numeric fields, alphabetical or reverse alphabetical for alphabetical fields, and by chronological or reverse chronological date for date fields. |
| Attribute Fields Sorting Update | You can now select **No Aggregation** as an option in Sort & Limit work area of the sidebar menu for an attribute field used in grouping the data for a visual. If you select an attribute field not used in grouping, you can sort by Count or Distinct Count. |
| Update Custom Charts | You can now edit dynamic variable settings for your custom charts in the sidebar menu. |
| Expanded Map Markers | You can now add field information to map markers using the sidebar menu, allowing users to see the field information you set as a tool tip on hover. |
| Expanded Dashboard Import API Payload | The payload for `/api/dashboards/import` has been expanded to return the imported object's status as CREATED or REUSED. After import, you can search for objects by name or ID, and build the object dependency graph from the response. |
| Content Security Policies for Embedded Pages | You can now tailor your content security policies for embedded Composer pages. |
| Apache Solr, Cloudera Search and Elasticsearch Improvements | The keyword search for these connectors is now consistent with other search behaviors in the Composer UI to provide you with a better, more consistent user experience. elect a specific, preferred time field to sort by **Most Recent**. |
| zoomdata.properties Update | A new property, `source.sampling.rows`, is included in the `zoomdata.properties` file. With a default value of `1000`, this is used to define the number of rows to sample and estimate metadata characteristics (e.g. cardinality) of the source fields. |
| WebSocket Updates | The `access_token` has been moved from the WebSocket URL to WebSocket messages to improve the security of WebSocket communication for embedded dashboards. |
| Delete Filters Update | You can now delete filters that use keysets from sources you don’t have permission to access. |
| Composer Monitoring Solution | In order to provide Composer deployments with observability into the health and performance of the running system, you can use a monitoring solution. This feature describes an example monitoring solution that we make available for download with each release of Composer. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 7.9 Feature Enhancements** | |
| Source Creation and Source Creation API Updates | Composer now supports the migration of sources created in Composer v7.8 and earlier to the the updated source creation workflow.  As a part of this migration and update process, the source creation API available on Composer v7.8 and earlier is no longer available for source creation.  Before attempting to upgrade to Composer v7.9, please contact your support representative to ascertain which version of Composer is an appropriate upgrade. |
| Source Creation Updates - Data Access | Composer now supports permissions to allow source data access. Existing users with READ permission on a source are given DATA ACCESS permission for that source on upgrade to v7.9. Users with DATA ACCESS can create new visuals, and grant DATA ACCESS to other users. This new permission also applies to related API endpoints. |
| Calculation Editor Changes | Composer now displays data in Preview automatically for custom metrics, even when the Pivot Table is disabled for your source. You no longer need to enable the visual. |
| Custom Chart CLI Updates | * [Version 6 of the Custom Chart CLI](https://www.npmjs.com/package/zoomdata-chart-cli "Version 6 of the Custom Chart CLI") is now available. Use with v7.9 of Composer and later. * You can now enable and disable the visibility of settings in the side panel for a custom chart. Enable or disable this visibility in Controls when editing a chart. * The ability to edit the visibility of a custom chart using the CLI has been removed. Use CLI version 6 with Composer v7.9 and higher.  * Deprecated libraries and visualization library endpoints have been removed from Composer. Recreate any charts you made prior to upgrading to Composer v3.7 using the CLI. |
| Edit Custom Charts | You can now edit dynamic variable settings for the `ungroupedList` variables in the Composer sidebar menu of your custom charts. |
| Edit Visuals | You can now re-render some visuals that contain filters based on columns that you do not have permission to access. Delete the filter to re-render the visual. |
| Derived Fields and Custom Metrics Updates | * You can now create and edit custom metrics and derived fields in dashboards if you have the group privilege **Can Edit Calculations** or write permissions for the source used by the visual. * You cannot delete a custom metric or derived field if it is used by any visuals, materialized views, actions, or chart defaults. * You can remove an unused custom metric or derived field using the dashboard picker after you have saved the dashboard. * You can’t remove a derived field when selected in a picker. |
| Time Bar Updates | Composer now includes a zoom in option on the time bar by default. |
| Fusion Source Updates | After installing Composer v7.9, existing fusion sources are upgraded, inheriting row and column security, group names, and column filter names. |
| Map Settings | After upgrading to this release of Composer, tile provider information for sources is is moved from Map chart defaults to the source's global settings. |
| Source Editing Field Validation | Validation updates prevent you from removing a field from a source if the field is used by filters, cross-source links, join configurations, or actions.  This validation also applies to `DELETE /api/sources/${sourceId}/fields/${fieldname}` and `PUT /api/sources/${sourceId}` when a field is removed using the PUT method. |
| Duplicate Custom Metrics | The ability to duplicate custom metrics in the Composer interface has been removed. You can continue to use the appropriate API endpoints to create multiple custom metrics with different names that use the same underlying formula. |
| Elasticsearch Support Update | Composer now supports Elasticsearch 7.0 - 7.17. |
| Extended Source Listing | The endpoint `/api/inventory/` has been expanded to return additional information about dashboards and sources. Additionally, a new field, `associatedItems` is returned, indicating any associated items such as DATA\_SOURCE, CONNECTION, or UPLOAD. |
| CentOS Support Update | CentOS 8 is no longer supported by Red Hat Linux (RHEL). Use CentOS 7 instead for your Composer environment. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 7.8 Feature Enhancements** | |
| Visuals Updates | Composer now loads, renders, and operates standard visuals and custom visuals without using unsafe evaluations that may not comply with some organizations' CSPs. Load and retrieve visuals using `/api/visual-types/components/{componentId}/wrap/`. |
| Edit Custom Charts | You can now create and edit dynamic variable settings for the `singlelist` variables in the Composer sidebar menu of your custom charts. |
| Calculation Editor Changes | The calculation editor for visuals and dashboards has been redesigned in Composer to improve the source creation, derived fields, and custom metrics processes. |
| Loading Times | Composer now returns lists of users more efficiently when called in the user interface or using the API. User Name and User ID information are provided: select an individual user to return that user’s full user information. |
| Integer Data Type Update | Integer field types are no longer supported in Composer as a stand alone data type. When you import an `INTEGER` into Composer , it is represented as a `NUMBER` data type, with two decimal places set by default. |
| Text Data Type Update | Text field types are no longer supported in Composer as a stand alone data type. When you import `TEXT` into Composer , it is represented an `ATTRIBUTE` data type. |
| Group Privileges UI Updates | The Privileges work area in Composer now displays simplified group privilege options based on what functional area each privilege affects. Dependent privileges are listed and linked with required parent privileges. API Privilege Names remain unchanged. |
| Consul Support Updates | Composer now supports Consul version 1.11.4.   * If you update or install Composer in a non-clustered environment using the bootstrap script, Composer is installed or upgraded without further actions needed.  * For custom or cluster-based deployments, consult [the official Consul documentation](https://www.consul.io/docs/upgrading/instructions/general-process "Consul documentation link") to upgrade your environment to include Consul 1.11.4. |
| Distinct Count Metric | You can now select distinct count aggregation for derived `ATTRIBUTE` and `NUMBER` fields and in group filters. The distinct count metric is also returned for these fields by API. |
| Custom Chart Update | The option **Enable Menu** has been removed from the Manage Custom Charts work area in Composer. |
| Ubuntu OS Support Updates | * Composer no longer supports installation in Ubuntu 16.04 environments. * You can now install Composer in Ubuntu 20.04 environments. |
| Amazon Linux 2 Support | You can now install Composer in an Amazon Linux 2 environment. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 7.7 Feature Enhancements** | |
| KPI Chart Labels | You can now edit labels for KPI Charts using the visual sidebar menu. |
| KPI Color Settings | Use the Color sidebar in the visual sidebar menu to define color inheritance behavior of a KPI Chart, or to optimize colors for visual contrast. |
| Visual Setting Support Updates | Several visual pickers for Composer have been redesigned for speed and ease of use. These include Color, Columns, Comparison Metric, Granularity, Group, Histogram, Metric, Rows, Size, Time Bar, Trend, X Axis, and Y Axis. The redesigned pickers utilize React/Redux to reduce reliance on Bootstrap JS and CSS. |
| Map Marker Settings | You can now use the Settings sidebar in the visual sidebar menu to adjust and save settings for a map visual's **Latitude**, **Longitude**, and **Lat/Long** Limit. |
| Map: World Countries | You can now adjust both **Country** and **Comparison Metric** for a Map: World Countries visual using the axis field label picker or the visual sidebar menu. |
| Library View Support Update | URL links to quick filters have been removed from the Dashboard Library to provide a more streamlined interface and embedding experience. Functionality of the quick filter icons remain unchanged. |
| Custom Charts Variable Support | You can now add custom variables to custom charts, including Boolean, String, and Text. Edit the variables you’ve added using the visual sidebar menu. |
| Impala Support Update | Composer v7.7 now supports use of multiple countd functions in a single query without needing to set `impala.approx-distinct-count=true` in the connector's configuration. |
| MemSQL Support Update | You can now use MemSQL versions 7.1 to 7.6 with Composer v7.7. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 7.6 Feature Enhancements** | | |
| Custom Volume Metrics | When you create a new source, Composer presents Volume as a custom metric, using the **Count(\*)** expression. Volume metrics for existing sources are converted to a custom metric. All Volume metrics are accessible from the Custom Metric work area. |
| Map: US Regions | When working with a US Regions map visual, you can now adjust and save attribute changes for **State**, **County**, and **Zip Code**, or set **Limits** as needed in the Settings panel. |
| Inherit Y-Axis Values | Combo chart Y axes can now inherit values from the Y-1 axis. |
| Volume Metrics - Custom Charts | After upgrading to Composer v7.6, update the source information for any custom charts that use the Volume metric, removing references to `controller.source.volumeMetric`. |
| Details Dialog | Use the redesigned details dialog to easily view and export raw data for single and fusion data sources. |
| Impala Support Update | You can now use Impala versions 3.2 to 3.4 with Composer v7.6. |
| MS SQL Support Update | The minimum version of MS SQL you can use with Composer v7.6 is v11.0 (SQL Server 2012). |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 7.5 Feature Enhancements** | | |
| User Auditing | Composer now supports robust user auditing for data accessed directly in the Composer UI, via an API, or as embedded objects. |
| Trusted Access | Composer now manages trusted user access in a more streamlined fashion utilizing two new and expanded endpoints. |
| Histogram Updates | The Cumulative Line setting for Histograms is now in the Settings panel. Several label changes correctly reflect the changes you make to a histogram. |
| Map: Markers Update | Map: Markers creation is now simplified in Composer. Max Zoom and Start Zoom can now be configured in the Settings sidebar. |
| Count Metrics for Materializations | Composer now requires you add a Count mapping when creating a new materialization view. |
| Extended Object ID | Composer now creates IDs for system objects, up to 36 characters in length, when you create or migrate objects. |
| Dashboard Reporting Support | The concurrent session count licensing restrictions apply to the trusted access token created for each recipient of the dashboard report. If the license limit is reached, the report won’t be sent. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 7.4 Feature Enhancements** | | |
| List Widget Display and Value Columns | You now have the ability to use different fields in the List Widget Display and Value columns. |
| Pivot Table Display Options | New Pivot Table options in Composer allow you to control how your pivot table data is displayed: **Rows Per Page**, **Column Limit**, and **Cell Limit**. |
| Count Aggregation | Composer now includes Count as an available aggregation for attributes, Grouped filters, and in Sort & Limit. |
| Pivot Table Row and Column Totals | The Pivot Table Settings sidebar now includes a **Totals** section, and two options to hide or display a Totals Row and Totals Column. |
| Chart Defaults | Source chart creation is now simplified in Composer. Several chart default options have been removed from the process: **Display Legend**, **Number of Bars**, **Axis Value**, and **Show Cumulative Line**. |
| Inherit Colors from Themes | Composer now supports theme color inheritance for the **Histogram**, **Line & Bar**, and **Combo** Charts. |
| SparkSQL Connector for AWS Databricks | Composer now supports a SparkSQL connector for AWS Databricks. |
| Oracle Connector Support Update | Composer Oracle connector now supports Oracle versions 11.2 - 21c. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 7.3 Feature Enhancements** | | | | | | |
| Nested Filters Support | You can now create nested filters in the Composer UI. |
| Distinct Count Aggregation | Composer now provides Distinct Count aggregation for all Attribute, Numeric and Integer fields. |
| Expanded RLE and Interpolation Support in Security Filters | Extended security filters now support existing row-level functions and admin-defined functions, and can use interpolation. |
| Null/Zero Conversion for KPI Charts | A new toggle "Display Null as Zero" is now available for KPI Charts, enabling you to change the display from 'Null' to '0' in cases where there is no data. |
| AWS Elasticsearch IAM Roles | Composer now supports IAM role authentication for Elasticsearch when running on an EC2 instance using AWS. |
| Multiple Datasources in Library View | The library view in Composer now displays all data sources used by each dashboard. |
| Radial Menus for Pivot Tables | You can now use the radial menu to access Details for grouped row values in pivot tables. |
| Custom SQL for BigQuery | You can now create Google BigQuery data sources that include custom SQL. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 7.2 Feature Enhancements** | | | | | | |
| List Widget Dropdown Option | You now have the option to select the **Dropdown** display style with single selection for the Filter list widget. |
| Library Embedding | The **Library** is now a standalone embeddable component so that you can quickly build out a self-service framework for your customers and end users. |
| Keyset Exclude Filter | You can now exclude keyset values in your filter. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 7.1 Feature Enhancements** | |
| Dashboard Import Changes | You can now use the API to import a dashboard using a new overwrite policy, so that dashboards with the same name are overwritten instead of being imported with a slightly altered name. |
| New Bullet Gauge | This release introduces a new visual style called a bullet gauge. Bullet gauges are based on a single metric. The metric is mapped against a background bar that shows value ranges using color. |
| Automatic KPI Metric Color Option | When **Inherit from Theme** is not selected for the **Metric Color** field in a KPI chart and you select the color in the Metric Color field to access the color dialog, an **Auto Color** option is now available on the color dialog. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 7.0 Feature Enhancements** | |
| Arc Gauge Updates | The **Show label description** and **Show as percentage** switches no longer appear on the Rulers sidebar for the gauge. They appear on the Settings sidebar and the Colors sidebar for the gauge instead. The **Show as percentage** arc metric switch has been renamed **Show Values As** and provides two options: **Absolute** and **Relative**. The **Show as percentage** color metric switch has been renamed **Thresholds in Percentage**. |
| KPI Chart Updates | You can now apply color formatting thresholds to the background color of a KPI chart. The default is to apply the color formatting thresholds to the displayed KPI chart value. A new **Apply Formatting To** setting is provided in the Color sidebar for KPI chart and in the data source KPI chart defaults. Valid values for the setting are **Metric** or **Background**. |
| Amazon Web Services (AWS) Authentication Support for Elasticsearch Connectors | Support for authentication with Amazon Web Services (AWS) credentials was added to the Composer Elasticsearch 6 and Elasticsearch 7 connectors in this release. |
| Custom Metric Date and Time Aggregation Function Changes | Custom metrics now support the `now()` and `time_add` functions used by row-level expressions. The original custom metric `DATE()`, `DateADD`, and `DateSUB` functions still work but should no longer be used. They are deprecated in this release and will be removed in a future release. Instead, use the `now()` and `time_add` functions. |
| New Custom Metric Filter Operators | Five new custom metric filter operators have been added: IS NULL, IS NOT NULL, STARTS WITH, ENDS WITH, and CONTAINS. Values supplied in WHERE clauses in reference to STARTS WITH, ENDS WITH, or CONTAINS are case-sensitive. |
| Dashboard Import Changes | You can now use the API to import a dashboard using a new overwrite policy, so that dashboards with the same name are overwritten instead of being imported with a slightly altered name. |

[Return to top](#top "return to top")

### Composer v6.9 and Earlier

| Title | Description |
| --- | --- |
| **Composer 6.9.29 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.28 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.27 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.26 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.25 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.24 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.23 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.22 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.21 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.20 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.19 Feature Enhancements** | |
| Expanded OpenStreetMap Support | You can now create map visuals using a custom URL that points to a local or other specific instance of OpenStreetMap. Enter the URL in the **Provider URL** field, available after selecting OpenStreetMap as the Tile Provider for a visual in Composer. |
| **Composer 6.9.18 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.17 Feature Enhancements** | |
| Time Bar | Composer now loads, renders, and operates standard visuals and custom visuals without using unsafe evaluations that may not comply with some organizations' CSPs. |
| Loading Times | Composer now returns lists of users more efficiently when called in the user interface or using the API. User Name and User ID information are provided: select an individual user to return that user’s full user information. |
| **Composer 6.9.16 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.15 Feature Enhancements** | |
| Modified Date Display | Composer now displays the modified date and time for sources, visuals, and dashboards in your local date and time. |
| **Composer 6.9.14 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.13 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.12 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.11 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.10 Feature Enhancements** | |
| Null/Zero Conversion for KPI Charts | A new toggle, **Display Null as Zero** is now available for KPI Charts, enabling you to change the display from `Null` to `0` in cases where there is no data. |
| **Composer 6.9.9 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.8 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.7 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.6 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.5 Feature Enhancements** | |
| Keyset Exclude Filter with CSV Upload | You can now exclude keyset values uploaded via CSV files in your filter. |
| **Composer 6.9.4 Feature Enhancements** | |
| None. |  |
| **Composer 6.9.3 Feature Enhancements** | |
| Dashboard Import Overwrite Permission Updates | The overwrite policy behavior for imported dashboards now honors the write permissions for all the dashboard components: the dashboard itself, its visuals, and the data sources used by its visuals. |
| **Composer 6.9.2 Feature Enhancements** | |
| Custom Metric Date and Time Aggregation Function Changes | Custom metrics now support the `now()` and `time_add` functions used by row-level expressions. The original custom metric `DATE()`, `DateADD`, and `DateSUB` functions still work but should no longer be used. They are deprecated in this release and will be removed in a future release. Instead, use the `now()` and `time_add` functions. |
| Dashboard Import Changes | You can now use the API to import a dashboard using a new overwrite policy, so that dashboards with the same name are overwritten instead of being imported with a slightly altered name. |
| **Composer 6.9.1 Feature Enhancements** | |
| None. |  |
| **Composer 6.9 Feature Enhancements** | |
| License Changes | This release implements a new license file structure.  **Important:** Older license keys are not compatible with Composer 6.9. If you are upgrading from any older Composer or Zoomdata release, a new license must be requested. |
| Authorization Changes | Two new privileges, **Can Create Visuals** and **Can Manage Visual Permissions** are introduced in this release to support the updates made for visual permissions.  If a user is granted the **Can Administer Visuals** privilege, they are now automatically granted both the **Can Create Visuals** and **Can Manage Visual Permissions** privileges as well.  A non-administrative user must have the **Can Create Visuals** or **Can Administer Visuals**group privilege to add a visual.  Finally, a non-administrative user must also have the **Can Create Visuals** (or **Can Administer Visuals**group privilege to import a dashboard. In prior releases, they only needed the **Can Create new Data Sources** and **Can Create Dashboards**group privilege. |
| Security Key Updates | Security keys are deprecated in this release and will be removed from the product in a future release. Use Trusted Access instead for all embedded workflows. See Trusted Access.  However, while Composer still supports security keys, the previous method of authorizing the use of visuals using new security keys changed due to the introduction of visual permissions in this release. |
| Connector Updates | The Elasticsearch 6 connector now supports Elasticsearch versions up to 6.8. In past Composer releases, the maximum supported Elasticsearch 6 version was 6.7. |
| The Elasticsearch 7 connector now supports Elasticsearch versions up to 7.12. In past Composer releases, the maximum supported Elasticsearch 7 version was 7.6. |
| The MySQL connector now supports MySQL versions 5.6 through 8.0. In past Composer releases, the only supported MySQL version was 5.6. |
| New InterSystems IRIS Connector | This release introduces an InterSystems IRIS connector. This connector lets you access the data available in an InterSystems IRIS data platform using the Composer client. |
| New Visual Permissions | This release introduces visual permissions. Visual permissions allow you to permit your entire account, groups within your account, or users within your account to read, write, or delete a visual. This allows you to share a visual with other users. API updates have been made to support this new functionality. |
| In past releases, if a user had Read permissions for a data source, they also had Read permission to any visuals created using the data source. However, with the introduction of visual permissions in this release, this is no longer true. With this release, authorization for visuals is now controlled by visual permissions. |
| Dashboard Save Changes | Saving dashboards has changed to support visual permissions. |
| The Save and Save As options that were available from a drop-down menu off of the dashboard icon bar have been separated. With this release, two icons on the dashboard icon bar are now provided: one for Save and one for Save As. |
| Dashboard save processing and dashboard copy processing have been improved and the Save Options and the Save As Options dialogs have changed to reflect the improvements. |
| **Note:** Pre-existing visuals are no longer automatically saved when you save a dashboard (new visuals are automatically saved). You must explicitly elect to save pre-existing visuals on the dashboard Save Options dialog. |
| Dashboard Link Changes | Dashboard link information is no longer stored with visual definitions, but with the dashboard definitions. When you upgrade to Composer 6.9, the dashboard link information is automatically upgraded for you. |
| Dashboard Javascript Embed Update | A new `composer-dashboard-failed` event has been added to the product and can be used in your Javascript embed code to control what happens when a dashboard fails to load. |
| New Dashboard Interactivity Setting | A new dashboard interactivity setting is introduced in this release: **Share Filter Sets**. |
| Visual Save Changes | The option to **Save** a visual with its current name has been removed from the visual drop-down menu. Instead, the save icon appears at the top of visuals that need to be saved. This icon allows you to save the visual with its current name. To save it using a new name, use the new **Save As** option. |
| New Visual Save As Support | A new **Save As** option on the visual drop-down menu when a visual is edited in a dashboard, a new icon on the visual when edited in the Visual Gallery, and a new Save As Options dialog have been added. Use these to save a visual with a new visual name. The original visual still exists with its original name in the system. |
| Visual Name Uniqueness | Visual name uniqueness is now enforced with this release. |
| New List Filter Visual Style | A new visual style called a list filter has been added to the product. A list filter visual can be used to list values of a data source field in a visual. You can select one or more of the field values in the list to quickly apply a filter to other visuals in the dashboard that subscribe to a cross-visual filter for the field. |
| New Stacked Area Chart Options | New **Display as stacked** and **Stacking Style** options on Line Trend: Attribute Value visuals allow you to create stacked area charts. |
| Table Changes | If a table has been grouped, the options to export its raw or visual data are no longer available. You cannot export raw and visual table data after it has been grouped. |
| New Visual Interactivity Settings | Three new visual interactivity settings are introduced in this release: **Maximize**, **Rename**, and **Show Time Bar Panel**. |
| Experimental Materialized View Enhancements | You can now create materialized view definitions using the Composer UI. In past releases, they could only be created using the API. This is an experimental feature.  **Important:** This is an experimental feature. |
| New Experimental Alerting API Functionality | This release introduces new API endpoints that you can use to alert your end users when a metric reaches a specified threshold.  **Important:** This is an experimental feature. |
| Keyset Updates | An error now displays when an attempt to upload keyset values uses a keyset upload file that contains more records than are allowed by the Composer environment configuration. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 6.8 Feature Enhancements** | |
| Query Engine Enhancements | The INFO-level messages logged by the query engine are enhanced to include more information about the request execution. |
| Visual Data Cache Changes | Visuals with some dynamic time ranges can now be cached. In past releases, visuals with dynamic time range filters were never cached. |
| Authorization Changes | Groups can no longer be transferred to a different account using the API. |
| New Dashboard Cross-Visual Filtering Controls | New dashboard cross-visual filtering controls are introduced in this release. You can now specify which cross-visual filter each dashboard visual publishes (which link fields it can apply cross-visual filtering for) and which cross-visual filter each visual subscribes to (which cross-visual filters can be applied to the visual). Cross-visual filters are filters created using same-source and cross-source link fields established in the dashboard.  Custom charts support cross-visual filtering controls if the chart supports the radial menu and filtering and if the appropriate publish and subscribe controls are enabled.  Cross-visual link publish and subscribe settings for a dashboard can be specified for embedded dashboards using JavaScript. Two JavaScript methods are provided with the `Zoomdata` object: `publish` and `subscribe`. |
| Radial Menu Changes | Use of the radial menu to apply cross-visual filters for cross-source links to other visuals in a dashboard has now been extended to also apply filters for same-source links, based on the publish and subscribe settings for the dashboard and its visuals. |
| Cross-Source Link Changes | The cross-source links dialog has changed in this release. In addition, cross-source links can now be published and subscribed using the new dashboard link controls. |
| Filter Changes | Cross-visual filters that are applied from same-source and cross-source links are now listed separately on the Filters sidebar from filters that are applied from the Filters sidebar. In addition, you can now view them from a drop-down dialog when you select the filter icon on the visual. |
| API Updates | The Composer API specification is now generated in OpenAPI 3.0 format. |
| Arc Gauge Changes | The maximum value for the arc gauge can now be determined by a second metric. A new **Static maximum value** switch is added to the Rulers sidebar for arc gauges that you can use to specify whether or not a second metric is used. |
| A new **Show Label Description** switch is added to the Rulers sidebar for arc gauge. Use this switch to display a description for the label on the gauge. |
| Percentages can now be used for the arc gauge metric range. A new **Show as percentage** switch is added to the Rulers sidebar for arc gauges that you can use to activate this. |
| You can now determine the maximum value of the color metric based on a different metric. A new **Static maximum value** switch is added to the Rulers sidebar for arc gauges that you can use to specify whether or not a second metric is used. |
| Percentages can now be used for the color rules of the color metric on the Color sidebar for the gauge, if the new **Show as percentage** switch is switched on for the color metric. |
| Table Enhancements | You can now specify the **Rows per Fetch** for an individual table. In past releases, this could be set at the data source level, but not for an individual table. |
| Dashboard and Visual Export Changes | The icon you select to export a dashboard or a visual has changed and the Export As PDF dialog is redesigned. In addition, when you export a dashboard to a PNG file, the PNG file is created and downloaded without an intermediate step. |
| Keyset Enhancements | You can now update the values of a keyset from a CSV file. |
| The keyset details panel that appears in the filters sidebar is updated visually. |
| User Interface Changes | A new icon is now added to visuals when they are subscribed to a dashboard cross-source or same-source link filter. |
| The cross-source links dialog has changed in this release. It is now available on a tab in the new Dashboard Interactions dialog that is also used to specify dashboard visual interaction controls. |
| Cross-visual filters that are applied from same-source and cross-source links are now listed separately on the Filters sidebar from filters that are applied from the Filters sidebar. |
| The Export As PDF dialog is redesigned to Composer's current standards. This dialog appears when you export a dashboard. In addition, the dashboard icon you select to export a dashboard has changed. |
| All dashboard, visual, visual gallery, and dashboard library warning dialogs are updated to a new style. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 6.7 Feature Enhancements** | |
| Permission Changes | Data source and dashboard permissions have some additional restrictions added in this release. You now can only assign dashboard or data source permissions equivalent to your own. |
| Read, write, and delete permissions for a visual are now controlled by the permissions assigned the data source used by the visual in combination with the user's group privileges. The creator of a visual is automatically granted read, write, and delete for the visual in the Visual Gallery, but when they are removed from the system, the supervisor is assigned ownership for the visual. |
| Connector Updates | The MongoDB connector now supports MongoDB versions up to 4.4. |
| New Dashboard Interactivity | This release introduces new dashboard interactivity settings you can use to control how users can interact with a dashboard after it is embedded. Dashboard interactivity settings allow you to control whether users can change the layout, add visuals to the dashboard, delete the dashboard, save the dashboard, filter the dashboard, rename the dashboard, add the dashboard to favorites, set up or change dashboard links, set up or change cross-source links, refresh the dashboard, export the dashboard to PNG or PDF format, or export the dashboard configuration. They also allow you to override the individual visual interactivity settings for the visuals in the dashboard. |
| Visual Interactivity Changes | With the introduction of dashboard interactivity, visual interactivity is removed from the visual sidebar menu when you edit a visual in a dashboard. Visual interactivity settings are still available for visuals when you edit the visual in the Visual Gallery.  In addition, a new **Preview Interactivity Settings** switch allows you to test the visual interactivity settings when you edit visual interactivity in the Visual Gallery. |
| Embedded Dashboard Changes | Embedded dashboards can now be controlled by dashboard interactivity settings. Several new properties and a new object for the Javascript `createComponent` method used to embed dashboards are added in this release to support dashboard interactivity. |
| New Embedded Visual Authoring | This release introduces the ability to embed Composer's visual authoring experience in your applications using JavaScript. This allows your users to add and maintain the visuals embedded in a dashboard. |
| New Combo Chart Visual | A new combo chart visual is added to Composer in this release. In addition, a new interactive legend is introduced for combo charts; the legend used by other visuals is not supported. |
| Arc Gauge Changes | You can now specify the minimum and maximum values of the metric that determines the color of the arc gauge on the Rulers sidebar. |
| The maximum value for the arc gauge can now be determined by a second metric. |
| Percentages can now be shown for an arc gauge metric. |
| You can determine the maximum value of the color metric based on a different metric. |
| Percentages can now be used for the color metric on the Rulers sidebar and used in the color rules for the metric on the Color sidebar for the gauge. |
| You can now view the raw values for the arc gauge metric and identify the metric used to determine the maximum value. |
| Keyset Enhancements | An administrator can now remove keysets they did not create. |
| You can now upload a keyset from a CSV file using the API. |
| A new **Upload Keyset Values** button on the Keyset tab of the Filters sidebar allows you to select a CSV file containing keyset values and save the value list with a new keyset name. |
| New Quarter Granularity Option | This release introduces the quarter granularity option for date and time fields. |
| Fused Data Source Changes | Text fields can now be joined in fused data sources. |
| Distinct Value Updates | When custom ranges or list values are requested for a field, full data scans are no longer performed. |
| Radial Menu Updates | Null values can now be removed from a visual using the radial menu **Remove** option. |
| User Interface Changes | The dashboard icon bar has changed. Cross-source links now have their own icon option and are split out from dashboard linking. |
| A new Dashboard Interactivity panel is introduced in the UI to support dashboard interactivity. |
| With the introduction of dashboard interactivity, visual interactivity is removed from the visual sidebar menu when you edit a visual in a dashboard. Visual interactivity settings are still available for visuals when you edit the visual in the Visual Gallery. |
| You can now edit a visual when it is maximized in a dashboard. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 6.6 Feature Enhancements** | |
| Authorization Changes | The group privilege **Can Manage Visuals** was renamed to **Can Administer Visuals** in this release. The corresponding API privilege **ROLE\_MANAGE\_VISUALS** was also renamed to **ROLE\_ADMINISTER\_VISUALS**. Customers who use the API to manage groups must manually make this change wherever **ROLE\_MANAGE\_VISUALS** is currently used; if you use the Composer user interface (UI) to manage groups, the change will happen automatically. |
| In addition, to alter and save an individual visual in a dashboard now, you must either be assigned to a group with the **Can Administer Visuals** (**ROLE\_ADMINISTER\_VISUALS**) privilege or be the creator of the visual. |
| Connector Updates | The maximum version of Spark SQL data stores supported by the Composer Spark SQL connector is now version 3.0. |
| COALESCE Function Changes | The COALESCE function now supports aggregate metrics with complex calculations using arithmetic functions (for example `COALESCE(max(sales) * 1.3, 0)`), so a default value can be used if null values are returned. |
| Performance Improvements | Improved server start times by 15 percent. |
| User Interface Changes | Labels on bar charts are upgraded to take into account the bar color as well as the background color of the UI. |
| Table data can now be aggregated by group field if the group field is not the first group field for the table and the data source indicates that the group field can be aggregated. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 6.5 Feature Enhancements** | |
| New Trusted Access Authorization Introduced | Composer now provides its own security methodology that allows for machine-to-machine authorization of Composer resources when embedded in your application (the “parent” application). This is a form of “delegated” authorization where the parent application can determine, on demand, how and when to authorize any given embedded Composer component to an end-user logged into the parent application. This methodology is called *Trusted Access*.  **Note:** insightsoftware recommends using Trusted Access for all embed-related workflows. |
| Embedded Dashboard Changes | Significant changes were made to how dashboards can be embedded in your applications. Primarily, while your existing embedded dashboard HTML snippets will continue to work, this release introduces the ability to embed dashboards using JavaScript code. This is more powerful than the HTML script snippet provided in previous releases because it provides you with more tailoring options for the dashboards in your application.  **Note:** insightsoftware recommends using Trusted Access for all embed-related workflows. |
| User Interface Changes | The Advanced options (**Root**, **Embed ID**, **Show Banner**, **Show Header**, **Show Logo**, **Show Title**, **Show Breadcrumbs**, and **Show Actions**) previously available on the Embed Code dialog that produces an embeddable HTML script snippet are removed. |
| The **OAUTH** option on the Security page of the Supervisor UI is renamed **Trusted Access & OAUTH**. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 6.4 Feature Enhancements** | |
| Raw Data Table Changes | Multiple changes were made to raw data tables, including:   * UI references to "raw data tables" or "raw data table" are changed to simply "tables" or "table." * A context menu is added to table column headings. * You can now group tables. * You can aggregate metrics in a table. * You can set even time intervals in a table. * You can alter the granularity of a time field in a table. |
| Data Source Configuration Changes | A new "Data Unavailable" message now appears when an error occurs obtaining data from a data source for a row security filter. In addition, if a row security filter returns no results, a new "No search results" message appears. |
| The default settings available for tables in a data source configuration have changed. |
| Caching Changes | A new metadata cache to cache field statistics and improve overall metadata caching performance is introduced. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 6.3 Feature Enhancements** | |
| Installation Changes | CentOS 6 is no longer supported and the special installation Bootstrap procedure (`bootstrap-zoomdata-centos6.run`) is no longer provided with this product. CentOS 6 is no longer supported by Red Hat Linux (RHEL). Use CentOS 7 or 8 instead. |
| Red Hat Linux 6 and Scientific Linux are no longer supported. |
| Rebranding Updates | The `Content-Type` header `vnd.zoomdata.v2+json` is no longer supported in version 5.9.1 and later and can no longer be used as the `Content-Type` for API routes. It is removed from the product. Use `vnd.composer.v2+json` as the `Content-Type` for API routes instead. |
| Custom Chart CLI Changes | A new version 5 of the custom chart CLI is introduced in this release. |
| Elasticsearch Connector Changes | Support for Composer Elasticsearch 6 and 7 indices with a disabled `_source` field or with a `_source` field with exclusions is introduced. In past releases, only Elasticsearch data stores with the `_source` field enabled and with no exclusions were supported. |
| A new `elasticsearch.inner-hits.size property` is introduced for Elasticsearch 6 and 7 connectors. |
| Data Source Permissions | This release introduces source permissions, the ability to permit your account or specific groups or users in your account to read, write, or delete a data source configuration.  As a result of the introduction of data source permissions in version 6.3, the ability to restrict data sources within group definitions is removed. Use data source permissions instead. |
| Column Security Updates | This release introduces support for multiple groups in a data source column security filter. In past releases, only a single group could be selected for a column security filter. |
| Authorization Updates | A new **Can Manage Source Permissions** privilege is added. |
| A new **Can Administer Sources** privilege is added. |
| The **Can Export Dashboards & Data Sources** privilege is renamed to simply **Can Export Dashboards** in this release. |
| The API privileges ROLE\_DELETE\_ALL\_SOURCES, ROLE\_MANAGE\_ALL\_SOURCES, ROLE\_VIEW\_ALL\_SOURCES, and ROLE\_MANAGE\_SOME\_SOURCES are removed from the product. |
| User Interface Changes | A new Permissions column is added to the Sources page. |
| The Column Security dialog is changed to support multiple group column security filters. A new Add Groups button is provided that activates a new Add Groups dialog. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 6.2 Feature Enhancements** | |
| Rebranding Updates | The name Zoomdata was replaced with Composer in error messages for source and dashboard imports as well as in several messages in log files. |
| Authorization Updates | The user experience when saving, updating, or sharing a dashboard is now consistent whether you use the Composer user interface or its API. |
| New Dremio Connector | A new Dremio connector is introduced in this release. |
| Data Source Changes | Data source configurations can no longer be disabled. Once they are enabled, they cannot be disabled by anyone. |
| Data Source Row Security And Column Security Changes | The row security and column security restrictions specified for a data source configuration can now reference the same field in the data source. In past releases this was not possible. |
| User Interface Changes | LDAP errors that occurred when logging in as a user whose Composer account was changed since the LDAP user definitions were established are resolved. |
| An error now appears if you try to import a dashboard that contains a visual that does not exist in Composer. |
| Null values can now display as zeros in line charts (including line & bar, multiple metric, and attribute line charts). A new **Display null as zero** checkbox is added when you set the granularity for time fields on line charts. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **Composer 6.1 Feature Enhancements** | |
| Query Engine Changes | A new property for the query engine was introduced in this release: `qe.max.rows.during.execution`. Use this property in the query engine properties file (`/etc/zoomdata/query-engine.properties`) to limit the number of rows of data that can be processed for a single query. |
| Data Source Configuration Changes | You can now insert variables in the custom SQL of a data source configuration and specify defaults for those variables. |
| Row Security Changes | Row security is enhanced in this release to allow you to use filters to restrict data source data for specific users or accounts. In past releases you could only restrict the data for specific groups. |
| User Interface Changes | The **Default** option on the visual drop-down menu is removed in this release. You can still specify the default settings for a visual style in a data source using the Visuals tab in the data source configuration wizard. |
| The Clear Cache icon on the Sources page has moved from its own column to the Actions column. In addition, the icon used for the Clear Cache button has changed. |
| The dashboard library is modified to match the look of the Sources and Connections pages as well as the Visual Gallery. The side menu is removed and the options on the side menu are converted to buttons at the top of the page. |
| Pagination mode is introduced for viewing raw data tables. You can now use a new pagination bar at the bottom of a raw data table to page through and view the fetched data. |

[Return to top](#top "return to top")

|  |  |
| --- | --- |
| **6.0 Enhancements** | |
| Migration Considerations | With this release, you can no longer use `<hostname>:8080/zoomdata/api/version`. This is no longer supported. Use `<hostname>:8080/composer/api/version` instead. |
| The `server.multiple-context-path.primary` and `server.multiple-context-path.secondary` properties in the `zoomdata.properties` file are deprecated. |
| If your installation uses Kerberos, the default behavior for unauthenticated users has also changed. From a browser, unauthenticated users are now redirected to the Composer login page. For API calls, links in the format `<hostname>:8080/api/version` or `<hostname>:8080/zoomdata/api/version` now return an unauthorized 401 error. To resolve the error, use `<hostname>:8080/composer/api/version`. |
| Rebranding Updates | The Service Monitor was rebranded. |
| Error messages in the UI were rebranded. |
| The word "chart" was changed to "visual," where appropriate, in the translation file used for internationalization. |
| Derived Field Changes | You can now use the `NOW()` function in a derived field definition to obtain the current date and time. However, `NOW()` functionality is not enabled by default. |
| User Interface Changes | The color of the **Add Filter** button on the Row Security dialog and on the Column Security dialog was adjusted to align with the color of other buttons in the UI (it is now blue) and the button was moved from the left side of the dialogs to the right. |
| A row security filter can now be assigned to more than one Composer group. In past releases, it could only be assigned to one group. |
| If a user belongs to more than one group, each with separate row security filters for the same data source, an error message now appears when the user tries to view a dashboard using the data source. |
| You can now use derived fields (row-level expressions) in row security filters. |
| Color palette names can now be translated using the translation file. |
| When a dashboard is embedded in an application, its sidebar now becomes a pop-up dialog (instead of a sidebar) when it is opened. |
| The maximum length of dashboard and chart descriptions has increased from 255 characters to 750 characters. |

[Return to top](#top "return to top")

## Resolved Issues

### Composer v26

| Title | Description |
| --- | --- |
| **26.1.2 Resolved Issues** | |
| Updates | This service pack includes various internal fixes. |
| **26.1.1 Resolved Issues** | |
| Dashboard & Visual Loading | Corrected an issue in Windows environments where the Edit Dashboard page returned an error when you refreshed or duplicated the browser tab. The dashboard editor now correctly persists its state across page refreshes and duplicate tabs. |
| Authentication Methods | Expanded the documentation provided with the Composer API to include more information about `basicAuth` and `trustedAccessAuth`. |
| Time Zone Display | Fixed an issue where the Time Bar's From and To values could display mismatched time zones in visuals. |
| **26.1 Resolved Issues** | |
| None. |  |

### Composer v25

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
| Embed Visual Event Trigger | A new setting, `fireOnEveryChange`, is now available for embedded dashboards. Disabled by default, enabling this makes it easier for you to track and respond to all user interactions within a dashboard.  When enabled, dashboards send out change events (`dashboard-level`/`visual-level updates`) every time something is modified: sorting, filtering, visual settings, and more. This gives you more granular visibility into user actions.  When disabled, events were are only triggered once for `dashboard-level`/`visual-level changes`.  Enable in the embed SDK configuration. See [Embedded Events](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070829709-Embedded-Events). |
| DNS Name Change Configuration | When updating the Composer site DNS name, ensure the correct base URL is configured in:   * Zoomdata properties file (on-premise Linux) * Helm charts (Kubernetes) * Zoomdata properties file (on-premise Windows)   This resolves site errors that occur after DNS name changes. |
| Consul Updates | Consol has been upgraded to version 1.22.1. |
| **25.4 Resolved Issues** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **25.3.7 Resolved Issues** | |
| Updates | This service pack includes various internal fixes. |
| **25.3.6 Resolved Issues** | |
| Dashboard & Visual Loading | Corrected an issue in Windows environments where the Edit Dashboard page returned an error when you refreshed or duplicated the browser tab. The dashboard editor now correctly persists its state across page refreshes and duplicate tabs. |
| Authentication Methods | Expanded the documentation provided with the Composer API to include more information about `basicAuth` and `trustedAccessAuth`. |
| Time Zone Display | Fixed an issue where the Time Bar's From and To values could display mismatched time zones in visuals. |
| **25.3.5 Resolved Issues** | |
| Large Data Value Handling in OData | A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.   * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option. * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.   Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests. |
| **25.3.4 Resolved Issues** | |
| Embed Visual Event Trigger | A new setting, `fireOnEveryChange`, is now available for embedded dashboards. Disabled by default, enabling this makes it easier for you to track and respond to all user interactions within a dashboard.  When enabled, dashboards send out change events (`dashboard-level`/`visual-level updates`) every time something is modified: sorting, filtering, visual settings, and more. This gives you more granular visibility into user actions.  When disabled, events were are only triggered once for `dashboard-level`/`visual-level changes`.  Enable in the embed SDK configuration. See [Embedded Events](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070829709-Embedded-Events). |
| Consul Updates | Consol has been upgraded to version 1.22.1. |
| **25.3.3 Resolved Issues** | |
| Time Bar Settings | You can now enable a time bar option in your environment that allows the time bar slider to snap to the closest interval of the defined granularity for a specific source. This is disabled by default: enable the new server-level variable, **timebar-snap-to-interval** to use in your environment.  See [Server-Level Variables](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables). |
| US Region Maps | Corrected an issue that prevented display of a US Region Map visual to which a new data column had been added. |
| **25.3.2 Resolved Issues** | |
| Updates | This service pack includes various internal fixes. |
| **25.3.1 Resolved Issues** | |
| Time Bar | By default, the Time Bar will display time information as presented in the associated data source with no offsets or bounds to the time field. If you are using UTC, this is indicated in the time bar. If the time is derived based on other settings, this is indicated in the time bar. |
| Source Selection - Creating Visuals | Corrected an issue that prevented display of source names during visual creation. |
| API Update | Corrected an issue that did not return multiple data type options for aggregation functions such as `LAST_VALUE` from `api/sources/<sourceid>/expression-syntax`. |
| **25.3 Resolved Issues** | |
| None. |  |

[Return to top](#top "return to top")

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
| Embed Visual Event Trigger | A new setting, `fireOnEveryChange`, is now available for embedded dashboards. Disabled by default, enabling this makes it easier for you to track and respond to all user interactions within a dashboard.  When enabled, dashboards send out change events (`dashboard-level`/`visual-level updates`) every time something is modified: sorting, filtering, visual settings, and more. This gives you more granular visibility into user actions.  When disabled, events were are only triggered once for `dashboard-level`/`visual-level changes`.  Enable in the embed SDK configuration. See [Embedded Events](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070829709-Embedded-Events). |
| Consul Updates | Consol has been upgraded to version 1.22.1. |
| **25.2.6 Resolved Issues** | |
| Time Bar Settings | You can now enable an time bar option in your environment that allows the time bar slider to snap to the closest interval of the defined granularity for a specific source. This is disabled by default: enable the new server-level variable, **timebar-snap-to-interval** to use in your environment.  See [Server-Level Variables](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables). |
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
| Scheduled Dashboard Reports to SFTP | The ability to deliver scheduled dashboard reports to an SFTP file location is now disabled by default. [To enable](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables) this option in your environment, contact Technical Support. |
| Dates in Bar Charts | Corrected an issue that displayed incorrect range dates for weeks as displayed in some bar chart visuals. |
| Importing Sources | Updated the workflows used to import sources to process imports more efficiently, preventing timeouts. |
| Exclude/NOTIN | Corrected an issue that incorrectly excluded records with NULL values instead of only excluding specified values. |
| Spark SQL Connector | Upgrading to this release corrects a driver issue related to connecting to a Databricks source. |
| **25.2.1 Resolved Issues** | |
| Scheduled Dashboard Reports | Corrected a browser issue that prevented scheduled dashboard reports (XLXS and PDF) from being generated due to memory leak under heavy load. |
| Upgraded External Library Files | We’ve upgraded `org.springframework:spring-webmv` from 5.3.26 to 5.3.39 in response to customer requests. |
| **25.2 Resolved Issues** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **25.1.11 Resolved Issues** | |
| Large Data Value Handling in OData | A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.   * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option. * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.   Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests. |
| **25.1.10 Resolved Issues** | |
| Embed Visual Event Trigger | A new setting, `fireOnEveryChange`, is now available for embedded dashboards. Disabled by default, enabling this makes it easier for you to track and respond to all user interactions within a dashboard.  When enabled, dashboards send out change events (`dashboard-level`/`visual-level updates`) every time something is modified: sorting, filtering, visual settings, and more. This gives you more granular visibility into user actions.  When disabled, events were are only triggered once for `dashboard-level`/`visual-level changes`.  Enable in the embed SDK configuration. See [Embedded Events](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701070829709-Embedded-Events). |
| Consul Updates | Consol has been upgraded to version 1.22.1. |
| **25.1.9 Resolved Issues** | |
| Time Bar Settings | You can now enable an time bar option in your environment that allows the time bar slider to snap to the closest interval of the defined granularity for a specific source. This is disabled by default: enable the new server-level variable, **timebar-snap-to-interval** to use in your environment.  See [Server-Level Variables](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables). |
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

[Return to top](#top "return to top")

[Return to top](#top "return to top")

### Composer v24

| Title | Description |
| --- | --- |
| **24.4.15 Resolved Issues** | |
| Dashboard & Visual Loading | Corrected an issue in Windows environments where the Edit Dashboard page returned an error when you refreshed or duplicated the browser tab. The dashboard editor now correctly persists its state across page refreshes and duplicate tabs. |
| Authentication Methods | Expanded the documentation provided with the Composer API to include more information about `basicAuth` and `trustedAccessAuth`. |
| Time Zone Display | Fixed an issue where the Time Bar's From and To values could display mismatched time zones in visuals. |
| **24.4.14 Resolved Issues** | |
| Consul Updates | Consol has been upgraded to version 1.22.1. |
| **24.4.13 Resolved Issues** | |
| US Region Maps | Corrected an issue that prevented display of a US Region Map visual to which a new data column had been added. |
| **24.4.12 Resolved Issues** | |
| Updates | This service pack includes various internal fixes. |
| **24.4.11 Resolved Issues** | |
| Time Bar | By default, the Time Bar will display time information as presented in the associated data source with no offsets or bounds to the time field. If you are using UTC, this is indicated in the time bar. If the time is derived based on other settings, this is indicated in the time bar. |
| Source Selection - Creating Visuals | Corrected an issue that prevented display of source names during visual creation. |
| API Update | Corrected an issue that did not return multiple data type options for aggregation functions such as `LAST_VALUE` from `api/sources/<sourceid>/expression-syntax`. |
| **24.4.10 Resolved Issues** | |
| Dashboard Sharing - Tenants | Corrected an issue in multi-tenant environments that prevented users from sharing dashboards with groups they are not members of. |
| **24.4.9 Resolved Issues** | |
| Dates in Bar Charts | Corrected an issue that displayed incorrect range dates for weeks as displayed in some bar chart visuals. |
| Importing Sources | Updated the workflows used to import sources to process imports more efficiently, preventing timeouts. |
| Exclude/NOTIN | Corrected an issue that incorrectly excluded records with NULL values instead of only excluding specified values. |
| Spark SQL Connector | Upgrading to this release corrects a driver issue related to connecting to a Databricks source. |
| **24.4.8 Resolved Issues** | |
| Scheduled Dashboard Reports | Corrected a browser issue that prevented scheduled dashboard reports (XLXS and PDF) from being generated due to memory leak under heavy load. |
| Cross-Source Linking | When you import dashboards and visuals into your instance, all cross-source links are now appropriately imported and linked. |
| Table Visuals | Corrected an issue that prevented creation of a table visual from some columns of a source. |
| **24.4.7 Resolved Issues** | |
| Scheduled Dashboard Reports | Corrected a browser driver issue that prevented scheduled dashboard reports from being generated due to memory leak under heavy load. |
| SQL Editor | Fixed a user interface layout responsiveness issue, ensuring smooth functionality without affecting other components. |
| Filter Snippets | Corrected an issue that prevented the use of some filter snippets that filter hierarchical data. |
| **24.4.6 Resolved Issues** | |
| Embed Updates | Updated the embed bundle to address various deployment issues. |
| Deployment Updates | The deployment package has been updated to remove MD5 references to allow for greater flexibility of deployment options in your environment. |
| **24.4.5 Resolved Issues** | |
| Embedded Components | Corrected an issue that returned an error when using a customized inventory table in an embedded environment. |
| User Interface | In this service pack, we have upgraded the AG Grid version used for the user interface. While this may cause some alignment issues on certain content library pages, the functionality remains unaffected. These issues will be resolved in an upcoming service pack. |
| Embedded Dashboards | Resolved an issue that previously restricted the full visibility of accessing the contextual menus located at the bottom of the embedded dashboards. |
| **24.4.4 Resolved Issues** | |
| Converting Custom SQL to Stored Procedure | When you convert custom SQL statements in a data to a stored procedure for visuals that also rely on custom metrics, Composer appropriately updates the underlying connector capabilities to support AGGREGATION, FILTERING, JOINING, PAGING\_AND\_SORTING, and PROJECTION. |
| First and Last Weeks of the Year | Data used in environments that use Australian time zones now appropriately reflect the correct weeks as the last and first weeks of the year. |
| Bar Charts | Changing the time zone on a user’s device no longer affects the appearance and behavior of date values used in some bar chart granularities. |
| **24.4.3 Resolved Issues** | |
| Time Ranges | Corrected an issue that caused the time bars to display and render an incorrect start year for bar charts that used year ranges and granularity set to week.. |
| Time Bar | Corrected an issue in the time bar that used and displayed UTC time in place of the configured time zone. |
| User Interface | Corrected an issue that included disabled features in the user interface. |
| Fields Visibility | Corrected an issue that caused hidden fields to display in the user interface when users create tables from a source that includes hidden fields. |
| **24.4.2 Resolved Issues** | |
| Embedded Dashboards | Corrected an issue that prevented selected dashboards from displaying properly in embedded environments. |
| Dashboard Error Messages | Corrected an issue that caused an error message to be returned when loading some dashboards that contained no errors. |
| **24.4.1 Resolved Issues** | |
| None. |  |
| **24.4 Resolved Issues** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **24.3.11 Resolved Issues** | |
| Dashboard Sharing - Tenants | Corrected an issue in multi-tenant environments that prevented users from sharing dashboards with groups they are not members of. |
| **24.3.10 Resolved Issues** | |
| Dates in Bar Charts | Corrected an issue that displayed incorrect range dates for weeks as displayed in some bar chart visuals. |
| Importing Sources | Updated the workflows used to import sources to process imports more efficiently, preventing timeouts. |
| Exclude/NOTIN | Corrected an issue that incorrectly excluded records with NULL values instead of only excluding specified values. |
| Spark SQL Connector | Upgrading to this release corrects a driver issue related to connecting to a Databricks source. |
| **24.3.9 Resolved Issues** | |
| Scheduled Dashboard Reports | Corrected a browser issue that prevented scheduled dashboard reports (XLXS and PDF) from being generated due to memory leak under heavy load. |
| Cross-Source Linking | When you import dashboards and visuals into your instance, all cross-source links are now appropriately imported and linked. |
| Table Visuals | Corrected an issue that prevented creation of a table visual from some columns of a source. |
| **24.3.8 Resolved Issues** | |
| Scheduled Dashboard Reports | Corrected a browser driver issue that prevented scheduled dashboard reports from being generated due to memory leak under heavy load. |
| SQL Editor | Fixed a user interface layout responsiveness issue, ensuring smooth functionality without affecting other components. |
| Filter Snippets | Corrected an issue that prevented the use of some filter snippets that filter hierarchical data. |
| **24.3.7 Resolved Issues** | |
| None. |  |
| **24.3.6 Resolved Issues** | |
| Converting Custom SQL to Stored Procedure | When you convert custom SQL statements in a data to a stored procedure for visuals that also rely on custom metrics, Composer appropriately updates the underlying connector capabilities to support AGGREGATION, FILTERING, JOINING, PAGING\_AND\_SORTING, and PROJECTION. |
| First and Last Weeks of the Year | Data used in environments that use Australian time zones now appropriately reflect the correct weeks as the last and first weeks of the year. |
| Bar Charts | Changing the time zone on a user’s device no longer affects the appearance and behavior of date values used in some bar chart granularities. |
| **24.3.5 Resolved Issues** | |
| Time Ranges | Corrected an issue that caused the time bars to display and render an incorrect start year for bar charts that used year ranges and granularity set to week.. |
| Time Bar | Corrected an issue in the time bar that used and displayed UTC time in place of the configured time zone. |
| **24.3.4 Resolved Issues** | |
| Embedded Dashboards | Corrected an issue that prevented selected dashboards from displaying properly in embedded environments. |
| Dashboard Error Messages | Corrected an issue that caused an error message to be returned when loading some dashboards that contained no errors. |
| **24.3.3 Resolved Issues** | |
| None. |  |
| **24.3.2 Resolved Issues** | |
| Line Trend: Attributes Visual Update | When you create a line trend visual that includes the option to include blank data, data with no value is displayed along with data that includes values. |
| **24.3.1 Resolved Issues** | |
| Content Security | Added the value `http.response.header.content-security-policy` to `zoomdata.properties`. Use to add appropriate content security values to support your implementation. See zoomdata.properties Properties. |
| **24.3 Resolved Issues** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **24.2.12 Resolved Issues** | |
| Scheduled Dashboard Reports | Corrected a browser issue that prevented scheduled dashboard reports (XLXS and PDF) from being generated due to memory leak under heavy load. |
| Cross-Source Linking | When you import dashboards and visuals into your instance, all cross-source links are now appropriately imported and linked. |
| **24.2.11 Resolved Issues** | |
| Scheduled Dashboard Reports | Corrected a browser driver issue that prevented scheduled dashboard reports from being generated due to memory leak under heavy load. |
| Filter Snippets | Corrected an issue that prevented the use of some filter snippets that filter hierarchical data. |
| **24.2.10 Resolved Issues** | |
| None. |  |
| **24.2.9 Resolved Issues** | |
| Converting Custom SQL to Stored Procedure | When you convert custom SQL statements in a data to a stored procedure for visuals that also rely on custom metrics, Composer appropriately updates the underlying connector capabilities to support AGGREGATION, FILTERING, JOINING, PAGING\_AND\_SORTING, and PROJECTION. |
| First and Last Weeks of the Year | Data used in environments that use Australian time zones now appropriately reflect the correct weeks as the last and first weeks of the year. |
| Bar Charts | Changing the time zone on a user’s device no longer affects the appearance and behavior of date values used in some bar chart granularities. |
| **24.2.8 Resolved Issues** | |
| Time Ranges | Corrected an issue that caused the time bars to display and render an incorrect start year for bar charts that used year ranges and granularity set to week. |
| Time Bar | Corrected an issue in the time bar that used and displayed UTC time in place of the configured time zone. |
| **24.2.7 Resolved Issues** | |
| Embedded Dashboards | Corrected an issue that prevented selected dashboards from displaying properly in embedded environments. |
| **24.2.6 Resolved Issues** | |
| None. |  |
| **24.2.5 Resolved Issues** | |
| Line Trend: Attributes Visual Update | When you create a line trend visual that includes the option to include blank data, data with no value is displayed along with data that includes values. |
| **24.2.4 Resolved Issues** | |
| Content Security | Added the value `http.response.header.content-security-policy` to `zoomdata.properties`. Use to add appropriate content security values to support your implementation. See zoomdata.properties Properties. |
| **24.2.3 Resolved Issues** | |
| Derived Fields | Corrected an issue that prevented attributes from being converted from text to time (creating a derived field) within a fused data source. |
| **24.2.2 Resolved Issues** | |
| Scheduled Reports | Corrected an issue that prevented simultaneous scheduled report generation in a multi-tenant environment. |
| **24.2.1 Resolved Issues** | |
| None. |  |
| **24.2 Resolved Issues** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **24.1.12 Resolved Issues** | |
| Converting Custom SQL to Stored Procedure | When you convert custom SQL statements in a data to a stored procedure for visuals that also rely on custom metrics, Composer appropriately updates the underlying connector capabilities to support AGGREGATION, FILTERING, JOINING, PAGING\_AND\_SORTING, and PROJECTION. |
| First and Last Weeks of the Year | Data used in environments that use Australian time zones now appropriately reflect the correct weeks as the last and first weeks of the year. |
| Bar Charts | Changing the time zone on a user’s device no longer affects the appearance and behavior of date values used in some bar chart granularities. |
| **24.1.11 Resolved Issues** | |
| Time Ranges | Corrected an issue that caused the time bars to display and render an incorrect start year for bar charts that used year ranges and granularity set to week. |
| Time Bar | Corrected an issue in the time bar that used and displayed UTC time in place of the configured time zone. |
| **24.1.10 Resolved Issues** | |
| Embedded Dashboards | Corrected an issue that prevented selected dashboards from displaying properly in embedded environments. |
| **24.1.9 Resolved Issues** | |
| None. |  |
| **24.1.8 Resolved Issues** | |
| Line Trend: Attributes Visual Update | When you create a line trend visual that includes the option to include blank data, data with no value is displayed along with data that includes values. |
| **24.1.7 Resolved Issues** | |
| Content Security | Added the value `http.response.header.content-security-policy` to `zoomdata.properties`. Use to add appropriate content security values to support your implementation. See zoomdata.properties Properties. |
| **24.1.6 Resolved Issues** | |
| Derived Fields | Corrected an issue that prevented attributes from being converted from text to time (creating a derived field) within a fused data source. |
| **24.1.5 Resolved Issues** | |
| Scheduled Reports | Corrected an issue that prevented simultaneous scheduled report generation in a multi-tenant environment. |
| **24.1.4 Resolved Issues** | |
| None. |  |
| **24.1.3 Resolved Issues** | |
| SAML SSO Integration | Corrected an issue that prevented use of Okta IdP to authenticate through SAML SSO. |
| Null Values | Resolved an issue with sources containing null values that prevented use in visuals and dashboards. |
| World Maps Filtering | You can now apply filters to the World Maps visual using the context menu. |
| **24.1.2 Resolved Issues** | |
| List Filter Selections | When you select multiple values in a list filter, Composer includes a scrollbar to allow you to scroll among your selections as needed. |
| **24.1.1 Resolved Issues** | |
| Ruler Log Scale Function | Corrected an issue that returned incorrect results from the log scale function if negative values or zero values were included. |
| Exporting Raw Data | Corrected an issue that prevented the export of visual data in visuals where the option Show Distinct Rows is used. |
| **24.1 Resolved Issues** | |
| None. |  |

[Return to top](#top "return to top")

### Composer v23

| Title | Description |
| --- | --- |
| **23.4.13 Resolved Issues** | |
| Line Trend: Attributes Visual Update | When you create a line trend visual that includes the option to include blank data, data with no value is displayed along with data that includes values. |
| **23.4.12 Resolved Issues** | |
| Content Security | Added the value `http.response.header.content-security-policy` to `zoomdata.properties`. Use to add appropriate content security values to support your implementation. . |
| **23.4.11 Resolved Issues** | |
| Derived Fields | Corrected an issue that prevented attributes from being converted from text to time (creating a derived field) within a fused data source. |
| **23.4.10 Resolved Issues** | |
| Scheduled Reports | Corrected an issue that prevented simultaneous scheduled report generation in a multi-tenant environment. |
| **23.4.9 Resolved Issues** | |
| SAML SSO Integration | Corrected an issue that prevented use of Okta IdP to authenticate through SAML SSO. |
| Null Values | Resolved an issue with sources containing null values that prevented use in visuals and dashboards. |
| **23.4.8 Resolved Issues** | |
| List Filter Selections | When you select multiple values in a list filter, Composer includes a scrollbar to allow you to scroll among your selections as needed. |
| **23.4.7 Resolved Issues** | |
| Exporting Raw Data | Corrected an issue that prevented the export of visual data in visuals where the option Show Distinct Rows is used. |
| **23.4.6 Resolved Issues** | |
| Ruler Log Scale Function | Corrected an issue that returned incorrect results from the log scale function if negative values or zero values were included. |
| **23.4.5 Resolved Issues** | |
| Filter Snippets | Corrected a display issue that prevented full access to filter lists for filter snippets. |
| Visual Data Export | Corrected an issue that prevented Composer from exporting the default number of rows. If you need to export more than 100,000 rows, adjust the property `zoomdata.export.visualdata.max.rows` in the zoomdata.properties Properties. |
| **23.4.4 Resolved Issues** | |
| Custom Attributes | Corrected an issue that returned an error when creating user accounts as members of the Administrators Group and incorporating encrypted custom attributes with special characters. |
| Color Palettes for Visuals | KPI visuals now utilize the selected custom color palettes when **Inherit from theme** is disabled. |
| **23.4.3 Resolved Issues** | |
| None. |  |
| **23.4.2 Resolved Issues** | |
| None. |  |
| **23.4.1 Resolved Issues** | |
| Raw Data Export | Composer exports raw data for hierarchical fields only when the raw data capability is enabled. |
| Source Deletion | Corrected an issue that prevented sources from being deleted after updates as part of an insertion strategy. |
| **23.4 Resolved Issues** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **23.3.14 Resolved Issues** | |
| Derived Fields | Corrected an issue that prevented attributes from being converted from text to time (creating a derived field) within a fused data source. |
| **23.3.13 Resolved Issues** | |
| Scheduled Reports | Corrected an issue that prevented simultaneous scheduled report generation in a multi-tenant environment. |
| **23.3.12 Resolved Issues** | |
| SAML SSO Integration | Corrected an issue that prevented use of Okta IdP to authenticate through SAML SSO. |
| **23.3.11 Resolved Issues** | |
| List Filter Selections | When you select multiple values in a list filter, Composer includes a scrollbar to allow you to scroll among your selections as needed. |
| **23.3.10 Resolved Issues** | |
| Exporting Raw Data | Corrected an issue that prevented the export of visual data in visuals where the option Show Distinct Rows is used. |
| **23.3.9 Resolved Issues** | |
| Filter Snippets | Corrected a display issue that prevented full access to filter lists for filter snippets. |
| Visual Data Export | Corrected an issue that prevented Composer from exporting the default number of rows. If you need to export more than 100,000 rows, adjust the property `zoomdata.export.visualdata.max.rows` in zoomdata.properties Properties. |
| **23.3.8 Resolved Issues** | |
| Custom Attributes | Corrected an issue that returned an error when creating user accounts as members of the Administrators Group and incorporating encrypted custom attributes with special characters. |
| Color Palettes for Visuals | KPI visuals now utilize the selected custom color palettes when s is disabled. |
| Embedded Source Editor | Corrected an issue that prevented return of an updated source editor in an embedded environment when updating embedded components shared to your application. |
| **23.3.7 Resolved Issues** | |
| None. |  |
| **23.3.6 Resolved Issues** | |
| Scheduled Reports in Excel Format | Corrected an issue that prevented scheduled reports from being sent to external users when custom attributes are used in the data source connection for the report. |
| **23.3.5 Resolved Issues** | |
| Source Deletion | Corrected an issue that prevented deletion of a source with in-dashboard visuals not attached to any dashboard in the system. |
| ElasticSearch | Corrected an issue with connecting to ElasticSearch 8.3. |
| **23.3.4 Resolved Issues** | |
| None. |  |
| **23.3.3 Resolved Issues** | |
| Elasticsearch 8 connector with High Level Rest Client v7.17 | Updated the Elasticsearch 8 connector to support data sources created with High Level Rest Client v7.17 in compatibility mode. |
| **23.3.2 Resolved Issues** | |
| Hierarchy Fields | Corrected an issue with visuals within a dashboard that fail to load when using some hierarchy fields that contain numerous duplicate nodes. |
| Upgraded External Libraries Package Versions | We have upgraded external libraries to later versions in response to customer requests:   * com.google.protobuf:protobuf-java upgraded from version 3.21.1 to 3.21.7 * org.thymeleaf:thymeleaf from 3.0.15 to 3.1.2 * net.minidev:json-smart from 2.4.8 to 2.4.9 * org.apache.velocity:velocity-engine-core from 2.0 to 2.3 * org.springframework.boot:spring-boot-autoconfigure from 2.7.2 to 2.7.12 * org.springframework:spring-webmv from 5.3.23 to 5.3.26 * org.springframework.boot:spring-boot-actuator-autoconfigure from 2.7.4 to 2.7.11 * org.springframework.hateoas:spring-hateoas from 1.5.2 to 1.5.5 * xalan:xalan from 2.7.2 to 2.7.3 |
| **23.3.1 Resolved Issues** | |
| None. |  |
| **23.3 Resolved Issues** | |
| Fields with Dynamic Override of Filter Values | Corrected an issue that presented cached filter values when Filter Value entities contained User Attributes. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **23.2.15 Resolved Issues** | |
| SAML SSO Integration | Corrected an issue that prevented use of Okta IdP to authenticate through SAML SSO. |
| **23.2.14 Resolved Issues** | |
| Visual Data Export | Corrected an issue that prevented Composer from exporting the default number of rows. If you need to export more than 100,000 rows, adjust the property `zoomdata.export.visualdata.max.rows` in zoomdata.properties Properties. |
| **23.2.13 Resolved Issues** | |
| None. |  |
| **23.2.12 Resolved Issues** | |
| Scheduled Reports in Excel Format | Corrected an issue that prevented scheduled reports from being sent to external users when custom attributes are used in the data source connection for the report. |
| **23.2.11 Resolved Issues** | |
| ElasticSearch | Corrected an issue with connecting to ElasticSearch 8.3. |
| **23.2.10 Resolved Issues** | |
| Elasticsearch 8 connector with High Level Rest Client v7.17 | Updated the Elasticsearch 8 connector to support data sources created with High Level Rest Client v7.17 in compatibility mode. |
| **23.2.9 Resolved Issues** | |
| Hierarchy Fields | Corrected an issue with visuals within a dashboard that fail to load when using some hierarchy fields that contain numerous duplicate nodes. |
| **23.2.8 Resolved Issues** | |
| None. |  |
| **23.2.7 Resolved Issues** | |
| None. |  |
| **23.2.6 Resolved Issues** | |
| None. |  |
| **23.2.5 Resolved Issues** | |
| API Dashboard Creation | We enhanced validation on the dashboard creation endpoint `/api/dashboards` to prevent dashboard creation with empty or invalid `content`. |
| **23.2.4 Resolved Issues** | |
| Deleting Users and Accounts | Corrected an issue where user and account deletions failed if associated with existing Rich Text snippets and Filter Snippets. |
| **23.2.3 Resolved Issues** | |
| Table Visual Exports | Corrected an issue that populated unnecessary data into CSV and XLSX exports of Table visuals when Conditional Formatting is applied to the table. |
| Tool Tips | Tooltips for visuals now display correctly in the Microsoft Edge browser. |
| **23.2.2 Resolved Issues** | |
| None. |  |
| **23.2.1 Resolved Issues** | |
| OData API | Corrected an issue where the OData API endpoint may not have returned data if a unique key was not defined. |
| Dashboards | Fixed minor dashboard tooltips and filters issues. |
| **23.2 Resolved Issues** | |
| Define Time Zones in Log Files for Microservices | Corrected an issue with timezone conversion in log files for Composer microservices.  The new property, `log.timestamp.pattern`, allows you to change the format of a log row timestamp and specify its timezone: `%date{"yyyy-MM-dd HH:mm:ss,SSS", UTC}`. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **23.1.14 Resolved Issues** | |
| ElasticSearch | Corrected an issue with connecting to ElasticSearch 8.3. |
| **23.1.13 Resolved Issues** | |
| Elasticsearch 8 connector with High Level Rest Client v7.17 | Updated the Elasticsearch 8 connector to support data sources created with High Level Rest Client v7.17 in compatibility mode. |
| **23.1.12 Resolved Issues** | |
| None. |  |
| **23.1.11 Resolved Issues** | |
| None. |  |
| **23.1.10 Resolved Issues** | |
| Table Visual Exports | Corrected an issue that populated unnecessary data into CSV and XLSX exports of Table visuals when Conditional Formatting is applied to the table. |
| Deleting Users and Accounts | Corrected an issue where user and account deletions failed if associated with existing Rich Text snippets and Filter Snippets. |
| **23.1.9 Resolved Issues** | |
| Alerts Icon | The alerts icon is no longer present in dashboards for users who do not have the Create Alerts or Administer Alerts privileges. |
| Cell Wrapping | Reprioritized the word wrapping functions to wrap cell text between words before splitting words when adjusting column widths. |
| **23.1.8 Resolved Issues** | |
| Tooltips | Corrected an issue that prevented some tooltips from displaying field names along with values. |
| **23.1.7 Resolved Issues** | |
| Conditional Formatting | Corrected an issue that applied background colors to cells that did not meet conditional formatting rules. |
| **23.1.6 Resolved Issues** | |
| None. |  |
| **23.1.5 Resolved Issues** | |
| Derived Fields Expressions Support | Improved support for escaped characters in string literals in derived field expressions. Characters such as `"\"` and `"'"` can now be used in expressions when prefixed by a `"\"` character. |
| Embedded Dashboards | Corrected an issue that prevented turning off creating snippets functionality in embed dashboard builder. |
| **23.1.4 Resolved Issues** | |
| OData API | Fixed a potential source name duplication issue that may affect the OData API. |
| BigQuery | Fixed BigQuery connectivity issues related to accessing different AWS regions. |
| **23.1.3 Resolved Issues** | |
| List Filter Visuals | Corrected an issue that prevented List Filter visuals from loading data after a WebSocket timeout. |
| **23.1.2 Resolved Issues** | |
| Dashboard and Widget Focus | Composer now returns focus to the previously maximized widget when it is again minimized in a dashboard. |
| Widget Size Minimum | The minimum height for a widget presented in the responsive dashboard layout is now 50 pixels. |
| **23.1.1 Resolved Issues** | |
| Fusion Source Filters | We’ve improved the push down for complex filters on fused sources that contain data entities from different connections. |
| **23.1 Resolved Issues** | |
| Visual Switching | Resolved an issue that prevented Composer from releasing unused memory when changing from one type of visual to another. |
| Health Status for Query Engine | Corrected an issue that incorrectly reported the Query Engine service status as **Critical** instead of **Warning** when Composer cannot open a connection to the internal database. |
| Derived Field Editor Update | When you create a derived field with a function that supports only specific values in a parameter and do not include a supported value, Composer now displays an error message that lists supported values. |
| Scroll Bars on Pivot Tables | Composer now correctly renders and displays horizontal scroll bars for Pivot Tables that include data wide enough to require scroll bars when the cells are maximized. |
| Table Visual Data | Composer now correctly displays the all of the grouped data values, independent of the Infinite scroll or Pagination settings. |
| Fusion Source Filters | We’ve improved the push down for complex filters on fused sources that contain data entities from different connections. |

[Return to top](#top "return to top")

### Composer v22

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **22.4.14 Resolved Issues** | |
| None. |  |
| **22.4.13 Resolved Issues** | |
| None. |  |
| **22.4.12 Resolved Issues** | |
| Recipient Rules API - Custom User Attributes | The Recipient Rules API (`user segregation` endpoints in Composer) now allows use of custom user attributes that include the "-" character. |
| **22.4.11 Resolved Issues** | |
| None. |  |
| **22.4.10 Resolved Issues** | |
| Derived Fields Expressions Support | Improved support for escaped characters in string literals in derived field expressions. Characters such as `"\"` and `"'"` can now be used in expressions when prefixed by a `"\"` character. |
| **22.4.9 Resolved Issues** | |
| List Filter Visuals | Corrected an issue that prevented List Filter visuals from loading data after a WebSocket timeout. |
| **22.4.8 Resolved Issues** | |
| Dashboard and Widget Focus | Composer now returns focus to the previously maximized widget when it is again minimized in a dashboard. |
| **22.4.7 Resolved Issues** | |
| Fusion Source Filters | We’ve improved the push down for complex filters on fused sources that contain data entities from different connections. |
| **22.4.6 Resolved Issues** | |
| Table Visual Data | Composer now correctly displays the all of the grouped data values, independent of the Infinite scroll or Pagination settings. |
| Scroll Bars on Pivot Tables | Composer now correctly renders and displays horizontal scroll bars for Pivot Tables that include data wide enough to require scroll bars when the cells are maximized. |
| **22.4.5 Resolved Issues** | |
| Legends and Visual Legends | Corrected an issue where some color codes in legends and visual legends did not refresh properly after a change was made to the visual. |
| **22.4.4 Resolved Issues** | |
| Derived Field Editor Update | When you create a derived field with a function that supports only specific values in a parameter and do not include a supported value, Composer now displays an error message that lists supported values. |
| **22.4.3 Resolved Issues** | |
| Health Status for Query Engine | Corrected an issue that incorrectly reported the Query Engine service status as **Critical** instead of **Warning** when can’t open a connection to the internal database. |
| **22.4.2 Resolved Issues** | |
| Field Sort Order Updates | After upgrading to this version of Composer, any visuals you create displays fields in the order they are retrieved from the source. If you create a source using custom SQL, your field data is shown in the order you specify.  On upgrade, the order of fields for existing visuals are not changed from the previous default sort, alphabetical.  If you create a source using the API, you can send a list of native fields or the entire list of fields in a sort order that meets your needs.  If you add a single field using the API or on the fields tab, it is added to the end of the fields list. |
| **22.4.1 Resolved Issues** | |
| Dashboard Export/Import | Updated the dashboard export and import APIs to include source cache settings for the data and statistics caches in the payload. |
| **22.4 Resolved Issues** | |
| Visual Attributes | Corrected an error that prevented some horizontal (x-axis) attributes and vertical (y-axis) attributes from updating when you change a visual’s type and save it. |
| Line Trend Visual | Corrected an error that cut off X-axis labels. |
| Account Switching | Switching between user accounts no longer returns a undefined error message. |
| Pivot Tables | Composer now correctly displays scroll bars for pivot tables that are larger than the viewable area of the visual. |
| Pivot Tables | Composer no longer exports extraneous Volume metrics for pivot tables. |

[Return to top](#top "return to top")

### Composer v8.4 and Earlier

| Title | Description |
| --- | --- |
| **8.4.1 Resolved Issues** | |
| Source Updates | Corrected an issue with updating sources that improves the performance of Composer. |
| **8.4 Resolved Issues** | |
| Export Pivot Table Data | Corrected an issue that prevented the export of data to CSV format for pivot tables that include a numeric group column with high-precision numbers. |
| Dashboard Links | Corrected an issue that prevented dashboard to dashboard links from transferring a filter if the group label included an ampersand (**&**). |
| Update Visual Types | Composer no longer returns an error when you change the visual type of a saved visual, then navigate between tabs, then attempt to reload the visual. |
| Complex Custom Metrics | Corrected an issue that may prevent visuals that use custom metrics with a `PreviousPeriod` function from loading. |
| Linking Time Fields | Corrected an issue that prevented you from selecting a second source in a timebar with linked time fields. |
| Visual Labels | Corrected an issue that prevented some value labels for pie chart and donut chart visuals from displaying completely. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **8.3 Resolved Issues** | |
| Copying Visuals | Creating a copy of a list filter visual that includes a Display Value no longer returns an error for the new visual. |
| Linked Time Fields | Corrected an issue that prevented you from adjusting linked time fields from multiple sources in the timebar. |
| Data Details Table | Corrected an issue that prevented inclusion of the Timebar filter for some Data Details tables. |
| Visual Loading | Corrected an issue that prevented the visual loading progress information from displaying correctly. |
| Hive and Other Data Filtering | Composer now correctly filters Hive data that includes commas.  Interpolation in Composer also supports escape characters inside of the variable placeholder, `${User.var}`. These characters include `\` (backslash), `|` (pipe), and `}` (right curly bracket). |
| Heat Maps | Composer now correctly displays numerical data in ascending or descending order in heat mapping visuals. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **8.2 Resolved Issues** | |
| User Account Maintenance Updates | Supervisor users can now delete Composer user accounts that have file uploads associated with the user account. Ownership of the file uploads is transferred to the Supervisor user. |
| Row Level Expressions | Composer now correctly displays the list of row level expressions in use in the calculation editor after you have added an admin defined function. |
| Visual Display Issues | Composer now correctly displays visuals in a Dashboard after you have viewed the Data Details for a visual. |
| Fonts for Visuals | Composer now applies font customization styling to all labels associated with a customized visual. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **8.1 Resolved Issues** | |
| Embedding Multiple Dashboards | Improvements were made to the loading and rendering of pages that include multiple dashboards in Composer to speed up load time and improve performance. |
| Visual Data Export (CSV) | Composer no longer exports extraneous visual data for visuals that use sub-group styles and sorting by metrics. |
| Visual Sidebar Menu Update | The **Apply** button on a number of secondary sidebar menu panels is now a **Continue** button. Make your changes, select **Continue**, and make any final adjustments before selecting **Apply** to apply your changes. |
| Time Presets Support | Several of Composer’s time presets have been updated to provide more consistent time range information. |
| Unsaved Changes Updates | When you navigate away from a dashboard that only has changes to cross-visual filters, Composer no longer displays an **Unsaved Changes?** dialog. |
| Cross-Source Link Updates | Composer now displays your lists of cross-source links in alphabetical order by field name when you open your list of Cross-Source Links for a saved dashboard. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **8.0 Resolved Issues** | |
| Heat Map Visual Color Mode | When you switch between adjusting the colors for a heat map visual manually and using Gradient options, Composer now correctly applies manual color thresholds when undoing the Auto Color Metric change. |
| Visualization Loading in Embedded Mode | Composer now loads grouped and individual visuals appropriately when embedded dashboards are opened in environments when environment or network performance is degraded. |

[Return to top](#top "return to top")

### Composer v7.10 and Earlier

| Title | Description |
| --- | --- |
| **7.10.23 Resolved Issues** | |
| Security | Improved security in enterprise data connectors. |
| **7.10.22 Resolved Issues** | |
| Derived Fields Expressions Support | Improved support for escaped characters in string literals in derived field expressions. Characters such as `"\"` and `"'"` can now be used in expressions when prefixed by a `"\"` character. |
| **7.10.21 Resolved Issues** | |
| Scroll Bars on Pivot Tables | Composer now correctly renders and displays horizontal scroll bars for Pivot Tables that include data wide enough to require scroll bars when the cells are maximized. |
| **7.10.20 Resolved Issues** | |
| Legends and Visual Legends | Corrected an issue where some color codes in legends and visual legends did not refresh properly after a change was made to the visual. |
| **7.10.19 Resolved Issues** | |
| None. |  |
| **7.10.18 Resolved Issues** | |
| Visual Fields Caching | Composer correctly displays available visual types when source fields needed to build a specific visual type have been updated. |
| **7.10.17 Resolved Issues** | |
| Custom SQL Queries | Composer no longer displays an Unexpected Exception error message when you update the custom SQL for a data source. |
| KPI Visuals | Corrected an issue that prevented some users of an newly created embedded KPI visual from adding a derived field or custom metric from the Y-axis. |
| **7.10.16 Resolved Issues** | |
| Timebar Display | Resolved an issue that prevented the timebar from loading correctly on the dashboards when focusing on visuals. |
| Dashboard Export/Import | Updated the dashboard export and import APIs to include source cache settings for the data and statistics caches in the payload. |
| **7.10.15 Resolved Issues** | |
| Pivot Tables | Composer no longer exports extraneous Volume metrics for pivot tables. |
| CSV File Uploads | Composer no longer includes unsuccessful CSV files in the data source creation workflow. |
| **7.10.14 Resolved Issues** | |
| Refresh All Fields | When you manually **Refresh All Fields** on the Cache tab, Composer now refreshes all fields regardless of the Schedule Refresh setting for each field. |
| Custom SQL Queries | Composer no longer returns an error when you add a new CASE clause to a successfully run custom SQL query for an existing data source. |
| Visual Attributes | Corrected an error that prevented some horizontal (x-axis) attributes and vertical (y-axis) attributes from updating when you change a visual’s type and save it. |
| Source Updates | Corrected an issue with updating sources that improves the performance of Composer. |
| Pivot Tables | Composer now correctly displays and allows drag & drop horizontal scroll bars for pivot tables. |
| **7.10.13 Resolved Issues** | |
| Visual Labels | Corrected an issue that prevented some value labels for pie chart and donut chart visuals from displaying completely. |
| Linking Time Fields | Corrected an issue that prevented you from selecting a second source in a timebar with linked time fields. |
| **7.10.12 Resolved Issues** | |
| Export Pivot Table Data | Corrected an issue that prevented the export of data to CSV format for pivot tables that include a numeric group column with high-precision numbers. |
| Complex Custom Metrics | Corrected an issue that may prevent visuals that use custom metrics with a `PreviousPeriod` function from loading. |
| Visual Filtering | Adjusted the placement of list filters to allow you to view the entire visual when you use a list filter. |
| Update Visual Types | Composer no longer returns an error when you change the visual type of a saved visual, then navigate between tabs, then attempt to reload the visual. |
| Dashboard Links | Corrected an issue that prevented dashboard to dashboard links from transferring a filter if the group label included an ampersand (**&**). |
| Composer Events | Corrected an issue that may trigger Composer events before Composer is in a state that is ready to respond to the events. |
| Heat Map Visuals | Corrected an issue that prevented you from setting color thresholds for number values that include decimal places. |
| **7.10.11 Resolved Issues** | |
| Visual Display Updates | Composer now correctly displays X-axis labels for visuals that include data groups with a zero value. |
| Linked Time Fields | Corrected an issue that prevented you from adjusting linked time fields from multiple sources in the timebar. |
| Heat Maps | Composer now correctly displays numerical data in ascending or descending order in heat mapping visuals. |
| Visual Loading | Corrected an issue that prevented the visual loading progress information from displaying correctly. |
| Embedded Connections and Sources | Composer now correctly links to the connections and sources from the home page when embedded in an iframe. |
| Hive and Other Data Filtering | Composer now correctly filters Hive data that includes commas.  Interpolation in Composer also supports escape characters inside of the variable placeholder, `${User.var}`. These characters include `\` (backslash), `|` (pipe), and `}` (right curly bracket). |
| Copying Visuals | Creating a copy of a list filter visual that includes a Display Value no longer returns an error for the new visual. |
| **7.10.10 Resolved Issues** | |
| Display Values | Composer now correctly displays metric labels appropriately in visuals that include negative values. |
| **7.10.9 Resolved Issues** | |
| None. |  |
| **7.10.8 Resolved Issues** | |
| Fonts for Visuals | Composer now applies font customization styling to all labels associated with a customized visual. |
| **7.10.7 Resolved Issues** | |
| Visual Display Issues | Composer now correctly displays visuals in a Dashboard after you have viewed the Data Details for a visual. |
| **7.10.6 Resolved Issues** | |
| Row Level Expressions | Composer now correctly displays the list of row level expressions in use in the calculation editor after you have added an admin defined function. |
| Visual Rendering Updates | When you make changes to an underlying custom metric or derived field, associated visuals are re-rendered to reflect the changed source data. |
| **7.10.5 Resolved Issues** | |
| User Account Maintenance Updates | Supervisor users can now delete Composer user accounts that have file uploads associated with the user account. Ownership of the file uploads is transferred to the Supervisor user. |
| **7.10.4 Resolved Issues** | |
| Visual Data Export (CSV) | Composer no longer exports extraneous visual data for visuals that use sub-group styles and sorting by metrics. |
| Time Presets Support | Several of Composer’s time presets have been updated to provide more consistent time range information. See Preset Time Ranges for more information. |
| Unsaved Changes Updates | When you navigate away from a dashboard that only has changes to cross-visual filters, Composer no longer displays an **Unsaved Changes?** dialog. |
| Cross-Source Link Updates | Composer now displays your lists of cross-source links in alphabetical order by field name when you open your list of Cross-Source Links for a saved dashboard. |
| **7.10.3 Resolved Issues** | |
| Embedding Multiple Dashboards | Improvements were made to the loading and rendering of pages that include multiple dashboards in Composer to speed up load time and improve performance. |
| Visual Sidebar Menu Update | The **Apply** button on a number of secondary sidebar menu panels is now a **Continue** button. Make your changes, select **Continue**, and make any final adjustments before selecting **Apply** to apply your changes. |
| **7.10.2 Resolved Issues** | |
| None. |  |
| **7.10.1 Resolved Issues** | |
| Visualization Loading in Embedded Mode | Composer now loads grouped and individual visuals appropriately when embedded dashboards are opened in environments when environment or network performance is degraded. |
| Heat Map Visual Color Mode | When you switch between adjusting the colors for a heat map visual manually and using Gradient options, Composer now correctly applies manual color thresholds when undoing the Auto Color Metric change. |
| **7.10 Resolved Issues** | |
| Embedded Visuals and Dashboards | Loading and unloading of embedded visuals and dashboards has been adjusted to consume memory more efficiently in Chrome browsers. |
| Pivot Tables Update | The time granularity label (minutes, hours, seconds) has been removed from the row and column group labels of pivot tables. |
| Visual Data Export (CSV) | Composer no longer returns an error when exporting visual data in CSV format for some dashboards that contain pivot tables. |
| Log4j Updates | Even though Composer does not use log4j for any normal workflows, the .jar files were included in a normal installation package for third party use. These .jar files are no longer included in Composer installation packages, to help mitigate any log4j vulnerabilities. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.9 Resolved Issues** | |
| Eval Error for Visuals | Composer no longer returns an error when attempting to display embedded dashboards that include Maps or KPIs for parent applications which use a monaco-editor third-party dependency. |
| Extended Filter Attributes | Composer now correctly displays selectable check box selections in Firefox browsers for extended length filter attribute names. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.8 Resolved Issues** | |
| Time Bar | The time bar and Data Details work area in Composer now display time at the same level of granularity you define for your visual at the source level. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.7 Resolved Issues** | |
| Playback for KPI Charts | Composer no longer returns an error when playback is enabled on a KPI chart with some types of Custom Metrics. |
| Playback and Live Settings | Composer no longer disables the **Enable Playback** and **Enable Live Mode** settings for the Time Bar when adding a custom time range. |
| Min Max Values | Composer now displays the appropriate Min and Max values as tool tips for Histogram visuals. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.6 Resolved Issues** | |
| Modal Popups | Composer now displays field pickers for modal popups appropriate to the picker location. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.5 Resolved Issues** | |
| Table Column Sizing | Composer now retains column sizes for tables and pivot tables when sized during creation or changed after creation. |
| Raw Data Exports From Fusion Sources | You can now use Composer to export raw data in CSV format from Fusion data sources. |
| Bar Charts Ruler Adjustments | Composer now correctly displays minimum and maximum values for bar charts after you have adjusted the Ruler Min value. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.4 Resolved Issues** | |
| CSS Styles for Table Visuals | The CSS styles of embedded Composer table visuals are now independent of CSS styles used by your parent application. |
| Null Values | In the Line Trend: Attributes Visual, Composer now displays groupings with null values. |
| Elasticsearch Source Filters | You can now add Elasticsearch source filters only at the root filters level of a visual. |
| Min/Max Value Calculations | Composer now correctly calculates minimum and maximum values based on row level security filters. |
| Menus for Embedded Visuals | Composer now correctly displays the More menu for visuals embedded using bootstrap@5.0.2. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.3 Resolved Issues** | |
| Dashboard Display | When opening an embedded dashboard, Composer now displays the top of the dashboard instead of scrolling to the last active visual. |
| Fusion Data Scheduled Reports | Composer now properly produces visuals and images for scheduled report PDF files generated using Fusion data. |
| Data Variance | Composer now correctly calculates and returns the results of 1 Mth YoY data to accommodate leap years. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.2 Resolved Issues** | |
| None. |  |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.1 Resolved Issues** | |
| Filters | Aggregations are now pushed down correctly when excluding many values in a filter. |
| Invisible Fields & Data Sources | You can no longer save a data source with an invisible field, if the invisible field is referenced in a visual or used in its filters and keysets. |
| Amazon S3 Connector | Improvements were made to the Amazon S3 error messages and log entries in Composer. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **7.0 Resolved Issues** | |
| Materialized Views | You can now create a materialized view definition when the Volume metric has been renamed. |

[Return to top](#top "return to top")

### Composer v6.9 and Earlier

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
| Fonts for Visuals | Composer now applies font customization styling to all labels associated with a customized visual. |
| PDF Export | Composer now includes uncropped visuals when exporting to a PDF. |
| **6.9.25 Resolved Issues** | |
| Time Presets Support | Several of Composer’s time presets have been updated to provide more consistent time range information. See Preset Time Ranges for more information. |
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
| **6.9.9 Resolved Issues** | |
| Sub-Group Search | Composer now returns consistent results when you search Sub-Groups by Attribute search terms. |
| CSS Styles for Table Visuals | The CSS styles of embedded Composer table visuals are now independent of CSS styles used by your parent application. |
| List Filter Widget | List filter visuals that contain multiple selections from data sources now expand to an appropriate navigable height. |
| Null Values | In the Line Trend: Attributes Visual, Composer now displays groupings with null values. |
| **6.9.8 Resolved Issues** | |
| Multiple Pivot Tables | Composer now displays pivot tables correctly after you have created and edited a dashboard containing multiple pivot tables. |
| Dashboard Display | When opening an embedded dashboard, Composer now displays the top of the dashboard instead of scrolling to the last active visual. |
| Fusion Data Scheduled Reports | Composer now properly produces visuals and images for scheduled report PDF files generated using Fusion data. |
| Data Variance | Composer now correctly calculates and returns the results of 1 Mth YoY data to accommodate leap years. |
| **6.9.7 Resolved Issues** | |
| Hive Datasource | Composer now properly handles invisible fields in the Hive datasource when customers upgrade from Composer 5.9 to 6.9. |
| **6.9.6 Resolved Issues** | |
| Large Dashboard Scheduling | Customers can now schedule and transmit large dashboards without getting a DataBufferLimitException error code. |
| **6.9.5 Resolved Issues** | |
| None. |  |
| **6.9.4 Resolved Issues** | |
| Amazon S3 Connector | Improvements were made to the Amazon S3 error messages and log entries in Composer. |
| Dashboard Links | The **Link** option on the radial menu no longer appears if a user does not have read permission for the dashboard that is linked. |
| **6.9.3 Resolved Issues** | |
| Field Conversion & Data Sources | An error is no longer produced when saving a data source after converting multiple integer fields to numbers. |
| Invisible Fields & Data Sources | You can no longer save a data source with an invisible field, if the invisible field is referenced in a visual (charted or used in filters and keysets). |
| Filters | Aggregations are now pushed down correctly when excluding many values in a filter. |
| Custom Metrics | The help dialog (available in the Function Library section of the Custom Metrics Editor) now appears for a dashboard embedded using Bootstrap version 3.3.7. |
| List Filter Widget | Values now appear on a list filter widget after it is maximized or minimized. |
| **6.9.2 Resolved Issues** | |
| Custom Metric Date and Time Aggregation Function Changes | Custom metrics now support the `now()` and `time_add` functions used by row-level expressions. The original custom metric `DATE()`, `DateADD`, and `DateSUB` functions still work but should no longer be used. They are deprecated in this release and will be removed in a future release. Instead, use the `now()` and `time_add` functions. |
| Dashboard Import Changes | You can now use the API to import a dashboard using a new overwrite policy, so that dashboards with the same name are overwritten instead of being imported with a slightly altered name. |
| Materialized Views | You can now create a materialized view definition when the Volume metric has been renamed. |
| **6.9.1 Resolved Issues** | |
| Dashboard Import | A problem importing dashboards from the same Composer version has been resolved. |
| **6.9 Resolved Issues** | |
| Cross-source Linked Dashboard Visual Filters | Filters now work correctly for dashboard visuals that are cross-source linked when the dashboard is linked by URL from an application. |
| UI errors | The scroll bar no longer disappears when scrolling through a long list of filter values. |
| Axes Colors | The colors of axes lines for visuals are now retained correctly after an upgrade. |
| Custom Charts | Resolved an issue with custom charts that broke with the removal of internal JavaScript libraries that were being used as dependencies. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **6.8 Resolved Issues** | |
| Data Sources | Changes to the Tables/Indices tab of a data source configuration (or the custom SQL specified there) no longer reset the custom labels and settings on the Fields tab of the data source or its global settings. |
| Connections | Connection attributes no longer appear broken when a system override is specified. |
| Calculated Value Appearance | When a dashboard loads, values that take a moment to be calculated are shown as a waiting (loading) using an image of three dots. |
| Dashboard Refreshes | Corrected a problem in which table data was not refreshed when the dashboard refresh button was selected. |
| Histograms | Corrected a problem in which histograms were not retaining their bar interval settings under specific circumstances. |
| Migration | Resolved a problem in which migration failed because the data source had no Volume Metric selected. |
| Embed Code | Composer no longer uses `hammer.js`. |
| Tables | Corrected a problem in which tables were not updated during playback. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **6.7 Resolved Issues** | |
| Visuals | Corrected a problem in which **Undo Changes** did not work for a visual while the visual sidebar was open. |
| Data Sources | Corrected a problem in which visuals were not honoring the Group By global default setting in the data source. |
| Radial Menu | Corrected a problem in which undoing a trend request (Trend option on the radial menu) produced errors. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **6.6 Resolved Issues** | |
| COALESCE Function Changes | The COALESCE function now supports aggregate metrics with complex calculations using arithmetic functions (for example `COALESCE(max(sales) * 1.3, 0)`), so a default value can be used if null values are returned. |
| Pivot Tables | Pivot table performance is improved for a Postgres data source that uses custom SQL. |
| Elasticsearch Connectors | Elasticsearch connectors now provide error messages when a Last Value metric cannot be computed correctly. See Elasticsearch Last Value Processing. |
| Line Trend Visuals | Improved performance of line trend visuals. |
| Performance | Java memory performance on live dashboards is improved. |
| API/SDK | It is no longer possible to create two visuals with the same `controlsCfg` ID using the API. |
| An incorrect call for the `removeEventListener` function is corrected. |
| Importing Dashboards | Resolved a problem in which an attempt to import a dashboard failed when the dashboard included a visual shared with another dashboard that had already been imported. |
| Embedded Dashboards | Dashboards are now embedded successfully when they contain no visuals. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **6.5 Resolved Issues** | |
| MSSQL Connections | Resolved a problem in which some MSSQL connections no longer worked for visuals and dashboards after an upgrade from 4.9 to 5.9. |
| Embedded Dashboards | Line and bar trend visuals now work in embedded scenarios. |
| Dashboards & Visuals | Corrected a problem in which leaving a dashboard or visual while the Settings sidebar is open caused the visual or dashboard to go blank. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **6.4 Resolved Issues** | |
| Embedded Dashboards | You can now remove a visual from an embedded dashboard. A new **Remove Visual** option is added to the embedded dashboard drop-down menu. |
| Numeric Data Exports | All numeric data in an exported CSV file is now exported in decimal form. In past releases, some numbers were exported using scientific notation. |
| Window Aggregation Functions | Window aggregation functions now support derived fields as partitioning arguments. See Window Aggregation Functions. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **6.3 Resolved Issues** | |
| Embedded Dashboards | Dialog elements now appear correctly for iFrameless embedded dashboards. |
| Filtering | Corrected a filter problem that occurred when drilling down (zooming) on a particular attribute. |
| Amazon S3 Connector | Corrected a problem in which the Amazon S3 connector sporadically failed to detect a file delimiter. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **6.2 Resolved Issues** | |
| LDAP | Resolved LDAP errors that occurred when logging in as a user whose Composer account was changed since the LDAP user definitions were established. |
| Embedded Dashboards | Unnecessary pop-up dialogs no longer appear in an embedded dashboard when the visual style is switched. |
| Time Bar | The initial load of a dashboard no longer hides the time bar. |
| Dashboards | The top of a long dashboard link list is now viewable when you scroll down the list. |
| An error now appears if you try to import a dashboard that contains a visual that does not exist in Composer. |
| Themes | Dark themes now work correctly with line charts. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **6.1 Resolved Issues** | |
| Jquery Support | Compoer updated the version of `jquery` it uses to version 3.5.0 or later. |
| Map Visuals | The OpenMapSurfer tile provider for maps is no longer supported. When you upgrade to this version of Composer, all visuals that use OpenMapSurfer are upgraded to use OpenStreetMap instead. |
| Snowflake Connector | Problems creating a Snowflake data source from a Snowflake table that contained a numeric or date field are resolved. |
| Performance | Peformance was improved for the sort and limit feature in visuals. |

[Return to top](#top "return to top")

| Title | Description |
| --- | --- |
| **6.0 Resolved Issues** | |
| Connectors | Connectors correctly start now when the `config-server.enabled=true` option is set in the `edc.properties` file in an HA environment. |
| Security | Improved security in enterprise data connectors. |
| Kerberos | If you have Kerberos enabled, you must use a static context path for the Composer login URL. Multiple or dynamic context paths are not supported at this time. |

[Return to top](#top "return to top")
