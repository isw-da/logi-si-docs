---
title: "Configure a High Availability Environment"
id: 4405851083287
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851083287-Configure-a-High-Availability-Environment
updated_at: 2021-09-21T01:28:47Z
---

# Configure a High Availability Environment

# Configure a High Availability Environment

A high availability environment includes multiple Composer nodes, each with its own set of microservices. This ensures that a microservice is available at all times, somewhere in the cluster.

A high-availability load balancer is required to distribute the network traffic across your user-facing Composer nodes. If only a single load balancer is deployed in a high availability environment, you will not be able to access any of the Composer nodes behind it if the load balancer should fail. Microservice load balancing and failover occur automatically within the Composer nodes themselves.

Different numbers of different types of microservices can be defined for the Composer nodes, although at least two of each must be installed. You can monitor all microservices and collect diagnostic trace information for them using the Service Monitor in conjunction with the tracing microservice. You can maintain properties for microservices of a given type in a single location in the Service Monitor. For example, if you have two query engine microservices running in your high availability environment, you can change the properties for both microservices in a single location, ensuring that the query engine microservices operate in the same manner across the product nodes.

In addition:

* At least one configuration server (`config-server`) must be installed and started in the high availability environment.
* Only one Service Monitor (`admin-server`) should be installed and started in the high availability environment. The Service Monitor is not required, but is helpful.
* The Consul's UI is available through port 8500 and is a lighter alternative to the Service Monitor. To ensure there is no single point of failure, Composer recommends that the Consul instance (`zoomdata-consul`) and the PostgreSQL metadata repository be configured as clusters external to the Composer nodes. For information, see <https://www.consul.io/commands/join> (`zoomdata-consul join <ip-address>`) and <https://www.postgresql.org/docs/12/high-availability.html>.
* Intra-service communication must be enabled by making any necessary networking (ports) and firewall changes.

The following diagram depicts a classic high availability setup. (In this diagram, the Consul cluster is configured separately.)

