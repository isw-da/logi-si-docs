---
title: "Logi Composer 26.2 Feature Enhancements"
id: 46968199924109
section: "Logi Composer  26 Release Notes Overview"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968199924109-Logi-Composer-26-2-Feature-Enhancements
updated_at: 2026-08-26T07:11:49Z
---

# Logi Composer 26.2 Feature Enhancements

# Logi Composer 26.2 Feature Enhancements

This topic provides details about the enhancements in Logi Composer 26.2.

To purchase this product, contact [insightsoftware Sales](mailto:loginewbusinessteam@insightsoftware.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "Sales email address.").

* [Home Page & UI Updates](#Home)
* [API Updates for Symphony Environments](#sym-api)
* [Self Service Reports](#Self)
* [Simba Intelligence Integration](#Simba)
* [Connect to Dundas BI Data](#Connect)
* [Page Size and Orientation Options](#Page)
* [Scheduled Reports Timing](#Schedule)
* [Full Dataset Searching](#Full)
* [Excel Export Enhancements](#Excel)
* [Source Editor Improvements](#Source)
* [Add Field Metadata to Sources](#Add)
* [Simba Intelligence Field Metadata](#Simba2)
* [New Display Styles for Line Trends](#New)
* [Large Integer (INT64) Precision Support](#Large)
* [Data Connection Java Update](#Data)
* [Grid Performance & Rendering Improvements](#Grid)
* [Embedded Connections](#Embedded)
* [Operating System Support Updates](#Operatin)

To purchase this product, contact [insightsoftware Sales](mailto:loginewbusinessteam@insightsoftware.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "Sales email address.").

## Home Page & UI Updates

Your home page, main menu, and overall user interface have been enhanced with a new look, feel, and fresh color theme. We call it the Enhanced Experience. It modernizes and expands the Classic Experience that has defined your embedded analytics experience.

The home page updates bring together changes that make it easier for users to access sources, visuals, libraries, and administrative features.

The main menu has been reimagined, so your users and administrators can quickly access the features, information, tenants, or other tools they need.

For more information, see [Home Page](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136935821-Home-Page) and [The Main Menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701160499853-The-Main-Menu).

Which interface will I see when I implement 26.2?

No matter your transition path, when implement v26.2 in your environment, your custom theme is honored. When you are ready to stage and then roll out the layout changes to your users, enable the `enhanced-experience` toggle. See [Server-Level Variables](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables).

* **The Enhanced Experience** If you are transitioning from Symphony 26.1 or earlier, you will see the enhanced experience layout and colors you are already using.
* **The Classic Experience** If this is a fresh installation of v26.2 in your environment, you will see the classic experience layout and [default **composer** color theme](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163831053-Manage-User-Interface-Themes#Supplied "default composer color theme"). Enable the `enhanced-experience` toggle in your staging environment to try it out, then roll it out to your users.
* **The Classic Experience** If you are transitioning from Composer 26.1 or earlier and using any [previous color theme](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163831053-Manage-User-Interface-Themes#Supplied "previous color theme") (**composer**, **modern**, **dark**), you will see the classic experience layout and composer color theme. Enable the `enhanced-experience` toggle in your staging environment to try it out, then roll it out to your users.
* **The Classic Experience** If you are transitioning from Composer 26.1 or earlier and using a custom color theme, you will see the classic experience layout with your colors. Enable the `enhanced-experience` toggle in your staging environment to see what it looks like. You will need to [add information to your existing color theme](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701210155405-Themes-JSON-File#Update "add information to your existing color theme") to expand it to include the new user interface elements before you roll it out to your users. See [User Interface Themes: v26.2 and Later](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701163831053-Manage-User-Interface-Themes#User2) and [Themes and UI Updates](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077251302669-Themes-and-UI-Updates).

**Caution:** Update your custom theme and enable the `enhanced-experience` toggle before upgrading past version 26.2. The enhanced homepage and navigation will become the standard experience for all users in the near future. We recommend making these updates now to ensure a smooth transition.

## API Updates for Symphony Environments

With the release of 26.2, Symphony has been restructured.

* Content previously managed in Visual Data Discovery or as embedded Visual Data Discovery content will be supported in Composer 26.2 and later releases.
* Content previously managed in Managed Dashboards and Reports will be supported in Dundas BI.

Along with this update, if you used Symphony with Visual Data Discovery embedded content or Managed Dashboard APIs, you must update your authentication workflow. Symphony used the Dundas BI authentication model, but going forward, this product will use the Composer API authentication model.

API user management orchestration is also impacted by this transition. Symphony Tenants, Users and Groups were managed by Managed Dashboards (DundasBI). For a successful transition, you must retarget the API calls to Composer 26.2 or later releases before you update your environment.

For more information on how to plan and work through this transition, reach out to [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) for assistance.

For a brief overview of all environment and capability changes, see [Transitioning for Symphony and Composer Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968228172557-Transitioning-for-Symphony-and-Composer-Users).

## Self Service Reports

Composer now includes [Self Service Reports](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46982003580173-Manage-Self-Service-Reports), giving your users a full-featured, self-service reporting experience available directly in Composer or as an embedded component in your application. Disabled by default, you can [enable this feature](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables) during upgrade or installation.

Users can [build customized reports](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46982018753165-Create-Self-Service-Reports) from table visuals with robust formatting for headers and footers, conditional formatting, grouping, and aggregate functions. Reports can be exported as PDF or Excel (XLSX), with [formatting](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46981992392077-Format-Self-Service-Reports) and grouping fully reflected in exports. Group-structured reports support multiple columns in group headers and detail sections.

[Schedule reports](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701093791245-Schedule-a-Self-Service-Report-or-Dashboard-Report) for one-time or recurring delivery by email to internal and external users, with configurable sender display name and reply-to address. [Permissions and access controls](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701029259149-Scheduled-Reports-Permissions-and-Behavior) mirror the Dashboard Library experience, allowing per-user or group-based access management. Reports can also be shared with users and [groups across your instance](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701077162637-Share-a-Dashboard-or-Self-Service-Report-with-Users).

Report generation and export performance varies significantly based on report complexity, report generation volume, and export format. For more information on environment sizing and use planning guidelines, see [Environment Configuration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Environm) and [Performance Considerations](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Performa).

**Note:** If you are transitioning from Symphony v26.1 or earlier, you will need to enable self service reports in your environment to continue offering it to your users. For a brief overview of all environment and capability changes, see [Transitioning for Symphony and Composer Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968228172557-Transitioning-for-Symphony-and-Composer-Users).

## Simba Intelligence Integration

This release introduces support for Simba Intelligence integration, bringing a comprehensive suite of AI-powered analytics capabilities to your environment. Simba Intelligence is separately licensed and powers the AI features described below.

For more information, see the [Simba Intelligence Product Overview](https://insightsoftware.mintlify.app/simba-intelligence/docs/getting-started/Product-Overview "Simba Intelligence Product Overview").

**Create Sources with AI**

Use AI to generate a data source from your available data connections. Select **Create with AI** from the Sources work area to open the **Data Source Agent** from Simba Intelligence, which guides you through building your source.

**Generate Visuals with AI**

Create visuals from natural language prompts from multiple entry points — the home page, the Visual Gallery, and directly within dashboards. The AI is context-aware, understanding the dimensions, measures, and filters of the visual or dashboard you're working in. Save generated visuals directly from the AI response, or open them for further editing before saving to a dashboard or the Visual Gallery.

**Source Field Metadata**

Add field-level metadata to your data sources to provide additional context — such as data lineage or usage restrictions — for both users and AI tools such as Simba Intelligence to make appropriate decisions.

Metadata is stored as key-value pairs, available via API, and exported with the source. You can retrieve the field metadata configured at the index in OpenSearch and Elasticsearch as part of a describe API call.

**Note:** If you are transitioning from Symphony v26.1 or earlier, you will need to enable Simba Intelligence in your environment to continue offering it to your users. For a brief overview of all environment and capability changes, see [Transitioning for Symphony and Composer Users](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/46968228172557-Transitioning-for-Symphony-and-Composer-Users) and work with Technical Support to enable this in your environment.

## Connect to Dundas BI Data

In an environment transitioning from Symphony that uses connected data in Dundas BI (Managed Dashboards & Reports) will need to enable the appropriate connections and credentials to add access to that source in version 26.2 and later. See [Connect to a Dundas BI Data Store](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701054605453-Modify-Data-Store-Connections#Reconnec).

## Page Size and Orientation Options

You can now select a page size and orientation for self service reports and scheduled self service reports. Options for PDF export and scheduled report sharing include:

* Page Size: US Letter, A4, A3
* Orientation: Portrait or Landscape
* By default, or if you do not make a selection, reports and scheduled reports default to **US Letter - Portrait**
* All available size and paper orientation options are paired in the user interface, for example, **US Letter - Portrait**, **US Letter - Landscape**

Report generation and export performance varies significantly based on report complexity, report generation volume, and export format. For more information on environment sizing and use planning guidelines, see [Environment Configuration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Environm) and [Performance Considerations](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Performa).

## Scheduled Reports Timing

Scheduled self service reports and dashboard reports now support a `timezone` field your users can use to run scheduled reports in a specified timezone, automatically adjusted for Daylight Saving Time (DST).

If no timezone is provided, schedules default to UTC. This ensures reports consistently deliver at the intended local time year-round without manual adjustments around DST transitions.

## Full Dataset Searching

Users can now search connected data sources beyond the previous record display limits and return the results to filters and filter snippets.

## Excel Export Enhancements

You can now export a table visual with grouped columns to [Excel (XLSX) format](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47469265422605-Export-Visual-Data-in-Excel-XLSX-Format). The export includes conditional formatting and grouping, if present in your table. This feature relies on the self service report [microservice](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice).

Report generation and export performance varies significantly based on report complexity, report generation volume, and export format. For more information on environment sizing and use planning guidelines, see [Environment Configuration](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Environm) and [Performance Considerations](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/47077282029965-Self-Service-Report-Microservice#Performa).

**Note:** To use self service reports, you will need to enable it in your environment. See [Server-Level Variables](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701053868173-Server-Level-Variables#scheduled-report).

## Source Editor Improvements

This release brings several improvements to the source creation and editing interfaces.

* The SQL editing work area is larger, making it easier to create your queries. The Add SQL Entity button is also easier to find.
* Entity and Filter Value Entity nodes now display helpful tooltips and on-canvas text.
* The Joins node label is now Add Join to make the interface more intuitive.

## Add Field Metadata to Sources

You can now add metadata at the field level to new and existing sources. This allows you and your users to add additional context to improve the understanding of this field. Use to add information such as data lineage or usage restrictions.

The field metadata is stored as a keyed pair of Property and Value in your environment. Use in several ways:

* As information consumed by an integrated AI tool: for example, Simba Intelligence or other tool can read the information and interpret it without adding it to the visual.
* As internal information for users who can view the data in your source.

The metadata you define is available using the API, and exported with the source (JSON format); when you move, share, and copy or export your source to share with other environments.

## Simba Intelligence Field Metadata

In environments that are integrated with Simba Intelligence, you can index the field metadata information added to your data sources by your users.

**Important:** 
You must have the appropriate licensing from insightsoftware to see this option.

## New Display Styles for Line Trends

Two new display styles and a smooth curve toggle are now available for Line Trend (Multi Metric) and Line Trend Continuous (Attribute Values) charts. Select the appropriate option in the **Display Style** and **Style** sections of the Settings sidebar menu.

* Line Chart: displays content as straight lines between points, with no fill. Default setting.
* Area Chart: fills the area beneath each line with a solid color.
* Gradient Area Chart: fades the fill from opaque to transparent for a more polished look.
* Smooth Curve toggle: renders lines with fluid spline interpolation instead of straight segments.

## Large Integer (INT64) Precision Support

Composer now more accurately handles large integer values with 16 or more digits across data source previews, visuals, custom metrics, as well as PDF and XLSX exports. Previously, values such as large numeric IDs were sometimes silently rounded due to floating-point precision limits, potentially producing incorrect results.

All INT64 values are now preserved exactly as stored in the data source.

## Data Connection Java Update

The data connection layer has been upgraded to Java 21, bringing improved performance, security, and long-term infrastructure compatibility.

## Grid Performance & Rendering Improvements

Our underlying grid engine has been upgraded to the latest version, 35.2.1.

## Embedded Connections

You can now embed inventory connections using the iframeless JavaScript API, allowing you to provide more content in an embedded iframeless format.

## Operating System Support Updates

When you install or upgrade to v26.2 in a Windows environment, your operating system must be Windows Server 2019 or later. See [Operating System Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136004365-Operating-System-Support).
