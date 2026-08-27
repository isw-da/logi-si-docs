---
title: "Logi Composer Version 26 Summary of Changes"
id: 43701192423949
section: "Logi Composer  26 Release Notes Overview"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701192423949-Logi-Composer-Version-26-Summary-of-Changes
updated_at: 2026-08-26T07:10:59Z
---

# Logi Composer Version 26 Summary of Changes

# Logi Composer Version 26 Summary of Changes

This is a summary of the major changes made in version 25 of Composer. It is provided so you can quickly identify new and changed Composer features before upgrading from Composer 25 to Composer 26.

This software is offered on a quarterly release schedule. The current major release is v26.2.

## Upgrade Considerations

Be sure to back up your metadata store (see [Back Up the Metadata Store](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701164946317-Back-Up-the-Metadata-Store)) before you upgrade.

Upgrading to Logi Composer v23.2 or later includes an upgrade of Java runtime from 11 to 17, installed and configured automatically during upgrade.

**Important:** Before you upgrade to Composer v25.2 or later you must use a newer version of CentOS than CentOS 7 or CentOS 8. If you are not using this tool, you can exclude the `sdk-service` when installing or upgrading Composer.

**Note:** CentOS 7 & 8 are end of life (EOL) support. CentOS Stream 9 is supported for new instances of Logi Composer 25.4 and higher. Upgrade your operating system to CentOS Stream 9 before upgrading your Composer instance. For more information, see [Operating System Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136004365-Operating-System-Support).

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

To ensure services start properly after upgrade in a Linux environment:

1. Verify all of your JVM setting overrides are defined in the `/etc/zoomdata` directory (not `/opt/zoomdata/conf`).
2. The `.jvm` files in `/etc/zoomdata/` only contain parameters that are different from default ones, typically Xms/Xms settings, javaagent settings.

   If you have copied the entire `.jvm` file from `/opt/zoomdata/conf` for placement into `/etc/zoomdata`, that configuration is not overwritten after upgrade. Properties such as `XX:+UseConcMarkSweepGC` can prevent services from starting on Java 17 runtime.

For more information on configuration setups and overrides, see [Configure Memory Settings](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701040681613-Configure-Memory-Settings) and [Connector Properties and Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992050061-Connector-Properties-and-Property-Files).