![](https://devnet.logianalytics.com/hc/article_attachments/4409054859159/ha-configure_864x495.png)

![](https://devnet.logianalytics.com/hc/article_attachments/4409070299415/criticalicon.gif) Configuring Composer in a distributed environment requires a multi-node license. Be sure you have obtained this before you start. Contact your Logi Analytics Technical Support representative for assistance.

Complete the following steps to set up a high availability Composer environment. (To upgrade an existing high availability environment, see [*Upgrade a Composer Distributed Environment*](https://devnet.logianalytics.com/hc/en-us/articles/4405851209495-Upgrade-a-Composer-Distributed-Environment)).

**Step 1: Identify or Install the Postgres Metadata Store**

All Composer installations require a Postgres metadata store. If you install Composer on a single server using the supplied bootstrap installation script, this metadata store is installed for you. If you install Composer manually, you must also manually set up the metadata store.

The metadata store should be centrally installed, accessible by all Composer nodes. In a high availability environment, it can be clustered.

When setting up a distributed environment, you need to determine whether the metadata store is installed. If you have already installed Composer and are now trying to set up a distributed environment, there is a good chance that the metadata store was installed with your existing Composer instance or instances.

If this is the first time you have installed Composer, and you want to set up a distributed environment, a new metadata store is required.

* If the metadata store has already been installed, identify its host name and port. Then follow the steps for upgrading a distributed environment. See [*Upgrade a Composer Distributed Environment*](https://devnet.logianalytics.com/hc/en-us/articles/4405851209495-Upgrade-a-Composer-Distributed-Environment).
* If the metadata store has not already been installed, manually install it now. Complete the following sub-steps. Then identify its host name and port.

  1. Set up the Metadata Store - Necessary for all installations.

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
  4. **Configure the Metadata Store for a Distributed Environment** - Not necessary if installing a high availability environment in the cloud.

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
  5. **Create user and Database** - Not necessary if installing a high availability environment in the cloud.

     The Composer PostgreSQL data store must be configured so it is available to all Composer instances in a distributed environment. For more information about PostgreSQL high availability clustering, see <https://www.postgresql.org/docs/12/high-availability.html>.

     To create users and databases in the PostgreSQL data store so they are available to all Composer instances:

     ```
     CREATE USER zoomdata WITH PASSWORD 'StrongZoomdataPassword';  
     CREATE DATABASE "zoomdata" WITH OWNER zoomdata;  
     CREATE DATABASE "zoomdata-upload" WITH OWNER zoomdata;  
     CREATE DATABASE "zoomdata-keyset" WITH OWNER zoomdata;  
     CREATE DATABASE "zoomdata-auth" WITH OWNER zoomdata;  
     CREATE DATABASE "zoomdata-qe" WITH OWNER zoomdata;  
     CREATE DATABASE "zoomdata-user-auditing" WITH OWNER zoomdata;
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
4. Run the bootstrap installation script after exporting the environment variables in the previous steps.

   ```
   curl -O https://composer-repo.logianalytics.com/<v.r>/bootstrap-zoomdata.run  
   sudo -E /bin/sh bootstrap-zoomdata.run
   ```

   where `<v.r>` is the Composer version and release.
5. After the installation, ensure that the following property files are correctly set up on each node. Add or update the properties as necessary. In each, the IP address, port, user name, and password of the PostgreSQL metadata store should be specified.

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

1. Repeat these steps for every Composer instance (node) in your Composer cluster. For additional information on how many nodes to deploy in a high availability environment, see [*Determine How Many Nodes to Deploy*](https://devnet.logianalytics.com/hc/en-us/articles/4405851082263-Determine-How-Many-Nodes-to-Deploy).

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

**Step 5. Configure Consul Services for High Availability**

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

**Step 6. Install and Configure the Configuration Microservice On Each Node**

Complete the following steps.

1. **Set Up the Configuration Microservice Metadata Store or Repository**

   Before you can install and start Composer's configuration microservice, you must set up a PostgreSQL metastore or a GitHub repository to store Composer property metadata. A separate PostgreSQL database or a separate GitHub repository must be configured.

   See the following sections:

   * [*PostgreSQL Setup for CentOS 7 or 8 Environments*](#PostgreS)
   * [*GitHub Repository Setup Notes*](#GitHub)

   ## PostgreSQL Database Setup Notes

   If you elect to persist property metadata to a PostgreSQL metastore:

   1. Configure a separate database and make it accessible to the connection user account:

      ```
      CREATE DATABASE <composer-config> WITH OWNER <db_username>;
      ```

      where `<composer-config>` is the name of the PostgreSQL database and `<db_username>` is the connection user account name.
   2. Add the following properties to the Composer`config-server.properties` file, located in the `/etc/zoomdata` directory:

      ```
      # metadata storage settings  
      spring.datasource.url=jdbc:postgresql://localhost:5432/<composer-config>  
      spring.datasource.username=<db_username>  
      spring.datasource.password=<db_password>
      ```

      Substitute the connection user account name and password you set up in Step 1 for `<db_username>` and `<db_password>`. Substitute the name of the PostgreSQL database for `<composer-config>`.
   3. Save the properties file. You will restart the configuration microservice when you configure it. See [*Configure and Start the Configuration Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4405859471255-Configure-and-Start-the-Configuration-Microservice).

   ## GitHub Repository Setup Notes

   If you elect to persist property metadata to a GitHub repository:

   1. Add the following properties to the Composer`config-server.properties` file, located in the `/etc/zoomdata` directory:

      ```
      # metadata storage settings  
      spring.cloud.config.server.git.uri=<repo_uri>
        
      spring.cloud.config.server.git.skipSslValidation=true
        
      spring.cloud.config.server.git.username=<repo_username>
        
      spring.cloud.config.server.git.password=<repo_password>
      ```

      Substitute the repository user account name and password for `<repo_username>` and `<repo_password>`. Substitute the URI of the repository for `<repo_uri>` (for example, `https://example.com/my/repo`).

      Additional and advanced configuration information can be found in [Spring.io's documentation](https://cloud.spring.io/spring-cloud-config/multi/multi__spring_cloud_config_server.html#_git_backend).
   2. Save the properties file. You will restart the configuration microservice when you configure it. See [*Configure and Start the Configuration Microservice*](https://devnet.logianalytics.com/hc/en-us/articles/4405859471255-Configure-and-Start-the-Configuration-Microservice).
2. **Install, Configure, and Start the Configuration Microservice**

   To install, configure, and start the Composer configuration microservice:

   1. Verify that you have set up a PostgreSQL metastore or a GitHub repository to store the property metadata. See [*Set Up the Configuration Microservice Metadata Store or Repository*](https://devnet.logianalytics.com/hc/en-us/articles/4405859472535-Set-Up-the-Configuration-Microservice-Metadata-Store-or-Repository).
   2. Open the SSH client associated with your Composer instance.
   3. Configure all installed and enabled Composer microservices to use the Composer configuration microservice. Run the following script:

      ```
      for i in $(systemctl list-unit-files | grep zoomdata | grep enabled | awk '{print $1}'|sed -e 's/\.service/.properties/g' -e 's/zoomdata\-//g');  
      do  
      echo "config-server.enabled=true">>/etc/zoomdata/$i;  
      done
      ```
   4. Install, enable and start the Composer configuration microservice. Enter the following commands:

      ```
      sudo yum install zoomdata-config-server \  
      && systemctl enable zoomdata-config-server \  
      && systemctl start zoomdata-config-server
      ```

      ![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg) After starting the configuration microservice with a valid database configuration, the microservice should connect to the database and create a properties table.
   5. Restart all the other Composer microservices. Enter the following command:

      ```
      sudo systemctl restart $(systemctl list-unit-files | grep zoomdata | grep enabled | awk '{print $1}')
      ```

      See also [*Restart Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851094679-Restart-Composer-Microservices).

**Step 7. Install and Configure the Service Monitor (Optional)**

The Composer Service Monitor microservice is not installed as part of a default Composer installation. The microservice name is `zoomdata-admin-server`.

To install, configure, and start the Service Monitor:

1. Open your SSH client.
2. Use the following command to install the Composer Service Monitor in a CentOS environment:

   ```
   sudo yum install zoomdata-admin-server -y
   ```

   Use the following command to install the Composer Service Monitor in an Ubuntu environment:

   ```
   sudo apt-get install zoomdata-admin-server
   ```
3. After the Service Monitor is installed, you must specify a user name and password in its properties file. The properties file is called `admin-server.properties` and can be found in the `/etc/zoomdata/` directory. If the properties file is not there, create it. The properties that must be defined are:

   * `monitor.user.name=<username>`
   * `monitor.user.password=<password>`

   Edit the properties file with a text editor and substitute a Service Monitor user name for `<username>` and its associated password for `<password>`. The user name and password can be any user name and password you want.

   When you have finished, save the file.
4. Add the following properties to the `zoomdata.properties` file, located in the `/etc/zoomdata` directory. These properties ensure that the Service Monitor has access to the Composer server actuator endpoints.

   * `actuator.user.name=<Composer-admin-username>`
   * `actuator.user.password=<Composer-pswd>`
   * `actuator.logging.external-file=<log-file-path>`

   Edit the properties file and substitute the valid user name and password of a Composer administrator for `<Composer-admin-username>` and `<Composer-pswd>`. If the default Composer log file path is not used for your installation, substitute your custom log file path for `<log-file-path>` (the default log file path is `/opt/zoomdata/logs/zoomdata.log`).

   ![](https://devnet.logianalytics.com/hc/article_attachments/4409054855575/noteicon.jpg) Setting these properties exposes valid Composer credentials as plain text in both the properties file and as tags in the Composer Consul. Anyone in your network with the ability to communicate directly with the Consul API or view the Consul UI will be able to see these values.

   When finished, save the file.
5. Start the microservice. For example, use the following command to start the Composer Service Monitor using `systemd` in a CentOS or Ubuntu environment:

   ```
   sudo systemctl start zoomdata-admin-server
   ```

   See also [*Start Composer Microservices*](https://devnet.logianalytics.com/hc/en-us/articles/4405851100567-Start-Composer-Microservices).

Additional high availability information, can be found in these topics:

* [*Determine How Many Nodes to Deploy*](https://devnet.logianalytics.com/hc/en-us/articles/4405851082263-Determine-How-Many-Nodes-to-Deploy)
* [*Add Nodes to an Existing High Availability Installation*](https://devnet.logianalytics.com/hc/en-us/articles/4405859366167-Add-Nodes-to-an-Existing-High-Availability-Installation)
* [*Remove Nodes from a High Availability Environment*](https://devnet.logianalytics.com/hc/en-us/articles/4405859367319-Remove-Nodes-from-a-High-Availability-Environment)
* [*Migrate Properties to the Configuration Server*](https://devnet.logianalytics.com/hc/en-us/articles/4405859368471-Migrate-Properties-to-the-Configuration-Server)
