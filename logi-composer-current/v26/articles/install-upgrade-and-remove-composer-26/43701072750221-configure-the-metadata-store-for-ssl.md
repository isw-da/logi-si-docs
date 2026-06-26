---
title: "Configure the Metadata Store for SSL"
id: 43701072750221
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072750221-Configure-the-Metadata-Store-for-SSL
updated_at: 2026-05-29T14:08:43Z
---

# Configure the Metadata Store for SSL

# Configure the Metadata Store for SSL

If you have specified SSL connections for the metadata store JDBC connections in `zoomdata.properties` file, the root CA certificate that is used for the PostgreSQL database must be added to the `/opt/zoomdata/.postgresql` directory. This directory does not exist by default and will need to be created. Complete the following steps.

1. Change to the `/opt/zoomdata` directory as a superuser:

   sudo cd /opt/zoomdata
2. Create a `.postgresql` subdirectory.

   sudo mkdir .postgresql
3. Copy the root CA certificate for the PostgreSQL database into the new directory:

   sudo cp root.ca /opt/zoomdata/.postgresql/root.ca
