---
title: "Logi Composer 26.1 Release Notes"
id: 43701161443469
section: "Logi Composer  26 Release Notes Overview"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701161443469-Logi-Composer-26-1-Release-Notes
updated_at: 2026-05-29T14:09:20Z
---

# Logi Composer 26.1 Release Notes

# Logi Composer 26.1 Release Notes

This topic describes feature enhancements, resolved issues, and important information for Composer 26.1.

To purchase this product, contact [insightsoftware Sales](mailto:loginewbusinessteam@insightsoftware.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "Sales email address.").

* [Feature Enhancements](#Feature "Feature Enahncements section")
* [Operating System Support](#OS)
* [API Updates](#API_Updates "API Updates section")
* [Resolved Issues](#Resolved)
* [Deprecated Features](#Deprecated_Features)
* [Removed Features](#Removed_Features)

See also [Important Notices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701141033869-Important-Notices), [Deprecated Features](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701161163533-Deprecated-Features), and [Logi Composer Version 26 Summary of Changes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701192423949-Logi-Composer-Version-26-Summary-of-Changes).

Composer is offered on a quarterly release schedule. The current major release of Composer is v26.1.

## Feature Enhancements

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

## Operating System Support

*List Updated: 15 March 2026*

**Important:** This information is provided to assist you in planning your future upgrade projects.

**Caution:** Running an older, unsupported operating system in your environment is done so at your own risk. Plan and upgrade to a supported operating system for full support and functionality.

* RHEL 9 (Red Hat)
* CentOS Stream 9
* Ubuntu 22.04.

  **Note:** Older versions of Ubuntu are nearing end of life (EOL) support. Composer 26.1 and later will require an operating system upgrade before you upgrade your Composer instance.
* Windows Server versions 2016 and 2019 or higher.

For more information on current and future planned operating system support information, see [Operating System Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136004365-Operating-System-Support).

## API Updates

API documentation is provided in your environment at this link: `https://<composer-URL>/composer/swagger-ui.html`.

| Endpoint | Method | Description |
| --- | --- | --- |
| **26.1.2 API Updates** | | |
| None. |  |  |
| **26.1.1 API Updates** | | |
| None. |  |  |
| **26.1 API Updates** | | |
| api/dashboards/ | GET | The GET api/dashboards/ endpoint now returns the creator's full name as **creatorFullName**. |

## Resolved Issues

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

## Deprecated Features

| Title | Description |
| --- | --- |
| **26.1.2 Deprecated Features** | |
| None. |  |
| **26.1.1 Deprecated Features** | |
| None. |  |
| **26.1 Deprecated Features** | |
| None. |  |

## Removed Features

| Title | Description |
| --- | --- |
| **26.1.2 Removed Features** | |
| None. |  |
| **26.1.1 Removed Features** | |
| None. |  |
| **26.1 Removed Features** | |
| None. |  |

## Known Issues

| Affected Releases | Description |
| --- | --- |
| **Logi Composer 26.1** and later | None. |
