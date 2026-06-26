---
title: "Upgrade Composer"
id: 34933226897037
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933226897037-Upgrade-Composer
updated_at: 2026-05-26T22:08:32Z
---

# Upgrade Composer

# Upgrade Composer

You can generally upgrade your environment to the latest major version of Composer from a prior major version.

**Important:** If you are upgrading from a version of Composer more than one major version back, work with Technical Support to plan and coordinate an upgrade of your operating system and other portions of you environment, if needed. See [Operating System Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/39993525943181-Operating-System-Support) and [Prerequisites to Upgrading Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933211393549-Prerequisites-to-Upgrading-Composer).

For information about the difference between a clean installation of Composer and an upgrade to the latest GA release, see [Clean Installation and Upgrade Differences](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932965432973-Clean-Installation-and-Upgrade-Differences).

#### Upgrade and Migration Considerations

* Windows Server 2012R2 is not compatible with both Java17 binaries and the latest releases of Composer (23.2 and later). We recommend you use Windows 2016 or later to run Composer 23.2 and later.
* In general, you can upgrade directly to the latest version of Composer from a prior version.
* If you are upgrading to a newer version of Composer and you also want to change your encryption mode, perform the upgrade first and then complete the steps described in [Change the Encryption Mode](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933139088269-Change-the-Encryption-Mode).

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

**Important:** If you are upgrading to a newer version of Composer and have created an attribute named `User.timeZone`, this may be overwritten on upgrade. See [Upgrade Workflow](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932887294349-Timezone-Conversion-for-Users#Upgrade) for more information about preparing your environment for the upgrade process.

To upgrade your Composer installation, read the following sections:

* [Prerequisites to Upgrading Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933211393549-Prerequisites-to-Upgrading-Composer)
* [Upgrade Steps for Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933218317069-Upgrade-Steps-for-Composer)

If you are upgrading a distributed environment, see  [Upgrade a Composer Distributed Environment](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933183541261--Upgrade-a-Composer-Distributed-Environment).
