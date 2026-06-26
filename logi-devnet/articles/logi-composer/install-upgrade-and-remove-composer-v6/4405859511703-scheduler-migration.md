---
title: "Scheduler Migration"
id: 4405859511703
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859511703-Scheduler-Migration
updated_at: 2021-09-21T01:29:59Z
---

# Scheduler Migration

# Scheduler Migration

The use of the Scheduler microservice was deprecated in Zoomdata 4.3. All the scheduling functionality provided by the Scheduler microservice is provided by [Composer's primary microservice](https://devnet.logianalytics.com/hc/en-us/articles/4405851149591-Composer-Microservice-Name-Reference). Because of this change, the following migration steps must be performed when you first upgrade to Zoomdata 4.3 (or later) or to Composer 5.7 (or later).

1. Back up the `zoomdata-scheduler` metadata store. Save the backup in case a problem occurs during the migration.
2. Add the following properties to the `zoomdata.properties` file for your current Composer installation and save the file:

   | Property | Description |
   | --- | --- |
   | `migration.job-scheduler.url=jdbc:postgresql://localhost:5432/<existing-zoomdata-scheduler-db-name>` | Specify the URL to the existing zoomdata-scheduler database. |
   | `migration.job-scheduler.username=<username>` | Specify a valid user name for the existing zoomdata-scheduler database. |
   | `migration.job-scheduler.password=<password>` | Specify the password associated with the user name for the existing zoomdata-scheduler database. |
3. Upgrade your Zoomdata installation to Zoomdata 4.3 (or later) or to Composer 5.7 or later. See [*Upgrade Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405859509271-Upgrade-Composer).
4. After the upgrade has completed, start Zoomdata or Composer. When you start the product the first time after the upgrade, the Scheduler metadata from your original `zoomdata-scheduler` database is migrated to the `zoomdata` metadata store.
5. Verify that your data source data refreshes correctly, as defined in your data source configurations.
6. If data store data refreshes are working correctly, remove the migration properties you defined in Step 2 from the `zoomdata.properties` file and save the file. If you do not do this, the software will attempt to perform the Scheduler metadata migration every time you start it.
7. Delete the `zoomdata-scheduler` database.
