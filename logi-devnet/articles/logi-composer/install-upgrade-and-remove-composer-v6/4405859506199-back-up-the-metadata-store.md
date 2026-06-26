---
title: "Back Up the Metadata Store"
id: 4405859506199
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859506199-Back-Up-the-Metadata-Store
updated_at: 2021-09-21T01:29:56Z
---

# Back Up the Metadata Store

# Back Up the Metadata Store

Before upgrading your Composer server, Composer recommends that you back up your PostgreSQL metadata store. The metadata includes refresh schedule data, object information for your environment (such as sources, dashboards, and visual definitions), and aggregated result sets. After the metadata store is backed up, perform the upgrade. If problems arise, you can restore the metadata store from your backup copy, if necessary.

This topic describes how to back up the metadata store. For information about restoring the metadata store, see [*Restore the Metadata From the Metadata Store Backup*](https://devnet.logianalytics.com/hc/en-us/articles/4405851208599-Restore-the-Metadata-From-the-Metadata-Store-Backup).

To back up the metadata store:

1. From your terminal, SSH to your Composer server.
2. Stop all microservices. For appropriate commands based on your operating system, see [*Stop Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851101463-Stop-Composer-Microservices).
3. Navigate to the `/etc/zoomdata` directory and create a backup folder:

   ```
   mkdir backups
   ```
4. Navigate to the backups directory.
5. Perform an SQL dump of Composer databases by entering the following commands:

   ```
   sudo -u postgres pg_dump zoomdata > zoomdata				  
   sudo -u postgres pg_dump zoomdata-upload > zoomdata-upload					  
   sudo -u postgres pg_dump zoomdata-keyset > zoomdata-keyset	  
   sudo -u postgres pg_dump zoomdata-qe > zoomdata-qe			
   ```
6. Restart all Composer microservices. For appropriate commands based on your OS, see [*Start Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851100567-Start-Composer-Microservices).

For more information on backup and restore processes for PostgreSQL, refer to the PostgreSQL [documentation](https://www.postgresql.org/docs/9.5/backup-dump.html).
