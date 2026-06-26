---
title: "Back Up the Metadata Store"
id: 34933195219213
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933195219213-Back-Up-the-Metadata-Store
updated_at: 2026-05-26T22:08:30Z
---

# Back Up the Metadata Store

# Back Up the Metadata Store

Before upgrading your Composer server, insightsoftware recommends that you back up your PostgreSQL metadata store. The metadata includes refresh schedule data, object information for your environment (such as sources, dashboards, and visual definitions), and aggregated result sets. After the metadata store is backed up, perform the upgrade. If problems arise, you can restore the metadata store from your backup copy, if necessary.

This topic describes how to back up the metadata store. For information about restoring the metadata store, see [Restore the Metadata From the Metadata Store Backup](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933210728333-Restore-the-Metadata-From-the-Metadata-Store-Backup).

**Back up the metadata store**

1. From your terminal, SSH to your server.
2. Stop all microservices. For appropriate commands based on your operating system, see  [Stop Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Stop).
3. Navigate to the `/etc/zoomdata` directory and create a backup folder:

   mkdir backups
4. Navigate to the backups directory.
5. Perform an SQL dump of the databases by entering the following commands:

   sudo -u postgres pg\_dump zoomdata > zoomdata
   sudo -u postgres pg\_dump zoomdata-upload > zoomdata-upload
   sudo -u postgres pg\_dump zoomdata-keyset > zoomdata-keyset   
   sudo -u postgres pg\_dump zoomdata-qe > zoomdata-qe
6. Restart all microservices. For appropriate commands based on your OS, see  [Start Microservices](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/35385540487565-About-Microservices#Start).

For more information on backup and restore processes for PostgreSQL, refer to the PostgreSQL [documentation](https://www.postgresql.org/docs/9.5/backup-dump.html).
