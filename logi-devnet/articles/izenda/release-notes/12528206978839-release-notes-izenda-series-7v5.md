---
title: "Release Notes Izenda Series 7v5"
id: 12528206978839
section: "Release Notes"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528206978839-Release-Notes-Izenda-Series-7v5
updated_at: 2026-06-22T15:26:08Z
---

# Release Notes Izenda Series 7v5

## Izenda Series 7 Release Notes

Note

* Preview Release - x.x.1 - Early access to new features in isolation
* Core Release - x.1.x - Quarterly stable release with preview releases and hotfixes combined
* Major Release - 1.x.x - Larger Features, potential breaking changes

We have changed Izenda to a new version numbering system. Izenda Series 7 v5 is now Izenda Series 7 v2023.1.1. Version names for Izenda Series 7 v5 and earlier remain unchanged.

Warning

> * For all upgrades and installations, downloads.izenda.com is moved to our customer portal at app.izenda.com

For more advanced information and details on our releases where needed, please see our Release Details and [Breaking Changes](#01JFAENQTB5Z690T3MAK3CBAB5).

## 

## v2025.4.1 Major Release Release Notes - November 24, 2025

We have released the following enhancements with v2025.4.1:

## Features v2025.4.1

### Library and Security Updates

The following updates have been made in this release, 2025.4.1:

* jQuery has been updated from 2.2.1 to 3.5.0
* TinyMCE has been updated from 4.4.0 to 7.3.0
* Karma has been updated from 0.13.21 to 6.3.16
* PostCSS has been updated from 5.0.21 to 8.4.31

### Show All Available Schedules

Users can now see the available schedules when they navigate to **Settings** > **System Configuration** > **Scheduling** to open the Scheduling page.

* On upgrade, Izenda now displays available schedules that are already set.
* This changes previous behavior: display of a blank scheduling page until the user further selected **Search**.

### Headers and Footers - Beta Reports (RD2) - Report layout updates

We have extended feature parity for headers and footers in Classic and Beta Reports. You can now Enable Preview for different print layouts in the PDF Emulator.

* Use the final Layout to visualize differences between web and print layouts
* Switch between different layouts while in the Preview page

## Fixes:

|  |  |
| --- | --- |
| **Defect** | **Description** |
| 25803 | Subtotal for collapsed All is incorrect in drilldowns. |
| 29714 | Multiple embedded From report has an issue while Exporting. |
| 30655 | When Using Arabic Language Pack The Header Date Will Display in English When Exporting The Report |
| 31304 | Custom view definition inconsistent syntax validation. |
| 33133 | Import same report multiple times in same category Path. |
| 34509 | Scheduled Report Not Delivered. |

## v2025.2.1 Major Release Release Notes - June 30, 2025

We have released the following enhancements with v2025.2.1:

## Features v2025.2.1

* **Library and Security Updates**

  + Upgraded .NET libraries including SixLabors.ImageSharp, BouncyCastle, Npgsql, Snowflake, Oracle, and MySQL.

    - Addressed CVE-2024-29857, CVE-2024-30172, CVE-2025-27598, and CVE-2025-24788
  + Migrated `System.Data.SqlClient` to `Microsoft.Data.SqlClient`.
  + Upgraded Quartz scheduling library to v3.13.1.
    - If Quartz ADO.NET Job Store is enabled (distributed environments), you will need to append `Encrypt=False` to the end of connectionString in `quartz.config`.
  + Report Part Defaults improvements.
  + Updated SharedVersionStorage tool to .NET 8 and relative libraries.
  + Upgraded javascript library, Moment.js to v2.30.1.
* **Enhanced Time Picker**

  + Added new user setting, Time Format, to differentiate between 12 & 24 Hour.
  + Improved time picker based on new user setting, Time Format, applies to scheduling, subscriptions, and time filter selection.
  + Time picker dropdown for hours, minutes, and if applicable, AM/PM.
* **Header and Footer in Beta Reports (RD2)**

  + Feature Parity between Classic and Beta Reports for headers and footers.
  + Enable Header, Footer, and Title & Description will appear in Layout Designer of Beta Report Designer.
    - Header/Footer will be layout specific - allowing for unique Web and Print Layouts.
  + Header and Footer will be migrated when upgrading classic report.
* **SMTP Microsoft Authentication**
  + Added support for Microsoft OAuth in addition to Basic Authentication.
  + Microsoft OAuth will be shown in Authentication Type dropdown in System Configuration → Email.
    - New SMTP OAuth settings have been added.

## Fixes:

|  |  |
| --- | --- |
| **Defect** | **Description** |
| 29320 | Report IDs are not retained when using external dashboard/import endpoint. |
| 30461 | Custom data formats with GroupBy do not show correctly on charts. |
| 31541 | Blank row appears in Excel export when separator value is empty. |
| 31736 | QuerySourceId column is not populated in IzendaReportDataSource table. |
| 34249 | Access Rights and Schedules do not save on new report created through Save As. |
| 34270 | Footer is misplaced in beta report viewer when multiple report parts are added. |
| 34277 | Dashboard shows blank screen after navigating from full screen presentation mode. |
| 34282 | KPI metric is not reflecting updated function. |
| 34285 | Calculated field in beta report designer do not display expected value. |
| 34301 | PDF Zoom functionality is not being applied when emailing or scheduling. |
| 34402 | Map does not display metrics in report part in certain scenarios. |
| 34410 | Query Source tables are not cleaned up after records are soft deleted. |
| 34417 | Visualization labels are being cut off in existing dashboards. |
| 34420 | PDF does not display report header format as seen in the report viewer. |
| 34424 | Unexpected gap between report parts in print layout designer. |
| 34428 | PDF Zoom is not applied to height in preview of layout designer. |
| 34430 | Map indefinitely loads when drilling into specific countries. |
| 34441 | Print Layout displays unexpected scroll and Page Break does not display properly. |

## 

## v2024.4.6 Service Pack Release Notes - April 02, 2025

## Fixes:

|  |  |
| --- | --- |
| **Defect** | **Description** |
| 33842 | Items in Export Manager are not deleted when deployed with Oracle configuration database. |
| 33934 | Visualization labels are not being displayed after report part fits to container. |
| 34040 | Updates to dashboard’s filters displays error when deployed with Oracle configuration database. |
| 34338 | Dashboard report parts are not being displayed or aligned in the container correctly. |
| 34341 | PDF exports fail when Pivot Grid contains blank cells. |

## v2024.4.5 Service Pack Release Notes - January 22, 2025

## Fixes:

|  |  |
| --- | --- |
| **Defect** | **Description** |
| 33961 | Visualization exports failed when deployed to Azure App Service. |
| 34288 | PDF exports fail when Header & Footer enabled on report but no items found. |

## v2024.4.4 Service Pack Release Notes - December 27, 2024

## Fixes:

|  |  |
| --- | --- |
| **Defect** | **Description** |
| 34276 | The EmbeddedUI package is incorrectly injecting native CSS into the parent HTML rather than the Izenda container. |

## v2024.4.3 Service Pack Release Notes - December 18, 2024

## Fixes:

|  |  |
| --- | --- |
| **Defect** | **Description** |
| 30658 | Filter with selected multiple value delimiter option does not allow space to be entered. |
| 33520 | Existing schedules do not reflect updates made to a filter to when converting it to a multiple value filter. |
| 33825 | Default datetime format is incorrect when grouping is applied in classic designer. |
| 33994 | KPI displays a blank report part in exported file when using Async Exporting. |
| 33996 | Deleted categories are displayed and unable to be deleted from dashboard list. |
| 34141 | Data Cache files are not cleaned up when Quartz database is enabled. |
| 34155 | Migrating Classic Reports to Beta Reports fail due to timeout. |
| 34165 | Image HTML tags do not export when Render HTML in Printing/Exporting is selected. |
| 34183 | Variables displayed in Share & Schedule do not represent report instead of dashboard. |
| 34187 | Selected emails are not retained and displayed in Email modal input. |
| 34192 | Fields added to Form are not retained once navigating to and back from M2 in Beta Designer. |
| 34208 | Unable to duplicate Form report part after navigating to Preview tab. |
| 34213 | Drag and Drop in Form report part does not drop item within Table structure. |
| 34214 | Selection focus on Smart Tag is inconsistent when designing a Form. |
| 34220 | Unsaved changes state is not being maintained as expected in report designer. |
| 34221 | Data is not being displayed in Preview tab of Form designer. |
| 34228 | Icons are not displayed when Heading property is applied to a field in Form designer. |
| 34231 | Multiple Grand Totals are being displayed in the same row. |
| 34232 | Loading animation is not being displayed during initial load of a Beta Report. |
| 34236 | Role Setup category accessibility error message is displayed when adding user who already has access to the specified category due to a different Role than the one being updated. |
| 34242 | Excel exports display data type warnings on Numeric values. |
| 34243 | Chart visualizations are re-rendering in dashboard full screen mode. |
| 34255 | Entering configuration mode of a dashboard tile displays a blank page. |
| 34258 | Data Defaults are not being set and updated in Beta Designer. |
| 34261 | Report Parts are not being aligned as expected in Beta Designer. |
| 34263 | Edit and Export drop-down in configuration mode of dashboard tile does not open. |
| 34265 | Save drop-down on Copy Management tab displays two arrows. |

## v2024.4.2 Service Pack Release Notes - November 8, 2024

## Fixes:

| **Defect** | **Description** |
| --- | --- |
| 34166 | Role Setup category accessibility error message is displayed when Full Report and Dashboard Access is selected |
| 34230 | Datetime displays incorrect values in exported Excel file when no format is set |

## v2024.4.1 Major Release Release Notes - October 21, 2024

## Breaking Changes v2024.4.1

* Izenda UI’s Bootstrap library upgraded to v5.3.0
  + In embedded instances, CSS conflicts may arise due to new bootstrap updates
  + Sample commits resolving these conflicts can be found in our MVC Core Starter Kit:  <https://github.com/Izenda7Series/MVCCore_DM1_StarterKit/commits/master/>
* Izenda UI’s TinyMCE library upgraded to v7.3.0
* Izenda API upgraded to support .NET 8
  + Hosting environments need to install the necessary hosting bundles to run .NET 8: <https://dotnet.microsoft.com/en-us/download/dotnet/8.0>
* The Izenda API SharpZipLib library is upgraded to v1.4.2
* Deprecated mutation events have been removed/replaced in Izenda UI
* Elasticsearch, Mongo, & Salesforce data adapters are no longer supported

## Fixes

| **Defect** | **Description** |
| --- | --- |
| 30470 | Conditional formatting does not export when embedded subreport is displayed within a Grid report part |
| 31788 | Images do not export when placed within a Form report part |
| 31840 | Image orientation is not respected when exported to PDF |
| 31847 | Image alignment is not respected when exported to PDF |
| 33945 | Report Part Defaults are not set when report is saved in M1S2 of RD2 |
| 33956 | Dashboard Viewer crashes when loading presentation mode |
| 33975 | BIGINT values do not display expected value |
| 33986 | Classic Report with header/footer does not load after migrating to RD2 |
| 34045 | RD2 does not allow changes to Chart type when multiple report parts are present |
| 34109 | Repeat Table Header in Forms (PDF) setting is not respected when `thead` tag is used |
| 34110 | System Variables when scheduling an email display reports and dashboard items |
| 34180 | Reports with sub and grand totals do not load after upgrading Izenda version |
| 34204 | CSS conflicts in MVC Core Starter Kit due to Bootstrap upgrade |

## 

## Izenda v2024.2.2 Service Pack Release Notes August 12, 2024

## Fixes

| **Defect** | **Description** |
| --- | --- |
| 31351 | Form report part editor updated to use HTML style attribute for borders |
| 34088 | When editing a schedule, the Bulb button in the email body is non-responsive |
| 34089 | PDF exports fail when exporting a decimal value and Culture/Language is not set |

## 

## v2024.2.1 Major Release Release Notes - May 10, 2024

We have released the following enhancements with v2024.2.1:

## Features v2024.2.1

* **New Report Designer (RD2) Enhancements**

  + Added Report Viewer button to quickly flip between Designer → Viewer.
  + Custom Recurrence for Scheduling Alerts.
  + File Location added as a Delivery Type in Sharing tab.
  + Report Part Defaults improvements.
* **Data Format Defaults**

  + Allows users to set default data formats on a per data type per tenant basis.
  + New section added to Settings → System Configuration → Report → Data Format Defaults.
  + New tenant and role permission added, *Report Part Defaults* → *Data Formats,* determines if default data formats can be modified.
  + If default data formats are set, they will automatically reflect when designing new report parts in New Report Designer, RD2.
* **Date Picker Min and Max Values**

  + Allows configuration of the minimum and maximum boundaries used by the date picker throughout the application - example: datetime filter.
  + New settings added to the front-end configuration: `minDate` and `maxDate`:
    - In Standalone deployments, located in the *izenda\_config.js* file.
    - In Embedded deployments, located where `IzendaSynergy.config(configJson)` is called, typically *izenda.integrate.js*.
  + Defaults to *1/1/1970 - Current Year + 20*. Allows for static and dynamic values, see shipped out defaults for examples.
  + Lowest configurable `minDate` is *1/1/0100 - no max* on `maxDate` but date picker performance will suffer depending on the range.

## Fixes

| **Defect** | **Description** |
| --- | --- |
| 31405 | RD2 Permission tab throws error when removing all selected tenants |
| 31488 | Notification drop-down UI improvements |
| 31741 | Report parts overlap in migrated RD2 reports, if they were originally duplicated |
| 31785 | Uncategorized categories are not displayed in report and dashboard lists |
| 33096 | Font size for PDF and Word exports do not match Report Viewer |
| 33129 | Filter drop-down does not search results consistently |
| 33184 | Key Join equal to Filter Comparison removes filter values that follow |
| 33235 | RD2 duplicate report name error message displays outside of modal |
| 33252 | RD2 does not allow users to edit the Email Body in Sharing tab |
| 33383 | Report Part Name appears in Cross Filtering section |
| 33354 | RD2 error in M1S3 after selecting a different table |
| 33465 | Deleting a tenant does not soft delete roles in configuration database |
| 33473 | Role Setup tab does not display success or error message |
| 33501 | Sub-report does not export data if opened from main-report using field mapping |
| 33515 | Metrics in Simple Gauges and KPI get truncated and cannot be adjusted |
| 33549 | Fractions do not export properly to Word and PDF when using Async Exporting |
| 33581 | Drill-down and Pivot Grids are being saved as Vertical Grids |
| 33672 | Charts are truncated in exports when using separators |
| 33690 | Charts are always defaulting to line chart when report part defaults are set |
| 33691 | Header and footers do not repeat per page in PDF exports |
| 33755 | Migrated RD2 Report does not display selected columns in Grids |
| 33814 | Inconsistent data displayed in charts when using Snowflake data connector |
| 33826 | Convert NULL to Empty String setting causes error in Snowflake data connectors |
| 33832 | Duplicate Move button in Dashboard List |
| 33844 | Roboto Font does not reflect report viewer in exported PDF |
| 33876 | MySQL data connector returns schema for case-differentiating databases |
| 33887 | Fields set to Available vs Visible in Data Connectors tab are being loaded and saved causing performance overhead |
| 33925 | Dashboard Report Part Edit Bar becomes inaccessible after saving report |
| 33948 | Image in report header is not displayed due to missing request headers |

## 

## Izenda v2023.1.3 Service Pack Release Notes January 31, 2024

## Fixes

| **Defect** | **Description** |
| --- | --- |
| 33173 | Title and Descriptions of copied report parts are updated when making changes to original report part |
| 33439 | The same key join in two separate joins displays duplicate join error |
| 33449 | Drilldown reports set Preview Record limit within JOIN clause leading to unexpected data - New Performance Settings flag added to move limit to top query node |
| 33560 | Duplicate data source in dictionary causes error for some reports being upgraded |
| 33653 | Paginated lists did not retain selected items when searching or navigating to other pages |
| 33745 | Custom URL field property does not properly encode multiple areas of string |
| 33758 | Oracle configuration database causes error when designing new or existing reports |
| 33857 | Updated MySQL.Data to v8.2.0 |

## Izenda v2023.1.2 Service Pack Release Notes September 26, 2023

## Fixes

| **Defect** | **Description** |
| --- | --- |
| 30499 | Excel Exports do not display fractions properly when using a different culture |
| 33044 | Legacy Grid Reports display error during export to PDF and Word |
| 33162 | Classic designer’s data source dropdown does not collapse and duplicate joined data source is visible |
| 33201 | PDF Exports do not display numbering and bullets in form report parts |
| 33284 | PDF Exports do not display bold and italics in form report parts |
| 33282 | PDF Exports are being created without file extension when using asynchronous exporting |
| 33332 | Migrating report with joined data sources causes report parts to display *No record found* |
| 33450 | Deleting and re-creating a tenant causes LVC Cache error throughout the application |

## v2023.1.1 Major Release July 17, 2023

We have released the following enhancements with v2023.1.1:

## Features v 2023.1.1

* **Report Part Defaults**

  + Allows user to set default RD2 report part properties and styles on a per tenant basis.
  + New section added to Settings → System Configuration → Report → Report Part Defaults
  + New tenant and role permission added, *Report Part Default Modifications*, determines if default report part properties can be modified.
  + If default report part properties are set, they will automatically reflect when designing new report parts.
* **New Report Designer Improvements**

  + Data Labels for High Maps
  + RD2 Metrics Option
  + Visibility for overlapping data points
  + RD2 description displayed in report list
* **Zoom Percentage for PDF Exports**

  + New Zoom Percentage property for RD2 Print Layouts allows for more content on a PDF page

## Fixes

| **Defect** | **Description** |
| --- | --- |
| 30125 | Report List drop-downs are not visible when it is the last report in the list |
| 30479 | CSV Export fails for Pivot Grid using group function on date field |
| 30602 | IzendaQuerySource table’s entity columns are not being populated |
| 30605 | Point Options on Maps are not displayed for small report layouts |
| 30614 | Alternative text does not appear in Word Exports |
| 31858 | Alternative text does not appear in PDF Exports |
| 30652 | Subscribe, Email, and Schedule throws error when using Language Packs |
| 30722 | OnPreExecute implementation triggers Save Changes modal in report viewer |
| 30725 | Charts on dashboards do not automatically re-render when updating tile size |
| 30831 | Text containing Less Than operator is not displayed in Excel and Word Exports |
| 30895 | Heat map box colors are not being applied due to Alternative Text configuration |
| 31086 | Performance overhead in POST external/user API endpoint |
| 31350 | Async Export fails when there is no records found in report part |
| 31573 | Report Footer Font properties are not being respected for Word Exports |
| 31626 | Legacy Ciphers are throwing exceptions when using DLLs in custom implementations |
| 31742 | Edit button for RD2 Report Part in Dashboard redirects to Legacy Designer |
| 31755 | Report with Invisible Data Connector does not show expected RD2 Migration message |
| 31760 | RD2 Footer is not visible in the new report viewer |
| 31774 | Print preview popup is not being displayed |
| 31776 | Report with KPI is not being saved after deleting Metric Tile |
| 31854 | RD2 M1S1 displays error when loading large data connectors/sources |
| 31869 | AZSQL data connector displays error after opening report |
| 31908 | Encryption Utility error when using Oracle configuration database |
| 31909 | Cannot provision Oracle configuration database on new instance |
| 31918 | Duplicate scrollbars being displayed in report parts |
| 32954 | Encryption Utility error when updating connection strings and license keys |
| 32978 | Global Category does not appear in RD2 Save As category dropdown |
| 33035 | RD2 Report throws error during Save As for non-system admin users |
| 33132 | Report with Chart, Gauge, and Calculated Field cannot Save As or Copy |

## v5.0 Major Release February 20, 2023

We have released the following enhancements with v5.0:

## Features v5.0

### New Report Designer Improvements

**Cross-Filters**

* Cross-filtering allows users to drill up and down data in multiple report parts. Each drilling action from the user will automatically filter related report parts. Cross-filtering is initiated on charts, gauges, or maps with more than one x-axis field as the drill-down feature of these items triggers the cross-filtering functionality for all other report parts.

**Gauges now support dynamic thresholds.**

* Gauges now support multiple metrics, each with a threshold set by data filed and static values.

**Drill down capabilities**

* Customers can drill down to their visualizations; it's similar functionality to the legacy designer, where clicking on the space or point representing the data will navigate to a lower level of data.

**Report Migration: Classic designer to New Report designer**

* Customer's Legacy reports can be migrated to a new report designer. There are two ways this migration can be leveraged report migration and batch migration.
* Suppose end users have permission to create and modify the reports for new report designers and are owners of the reports. In that case, they can migrate reports simply by clicking migrate option available in the headers.  
  ![](https://devnet.logianalytics.com/hc/article_attachments/12528162284311)

* System admin users can migrate reports in batch migration from the settings tab. System users can filter the reports they like to migrate in batch by Tenant, user, and role.  
  ![](https://devnet.logianalytics.com/hc/article_attachments/12528162291351)

## BREAKING CHANGES v5.0

**Update backend libraries to NET6.**

* Izenda API is now supported on NET6, and customers can refer to the installation documentation to deploy their Izenda instance.
* Izenda API now does not support legacy encryption, so customers need to update the encryption metadata in Izenda Config DB.
* Customers on 4.x.x can leverage upgrade button from the settings tab to update their Izenda config DB.  
  ![](https://devnet.logianalytics.com/hc/article_attachments/12528162305687)
  + Customers on 3.x.x need to use Izenda Encryption Utility to update their Izenda Config DB. The Izenda Encryption utility can be downloaded along with Izenda 5.0.0 release artifacts.  
    ![](https://devnet.logianalytics.com/hc/article_attachments/12528162309655)

**Exporting engine update**

* Izenda has updated the exporting process from the outer source to the inner source using chromium open source.
* Windows servers have no impact, but Linux Servers may need to add supporting libraries/services → [Installation Guide | Configure Exporting](https://insightsoftware.atlassian.net/wiki/spaces/PD/pages/15827075232/Installation+Guide#Configure-Exporting)

**System cache improvements**

* Izenda metadata caching is now leveraging an in-house shared and local version cache system, which replaces DATA storage options for Izenda config DB (Izenda metadata). Data caching has no impact due to this.
* The new caching mechanism is default ON, and customers with web farm env can extend their caching storage using the SharedVersionStorage application.

**IAdHocExtension reference models**

* References to **QuerySource** and **QuerySourceField** should be updated to **LvvQuerySource** and **LvvQuerySourceField** in any custom IAdHocExtension implementations. DLL references should also be updated in any Izenda upgrade.
* **Please see the changes in our CoreIAdHocExtensionSamples for an example of changes required →** [**Izenda Git Hub Samples**](https://github.com/Izenda7Series/CoreIAdHocExtensionSamples/commit/578db7ba9b2af559806cd94b549f38e05b8eceb9)
