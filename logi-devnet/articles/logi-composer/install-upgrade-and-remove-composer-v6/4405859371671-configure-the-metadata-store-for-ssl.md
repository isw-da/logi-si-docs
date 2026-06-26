---
title: "Configure the Metadata Store for SSL"
id: 4405859371671
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859371671-Configure-the-Metadata-Store-for-SSL
updated_at: 2021-09-21T01:28:49Z
---

# Configure the Metadata Store for SSL

# Configure the Metadata Store for SSL

In Zoomdata 4.9 (or later) and Composer 5.7 (or later), a newer driver of the PostgreSQL client was introduced. If you have specified SSL connections for the metadata store JDBC connections in `zoomdata.properties` file, the root CA certificate that is used for the PostgreSQL database must be added to the `/opt/zoomdata/.postgresql` directory. This directory does not exist by default and will need to be created. Complete the following steps.

1. Change to the `/opt/zoomdata` directory as a superuser:

   ```
   sudo cd /opt/zoomdata
   ```
2. Create a `.postgresql` subdirectory.

   ```
   sudo mkdir .postgresql
   ```
3. Copy the root CA certificate for the PostgreSQL database into the new directory:

   ```
   sudo cp root.ca /opt/zoomdata/.postgresql/root.ca
   ```
