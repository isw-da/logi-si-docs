---
title: "Configure the Composer Server Behind a Load Balancer"
id: 34932685439501
section: "Install, Upgrade, and Remove Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932685439501-Configure-the-Composer-Server-Behind-a-Load-Balancer
updated_at: 2026-05-26T22:10:24Z
---

# Configure the Composer Server Behind a Load Balancer

# Configure the Composer Server Behind a Load Balancer

Load balancing helps you to scale Composer to hundreds of users. You can use load balancing both on-premises and with cloud deployments, meaning you can use load balancing for various environments. When the server is load balanced within your network environment, it includes native SSL support and can proxy WebSocket traffic.

The following diagram depicts a classic load balancing setup.

![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167429762061)

Composer has tested active-active load balancing configuration, which is the particular setup used in the steps below. In addition, the instructions provided below take into account that Composer, when it runs standalone, uses its own dedicated PostgreSQL server as the metadata store (in other words, PostgreSQL was installed as part of the Composer installation process). If you are running in a high availability environment, you will need to use a high availability (clustered) PostgreSQL data store. See [Configure a High Availability Environment](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933027142285-Configure-a-High-Availability-Environment).

**Important:** 
Configuring Composer in a distributed environment requires a multi-node license. Be sure you have obtained this before you start. Contact your insightsoftware Technical Support representative for assistance.

Complete the following steps to configure load balancing in your environment.

