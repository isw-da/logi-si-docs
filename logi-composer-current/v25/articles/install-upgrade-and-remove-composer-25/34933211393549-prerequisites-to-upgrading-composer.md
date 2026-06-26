---
title: "Prerequisites to Upgrading Composer"
id: 34933211393549
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933211393549-Prerequisites-to-Upgrading-Composer
updated_at: 2026-05-26T22:08:30Z
---

# Prerequisites to Upgrading Composer

# Prerequisites to Upgrading Composer

Prior to upgrading your software, we **strongly recommend** that you back up your metadata store. See [Back Up the Metadata Store](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933195219213-Back-Up-the-Metadata-Store).

Failure to have a proper backup could result in losing data during the upgrade process. For more information, see [Back Up the Metadata Store](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933195219213-Back-Up-the-Metadata-Store).

### JDK Installation Option

An option to install OpenJDK is included in the installation and upgrade scripts provided by Composer. If you skip this option or if you install or upgrade the product manually, make sure that Java 11.0.5 is installed for Composer version 23.1 and Java 17 for Composerversion 23.2. If you do not, Composer will not start after the upgrade.

### Environment Prerequisites

* RHEL 9 (Red Hat)
* CentOS 7 and CentOS 8.

  **Note:** CentOS 7 & 8 are end of life (EOL) support. CentOS Stream 9 is supported for new instances of Logi Composer 25.4 and higher. Upgrade your operating system to CentOS Stream 9 before upgrading your Composer instance.
* Ubuntu 16.04, Ubuntu 18.04, 20.04, and Ubuntu 22.04.

  **Note:** Ubuntu 16.04 is nearing end of life (EOL) support. Composer will support Ubuntu 16.04 through the release of Composer 25.3. Composer 25.4 and later will require an operating system upgrade before you upgrade your Composer instance.
* Windows Server versions 2016 and 2019 or higher.

  **Note:** Windows Server version 2012 R2 is nearing end of life (EOL) support. Composer will support Windows Server 2012 R2 through the release of Composer 25.3. Composer 25.4 and later will require an operating system upgrade before you upgrade your Composer instance.

**Caution:** If your operating system has reached or will soon reach its EOL date, insightsoftware recommends you schedule an appropriate time to upgrade both the Composer and operating system to a later version. For more information, see [Operating System Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/39993525943181-Operating-System-Support).

**Important:** If you are upgrading from a version of Composer more than one major version back, work with Technical Support to plan and coordinate an upgrade of your operating system and other portions of you environment, if needed. See [Operating System Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/39993525943181-Operating-System-Support) and [Prerequisites to Upgrading Composer](#).

See [System Requirements](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933082999693-System-Requirements#Browsers) for recommended settings for deploying Composer on-premise.

The target server for the Composer program should meet the following conditions:

* Server is connected to the Internet
* The user installing Composer is able to use the 'sudo' command in the server
