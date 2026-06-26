---
title: "Vacuum Composer's Metadata Store"
id: 4405851091735
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851091735-Vacuum-Composer-s-Metadata-Store
updated_at: 2021-09-21T01:28:51Z
---

# Vacuum Composer's Metadata Store

# Vacuum Composer's Metadata Store

Logi Analytics highly recommends that you vacuum the Composer PostgreSQL metadata store after every upgrade. Vacuuming the metadata store optimizes it by maximizing database performance and minimizing the disk space it uses. The following simple procedure recollects metadata store statistics and "vacuums" the unused or dead rows in the database.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) This procedure blocks writing to the database. Consequently, work with the database is impossible until the procedure completes.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) This procedure only works for a PostgreSQL database.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg)Logi Analytics tested this procedure after an upgrade to Composer 5.9. on a machine with 2.6 GHz 6-Core Intel Core i7, 16 GB 2667 MHz DDR4, and SSD storage. The tested database contained 300 accounts, 4800 users, 60,000 sources, 9000 dashboards with 30 visuals each. The procedure took 5-10 minutes.

If you have performance problems with your PostgreSQL metadata store, examine the database settings related to automatic vacuuming, automatic analyzing, and the write-ahead log (WAL). See [*Optimize Composer's Metadata Store Performance*](https://devnet.logianalytics.com/hc/en-us/articles/4405851090839-Optimize-Composer-s-Metadata-Store-Performance).

To vacuum your PostgreSQL metadata store:

1. Upgrade your version of Composer (if you have not already done so). This automatically upgrades the PostgreSQL metadata store.
2. Stop Composer and any process connecting to its PostgreSQL metadata store. See [*Stop Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851101463-Stop-Composer-Microservices).
3. Back up the PostgreSQL metadata store. See [*Back Up the Metadata Store*](https://devnet.logianalytics.com/hc/en-us/articles/4405859506199-Back-Up-the-Metadata-Store).
4. Connect to the PostgreSQL database.
5. Run the following command in the console for the PostgreSQL database:

   ```
   VACUUM (FULL, ANALYZE);
   ```

   For more information about VACUUM, see <https://www.postgresql.org/docs/12/sql-vacuum.html>.
6. After vacuuming completes, start Composer. See [*Start Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851100567-Start-Composer-Microservices).
