---
title: "Restore the Metadata From the Metadata Store Backup"
id: 43701168136205
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701168136205-Restore-the-Metadata-From-the-Metadata-Store-Backup
updated_at: 2026-05-29T14:09:41Z
---

# Restore the Metadata From the Metadata Store Backup

# Restore the Metadata From the Metadata Store Backup

This topic describes how to restore the metadata store from a backup copy. For information about backing up the metadata store, see [Back Up the Metadata Store](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701164946317-Back-Up-the-Metadata-Store).

Prior to restoring the metadata, ensure that the target PostgreSQL data store is clean.

**Restore the metadata store**

1. From your terminal, SSH to your Composer server.
2. Stop all Composer microservices. For appropriate commands based on your OS, see  [Stop Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Stop).
3. Navigate to your backup directory and enter the following commands:

   sudo -u postgres psql zoomdata < zoomdata
   sudo -u postgres psql zoomdata-upload < zoomdata-upload
   sudo -u postgres psql zoomdata-keyset < zoomdata-keyset
   sudo -u postgres psql zoomdata-qe < zoomdata-qe
4. Restart all Composer microservices. For appropriate commands based on your OS, see  [Restart Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Restart).

For more information on backup and restore processes for PostgreSQL, refer to the PostgreSQL [documentation](https://www.postgresql.org/docs/9.5/backup-dump.html).
