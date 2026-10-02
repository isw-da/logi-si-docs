> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Plan Your Installation

## Installation Prerequisites

The installation script works in the following environments:

* RHEL 9 (Red Hat)

* CentOS Stream 9

* Ubuntu 22.04

  <Note>
    Older versions of Ubuntu are nearing end of life (EOL) support. Self-Service Analytics 26.3 and later will require an operating system upgrade before you upgrade your instance.
  </Note>

* Windows Server version 2019 or higher.

<Danger>
  If your operating system has reached or will soon reach its EOL date, insightsoftware recommends you schedule an appropriate time to upgrade both the Self-Service Analytics and operating system to a later version. For more information, see [Operating System Support](#operating-system-support).
</Danger>

For more information, see [Supported Technologies Reference](#supported-technologies-reference).

<h4 id="installation-prerequisites-upgrade-and-migration-considerations">
  Upgrade and Migration Considerations
</h4>

* Windows Server 2012R2 is not compatible with both Java17 binaries Self-Service Analytics. We recommend you use Windows 2019 or later.
* In general, you can upgrade directly to the latest version of Self-Service Analytics from a prior version of Composer.
* If you are upgrading to a newer version of Self-Service Analytics and you also want to change your encryption mode, perform the upgrade first and then complete the steps described in [Encryption](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/changing-encryption-mode).

<Note>
  New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

<Warning>
  If you are upgrading to Self-Service Analytics and have created an attribute named `User.timeZone`, this may be overwritten on upgrade. See [Upgrade Workflow](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#upgrade-workflow) for more information about preparing your environment for the upgrade process.
</Warning>

#### Upgrading with Kubernetes

<Warning>
  does not support upgrading to use Kubernetes in this release.
</Warning>

#### Java Considerations

Java 21 is required to run Self-Service Analytics 26.3 and later.

An option to install OpenJDK is included in the installation and upgrade scripts provided by insightsoftware. If you skip this option or if you install or upgrade the product manually, make sure that Java 21 is installed for Self-Service Analytics 26.3 and later. If you do not, Self-Service Analytics will not start after the installation.

#### Target Server Prerequisites

The target server for the Self-Service Analytics software should meet the following prerequisites:

* The server must be connected to the Internet.
* If this is a new (fresh) installation, the server must not have PostgreSQL already installed. (Not required for upgrades.)
* If this is a new (fresh) installation, the server must not contain any `zoomdata` folders or property files from previous versions. If a previous version of Zoomdata or Self-Service Analytics was installed on this server, ensure that all property files have been deleted before running the installer script. (Not required for upgrades.)
* The user installing Self-Service Analytics must be able to use the `sudo` command on the server on Linux platforms or `Administrator` privileges for the server on Windows platforms.

If you do not have an internet connection on the server on which Self-Service Analytics is being installed, download the installation package and load it onto the target server. After this is done, you can manually install Self-Service Analytics. See [Install Self-Service Analytics Manually](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#install-self-service-analytics-manually).

If the server on which Self-Service Analytics is to be installed does not meet all the prerequisites, see [Alternative Installation Options](#alternative-installation-options).

In addition, Self-Service Analytics benefits from having time synchronization in your network. Specifically, Self-Service Analytics leverages the Network Time Protocol daemon (NTPD), which performs time synchronization of networked servers to Coordinated Universal Time (UTC). See [Use the Network Time Protocol to Synchronize Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#use-the-network-time-protocol-to-synchronize-time).

After you have made any needed adjustments to your network configurations, you can continue the installation process.

<h2 id="system-requirements">
  System Requirements
</h2>

Self-Service Analytics can be downloaded and installed in different Linux and Windows distributions. You can also deploy Self-Service Analytics in the cloud.

The client application is accessed using web browsers that support WebSocket technology. See [caniuse.com](https://caniuse.com/#search=websockets) to check whether your web browser supports WebSocket technology. The following requirements are needed in order to successfully deploy and access the Self-Service Analytics Server in your operating environment.

* [Operating System and Software Requirements](#operating-system-and-software-requirements)
* [Hardware Requirements](#hardware-requirements)
* [Metadata Repository](#metadata-repository)
* [Network Requirements](#network-requirements)

See also Plan Your Installation.

<h3 id="operating-system-and-software-requirements">
  Operating System and Software Requirements
</h3>

For all deployments, a 64-bit OS is required. The server also uses Java and PostgreSQL. Ensure that the appropriate version of these tools are used in the deployment of Self-Service Analytics in your operating environment.

* RHEL 9 (Red Hat)

* CentOS Stream 9

* Ubuntu 22.04

  <Note>
    Older versions of Ubuntu are nearing end of life (EOL) support. Self-Service Analytics 26.3 and later will require an operating system upgrade before you upgrade your instance.
  </Note>

* Windows Server version and 2019 or higher.

<Danger>
  If your operating system has reached or will soon reach its EOL date, insightsoftware recommends you schedule an appropriate time to upgrade both the Self-Service Analytics and operating system to a later version. For more information, see [Operating System Support](#operating-system-support).
</Danger>

Support services required versions:

| Service | Required Version |
| - | - |
| PostgreSQL | 16 |
| Java | 11 for version 23.1, 17 for 23.2 and later |

<h3 id="hardware-requirements">
  Hardware Requirements
</h3>

The following server specifications are recommended:

* 64 GB RAM (minimum is 16 GB)
* 500 GB disk space
* 16 cores

See also [Server Size Guidelines](#server-size-guidelines).

<h3 id="metadata-repository">
  Metadata Repository
</h3>

<Warning>
  Self-Service Analytics uses a packaged PostgreSQL database instance to store its metadata. Use the provided instance due to the specific configuration and version combination:
</Warning>

* Self-Service Analytics 26.3 and later: PostgreSQL 16

If you would like to use another PostgreSQL instance, contact [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) for further guidance.

<Note>
  New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

<h3 id="network-requirements">
  Network Requirements
</h3>

<h4 id="ports">
  Ports
</h4>

The following table lists the ports you must consider when installing or upgrading Self-Service Analytics.

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Microservice</th>
      <th>Default Port</th>
      <th>Required?</th>
      <th>Notes</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Self-Service Analytics server</td>
      <td>`zoomdata`</td>
      <td>8080</td>
      <td>P</td>

      <td />
    </tr>

    <tr>
      <td>Self-Service Analytics server</td>
      <td>`zoomdata`</td>
      <td>8443, 443</td>
      <td>O</td>
      <td>Required only if you use HTTPS</td>
    </tr>

    <tr>
      <td>[Consul](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#service-discovery-microservice)</td>
      <td>`zoomdata-consul`</td>
      <td>8500</td>
      <td>P</td>

      <td />
    </tr>

    <tr>
      <td>[Query Engine](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#manage-the-self-service-analytics-query-engine)</td>
      <td>`zoomdata-query-engine`</td>
      <td>5580</td>
      <td>P</td>

      <td />
    </tr>

    <tr>
      <td>Appropriate Self-Service Analytics connectors</td>
      <td>`zoomdata-edc-<connector>`</td>
      <td>varies</td>
      <td>P</td>

      <td>
        Only the ports for the Self-Service Analytics connectors to the data stores you will use are required.

        <br />

        For a complete list, see [Data Connector Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference).
      </td>
    </tr>

    <tr>
      <td>[Data Writer](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#data-writer-microservice)</td>
      <td>`zoomdata-data-writer`</td>
      <td>8081</td>
      <td>O</td>
      <td>Required only if you use [flat file](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) or [Upload API](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/uploading-a-flat-file) sources.</td>
    </tr>

    <tr>
      <td>[Screenshot Service](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/screenshot-install)</td>
      <td>`zoomdata-screenshot-service`</td>
      <td>8083</td>
      <td>O</td>
      <td>Required only if you schedule [dashboard reports and self service reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/analyze-data/dashboards/dash-schedule).</td>
    </tr>

    <tr>
      <td>[Self Service Report microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-report-microservice)</td>
      <td>`zoomdata-report-service`</td>
      <td>8087</td>
      <td>O</td>
      <td>Required only if you intend to offer [self service reports](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-report-microservice) and expanded data export options.</td>
    </tr>

    <tr>
      <td>PostgreSQL [metadata repository](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/ov-vis#metadata-repository)</td>
      <td>`zoomdata-postgres`</td>
      <td>5432</td>
      <td>P</td>

      <td />
    </tr>
  </tbody>
</table>

#### Time Synchronization

insightsoftware recommends installing the Network Time Protocol daemon (NTPD) to allow for time synchronization of networked servers to Coordinated Universal Time (UTC), if not already available in your network. See [Using the Network Time Protocol to Synchronize Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#use-the-network-time-protocol-to-synchronize-time) for guidance.

<h2 id="supported-technologies-reference">
  Supported Technologies Reference
</h2>

Prepare your environment to run your embedded analytics environment using the right technologies and infrastructure. This article covers what you must have in place, what we build into Self-Service Analytics, and details important information about optional components for advanced deployment scenarios.

* [Required Components](#required-components)
* [Built In Components](#built-in-components)
* [Optional Components](#optional-components)

<h3 id="required-components">
  Required Components
</h3>

Get your environment ready with these essential technologies. Having these in place empowers your team to deploy and run Self-Service Analytics successfully.

### Operating Systems

You can set up your environment on 64-bit operating systems. Choose one of the following:

<h4 id="self-service-analytics-26-3">
  Self-Service Analytics 26.3
</h4>

* RHEL 9 (Red Hat)

* CentOS Stream 9

* Ubuntu 22.04

  <Note>
    Older versions of Ubuntu are nearing end of life (EOL) support. Versions 26.3 and later will require an operating system upgrade before you upgrade your instance.
  </Note>

* Windows Server version and 2019 or higher.

For more information, see [Operating System Support](#operating-system-support).

### Java Runtime

The specific version of Java required depends on the version of Self-Service Analytics you deploy in your environment.

| Version | Required Java Version |
| - | - |
| v23.1 and earlier | Java 11.0.5 |
| v23.2 through v26.1 | Java 17 |
| v26.2 and later | Java 21 |
| Self-Service Analytics | Java 21 |

The installation script includes an option you can use to install OpenJDK. If you skip this option or perform a manual installation, verify you have the appropriate Java version installed. See Plan Your Installation.

### PostgreSQL Database

A PostgreSQL database stores the metadata pertinent to your data environment. The installation process includes a preconfigured PostgreSQL instance we recommend you use. The version

| Version | PostgreSQL |
| - | - |
| Composer v24.2 and earlier | PostgreSQL 12 |
| Composer v24.3 and later | PostgreSQL 16 |
| Self-Service Analytics | PostgreSQL 16 |

* If you are upgrading to Self-Service Analytics from Composer v24.3 or later, you can keep your existing PostgreSQL version.
* If you are performing a new installation, we use PostgreSQL 16.
* Optionally, use an external PostgreSQL database. Contact [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) for more assistance.

### Hardware

These server specifications are recommended for production deployments:

* 64 GB RAM (minimum: 16 GB)
* 500 GB disk space
* 16 CPU cores

For sizing guidance based on your deployment size and use case, see [Server Size Guidelines](#server-size-guidelines).

### Browser Requirements

Access your environment for use with a supported web browser. See [caniuse.com](https://caniuse.com/#search=websockets).

### Network and Time Synchronization

Make sure your target server meets these network requirements:

* Internet connectivity (or offline installation as described in [Install Self-Service Analytics Manually](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#install-self-service-analytics-manually)).
* Required ports open (see [Ports](#ports) in [System Requirements](#system-requirements)).
* Network Time Protocol (NTPD) configured for UTC synchronization (recommended). See [Use the Network Time Protocol to Synchronize Time](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#use-the-network-time-protocol-to-synchronize-time).

<h2 id="built-in-components">
  Built In Components
</h2>

These are some of the internal technologies that power Self-Service Analytics. You do not need to install these separately: they're included. We are including them here for transparency, and to help you understand the technology that powers the performance and capabilities of this data analytics software.

### Front End Components

* **React 17**: A web application framework that powers the user interface.
* **ag-grid 35.2.1**: Advanced data grid engine for fast, responsive data visualization and exploration.
* **jQuery**: Lightweight JavaScript library for UI interactions and asset management.

### Application Framework

* **Spring Boot 3.5.5**: Production-grade application framework that powers Self-Service Analytics's backend services. Provides security hardening, microservices support, and long-term stability.
* **Java 21** in the Data Connection Layer: The data processing and query execution layer uses Java 21 for enhanced performance and security.
* **Logback**: A unified logging framework that enables consistent log collection and management across all microservices.

### Included JDBC Drivers

Installation includes JDBC database drivers for:

* PostgreSQL
* Microsoft SQL Server
* Snowflake

For other data sources such as MySQL, Oracle, Teradata, Vertica, Dremio), you must provide the JDBC driver. See [Add a JDBC Driver](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#add-a-jdbc-driver).

<h2 id="optional-components">
  Optional Components
</h2>

These technologies extend your environment's capabilities for specific deployment scenarios and operational requirements. Set these up only if your use case requires them.

### Kubernetes Deployment

Deploy on Kubernetes for container orchestration, auto-scaling, and cloud-native operations.

* **Kubernetes**: versions 1.23 through 1.27
* **Helm**: versions 3.8 through 3.11 (for package management)
* **Docker**: Access to the insightsoftware registry on Docker Hub

See [Run Self-Service Analytics in Kubernetes](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/kubernetes-ov) and [Helm Chart for Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/kubernetes-ov#helm-chart-for-self-service-analytics) for complete deployment instructions.

### Observability and Monitoring

Monitor microservices and collect detailed operational metrics.

* **Prometheus**: Scrape metrics from the metrics endpoint. See [Monitoring Microservices: Prometheus](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#monitoring-microservices-prometheus).
* **Statsd and Graphite**: Collect metrics using the Statsd network daemon and visualize in Graphite. See [Monitoring Microservices: Statsd and Graphite](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#monitoring-microservices-statsd-and-graphite).

### Centralized Logging

Collect logs from all Composer microservices in a unified logging system.

Fluentd: Open-source log aggregation and shipping. See [Enable Unified Logging in Self-Service Analytics Using Fluentd](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/fluentd-logging#enable-unified-logging-in-self-service-analytics-using-fluentd).

### Data Source Connectors

You can connect to a variety of data sources. Some data sources are supported for specific version.

* **[Elasticsearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-elastic-search)**: versions 8.1 through 8.17
* **[OpenSearch](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-opensearch)**: versions 1.x and higher (AWS-managed alternative to Elasticsearch)
* **[MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql)**, **[Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle)**, **[Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata)**, **[Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica)**, **[Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio)**: User-provided JDBC drivers required. See [Add a JDBC Driver](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#add-a-jdbc-driver).

For a complete list of supported data sources and connectors, see [Data Connector Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference).

<h3 id="service-discovery-kubernetes">
  Service Discovery (Kubernetes)
</h3>

For Kubernetes deployments, the Helm chart includes optional sub-charts for infrastructure components:

* **Consul**: Service discovery and configuration management (available as Helm sub-chart).
* **PostgreSQL**: Optional external PostgreSQL instance managed by Helm (available as Helm sub-chart).
* **OpenTelemetry Collector**: Observability instrumentation (available as Helm sub-chart).

<h2 id="server-size-guidelines">
  Server Size Guidelines
</h2>

To maximize the operational efficiency of your environment, you need to take into account several factors to appropriately size the server in your operating environment:

* Concurrent user count. This is the most important parameter that increases the load on the system. Concurrent users represent only a portion of the total number of available users in an organization who may access the Self-Service Analytics server at the same time. A single-node deployment can handle up to 100 concurrent users with acceptable performance. If you need more than 100 users, you should consider using several nodes.
* Entity (users, data sources, visuals, dashboard, etc) count. The number of entities in the system doesn’t impact the performance of the system if you have up to 1000 instances of each entity type. If you want to support more than 1000 instances of each entity type you must allocate more resources than shown in the table below.
* Data cardinality. The amount of data processed does not affect the performance of Self-Service Analytics, because the software pushes the work for the queries down to your data stores and thus will rely on the performance of your data stores. However, if you have large data set and want to group the data by a high-cardinality field, you should increase the resource allocation for the query engine.
* High availability (HA). If your Self-Service Analytics environment is an HA environment, sizing requirements may double if each microservice is running on multiple instances.

See [System Requirements](#system-requirements) and [Operating System Support](#operating-system-support) for more information about system requirements. For further information on memory requirements, see [Configure Memory Settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configure-memory-settings).

<h3 id="single-node-environment-minimums">
  Single-Node Environment Minimums
</h3>

The table below reviews the recommended sizing guidelines for a single-node server. Keep in mind that the specifications provided are suggested starting points and reflect only **the minimum estimates**. Sizing for performance is impacted by many other factors outside of the ones mentioned here, such as where Self-Service Analytics. resides, the types of data sources you are using, interactions between applications and data sources, and a variety of other factors.

The following sizing guidelines reflect testing of a single-node deployment with up to 1000 concurrent users, 400 data sources, 500 dashboards, and 6000 visuals.

<table>
  <thead>
    <tr>
      <th scope="col">Concurrent Users</th>
      <th scope="col">Hardware Requirements</th>
      <th scope="col">Time Opening Dashboard (12 Visuals)</th>
      <th scope="col">Composer Web</th>
      <th scope="col">Query Engine</th>
      <th scope="col">Connector</th>
      <th scope="col">PostgreSQL Metadata Store</th>
      <th>Self Service Reports (if enabled)</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Up to 5</td>
      <td>Memory: 8 GB <br />CPU: 8 core<br />Disk: 100 GB</td>
      <td>17 seconds</td>
      <td>Memory: 2 GB</td>
      <td>Memory: 1 GB</td>
      <td>Memory: 512 MB</td>
      <td>Memory: 512 MB</td>
      <td>2 GB</td>
    </tr>

    <tr>
      <td>Up to 20</td>
      <td>Memory: 8 GB <br />CPU: 8 core<br />Disk: 100 GB</td>
      <td>19 seconds</td>
      <td>Memory: 2 GB</td>
      <td>Memory: 1 GB</td>
      <td>Memory: 512 MB</td>
      <td>Memory: 512 MB</td>
      <td>4 GB</td>
    </tr>

    <tr>
      <td>Up to 100</td>
      <td>Memory: 16 GB <br />CPU: 16 core<br />Disk: 100 GB</td>
      <td>26 seconds</td>

      <td>
        Memory: 4 GB

        <br />

        Configuration Settings:

        <br />

        ```properties theme={null}
        spring.datasource.hikari.maximum-pool-size=50
        ```
      </td>

      <td>Memory: 3 GB</td>
      <td>Memory: 1 GB</td>
      <td>Memory: 1 GB</td>
      <td>Will not support high PDF & XLSX generation load</td>
    </tr>

    <tr>
      <td>Up to 1000</td>
      <td>Memory: 16 GB <br />CPU: 16 core<br />Disk: 100 GB</td>
      <td>4 minutes</td>

      <td>
        Memory: 5 GB

        <br />

        Configuration Settings:

        <br />

        ```properties theme={null}
        spring.datasource.hikari.maximum-pool-size=150
        server.jetty.max-threads=1000
        query.engine.service.maxConcurrentRequests=1000
        ```
      </td>

      <td>
        Memory: 4 GB

        <br />

        Configuration Settings:

        <br />

        ```properties theme={null}
        server.jetty.max-threads=1000
        ```
      </td>

      <td>Memory: 1 GB</td>
      <td>Memory: 1 GB</td>
      <td>Will not support high PDF & XLSX generation load</td>
    </tr>
  </tbody>
</table>

<h2 id="clean-installation-and-upgrade-differences">
  Clean Installation and Upgrade Differences
</h2>

An upgrade of Self-Service Analytics means that you are upgrading from an earlier version to a newer version of Self-Service Analytics. This includes uninstalling the previous version and installing a later version. To learn more about upgrades, see [Upgrade Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/upgrading-server).

A clean installation of Self-Service Analytics means that you are installing a new version of Self-Service Analytics from scratch. The Self-Service Analytics metadata is empty and contains no information. This either means that the PostgreSQL is a fresh install as well or that the **zoomdata** database is empty.

A supported upgrade of Self-Service Analytics allows users to continue working in an existing Self-Service Analytics environment while a clean installation of Self-Service Analytics is completely new. For clean installation instructions, see [Install Self-Service Analytics - Linux](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov).

The main difference between an upgrade and clean installation of Self-Service Analytics is whether or not the PostgreSQL is from an existing Self-Service Analytics installation or is new and empty.

<Warning>
  If you are upgrading from a version of Self-Service Analytics more than one major version back, work with Technical Support to plan and coordinate an upgrade of your operating system and other portions of you environment, if needed. See [Operating System Support](#operating-system-support) and [Prerequisites to Upgrading Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/upgrading-server#prerequisites-to-upgrading-self-service-analytics).
</Warning>

<h2 id="alternative-installation-options">
  Alternative Installation Options
</h2>

The following alternative installation options are available. Select an option for step-by-step instructions to set up your Self-Service Analytics instance:

* [Install Self-Service Analytics Manually](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#install-self-service-analytics-manually) (instead of using the [installation script](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov)). This entails (1) downloading and placing the Self-Service Analytics installation package in a dedicated directory on your target server, (2) installing the Self-Service Analytics components and (3) registering and activating the components.
* Install Self-Service Analytics from a tarball package. Contact [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) for assistance. You will receive a tarball package that you unzip in a dedicated directory. You can then install each component manually.

<h2 id="operating-system-support">
  Operating System Support
</h2>

Self-Service Analytics is designed to run on a number of current, secure, and actively maintained operating systems. As operating systems approach their end-of-life (EOL), we will sunset support for those operating systems in your software environment. For more information on the software components that go into your environment, see [Supported Technologies Reference](#supported-technologies-reference).

<h3 id="self-service-analytics-26-3-and-later">
  Self-Service Analytics 26.3 and Later
</h3>

*List Updated: 30 June 2026*

<Warning>
  This information is provided to assist you in planning your future upgrade projects.
</Warning>

<Danger>
  Running an older, unsupported operating system in your environment is done so at your own risk. Plan and upgrade to a supported operating system for full support and functionality.
</Danger>

* RHEL 9 (Red Hat)

* CentOS Stream 9

* Ubuntu 22.04

  <Note>
    Older versions of Ubuntu are nearing end of life (EOL) support. Self-Service Analytics and later will require an operating system upgrade before you upgrade your instance.
  </Note>

* Windows Server version and 2019 or higher.

<h3 id="composer-26-2">
  Composer 26.2
</h3>

*List Updated: 30 June 2026*

<Warning>
  This information is provided to assist you in planning your future upgrade projects.
</Warning>

<Danger>
  Running an older, unsupported operating system in your environment is done so at your own risk. Plan and upgrade to a supported operating system for full support and functionality.
</Danger>

* RHEL 9 (Red Hat)

* CentOS Stream 9

* Ubuntu 22.04

  <Note>
    Older versions of Ubuntu are nearing end of life (EOL) support. Composer 26.2 and later will require an operating system upgrade before you upgrade your instance.
  </Note>

* Windows Server version and 2019 or higher.

<h3 id="composer-26-1">
  Composer 26.1
</h3>

*List Updated: 15 March 2026*

<Warning>
  This information is provided to assist you in planning your future upgrade projects.
</Warning>

<Danger>
  Running an older, unsupported operating system in your environment is done so at your own risk. Plan and upgrade to a supported operating system for full support and functionality.
</Danger>

* RHEL 9 (Red Hat)

* CentOS Stream 9

* Ubuntu 22.04

  <Note>
    Older versions of Ubuntu are nearing end of life (EOL) support. Composer 26.1 and later will require an operating system upgrade before you upgrade your Composer instance.
  </Note>

* Windows Server versions 2016 and 2019 or higher.

<h3 id="composer-25-4">
  Composer 25.4
</h3>

*List Updated: 15 March 2026*

<Danger>
  Running an older, unsupported operating system in your environment is done so at your own risk. Plan and upgrade to a supported operating system for full support and functionality.
</Danger>

* RHEL 9 (Red Hat)

* CentOS Stream 9

  <Note>
    CentOS 7 & 8 are end of life (EOL) support. CentOS Stream 9 is supported for new instances of Composer 25.4 and higher. Upgrade your operating system to CentOS Stream 9 before upgrading your Composer instance.
  </Note>

* Ubuntu 20.04, and Ubuntu 22.04.

  <Note>
    Older versions of Ubuntu are nearing end of life (EOL) support. Composer 26.1 and later will require an operating system upgrade before you upgrade your Composer instance.
  </Note>

* Windows Server versions 2016 and 2019 or higher.

<h3 id="composer-25-3">
  Composer 25.3
</h3>

*List Updated: 15 March 2026*

<Danger>
  Running an older, unsupported operating system in your environment is done so at your own risk. Plan and upgrade to a supported operating system for full support and functionality.
</Danger>

* RHEL 9 (Red Hat)

* CentOS 7 and CentOS 8.

  <Note>
    CentOS 7 & 8 are end of life (EOL) support. CentOS Stream 9 is supported for new instances of Composer 25.4 and higher. Upgrade your operating system to CentOS Stream 9 before upgrading your Composer instance.
  </Note>

* Ubuntu 20.04 and Ubuntu 22.04.

  <Note>
    Older versions of Ubuntu are nearing end of life (EOL) support. Composer 26.1 and later will require an operating system upgrade before you upgrade your Composer instance.
  </Note>

* Windows Server versions 2016 and 2019 or higher.

  <Note>
    Windows Server version 2012 R2 is nearing end of life (EOL) support. Composer will support Windows Server 2012 R2 through the release of Composer 25.3. Composer 25.4 and later will require an operating system upgrade before you upgrade your Composer instance.
  </Note>

<h2 id="self-service-analytics-release-vehicles-and-third-party-end-of">
  Self-Service Analytics Release Vehicles and Third Party End of Life Policy
</h2>

### Important Notices

Self-Service Analytics software is offered on a quarterly release schedule. The current major release is v26.3.

For information about Self-Service Analytics's end-of-life policy for third-party software, see [Third Party End of Life Policy](#third-party-end-of-life-policy).

<Warning>
  Older license keys may not be compatible with Self-Service Analytics. If you are upgrading from any older Composer release, a new license must be requested. See [Request and Apply a New License Key](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/license-request).
</Warning>

### Current Releases

<Warning>
  The current major release of Logi Symphony is v26.1. The capabilities and features you use in your analytics environment have been restructured. For more information, see [Transitioning for Symphony and Composer Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/transition-sym).
</Warning>

Each quarterly release is supported using service packs to address any issues until the next quarterly release is available. Subsequent fixes for a non-current quarterly release are limited to the most severe issues for the next three quarters. Upgrade to the most current quarterly release for the most up to date support and features.

<table>
  <thead>
    <tr>
      <th>Release</th>
      <th>Support Cycle</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>Q1 Releases</td>

      <td>
        * Service packs for all issues throughout Q2
        * Service packs for severe issues only throughout Q3 and Q4
        * End of life for Q1 release at next Q1 release
      </td>
    </tr>

    <tr>
      <td>Q2 Releases</td>

      <td>
        * Service packs for all issues throughout Q3
        * Service packs for severe issues only throughout Q4 and Q1
        * End of life for Q2 release at next Q2 release
      </td>
    </tr>

    <tr>
      <td>Q3 Releases</td>

      <td>
        * Service packs for all issues throughout Q4
        * Service packs for severe issues only throughout Q1 and Q2
        * End of life for Q3 release at next Q3 release
      </td>
    </tr>

    <tr>
      <td>Q4 Release</td>

      <td>
        * Service packs for all issues throughout Q1
        * Service packs for severe issues only throughout Q2 and Q3
        * End of life for Q4 release at next Q4 release
      </td>
    </tr>
  </tbody>
</table>

See [Request and Apply a New License Key](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/license-request) to obtain a license appropriate for your release of choice from our support team. For information about retired releases, see .

<h3 id="self-service-analytics-release-vehicles-and-third-party-end-of-2">
  Upgrade and Migration Considerations
</h3>

* Windows Server 2012R2 is not compatible with both Java17 binaries and the releases of Composer 23.2 and later. We recommend you use Windows 2019 or later to run Self-Service Analytics 26.3 and later.
* In general, you can upgrade directly to the latest version of Self-Service Analytics from a prior version.
* If you are upgrading to a newer version of Self-Service Analytics and you also want to change your encryption mode, perform the upgrade first and then complete the steps described in [Encryption](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/changing-encryption-mode).

<Note>
  New installations of Self-Service Analytics Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.
</Note>

<Warning>
  If you are upgrading to a newer version of Self-Service Analytics and have created an attribute named `User.timeZone`, this may be overwritten on upgrade. See [Upgrade Workflow](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#upgrade-workflow) for more information about preparing your environment for the upgrade process.
</Warning>

<h3 id="previous-releases-retired-releases">
  Previous Releases / Retired Releases
</h3>

If you are using an earlier version of Composer, you should contact Sales and upgrade to the most current release. We no longer publish documentation for any Composer products prior to version v25.

<h3 id="third-party-end-of-life-policy">
  Third Party End of Life Policy
</h3>

As third-party software (such as operating system, database engine, and cluster environment software) ages, it becomes increasingly difficult for insightsoftware to provide the support and level of functionality that our customers expect. To ease this difficulty, insightsoftware has established the following end-of-life (EOL) policy for third-party software. An EOL policy describes when Self-Service Analytics will cease to provide support for a version of third-party software.

Third-party software vendors set the EOL for its software versions. This is the period of time during which the vendor provides patches, fixes, and other updates for a given software version.

When a vendor no longer provides updates and patches or declares an EOL for their software,insightsoftware will remove support for that third-party software version.

When a third-party software version reaches EOL, it continues to function normally. Existing Self-Service Analytics installations using that third-party software version will also continue to function normally. However, you will be unable to perform:

* **Fresh installations of Self-Service Analytics** — Self-Service Analytics prevents new installations after the third-party software reaches EOL.
* **Upgrades to new versions of Self-Service Analytics** — Self-Service Analytics prevents upgrades after the third-party software reaches EOL.
* **Third-party-specific fixes** — Self-Service Analytics does not provide fixes, security or otherwise, after the third-party software reaches EOL.

<Danger>
  If your operating system has reached or will soon reach its EOL date, insightsoftware recommends you schedule an appropriate time to upgrade both the Self-Service Analytics and operating system to a later version. For more information, see [Operating System Support](#operating-system-support).
</Danger>

space
