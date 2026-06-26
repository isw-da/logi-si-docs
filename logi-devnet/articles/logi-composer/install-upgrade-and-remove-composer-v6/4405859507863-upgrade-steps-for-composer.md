---
title: "Upgrade Steps for Composer"
id: 4405859507863
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859507863-Upgrade-Steps-for-Composer
updated_at: 2021-09-21T01:29:59Z
---

# Upgrade Steps for Composer

# Upgrade Steps for Composer

To begin the upgrade process, you must receive an email containing upgrade instructions from [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support). This email provides the upgrade script that you need to run on the server where the Composer environment resides.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If you have not received upgrade instructions, open a ticket with Composer Support.

1. Make sure you have read and performed the recommendations in [*Prerequisites to Upgrading Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405851210391-Prerequisites-to-Upgrading-Composer). Be sure to back up your metadata store before you upgrade (see [*Back Up the Metadata Store*](https://devnet.logianalytics.com/hc/en-us/articles/4405859506199-Back-Up-the-Metadata-Store)).
2. When you receive the email, enter the upgrade command on your target server to start the automated upgrade process. The following Composer components are downloaded on your target server:

   * The Composer server
   * Connector microservices
   * Query Engine
   * Data Writer microservice
3. After the upgrade script has completed, it will take a few minutes for Composer to complete its update of the metadata store. We recommend that you wait a few minutes before accessing Composer from your web browser.

   If you receive a message indicating that Composer is not yet accessible, it may not have completed its setup yet. Wait a few more minutes before trying again or opening a Support ticket. If you continue to have issues accessing Composer from your browser, open a ticket with Composer [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support). For information about accessing Composer, see
   [*Access Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405850867223-Access-Composer).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If you notice some unusual behavior in the Composer UI after upgrading the Composer software (for example, if a drop-down menu doesn't open or the application doesn't react when you select a button), clear the browser cache and try again. If the problem persists, contact Support.
4. The upgrade script provided by [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support) assumes that your Postgres metadata store is running locally on the same machine as the Composer code and automatically adds the new databases required by Zoomdata 4.9 (or later) and Composer 5.7 (or later) to your local installation. If you have upgraded and your metadata store is installed on a different machine (not locally), you will need to manually create the following databases in your Postgres metadata store after the upgrade.

   * `zoomdata`
   * `zoomdata-keyset`
   * `zoomdata-qe`
   * `zoomdata-upload`

   See [*Create the Metadata Store User & Stores*](https://devnet.logianalytics.com/hc/en-us/articles/4405859370391-Create-the-Metadata-Store-User-Stores).
5. The firewall setup you used with earlier versions of Composer should have been retained and your Composer IP address should remain unchanged, but see the following for more information:

   * [*Configure the Firewall*](https://devnet.logianalytics.com/hc/en-us/articles/4405859364759-Configure-the-Firewall)
   * [*Identify the Composer IP Address*](https://devnet.logianalytics.com/hc/en-us/articles/4405851084311-Identify-the-Composer-IP-Address)
6. SQL connectors require a JDBC driver to be configured before you can connect to your data source. You can download the driver from the vendor’s site. Be aware that you need to download and configure JDBC drivers for the following Composer connectors:

   * [Microsoft SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/4405859229975-Manage-the-Microsoft-SQL-Server-Connector)
   * [MemSQL](https://devnet.logianalytics.com/hc/en-us/articles/4405859228567-Manage-the-MemSQL-Connector)
   * [MySQL](https://devnet.logianalytics.com/hc/en-us/articles/4405850958487-Manage-the-MySQL-Connector)
   * [Oracle](https://devnet.logianalytics.com/hc/en-us/articles/4405850959383-Manage-the-Oracle-Connector)
   * [Amazon Redshift](https://devnet.logianalytics.com/hc/en-us/articles/4405859198103-Manage-the-Amazon-Redshift-Connector)
   * [Teradata](https://devnet.logianalytics.com/hc/en-us/articles/4405859235607-Manage-the-Teradata-Connector)

   If you are using one of these connectors, you need to download and configure a JDBC driver as soon as your Composer server has finished upgrading. For steps, see [*Add a JDBC Driver*](https://devnet.logianalytics.com/hc/en-us/articles/4405859376919-Add-a-JDBC-Driver).
7. Reimport any CA certificates to the Java 11.0.5 or later you installed prior to the Composer upgrade. (In [*Prerequisites to Upgrading Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405851210391-Prerequisites-to-Upgrading-Composer), we recommended that you store them or back them up before the Composer upgrade.
