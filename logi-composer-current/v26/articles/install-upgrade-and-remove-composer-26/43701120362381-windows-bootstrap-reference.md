---
title: "Windows Bootstrap Reference"
id: 43701120362381
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120362381-Windows-Bootstrap-Reference
updated_at: 2026-05-29T14:08:45Z
---

# Windows Bootstrap Reference

# Windows Bootstrap Reference

The Windows bootstrap installation script installs, by default, these components for Composer:

Composer core components:

* Zoomdata web application
* Query Engine
* Consul

Mandatory dependencies:

* Corretto JDK17
* PostgreSQL 12 or 16

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

Other components:

* MSSQL
* Mongo DB
* Elastic 7
* Solr
* Cloudera Search
* Chocolatey

Add or remove other components or adjust optional components using bootstrap switches. For further help with the bootstrap script, run `Get-Help ./bootstrap-composer.ps1` for syntax help or `Get-Help ./bootstrap-composer.ps1 -Full` for extended parameter help.

**Important:** 
When you upgrade Composer, all services are stopped before the upgrade is installed, and can't be accessed by users until the upgrade is complete and services restarted.

## Installation Parameters

| Parameter | Description | Notes |
| --- | --- | --- |
| `-InstallDestinationPath` | The path to install Composer files. |  |
| `-ComposerVersion` | The version of Composer to install. | `latest` Install the most recent version of Composer available.  `X.x` Install the most recent version of Composer available for that trunk line (for example, `25.4`.  `X.x.x` Install the exact patch version of Composer specified (for example, `25.4.1`. |
| `-ComposerRepository` | The repository to connect to for installation manifests and binary packages for Composer. | Official Composer repository: `<https://composer-repo.logianalytics.com`. |
| `-ConnectorsList` | A comma separated list of connectors to install. | By default, MSSQL, PostgreSQL, MongoDB, Elasticsearch 7.0, Apache Solr, and Cloudera Search are installed if you make no changes to the initial script.  If you include connectors with this parameter, only those connectors are installed. Include the default connectors to install those as well.  If you run the script with new connectors added using this parameter, the new connectors included are added to the existing installed connectors.  See [Data Connector Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113495693-Data-Connector-Reference). |
| `-AdditionalComponentsList` | A comma separated list of additional services to install. | Include one or more of the following services. By default, all are included if you make no changes to the initial script.   * data-writer-mssql * data-writer-postgresql * screenshot-service * zoomdata-admin-server * zoomdata-config-server   If you install the screenshot-service, Google Chrome and the Chrome driver are installed as well. |
| `-PostgreSQLHost` | The hostname or IP adddress of your external PostgreSQL server (configured for Composer metadata storage). | By default, `localhost`, which installs a new instance of PostgreSQL.   * PostgreSQL 12 for version 24.2 and earlier * PostgreSQL 16 for version 24.3 and later |
| `-PostgreSQLTCP` | The TCP port of your external PostgreSQL server (configured for Composer metadata storage). |  |
| `-PostgreSQLUser` | The PostgreSQL user name configured as owner of your Composer database. |  |
| `-PostgreSQLPass` | The PostgreSQL password for the user configured as owner of your Composer database. |  |
| `-ServicesAction` | Manage Windows services for Composer. You can perform this without performing other bootstrap activities. | Use on one or more services as needed. Actions include:   * install * start * stop * restart * status * uninstall |
| `-SkipDependenciesInstall` | Set to skip installing Composer dependencies. | * Chocolatey * PostgreSQL 12 or PostgreSQL 16 * Google Chrome * Google Chrome Driver |
| `-SkipComposerInstall` | Set to skip installing Composer services. | Download, extract, and configure actions are the only actions performed. |
| `-SkipComposerConfigure` | Set to skip configuring Composer services. | Download, extract, and install actions are the only actions performed. |
| `-SkipComposerStart` | Set to perform all installation actions, but do not start Composer services. |  |
| `-SkipMetadataDumpOnUpgrade` | Set to disable automatic metadata dumping during upgrade or installation of Composer services. |  |
| `-DumpComposerMetadata` | This is a separate action to perform a metadata dump. You must stop all services first to ensure consistency. | After stopping all services, you can perform this without performing other bootstrap activities. |
| `-DeinstallComposer` | Completely remove all Composer components and dependencies from this instance. |  |
| `-PreDownloadedPackagesPath` | Set to install Composer binaries from the defined path instead of downloading from the Composer repository. | The folder you point to must include all core components, required connectors, and additional services. |
| `-BootstrapLogFile` | Set to define an alternative path to record the bootstrap logs. | By default, the log file is put in the same folder you use to launch the bootstrap script. |

**Note:** 
Manual install of Composer is not currently supported for Windows environments.

See
[Post-Installation Options](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072984717-Post-Installation-Options) for more information and links to instructions.

## Installation Examples

Install the most recent rapid release version of Composer and PostgreSQL as a dependency. Includes Impala and MSSQL EDC connectors and the MSSQL-based data writer service to `c:\logi-composer`. All components are started after installation.

./bootstrap-composer.ps1 -ComposerVersion latest -ConnectorsList impala,mssql -AdditionalComponentsList data-writer-mssql

Install only core components (Consul, Composer Server, Query Engine) of the most recent released Composer version in the 7.10 trunk. Default EDC connectors are installed (MSSQL, PostgreSQL, Mongo DB, Elastic 7, Solr, Cloudera Search).

./bootstrap-composer.ps1 -ComposerVersion 25.4

Install the most recent published long term support version of Composer. Do not start services.

./bootstrap-composer.ps1 -ComposerVersion latest-lts -SkipComposerStart
