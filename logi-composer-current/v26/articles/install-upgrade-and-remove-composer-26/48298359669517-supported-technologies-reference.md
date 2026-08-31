---
title: "Supported Technologies Reference"
id: 48298359669517
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/48298359669517-Supported-Technologies-Reference
updated_at: 2026-08-31T04:12:29Z
---

# Supported Technologies Reference

# Supported Technologies Reference

Prepare your environment to run your embedded analytics environment using the right technologies and infrastructure. This article covers what you must have in place, what we build into Composer, and details important information about optional components for advanced deployment scenarios.

* [Required Components](#Required)
* [Built In Components](#Built)
* [Optional Components](#Optional)

## Required Components

Get your environment ready with these essential technologies. Having these in place empowers your team to deploy and run Composer successfully.

### Operating Systems

You can set up your environment on 64-bit operating systems. Choose one of the following:

#### Composer v26.2

* RHEL 9 (Red Hat)
* CentOS Stream 9
* Ubuntu 22.04

  **Note:** Older versions of Ubuntu are nearing end of life (EOL) support. Composer 26.2 and later will require an operating system upgrade before you upgrade your Composer instance.
* Windows Server version and 2019 or higher.

For more information, see [Operating System Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136004365-Operating-System-Support).

### Java Runtime

The specific version of Java required depends on the version of Composer you deploy in your environment.

| Version | Required Java Version |
| --- | --- |
| v23.1 and earlier | Java 11.0.5 |
| v23.2 through v26.1 | Java 17 |
| v26.2 and later | Java 21 |

The installation script includes an option you can use to install OpenJDK. If you skip this option or perform a manual installation, verify you have the appropriate Java version installed. See [Installation Prerequisites](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701135037709-Installation-Prerequisites).

### PostgreSQL Database

A PostgreSQL database stores the metadata pertinent to your data environment. The installation process includes a preconfigured PostgreSQL instance we recommend you use. The version

| Version | PostgreSQL |
| --- | --- |
| Composer v24.2 and earlier | PostgreSQL 12 |
| Composer v24.3 and later | PostgreSQL 16 |

* If you are upgrading to v24.3 or later, you can keep your existing PostgreSQL version.
* If you are performing a new installation, we use PostgreSQL 16.
* Optionally, use an external PostgreSQL database. Contact [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) for more assistance.

### Hardware

These server specifications are recommended for production deployments:

* 64 GB RAM (minimum: 16 GB)
* 500 GB disk space
* 16 CPU cores

For sizing guidance based on your deployment size and use case, see [Server Size Guidelines](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073249037-Server-Size-Guidelines).

### Browser Requirements

Access your environment for use with a supported web browser. See [caniuse.com](https://caniuse.com/#search=websockets).

### Network and Time Synchronization

Make sure your target server meets these network requirements:

* Internet connectivity (or offline installation as described in [Install Composer Manually](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105134605-Install-Composer-Manually)).
* Required ports open (see [Ports](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105740685-System-Requirements#Ports) in [System Requirements](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105740685-System-Requirements)).
* Network Time Protocol (NTPD) configured for UTC synchronization (recommended). See [Use the Network Time Protocol to Synchronize Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073403021-Use-the-Network-Time-Protocol-to-Synchronize-Time).

## Built In Components

These are some of the internal technologies that power Composer. You do not need to install these separately: they're included. We are including them here for transparency, and to help you understand the technology that powers the performance and capabilities of this data analytics software.

### Front End Components

* **React 17**: A web application framework that powers the user interface.
* **ag-grid 35.2.1**: Advanced data grid engine for fast, responsive data visualization and exploration.
* **jQuery**: Lightweight JavaScript library for UI interactions and asset management.

### Application Framework

* **Spring Boot 3.5.5**: Production-grade application framework that powers Composer's backend services. Provides security hardening, microservices support, and long-term stability.
* **Java 21** in the Data Connection Layer: The data processing and query execution layer uses Java 21 for enhanced performance and security.
* **Logback**: A unified logging framework that enables consistent log collection and management across all microservices.

### Included JDBC Drivers

Installation includes JDBC database drivers for:

* PostgreSQL
* Microsoft SQL Server
* Snowflake

For other data sources such as MySQL, Oracle, Teradata, Vertica, Dremio), you must provide the JDBC driver. See [Add a JDBC Driver](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120472333-Add-a-JDBC-Driver).

## Optional Components

These technologies extend your environment's capabilities for specific deployment scenarios and operational requirements. Set these up only if your use case requires them.

### Kubernetes Deployment

Deploy on Kubernetes for container orchestration, auto-scaling, and cloud-native operations.

* **Kubernetes**: versions 1.23 through 1.27
* **Helm**: versions 3.8 through 3.11 (for package management)
* **Docker**: Access to the insightsoftware registry on Docker Hub

See [Running Composer in Kubernetes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701110924173-Running-Composer-in-Kubernetes) and [Helm Chart for Composer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701110873869-Helm-Chart-for-Composer) for complete deployment instructions.

### Observability and Monitoring

Monitor microservices and collect detailed operational metrics.

* **Prometheus**: Scrape metrics from the metrics endpoint. See [Monitoring Microservices: Prometheus](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073263245-Composer-System-Metrics#Monitori).
* **Statsd and Graphite**: Collect metrics using the Statsd network daemon and visualize in Graphite. See [Monitoring Microservices: Statsd and Graphite](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073263245-Composer-System-Metrics#Monitori2).

### Centralized Logging

Collect logs from all Composer microservices in a unified logging system.

Fluentd: Open-source log aggregation and shipping. See [Enable Unified Logging in Composer Using Fluentd](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701111180429-Enable-Unified-Logging-in-Composer-Using-Fluentd).

### Data Source Connectors

You can connect to a variety of data sources. Some data sources are supported for specific version.

* **[Elasticsearch](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701025911309-Manage-the-Elasticsearch-Connector)**: versions 8.1 through 8.17
* **[OpenSearch](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701074183053-Manage-the-OpenSearch-Connector)**: versions 1.x and higher (AWS-managed alternative to Elasticsearch)
* **[MySQL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044330253-Manage-the-MySQL-Connector)**, **[Oracle](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701011976717-Manage-the-Oracle-Connector)**, **[Teradata](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701091479437-Manage-the-Teradata-Connector)**, **[Vertica](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701027298189-Manage-the-Vertica-Connector)**, **[Dremio](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701043446285-Manage-the-Dremio-Connector)**: User-provided JDBC drivers required. See [Add a JDBC Driver](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120472333-Add-a-JDBC-Driver).

For a complete list of supported data sources and connectors, see [Data Connector Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113495693-Data-Connector-Reference).

### Service Discovery (Kubernetes)

For Kubernetes deployments, the Helm chart includes optional sub-charts for infrastructure components:

* **Consul**: Service discovery and configuration management (available as Helm sub-chart).
* **PostgreSQL**: Optional external PostgreSQL instance managed by Helm (available as Helm sub-chart).
* **OpenTelemetry Collector**: Observability instrumentation (available as Helm sub-chart).