**Caution:** 
If you are upgrading from an earlier version of Logi Composer, this may be a breaking change: the introduction of the system attribute `User.timeZone` may cause a conflict if you used this as a custom attribute. See [Upgrade Workflow](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068707725-Timezone-Conversion-for-Users#Upgrade).

## Enhancements

The following sections provide you with a summary of enhancements in the previous releases, all of which are present in the latest release of Logi Composer.

* [v26.2 Enhancements](#q2)
* [v26.1 Enhancements](#q1)
* [Removed Features From Logi Composer v25](#Removed)
* [API Updates in Logi Composer v26](#API)

## v26.2 Enhancements

* [Home Page & UI Updates](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#Home)
* [API Updates for Symphony Environments](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#sym-api)
* [Self Service Reports](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#Self)
* [Simba Intelligence Integration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#Simba)
* [Connect to Dundas BI Data](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#Connect)
* [Page Size and Orientation Options](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#Page)
* [Scheduled Reports Timing](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#Schedule)
* [Full Dataset Searching](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#Full)
* [Excel Export Enhancements](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#Excel)
* [Source Editor Improvements](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#Source)
* [Add Field Metadata to Sources](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#Add)
* [Simba Intelligence Field Metadata](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#Simba2)
* [New Display Styles for Line Trends](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#New)
* [Large Integer (INT64) Precision Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#Large)
* [Data Connection Java Update](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#Data)
* [Grid Performance & Rendering Improvements](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#Grid)
* [Embedded Connections](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#Embedded)
* [Operating System Support Updates](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements#Operatin)

## v26.1 Enhancements

* [Source Creation Updates](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#Source)
* [Tenant Management Updates](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#Tenant)
* [Interactivity Overrides](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#Interact)
* [Mapbox Style & Satellite Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#Mapbox)
* [Numeric Ratios](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#Numeric)
* [PDF Generation](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#PDF)
* [UI Improvements](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#UI)
* [Dependency & Tooling Upgrades](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#Dependen)
* [Spring Boot Updates](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701146985741-Logi-Composer-26-1-Feature-Enhancements#Spring)

## Removed Features From Logi Composer v25

The following features were removed from Logi Composer v25 to make way for improvements in Logi Composer v26.

### Logi Composer 26.2

| Title | Description |
| --- | --- |
| **26.2.2 Removed Features** | |
| None. |  |
| **26.2.1 Removed Features** | |
| None. |  |
| **26.2 Removed Features** | |
| UI Menu | In environments where the [enhanced-experience](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables#ui-toggle "enhanced-experience link") toggle has been enabled, the UI menu has been reconfigured into an always-available main menu. Access your content and navigate options using the [main menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Main-Menu) or [home page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page). |
| Top-Level Navigation | In environments where the [enhanced-experience](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables#ui-toggle "enhanced-experience link") toggle has been enabled, the top-level navigation option has been removed from the user interface. Access your content and navigate options using the [main menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Main-Menu) or [home page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page). |
| System Users Menu Option | In environments where the [enhanced-experience](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables#ui-toggle "enhanced-experience link") toggle has been enabled, the menu option **System Users** has been removed from the main menu UI. Users with appropriate privileges can instead access users using the **User** menu option, and groups using the **Groups** menu option. |
| Multi-Tenancy Menu Option | In environments where the [enhanced-experience](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables#ui-toggle "enhanced-experience link") toggle has been enabled, the menu option **Multi-Tenancy** has been renamed **Tenants**. Use this option to create, access, and manage tenant accounts. |
| Edit Tenant Work Area | In environments where the [enhanced-experience](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables#ui-toggle "enhanced-experience link") toggle has been enabled, the Edit Tenant work area has been redesigned. Switch between tenants to edit by selecting a different tenant from the tenant list in the Multi-Tenancy work area.  The **General** tab and tenant switching dropdown list have been removed. |

### Logi Composer 26.1

| Title | Description |
| --- | --- |
| **26.1.3 Removed Features** | |
| None. |  |
| **26.1.2 Removed Features** | |
| None. |  |
| **26.1.1 Removed Features** | |
| None. |  |
| **26.1 Removed Features** | |
| None. |  |

## API Updates in Logi Composer v26

This table provides a breakdown of all reported updates in Logi Composer v26.

### Logi Composer 26.2

| Endpoint | Method | Description |
| --- | --- | --- |
| **26.2.2 API Updates** | | |
| None. |  |  |
| **26.2.1 API Updates** | | |
| None. |  |  |
| **26.2 API Updates** | | |
| api/export/visualdata/enriched | POST | Export visual data for table visuals including grouped data in Excel (XLSX) format. Your formatting, aggregation, and conditional formatting are preserved in the exported file.  Report generation and export performance varies significantly based on report complexity, report generation volume, and export format. For more information on environment sizing and use planning guidelines, see [Environment Configuration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Environm) and [Performance Considerations](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Performa). |
| api/dashboards/{dashboardId}/reports  api/dashboards/{dashboardId}/reports/{reportId} | POST  PUT | Create or update a scheduled dashboard report. This supports features added in this release.   * `timezone`: include to support DST-aware scheduling instead of the default UTC |
| api/dashboards/{dashboardId}/reports  api/dashboards/{dashboardId}/reports/{reportId} | POST  PUT | Create or update a scheduled self service report. This supports features added in this release.   * `timezone`: include to support DST-aware scheduling instead of the default UTC * `pageSize`: include a setting to override the default of US Letter Portrait. Size options include LETTER, A4, and A3. * `orientation`: define the orientation of the report. This includes page-aware column count validation and font size validation for the selected orientation.    * PORTRAIT: 15 column max for Letter and A4 paper sizes. 22 column max for A3 paper size.   * LANDSCAPE. 20 column max for Letter. 22 column max for A4. 30 column max for A3.  **Note:** Column count validation is not performed on Group Structured Reports.   Report generation and export performance varies significantly based on report complexity, report generation volume, and export format. For more information on environment sizing and use planning guidelines, see [Environment Configuration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Environm) and [Performance Considerations](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Performa). |
| api/self-service-reports/export | POST | Export self service reports. This supports features added in this release.   * `pageSize`: include a setting to override the default of US Letter Portrait. Size options include LETTER, A4, and A3. * `orientation`: define the orientation of the report. This includes page-aware column count validation and font size validation for the selected orientation.    * PORTRAIT: 15 column max for Letter and A4 paper sizes. 22 column max for A3 paper size.   * LANDSCAPE. 20 column max for Letter. 22 column max for A4. 30 column max for A3.  **Note:** Column count validation is not performed on Group Structured Reports.   Report generation and export performance varies significantly based on report complexity, report generation volume, and export format. For more information on environment sizing and use planning guidelines, see [Environment Configuration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Environm) and [Performance Considerations](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Performa). |

### Logi Composer 26.1

| Endpoint | Method | Description |
| --- | --- | --- |
| **26.1.3 API Updates** | | |
| None. |  |  |
| **26.1.2 API Updates** | | |
| None. |  |  |
| **26.1.1 API Updates** | | |
| None. |  |  |
| **26.1 API Updates** | | |
| api/dashboards/ | GET | The GET api/dashboards/ endpoint now returns the creator's full name as **creatorFullName**. |
