---
title: "Installation Prerequisites"
id: 4405851087895
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851087895-Installation-Prerequisites
updated_at: 2021-09-21T01:28:50Z
---

# Installation Prerequisites

# Installation Prerequisites

The installation script works in the following environments:

* Centos 7 and 8
* Ubuntu 16.04, and 18
* RHEL 7 and 8

#### Upgrade and Migration Considerations

* In general, you can upgrade directly to the latest version of Composer from a prior version.
* If you are upgrading to a newer version of Composer and you also want to change your encryption mode, perform the upgrade first and then complete the steps described in [*Change the Encryption Mode*](https://devnet.logianalytics.com/hc/en-us/articles/4405859459351-Change-the-Encryption-Mode).
* Manually upgrading Composer no longer provides the Java Runtime Environment (JRE) needed for Composer to start. Make sure you have Java 11.0.5 or later installed before you manually install or manually upgrade to Composer 5.8 or later. If you do not, Composer will not start.

#### Important CentOS 6 Information

CentOS 6 is no longer supported and the special installation Bootstrap procedure (`bootstrap-zoomdata-centos6.run`) is no longer provided with this product. CentOS 6 is no longer supported by Red Hat Linux (RHEL). Use CentOS 7 or 8 instead.

#### Java Considerations

Java 11.0.5 or later is required to run Composer.

An option to install OpenJDK is included in the installation and upgrade scripts provided by Composer. If you skip this option or if you install or upgrade the product manually, make sure that Java 11.0.5 (or later) is installed. If you do not, Composer will not start after the installation.

#### Target Server Prerequisites

The target server for the Composer software should meet the following prerequisites:

* The server must be connected to the Internet.
* If this is a new (fresh) installation, the server must not have PostgreSQL already installed. (Not required for upgrades.)
* If this is a new (fresh) installation, the server must not contain any `zoomdata` folders or property files from previous versions. If a previous version of Zoomdata or Composer was installed on this server, ensure that all property files have been deleted before running the installer script.(Not required for upgrades.)
* The user installing Composer must be able to use the `sudo` command on the server.

If you do not have an internet connection on the server on which Composer is being installed, download the Composer installation package and load it onto the target server. After this is done, you can manually install Composer. See
[*Install Composer Manually*](https://devnet.logianalytics.com/hc/en-us/articles/4405851085207-Install-Composer-Manually).

If the server on which Composer is to be installed does not meet all the prerequisites, see [*Alternative Installation Options*](https://devnet.logianalytics.com/hc/en-us/articles/4405851076887-Alternative-Installation-Options).

In addition, Composer benefits from having time synchronization in your network. Specifically, Composer leverages the Network Time Protocol daemon (NTPD), which performs time synchronization of networked servers to Coordinated Universal Time (UTC). If needed, read [*Use the Network Time Protocol to Synchronize Time*](https://devnet.logianalytics.com/hc/en-us/articles/4405859386519-Use-the-Network-Time-Protocol-to-Synchronize-Time)
for instructions to set this up.

After you have made any needed adjustments to your network configurations, you can continue the installation process.
