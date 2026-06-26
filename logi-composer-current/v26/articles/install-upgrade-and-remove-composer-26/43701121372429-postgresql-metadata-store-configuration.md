---
title: "PostgreSQL\u00a0Metadata Store Configuration"
id: 43701121372429
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701121372429-PostgreSQL-Metadata-Store-Configuration
updated_at: 2026-05-29T14:08:56Z
---

# PostgreSQL Metadata Store Configuration

# PostgreSQL Metadata Store Configuration

* [Internal PostgreSQL Metadata Store](#Internal)

  + [Configuring Credentials](#Configur)
  + [Reusing Existing Internal Metadata Database for New Release](#Reusing)
* [External PostgreSQL Metadata Store](#External)

Composer stores its metadata in a PostgreSQL database. The Helm chart lets you customize the location of the metadata store database. You have two options:

* Default: The chart installs an *internal* instance of PostgreSQL.
* Recommended: Point Composer to an *external*, managed instance of PostgreSQL.

## Internal PostgreSQL Metadata Store

### Configuring Credentials

The default chart config is supplied with the hardcoded database username and password to simplify the initial installation of the chart:

defaultDbUsername: "zoomdata"
defaultDbPassword: "ChangeMe12345"

**Important:** 
Change the username and password for your production release if you choose to use the internal PostgreSQL instance.

### Reusing Existing Internal Metadata Database for New Release

The usage of an *internal* instance of PostgreSQL will create a PersistentVolumeClaim (PVC) and corresponding PervistentVolume (PV) with the PostgreSQL data dir folder. Uninstalling such a chart will keep these PVC and PV so that you can re-use the metadata for another release. The usual name of the PVC is a name such as `data-<release-name>-postgresql-0`. To reuse the metadata:

1. Add the following config to your `values.yaml` to point a new release to the existing PVC:

   postgresql:
   primary:
   persistence:
   existingClaim=data-<release-name>-postgresql-0
2. Install or upgrade the Helm chart.

## External PostgreSQL Metadata Store

To configure the chart to use an *external* PostgreSQL-compatible database system:

1. Disable the creation of the built-in PostgreSQL instance by adding this config to your `values.yaml`.

   postgresql:
   enabled: false
2. Create the next databases in your database system.

   zoomdata
   zoomdata-upload
   zoomdata-keyset
   zoomdata-user-auditing
   zoomdata-qe

   We recommend that you also create a separate PostgreSQL user for Composer databases. See [Create the Metadata Store User & Stores](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134856333-Create-the-Metadata-Store-User-Stores).
3. Define the following Helm chart parameters in your `values.yaml` and set them according to your database setup.

   zoomdataWeb:
   metadataDbUrl: ""
   metadataDbUsername: ""
   metadataDbPassword: ""
   uploadDbUrl: ""
   uploadDbUsername: ""
   uploadDbPassword: ""
   keysetDbUrl: ""
   keysetDbUsername: ""
   keysetDbPassword: ""
   userAuditingDbUrl: ""
   userAuditingDbUsername: ""
   userAuditingDbPassword: ""
   queryEngine:
   dbUrl: ""
   dbUsername: ""
   dbPassword: ""

   If you only define a single user, then you can skip individual `*DbUsername` and `*DbPassword` parameters and set only the following two defaults.

   defaultDbUsername: ""
   defaultDbPassword: ""
4. Install or upgrade the Helm chart.

**Note:** 
Find more information about Composer and Kubernetes here: [Running Composer in Kubernetes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701110924173-Running-Composer-in-Kubernetes).
