---
title: "Installation Prerequisites"
id: 34933029670157
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933029670157-Installation-Prerequisites
updated_at: 2026-05-26T22:07:30Z
---

# Installation Prerequisites

# Installation Prerequisites

The installation script works in the following environments:

* RHEL 9 (Red Hat)
* CentOS 7 and CentOS 8.

  **Note:** CentOS 7 & 8 are end of life (EOL) support. CentOS Stream 9 is supported for new instances of Logi Composer 25.4 and higher. Upgrade your operating system to CentOS Stream 9 before upgrading your Composer instance.
* Ubuntu 16.04, Ubuntu 18.04, 20.04, and Ubuntu 22.04.

  **Note:** Ubuntu 16.04 is nearing end of life (EOL) support. Composer will support Ubuntu 16.04 through the release of Composer 25.3. Composer 25.4 and later will require an operating system upgrade before you upgrade your Composer instance.
* Windows Server versions 2016 and 2019 or higher.

  **Note:** Windows Server version 2012 R2 is nearing end of life (EOL) support. Composer will support Windows Server 2012 R2 through the release of Composer 25.3. Composer 25.4 and later will require an operating system upgrade before you upgrade your Composer instance.

**Caution:** If your operating system has reached or will soon reach its EOL date, insightsoftware recommends you schedule an appropriate time to upgrade both the Composer and operating system to a later version. For more information, see [Operating System Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/39993525943181-Operating-System-Support).

#### Upgrade and Migration Considerations

* Windows Server 2012R2 is not compatible with both Java17 binaries and the latest releases of Composer (23.2 and later). We recommend you use Windows 2016 or later to run Composer 23.2 and later.
* In general, you can upgrade directly to the latest version of Composer from a prior version.
* If you are upgrading to a newer version of Composer and you also want to change your encryption mode, perform the upgrade first and then complete the steps described in [Change the Encryption Mode](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933139088269-Change-the-Encryption-Mode).

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

**Important:** If you are upgrading to a newer version of Composer and have created an attribute named `User.timeZone`, this may be overwritten on upgrade. See [Upgrade Workflow](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932887294349-Timezone-Conversion-for-Users#Upgrade) for more information about preparing your environment for the upgrade process.

#### Upgrading with Kubernetes

**Important:** Composer does not support upgrading to use Kubernetes in this release.

#### Java Considerations

Java 11.0.5 is required to run Composer 23.1 and Java 17 is required to run Composer 23.2.

An option to install OpenJDK is included in the installation and upgrade scripts provided by Composer. If you skip this option or if you install or upgrade the product manually, make sure that Java 11.0.5 is installed for Composer 23.1 and Java 17 for Composer 23.2. If you do not, Composer will not start after the installation.

#### Target Server Prerequisites

The target server for the Composer software should meet the following prerequisites:

* The server must be connected to the Internet.
* If this is a new (fresh) installation, the server must not have PostgreSQL already installed. (Not required for upgrades.)
* If this is a new (fresh) installation, the server must not contain any `zoomdata` folders or property files from previous versions. If a previous version of Zoomdata or Composer\ was installed on this server, ensure that all property files have been deleted before running the installer script. (Not required for upgrades.)
* The user installing Composer\ must be able to use the `sudo` command on the server on Linux platforms or `Administrator` privileges for the server on Windows platforms.

If you do not have an internet connection on the server on which Composer\ is being installed, download the \ installation package and load it onto the target server. After this is done, you can manually install Composer. See
[Install Composer Manually](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933041539853-Install-Composer-Manually).

If the server on which Composer is to be installed does not meet all the prerequisites, see [Alternative Installation Options](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980958477-Alternative-Installation-Options).

In addition, Composer benefits from having time synchronization in your network. Specifically, Composer leverages the Network Time Protocol daemon (NTPD), which performs time synchronization of networked servers to Coordinated Universal Time (UTC). If needed, read[Use the Network Time Protocol to Synchronize Time](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933015136781-Use-the-Network-Time-Protocol-to-Synchronize-Time)
for instructions to set this up.

After you have made any needed adjustments to your network configurations, you can continue the installation process.
