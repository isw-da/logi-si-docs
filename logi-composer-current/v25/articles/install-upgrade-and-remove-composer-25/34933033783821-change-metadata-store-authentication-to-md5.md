---
title: "Change Metadata Store Authentication to MD5"
id: 34933033783821
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933033783821-Change-Metadata-Store-Authentication-to-MD5
updated_at: 2026-05-26T22:07:34Z
---

# Change Metadata Store Authentication to MD5

# Change Metadata Store Authentication to MD5

If you installed Composer's metadata store on a server running CentOS or RedHat, complete the configuration steps below. If the server is running Ubuntu, ignore these instructions.

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

**Change authentication for your metadata store to MD5**

1. Edit the `pg_hba.conf` file for the appropriate version of PosgreSQL.

   sudo vi /var/lib/pgsql/12/data/pg\_hba.conf
2. Change METHOD to MD5.

   # IPv4 local connections:
   host all all 127.0.0.1/32 md5 # IPv6 local connections: host all all ::1/128 md5
3. Restart PostgreSQL. In CentOS environments, run:

   sudo systemctl restart postgresql-12
