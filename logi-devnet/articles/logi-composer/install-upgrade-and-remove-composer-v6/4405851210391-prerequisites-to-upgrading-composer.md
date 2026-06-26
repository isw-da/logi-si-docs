---
title: "Prerequisites to Upgrading Composer"
id: 4405851210391
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851210391-Prerequisites-to-Upgrading-Composer
updated_at: 2021-09-21T01:29:58Z
---

# Prerequisites to Upgrading Composer

# Prerequisites to Upgrading Composer

Prior to upgrading your software, we **strongly recommend** that you:

* Back up your metadata store. See [*Back Up the Metadata Store*](https://devnet.logianalytics.com/hc/en-us/articles/4405859506199-Back-Up-the-Metadata-Store).
* Back up any previously uploaded CSV files. These files are located in the `/opt/zoomdata/data` directory.
* Store or back up any CA certificates you added to the Java code installed by Zoomdata 4 and Composer 5.7 installations. The CA certificates you added to Java in previous versions will be lost when you perform the manual installation of Java 11.0.5 or later requested by Composer 5.8 (or later) installations. After you have upgraded to Composer 5.8 (or later), you can reimport the CA certificates to your new version of Java.

Failure to have a proper backup could result in losing data during the upgrade process. For more information, see [*Back Up the Metadata Store*](https://devnet.logianalytics.com/hc/en-us/articles/4405859506199-Back-Up-the-Metadata-Store).

### JDK Installation Option

An option to install OpenJDK is included in the installation and upgrade scripts provided by Composer. If you skip this option or if you install or upgrade the product manually, make sure that Java 11.0.5 (or later) is installed. If you do not, Composer will not start after the upgrade.

### Environment Prerequisites

The installer script works in the following environments:

* CentOS 7 or 8
* Ubuntu 16 or 18

#### Important CentOS 6 Information

CentOS 6 is no longer supported and the special installation Bootstrap procedure (`bootstrap-zoomdata-centos6.run`) is no longer provided with this product. CentOS 6 is no longer supported by Red Hat Linux (RHEL). Use CentOS 7 or 8 instead.

#### Important Ubuntu Information

Ubuntu users who have Composer or Zoomdata versions earlier than 5.8 installed must first remove the legacy repository before upgrading Composer 5.8 or later. Use this command:

```
sudo rm -f /etc/apt/sources.list.d/saltstack.list
```

See [*System Requirements*](https://devnet.logianalytics.com/hc/en-us/articles/4405859384727-System-Requirements#Browsers) for recommended settings for deploying Composer on-premise.

The target server for the Composer program should meet the following conditions:

* Server is connected to the Internet
* The user installing Composer is able to use the 'sudo' command in the server