[**Step 1: Identify or Install the Postgres Metadata Store**](#)

All Composer installations require a Postgres metadata store. If you install Composer on a single server using the supplied bootstrap installation script, this metadata store is installed for you. If you install Composer manually, you must also manually set up the metadata store.

The metadata store should be centrally installed, accessible by all Composer nodes. In a high availability environment, it can be clustered.

When setting up a distributed environment, you need to determine whether the metadata store is installed. If you have already installed Composer and are now trying to set up a distributed environment, there is a good chance that the metadata store was installed with your existing Composer instance or instances.

If this is the first time you have installed Composer, and you want to set up a distributed environment, a new metadata store is required.

* If the metadata store has already been installed, identify its host name and port. Then follow the steps for upgrading a distributed environment. See  [Upgrade a Composer Distributed Environment](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933183541261--Upgrade-a-Composer-Distributed-Environment).
* If the metadata store has not already been installed, manually install it now. Complete the following sub-steps. Then identify its host name and port.

  1. [**Create the Metadata Store User & Stores** - Necessary for all installations.](#)

     The instructions to set up PostgreSQL as Composer's metadata store differ depending on the Linux operating system used by the target server. Select a topic below:

     + [PostgreSQL Setup for CentOS Environments](#PostgreS)
     + [PostgreSQL Setup for Ubuntu Environments](#PostgreS2)

     ## PostgreSQL Setup for CentOS Environments

     **Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

     1. Add the PostgreSQL Yum repository to CentOS by running this command calling the appropriate PostgreSQL version:

        sudo yum -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-7-x86\_64/pgdg-redhat-repo-latest.noarch.rpm
     2. Install the PostgreSQL client and server packages by running these commands:

        sudo yum -y install epel-release yum-utils
        sudo yum-config-manager --enable pgdg12
        sudo yum install postgresql12-server postgresql12
     3. After installation, initialize the PostgreSQL database:

        sudo /usr/pgsql-12/bin/postgresql12-setup initdb
     4. Start and enable the PostgreSQLmicroservice:

        sudo systemctl enable --now postgresql-12
     5. Confirm that the service started without errors:

        sudo systemctl status postgresql-12

        If necessary, start it:

        sudo systemctl start postgresql-12
     6. If you have a running firewall and remote clients should be able to connect to the PostgreSQL metadata store, modify the firewall to allow the PostgreSQL service:

        sudo firewall-cmd --add-service=postgresql --permanent
        sudo firewall-cmd --reload
     7. If the PostgreSQL database is operating in a cluster, repeat steps 3-6 for each instance of the database.
     8. Set up the PostgreSQL Admin user and password:

        sudo su - postgres
        ~]$ psql -c "alter user postgres with password 'StrongPassword'"
        ALTER ROLE

     ## PostgreSQL Setup for Ubuntu Environments

     **Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

     1. If this is a new server instance, update your current system packages:

        sudo apt update
        sudo apt -y install vim bash-completion wget
        sudo apt -y upgrade

        A reboot is necessary after an upgrade.

        sudo reboot
     2. Import the GPG key and add the appropriate PostgreSQL version repository to your Ubuntu machine. Run the following commands:

        wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add
        echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb\_release -cs`-pgdg main" |sudo tee /etc/apt/sources.list.d/pgdg.list

        The added repository contains many different packages and third-party add-ons, including: `postgresql-client`, `postgresql`, `libpq-dev`, `postgresql-server-dev`, and `pgadmin packages`.
     3. Update the package list and install the PostgreSQL server and client packages:

        sudo apt update
        sudo apt -y install postgresql-12 postgresql-client-12

        The PostgreSQL microservice is started and will start with every system reboot.
     4. If you have a running firewall and remote clients should be able to connect to the PostgreSQL metadata store, modify the firewall to allow the PostgreSQL service port:

        sudo ufw allow 5432/tcp
     5. Test the PostgreSQL connection.

        1. During installation, a user named `postgres` is created automatically with full superadmin access to your entire PostgreSQL instance. Before you switch to this account, your logged in system user should have sudo privileges:

           sudo su - postgres
        2. Replace the `postgres` password with a strong password:

           psql -c "alter user postgres with password 'StrongAdminP@ssw0rd'"
        3. Start PostgreSQL using this command.

           $ psql
        4. Get connection details as shown below.

           postgres=# \conninfo
           You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".
        5. Create a test database called `mytestdb` to see if everything is working.

           postgres=# CREATE DATABASE mytestdb;
           CREATE DATABASE
           postgres=# CREATE USER mytestuser WITH ENCRYPTED PASSWORD 'MyStr0ngP@SS';
           CREATE ROLE
           postgres=# GRANT ALL PRIVILEGES ON DATABASE mytestdb to mytestuser;
           GRANT

           You can list the created databases by running:

           postgres=# \l
        6. Connect to your test database.

           postgres-# \c mytestdb
           You are now connected to database "mytestdb" as user "postgres".
  2. [**Change Metadata Store Authentication to MD5** -- Not necessary when installing a high availability environment in the cloud.](#)

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
  3. [**Configure the Metadata Store for SSL** - Not necessary if installing a high availability environment in the cloud.](#)

     If you have specified SSL connections for the metadata store JDBC connections in `zoomdata.properties` file, the root CA certificate that is used for the PostgreSQL database must be added to the `/opt/zoomdata/.postgresql` directory. This directory does not exist by default and will need to be created. Complete the following steps.

     1. Change to the `/opt/zoomdata` directory as a superuser:

        sudo cd /opt/zoomdata
     2. Create a `.postgresql` subdirectory.

        sudo mkdir .postgresql
     3. Copy the root CA certificate for the PostgreSQL database into the new directory:

        sudo cp root.ca /opt/zoomdata/.postgresql/root.ca
  4. [**Configure the Metadata Store for a Distributed Environment**](#)

     The Composer PostgreSQL data store must be configured so it is available to all Composer instances in a distributed environment. For more information about PostgreSQL high availability clustering, see PostgreSQL documentation on high availability environments.

     **Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

     **Configure the PostgreSQL data store so it is available to all instances**

     1. Edit the `postgresql.conf` file using the appropriate version and paths:

        vi /var/lib/pgsql/12/data/postgresql.conf
     2. Set the following property in `postgresql.conf` and save the file.

        listen\_address='\*'
     3. Edit the `pg_hba.conf file`:

        vi /var/lib/pgsql/12/data/pg\_hba.conf
     4. Add the following to the `pg_hba.conf file`:

        # TYPE DATABASE USER ADDRESS METHOD
        # IPv4 local connections
        host all all 0.0.0.0 /0 md5
     5. Save the `pg_hba.conf` file.
     6. Restart the PostgreSQL service:

        sudo service postgresql-12 restart

[**Step 2. Install Composer On Your Distributed Servers**](#)

Intra-service communication must be enabled by making any necessary networking (ports) and firewall changes.

**Deploy multiple** Composer **nodes (or instances) in a distributed environment, complete the following steps for each instance**

1. For each instance, run the following commands to set up the environment variables for the installation:

   export ZOOMDATA\_POSTGRES\_HOST=<postgres-host>  
   export ZOOMDATA\_POSTGRES\_PORT=<postgres-port>  
   export ZOOMDATA\_POSTGRES\_USER=<postgres-db-username>  
   export ZOOMDATA\_POSTGRES\_PASS=<postgres-db-password>

   where:

   * `<postgres-host>` and `<postgres-port>` are the host name and port number of the Composer PostgreSQl metadata store
   * `<postgres-db-username>` and `<postgres-db-password>` are the user name and password required to access the Composer PostgreSQL metadata store.
2. In each instance, run the following command to set up the environment variables for specific enterprise data connector (EDC) packages:

   export ZOOMDATA\_EDC\_PACKAGES='<edc>,<edc>[,<edc>]...'

   where `<edc>` is the name of the data connector you'd like to install. You must install the PostgreSQL connector because it connects to the metadata store. Data connector names are the same as their connector microservice names without the `zoomdata-edc-` prefix. See [Data Connector Reference](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933117968525-Data-Connector-Reference).
3. Run the bootstrap installation script after exporting the environment variables in the previous steps.

   curl -O https://composer-repo.logianalytics.com/<v.r>/bootstrap-zoomdata.run  
   sudo -E /bin/sh bootstrap-zoomdata.run

   where `<v.r>` is the Composer version and release.
4. After the installation, ensure that the following property files are correctly set up on each node. Add or update the properties as necessary. In each, the IP address, port, user name, and password of the PostgreSQL metadata store should be specified.

   **In the** `zoomdata.properties` **file:**

   spring.datasource.url=jdbc:postgresql://<IP-address>:<port>/zoomdata  
   spring.datasource.username=<db-username>  
   spring.datasource.password=<db-password>  
   keyset.destination.params.jdbc\_url=jdbc:postgresql://<IP-address>:<port>/zoomdata-keyset  
   keyset.destination.params.user\_name=<db-username>  
   keyset.destination.params.password=<db-password>  
   keyset.destination.schema=public  
   upload.destination.params.jdbc\_url=jdbc:postgresql://<IP-address>:<port>/zoomdata-upload  
   upload.destination.params.user\_name=<db-username>  
   upload.destination.params.password=<db-password>

   **In the** `query-engine.properties` **file:**

   spring.qe.datasource.jdbcUrl=jdbc:postgresql://<IP-address>:<port>/zoomdata-qe  
   spring.qe.datasource.username=<db-username>  
   spring.qe.datasource.password=<db-password>
5. Ensure that port 8080 is open on all your back-end servers to support load balancing. If not, run the following command:

   sudo iptables -I INPUT 1 -p tcp --dport 8080 -j ACCEPT  
   sudo service iptables save
6. Repeat these steps for every Composer instance (node) in your Composer cluster.

[**Step 3. Set Up a Load Balancer**](#)

Set up one or more load balancers in your environment. For a simple load balanced configuration, only one is needed. In a high availability configuration, however, more than one load balancer is recommended; if only a single load balancer is deployed in a high availability environment, you will not be able to access any of the Composer nodes behind it if the load balancer should fail.

The following steps provide an example of setting up HAProxy as a load balancer. Regardless of what kind of load balancer you use, ensure that port 443 is open on it.

**Set up an HAProxy load balancer**

1. On your machine, run the following command to install HAProxy:

   sudo yum install haproxy
2. Navigate to the HAProxy folder.

   cd /etc/haproxy
3. Create a certificate or copy an existing certificate to the `/etc/haproxy` folder. If you need to create a certificate, run the following commands:

   sudo openssl genrsa -out ca.key 1024  
   sudo openssl req -new -key ca.key -out ca.csr  
   sudo openssl x509 -req -days 365 -in ca.csr -signkey ca.key -out ca.crt  
   sudo vi cert.pem #Create and save an empty file  
   sudo chmod a+w cert.pem  
   sudo cat ca.key ca.crt > cert.pem
4. In the same folder, replace the contents of the `haproxy.cfg` file with the contents of the [Composer haproxy configuration file](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167966138893). In the file, replace the `<node1-ip>` and `<node2-ip>` with the IP addresses of your servers. If you have more than two servers, add additional lines for each server.
5. Save your changes and exit the file.
6. Start the HAProxy microservice

   sudo service haproxy restart
7. Use the following command to configure the HAProxy microservice to start automatically in CentOS environments:

   sudo systemctl enable haproxy
8. Ensure that port 443 is open on your load balancer. If not, run the following command:

   sudo iptables -I INPUT 1 -p tcp --dport 443 -j ACCEPT  
   sudo service iptables save

For assistance with configuring SAML for use with HAProxy, contact insightsoftware Technical Support.

[*Step 4. Copy Specialized Files*](#)

If you have any specialized files for Composer, such as vocabulary files, manually copy them to each instance of Composer in your distributed environment.
