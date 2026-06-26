---
title: "Install and Set Up Composer's Metadata Store"
id: 34933034282381
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933034282381-Install-and-Set-Up-Composer-s-Metadata-Store
updated_at: 2026-05-26T22:07:34Z
---

# Install and Set Up Composer's Metadata Store

# Install and Set Up Composer's Metadata Store

Before the Composer components can be installed in the target server, you must install and set up the metadata store that is used in the Composer environment. This must occur regardless of the technique used to install the components (using the [installation script](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933011559565-Install-Composer) or an [alternative installation method](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980958477-Alternative-Installation-Options)).

**Important:** Composer uses a packaged PostgreSQL database instance to store its metadata. Use the provided instance due to the specific configuration and version combination:

* Logi Composer v24.2 and earlier: PostgreSQL 12
* Composer v24.3 and later: PostgreSQL 16

If you would like to use another PostgreSQL instance, contact [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) for further guidance.

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

**Important:** 
Before you attempt to upgrade to Composer, be sure to back up your metadata store. See [Back Up the Metadata Store](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933195219213-Back-Up-the-Metadata-Store).

If you are upgrading Composer, consider the following possible PostgreSQL migration issues:

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

* No check for available disk space is performed during the upgrade. So the PostgreSQL automatic upgrade might fail if there is not enough available disk space to accommodate it. The Bootstrap installation procedure cannot predict the required amount of free disk space it will need.
* If your installation uses an external PostgreSQL instance for Composer's metadata store, you **must** disable the automatic PostgreSQL upgrade in the Bootstrap procedure before you upgrade Composer.

If either of these migration issues is true for your installation, you can disable the automatic PostgreSQL upgrade using the Bootstrap `ZOOMDATA_POSTGRES_DISABLE_UPGRADE` option. This option must be exported before running the Bootstrap procedure (for example by running `export ZOOMDATA_POSTGRES_DISABLE_UPGRADE=TRUE`). After running the Bootstrap procedure with the PostgreSQL upgrade disabled, you must manually upgrade your PostgreSQL metadata store to the appropriate version before you can use Composer.

Configuring PostgreSQL as the Composer involves defining authentication and connection parameters, restarting PostgreSQL, establishing login credentials for the Composer user, and creating metadata space for the Composer server and microservices.
Complete the following steps to install and set up the PostgreSQL metadata store:

1. [Set Up the PostgreSQL Metadata Store](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933011090701--Set-Up-the-PostgreSQL-Metadata-Store)
2. [Change Metadata Store Authentication to MD5](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933033783821-Change-Metadata-Store-Authentication-to-MD5) -- not necessary in Ubuntu environments
3. [Create the Metadata Store User & Stores](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933041785357-Create-the-Metadata-Store-User-Stores)
4. [Configure the Metadata Store for SSL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933011231885-Configure-the-Metadata-Store-for-SSL)

In addition, insightsoftware highly recommends that you optimize the PostgreSQL database instance after every upgrade. See [Vacuum Composer's Metadata Store](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933044105485-Vacuum-Composer-s-Metadata-Store).

If you have performance problems with your PostgreSQL metadata store, examine the database settings related to automatic vacuuming, automatic analyzing, and the write-ahead log (WAL). See [Optimize Composer's Metadata Store Performance](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932999035405-Optimize-Composer-s-Metadata-Store-Performance).

Optionally, if the target server on which Composer will be installed does not have Internet access, read [Obtain the Installation Package Without Internet Access](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933030928269-Obtain-the-Installation-Package-Without-Internet-Access).
