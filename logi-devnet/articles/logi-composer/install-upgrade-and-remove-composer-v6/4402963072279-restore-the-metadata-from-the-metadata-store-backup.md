---
title: "Restore the Metadata From the Metadata Store Backup"
id: 4402963072279
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402963072279-Restore-the-Metadata-From-the-Metadata-Store-Backup
updated_at: 2021-08-07T17:32:18Z
---

# Restore the Metadata From the Metadata Store Backup

# Restore the Metadata From the Metadata Store Backup

This topic describes how to restore the metadata store from a backup copy. For information about backing up the metadata store, see [*Back Up the Metadata Store*](https://devnet.logianalytics.com/hc/en-us/articles/4402963071511-Back-Up-the-Metadata-Store).

Prior to restoring the metadata, ensure that the target PostgreSQL data store is clean.

To restore the metadata store:

1. From your terminal, SSH to your Composer server.
2. Stop all Composer microservices. For appropriate commands based on your OS, see [*Stop Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4402955610391-Stop-Composer-Microservices).
3. Navigate to your backup directory and enter the following commands:

   ```
   sudo -u postgres psql zoomdata < zoomdata				  
   sudo -u postgres psql zoomdata-upload < zoomdata-upload					  
   sudo -u postgres psql zoomdata-keyset < zoomdata-keyset  
   sudo -u postgres psql zoomdata-qe < zoomdata-qe			
   ```
4. Restart all Composer microservices. For appropriate commands based on your OS, see [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4402963006871-Restart-Composer-Microservices).

For more information on backup and restore processes for PostgreSQL, refer to the PostgreSQL [documentation](https://www.postgresql.org/docs/9.5/backup-dump.html).
