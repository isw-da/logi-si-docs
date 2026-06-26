---
title: "Install Composer in a Windows Environment"
id: 34932997752077
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932997752077-Install-Composer-in-a-Windows-Environment
updated_at: 2026-05-26T22:07:23Z
---

# Install Composer in a Windows Environment

# Install Composer in a Windows Environment

This section provides instructions for performing a clean installation of Composer in your Windows Server environment.

For information about the difference between a clean installation of Composer and an upgrade to the latest GA release, see [Clean Installation and Upgrade Differences](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932965432973-Clean-Installation-and-Upgrade-Differences).

#### Upgrade and Migration Considerations

* Windows Server 2012R2 is not compatible with both Java17 binaries and the latest releases of Composer (23.2 and later). We recommend you use Windows 2016 or later to run Composer 23.2 and later.
* In general, you can upgrade directly to the latest version of Composer from a prior version.
* If you are upgrading to a newer version of Composer and you also want to change your encryption mode, perform the upgrade first and then complete the steps described in [Change the Encryption Mode](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933139088269-Change-the-Encryption-Mode).

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

**Important:** If you are upgrading to a newer version of Composer and have created an attribute named `User.timeZone`, this may be overwritten on upgrade. See [Upgrade Workflow](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932887294349-Timezone-Conversion-for-Users#Upgrade) for more information about preparing your environment for the upgrade process.

In general, the installation process is automated and you only need to run an installation script. The installation script is implemented using Bootstrap. This script accesses a dedicated Composer repository and automatically downloads all the necessary components to install your Composer microservice.

By default, the bootstrap script installs these core components, connectors, and required dependencies:

* Zoomdata web application
* Query Engine
* MSSQL
* Mongo DB
* Elastic 7
* Solr
* Cloudera Search
* Consul
* PostgreSQL 12
* Corretto JDK17
* Chocolatey

To install other components, adjust bootstrap switches as needed. See [Windows Bootstrap Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932997610381-Windows-Bootstrap-Reference), [Composer  Microservice Name Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933143202829-Composer-Microservice-Name-Reference) and [Data Connector Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933117968525-Data-Connector-Reference).

After the installation has completed, you need to activate the Composer microservices, download and configure a JDBC driver if you are using specific data sources (see [Post-Installation Options](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933012964365-Post-Installation-Options) for a list), and open a browser window and enter the specific IP address to access the Composer client.

Review and complete (as appropriate for your installation) the following installation information:

* [Installation Prerequisites](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933029670157-Installation-Prerequisites)
* [Installation Steps](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933029876365-Installation-Steps)
* [Post-Installation Options](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933012964365-Post-Installation-Options)
* [Access Logi Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932621501453-Access-Logi-Composer)
