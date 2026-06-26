---
title: "Optimize Composer's Metadata Store Performance"
id: 4405851090839
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851090839-Optimize-Composer-s-Metadata-Store-Performance
updated_at: 2021-09-21T01:28:53Z
---

# Optimize Composer's Metadata Store Performance

# Optimize Composer's Metadata Store Performance

If you have performance problems with your PostgreSQL metadata store, examine the database settings related to [automatic vacuuming](#Automati), [automatic analyzing](#Automati2), and the [write-ahead log (WAL)](#Write-Ah).

## Automatic Vacuuming (VACUUM)

In PostgreSQL, whenever rows in a table are deleted, the existing row (or tuple) is marked as "dead," but it is not physically removed. During an update, PostgreSQL marks the existing tuple as dead and inserts a new tuple. So a PostgreSQL UPDATE operation is a combination of a delete and an insert operation (DELETE + INSERT).

Dead tuples consume unnecessary storage and eventually, your PostgreSQL database is bloated with them. The VACUUM procedure reclaims the storage occupied by dead tuples. Bear in mind that the reclaimed storage space is never given back to the resident operating system. Instead it is just defragmented within the same database page, and the storage is available for reuse by future data inserts in the same table.

Bloating seriously affects PostgreSQL query performance. PostgreSQL tables and indexes are stored as an array of fixed-size pages (usually 8 KB in size). When a query request for rows is processed, the PostgreSQL instance loads these pages into the memory and the dead rows cause expensive disk I/O during data loading.

To check for dead tuples and the latest vacuum run, use the following query:

```
SELECT  
  schemaname,
  relname,
  n_live_tup,
  n_dead_tup,
  last_autovacuum,
  last_vacuum
FROM pg_stat_user_tables
ORDER BY n_dead_tup
/ (n_live_tup
current_setting('autovacuum_vacuum_scale_factor')::float8
+ current_setting('autovacuum_vacuum_threshold')::float8)
DESC;
```

To check your automatic vacuuming settings, use the following query:

```
select
from pg_settings
where
name like '%autovacuum%';
```

For more information about adjusting automatic VACUUM settings, see:

* <https://www.postgresql.org/docs/current/runtime-config-autovacuum.html>
* <https://habr.com/en/company/postgrespro/blog/486104/>
* <https://dzone.com/articles/tuning-postgresql-autovacuum-to-prevent-table-bloa>

For information about vacuuming your Composer PostgreSQL metadata store, see [*Vacuum Composer's Metadata Store*](https://devnet.logianalytics.com/hc/en-us/articles/4405851091735-Vacuum-Composer-s-Metadata-Store).

## Automatic Analyzing (ANALYZE)

The PostgreSQL query planner relies on statistical information about the contents of tables to generate good plans for queries. These statistics are gathered using the ANALYZE command, which can be invoked by itself or as an optional step in VACUUM. It is important to have reasonably accurate statistics, or poor planning choices might degrade database performance. The PostgreSQL autovacuum daemon, if enabled, automatically issues ANALYZE commands whenever the content of a table has changed sufficiently. The daemon schedules ANALYZE strictly as a function of the number of rows inserted or updated; it has no knowledge of whether that will lead to meaningful statistical changes.

As with vacuuming for space recovery, frequent updates of statistics are more useful for heavily updated tables. But even for a heavily updated table, there might be no need for statistics updates if the statistical distribution of the data has not changing much. A simple rule of thumb is to consider how much the minimum and maximum values of the columns in the table change. For example, a time stamp column that contains the time of row update will have a constantly-increasing maximum value as rows are added and updated; such a column will probably need more frequent statistic updates than a column containing URLs for pages accessed on a website. The URL column might receive changes just as often, but the statistical distribution of its values probably changes relatively slowly.

For more information about the use of automatic ANALYZE processing, see:

* <https://www.postgresql.org/docs/12/sql-analyze.html>
* <https://habr.com/en/company/postgrespro/blog/486104/>

## Write-Ahead Log (WAL)

PostgreSQL databases rely on a write-ahead log (WAL). All databases changes and transactions are written to the WAL first, and then to the data files. This provides durability, because if the database crashes, it can use the WAL to recover. It can read the changes from the WAL and reapply them to the data files. While this may double the number of writes, it may actually improve performance. Users only have to wait for the WAL (to be flushed to disk), while the data files are modified only in memory and then flushed later in the background. PostgreSQL uses checkpoints in its sequence of transactions to identify points at which the data files and the heap have been updated fully with all the data written before the checkpoint. Checkpoints are points in the transaction stream before which the WAL is no longer needed for recovery, reducing disk space requirements and recovery time.

For more information about the WAL, see:

* <https://habr.com/en/company/postgrespro/blog/494464/>
* <https://www.postgresql.org/docs/current/runtime-config-wal.html>
* <https://postgreshelp.com/postgresql-checkpoint/>
* <https://www.postgresql.org/docs/9.5/wal-configuration.html>
