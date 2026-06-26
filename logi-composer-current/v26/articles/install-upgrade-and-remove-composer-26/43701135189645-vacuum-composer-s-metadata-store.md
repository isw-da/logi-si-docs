---
title: "Vacuum Composer's Metadata Store"
id: 43701135189645
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701135189645-Vacuum-Composer-s-Metadata-Store
updated_at: 2026-05-29T14:08:46Z
---

# Vacuum Composer's Metadata Store

# Vacuum Composer's Metadata Store

insightsoftware highly recommends that you vacuum the Composer PostgreSQL metadata store after every upgrade. Vacuuming the metadata store optimizes it by maximizing database performance and minimizing the disk space it uses. The following simple procedure recollects metadata store statistics and "vacuums" the unused or dead rows in the database.

**Note:** 
This procedure blocks writing to the database. Consequently, work with the database is impossible until the procedure completes.

This procedure only works for a PostgreSQL database.

insightsoftware tested this procedure after an upgrade to Composer 5.9. on a machine with 2.6 GHz 6-Core Intel Core i7, 16 GB 2667 MHz DDR4, and SSD storage. The tested database contained 300 accounts, 4800 users, 60,000 sources, 9000 dashboards with 30 visuals each. The procedure took 5-10 minutes.

If you have performance problems with your PostgreSQL metadata store, examine the database settings related to automatic vacuuming, automatic analyzing, and the write-ahead log (WAL). See [Optimize Composer's Metadata Store Performance](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105444365-Optimize-Composer-s-Metadata-Store-Performance).

**Vacuum your PostgreSQL metadata store**

1. Upgrade your version of Composer (if you have not already done so). This automatically upgrades the PostgreSQL metadata store.
2. Stop Composer and any process connecting to its PostgreSQL metadata store. See  [Stop Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Stop).
3. Back up the PostgreSQL metadata store. See [Back Up the Metadata Store](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701164946317-Back-Up-the-Metadata-Store).
4. Connect to the PostgreSQL database.
5. Run the following command in the console for the PostgreSQL database:

   VACUUM (FULL, ANALYZE);

   For more information about VACUUM, see <https://www.postgresql.org/docs/12/sql-vacuum.html>.
6. After vacuuming completes, start Composer. See  [Start Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Start).
