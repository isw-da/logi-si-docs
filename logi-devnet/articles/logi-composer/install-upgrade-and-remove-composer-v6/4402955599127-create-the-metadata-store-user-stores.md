---
title: "Create the Metadata Store User &\u00a0Stores"
id: 4402955599127
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955599127-Create-the-Metadata-Store-User-Stores
updated_at: 2021-08-07T17:31:15Z
---

# Create the Metadata Store User & Stores

# Create the Metadata Store User & Stores

A Composer user must be established for the Postgres metadata store.

To create the Composer user for the Postgres metadata store, complete the following steps:

1. For all Linux operating systems, create the Composer user in PostgreSQL. Run the following command:

   ```
   sudo -u postgres -H psql -c "CREATE USER <db_username> WITH PASSWORD '<db_password>'"
   ```

   Substitute the PostgreSQL user name and password for `<db_username>` and `<db_password>`.
2. Create the stores that will hold the Composer metadata, upload data, keyset, and query engine data. Run the following series of commands, substituting the user name for `<db_username>`:

   ```
   sudo -u postgres -H psql -c "CREATE DATABASE\"zoomdata\" WITH OWNER <db_username>"
     
   sudo -u postgres -H psql -c "CREATE DATABASE\"zoomdata-upload\" WITH OWNER <db_username>"  
   sudo -u postgres -H psql -c "CREATE DATABASE\"zoomdata-keyset\" WITH OWNER <db_username>"  
   sudo -u postgres -H psql -c "CREATE DATABASE\"zoomdata-qe\" WITH OWNER <db_username>"
   ```
