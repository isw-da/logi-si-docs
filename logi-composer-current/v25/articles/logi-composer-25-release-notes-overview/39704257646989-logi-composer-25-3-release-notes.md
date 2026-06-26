---
title: "Logi Composer 25.3 Release Notes"
id: 39704257646989
section: "Logi Composer  25 Release Notes Overview"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/39704257646989-Logi-Composer-25-3-Release-Notes
updated_at: 2026-05-26T22:10:34Z
---

# Logi Composer 25.3 Release Notes

# Logi Composer 25.3 Release Notes

This topic describes feature enhancements, resolved issues, and important information for Composer 25.3.

To purchase this product, contact [insightsoftware Sales](mailto:loginewbusinessteam@insightsoftware.com?subject=I%20am%20interested%20in%20purchasing%20this%20product,%20please%20contact%20me. "Sales email address.").

* [Feature Enhancements](#Feature "Feature Enahncements section")
* [Operating System Support](#OS)
* [API Updates](#API_Updates "API Updates section")
* [Resolved Issues](#Resolved)
* [Deprecated Features](#Deprecated_Features)
* [Removed Features](#Removed_Features)

See also [Important Notices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933115853197-Important-Notices), [Deprecated Features](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933137766029-Deprecated-Features), and [Logi Composer Version 25 Summary of Changes](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933145504013-Logi-Composer-Version-25-Summary-of-Changes).

Composer is offered on a quarterly release schedule. The current major release of Composer is v25.3.

## Feature Enhancements

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
| [Scheduled Dashboard Reports - Tenants](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/39704284909453-Logi-Composer-25-3-Feature-Enhancements#Schedule) | Users with appropriate permissions can specify a "Reply-To" and "Sender Display Name" for the emails generated for your scheduled dashboard reports.  This flexibility allows you to direct replies to your selected recipient and include a user-friendly sender display name for ease of use by your end users. If not defined, this defaults to the system values.  Additionally, the Accounts API has been updated so you can retrieve and define all tenant configuration information, including SFTP file drop and STMP details.  See [API Updates](#API_Updates). |
| [User Interface Flexibility](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/39704284909453-Logi-Composer-25-3-Feature-Enhancements#User) | We have introduced a number of flexible improvements to the user interface. When you work in some pop-up modals, you can resize some common columns to see more of the information about the resources you are using. Use your cursor to grab a column header break to adjust as needed.  These pop-ups include Dashboard Alerts, Dashboard Sharing, and Permissions for Sources, Visuals, and Dashboards. |
| [Customize Label Color](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/39704284909453-Logi-Composer-25-3-Feature-Enhancements#Customiz) | You can now customize the label color for the combo chart visual in Composer if you do not want to use the themed color. Disable **Inherit from theme** in the Colors sidebar menu, then select the color you wish to use. |

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
| **25.3.7 API Updates** | | |
| None. |  |  |
| **25.3.6 API Updates** | | |
| None. |  |  |
| **25.3.5 API Updates** | | |
| api/sources/odata/s\_{sourceid} | GET | A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.   * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option. * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.   Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests. |
| **25.3.4 API Updates** | | |
| None. |  |  |
| **25.3.3 API Updates** | | |
| None. |  |  |
| **25.3.2 API Updates** | | |
| None. |  |  |
| **25.3.1 API Updates** | | |
| None. |  |  |
| **25.3 API Updates** | | |
| api/accounts/{id}  api/accounts  api/accounts/name/{name} | GET, POST, PUT | Use the updated Accounts API to retrieve or define all tenant configuration information, or specific information, such as tenant-level information related to SFTP and SMTP configuration details as needed.  Reserved attributes include:   * sftp.host * sftp.password * sftp.port * sftp.remoteDirectory * sftp.strictHostKeyChecking * sftp.user * email.replyToAddress * email.senderDisplayName |
| api/accounts/{id}  api/accounts | POST, PUT | Users with appropriate permissions to create accounts (tenants) can define a "Reply-To" and "Sender Display Name" for the emails generated to send scheduled dashboard reports. Users with appropriate permissions to update accounts (tenants) can define these attributes for specific accounts (tenants).  Attributes:   * email.replyToAddress * email.senderDisplayName |

## Resolved Issues

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
| Embed Visual Event Trigger | A new setting, `fireOnEveryChange`, is now available for embedded dashboards. Disabled by default, enabling this makes it easier for you to track and respond to all user interactions within a dashboard.  When enabled, dashboards send out change events (`dashboard-level`/`visual-level updates`) every time something is modified: sorting, filtering, visual settings, and more. This gives you more granular visibility into user actions.  When disabled, events were are only triggered once for `dashboard-level`/`visual-level changes`.  Enable in the embed SDK configuration. See [Embedded Events](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932937400973-Embedded-Events). |
| Consul Updates | Consol has been upgraded to version 1.22.1. |
| **25.3.3 Resolved Issues** | |
| Time Bar Settings | You can now enable a time bar option in your environment that allows the time bar slider to snap to the closest interval of the defined granularity for a specific source. This is disabled by default: enable the new server-level variable, **timebar-snap-to-interval** to use in your environment.  See [Server-Level Variables](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932636844045-Server-Level-Variables). |
| US Region Maps | Corrected an issue that prevented display of a US Region Map visual to which a new data column had been added. |
| **25.3.2 Resolved Issues** | |
| Updates | This service pack includes various internal fixes. |
| **25.3.1 Resolved Issues** | |
| Time Bar | By default, the Time Bar will display time information as presented in the associated data source with no offsets or bounds to the time field. If you are using UTC, this is indicated in the time bar. If the time is derived based on other settings, this is indicated in the time bar. |
| Source Selection - Creating Visuals | Corrected an issue that prevented display of source names during visual creation. |
| API Update | Corrected an issue that did not return multiple data type options for aggregation functions such as `LAST_VALUE` from `api/sources/<sourceid>/expression-syntax`. |
| **25.3 Resolved Issues** | |
| None. |  |

## Deprecated Features

| Title | Description |
| --- | --- |
| **25.3.7 Deprecated Features** | |
| None. |  |
| **25.3.6 Deprecated Features** | |
| None. |  |
| **25.3.5 Deprecated Features** | |
| None. |  |
| **25.3.4 Deprecated Features** | |
| None. |  |
| **25.3.3 Deprecated Features** | |
| None. |  |
| **25.3.2 Deprecated Features** | |
| None. |  |
| **25.3.1 Deprecated Features** | |
| None. |  |
| **25.3 Deprecated Features** | |
| None. |  |

## Removed Features

| Title | Description |
| --- | --- |
| **25.3.7 Removed Features** | |
| None. |  |
| **25.3.6 Removed Features** | |
| None. |  |
| **25.3.5 Removed Features** | |
| None. |  |
| **25.3.4 Removed Features** | |
| None. |  |
| **25.3.3 Removed Features** | |
| None. |  |
| **25.3.2 Removed Features** | |
| None. |  |
| **25.3.1 Removed Features** | |
| None. |  |
| **25.3 Removed Features** | |
| None. |  |

## Known Issues

| Affected Releases | Description |
| --- | --- |
| **Logi Composer 25.3** and later | None. |
