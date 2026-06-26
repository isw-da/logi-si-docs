---
title: "System Requirements"
id: 43701105740685
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105740685-System-Requirements
updated_at: 2026-05-29T14:08:50Z
---

# System Requirements

# System Requirements

Logi Composer can be downloaded and installed in different Linux and Windows distributions.
You can also deploy Logi Composer in the cloud. To try Logi Composer for free, check out our [Free Trials](https://www.logianalytics.com/composer-trial/) page.

The client application is accessed using web browsers that support WebSocket technology. See [caniuse.com](https://caniuse.com/#search=websockets) to check whether your web browser supports WebSocket technology. The following requirements are needed in order to successfully deploy and access the Logi Composer Server in your operating environment.

* [Operating System and Software Requirements](#Soft)
* [Hardware Requirements](#SysReqs_HW)
* [Metadata Repository](#Metadata)
* [Network Requirements](#Netw)

See also [Installation Prerequisites](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701135037709-Installation-Prerequisites).

## Operating System and Software Requirements

For all deployments, a 64-bit OS is required. The Logi Composer server also uses Java and PostgreSQL. Ensure that the appropriate version of these tools are used in the deployment of Logi Composer in your operating environment.

* RHEL 9 (Red Hat)
* CentOS 7 and CentOS 8.

  **Note:** CentOS 7 & 8 are end of life (EOL) support. CentOS Stream 9 is supported for new instances of Logi Composer 25.4 and higher. Upgrade your operating system to CentOS Stream 9 before upgrading your Composer instance.
* Ubuntu 16.04, Ubuntu 18.04, 20.04, and Ubuntu 22.04.

  **Note:** Ubuntu 16.04 is nearing end of life (EOL) support. Composer will support Ubuntu 16.04 through the release of Composer 25.3. Composer 25.4 and later will require an operating system upgrade before you upgrade your Composer instance.
* Windows Server versions 2016 and 2019 or higher.

  **Note:** Windows Server version 2012 R2 is nearing end of life (EOL) support. Composer will support Windows Server 2012 R2 through the release of Composer 25.3. Composer 25.4 and later will require an operating system upgrade before you upgrade your Composer instance.

**Caution:** If your operating system has reached or will soon reach its EOL date, insightsoftware recommends you schedule an appropriate time to upgrade both the Composer and operating system to a later version. For more information, see [Operating System Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136004365-Operating-System-Support).

Support services required versions:

| Service | Required Version |
| --- | --- |
| PostgreSQL | 16 |
| Java | 11 for Composer version 23.1, 17 for Composer 23.2 and later |

## Hardware Requirements

The following server specifications are recommended:

* 64 GB RAM (minimum is 16 GB)
* 500 GB disk space
* 16 cores

See also [Server Size Guidelines](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073249037-Server-Size-Guidelines).

## Metadata Repository

**Important:** Composer uses a packaged PostgreSQL database instance to store its metadata. Use the provided instance due to the specific configuration and version combination:

* Logi Composer v24.2 and earlier: PostgreSQL 12
* Composer v24.3 and later: PostgreSQL 16

If you would like to use another PostgreSQL instance, contact [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) for further guidance.

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

## Network Requirements

### Ports

The following table lists the ports you must consider when installing or upgrading Logi Composer.

| Logi Composer Feature | Microservice | Default Port | Required? | Notes |
| --- | --- | --- | --- | --- |
| Logi Composer server | `zoomdata` | 8080 | P |  |
| Logi Composer server | `zoomdata` | 8443, 443 | O | Required only if you use HTTPS |
| [Consul](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701124841229-Service-Discovery-Microservice) | `zoomdata-consul` | 8500 | P |  |
| [Query Engine](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701037846797-Manage-the-Composer-Query-Engine) | `zoomdata-query-engine` | 5580 | P |  |
| Appropriate Logi Composer connectors | `zoomdata-edc-<connector>` | varies | P | Only the ports for the Logi Composer connectors to the data stores you will use are required.  For a complete list, see [Data Connector Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113495693-Data-Connector-Reference). |
| [Data Writer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701106979981-Data-Writer-Microservice) | `zoomdata-data-writer` | 8081 | O | Required only if you use [flat file](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads) or [Upload API](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701044052621-Manage-File-Uploads) sources. |
| [Screenshot Service](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073104013-Set-Up-the-Screenshot-Microservice) | `zoomdata-screenshot-service` | 8083 | O | Required only if you schedule [dashboard reports](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43700998266509-About-Scheduled-Dashboard-Reports). |
| PostgreSQL [metadata repository](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701122518797-Metadata-Repository) | `zoomdata-postgres` | 5432 | P |  |

### Time Synchronization

Logi Composer recommends installing the Network Time Protocol daemon (NTPD) to allow for time synchronization of networked servers to Coordinated Universal Time (UTC), if not already available in your network. See [Using the Network Time Protocol to Synchronize Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073403021-Use-the-Network-Time-Protocol-to-Synchronize-Time) for guidance.
