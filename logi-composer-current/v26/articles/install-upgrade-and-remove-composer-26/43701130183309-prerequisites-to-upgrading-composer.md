---
title: "Prerequisites to Upgrading Composer"
id: 43701130183309
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701130183309-Prerequisites-to-Upgrading-Composer
updated_at: 2026-05-29T14:09:38Z
---

# Prerequisites to Upgrading Composer

# Prerequisites to Upgrading Composer

Prior to upgrading your software, we **strongly recommend** that you back up your metadata store. See [Back Up the Metadata Store](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701164946317-Back-Up-the-Metadata-Store).

Failure to have a proper backup could result in losing data during the upgrade process. For more information, see [Back Up the Metadata Store](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701164946317-Back-Up-the-Metadata-Store).

### JDK Installation Option

An option to install OpenJDK is included in the installation and upgrade scripts provided by Composer. If you skip this option or if you install or upgrade the product manually, make sure that Java 11.0.5 is installed for Composer version 23.1 and Java 17 for Composerversion 23.2. If you do not, Composer will not start after the upgrade.

### Environment Prerequisites

* RHEL 9 (Red Hat)
* CentOS Stream 9
* Ubuntu 22.04.

  **Note:** Older versions of Ubuntu are nearing end of life (EOL) support. Composer 26.1 and later will require an operating system upgrade before you upgrade your Composer instance.
* Windows Server versions 2016 and 2019 or higher.

**Caution:** If your operating system has reached or will soon reach its EOL date, insightsoftware recommends you schedule an appropriate time to upgrade both the Composer and operating system to a later version. For more information, see [Operating System Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136004365-Operating-System-Support).

**Important:** If you are upgrading from a version of Composer more than one major version back, work with Technical Support to plan and coordinate an upgrade of your operating system and other portions of you environment, if needed. See [Operating System Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136004365-Operating-System-Support) and [Prerequisites to Upgrading Composer](#).

See [System Requirements](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105740685-System-Requirements#Browsers) for recommended settings for deploying Composer on-premise.

The target server for the Composer program should meet the following conditions:

* Server is connected to the Internet
* The user installing Composer is able to use the 'sudo' command in the server
