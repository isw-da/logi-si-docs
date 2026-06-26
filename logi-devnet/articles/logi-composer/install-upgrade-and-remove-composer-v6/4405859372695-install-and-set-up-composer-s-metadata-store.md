---
title: "Install and Set Up Composer's Metadata Store"
id: 4405859372695
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859372695-Install-and-Set-Up-Composer-s-Metadata-Store
updated_at: 2021-09-21T01:28:50Z
---

# Install and Set Up Composer's Metadata Store

# Install and Set Up Composer's Metadata Store

Before the Composer components can be installed in the target server, you must install and set up the metadata store that is used in the Composer environment. This must occur regardless of the technique used to install the components (using the [installation script](https://devnet.logianalytics.com/hc/en-us/articles/4405859373719-Install-Composer) or an [alternative installation method](https://devnet.logianalytics.com/hc/en-us/articles/4405851076887-Alternative-Installation-Options)).

Composeruses a packaged PostgreSQL v12 database instance to store its metadata and strongly recommends using this instance due to the specific configuration and version employed. If you would like to use another PostgreSQL instance, contact [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support) for further guidance.

The upgrade to Composer 5.9 or later from a Composer or Zoomdata version prior to 5.9, will usually successfully upgrade the PostgreSQL code and your Composer metadata store automatically. In addition, the previous PostgreSQL 9.5 installation is retained to ensure that data is not lost if the upgrade should fail.

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) Before you attempt to upgrade to Composer 5.9, be sure to back up your metadata store. See [*Back Up the Metadata Store*](https://devnet.logianalytics.com/hc/en-us/articles/4405859506199-Back-Up-the-Metadata-Store).

If you are upgrading to Composer 5.9 or later, consider the following possible PostgreSQL migration issues:

* No check for available disk space is performed during the upgrade. So the PostgreSQL automatic upgrade might fail if there is not enough available disk space to accommodate it. The Bootstrap installation procedure cannot predict the required amount of free disk space it will need.
* If your installation uses an external PostgreSQL instance for Composer's metadata store, you **must** disable the automatic PostgreSQL upgrade in the Bootstrap procedure before you upgrade Composer.

If either of these migration issues is true for your installation, you can disable the automatic PostgreSQL upgrade using the Bootstrap `ZOOMDATA_POSTGRES_DISABLE_UPGRADE` option. This option must be exported before running the Bootstrap procedure (for example by running `export ZOOMDATA_POSTGRES_DISABLE_UPGRADE=TRUE`). After running the Bootstrap procedure with the PostgreSQL upgrade disabled, you must manually upgrade your PostgreSQL metadata store to PostgreSQL 12 before you can use Composer 5.9 or later.

Configuring PostgreSQL as the Composer involves defining authentication and connection parameters, restarting PostgreSQL, establishing login credentials for the Composer user, and creating metadata space for the Composer server and microservices.
Complete the following steps to install and set up the PostgreSQL metadata store:

1. [*Set Up the PostgreSQL Metadata Store*](https://devnet.logianalytics.com/hc/en-us/articles/4405851086999-Set-Up-the-PostgreSQL-Metadata-Store)
2. [*Change Metadata Store Authentication to MD5*](https://devnet.logianalytics.com/hc/en-us/articles/4405851086103-Change-Metadata-Store-Authentication-to-MD5) -- not necessary in Ubuntu environments
3. [*Create the Metadata Store User & Stores*](https://devnet.logianalytics.com/hc/en-us/articles/4405859370391-Create-the-Metadata-Store-User-Stores)
4. [*Configure the Metadata Store for SSL*](https://devnet.logianalytics.com/hc/en-us/articles/4405859371671-Configure-the-Metadata-Store-for-SSL)

In addition, Logi Analytics highly recommends that you optimize the PostgreSQL database instance after every upgrade. See [*Vacuum Composer's Metadata Store*](https://devnet.logianalytics.com/hc/en-us/articles/4405851091735-Vacuum-Composer-s-Metadata-Store).

If you have performance problems with your PostgreSQL metadata store, examine the database settings related to automatic vacuuming, automatic analyzing, and the write-ahead log (WAL). See [*Optimize Composer's Metadata Store Performance*](https://devnet.logianalytics.com/hc/en-us/articles/4405851090839-Optimize-Composer-s-Metadata-Store-Performance).

Optionally, if the target server on which Composer will be installed does not have Internet access, read [*Obtain the Installation Package Without Internet Access*](https://devnet.logianalytics.com/hc/en-us/articles/4405851093783-Obtain-the-Installation-Package-Without-Internet-Access).
