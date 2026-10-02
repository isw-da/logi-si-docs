> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Install Self-Service Analytics - Windows

## Windows Environment

This section provides instructions for performing a clean installation of Self-Service Analytics in your Windows Server environment.

For information about the difference between a clean installation of Self-Service Analytics and an upgrade to the latest GA release, see [Clean Installation and Upgrade Differences](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#clean-installation-and-upgrade-differences).

### Upgrade and Migration Considerations

* Windows Server 2012R2 is not compatible with both Java17 binaries and the latest releases of Self-Service Analytics. We recommend you use Windows 2019 or later.
* In general, you can upgrade directly to the latest version of Self-Service Analytics from a prior version of Composer.
* If you are upgrading to a newer version of Self-Service Analytics and you also want to change your encryption mode, perform the upgrade first and then complete the steps described in [Encryption](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/changing-encryption-mode).

<Note>
  New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

<Warning>
  If you are upgrading to a newer version of Self-Service Analytics and have created an attribute named `User.timeZone`, this may be overwritten on upgrade. See [Upgrade Workflow](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#upgrade-workflow) for more information about preparing your environment for the upgrade process.
</Warning>

In general, the installation process is automated and you only need to run an installation script. The installation script is implemented using Bootstrap. This script accesses a dedicated Self-Service Analytics repository and automatically downloads all the necessary components to install your Self-Service Analytics microservice.

By default, the bootstrap script installs these core components, connectors, and required dependencies:

* Zoomdata web application
* Query Engine
* MSSQL
* Mongo DB
* Elastic 7
* Solr
* Cloudera Search
* Consul
* PostgreSQL 16
* Corretto JDK17
* Chocolatey

To install other components, adjust bootstrap switches as needed. See [Windows Bootstrap Reference](#windows-bootstrap-reference), [Self-Service Analytics Microservice Name Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-analytics-microservice-name-reference) and [Data Connector Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference).

After the installation has completed, you need to activate the Self-Service Analytics microservices, download and configure a JDBC driver if you are using specific data sources (see [Post-Installation Options](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#post-installation-options) for a list), and open a browser window and enter the specific IP address to access the Self-Service Analytics client.

Review and complete (as appropriate for your installation) the following installation information:

* [Plan Your Installation](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites)
* [Installation Steps](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#installation-steps)
* [Post-Installation Options](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#post-installation-options)
* [Access and Use Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access)

<h2 id="windows-bootstrap-reference">
  Windows Bootstrap Reference
</h2>

The Windows bootstrap installation script installs, by default, these components for Self-Service Analytics:

Core components:

* Zoomdata web application
* Query Engine
* Consul

Mandatory dependencies:

* Corretto JDK17
* PostgreSQL 16

<Note>
  New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

Other components:

* MSSQL
* Mongo DB
* Elastic 7
* Solr
* Cloudera Search
* Chocolatey

Add or remove other components or adjust optional components using bootstrap switches. For further help with the bootstrap script, run `Get-Help ./bootstrap-composer.ps1` for syntax help or `Get-Help ./bootstrap-composer.ps1 -Full` for extended parameter help.

<Warning>
  When you upgrade Self-Service Analytics, all services are stopped before the upgrade is installed, and can not be accessed by users until the upgrade is complete and services restarted.
</Warning>

<h3 id="windows-bootstrap-reference-installation-parameters">
  Installation Parameters
</h3>

<table>
  <thead>
    <tr>
      <th scope="col">Parameter</th>
      <th>Description</th>
      <th>Notes</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`-InstallDestinationPath`</td>
      <td>The path to install Self-Service Analytics files.</td>

      <td />
    </tr>

    <tr>
      <td>`-ComposerVersion`</td>
      <td>The version of Self-Service Analytics to install.</td>

      <td>
        `latest` Install the most recent version of Self-Service Analytics available.

        <br />

        `X.x` Install the most recent version of Self-Service Analytics available for that trunk line (for example, `26.3`.

        <br />

        `X.x.x` Install the exact patch version of Self-Service Analytics specified (for example, `26.3.1`.
      </td>
    </tr>

    <tr>
      <td>`-ComposerRepository`</td>
      <td>The repository to connect to for installation manifests and binary packages for Self-Service Analytics.</td>
      <td>Official Self-Service Analytics repository: `<https://composer-repo.logianalytics.com`.</td>
    </tr>

    <tr>
      <td>`-ConnectorsList`</td>
      <td>A comma separated list of connectors to install.</td>

      <td>
        By default, MSSQL, PostgreSQL, MongoDB, Elasticsearch 7.0, Apache Solr, and Cloudera Search are installed if you make no changes to the initial script.

        <br />

        If you include connectors with this parameter, only those connectors are installed. Include the default connectors to install those as well.

        <br />

        If you run the script with new connectors added using this parameter, the new connectors included are added to the existing installed connectors.

        <br />

        See [Data Connector Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference).
      </td>
    </tr>

    <tr>
      <td>`-AdditionalComponentsList`</td>
      <td>A comma separated list of additional services to install.</td>

      <td>
        Include one or more of the following services. By default, all are included if you make no changes to the initial script.

        <br />

        * data-writer-mssql
        * data-writer-postgresql
        * screenshot-service
        * zoomdata-admin-server
        * zoomdata-config-server

        <br />

        If you install the screenshot-service, Google Chrome and the Chrome driver are installed as well.
      </td>
    </tr>

    <tr>
      <td>`-PostgreSQLHost`</td>
      <td>The hostname or IP address of your external PostgreSQL server (configured for Self-Service Analytics metadata storage).</td>

      <td>
        By default, `localhost`, which installs a new instance of PostgreSQL.

        <br />

        * PostgreSQL 16 for version 26.3 and later
      </td>
    </tr>

    <tr>
      <td>`-PostgreSQLTCP`</td>
      <td>The TCP port of your external PostgreSQL server (configured for Self-Service Analytics metadata storage).</td>

      <td />
    </tr>

    <tr>
      <td>`-PostgreSQLUser`</td>
      <td>The PostgreSQL user name configured as owner of your Composer database.</td>

      <td />
    </tr>

    <tr>
      <td>`-PostgreSQLPass`</td>
      <td>The PostgreSQL password for the user configured as owner of your Composer database.</td>

      <td />
    </tr>

    <tr>
      <td>`-ServicesAction`</td>
      <td>Manage Windows services for Self-Service Analytics. You can perform this without performing other bootstrap activities.</td>

      <td>
        Use on one or more services as needed. Actions include:

        <br />

        * install
        * start
        * stop
        * restart
        * status
        * uninstall
      </td>
    </tr>

    <tr>
      <td>`-SkipDependenciesInstall`</td>
      <td>Set to skip installing Self-Service Analytics dependencies.</td>

      <td>
        * Chocolatey
        * PostgreSQL 16
        * Google Chrome
        * Google Chrome Driver
      </td>
    </tr>

    <tr>
      <td>`-SkipComposerInstall`</td>
      <td>Set to skip installing Self-Service Analytics services.</td>
      <td>Download, extract, and configure actions are the only actions performed.</td>
    </tr>

    <tr>
      <td>`-SkipComposerConfigure`</td>
      <td>Set to skip configuring Self-Service Analytics services.</td>
      <td>Download, extract, and install actions are the only actions performed.</td>
    </tr>

    <tr>
      <td>`-SkipComposerStart`</td>
      <td>Set to perform all installation actions, but do not start Self-Service Analytics services.</td>

      <td />
    </tr>

    <tr>
      <td>`-SkipMetadataDumpOnUpgrade`</td>
      <td>Set to disable automatic metadata dumping during upgrade or installation of Self-Service Analytics services.</td>

      <td />
    </tr>

    <tr>
      <td>`-DumpComposerMetadata`</td>
      <td>This is a separate action to perform a metadata dump. You must stop all services first to ensure consistency.</td>
      <td>After stopping all services, you can perform this without performing other bootstrap activities.</td>
    </tr>

    <tr>
      <td>`-DeinstallComposer`</td>
      <td>Completely remove all Self-Service Analytics components and dependencies from this instance.</td>

      <td />
    </tr>

    <tr>
      <td>`-PreDownloadedPackagesPath`</td>
      <td>Set to install Self-Service Analytics binaries from the defined path instead of downloading from the Self-Service Analytics repository.</td>
      <td>The folder you point to must include all core components, required connectors, and additional services.</td>
    </tr>

    <tr>
      <td>`-BootstrapLogFile`</td>
      <td>Set to define an alternative path to record the bootstrap logs.</td>
      <td>By default, the log file is put in the same folder you use to launch the bootstrap script.</td>
    </tr>
  </tbody>
</table>

<Note>
  Manual install of Self-Service Analytics is not currently supported for Windows environments.
</Note>

See [Post-Installation Options](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#post-installation-options) for more information and links to instructions.

<h3 id="windows-bootstrap-reference-installation-examples">
  Installation Examples
</h3>

Install the most recent rapid release version of Self-Service Analytics and PostgreSQL as a dependency. Includes Impala and MSSQL EDC connectors and the MSSQL-based data writer service to `c:\logi-composer`. All components are started after installation.

```bash theme={null}
./bootstrap-composer.ps1 -ComposerVersion latest -ConnectorsList impala,mssql -AdditionalComponentsList data-writer-mssql
```

Install only core components (Consul, Self-Service Analytics Server, Query Engine) of the most recent released Self-Service Analytics version in the 26.3 trunk. Default EDC connectors are installed (MSSQL, PostgreSQL, Mongo DB, Elastic 7, Solr, Cloudera Search).

```bash theme={null}
./bootstrap-composer.ps1 -ComposerVersion 26.3
```

Install the most recent published long term support version of Self-Service Analytics. Do not start services.

```bash theme={null}
./bootstrap-composer.ps1 -ComposerVersion latest-lts -SkipComposerStart
```

<h2 id="windows-bootstrap-reference-2">
  Windows Bootstrap Reference
</h2>

The Windows bootstrap installation script installs, by default, these components for Self-Service Analytics:

Core components:

* Zoomdata web application
* Query Engine
* Consul

Mandatory dependencies:

* Corretto JDK17
* PostgreSQL 16

<Note>
  New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

Other components:

* MSSQL
* Mongo DB
* Elastic 7
* Solr
* Cloudera Search
* Chocolatey

Add or remove other components or adjust optional components using bootstrap switches. For further help with the bootstrap script, run `Get-Help ./bootstrap-composer.ps1` for syntax help or `Get-Help ./bootstrap-composer.ps1 -Full` for extended parameter help.

<Warning>
  When you upgrade Self-Service Analytics, all services are stopped before the upgrade is installed, and can not be accessed by users until the upgrade is complete and services restarted.
</Warning>

<h3 id="windows-bootstrap-reference-2-installation-parameters">
  Installation Parameters
</h3>

<table>
  <thead>
    <tr>
      <th scope="col">Parameter</th>
      <th>Description</th>
      <th>Notes</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>`-InstallDestinationPath`</td>
      <td>The path to install Self-Service Analytics files.</td>

      <td />
    </tr>

    <tr>
      <td>`-ComposerVersion`</td>
      <td>The version of Self-Service Analytics to install.</td>

      <td>
        `latest` Install the most recent version of Self-Service Analytics available.

        <br />

        `X.x` Install the most recent version of Self-Service Analytics available for that trunk line (for example, `26.3`.

        <br />

        `X.x.x` Install the exact patch version of Self-Service Analytics specified (for example, `26.3.1`.
      </td>
    </tr>

    <tr>
      <td>`-ComposerRepository`</td>
      <td>The repository to connect to for installation manifests and binary packages for Self-Service Analytics.</td>
      <td>Official Self-Service Analytics repository: `<https://composer-repo.logianalytics.com`.</td>
    </tr>

    <tr>
      <td>`-ConnectorsList`</td>
      <td>A comma separated list of connectors to install.</td>

      <td>
        By default, MSSQL, PostgreSQL, MongoDB, Elasticsearch 7.0, Apache Solr, and Cloudera Search are installed if you make no changes to the initial script.

        <br />

        If you include connectors with this parameter, only those connectors are installed. Include the default connectors to install those as well.

        <br />

        If you run the script with new connectors added using this parameter, the new connectors included are added to the existing installed connectors.

        <br />

        See [Data Connector Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference).
      </td>
    </tr>

    <tr>
      <td>`-AdditionalComponentsList`</td>
      <td>A comma separated list of additional services to install.</td>

      <td>
        Include one or more of the following services. By default, all are included if you make no changes to the initial script.

        <br />

        * data-writer-mssql
        * data-writer-postgresql
        * screenshot-service
        * zoomdata-admin-server
        * zoomdata-config-server

        <br />

        If you install the screenshot-service, Google Chrome and the Chrome driver are installed as well.
      </td>
    </tr>

    <tr>
      <td>`-PostgreSQLHost`</td>
      <td>The hostname or IP address of your external PostgreSQL server (configured for Self-Service Analytics metadata storage).</td>

      <td>
        By default, `localhost`, which installs a new instance of PostgreSQL.

        <br />

        * PostgreSQL 16 for version 26.3 and later
      </td>
    </tr>

    <tr>
      <td>`-PostgreSQLTCP`</td>
      <td>The TCP port of your external PostgreSQL server (configured for Self-Service Analytics metadata storage).</td>

      <td />
    </tr>

    <tr>
      <td>`-PostgreSQLUser`</td>
      <td>The PostgreSQL user name configured as owner of your Composer database.</td>

      <td />
    </tr>

    <tr>
      <td>`-PostgreSQLPass`</td>
      <td>The PostgreSQL password for the user configured as owner of your Composer database.</td>

      <td />
    </tr>

    <tr>
      <td>`-ServicesAction`</td>
      <td>Manage Windows services for Self-Service Analytics. You can perform this without performing other bootstrap activities.</td>

      <td>
        Use on one or more services as needed. Actions include:

        <br />

        * install
        * start
        * stop
        * restart
        * status
        * uninstall
      </td>
    </tr>

    <tr>
      <td>`-SkipDependenciesInstall`</td>
      <td>Set to skip installing Self-Service Analytics dependencies.</td>

      <td>
        * Chocolatey
        * PostgreSQL 16
        * Google Chrome
        * Google Chrome Driver
      </td>
    </tr>

    <tr>
      <td>`-SkipComposerInstall`</td>
      <td>Set to skip installing Self-Service Analytics services.</td>
      <td>Download, extract, and configure actions are the only actions performed.</td>
    </tr>

    <tr>
      <td>`-SkipComposerConfigure`</td>
      <td>Set to skip configuring Self-Service Analytics services.</td>
      <td>Download, extract, and install actions are the only actions performed.</td>
    </tr>

    <tr>
      <td>`-SkipComposerStart`</td>
      <td>Set to perform all installation actions, but do not start Self-Service Analytics services.</td>

      <td />
    </tr>

    <tr>
      <td>`-SkipMetadataDumpOnUpgrade`</td>
      <td>Set to disable automatic metadata dumping during upgrade or installation of Self-Service Analytics services.</td>

      <td />
    </tr>

    <tr>
      <td>`-DumpComposerMetadata`</td>
      <td>This is a separate action to perform a metadata dump. You must stop all services first to ensure consistency.</td>
      <td>After stopping all services, you can perform this without performing other bootstrap activities.</td>
    </tr>

    <tr>
      <td>`-DeinstallComposer`</td>
      <td>Completely remove all Self-Service Analytics components and dependencies from this instance.</td>

      <td />
    </tr>

    <tr>
      <td>`-PreDownloadedPackagesPath`</td>
      <td>Set to install Self-Service Analytics binaries from the defined path instead of downloading from the Self-Service Analytics repository.</td>
      <td>The folder you point to must include all core components, required connectors, and additional services.</td>
    </tr>

    <tr>
      <td>`-BootstrapLogFile`</td>
      <td>Set to define an alternative path to record the bootstrap logs.</td>
      <td>By default, the log file is put in the same folder you use to launch the bootstrap script.</td>
    </tr>
  </tbody>
</table>

<Note>
  Manual install of Self-Service Analytics is not currently supported for Windows environments.
</Note>

See [Post-Installation Options](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#post-installation-options) for more information and links to instructions.

<h3 id="windows-bootstrap-reference-2-installation-examples">
  Installation Examples
</h3>

Install the most recent rapid release version of Self-Service Analytics and PostgreSQL as a dependency. Includes Impala and MSSQL EDC connectors and the MSSQL-based data writer service to `c:\logi-composer`. All components are started after installation.

```bash theme={null}
./bootstrap-composer.ps1 -ComposerVersion latest -ConnectorsList impala,mssql -AdditionalComponentsList data-writer-mssql
```

Install only core components (Consul, Self-Service Analytics Server, Query Engine) of the most recent released Self-Service Analytics version in the 26.3 trunk. Default EDC connectors are installed (MSSQL, PostgreSQL, Mongo DB, Elastic 7, Solr, Cloudera Search).

```bash theme={null}
./bootstrap-composer.ps1 -ComposerVersion 26.3
```

Install the most recent published long term support version of Self-Service Analytics. Do not start services.

```bash theme={null}
./bootstrap-composer.ps1 -ComposerVersion latest-lts -SkipComposerStart
```
