---
title: "Upgrade Steps for Composer"
id: 34933218317069
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933218317069-Upgrade-Steps-for-Composer
updated_at: 2026-05-26T22:08:31Z
---

# Upgrade Steps for Composer

# Upgrade Steps for Composer

To begin the upgrade process, you must receive an email containing upgrade instructions from [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support). This email provides the upgrade script that you need to run on the server where the Composer environment resides.

**Note:** 
If you have not received upgrade instructions, open a ticket with Composer Support.

**Important:** If you are upgrading from a version of Composer more than one major version back, work with Technical Support to plan and coordinate an upgrade of your operating system and other portions of you environment, if needed. See [Operating System Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/39993525943181-Operating-System-Support) and [Prerequisites to Upgrading Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933211393549-Prerequisites-to-Upgrading-Composer).

1. Make sure you have read and performed the recommendations in [Prerequisites to Upgrading Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933211393549-Prerequisites-to-Upgrading-Composer). Be sure to back up your metadata store before you upgrade (see [Back Up the Metadata Store](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933195219213-Back-Up-the-Metadata-Store)).
2. When you receive the email, enter the upgrade command on your target server to start the automated upgrade process. The following Composer components are downloaded on your target server:

   * The Composer server
   * Connector microservices
   * Query Engine
   * Data Writer microservice
3. After the upgrade script has completed, it will take a few minutes for Composer to complete its update of the metadata store. We recommend that you wait a few minutes before accessing Composer from your web browser.

   If you receive a message indicating that Composer is not yet accessible, it may not have completed its setup yet. Wait a few more minutes before trying again or opening a Support ticket. If you continue to have issues accessing Composer from your browser, open a ticket with Composer [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support). For information about accessing Composer, see
   [Access Logi Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932621501453-Access-Logi-Composer).

   **Note:** 
   If you notice some unusual behavior in the Composer UI after upgrading the Composer software (for example, if a drop-down menu doesn't open or the application doesn't react when you select a button), clear the browser cache and try again. If the problem persists, contact Support.
4. The upgrade script provided by [Technical Support](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932980712461-Contact-Technical-Support) assumes that your Postgres metadata store is running locally on the same machine as the Composer code and automatically adds the new databases required by Zoomdata 4.9 (or later) and Composer 5.7 (or later) to your local installation. If you have upgraded and your metadata store is installed on a different machine (not locally), you will need to manually create the following databases in your Postgres metadata store after the upgrade.

   * `zoomdata`
   * `zoomdata-keyset`
   * `zoomdata-qe`
   * `zoomdata-upload`

   See [Create the Metadata Store User & Stores](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933041785357-Create-the-Metadata-Store-User-Stores).
5. The firewall setup you used with earlier versions of Composer should have been retained and your Composer IP address should remain unchanged, but see the following for more information:

   * [Configure the Firewall](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933006781709-Configure-the-Firewall)
   * [Identify the Composer IP Address](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933010272525-Identify-the-Composer-IP-Address)
6. SQL connectors require a JDBC driver to be configured before you can connect to your data source. You can download the driver from the vendor’s site. Be aware that you need to download and configure JDBC drivers for the following Composer connectors:

   * [Microsoft SQL Server](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730176653-Manage-the-Microsoft-SQL-Server-Connector)
   * [MemSQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932747006861-Manage-the-MemSQL-Connector)
   * [MySQL](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730297485-Manage-the-MySQL-Connector)
   * [Oracle](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932730448653-Manage-the-Oracle-Connector)
   * [Amazon Redshift](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932733806989-Manage-the-Amazon-Redshift-Connector)
   * [Teradata](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932773152781-Manage-the-Teradata-Connector)

   If you are using one of these connectors, you need to download and configure a JDBC driver as soon as your Composer server has finished upgrading. For steps, see [Add a JDBC Driver](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932998821005-Add-a-JDBC-Driver).
7. Reimport any CA certificates to the Java 11.0.5 for Composer 23.1 and Java 17 for Composer 23.2 or later you installed prior to the Composer upgrade. (In [Prerequisites to Upgrading Composer](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933211393549-Prerequisites-to-Upgrading-Composer), we recommended that you store them or back them up before the Composer upgrade.)
