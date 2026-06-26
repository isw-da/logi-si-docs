---
title: "Create the Metadata Store User &\u00a0Stores"
id: 43701134856333
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134856333-Create-the-Metadata-Store-User-Stores
updated_at: 2026-05-29T14:08:42Z
---

# Create the Metadata Store User & Stores

# Create the Metadata Store User & Stores

A Composer user must be established for the Postgres metadata store.

To create the Composer user for the Postgres metadata store, complete the following steps:

1. For all Linux operating systems, create the Composer user in PostgreSQL. Run the following command:

   sudo -u postgres -H psql -c "CREATE USER <db\_username> WITH PASSWORD '<db\_password>'"

   Substitute the PostgreSQL user name and password for `<db_username>` and `<db_password>`.
2. Create the stores that will hold the Composer metadata, upload data, keyset, and query engine data. Run the following series of commands, substituting the user name for `<db_username>`:

   sudo -u postgres -H psql -c "CREATE DATABASE\"zoomdata\" WITH OWNER <db\_username>"
   sudo -u postgres -H psql -c "CREATE DATABASE\"zoomdata-upload\" WITH OWNER <db\_username>"
   sudo -u postgres -H psql -c "CREATE DATABASE\"zoomdata-keyset\" WITH OWNER <db\_username>"
   sudo -u postgres -H psql -c "CREATE DATABASE\"zoomdata-qe\" WITH OWNER <db\_username>"
