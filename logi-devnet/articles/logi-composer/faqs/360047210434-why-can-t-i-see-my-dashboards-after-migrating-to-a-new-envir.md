---
title: "Why Can't I See My Dashboards After Migrating to a New Environment?"
id: 360047210434
section: "FAQs"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/360047210434-Why-Can-t-I-See-My-Dashboards-After-Migrating-to-a-New-Environment
updated_at: 2020-07-27T22:43:14Z
---

# Why Can't I See My Dashboards After Migrating to a New Environment?

This article applies to Composer 5.9 and Zoomdata 4.9.

### Issue

After migrating data to a new Composer instance, previously created dashboards may no longer show up.

This issue occurs when the metadata table does not contain data necessary to run dashboards that appear to be missing.  Restore the metadata from a backup using the following steps.

### Solution: Restore Metadata from Backup

1.  Stop all Composer services:

```
sudo systemctl stop $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')
```

2. Drop the zoomdata and zoomdata-scheduler databases in Postgres:

<https://www.postgresql.org/docs/12/sql-dropdatabase.html>

```
sudo –u postgres –H psql –c “DROP DATABASE zoomdata”
```

* –u = user (run this as ‘postgres’)
* –H = run the command
* –c = pipe it to the logs

3. Create the databases again using this command:

```
sudo -u postgres -H psql -c "CREATE DATABASE \"zoomdata\" WITH OWNER zoomdata "
```

4. Navigate to your backup directory and restore the metadata from your Postgres dump file:

```
sudo -u postgres psql zoomdata < zoomdata  
sudo -u postgres psql zoomdata-upload < zoomdata-upload  
sudo -u postgres psql zoomdata-keyset < zoomdata-keyset  
sudo -u postgres psql zoomdata-qe < zoomdata-qe
```

5. Restart services again:

```
sudo systemctl start $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')
```

### References

[Documentation: Backing Up Metadata](https://documentation.logianalytics.com/composerrapid/topics/upgrade/backing-up-metadata-store.html?Highlight=backing%20up)
