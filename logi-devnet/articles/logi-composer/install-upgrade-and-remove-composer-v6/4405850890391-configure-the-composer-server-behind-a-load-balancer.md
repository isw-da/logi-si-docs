---
title: "Configure the Composer Server Behind a Load Balancer"
id: 4405850890391
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405850890391-Configure-the-Composer-Server-Behind-a-Load-Balancer
updated_at: 2021-09-21T01:26:50Z
---

# Configure the Composer Server Behind a Load Balancer

# Configure the Composer Server Behind a Load Balancer

Load balancing helps you to scale Composer to hundreds of users. You can use load balancing both on-premises and with cloud deployments, meaning you can use load balancing for various environments. When the server is load balanced within your network environment, it includes native SSL support and can proxy WebSocket traffic.

The following diagram depicts a classic load balancing setup.

![](https://devnet.logianalytics.com/hc/article_attachments/4409070306967/load-balancing_672x267.png)

Composer has tested active-active load balancing configuration, which is the particular setup used in the steps below. In addition, the instructions provided below take into account that Composer, when it runs standalone, uses its own dedicated PostgreSQL server as the metadata store (in other words, PostgreSQL was installed as part of the Composer installation process). If you are running in a high availability environment, you will need to use a high availability (clustered) PostgreSQL data store. See [*Configure a High Availability Environment*](https://devnet.logianalytics.com/hc/en-us/articles/4405851083287-Configure-a-High-Availability-Environment).

![](https://devnet.logianalytics.com/hc/article_attachments/4409070299415/criticalicon.gif) Configuring Composer in a distributed environment requires a multi-node license. Be sure you have obtained this before you start. Contact your Logi Analytics Technical Support representative for assistance.

Complete the following steps to configure load balancing in your environment.

**Step 1: Identify or Install the Postgres Metadata Store**

All Composer installations require a Postgres metadata store. If you install Composer on a single server using the supplied bootstrap installation script, this metadata store is installed for you. If you install Composer manually, you must also manually set up the metadata store.

The metadata store should be centrally installed, accessible by all Composer nodes. In a high availability environment, it can be clustered.

When setting up a distributed environment, you need to determine whether the metadata store is installed. If you have already installed Composer and are now trying to set up a distributed environment, there is a good chance that the metadata store was installed with your existing Composer instance or instances.

If this is the first time you have installed Composer, and you want to set up a distributed environment, a new metadata store is required.

* If the metadata store has already been installed, identify its host name and port. Then follow the steps for upgrading a distributed environment. See [*Upgrade a Composer Distributed Environment*](https://devnet.logianalytics.com/hc/en-us/articles/4405851209495-Upgrade-a-Composer-Distributed-Environment).
* If the metadata store has not already been installed, manually install it now. Complete the following sub-steps. Then identify its host name and port.

  1. **Create the Metadata Store User & Stores** - Necessary for all installations.

     The instructions to set up PostgreSQL as Composer's metadata store differ depending on the Linux operating system used by the target server. Select a topic below:

     + [*PostgreSQL Setup for CentOS 7 or 8 Environments*](#PostgreS)
     + [*PostgreSQL Setup for Ubuntu 16 or 18 Environments*](#PostgreS2)

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
  2. **Change Metadata Store Authentication to MD5** -- Not necessary when installing a high availability environment in the cloud.

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
  3. **Configure the Metadata Store for SSL** - Not necessary if installing a high availability environment in the cloud.

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
  4. **Configure the Metadata Store for a Distributed Environment**

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

**Step 2. Install Composer On Your Distributed Servers**

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
2. In each instance, run the following command to set up the environment variables for specific enterprise data connector (EDC) packages:

   ```
   export ZOOMDATA_EDC_PACKAGES='<edc>,<edc>[,<edc>]...'
   ```

   where `<edc>` is the name of the data connector you'd like to install. You must install the PostgreSQL connector because it connects to the metadata store. Data connector names are the same as their connector microservice names without the `zoomdata-edc-` prefix. See [*Composer Data Connector Reference*](https://devnet.logianalytics.com/hc/en-us/articles/4405859436055-Composer-Data-Connector-Reference).
3. Run the bootstrap installation script after exporting the environment variables in the previous steps.

   ```
   curl -O https://composer-repo.logianalytics.com/<v.r>/bootstrap-zoomdata.run  
   sudo -E /bin/sh bootstrap-zoomdata.run
   ```

   where `<v.r>` is the Composer version and release.
4. After the installation, ensure that the following property files are correctly set up on each node. Add or update the properties as necessary. In each, the IP address, port, user name, and password of the PostgreSQL metadata store should be specified.

   In the `/etc/zoomdata/zoomdata.properties` file:

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

1. Restart the Zoomdata service by entering the following command:

```
sudo service zoomdata restart
```

1. Ensure that port 8080 is open on all your back-end servers to support load balancing. If not, run the following command:

```
sudo yum install -y iptables-services  
sudo iptables -I INPUT 1 -p tcp --dport 8080 -j ACCEPT  
sudo service iptables save
```

1. Repeat these steps for every Composer instance (node) in your Composer cluster.

**Step 3. Set Up a Load Balancer**

Set up one or more load balancers in your environment. For a simple load balanced configuration, only one is needed. In a high availability configuration, however, more than one load balancer is recommended; if only a single load balancer is deployed in a high availability environment, you will not be able to access any of the Composer nodes behind it if the load balancer should fail.

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

*Step 4. Copy Specialized Files*

If you have any specialized files for Composer, such as vocabulary files, manually copy them to each instance of Composer in your distributed environment.
