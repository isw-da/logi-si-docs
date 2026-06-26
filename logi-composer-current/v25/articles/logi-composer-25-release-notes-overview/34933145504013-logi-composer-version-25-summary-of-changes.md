---
title: "Logi Composer Version 25 Summary of Changes"
id: 34933145504013
section: "Logi Composer  25 Release Notes Overview"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933145504013-Logi-Composer-Version-25-Summary-of-Changes
updated_at: 2026-05-26T22:08:37Z
---

# Logi Composer Version 25 Summary of Changes

# Logi Composer Version 25 Summary of Changes

This is a summary of the major changes made in version 25 of Composer. It is provided so you can quickly identify new and changed Composer features before upgrading from Composer 24 to Composer 25.

Composer is offered on a quarterly release schedule, and our version numbering system reflects this. The current major release of Composer is v25.4.

## Upgrade Considerations

Be sure to back up your metadata store (see [Back Up the Metadata Store](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933195219213-Back-Up-the-Metadata-Store)) before you upgrade.

Upgrading to Logi Composer v23.2 or later includes an upgrade of Java runtime from 11 to 17, installed and configured automatically during upgrade.

**Important:** Before you upgrade to Composer v25.2 you must use a newer version of CentOS than CentOS 7. If you are not using this tool, you can exclude the `sdk-service` when installing or upgrading Composer.

**Note:** CentOS 7 & 8 are end of life (EOL) support. CentOS Stream 9 is supported for new instances of Logi Composer 25.4 and higher. Upgrade your operating system to CentOS Stream 9 before upgrading your Composer instance. For more information, see [Operating System Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/39993525943181-Operating-System-Support).

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

To ensure services start properly after upgrade in a Linux environment:

1. Verify all of your JVM setting overrides are defined in the `/etc/zoomdata` directory (not `/opt/zoomdata/conf`).
2. The `.jvm` files in `/etc/zoomdata/` only contain parameters that are different from default ones, typically Xms/Xms settings, javaagent settings.

   If you have copied the entire `.jvm` file from `/opt/zoomdata/conf` for placement into `/etc/zoomdata`, that configuration is not overwritten after upgrade. Properties such as `XX:+UseConcMarkSweepGC` can prevent services from starting on Java 17 runtime.

For more information on configuration setups and overrides, see [Configure Memory Settings](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932637063437-Configure-Memory-Settings) and [Connector Properties and Property Files](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932637143949-Connector-Properties-and-Property-Files).

