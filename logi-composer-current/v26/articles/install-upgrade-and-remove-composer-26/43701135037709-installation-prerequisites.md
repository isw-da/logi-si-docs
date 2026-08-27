---
title: "Installation Prerequisites"
id: 43701135037709
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701135037709-Installation-Prerequisites
updated_at: 2026-08-26T07:11:15Z
---

# Installation Prerequisites

# Installation Prerequisites

The installation script works in the following environments:

* RHEL 9 (Red Hat)
* CentOS Stream 9
* Ubuntu 22.04

  **Note:** Older versions of Ubuntu are nearing end of life (EOL) support. Composer 26.2 and later will require an operating system upgrade before you upgrade your Composer instance.
* Windows Server version and 2019 or higher.

**Caution:** If your operating system has reached or will soon reach its EOL date, insightsoftware recommends you schedule an appropriate time to upgrade both the Composer and operating system to a later version. For more information, see [Operating System Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136004365-Operating-System-Support).

For more information, see [Supported Technologies Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/48298359669517-Supported-Technologies-Reference).

#### Upgrade and Migration Considerations

* Windows Server 2012R2 is not compatible with both Java17 binaries and the latest releases of Composer (23.2 and later). We recommend you use Windows 2019 or later to run Composer 26.2 and later.
* In general, you can upgrade directly to the latest version of Composer from a prior version.
* If you are upgrading to a newer version of Composer and you also want to change your encryption mode, perform the upgrade first and then complete the steps described in [Change the Encryption Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701175423245-Change-the-Encryption-Mode).

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

**Important:** If you are upgrading to a newer version of Composer and have created an attribute named `User.timeZone`, this may be overwritten on upgrade. See [Upgrade Workflow](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068707725-Timezone-Conversion-for-Users#Upgrade) for more information about preparing your environment for the upgrade process.

#### Upgrading with Kubernetes

**Important:** Composer does not support upgrading to use Kubernetes in this release.

#### Java Considerations

Java 17 is required to run Composer 23.2, and Java 21 is required to run Composer 26.2 and later.

An option to install OpenJDK is included in the installation and upgrade scripts provided by Composer. If you skip this option or if you install or upgrade the product manually, make sure that Java 17 is installed for Composer 23.2 or Java 21 for Composer 26.2 and later. If you do not, Composer will not start after the installation.

#### Target Server Prerequisites

The target server for the Composer software should meet the following prerequisites:

* The server must be connected to the Internet.
* If this is a new (fresh) installation, the server must not have PostgreSQL already installed. (Not required for upgrades.)
* If this is a new (fresh) installation, the server must not contain any `zoomdata` folders or property files from previous versions. If a previous version of Zoomdata or Composer\ was installed on this server, ensure that all property files have been deleted before running the installer script. (Not required for upgrades.)
* The user installing Composer\ must be able to use the `sudo` command on the server on Linux platforms or `Administrator` privileges for the server on Windows platforms.

If you do not have an internet connection on the server on which Composer\ is being installed, download the \ installation package and load it onto the target server. After this is done, you can manually install Composer. See
[Install Composer Manually](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105134605-Install-Composer-Manually).

If the server on which Composer is to be installed does not meet all the prerequisites, see [Alternative Installation Options](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072353933-Alternative-Installation-Options).

In addition, Composer benefits from having time synchronization in your network. Specifically, Composer leverages the Network Time Protocol daemon (NTPD), which performs time synchronization of networked servers to Coordinated Universal Time (UTC). If needed, read[Use the Network Time Protocol to Synchronize Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073403021-Use-the-Network-Time-Protocol-to-Synchronize-Time)
for instructions to set this up.

After you have made any needed adjustments to your network configurations, you can continue the installation process.
