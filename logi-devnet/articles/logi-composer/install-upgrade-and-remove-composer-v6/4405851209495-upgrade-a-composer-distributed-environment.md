---
title: "Upgrade a Composer Distributed Environment"
id: 4405851209495
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851209495-Upgrade-a-Composer-Distributed-Environment
updated_at: 2021-09-21T01:29:57Z
---

# Upgrade a Composer Distributed Environment

# Upgrade a Composer Distributed Environment

To upgrade a Composer distributed environment from a previous version of Composer or from a Composer environment that was not distributed, follow these steps.

![](https://devnet.logianalytics.com/hc/article_attachments/4409070299415/criticalicon.gif) We recommend that you set up a test environment to run through the upgrade process prior to upgrading your production environment. This will ensure that any errors are understood and resolved that could potentially impact your customers running the production environment.

![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg) If you are upgrading to Composer 5.9 or later from an earlier Composer version, you will also need to upgrade to Java JDK 11 and PostgreSQL 12. When upgrading to these releases, we recommend that you use the bootstrap installation script provided by Logi Analytics to upgrade to avoid manual upgrades to Java JDK 11 and PostgreSQL 12. If you use the bootstrap script, these upgrades happen automatically.

To upgrade a Composer distributed environment, complete the following steps:

**Step 1: Disable and Stop All Composer Microservices**

Before you can start the upgrade, you must disable and stop all Composer microservices. Run the commands described in this section.

To disable all Composer microservices, enter the following command:

```
sudo systemctl disable $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')
```

To stop all Composer microservices, enter the following command:

```
sudo systemctl stop $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')
```

**Step 2: Back Up the Postgres Metadata Store**

Before upgrading your Composer server, Composer recommends that you back up your PostgreSQL metadata store. The metadata includes refresh schedule data, object information for your environment (such as sources, dashboards, and visual definitions), and aggregated result sets. After the metadata store is backed up, perform the upgrade. If problems arise, you can restore the metadata store from your backup copy, if necessary.

To back up the metadata store:

1. From your terminal, SSH to your Composer server.
2. Stop all microservices. For appropriate commands based on your operating system, see [*Stop Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851101463-Stop-Composer-Microservices).
3. Navigate to the `/etc/zoomdata` directory and create a backup folder:

   ```
   mkdir backups
   ```
4. Navigate to the backups directory.
5. Perform an SQL dump of Composer databases by entering the following commands:

   ```
   sudo -u postgres pg_dump zoomdata > zoomdata				  
   sudo -u postgres pg_dump zoomdata-upload > zoomdata-upload					  
   sudo -u postgres pg_dump zoomdata-keyset > zoomdata-keyset	  
   sudo -u postgres pg_dump zoomdata-qe > zoomdata-qe			
   ```
6. Restart all Composer microservices. For appropriate commands based on your OS, see [*Start Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851100567-Start-Composer-Microservices).

For more information on backup and restore processes for PostgreSQL, refer to the PostgreSQL [documentation](https://www.postgresql.org/docs/9.5/backup-dump.html).

*Step 3: Create A New Postgres Metadata Store*

While you can upgrade in place, using an existing metadata store, we recommend that you set up a new instance of the PostgreSQL metadata store for your upgrades. This will preserve the old metadata store in case you need to roll back. If you prefer to upgrade using your existing metadata store, contact your Technical Support representative.

The metadata store should be centrally installed, accessible by all Composer nodes. In a high availability environment, it can be clustered. Complete the following steps.

1. *Complete PostgreSQL Setup Steps*

   The instructions to set up PostgreSQL as Composer's metadata store differ depending on the Linux operating system used by the target server. Select a topic below:

   * [*PostgreSQL Setup for CentOS 7 or 8 Environments*](#PostgreS)
   * [*PostgreSQL Setup for Ubuntu 16 or 18 Environments*](#PostgreS2)

   ## PostgreSQL Setup for CentOS 7 or 8 Environments

   1. Add the PostgreSQL Yum repository to CentOS 7 or 8 by running this command:

      ```
      sudo yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
      ```
   2. Install the PostgreSQL client and server packages by running these commands:

      ```
      sudo yum -y install epel-release yum-utils  
      sudo yum-config-manager --enable pgdg12  
      sudo yum install postgresql12-server postgresql12
      ```
   3. After installation, initialize the PostgreSQL database:

      ```
      sudo /usr/pgsql-12/bin/postgresql-12-setup initdb
      ```
   4. Start and enable the PostgreSQLmicroservice:

      ```
      sudo systemctl enable --now postgresql-12
      ```
   5. Confirm that the service started without errors:

      ```
      sudo systemctl status postgresql-12
      ```

      If necessary, start it:

      ```
      sudo systemctl start postgresql-12
      ```
   6. If you have a running firewall and remote clients should be able to connect to the PostgreSQL metadata store, modify the firewall to allow the PostgreSQL service:

      ```
      sudo firewall-cmd --add-service=postgresql --permanent  
      sudo firewall-cmd --reload
      ```
   7. If the PostgreSQL database is operating in a cluster, repeat steps 3-6 for each instance of the database.
   8. Set up the PostgreSQL Admin user and password:

      ```
      sudo su - postgres  
      ~]$ psql -c "alter user postgres with password 'StrongPassword'"  
      ALTER ROLE
      ```

   ## PostgreSQL Setup for Ubuntu 16 or 18 Environments

   1. If this is a new server instance, update your current system packages:

      ```
      sudo apt update  
      sudo apt -y install vim bash-completion wget  
      sudo apt -y upgrade
      ```

      A reboot is necessary after an upgrade.

      ```
      sudo reboot
      ```
   2. Import the GPG key and add the PostgreSQL 12 repository to your Ubuntu machine. Run the following commands:

      ```
      wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add   
      echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
      ```

      The added repository contains many different packages and third-party add-ons, including: `postgresql-client`, `postgresql`, `libpq-dev`, `postgresql-server-dev`, and `pgadmin packages`.
   3. Update the package list and install the PostgreSQL server and client packages:

      ```
      sudo apt update  
      sudo apt -y install postgresql-12 postgresql-client-12
      ```

      The PostgreSQL microservice is started and will start with every system reboot.
   4. If you have a running firewall and remote clients should be able to connect to the PostgreSQL metadata store, modify the firewall to allow the PostgreSQL service port:

      ```
      sudo ufw allow 5432/tcp
      ```
   5. Set Up the PostgreSQL Admin user and password.

   ```
   sudo su - postgres  
   ~]$ psql -c "alter user postgres with password 'StrongPassword'"  
   ALTER ROLE
   ```
2. **Change Metadata Store Authentication to MD5**

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
3. **Create the Metadata Store User**

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
4. **Configure the Metadata Store for SSL**

   In Zoomdata 4.9 (or later) and Composer 5.7 (or later), a newer driver of the PostgreSQL client was introduced. If you have specified SSL connections for the metadata store JDBC connections in `zoomdata.properties` file, the root CA certificate that is used for the PostgreSQL database must be added to the `/opt/zoomdata/.postgresql` directory. This directory does not exist by default and will need to be created. Complete the following steps.

   1. Change to the `/opt/zoomdata` directory as a superuser:

      ```
      sudo cd /opt/zoomdata
      ```
   2. Create a `.postgresql` subdirectory.

      ```
      sudo mkdir .postgresql
      ```
   3. Copy the root CA certificate for the PostgreSQL database into the new directory:

      ```
      sudo cp root.ca /opt/zoomdata/.postgresql/root.ca
      ```
5. **Configure the Metadata Store for a Distributed Environment**

   The Composer PostgreSQL data store must be configured so it is available to all Composer instances in a distributed environment. For more information about PostgreSQL high availability clustering, see <https://www.postgresql.org/docs/12/high-availability.html>.

   To configure the PostgreSQL data store so it is available to all Composer instances:

   1. Edit the postgresql.con file:

   ```
   sudo vi /var/lib/pgsql/12/data/postgresql.conf
   ```

   2. Set the following property in postgresql.conf and save the file.

   ```
   listen_address='*'
   ```

   1. Edit the pg\_hba.conf file:

   ```
   sudo vi /var/lib/pgsql/12/data/pg_hba.conf
   ```

   1. Add the following to the pg\_hba.conf file:

   ```
   # TYPE DATABASE USER ADDRESS METHOD  
              # IPv4 local connections  
              host all all 0.0.0.0 /0 md5
   ```

   1. Save the pg\_hba.conf file.
   2. Restart the PostgreSQL service:

   ```
   sudo service postgresql-12 restart
   ```

**Step 4: Restore the Metadata From the Metadata Store Backup**

Prior to restoring the metadata, ensure that the target PostgreSQL data store is clean.

To restore the metadata store:

1. From your terminal, SSH to your Composer server.
2. Stop all Composer microservices. For appropriate commands based on your OS, see [*Stop Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851101463-Stop-Composer-Microservices).
3. Navigate to your backup directory and enter the following commands:

   ```
   sudo -u postgres psql zoomdata < zoomdata				  
   sudo -u postgres psql zoomdata-upload < zoomdata-upload					  
   sudo -u postgres psql zoomdata-keyset < zoomdata-keyset  
   sudo -u postgres psql zoomdata-qe < zoomdata-qe			
   ```
4. Restart all Composer microservices. For appropriate commands based on your OS, see [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).

For more information on backup and restore processes for PostgreSQL, refer to the PostgreSQL [documentation](https://www.postgresql.org/docs/9.5/backup-dump.html).

**Step 5. Upgrade Your Composer Software On All Servers**

Intra-service communication must be enabled by making any necessary networking (ports) and firewall changes.

To deploy multiple Composer nodes (or instances) in a distributed environment, complete the following steps for each instance:

1. For each instance, run the following commands to set up the environment variables for the installation:

   ```
   export ZOOMDATA_POSTGRES_HOST=<postgres-host>  
   export ZOOMDATA_POSTGRES_PORT=<postgres-port>  
   export ZOOMDATA_POSTGRES_USER=<postgres-db-username>  
   export ZOOMDATA_POSTGRES_PASS=<postgres-db-password>
   ```

   where:

   * `<postgres-host>` and `<postgres-port>` are the host name and port number of the Composer PostgreSQl metadata store
   * `<postgres-db-username>` and `<postgres-db-password>` are the user name and password required to access the Composer PostgreSQL metadata store.
2. In high availability (HA) environments only, run the following commands for each instance to set up the environment variables for the Consul configuration:

   ```
   export ZOOMDATA_CONSUL_ADDRESS=<instance_ip>:8500  
   export ZOOMDATA_CONSUL_CLIENT=0.0.0.0
   ```

   where `<instance_ip>` is the IP address of the Composer instance.
3. In each instance, run the following command to set up the environment variables for specific enterprise data connector (EDC) packages:

   ```
   export ZOOMDATA_EDC_PACKAGES='<edc>,<edc>[,<edc>]...'
   ```

   where `<edc>` is the name of the data connector you'd like to install. You must install the PostgreSQL connector because it connects to the metadata store. Data connector names are the same as their connector microservice names without the `zoomdata-edc-` prefix. See [*Composer Data Connector Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405859436055-Composer-Data-Connector-Reference).
4. Disable the automatic PostgreSQL metadata store upgrade by running the following command:

   ```
   export ZOOMDATA_POSTGRES_DISABLE_UPGRADE=TRUE'
   ```
5. Run the bootstrap installation script after exporting the environment variables in the previous steps.

   ```
   curl -O https://composer-repo.logianalytics.com/<v.r>/bootstrap-zoomdata.run  
   sudo -E /bin/sh bootstrap-zoomdata.run
   ```

   where `<v.r>` is the Composer version and release.
6. After the installation, ensure that the following property files are correctly set up on each node. Add or update the properties as necessary. In each, the IP address, port, user name, and password of the PostgreSQL metadata store should be specified.

   In the `zoomdata.properties` file:

   ```
   spring.datasource.url=jdbc:postgresql://<IP-address>:<port>/zoomdata  
   spring.datasource.username=<db-username>  
   spring.datasource.password=<db-password>  
   keyset.destination.params.jdbc_url=jdbc:postgresql://<IP-address>:<port>/zoomdata-keyset  
   keyset.destination.params.user_name=<db-username>  
   keyset.destination.params.password=<db-password>  
   keyset.destination.schema=public  
   upload.destination.params.jdbc_url=jdbc:postgresql://<IP-address>:<port>/zoomdata-upload  
   upload.destination.params.user_name=<db-username>  
   upload.destination.params.password=<db-password>
   ```

   In the `query-engine.properties` file:

   ```
   spring.qe.datasource.jdbcUrl=jdbc:postgresql://<IP-address>:<port>/zoomdata-qe  
   spring.qe.datasource.username=<db-username>  
   spring.qe.datasource.password=<db-password>
   ```
7. Ensure that port 8080 is open on all your back-end servers to support load balancing. If not, run the following command:

   ```
   sudo iptables -I INPUT 1 -p tcp --dport 8080 -j ACCEPT  
   sudo service iptables save
   ```
8. Repeat these steps for every Composer instance (node) in your Composer cluster. For additional information on how many nodes to deploy in a high availability environment, see [*Determine How Many Nodes to Deploy*](https://devnet.logianalytics.com/hc/en-us/articles/4405851082263-Determine-How-Many-Nodes-to-Deploy).

**Step 6. Set Up a Load Balancer (Optional)**

If you are upgrading from an existing distributed environment to another distributed environment, you can skip this step. Your load balancers were set up when you first installed the product.

If you are upgrading from a non-distributed environment to a distributed environment, set up one or more load balancers in your environment. For a simple load balanced configuration, only one is needed. In a high availability configuration, however, more than one load balancer is recommended; if only a single load balancer is deployed in a high availability environment, you will not be able to access any of the Composer nodes behind it if the load balancer should fail.

The following steps provide an example of setting up HAProxy as a load balancer. Regardless of what kind of load balancer you use, ensure that port 443 is open on it.

To set up an HAProxy load balancer:

1. On your machine, run the following command to install HAProxy:

   ```
   sudo yum install haproxy
   ```
2. Navigate to the HAProxy folder.

   ```
   cd /etc/haproxy
   ```
3. Create a certificate or copy an existing certificate to the `/etc/haproxy` folder. If you need to create a certificate, run the following commands:

   ```
   sudo openssl genrsa -out ca.key 1024  
   sudo openssl req -new -key ca.key -out ca.csr  
   sudo openssl x509 -req -days 365 -in ca.csr -signkey ca.key -out ca.crt  
   sudo vi cert.pem #Create and save an empty file  
   sudo chmod a+w cert.pem  
   sudo cat ca.key ca.crt > cert.pem
   ```
4. In the same folder, replace the contents of the `haproxy.cfg` file with the contents of the [Composer haproxy configuration file](https://devnet.logianalytics.com/hc/article_attachments/4409054855959/haproxy.txt). In the file, replace the `<node1-ip>` and `<node2-ip>` with the IP addresses of your servers. If you have more than two servers, add additional lines for each server.
5. Save your changes and exit the file.
6. Start the HAProxy microservice

   ```
   sudo service haproxy restart
   ```
7. Use the following command to configure the HAProxy microservice to start automatically in CentOS 7 or 8 environments:

   ```
   sudo systemctl enable haproxy
   ```
8. Ensure that port 443 is open on your load balancer. If not, run the following command:

   ```
   sudo yum install -y iptables-services  
   sudo iptables -I INPUT 1 -p tcp --dport 443 -j ACCEPT  
   sudo service iptables save
   ```

For assistance with configuring SAML for use with HAProxy, contact Composer Technical Support.

**Step 7. Configure Consul Services for High Availability (Optional)**

If you are upgrading from an existing high availability environment to another high availability environment, you can skip this step. Consul services were set up when you first installed the product.

If you are upgrading from a non-distributed environment to a high availability environment, Consul services must be configured.

You can install individual Consul instances locally for each Composer node and then configure the Consul instances as a cluster for the Composer high availability environment. Before you do, make sure you are familiar with the general clustering techniques used for Consul. See <https://www.consul.io/docs/install/bootstrapping> for more information.

The primary advantage of using a Consul cluster in a Composer high availability environment is that it requires fewer configuration changes to Composer components. Each component will look for the Consul on the localhost interface at port 127.0.0.1. The only configuration necessary is to the Consul cluster nodes themselves.

Another advantage is that each node of the Composer high availability cluster will use several discovered instances of the same component to balance the load and become more tolerant of any component failures.

To configure a Consul cluster for a Composer high availability environment:

1. Install all the individual Consul instances on each Composer node. This happens automatically when you use the Composer bootstrap installation procedure.
2. Make sure that a firewall is opened in your environment for ports 8500, 8300, 8301, and 8302 on all hosts that will form the Consul cluster.
3. Edit the Consul custom configuration file `consul.json` on each Composer node.

   ```
   sudo vi /etc/zoomdata/consul.json
   ```

   If you did not install the Consul instances using the Composer bootstrap installation procedure, its custom configuration file might have a different name and location.
4. Configure the Consul custom configuration file for each Consul instance so it includes these lines:

   ```
   {  
   .........  
   "node_name": "<node-name>"  
   "bind_addr": "0.0.0.0",  
   "bootstrap": false,  
   "client_addr": "0.0.0.0",  
   "retry_join": [  
   "<host-ip-address-1>",  
   "<host-ip-address-2>",  
   "<host-ip-address-n>"  
   ],  
   "server": true  
   .........  
   }
   ```

   The `<node-name>` settings for each Consul node should be unique within the cluster. Each Consul instance in the cluster should have a different name.

   A bind address (`bind_addr`) and client address (`client_addr`) of `0.0.0.0` allow the Consul to listen over all network interfaces. The `bind_addr` setting can be limited to the host's IP address instead.

   The `bootstrap` setting should be set to `true` on one node in the cluster only. Set it to `false` on all other cluster nodes.

   For the `retry_join` option, list all the Composer host IP addresses in the cluster. At least one must be listed. If you are using cloud-hosted instances such as AWS or GCE, the `retry_join` option can be changed to something like this (assuming each cluster node is an AWS EC2 instance and has a `tag_key` called `Role` that is assigned to `zoomdata-cluster-node`):

   ```
   .........  
   "retry_join": [  
   "provider=aws tag_key=Role tag_value=zoomdata-cluster-node"  
   ],  
   .........
   ```

1. Restart each Consul instance by entering the following command:

```
sudo systemctl restart consul
```

Wait for several seconds for the cluster to form.

1. Then, validate the cluster by entering the following command:

```
#/opt/zoomdata/bin/zoomdata-consul members
```

The following shows sample output from this command:

| Node | Address | Status | Type | Build | Protocol | DC | Segment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `node-1` | `10.0.0.1:8301` | `alive` | `server` | `1.2.2` | `2` | `dc1` | `<all>` |
| `node-3` | `10.0.0.3:8301` | `alive` | `server` | `1.2.2` | `2` | `dc1` | `<all>` |
| `node-2` | `10.0.0.2:8301` | `alive` | `server` | `1.2.2` | `2` | `dc1` | `<all>` |

1. When the Consul cluster has formed correctly, restart all the Composer microservices for the instance. See [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).

**Step 8: Vacuum the Metadata Store**

Logi Analytics highly recommends that you vacuum the Composer PostgreSQL metadata store after every upgrade. Vacuuming the metadata store optimizes it by maximizing database performance and minimizing the disk space it uses. The following simple procedure recollects metadata store statistics and "vacuums" the unused or dead rows in the database.

![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg) This procedure blocks writing to the database. Consequently, work with the database is impossible until the procedure completes.

![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg) This procedure only works for a PostgreSQL database.

![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg)Logi Analytics tested this procedure after an upgrade to Composer 5.9. on a machine with 2.6 GHz 6-Core Intel Core i7, 16 GB 2667 MHz DDR4, and SSD storage. The tested database contained 300 accounts, 4800 users, 60,000 sources, 9000 dashboards with 30 visuals each. The procedure took 5-10 minutes.

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

**Step 9: Enable and Start All Composer Microservices**

After the upgrade, you must enable and start all Composer microservices. Run the commands described in this section.

To enable all Composer microservices, enter the following command:

```
sudo systemctl enable $(systemctl list-unit-files | grep zoomdata | grep edc | awk '{print $1}')
```

To start all Composer microservices, enter the following command:

```
sudo systemctl start $(systemctl list-unit-files | grep zoomdata | grep edc | awk '{print $1}')
```
