---
title: "Change Metadata Store Authentication to MD5"
id: 4405851086103
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851086103-Change-Metadata-Store-Authentication-to-MD5
updated_at: 2021-09-21T01:28:49Z
---

# Change Metadata Store Authentication to MD5

# Change Metadata Store Authentication to MD5

If you installed Composer's metadata store on a server running CentOS or RedHat, complete the configuration steps below. If the server is running Ubuntu, ignore these instructions.

To change authentication for your metadata store to MD5:

1. Edit the `pg_hba.conf` file.

   ```
   sudo vi /var/lib/pgsql/12/data/pg_hba.conf
   ```
2. Change METHOD to MD5.

   ```
   # IPv4 local connections:  
   host all all 127.0.0.1/32 md5  
   # IPv6 local connections:  
   host all all ::1/128 md5
   ```
3. Restart PostgreSQL. In CentOS v7 environments, run:

   ```
   sudo systemctl restart postgresql-12
   ```
