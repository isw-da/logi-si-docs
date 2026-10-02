> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Install and Set Up Self-Service Analytics 's Metadata Store

Before the Self-Service Analytics components can be installed in the target server, you must install and set up the metadata store that is used in the environment. This must occur regardless of the technique used to install the components (using the [installation script](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov) or an [alternative installation method](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#alternative-installation-options)).

<Warning>
  Self-Service Analytics uses a packaged PostgreSQL database instance to store its metadata. Use the provided instance due to the specific configuration and version combination:
</Warning>

* Self-Service Analytics 26.3 and later: PostgreSQL 16

If you would like to use another PostgreSQL instance, contact [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) for further guidance.

<Note>
  New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

<Warning>
  Before you attempt to upgrade to Self-Service Analytics, be sure to back up your metadata store. See [Back Up the Metadata Store](#back-up-the-metadata-store).
</Warning>

If you are upgrading Self-Service Analytics, consider the following possible PostgreSQL migration issues:

<Note>
  New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

* No check for available disk space is performed during the upgrade. The PostgreSQL automatic upgrade might fail if there is not enough available disk space to accommodate it. The Bootstrap installation procedure cannot predict the required amount of free disk space it will need.
* If your installation uses an external PostgreSQL instance for Self-Service Analytics's metadata store, you **must** disable the automatic PostgreSQL upgrade in the Bootstrap procedure before you upgrade Self-Service Analytics.

If either of these migration issues is true for your installation, you can disable the automatic PostgreSQL upgrade using the Bootstrap `ZOOMDATA_POSTGRES_DISABLE_UPGRADE` option. This option must be exported before running the Bootstrap procedure (for example by running `export ZOOMDATA_POSTGRES_DISABLE_UPGRADE=TRUE`). After running the Bootstrap procedure with the PostgreSQL upgrade disabled, you must manually upgrade your PostgreSQL metadata store to the appropriate version before you can use Self-Service Analytics.

Configuring PostgreSQL as the metadata store involves defining authentication and connection parameters, restarting PostgreSQL, establishing login credentials for the user, and creating metadata space for the server and microservices. Complete the following steps to install and set up the PostgreSQL metadata store:

1. [Set Up the PostgreSQL Metadata Store](#set-up-the-postgresql-metadata-store)
2. [Change Metadata Store Authentication to MD5](#change-metadata-store-authentication-to-md5) -- not necessary in Ubuntu environments
3. [Create the Metadata Store User & Stores](#create-the-metadata-store-user-stores)
4. [Configure the Metadata Store for SSL](#configure-the-metadata-store-for-ssl)

In addition, insightsoftware highly recommends that you optimize the PostgreSQL database instance after every upgrade. See [Optimize Self-Service Analytics's Metadata Store Performance](#optimize-self-service-analytics-s-metadata-store-performance).

If you have performance problems with your PostgreSQL metadata store, examine the database settings related to automatic vacuuming, automatic analyzing, and the write-ahead log (WAL). See [Optimize Self-Service Analytics's Metadata Store Performance](#optimize-self-service-analytics-s-metadata-store-performance).

Optionally, if the target server on which will be installed does not have Internet access, read [Obtain the Installation Package Without Internet Access](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#obtain-the-installation-package-without-internet-access).

<h2 id="set-up-the-postgresql-metadata-store">
  Set Up the PostgreSQL Metadata Store
</h2>

The instructions to set up PostgreSQL as Self-Service Analytics's metadata store differ depending on the Linux operating system used by the target server. Select a topic below:

* [PostgreSQL Setup for CentOS Environments](#postgresql-setup-for-centos-environments)
* [PostgreSQL Setup for Ubuntu Environments](#postgresql-setup-for-ubuntu-environments)

<h2 id="postgresql-setup-for-centos-environments">
  PostgreSQL Setup for CentOS Environments
</h2>

<Note>
  New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

1. Add the PostgreSQL Yum repository to CentOS by running this command calling the appropriate PostgreSQL version:

   ```bash theme={null}
   sudo yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
   ```

2. Install the PostgreSQL client and server packages by running these commands:

   ```bash theme={null}
   sudo yum -y install epel-release yum-utils sudo yum-config-manager --enable pgdg12 sudo yum install postgresql12-server postgresql12
   ```

3. After installation, initialize the PostgreSQL database:

   ```bash theme={null}
   sudo /usr/pgsql-12/bin/postgresql12-setup initdb
   ```

4. Start and enable the PostgreSQLmicroservice:

   ```bash theme={null}
   sudo systemctl enable --now postgresql-12
   ```

5. Confirm that the service started without errors:

   ```bash theme={null}
   sudo systemctl status postgresql-12
   ```

   If necessary, start it:

   ```bash theme={null}
   sudo systemctl start postgresql-12
   ```

6. If you have a running firewall and remote clients should be able to connect to the PostgreSQL metadata store, modify the firewall to allow the PostgreSQL service:

   ```bash theme={null}
   sudo firewall-cmd --add-service=postgresql --permanent sudo firewall-cmd --reload
   ```

7. If the PostgreSQL database is operating in a cluster, repeat steps 3-6 for each instance of the database.

8. Set up the PostgreSQL Admin user and password:

   ```bash theme={null}
   sudo su - postgres ~]$ psql -c "alter user postgres with password 'StrongPassword'" ALTER ROLE
   ```

<h2 id="postgresql-setup-for-ubuntu-environments">
  PostgreSQL Setup for Ubuntu Environments
</h2>

<Note>
  New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

1. If this is a new server instance, update your current system packages:

   ```bash theme={null}
   sudo apt update sudo apt -y install vim bash-completion wget sudo apt -y upgrade
   ```

   A reboot is necessary after an upgrade.

   ```bash theme={null}
   sudo reboot
   ```

2. Import the GPG key and add the appropriate PostgreSQL version repository to your Ubuntu machine. Run the following commands:

   ```bash theme={null}
   wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee /etc/apt/sources.list.d/pgdg.list
   ```

   The added repository contains many different packages and third-party add-ons, including: `postgresql-client`, `postgresql`, `libpq-dev`, `postgresql-server-dev`, and `pgadmin packages`.

3. Update the package list and install the PostgreSQL server and client packages:

   ```bash theme={null}
   sudo apt update sudo apt -y install postgresql-12 postgresql-client-12
   ```

   The PostgreSQL microservice is started and will start with every system reboot.

4. If you have a running firewall and remote clients should be able to connect to the PostgreSQL metadata store, modify the firewall to allow the PostgreSQL service port:

   ```bash theme={null}
   sudo ufw allow 5432/tcp
   ```

5. Test the PostgreSQL connection.

   1. During installation, a user named `postgres` is created automatically with full superadmin access to your entire PostgreSQL instance. Before you switch to this account, your logged in system user should have sudo privileges:

      ```bash theme={null}
      sudo su - postgres
      ```

   2. Replace the `postgres` password with a strong password:

      ```bash theme={null}
      psql -c "alter user postgres with password 'StrongAdminP@ssw0rd'"
      ```

   3. Start PostgreSQL using this command.

      ```
      $ psql
      ```

   4. Get connection details as shown below.

      ```properties theme={null}
      postgres=# \conninfo You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".
      ```

   5. Create a test database called `mytestdb` to see if everything is working.

      ```properties theme={null}
      postgres=# CREATE DATABASE mytestdb; CREATE DATABASE postgres=# CREATE USER mytestuser WITH ENCRYPTED PASSWORD 'MyStr0ngP@SS'; CREATE ROLE postgres=# GRANT ALL PRIVILEGES ON DATABASE mytestdb to mytestuser; GRANT
      ```

      You can list the created databases by running:

      ```properties theme={null}
      postgres=# \l
      ```

   6. Connect to your test database.

      ```
      postgres-# \c mytestdb You are now connected to database "mytestdb" as user "postgres".
      ```

<h2 id="change-metadata-store-authentication-to-md5">
  Change Metadata Store Authentication to MD5
</h2>

If you installed Self-Service Analytics's metadata store on a server running CentOS or RedHat, complete the configuration steps below. If the server is running Ubuntu, ignore these instructions.

<Note>
  New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

**Change authentication for your metadata store to MD5**

1. Edit the `pg_hba.conf` file for the appropriate version of PosgreSQL.

   ```bash theme={null}
   sudo vi /var/lib/pgsql/12/data/pg_hba.conf
   ```

2. Change METHOD to MD5.

   ```
   # IPv4 local connections: host all all 127.0.0.1/32 md5 # IPv6 local connections: host all all ::1/128 md5
   ```

3. Restart PostgreSQL. In CentOS environments, run:

   ```bash theme={null}
   sudo systemctl restart postgresql-12
   ```

<h2 id="create-the-metadata-store-user-stores">
  Create the Metadata Store User & Stores
</h2>

A Self-Service Analytics user must be established for the Postgres metadata store.

To create the Self-Service Analytics user for the Postgres metadata store, complete the following steps:

1. For all Linux operating systems, create the Self-Service Analytics user in PostgreSQL. Run the following command:

   ```bash theme={null}
   sudo -u postgres -H psql -c "CREATE USER <db_username> WITH PASSWORD '<db_password>'"
   ```

   Substitute the PostgreSQL user name and password for `<db_username>` and `<db_password>`.

2. Create the stores that will hold the Self-Service Analytics metadata, upload data, keyset, and query engine data. Run the following series of commands, substituting the user name for `<db_username>`:

   ```bash theme={null}
   sudo -u postgres -H psql -c "CREATE DATABASE\"zoomdata\" WITH OWNER <db_username>" sudo -u postgres -H psql -c "CREATE DATABASE\"zoomdata-upload\" WITH OWNER <db_username>" sudo -u postgres -H psql -c "CREATE DATABASE\"zoomdata-keyset\" WITH OWNER <db_username>" sudo -u postgres -H psql -c "CREATE DATABASE\"zoomdata-qe\" WITH OWNER <db_username>"
   ```

<h2 id="configure-the-metadata-store-for-ssl">
  Configure the Metadata Store for SSL
</h2>

If you have specified SSL connections for the metadata store JDBC connections in `zoomdata.properties` file, the root CA certificate that is used for the PostgreSQL database must be added to the `/opt/zoomdata/.postgresql` directory. This directory does not exist by default and will need to be created. Complete the following steps.

1. Change to the `/opt/zoomdata` directory as a superuser:

   ```bash theme={null}
   sudo cd /opt/zoomdata
   ```

2. Create a `.postgresql` subdirectory.

   ```bash theme={null}
   sudo mkdir .postgresql
   ```

3. Copy the root CA certificate for the PostgreSQL database into the new directory:

   ```bash theme={null}
   sudo cp root.ca /opt/zoomdata/.postgresql/root.ca
   ```

<h2 id="optimize-self-service-analytics-s-metadata-store-performance">
  Optimize Self-Service Analytics's Metadata Store Performance
</h2>

If you have performance problems with your PostgreSQL metadata store, examine the database settings related to [automatic vacuuming](#automatic-vacuuming-vacuum), [automatic analyzing](#automatic-analyzing-analyze), and the [write-ahead log (WAL)](#write-ahead-log-wal).

<h3 id="automatic-vacuuming-vacuum">
  Automatic Vacuuming (VACUUM)
</h3>

In PostgreSQL, whenever rows in a table are deleted, the existing row (or tuple) is marked as "dead," but it is not physically removed. During an update, PostgreSQL marks the existing tuple as dead and inserts a new tuple. So a PostgreSQL UPDATE operation is a combination of a delete and an insert operation (DELETE + INSERT).

Dead tuples consume unnecessary storage and eventually, your PostgreSQL database is bloated with them. The VACUUM procedure reclaims the storage occupied by dead tuples. Bear in mind that the reclaimed storage space is never given back to the resident operating system. Instead it is just defragmented within the same database page, and the storage is available for reuse by future data inserts in the same table.

Bloating seriously affects PostgreSQL query performance. PostgreSQL tables and indexes are stored as an array of fixed-size pages (usually 8 KB in size). When a query request for rows is processed, the PostgreSQL instance loads these pages into the memory and the dead rows cause expensive disk I/O during data loading.

To check for dead tuples and the latest vacuum run, use the following query:

```sql theme={null}
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

```sql theme={null}
select
from pg_settings
where
name like '%autovacuum%';
```

For more information about adjusting automatic VACUUM settings, see:

* [https://www.postgresql.org/docs/current/runtime-config-autovacuum.html](https://www.postgresql.org/docs/current/runtime-config-autovacuum.html)
* [https://habr.com/en/company/postgrespro/blog/486104/](https://habr.com/en/company/postgrespro/blog/486104/)
* [https://dzone.com/articles/tuning-postgresql-autovacuum-to-prevent-table-bloa](https://dzone.com/articles/tuning-postgresql-autovacuum-to-prevent-table-bloa)

For information about vacuuming your Self-Service Analytics PostgreSQL metadata store, see [Automatic Vacuuming (VACUUM)](#automatic-vacuuming-vacuum).

<h3 id="automatic-analyzing-analyze">
  Automatic Analyzing (ANALYZE)
</h3>

The PostgreSQL query planner relies on statistical information about the contents of tables to generate good plans for queries. These statistics are gathered using the ANALYZE command, which can be invoked by itself or as an optional step in VACUUM. It is important to have reasonably accurate statistics, or poor planning choices might degrade database performance. The PostgreSQL autovacuum daemon, if enabled, automatically issues ANALYZE commands whenever the content of a table has changed sufficiently. The daemon schedules ANALYZE strictly as a function of the number of rows inserted or updated; it has no knowledge of whether that will lead to meaningful statistical changes.

As with vacuuming for space recovery, frequent updates of statistics are more useful for heavily updated tables. But even for a heavily updated table, there might be no need for statistics updates if the statistical distribution of the data has not changing much. A simple rule of thumb is to consider how much the minimum and maximum values of the columns in the table change. For example, a time stamp column that contains the time of row update will have a constantly-increasing maximum value as rows are added and updated; such a column will probably need more frequent statistic updates than a column containing URLs for pages accessed on a website. The URL column might receive changes just as often, but the statistical distribution of its values probably changes relatively slowly.

For more information about the use of automatic ANALYZE processing, see:

* [https://www.postgresql.org/docs/12/sql-analyze.html](https://www.postgresql.org/docs/12/sql-analyze.html)
* [https://habr.com/en/company/postgrespro/blog/486104/](https://habr.com/en/company/postgrespro/blog/486104/)

<h3 id="write-ahead-log-wal">
  Write-Ahead Log (WAL)
</h3>

PostgreSQL databases rely on a write-ahead log (WAL). All databases changes and transactions are written to the WAL first, and then to the data files. This provides durability, because if the database crashes, it can use the WAL to recover. It can read the changes from the WAL and reapply them to the data files. While this may double the number of writes, it may actually improve performance. Users only have to wait for the WAL (to be flushed to disk), while the data files are modified only in memory and then flushed later in the background. PostgreSQL uses checkpoints in its sequence of transactions to identify points at which the data files and the heap have been updated fully with all the data written before the checkpoint. Checkpoints are points in the transaction stream before which the WAL is no longer needed for recovery, reducing disk space requirements and recovery time.

For more information about the WAL, see:

* [https://habr.com/en/company/postgrespro/blog/494464/](https://habr.com/en/company/postgrespro/blog/494464/)
* [https://www.postgresql.org/docs/current/runtime-config-wal.html](https://www.postgresql.org/docs/current/runtime-config-wal.html)
* [https://postgreshelp.com/postgresql-checkpoint/](https://postgreshelp.com/postgresql-checkpoint/)
* [https://www.postgresql.org/docs/9.5/wal-configuration.html](https://www.postgresql.org/docs/9.5/wal-configuration.html)

<h2 id="vacuum-self-service-analytics-s-metadata-store">
  Vacuum Self-Service Analytics's Metadata Store
</h2>

insightsoftware highly recommends that you vacuum the Self-Service Analytics PostgreSQL metadata store after every upgrade. Vacuuming the metadata store optimizes it by maximizing database performance and minimizing the disk space it uses. The following simple procedure recollects metadata store statistics and "vacuums" the unused or dead rows in the database.

<Note>
  This procedure blocks writing to the database. Consequently, work with the database is impossible until the procedure completes.
</Note>

This procedure only works for a PostgreSQL database.

If you have performance problems with your PostgreSQL metadata store, examine the database settings related to automatic vacuuming, automatic analyzing, and the write-ahead log (WAL). See [Optimize Self-Service Analytics's Metadata Store Performance](#optimize-self-service-analytics-s-metadata-store-performance).

**Vacuum your PostgreSQL metadata store**

1. Upgrade your version of Self-Service Analytics (if you have not already done so). This automatically upgrades the PostgreSQL metadata store.

2. Stop Self-Service Analytics and any process connecting to its PostgreSQL metadata store. See [Stop Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#stop-microservices).

3. Back up the PostgreSQL metadata store. See [Back Up the Metadata Store](#back-up-the-metadata-store).

4. Connect to the PostgreSQL database.

5. Run the following command in the console for the PostgreSQL database:

   ```
   VACUUM (FULL, ANALYZE);
   ```

   For more information about VACUUM, see [https://www.postgresql.org/docs/12/sql-vacuum.html](https://www.postgresql.org/docs/12/sql-vacuum.html).

6. After vacuuming completes, start Self-Service Analytics. See [Start Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#start-microservices).

<h2 id="restore-the-metadata-from-the-metadata-store-backup">
  Restore the Metadata From the Metadata Store Backup
</h2>

This topic describes how to restore the metadata store from a backup copy. For information about backing up the metadata store, see [Back Up the Metadata Store](#back-up-the-metadata-store).

Prior to restoring the metadata, ensure that the target PostgreSQL data store is clean.

**Restore the metadata store**

1. From your terminal, SSH to your Self-Service Analytics server.

2. Stop all Self-Service Analytics microservices. For appropriate commands based on your OS, see [Stop Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#stop-microservices).

3. Navigate to your backup directory and enter the following commands:

   ```bash theme={null}
   sudo -u postgres psql zoomdata < zoomdata
   sudo -u postgres psql zoomdata-upload < zoomdata-upload
   sudo -u postgres psql zoomdata-keyset < zoomdata-keyset
   sudo -u postgres psql zoomdata-qe < zoomdata-qe
   ```

4. Restart all Self-Service Analytics microservices. For appropriate commands based on your OS, see [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

For more information on backup and restore processes for PostgreSQL, refer to the PostgreSQL [documentation](https://www.postgresql.org/docs/9.5/backup-dump.html).

<h2 id="back-up-the-metadata-store">
  Back Up the Metadata Store
</h2>

Before upgrading your Self-Service Analytics server, insightsoftware recommends that you back up your PostgreSQL metadata store. The metadata includes refresh schedule data, object information for your environment (such as sources, dashboards, and visual definitions), and aggregated result sets. After the metadata store is backed up, perform the upgrade. If problems arise, you can restore the metadata store from your backup copy, if necessary.

This topic describes how to back up the metadata store. For information about restoring the metadata store, see [Restore the Metadata From the Metadata Store Backup](#restore-the-metadata-from-the-metadata-store-backup).

**Back up the metadata store**

1. From your terminal, SSH to your server.

2. Stop all microservices. For appropriate commands based on your operating system, see [Stop Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#stop-microservices).

3. Navigate to the `/etc/zoomdata` directory and create a backup folder:

   ```bash theme={null}
   mkdir backups
   ```

4. Navigate to the backups directory.

5. Perform an SQL dump of the databases by entering the following commands:

   ```bash theme={null}
   sudo -u postgres pg_dump zoomdata > zoomdata
   sudo -u postgres pg_dump zoomdata-upload > zoomdata-upload
   sudo -u postgres pg_dump zoomdata-keyset > zoomdata-keyset
   sudo -u postgres pg_dump zoomdata-qe > zoomdata-qe
   ```

6. Restart all microservices. For appropriate commands based on your OS, see [Start Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#start-microservices).

For more information on backup and restore processes for PostgreSQL, refer to the PostgreSQL [documentation](https://www.postgresql.org/docs/9.5/backup-dump.html).