**Note:** 
If you are upgrading from an earlier version of Logi Composer, this may be a breaking change: the introduction of the system attribute `User.timeZone` may cause a conflict if you used this as a custom attribute. See [Upgrade Workflow](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932887294349-Timezone-Conversion-for-Users#Upgrade).

## Enhancements

The following sections provide you with a summary of enhancements in the previous releases, all of which are present in the latest release of Logi Composer.

* [v25.4 Enhancements](#V25.4)
* [v25.3 Enhancements](#V25.3)
* [v25.2 Enhancements](#V25.2)
* [v25.1 Enhancements](#V25.1)
* [Removed Features From Logi Composer v24](#Removed)
* [API Updates in Logi Composer v25](#API)

## v25.4 Enhancements

* [Source Creation Redesign](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/41964693319821-Logi-Composer-25-4-Feature-Enhancements#Source)
* [OData Updates](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/41964693319821-Logi-Composer-25-4-Feature-Enhancements#OData)
* [Dashboard and Source Tag Entities](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/41964693319821-Logi-Composer-25-4-Feature-Enhancements#Dashboar)
* [Composer Bill of Materials](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/41964693319821-Logi-Composer-25-4-Feature-Enhancements#Composer)
* [Expanded Aggregate Metric Function Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/41964693319821-Logi-Composer-25-4-Feature-Enhancements#Expanded)
* [Time Bar Settings](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/41964693319821-Logi-Composer-25-4-Feature-Enhancements#Time)
* [Hierarchical Filter State Persistence](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/41964693319821-Logi-Composer-25-4-Feature-Enhancements#Hierarch)

## v25.3 Enhancements

* [Scheduled Dashboard Reports - Tenants](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/39704284909453-Logi-Composer-25-3-Feature-Enhancements#Schedule)
* [User Interface Flexibility](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/39704284909453-Logi-Composer-25-3-Feature-Enhancements#User)
* [Customize Label Color](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/39704284909453-Logi-Composer-25-3-Feature-Enhancements#Customiz)

## v25.2 Enhancements

* [Updated Connector Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#connect)
* [OpenSearch Connector Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#connect2)
* [Dashboard Filtering and Data Refresh Improvements](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#Dashboard)
* [Show and Hide Column Labels](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#Metric)
* [Install / Upgrade Operating System Requirements](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#Install)
* [Free-Form Widget Placement on Dashboards](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#Free-For)
* [Scheduled Dashboard Reports](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#Schedule)
* [Embedded Source Events](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#Embedded)
* [Elasticsearch Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/37515149372941-Logi-Composer-25-2-Feature-Enhancements#elastic)

## v25.1 Enhancements

* [User Interface Simplification and Updates](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933122669837-Logi-Composer-25-1-Feature-Enhancements#User)
* [Data Zoom Scroll Options for Visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933122669837-Logi-Composer-25-1-Feature-Enhancements#Data)
* [OData Enhancements](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933122669837-Logi-Composer-25-1-Feature-Enhancements#OData)
* [Dashboard Authors](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933122669837-Logi-Composer-25-1-Feature-Enhancements#Dashboard)

## Removed Features From Logi Composer v24

The following features were removed from Logi Composer v24 to make way for improvements in Logi Composer v25.

### Logi Composer 25.4

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

### Logi Composer 25.3

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

### Logi Composer 25.2

| Title | Description |
| --- | --- |
| **25.2.10 Removed Features** | |
| None. |  |
| **25.2.9 Removed Features** | |
| None. |  |
| **25.2.8 Removed Features** | |
| None. |  |
| **25.2.7 Removed Features** | |
| None. |  |
| **25.2.6 Removed Features** | |
| None. |  |
| **25.2.5 Removed Features** | |
| None. |  |
| **25.2.4 Removed Features** | |
| None. |  |
| **25.2.3 Removed Features** | |
| None. |  |
| **25.2.2 Removed Features** | |
| None. |  |
| **25.2.1 Removed Features** | |
| None. |  |
| **25.2 Removed Features** | |
| None. |  |

### Logi Composer 25.1

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

## API Updates in Logi Composer v25

This table provides a breakdown of all reported updates in Logi Composer v25.

### Logi Composer 25.4

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

### Logi Composer 25.3

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

### Logi Composer 25.2

| Endpoint | Method | Description |
| --- | --- | --- |
| **25.2.10 API Updates** | | |
| None. |  |  |
| **25.2.9 API Updates** | | |
| None. |  |  |
| **25.2.8 API Updates** | | |
| api/sources/odata/s\_{sourceid} | GET | A new optional query parameter, **number\_format** can now be appended to the url to get the large numeric field values as plain decimals that may, by default, be converted to scientific notation.   * **number\_format=plain** — All scientific notation values are converted to plain decimal format. Double values smaller than 10⁻⁵ will be treated as 0 when using this option. * **number\_format=default** — Values are returned in the existing format. This is the default behavior if the parameter is omitted.   Existing integrations are unaffected. To opt into plain decimal formatting, add **?number\_format=plain** to your OData requests. |
| **25.2.7 API Updates** | | |
| None. |  |  |
| **25.2.6 API Updates** | | |
| None. |  |  |
| **25.2.5 API Updates** | | |
| None. |  |  |
| **25.2.4 API Updates** | | |
| None. |  |  |
| **25.2.3 API Updates** | | |
| None. |  |  |
| **25.2.2 API Updates** | | |
| None. |  |  |
| **25.2.1 API Updates** | | |
| None. |  |  |
| **25.2 API Updates** | | |
| /api/dashboards/{dashboard\_id}/reports/report\_id/  /api/dashboards/{dashboard\_id}/reports | PUT, POST | You can now add a `destinationType` of `EMAIL` or `FILE_DROP` to support SFTP and SMTP dispatch of scheduled dashboard reports. |

### Logi Composer 25.1

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
