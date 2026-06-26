---
title: "Logi Composer Version 26 Summary of Changes"
id: 43701192423949
section: "Logi Composer  26 Release Notes Overview"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701192423949-Logi-Composer-Version-26-Summary-of-Changes
updated_at: 2026-05-29T14:09:22Z
---

# Logi Composer Version 26 Summary of Changes

# Logi Composer Version 26 Summary of Changes

This is a summary of the major changes made in version 25 of Composer. It is provided so you can quickly identify new and changed Composer features before upgrading from Composer 25 to Composer 26.

Composer is offered on a quarterly release schedule, and our version numbering system reflects this. The current major release of Composer is v26.1.

## Upgrade Considerations

Be sure to back up your metadata store (see [Back Up the Metadata Store](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701164946317-Back-Up-the-Metadata-Store)) before you upgrade.

Upgrading to Logi Composer v23.2 or later includes an upgrade of Java runtime from 11 to 17, installed and configured automatically during upgrade.

**Important:** Before you upgrade to Composer v25.2 or later you must use a newer version of CentOS than CentOS 7 or CentOS 8. If you are not using this tool, you can exclude the `sdk-service` when installing or upgrading Composer v24.

**Note:** CentOS 7 & 8 are end of life (EOL) support. CentOS Stream 9 is supported for new instances of Logi Composer 25.4 and higher. Upgrade your operating system to CentOS Stream 9 before upgrading your Composer instance. For more information, see [Operating System Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136004365-Operating-System-Support).

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

To ensure services start properly after upgrade in a Linux environment:

1. Verify all of your JVM setting overrides are defined in the `/etc/zoomdata` directory (not `/opt/zoomdata/conf`).
2. The `.jvm` files in `/etc/zoomdata/` only contain parameters that are different from default ones, typically Xms/Xms settings, javaagent settings.

   If you have copied the entire `.jvm` file from `/opt/zoomdata/conf` for placement into `/etc/zoomdata`, that configuration is not overwritten after upgrade. Properties such as `XX:+UseConcMarkSweepGC` can prevent services from starting on Java 17 runtime.

For more information on configuration setups and overrides, see [Configure Memory Settings](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701040681613-Configure-Memory-Settings) and [Connector Properties and Property Files](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700992050061-Connector-Properties-and-Property-Files).

**Note:** 
If you are upgrading from an earlier version of Logi Composer, this may be a breaking change: the introduction of the system attribute `User.timeZone` may cause a conflict if you used this as a custom attribute. See [Upgrade Workflow](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068707725-Timezone-Conversion-for-Users#Upgrade).

## Enhancements

The following sections provide you with a summary of enhancements in the previous releases, all of which are present in the latest release of Logi Composer.

* [v26.1 Enhancements](#q1)
* [Removed Features From Logi Composer v25](#Removed)
* [API Updates in Logi Composer v26](#API)

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

The following features were removed from Logi Composer v24 to make way for improvements in Logi Composer v25.

### Logi Composer 26.1

| Title | Description |
| --- | --- |
| **26.1.2 Removed Features** | |
| None. |  |
| **26.1.1 Removed Features** | |
| None. |  |
| **26.1 Removed Features** | |
| None. |  |

## API Updates in Logi Composer v26

This table provides a breakdown of all reported updates in Logi Composer v26.

### Logi Composer 26.1

| Endpoint | Method | Description |
| --- | --- | --- |
| **26.1.2 API Updates** | | |
| None. |  |  |
| **26.1.1 API Updates** | | |
| None. |  |  |
| **26.1 API Updates** | | |
| api/dashboards/ | GET | The GET api/dashboards/ endpoint now returns the creator's full name as **creatorFullName**. |
