---
title: "System Requirements"
id: 4405859384727
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859384727-System-Requirements
updated_at: 2021-10-13T23:55:21Z
---

# System Requirements

# System Requirements

Composer can be downloaded and installed in different Linux distributions.
You can also deploy Composer in the cloud. To try Logi Composer for free, check out our [Free Trials](https://www.logianalytics.com/composer-trial/) page.

The client application is accessed using web browsers that support web socket technology. See [caniuse.com](https://caniuse.com/#search=websockets) to check whether your web browser supports web socket technology. The following requirements are needed in order to successfully deploy and access the Composer Server in your operating environment.

* [*Operating System and Software Requirements*](#Soft)
* [*Hardware Requirements*](#SysReqs_HW)
* [*Metadata Repository*](#Metadata)
* [*Network Requirements*](#Netw)

See also [*Installation Prerequisites*](https://devnet.logianalytics.com/hc/en-us/articles/4405851087895-Installation-Prerequisites).

## Operating System and Software Requirements

For Linux deployments, 64-bit Linux-based OS is required. The following table shows the Linux distributions supported along with the corresponding minimum supported version. Composer Server also uses Java and PostgreSQL. Ensure that the appropriate version of these tools are used in the deployment of Composer in your operating environment.

| Distribution | Supported Version |
| --- | --- |
| CentOS | 7 & 8 |
| Red Hat | 7 & 8 |
| Ubuntu | 16.04 LTS, 18 |
| PostgreSQL | 12 |
| Java | 11.0.5 (or later) |

#### Important CentOS 6 Information

CentOS 6 is no longer supported and the special installation Bootstrap procedure (`bootstrap-zoomdata-centos6.run`) is no longer provided with this product. CentOS 6 is no longer supported by Red Hat Linux (RHEL). Use CentOS 7 or 8 instead.

#### Important Ubuntu Information

Ubuntu users who have Composer or Zoomdata versions earlier than 5.8 installed must first remove the legacy repository before upgrading Composer 5.8 or later. Use this command:

```
sudo rm -f /etc/apt/sources.list.d/saltstack.list
```

## Hardware Requirements

For RPM and Ubuntu installations, the following server specifications are recommended:

* 64 GB RAM (minimum is 16 GB)
* 500 GB disk space
* 16 cores

See also [*Server Size Guidelines*](https://devnet.logianalytics.com/hc/en-us/articles/4405851099543-Server-Size-Guidelines).

## Metadata Repository

Composer uses a packaged PostgreSQL v12 database instance to store its metadata and strongly recommends using this instance due to the specific configuration and version employed. If you would like to use another PostgreSQL instance, contact [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support) for further guidance.

## Network Requirements

### Ports

The following table lists the ports you must consider when installing or upgrading Logi Composer.

| Composer Feature | Microservice | Default Port | Required? | Notes |
| --- | --- | --- | --- | --- |
| Composer server | `zoomdata` | 8080 | P |  |
| Composer server | `zoomdata` | 8443, 443 | O | Required only if you use HTTPS |
| [Consul](https://devnet.logianalytics.com/hc/en-us/articles/4405851117847-Service-Discovery-Microservice) | `zoomdata-consul` | 8500 | P |  |
| [Query Engine](https://devnet.logianalytics.com/hc/en-us/articles/4405859161751-Manage-the-Composer-Query-Engine) | `zoomdata-query-engine` | 5580 | P |  |
| Appropriate Composer connectors | `zoomdata-edc-<connector>` | varies | P | Only the ports for the Composer connectors to the data stores you will use are required. For a complete list, see [*Composer Data Connector Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405859436055-Composer-Data-Connector-Reference). |
| [Data Writer](https://devnet.logianalytics.com/hc/en-us/articles/4405851118743-Data-Writer-Microservice) | `zoomdata-data-writer` | 8081 | O | Required only if you use [flat file](https://devnet.logianalytics.com/hc/en-us/articles/4405850954647-Upload-a-Flat-File-into-Composer) or [Upload API](https://devnet.logianalytics.com/hc/en-us/articles/4405859140247-Use-the-Upload-API) sources. |
| [Screenshot Service](https://devnet.logianalytics.com/hc/en-us/articles/4405851095575-Set-Up-the-Screenshot-Microservice) | `zoomdata-screenshot-service` | 8083 | O | Required only if you schedule [dashboard reports](https://devnet.logianalytics.com/hc/en-us/articles/4405850989335-About-Scheduled-Dashboard-Reports). |
| PostgreSQL [metadata repository](https://devnet.logianalytics.com/hc/en-us/articles/4405851126039-Metadata-Repository) | `zoomdata-postgres` | 5432 | P |  |

### Time Synchronization

Composer recommends installing the Network Time Protocol daemon (NTPD) to allow for time synchronization of networked servers to Coordinated Universal Time (UTC), if not already available in your network. See [Using the Network Time Protocol to Synchronize Time](https://devnet.logianalytics.com/hc/en-us/articles/4405859386519-Use-the-Network-Time-Protocol-to-Synchronize-Time) for guidance.
