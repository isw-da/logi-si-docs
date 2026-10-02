> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Distributed Environment Support

You can deploy Self-Service Analytics microservices in a distributed environment. Such an environment ensures that you can minimize the downtime caused by:

* hardware or software failures due to excessive resource use or other events
* software upgrades or updates

You have two options for setting up a distributed Self-Service Analytics environment:

* **Load balancing:** Load balancing helps you scale Self-Service Analytics for hundreds of users. You can use load balancing both on-premises and with cloud deployments. A single set of microservices communicate with each other in a monolithic flow.

  For more information, see [Configure the Self-Service Analytics Server Behind a Load Balancer](#configure-the-self-service-analytics-server-behind-a-load).

* **High Availability:** A high availability environment includes multiple Self-Service Analytics nodes, each with its own set of microservices. This ensures that a microservice is available at all times, somewhere in the cluster. Each microservice communicates with others using service discovery.

  Different numbers of different types of microservices can be defined for the Self-Service Analytics nodes, although at least two of each must be installed.

  A high-availability load balancer is required to distribute the network traffic across your user-facing Self-Service Analytics nodes. If only a single load balancer is deployed in a high availability environment, you will not be able to access any of the Self-Service Analytics nodes behind it if the load balancer should fail. Microservice load balancing and failover occur automatically within the Self-Service Analytics nodes themselves.

  For more information, see [Configure a High Availability Environment](#configure-a-high-availability-environment).

If you have the configuration microservice configured and running, you can maintain properties for microservices of a given type in a single location in the Service Monitor. For example, if you have two query engine microservices running in your high availability environment, you can change the properties for both microservices in a single location, ensuring that the query engine microservices operate in the same manner across the product nodes. A `config-server-upload.jar` utility is provided that can be used to migrate the microservice properties from your standalone Self-Service Analytics servers to the Self-Service Analytics configuration data in the high availability PostgreSQL data store, where the configuration microservice can maintain them. For more information see [Migrate Properties to the Configuration Server](#migrate-properties-to-the-configuration-server).

<h2 id="configure-a-distributed-self-service-analytics-environment">
  Configure a Distributed Self-Service Analytics Environment
</h2>

The Self-Service Analytics uses independent Java microservices so you can set up a distributed, load-balanced, or high-availability environment tailored to your needs. Here's how they're organized for you to plan with when considering application availability:

* Core microservices - application components of Self-Service Analytics. These services provide key functionality in the application.
* Platform microservices - services that facilitate the operation and coordination between core microservices.
* Management microservices - services that provide views and controls for administration and troubleshooting of core microservices.

The communication protocols used by the microservices include WebSockets (for realtime bidirectional communication) and HTTP/HTTPS.

A metadata store is also needed to store Self-Service Analytics's metadata, application configuration data, and application trace data. Self-Service Analytics centralizes its metadata store in a relational database and includes an internal messaging queue.

The microservices and metadata store are depicted in the following diagram:

<img src="https://mintcdn.com/insightsoftware/sLccJ1EJ28cO5lT_/simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagrams/ha-microservices.png?fit=max&auto=format&n=sLccJ1EJ28cO5lT_&q=85&s=1608d5f735df61d394d8d2ff62a3e07e" alt="" width="576" height="227" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagrams/ha-microservices.png" />

You have two options for setting up a distributed Self-Service Analytics environment:

* **Load Balancing:** Load balancing helps you scale Self-Service Analytics for hundreds of users. You can use load balancing both on-premises and with cloud deployments. A single set of microservices communicate with each other in a monolithic flow.

  For more information, see [Configure the Self-Service Analytics Server Behind a Load Balancer](#configure-the-self-service-analytics-server-behind-a-load).

* **High Availability:** A high availability environment includes multiple Self-Service Analytics nodes, each with its own set of microservices. This ensures that a microservice is available at all times, somewhere in the cluster. Each microservice communicates with others using service discovery.

  Different numbers of different types of microservices can be defined for the Self-Service Analytics nodes, although at least two of each must be installed.

  A high-availability load balancer is required to distribute the network traffic across your user-facing Self-Service Analytics nodes. If only a single load balancer is deployed in a high availability environment, you will not be able to access any of the Self-Service Analytics nodes behind it if the load balancer should fail. Microservice load balancing and failover occur automatically within the Self-Service Analytics nodes themselves.

  For more information, see [Configure a High Availability Environment](#configure-a-high-availability-environment).

Both load balancing and high availability require a centralized metadata store and a multi-node license. In a high availability environment, the metadata store can be clustered.

The configuration of load balancing and high availability are similar, but the high availability configuration is more complex in regards to its Consul configuration. To configure either, select one of the links above.

If you already have a distributed Self-Service Analytics environment in place, read [Upgrade a Self-Service Analytics Distributed Environment](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/upgrading-server#upgrade-a-self-service-analytics-distributed-environment) to upgrade it.

<h2 id="configure-a-high-availability-environment">
  Configure a High Availability Environment
</h2>

A high availability environment includes multiple Self-Service Analytics nodes, each with its own set of microservices. This ensures that a microservice is available at all times, somewhere in the cluster.

A high-availability load balancer is required to distribute the network traffic across your user-facing nodes. If only a single load balancer is deployed in a high availability environment, you will not be able to access any of the Self-Service Analytics nodes behind it if the load balancer should fail. Microservice load balancing and failover occur automatically within the nodes themselves.

Different numbers of different types of microservices can be defined for the Self-Service Analytics nodes, although at least two of each must be installed. You can monitor all microservices and collect diagnostic trace information for them using the Service Monitor in conjunction with your distributed tracing services. You can maintain properties for microservices of a given type in a single location in the Service Monitor. For example, if you have two query engine microservices running in your high availability environment, you can change the properties for both microservices in a single location, ensuring that the query engine microservices operate in the same manner across the product nodes.

In addition:

* At least one configuration server (`config-server`) must be installed and started in the high availability environment.
* Only one Service Monitor (`admin-server`) should be installed and started in the high availability environment. The Service Monitor is not required, but is helpful.
* The Consul's UI is available through port 8500 and is a lighter alternative to the Service Monitor. To ensure there is no single point of failure, Self-Service Analytics recommends that the Consul instance (`zoomdata-consul`) and the PostgreSQL metadata repository be configured as clusters external to the Self-Service Analytics nodes. For information, see [https://www.consul.io/commands/join](https://www.consul.io/commands/join) (`zoomdata-consul join <ip-address>`) and [https://www.postgresql.org/docs/12/high-availability.html](https://www.postgresql.org/docs/12/high-availability.html).
* Intra-service communication must be enabled by making any necessary networking (ports) and firewall changes.

<Note>
  Self-Service Analytics's microservice architecture supports client-side load balancing for all microservices except Composer Web.
</Note>

The following diagram depicts a classic high availability setup. (In this diagram, the Consul cluster is configured separately.)

<img src="https://mintcdn.com/insightsoftware/GTXU--ZlYc3DodOR/simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagrams/ha-configure.png?fit=max&auto=format&n=GTXU--ZlYc3DodOR&q=85&s=5698c28b8797f5b4a8c4bb72e1c4edc8" alt="" width="864" height="495" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/diagrams/ha-configure.png" />

Complete the following steps to set up a high availability Self-Service Analytics environment. (To upgrade an existing high availability environment, see [Upgrade a Self-Service Analytics Distributed Environment](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/upgrading-server#upgrade-a-self-service-analytics-distributed-environment)).

**Step 1: Identify or Install the Postgres Metadata Store**

All Self-Service Analytics installations require a Postgres metadata store. If you install Self-Service Analytics on a single server using the supplied bootstrap installation script, this metadata store is installed for you. If you install Self-Service Analytics manually, you must also manually set up the metadata store.

The metadata store should be centrally installed, accessible by all Self-Service Analytics nodes. In a high availability environment, it can be clustered.

When setting up a distributed environment, you need to determine whether the metadata store is installed. If you have already installed Self-Service Analytics and are now trying to set up a distributed environment, there is a good chance that the metadata store was installed with your existing Self-Service Analytics instance or instances.

If this is the first time you have installed Self-Service Analytics, and you want to set up a distributed environment, a new metadata store is required.

* If the metadata store has already been installed, identify its host name and port. Then follow the steps for upgrading a distributed environment. See [Upgrade a Self-Service Analytics Distributed Environment](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/upgrading-server#upgrade-a-self-service-analytics-distributed-environment).

* If the metadata store has not already been installed, manually install it now. Complete the following sub-steps. Then identify its host name and port.

  1. Set up the Metadata Store - Necessary for all installations.

     The instructions to set up PostgreSQL as Self-Service Analytics's metadata store differ depending on the Linux operating system used by the target server. Select a topic below:

     * [PostgreSQL Setup for CentOS Environments](#postgresql-setup-for-centos-environments)
     * [PostgreSQL Setup for Ubuntu Environments](#postgresql-setup-for-ubuntu-environments)

     ### PostgreSQL Setup for CentOS Environments

     <Note>
       New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment, you can retain your existing PostgreSQL version.
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

     ### PostgreSQL Setup for Ubuntu Environments

     <Note>
       New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment, you can retain your existing PostgreSQL version.
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

  2. **Change Metadata Store Authentication to MD5** -- Not necessary when installing a high availability environment in the cloud.

     If you installed Self-Service Analytics's metadata store on a server running CentOS or RedHat, complete the configuration steps below. If the server is running Ubuntu, ignore these instructions.

     <Note>
       New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment, you can retain your existing PostgreSQL version.
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

  3. **Configure the Metadata Store for SSL** - Not necessary if installing a high availability environment in the cloud.

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

  4. **Configure the Metadata Store for a Distributed Environment** - Not necessary if installing a high availability environment in the cloud.

     The PostgreSQL data store must be configured so it is available to all Self-Service Analytics instances in a distributed environment. For more information about PostgreSQL high availability clustering, see PostgreSQL documentation on high availability environments.

     <Note>
       New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment, you can retain your existing PostgreSQL version.
     </Note>

     **Configure the PostgreSQL data store so it is available to all instances**

     1. Edit the `postgresql.conf` file using the appropriate version and paths:

        ```bash theme={null}
        vi /var/lib/pgsql/12/data/postgresql.conf
        ```

     2. Set the following property in `postgresql.conf` and save the file.

        ```properties theme={null}
        listen_address='*'
        ```

     3. Edit the `pg_hba.conf file`:

        ```bash theme={null}
        vi /var/lib/pgsql/12/data/pg_hba.conf
        ```

     4. Add the following to the `pg_hba.conf file`:

        ```
        # TYPE DATABASE USER ADDRESS METHOD # IPv4 local connections host all all 0.0.0.0 /0 md5
        ```

     5. Save the `pg_hba.conf` file.

     6. Restart the PostgreSQL service:

        ```bash theme={null}
        sudo service postgresql-12 restart
        ```

  5. **Create user and Database** - Not necessary if installing a high availability environment in the cloud.

     The PostgreSQL data store must be configured so it is available to all instances in a distributed environment. For more information about PostgreSQL high availability clustering, see [https://www.postgresql.org/docs/12/high-availability.html](https://www.postgresql.org/docs/12/high-availability.html).

     **Create users and databases in the PostgreSQL data store so they are available to all Self-Service Analytics** **instances**

     ```sql theme={null}
     CREATE USER zoomdata WITH PASSWORD 'StrongZoomdataPassword'; CREATE DATABASE "zoomdata" WITH OWNER zoomdata; CREATE DATABASE "zoomdata-upload" WITH OWNER zoomdata; CREATE DATABASE "zoomdata-keyset" WITH OWNER zoomdata; CREATE DATABASE "zoomdata-auth" WITH OWNER zoomdata; CREATE DATABASE "zoomdata-qe" WITH OWNER zoomdata; CREATE DATABASE "zoomdata-user-auditing" WITH OWNER zoomdata;
     ```

**Step 2. Install Self-Service Analytics On Your Distributed Servers**

Intra-service communication must be enabled by making any necessary networking (ports) and firewall changes.

**Deploy multiple Self-Service Analytics** **nodes (or instances) in a distributed environment, complete the following steps for each instance**

1. For each instance, run the following commands to set up the environment variables for the installation:

   ```bash theme={null}
   export ZOOMDATA_POSTGRES_HOST=<postgres-host>
   export ZOOMDATA_POSTGRES_PORT=<postgres-port>
   export ZOOMDATA_POSTGRES_USER=<postgres-db-username>
   export ZOOMDATA_POSTGRES_PASS=<postgres-db-password>
   ```

   where:

   * `<postgres-host>` and `<postgres-port>` are the host name and port number of the Self-Service Analytics PostgreSQl metadata store
   * `<postgres-db-username>` and `<postgres-db-password>` are the user name and password required to access the Self-Service Analytics PostgreSQL metadata store.

2. In high availability (HA) environments only, run the following commands for each instance to set up the environment variables for the Consul configuration:

   ```bash theme={null}
   export ZOOMDATA_CONSUL_ADDRESS=<instance_ip>:8500
   export ZOOMDATA_CONSUL_CLIENT=0.0.0.0
   ```

   where `<instance_ip>` is the IP address of the Self-Service Analytics instance.

3. In each instance, run the following command to set up the environment variables for specific enterprise data connector (EDC) packages:

   ```bash theme={null}
   export ZOOMDATA_EDC_PACKAGES='<edc>,<edc>[,<edc>]...'
   ```

   where `<edc>` is the name of the data connector you would like to install. You must install the PostgreSQL connector because it connects to the metadata store. Data connector names are the same as their connector microservice names without the `zoomdata-edc-` prefix. See [Data Connector Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference).

4. Run the bootstrap installation script after exporting the environment variables in the previous steps.

   ```bash theme={null}
   curl -O https://composer-repo.logianalytics.com/<v.r>/bootstrap-zoomdata.run
   sudo -E /bin/sh bootstrap-zoomdata.run
   ```

   where `<v.r>` is the Self-Service Analytics version and release.

5. After the installation, ensure that the following property files are correctly set up on each node. Add or update the properties as necessary. In each, the IP address, port, user name, and password of the PostgreSQL metadata store should be specified.

   **In the** `zoomdata.properties` **file:**

   ```properties theme={null}
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

   **In the** `query-engine.properties` **file:**

   ```properties theme={null}
   spring.qe.datasource.jdbcUrl=jdbc:postgresql://<IP-address>:<port>/zoomdata-qe
   spring.qe.datasource.username=<db-username>
   spring.qe.datasource.password=<db-password>
   ```

6. Ensure that port 8080 is open on all your back-end servers to support load balancing. If not, run the following command:

   ```bash theme={null}
   sudo iptables -I INPUT 1 -p tcp --dport 8080 -j ACCEPT
   sudo service iptables save
   ```

7. Repeat these steps for every Self-Service Analytics instance (node) in your Self-Service Analytics cluster. For additional information on how many nodes to deploy in a high availability environment, see [Determine How Many Nodes to Deploy](#determine-how-many-nodes-to-deploy).

**Step 3. Set Up a Load Balancer**

Set up one or more load balancers in your environment. For a simple load balanced configuration, only one is needed. In a high availability configuration, however, more than one load balancer is recommended; if only a single load balancer is deployed in a high availability environment, you will not be able to access any of the Self-Service Analytics nodes behind it if the load balancer should fail.

The following steps provide an example of setting up HAProxy as a load balancer. Regardless of what kind of load balancer you use, ensure that port 443 is open on it.

**Set up an HAProxy load balancer**

1. On your machine, run the following command to install HAProxy:

   ```bash theme={null}
   sudo yum install haproxy
   ```

2. Navigate to the HAProxy folder.

   ```bash theme={null}
   cd /etc/haproxy
   ```

3. Create a certificate or copy an existing certificate to the `/etc/haproxy` folder. If you need to create a certificate, run the following commands:

   ```bash theme={null}
   sudo openssl genrsa -out ca.key 1024
   sudo openssl req -new -key ca.key -out ca.csr
   sudo openssl x509 -req -days 365 -in ca.csr -signkey ca.key -out ca.crt
   sudo vi cert.pem #Create and save an empty file
   sudo chmod a+w cert.pem
   sudo cat ca.key ca.crt > cert.pem
   ```

4. In the same folder, replace the contents of the `haproxy.cfg` file with the contents of the [Self-Service Analytics haproxy configuration file](/simba-embedded-analytics/docs/self-service-analytics/26.3/images/files/haproxy.txt). In the file, replace the `<node1-ip>` and `<node2-ip>` with the IP addresses of your servers. If you have more than two servers, add additional lines for each server.

5. Save your changes and exit the file.

6. Start the HAProxy microservice

   ```bash theme={null}
   sudo service haproxy restart
   ```

7. Use the following command to configure the HAProxy microservice to start automatically in CentOS environments:

   ```bash theme={null}
   sudo systemctl enable haproxy
   ```

8. Ensure that port 443 is open on your load balancer. If not, run the following command:

   ```bash theme={null}
   sudo iptables -I INPUT 1 -p tcp --dport 443 -j ACCEPT
   sudo service iptables save
   ```

For assistance with configuring SAML for use with HAProxy, contact insightsoftware Technical Support.

*Step 4. Copy Specialized Files*

If you have any specialized files for Self-Service Analytics, such as vocabulary files, manually copy them to each instance of Self-Service Analytics in your distributed environment.

**Step 5. Configure Consul Services for High Availability**

You can install individual Consul instances locally for each Self-Service Analytics node and then configure the Consul instances as a cluster for the Self-Service Analytics high availability environment. Before you do, make sure you are familiar with the general clustering techniques used for Consul. See [https://www.consul.io/docs/install/bootstrapping](https://www.consul.io/docs/install/bootstrapping) for more information.

The primary advantage of using a Consul cluster in a high availability environment is that it requires fewer configuration changes to Self-Service Analytics components. Each component will look for the Consul on the localhost interface at port 127.0.0.1. The only configuration necessary is to the Consul cluster nodes themselves.

Another advantage is that each node of the high availability cluster will use several discovered instances of the same component to balance the load and become more tolerant of any component failures.

**Configure a Consul cluster for a Self-Service Analytics** **high availability environment**

1. Install all the individual Consul instances on each node. This happens automatically when you use the bootstrap installation procedure.

2. Make sure that a firewall is opened in your environment for ports 8500, 8300, 8301, and 8302 on all hosts that will form the Consul cluster.

3. Edit the Consul custom configuration file `consul.json` on each node.

   ```bash theme={null}
   vi /etc/zoomdata/consul.json
   ```

   If you did not install the Consul instances using the bootstrap installation procedure, its custom configuration file might have a different name and location.

4. Configure the Consul custom configuration file for each Consul instance so it includes these lines:

   ```json theme={null}
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

   For the `retry_join` option, list all the host IP addresses in the cluster. At least one must be listed. If you are using cloud-hosted instances such as AWS or GCE, the `retry_join` option can be changed to something like this (assuming each cluster node is an AWS EC2 instance and has a `tag_key` called `Role` that is assigned to `zoomdata-cluster-node`):

   ```
   .........
   "retry_join": [
   "provider=aws tag_key=Role tag_value=zoomdata-cluster-node"
   ],
   .........
   ```

5. Restart each Consul instance and wait for several seconds for the cluster to form. Then validate the cluster by entering the following command:

   ```
   #/opt/zoomdata/bin/zoomdata-consul members
   ```

   The following shows sample output from this command:

   | Node | Address | Status | Type | Build | Protocol | DC | Segment |
   | - | - | - | - | - | - | - | - |
   | `node-1` | `10.0.0.1:8301` | `alive` | `server` | `1.2.2` | `2` | `dc1` | `<all>` |
   | `node-3` | `10.0.0.3:8301` | `alive` | `server` | `1.2.2` | `2` | `dc1` | `<all>` |
   | `node-2` | `10.0.0.2:8301` | `alive` | `server` | `1.2.2` | `2` | `dc1` | `<all>` |

6. When the Consul cluster has formed correctly, restart all the microservices for the instance. See [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

**Step 6. Install and Configure the Configuration Microservice On Each Node**

Complete the following steps.

1. **Set Up the Configuration Microservice Metadata Store or Repository**

   Before you can install and start Self-Service Analytics's configuration microservice, you must set up a PostgreSQL metastore or a GitHub repository to store Self-Service Analytics property metadata. A separate PostgreSQL database or a separate GitHub repository must be configured.

   ### PostgreSQL Database Setup Notes

   **If you elect to persist property metadata to a PostgreSQL metastore:**

   1. Configure a separate database and make it accessible to the connection user account:

      ```sql theme={null}
      CREATE DATABASE <composer-config> WITH OWNER <db_username>;
      ```

      where `<composer-config>` is the name of the PostgreSQL database and `<db_username>` is the connection user account name.

   2. Add the following properties to the Self-Service Analytics `config-server.properties` file, located in the `/etc/zoomdata` directory:

      ```
      # metadata storage settings spring.datasource.url=jdbc:postgresql://localhost:5432/<composer-config> spring.datasource.username=<db_username> spring.datasource.password=<db_password>
      ```

      Substitute the connection user account name and password you set up in Step 1 for `<db_username>` and `<db_password>`. Substitute the name of the PostgreSQL database for `<composer-config>`.

   3. Save the properties file. You will restart the configuration microservice when you configure it. See [Configure and Start the Configuration Microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/service-monitor-overview#configure-and-start-the-configuration-microservice).

   ### GitHub Repository Setup Notes

   **If you elect to persist property metadata to a GitHub repository:**

   1. Add the following properties to the Self-Service Analytics `config-server.properties` file, located in the `/etc/zoomdata` directory:

      ```
      # metadata storage settings spring.cloud.config.server.git.uri=<repo_uri> spring.cloud.config.server.git.skipSslValidation=true spring.cloud.config.server.git.username=<repo_username> spring.cloud.config.server.git.password=<repo_password>
      ```

      Substitute the repository user account name and password for `<repo_username>` and `<repo_password>`. Substitute the URI of the repository for `<repo_uri>` (for example, `https://example.com/my/repo`).

      Additional and advanced configuration information can be found in [Spring.io's documentation](https://cloud.spring.io/spring-cloud-config/multi/multi__spring_cloud_config_server.html#_git_backend).

   2. Save the properties file. You will restart the configuration microservice when you configure it. See [Configure and Start the Configuration Microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/service-monitor-overview#configure-and-start-the-configuration-microservice).

2. **Install, Configure, and Start the Configuration Microservice**

   **Install, configure, and start the Self-Service Analytics** **configuration microservice**

   1. Verify that you have set up a PostgreSQL metastore or a GitHub repository to store the property metadata. See [Set Up the Configuration Microservice Metadata Store or Repository](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/service-monitor-overview#set-up-the-configuration-microservice-metadata-store-or).

   2. Open the SSH client associated with your instance.

   3. Configure all installed and enabled microservices to use the configuration microservice. Run the following script:

      ```
      for i in $(systemctl list-unit-files | grep zoomdata | grep enabled | awk '{print $1}'|sed -e 's/\.service/.properties/g' -e 's/zoomdata\-//g');
      do
      echo "config-server.enabled=true">>/etc/zoomdata/$i;
      done
      ```

   4. Each microservice supports two configuration properties related to the configuration microservice:

      * `config-server.enabled`: Enables or disables integration with the configuration microservice. Valid values are `true` (enable integration) and `false` (disable integration). The default is `true`.
      * `config-client.retry.max-attempts`: Sets the maximum number of attempts that should be made to connect to the configuration microservice. The default is 20. The Self-Service Analytics microservice will fail if the number of attempts to connect to the configuration microservice exceeds this value. This property is useful in situations where the configuration microservice starts with a delay. If your microservice fails while waiting for the configuration microservice and you want to give it more time, increase this value.

      Update these properties, as appropriate, for each microservice.

   5. Install, enable and start the configuration microservice. Enter the following commands:

      ```bash theme={null}
      sudo yum install zoomdata-config-server \
      && systemctl enable zoomdata-config-server \
      && systemctl start zoomdata-config-server
      ```

      <Note>
        After starting the configuration microservice with a valid database configuration, the microservice should connect to the database and create a properties table.
      </Note>

   6. Restart all the other microservices. Enter the following command:

      ```bash theme={null}
      sudo systemctl restart $(systemctl list-unit-files | grep zoomdata | grep enabled | awk '{print $1}')
      ```

      See also [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

**Step 7. Install and Configure the Service Monitor (Optional)**

The Self-Service Analytics Service Monitor microservice is not installed as part of a default Self-Service Analytics installation. The microservice name is `zoomdata-admin-server`.

<Note>
  If you are installing Self-Service Analytics in a Windows environment, you can install the Service Monitor as part of running the initial bootstrap script. See [Install Self-Service Analytics - Windows](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-windows) and [Windows Bootstrap Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-windows#windows-bootstrap-reference).
</Note>

**Install, configure, and start the Service Monitor**

1. Open your SSH client.

2. Use the following command to install the Self-Service Analytics Service Monitor in a CentOS environment:

   ```bash theme={null}
   sudo yum install zoomdata-admin-server -y
   ```

   Use the following command to install the Self-Service Analytics Service Monitor in an Ubuntu environment:

   ```bash theme={null}
   sudo apt-get install zoomdata-admin-server
   ```

3. After the Service Monitor is installed, you must specify a user name and password in its properties file. The properties file is called `admin-server.properties` and can be found in the `/etc/zoomdata/` directory (Linux) or the `<install-path>/conf-modify/` directory (Windows). If the properties file is not there, create it. The properties that must be defined are:

   * `monitor.user.name=<username>`
   * `monitor.user.password=<password>`

   Edit the properties file with a text editor and substitute a Service Monitor user name for `<username>` and its associated password for `<password>`. The user name and password can be any user name and password you want.

   When you have finished, save the file.

4. Add the following properties to the `zoomdata.properties` file, located in the `/etc/zoomdata` directory (Linux) or the `<install-path>/conf-modify/` (Windows). These properties ensure that the Service Monitor has access to the Self-Service Analytics server actuator endpoints.

   * `actuator.user.name=<composer-admin-username>`
   * `actuator.user.password=<composer-pswd>`
   * `actuator.logging.external-file=<log-file-path>`

   Edit the properties file and substitute the valid user name and password of a Self-Service Analytics administrator for `<composer-admin-username>` and `<composer-pswd>`. If the default Self-Service Analytics log file path is not used for your installation, substitute your custom log file path for `<log-file-path>`. The default log file path is `/opt/zoomdata/logs/zoomdata.log` for Linux and `<install-path>/logs/zoomdata.log` for Windows.

   <Note>
     Setting these properties exposes valid Self-Service Analytics credentials as plain text in both the properties file and as tags in the Self-Service Analytics Consul. Anyone in your network with the ability to communicate directly with the Consul API or view the Consul UI will be able to see these values.
   </Note>

   When finished, save the file.

5. Start the microservice. For example, use the following command to start the Self-Service Analytics Service Monitor using `systemd` in a CentOS or Ubuntu environment:

   ```bash theme={null}
   sudo systemctl start zoomdata-admin-server
   ```

   See also [Start Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#start-microservices).

Additional high availability information can be found in these topics:

* [Determine How Many Nodes to Deploy](#determine-how-many-nodes-to-deploy)
* [Add Nodes to an Existing High Availability Installation](#add-nodes-to-an-existing-high-availability-installation)
* [Remove Nodes from a High Availability Environment](#remove-nodes-from-a-high-availability-environment)
* [Migrate Properties to the Configuration Server](#migrate-properties-to-the-configuration-server)

## Configure Load Balancing in a High Availability Environment

A high availability environment is designed to ensure concurrent users having access to the same microservices at the same time, including the COMPOSER-WEB service. To have a high availability environment, you need to [Configure a High Load Environment](#configure-a-high-load-environment) along with setting up at least two instances of each microservice, including COMPOSER-WEB. These services must be accessible through a Load Balancer.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/highavailibilityloadbalancer.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=92552a22931b5efe92131cc06ab8fad1" alt="Use this as a guide to set up your HA environment for your microservices." width="1042" height="683" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/highavailibilityloadbalancer.png" />

<Warning>
  This is different from how you [Configure a High Load Environment](#configure-a-high-load-environment). Here you add multiple instances of each microservice.
</Warning>

### Setting Up Your Load Balancer

The following steps provide an example of setting up HAProxy as a load balancer. Regardless of what kind of load balancer you use, ensure that its port 443 is open.

**Set up an HAProxy load balancer**

1. On your machine, run the following command to install HAProxy:

   ```bash theme={null}
   sudo yum install haproxy
   ```

2. Navigate to the HAProxy folder.

   ```bash theme={null}
   cd /etc/haproxy
   ```

3. Create a certificate or copy an existing certificate to the `/etc/haproxy` folder. If you need to create a certificate, run the following commands:

   ```bash theme={null}
   sudo openssl genrsa -out ca.key 1024
   sudo openssl req -new -key ca.key -out ca.csr
   sudo openssl x509 -req -days 365 -in ca.csr -signkey ca.key -out ca.crt
   sudo vi cert.pem #Create and save an empty file
   sudo chmod a+w cert.pem
   sudo cat ca.key ca.crt > cert.pem
   ```

4. In the same folder, replace the contents of the `haproxy.cfg` file with the contents of the [Self-Service Analytics haproxy configuration file](/simba-embedded-analytics/docs/self-service-analytics/26.3/images/files/haproxy.txt). In the file, replace the `<node1-ip>` and `<node2-ip>` with the IP addresses of your servers. If you have more than two servers, add additional lines for each server.

5. Save your changes and exit the file.

6. Start the HAProxy microservice.

   ```bash theme={null}
   sudo service haproxy restart
   ```

7. Use the following command to configure the HAProxy microservice to start automatically in CentOS environments:

   ```bash theme={null}
   sudo systemctl enable haproxy
   ```

8. Ensure that port 443 is open on your load balancer. If not, run the following command:

   ```bash theme={null}
   sudo iptables -I INPUT 1 -p tcp --dport 443 -j ACCEPT
   sudo service iptables save
   ```

For assistance with configuring SAML for use with HAProxy, contact insightsoftware Technical Support.

<h2 id="determine-how-many-nodes-to-deploy">
  Determine How Many Nodes to Deploy
</h2>

To effectively implement high availability in your Self-Service Analytics environment, at least two nodes, each containing the following microservices, are required.

* Web App microservice
* Query Engine microservice
* Data Writer microservice
* Appropriate connector microservices for your installation
* Configuration microservice

The Service Monitor and Screenshot microservices, as well as distributed tracing services, are not required on every node. Install these microservices on at least two nodes in your cluster to ensure that management of the nodes is retained should one node fail.

Finally, the Consul instance and the PostgreSQL data store used to store metadata, configuration data, and tracing data must be available to all the nodes in your Self-Service Analytics cluster. We recommend that you cluster the Consul instance and your PostgreSQL data store to ensure there is no single point of failure.

<h2 id="add-nodes-to-an-existing-high-availability-installation">
  Add Nodes to an Existing High Availability Installation
</h2>

**Add Self-Service Analytics** **nodes (or instances) to an existing high availability environment**

1. If not already installed, install the Self-Service Analytics instance as though it were a single instance (and not running in a high availability environment). See [Install Self-Service Analytics - Linux](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov).

2. Edit the `zoomdata.properties` and `query-engine.properties` files and ensure that the JDBC settings point to the PostgreSQL data store shared by the entire Self-Service Analytics cluster. Also ensure that the user name and password used to access the PostgreSQL data store are correct in these files. For information about the shared PostgreSQL data store, see [Configure a High Availability Environment](#configure-a-high-availability-environment).

3. Edit the `consul.json` file on the instance you are adding.

   ```bash theme={null}
   vi /etc/zoomdata/consul.json
   ```

4. Verify the `consul.json` file looks like this:

   ```json theme={null}
   {
   "bind_addr": "0.0.0.0",
   "bootstrap": false,
   "bootstrap_expect": 2,
   "client_addr": "0.0.0.0",
   "data_dir": "/opt/zoomdata/data/consul",
   "server": true
   }
   ```

   A bind address (`bind_addr`) and client address (`client_addr`) of `0.0.0.0` allow the Consul to listen over all network interfaces. Depending on your network setup, you may want to explicitly specify an IP address for this.

   The `bootstrap_expect` value is the total number of Self-Service Analytics nodes (instances) in your Self-Service Analytics cluster and must be the same value on every instance in the cluster.

5. Restart all the Self-Service Analytics microservices for the instance. See [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

6. Join each instance to the Consul cluster by running this command:

   ```
   /opt/zoomdata/bin/zoomdata-consul join <external-Consul-node-IP>
   ```

   You can verify that the node has joined the Consul cluster by running this command:

   ```
   /opt/zoomdata/bin/zoomdata-consul members
   ```

<h2 id="remove-nodes-from-a-high-availability-environment">
  Remove Nodes from a High Availability Environment
</h2>

**Remove Self-Service Analytics** **nodes (or instances) from a high availability environment**

1. Run the following command on the instance:

   ```
   /opt/zoomdata/bin/zoomdata-consul leave -http-addr=http://<external-Consul-node-IP>:<port>
   ```

   where `<external-Consul-node-IP>` is the IP address of the Consul used by the high availability environment.

2. If the instance you are removing will be run standalone, edit the `zoomdata.properties``and query-engine.properties` files to point at a local PostgreSQL data store for that instance. Ensure that the JDBC settings point to the local PostgreSQL and that the user name and password used to access the local PostgreSQL data store are correct in these files. After changing the settings, restart all the Self-Service Analytics microservices for the instance. See [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

   If the instance you are removing will not be used at all, you can skip this step.

3. Edit the `consul.json` file on all the remaining Self-Service Analytics instances in your high availability environment.

   ```bash theme={null}
   vi /etc/zoomdata/consul.json
   ```

4. Reduce the value specified for the `bootstrap_expect` setting by one. This value is the total number of Self-Service Analytics nodes (instances) in your Self-Service Analytics cluster and must be the same value on every instance in the cluster.

5. Restart the `zoomdata-consul` microservice on every Self-Service Analytics instance in the cluster to ensure they all pic up the node count change.

<h2 id="add-a-new-node-to-existing-self-service-analytics-multi-node">
  Add a New Node to Existing Self-Service Analytics Multi-Node Deployments
</h2>

### Environment Prerequisites

* You must have previously configured your Self-Service Analytics multi-node deployment. `zoomdata-consul` and `postgresql`, configured as clusters external to the nodes, must be configured to accept incoming connections.

  * See [https://www.consul.io/commands/join](https://www.consul.io/commands/join) (`zoomdata-consul join <ip-address>`).
  * See [https://www.postgresql.org/docs/12/high-availability.html](https://www.postgresql.org/docs/12/high-availability.html).

* You must have Linux machines where additional Self-Service Analytics components will be installed.

### Node Installation and Configuration

Each process described here must be performed on each additional node of your Self-Service Analytics multi-node deployment.

<h4 id="install-a-java-21-distribution-26-3-and-later">
  Install A Java 21 Distribution (26.3 and later)
</h4>

Supported options include:

* Oracle: [download here (https://www.oracle.com/java/technologies/downloads/#java21)](https://www.oracle.com/java/technologies/downloads/#java21)
* OpenJDK: [download here (https://openjdk.org/projects/jdk/21/)](https://openjdk.org/projects/jdk/21/)
* AWS Corretto: [download here (https://docs.aws.amazon.com/corretto/latest/corretto-21-ug/downloads-list.html)](https://docs.aws.amazon.com/corretto/latest/corretto-21-ug/downloads-list.html)

#### Add an OS Package Repository

you will need to include an OS package repository of your version of Self-Service Analytics.

**CentOS/RHEL**`/etc/yum.repos.d/zoomdata.repo`

<Note>
  `<COMPOSER-VERSION` must be replaced by the same trunk version (such as 25.4 or 26.3) as your other Self-Service Analytics cluster nodes are equipped with. `RHEL-RELEASE` must be replaced by the supported version of CentOS/RHEL.
</Note>

```properties theme={null}
[zoomdata-stable]
baseurl=https://composer-repo.logianalytics.com/<COMPOSER-VERSION>/yum/redhat/<RHEL-RELEASE>/x86_64/stable
	gpgcheck=1
	gpgkey=https://composer-repo.logianalytics.com/ZOOMDATA-GPG-KEY.pub
	name=Zoomdata stable RPMs
	enabled=1

[zoomdata-tools-stable]
baseurl=https://composer-repo.logianalytics.com/tools/yum/redhat/<RHEL-RELEASE>/x86_64/stable
	gpgcheck=1
	gpgkey=https://composer-repo.logianalytics.com/ZOOMDATA-GPG-KEY.pub
	name=Zoomdata tools stable RPMs
	enabled=1
```

**Ubuntu**`/etc/apt/sources.list.d/zoomdata.list`

<Note>
  `<COMPOSER-VERSION` must be replaced by the same trunk version (such as 26.3) as your other Self-Service Analytics cluster nodes are equipped with. `UBUNTU-CODENAME` must be replaced by one of the supported versions of Ubuntu.
</Note>

<Warning>
  Call `apt update` after adding the additional repository list.
</Warning>

```
deb https://composer-repo.logianalytics.com/<COMPOSER-VERSION>/apt/ubuntu <UBUNTU-CODENAME> stable
deb https://composer-repo.logianalytics.com/tools/apt/ubuntu <UBUNTU-CODENAME> stable
```

<h4 id="install-the-zoomdata-consul-package">
  Install the `zoomdata-consul` Package
</h4>

This allows the cluster node to communicate in Service Discovery with other cluster nodes.

**CentOS/RHEL**

```bash theme={null}
yum install -y zoomdata-consul
```

**Ubuntu**

```bash theme={null}
apt install -y zoomdata-consul
```

#### Configure the Zoomdata Consul Package

Configure the Zoomdata Consul package to be a part of the existing cluster.

1. Stop the `zoomdata-consul` service if it is running.
2. Edit the `/etc/zoomdata/consul.json` file and add:
3. Start the `zoomdata-consul` service. Check if it joined the cluster: `/opt/zoomdata/bin/zoomdata-consul members`

<h4 id="install-self-service-analytics-components">
  Install Self-Service Analytics Components
</h4>

Install the subset of Self-Service Analytics components required by the role of each node you're adding.

<Note>
  COMPOSER-WEB (`zoomdata`) and Self-Service Analytics Query Engine (`zoomdata-query-engine`) require extra configuration to use [the shared metadata storage you configured](#configure-the-metadata-store-for-a-distributed-environment).
</Note>

For example, to install an additional Self-Service Analytics Query Engine and MSSQL connector:

* RHEL/CentOS
* Ubuntu

### Validation

1. Ensure `zoomdata-consul` service, and other zoomdata services are running and not in a failed state.

   ```bash theme={null}
   systemctl status zoomdata\*
   ```

2. Check that the Consul cluster formed successfully. It should show all nodes, including the node or nodes you just added.

   ```
   /opt/zoomdata/bin/zoomdata-consul members
   ```

3. Check the logs to troubleshoot any issues you may have.

   ```
   /opt/zoomdata/logs
   ```

<h2 id="migrate-properties-to-the-configuration-server">
  Migrate Properties to the Configuration Server
</h2>

If you have the configuration microservice configured and running in a high availability environment, you can maintain properties for microservices of a given type in a single location in the Service Monitor. For example, if you have two query engine microservices running in your high availability environment, you can change the properties for both microservices in a single location, ensuring that the query engine microservices operate in the same manner across the product nodes. See [Maintain Application Properties](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/service-monitor-overview#maintain-application-properties) and [Configure and Start the Configuration Microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/service-monitor-overview#configure-and-start-the-configuration-microservice) for information about the configuration microservice.

A utility is provided that can be used to migrate the microservice properties from your standalone Self-Service Analytics server to the Self-Service Analytics configuration data in the high availability PostgreSQL data store, where the configuration microservice can maintain them. The utility is located in the zoomdata tarball at `…/scripts/zoomdata/config-server-upload.jar`.

Run this utility using the following syntax:

```bash theme={null}
java -jar config-server-upload.jar <service> <properties-file> <config-service-url>
```

where `<service>` is the microservice name, `<properties-file>` is the fully qualified file name of the properties file you want to migrate, and `<config-service-url>` is the URL of the configuration microservice (usually `http://localhost:8888/api/environment`).

The following example migrates the properties from `/etc/zoomdata/zoomdata.properties` for the Self-Service Analytics microservice to the configuration data in the high availability PostgreSQL data store at the URL `http://localhost:8888/api/environment`:

```bash theme={null}
java -jar /opt/zoomdata/scripts/zoomdata/config-server-upload.jar zoomdata /etc/zoomdata/zoomdata.properties http://localhost:8888/api/environment
```

<Note>
  In high availability environments, you will need to run this utility for every type of microservice in the environment to ensure that you can maintain the properties for all microservices in the Service Monitor.
</Note>

<h2 id="configure-a-high-load-environment">
  Configure a High Load Environment
</h2>

A high load environment should be able to handle hundreds of concurrent users. One of the simplest solutions is to dedicate powerful machines to our microservices, but it’s cost-inefficient and hardly scalable. Self-Service Analytics has a microservice architecture and supports client-side load balancing for all microservices except COMPOSER-WEB. It enables you to deploy several instances of the same microservice on smaller machines and get a performance gain. You are also able to scale each microservice independently according to the type of load your system receives.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/highloadenvironment.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=bf55bee1c49e88ffca6b35f50d57e395" alt="Flow of a high load environment." width="919" height="616" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/highloadenvironment.png" />

<Warning>
  To configure Self-Service Analytics in a distributed environment, you need a multi-node license before you start setting up your distributed environment. Contact Technical Support for assistance.
</Warning>

<Warning>
  Self-Service Analytics is designed to handle high loads and with an ability to scale. Bottlenecks may not be caused by microservices, but instead in the metastore (PostgreSQL) or other data stores from which you are retrieving data for visualizations.
</Warning>

### Install PostgreSQL

When setting up your distributed environment, you need to determine if a metadata store is already installed in your environment. If you have already installed Self-Service Analytics and are now setting up a distributed environment, your metadata store may be installed with your existing Self-Service Analytics instance or instances.

If this is the first time you're installing Self-Service Analytics, and you want to set up a distributed environment, you must set up a new metadata store.

1. [Set Up the PostgreSQL Metadata Store](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-metadata-store#set-up-the-postgresql-metadata-store)
2. [Change Metadata Store Authentication to MD5](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-metadata-store#change-metadata-store-authentication-to-md5)
3. [Create the Metadata Store User & Stores](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-metadata-store#create-the-metadata-store-user-stores)
4. [Configure the Metadata Store for SSL](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-metadata-store#configure-the-metadata-store-for-ssl)
5. [Configure the Metadata Store for a Distributed Environment](#configure-the-metadata-store-for-a-distributed-environment)

<h4 id="configure-the-metadata-store-for-a-distributed-environment">
  Configure the Metadata Store for a Distributed Environment
</h4>

**Configure the Metadata Store for a Distributed Environment**

All Self-Service Analytics installations require a Postgres metadata store. If you install Self-Service Analytics on a single server using the supplied bootstrap installation script, this metadata store is installed for you. If you install Self-Service Analytics manually, you must also manually set up the metadata store.

The metadata store should be centrally installed, accessible by all Self-Service Analytics nodes. In a high availability environment, it can be clustered.

When setting up a distributed environment, you need to determine whether the metadata store is installed. If you have already installed Self-Service Analytics and are now trying to set up a distributed environment, there is a good chance that the metadata store was installed with your existing Self-Service Analytics instance or instances.

If this is the first time you have installed Self-Service Analytics, and you want to set up a distributed environment, a new metadata store is required.

* If the metadata store has already been installed, identify its host name and port. Then follow the steps for upgrading a distributed environment. See [Upgrade a Self-Service Analytics Distributed Environment](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/upgrading-server#upgrade-a-self-service-analytics-distributed-environment).

* If the metadata store has not already been installed, manually install it now. Complete the following sub-steps. Then identify its host name and port.

  1. Set up the Metadata Store - Necessary for all installations.

     The instructions to set up PostgreSQL as Self-Service Analytics's metadata store differ depending on the Linux operating system used by the target server. Select a topic below:

     * [PostgreSQL Setup for CentOS Environments](#configure-a-high-load-environment)
     * [PostgreSQL Setup for Ubuntu Environments](#configure-a-high-load-environment)

     ### PostgreSQL Setup for CentOS Environments

     <Note>
       New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment, you can retain your existing PostgreSQL version.
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

     ### PostgreSQL Setup for Ubuntu Environments

     <Note>
       New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment, you can retain your existing PostgreSQL version.
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

  2. **Change Metadata Store Authentication to MD5** -- Not necessary when installing a high availability environment in the cloud.

     If you installed Self-Service Analytics's metadata store on a server running CentOS or RedHat, complete the configuration steps below. If the server is running Ubuntu, ignore these instructions.

     <Note>
       New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment, you can retain your existing PostgreSQL version.
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

  3. **Configure the Metadata Store for SSL** - Not necessary if installing a high availability environment in the cloud.

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

  4. **Configure the Metadata Store for a Distributed Environment** - Not necessary if installing a high availability environment in the cloud.

     The PostgreSQL data store must be configured so it is available to all Self-Service Analytics instances in a distributed environment. For more information about PostgreSQL high availability clustering, see PostgreSQL documentation on high availability environments.

     <Note>
       New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment, you can retain your existing PostgreSQL version.
     </Note>

     **Configure the PostgreSQL data store so it is available to all instances**

     1. Edit the `postgresql.conf` file using the appropriate version and paths:

        ```bash theme={null}
        vi /var/lib/pgsql/12/data/postgresql.conf
        ```

     2. Set the following property in `postgresql.conf` and save the file.

        ```properties theme={null}
        listen_address='*'
        ```

     3. Edit the `pg_hba.conf file`:

        ```bash theme={null}
        vi /var/lib/pgsql/12/data/pg_hba.conf
        ```

     4. Add the following to the `pg_hba.conf file`:

        ```
        # TYPE DATABASE USER ADDRESS METHOD # IPv4 local connections host all all 0.0.0.0 /0 md5
        ```

     5. Save the `pg_hba.conf` file.

     6. Restart the PostgreSQL service:

        ```bash theme={null}
        sudo service postgresql-12 restart
        ```

  5. **Create user and Database** - Not necessary if installing a high availability environment in the cloud.

     The PostgreSQL data store must be configured so it is available to all instances in a distributed environment. For more information about PostgreSQL high availability clustering, see [https://www.postgresql.org/docs/12/high-availability.html](https://www.postgresql.org/docs/12/high-availability.html).

     **Create users and databases in the PostgreSQL data store so they are available to all Self-Service Analytics** **instances**

     ```sql theme={null}
     CREATE USER zoomdata WITH PASSWORD 'StrongZoomdataPassword'; CREATE DATABASE "zoomdata" WITH OWNER zoomdata; CREATE DATABASE "zoomdata-upload" WITH OWNER zoomdata; CREATE DATABASE "zoomdata-keyset" WITH OWNER zoomdata; CREATE DATABASE "zoomdata-auth" WITH OWNER zoomdata; CREATE DATABASE "zoomdata-qe" WITH OWNER zoomdata; CREATE DATABASE "zoomdata-user-auditing" WITH OWNER zoomdata;
     ```

### Install Consul Cluster

Self-Service Analytics requires consul 1.2.2 to discover microservices. We recommend using consul reference deployment with 3 dedicated consul servers, and consul agents on each node that contains a Self-Service Analytics microservice. [See the deployment guidelines](https://learn.hashicorp.com/tutorials/consul/deployment-guide?in=consul/production-deploy) for more information on installing consul server nodes.

### Install Microservices

Self-Service Analytics consists of several microservices. In a distributed environment, we recommend installing each microservice on a separate machine with a consul agent. The consul agent should be connected to the consul cluster you installed in a previous step. [See the deployment guidelines](https://learn.hashicorp.com/tutorials/consul/deployment-guide?in=consul/production-deploy) for more information on installing consul server nodes.

We recommend including at least two instances of each microservice except COMPOSER-WEB. Enable intra-service communication by making any necessary networking (ports) and firewall changes. To install a microservice on a machine, see [Add a New Node to Existing Self-Service Analytics Multi-Node Deployments](#add-a-new-node-to-existing-self-service-analytics-multi-node).

| Microservice | Required |
| - | - |
| COMPOSER-WEB | Yes. |
| QUERY ENGINE | Yes. |
| CONNECTOR | Required only for target data sources. |
| SCREENSHOT SERVICE | Required only if you use dashboard reporting. |
| DATA WRITER | Required only if you use upload sources. |
| CONFIG SERVER | No, this is a platform microservice. |
| SERVICE MONITOR | No, this is a platform microservice. |

### Next Steps

* [Scaling Self-Service Analytics Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#scaling-self-service-analytics-microservices)
* [Install and Configure the Configuration Microservice on Each Node](#install-and-configure-the-configuration-microservice-on-each)
* [Install and Configure the Service Monitor (Optional)](#install-and-configure-the-service-monitor-optional)

<h3 id="install-and-configure-the-configuration-microservice-on-each">
  Install and Configure the Configuration Microservice on Each Node
</h3>

**Install and Configure the Configuration Microservice On Each Node**

Complete the following steps.

1. **Set Up the Configuration Microservice Metadata Store or Repository**

   Before you can install and start Self-Service Analytics's configuration microservice, you must set up a PostgreSQL metastore or a GitHub repository to store Self-Service Analytics property metadata. A separate PostgreSQL database or a separate GitHub repository must be configured.

   #### PostgreSQL Database Setup Notes

   **If you elect to persist property metadata to a PostgreSQL metastore:**

   1. Configure a separate database and make it accessible to the connection user account:

      ```sql theme={null}
      CREATE DATABASE <composer-config> WITH OWNER <db_username>;
      ```

      where `<composer-config>` is the name of the PostgreSQL database and `<db_username>` is the connection user account name.

   2. Add the following properties to the Self-Service Analytics `config-server.properties` file, located in the `/etc/zoomdata` directory:

      ```
      # metadata storage settings spring.datasource.url=jdbc:postgresql://localhost:5432/<composer-config> spring.datasource.username=<db_username> spring.datasource.password=<db_password>
      ```

      Substitute the connection user account name and password you set up in Step 1 for `<db_username>` and `<db_password>`. Substitute the name of the PostgreSQL database for `<composer-config>`.

   3. Save the properties file. You will restart the configuration microservice when you configure it. See [Configure and Start the Configuration Microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/service-monitor-overview#configure-and-start-the-configuration-microservice).

   #### GitHub Repository Setup Notes

   **If you elect to persist property metadata to a GitHub repository:**

   1. Add the following properties to the Self-Service Analytics `config-server.properties` file, located in the `/etc/zoomdata` directory:

      ```
      # metadata storage settings spring.cloud.config.server.git.uri=<repo_uri> spring.cloud.config.server.git.skipSslValidation=true spring.cloud.config.server.git.username=<repo_username> spring.cloud.config.server.git.password=<repo_password>
      ```

      Substitute the repository user account name and password for `<repo_username>` and `<repo_password>`. Substitute the URI of the repository for `<repo_uri>` (for example, `https://example.com/my/repo`).

      Additional and advanced configuration information can be found in [Spring.io's documentation](https://cloud.spring.io/spring-cloud-config/multi/multi__spring_cloud_config_server.html#_git_backend).

   2. Save the properties file. You will restart the configuration microservice when you configure it. See [Configure and Start the Configuration Microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/service-monitor-overview#configure-and-start-the-configuration-microservice).

2. **Install, Configure, and Start the Configuration Microservice**

   **Install, configure, and start the Self-Service Analytics** **configuration microservice**

   1. Verify that you have set up a PostgreSQL metastore or a GitHub repository to store the property metadata. See [Set Up the Configuration Microservice Metadata Store or Repository](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/monitor/service-monitor-overview#set-up-the-configuration-microservice-metadata-store-or).

   2. Open the SSH client associated with your instance.

   3. Configure all installed and enabled microservices to use the configuration microservice. Run the following script:

      ```
      for i in $(systemctl list-unit-files | grep zoomdata | grep enabled | awk '{print $1}'|sed -e 's/\.service/.properties/g' -e 's/zoomdata\-//g');
      do
      echo "config-server.enabled=true">>/etc/zoomdata/$i;
      done
      ```

   4. Each microservice supports two configuration properties related to the configuration microservice:

      * `config-server.enabled`: Enables or disables integration with the configuration microservice. Valid values are `true` (enable integration) and `false` (disable integration). The default is `true`.
      * `config-client.retry.max-attempts`: Sets the maximum number of attempts that should be made to connect to the configuration microservice. The default is 20. The Self-Service Analytics microservice will fail if the number of attempts to connect to the configuration microservice exceeds this value. This property is useful in situations where the configuration microservice starts with a delay. If your microservice fails while waiting for the configuration microservice and you want to give it more time, increase this value.

      Update these properties, as appropriate, for each microservice.

   5. Install, enable and start the configuration microservice. Enter the following commands:

      ```bash theme={null}
      sudo yum install zoomdata-config-server \
      && systemctl enable zoomdata-config-server \
      && systemctl start zoomdata-config-server
      ```

      <Note>
        After starting the configuration microservice with a valid database configuration, the microservice should connect to the database and create a properties table.
      </Note>

   6. Restart all the other microservices. Enter the following command:

      ```bash theme={null}
      sudo systemctl restart $(systemctl list-unit-files | grep zoomdata | grep enabled | awk '{print $1}')
      ```

      See also [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

<h3 id="install-and-configure-the-service-monitor-optional">
  Install and Configure the Service Monitor (Optional)
</h3>

**Install and Configure the Service Monitor (Optional)**

The Self-Service Analytics Service Monitor microservice is not installed as part of a default Self-Service Analytics installation. The microservice name is `zoomdata-admin-server`.

<Note>
  If you are installing Self-Service Analytics in a Windows environment, you can install the Service Monitor as part of running the initial bootstrap script. See [Install Self-Service Analytics - Windows](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-windows) and [Windows Bootstrap Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-windows#windows-bootstrap-reference).
</Note>

**Install, configure, and start the Service Monitor**

1. Open your SSH client.

2. Use the following command to install the Self-Service Analytics Service Monitor in a CentOS environment:

   ```bash theme={null}
   sudo yum install zoomdata-admin-server -y
   ```

   Use the following command to install the Self-Service Analytics Service Monitor in an Ubuntu environment:

   ```bash theme={null}
   sudo apt-get install zoomdata-admin-server
   ```

3. After the Service Monitor is installed, you must specify a user name and password in its properties file. The properties file is called `admin-server.properties` and can be found in the `/etc/zoomdata/` directory (Linux) or the `<install-path>/conf-modify/` directory (Windows). If the properties file is not there, create it. The properties that must be defined are:

   * `monitor.user.name=<username>`
   * `monitor.user.password=<password>`

   Edit the properties file with a text editor and substitute a Service Monitor user name for `<username>` and its associated password for `<password>`. The user name and password can be any user name and password you want.

   When you have finished, save the file.

4. Add the following properties to the `zoomdata.properties` file, located in the `/etc/zoomdata` directory (Linux) or the `<install-path>/conf-modify/` (Windows). These properties ensure that the Service Monitor has access to the Self-Service Analytics server actuator endpoints.

   * `actuator.user.name=<composer-admin-username>`
   * `actuator.user.password=<composer-pswd>`
   * `actuator.logging.external-file=<log-file-path>`

   Edit the properties file and substitute the valid user name and password of a Self-Service Analytics administrator for `<composer-admin-username>` and `<composer-pswd>`. If the default Self-Service Analytics log file path is not used for your installation, substitute your custom log file path for `<log-file-path>`. The default log file path is `/opt/zoomdata/logs/zoomdata.log` for Linux and `<install-path>/logs/zoomdata.log` for Windows.

   <Note>
     Setting these properties exposes valid Self-Service Analytics credentials as plain text in both the properties file and as tags in the Self-Service Analytics Consul. Anyone in your network with the ability to communicate directly with the Consul API or view the Consul UI will be able to see these values.
   </Note>

   When finished, save the file.

5. Start the microservice. For example, use the following command to start the Self-Service Analytics Service Monitor using `systemd` in a CentOS or Ubuntu environment:

   ```bash theme={null}
   sudo systemctl start zoomdata-admin-server
   ```

   See also [Start Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#start-microservices).

<h2 id="configure-the-self-service-analytics-server-behind-a-load">
  Configure the Self-Service Analytics Server Behind a Load Balancer
</h2>

Load balancing helps you to scale Self-Service Analytics to hundreds of users. You can use load balancing both on-premises and with cloud deployments, meaning you can use load balancing for various environments. When the server is load balanced within your network environment, it includes native SSL support and can proxy WebSocket traffic.

The following diagram depicts a classic load balancing setup.

<img src="https://mintcdn.com/insightsoftware/2cXq_sDOxrDVXUcv/simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/load-balancing.png?fit=max&auto=format&n=2cXq_sDOxrDVXUcv&q=85&s=62af82197d362b2399d215de48ef6f92" alt="" width="672" height="267" data-path="simba-embedded-analytics/docs/self-service-analytics/26.3/images/config/load-balancing.png" />

Self-Service Analytics has tested active-active load balancing configuration, which is the particular setup used in the steps below. In addition, the instructions provided below take into account that Self-Service Analytics, when it runs standalone, uses its own dedicated PostgreSQL server as the metadata store (in other words, PostgreSQL was installed as part of the Self-Service Analytics installation process). If you are running in a high availability environment, you will need to use a high availability (clustered) PostgreSQL data store. See [Configure a High Availability Environment](#configure-a-high-availability-environment).

<Warning>
  Configuring Self-Service Analytics in a distributed environment requires a multi-node license. Be sure you have obtained this before you start. Contact your insightsoftware Technical Support representative for assistance.
</Warning>

Complete the following steps to configure load balancing in your environment.

<AccordionGroup>
  <Accordion title="Step 1: Identify or Install the Postgres Metadata Store">
    All Self-Service Analytics installations require a Postgres metadata store. If you install Self-Service Analytics on a single server using the supplied bootstrap installation script, this metadata store is installed for you. If you install Self-Service Analytics manually, you must also manually set up the metadata store.

    The metadata store should be centrally installed, accessible by all Self-Service Analytics nodes. In a high availability environment, it can be clustered.

    When setting up a distributed environment, you need to determine whether the metadata store is installed. If you have already installed Self-Service Analytics and are now trying to set up a distributed environment, there is a good chance that the metadata store was installed with your existing Self-Service Analytics instance or instances.

    If this is the first time you have installed Self-Service Analytics, and you want to set up a distributed environment, a new metadata store is required.

    * If the metadata store has already been installed, identify its host name and port. Then follow the steps for upgrading a distributed environment. See [Upgrade a Self-Service Analytics Distributed Environment](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/upgrading-server#upgrade-a-self-service-analytics-distributed-environment).

    * If the metadata store has not already been installed, manually install it now. Complete the following sub-steps. Then identify its host name and port.

      1.     <Accordion title="Create the Metadata Store User & Stores - Necessary for all installations.">
               The instructions to set up PostgreSQL as Self-Service Analytics's metadata store differ depending on the Linux operating system used by the target server. Select a topic below:

               * [PostgreSQL Setup for CentOS Environments](#configure-the-self-service-analytics-server-behind-a-load)
               * [PostgreSQL Setup for Ubuntu Environments](#configure-the-self-service-analytics-server-behind-a-load)

               ### PostgreSQL Setup for CentOS Environments

               <Note>
                 New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment from an earlier version of Composer, you can retain your existing PostgreSQL version.
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

               ### PostgreSQL Setup for Ubuntu Environments

               <Note>
                 New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment from an earlier version of Composer, you can retain your existing PostgreSQL version.
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
             </Accordion>
      2.     <Accordion title="Change Metadata Store Authentication to MD5 -- Not necessary when installing a high availability environment in the cloud.">
               If you installed Self-Service Analytics's metadata store on a server running CentOS or RedHat, complete the configuration steps below. If the server is running Ubuntu, ignore these instructions.

               <Note>
                 New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment from an earlier version of Composer, you can retain your existing PostgreSQL version.
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
             </Accordion>
      3.     <Accordion title="Configure the Metadata Store for SSL - Not necessary if installing a high availability environment in the cloud.">
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
             </Accordion>
      4.     <Accordion title="Configure the Metadata Store for a Distributed Environment">
               The PostgreSQL data store must be configured so it is available to all Self-Service Analytics instances in a distributed environment. For more information about PostgreSQL high availability clustering, see PostgreSQL documentation on high availability environments.

               <Note>
                 New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment from an earlier version of Composer, you can retain your existing PostgreSQL version.
               </Note>

               **Configure the PostgreSQL data store so it is available to all instances**

               1. Edit the `postgresql.conf` file using the appropriate version and paths:

                  ```bash theme={null}
                  vi /var/lib/pgsql/12/data/postgresql.conf
                  ```

               2. Set the following property in `postgresql.conf` and save the file.

                  ```properties theme={null}
                  listen_address='*'
                  ```

               3. Edit the `pg_hba.conf file`:

                  ```bash theme={null}
                  vi /var/lib/pgsql/12/data/pg_hba.conf
                  ```

               4. Add the following to the `pg_hba.conf file`:

                  ```
                  # TYPE DATABASE USER ADDRESS METHOD # IPv4 local connections host all all 0.0.0.0 /0 md5
                  ```

               5. Save the `pg_hba.conf` file.

               6. Restart the PostgreSQL service:

                  ```bash theme={null}
                  sudo service postgresql-12 restart
                  ```
             </Accordion>
  </Accordion>

  <Accordion title="Step 2. Install Self-Service Analytics On Your Distributed Servers">
    Intra-service communication must be enabled by making any necessary networking (ports) and firewall changes.

    **To deploy multiple nodes (or instances) in a distributed environment, complete the following steps for each instance**

    1. For each instance, run the following commands to set up the environment variables for the installation:

       ```bash theme={null}
       export ZOOMDATA_POSTGRES_HOST=<postgres-host>
       export ZOOMDATA_POSTGRES_PORT=<postgres-port>
       export ZOOMDATA_POSTGRES_USER=<postgres-db-username>
       export ZOOMDATA_POSTGRES_PASS=<postgres-db-password>
       ```

       where:

       * `<postgres-host>` and `<postgres-port>` are the host name and port number of the Self-Service Analytics PostgreSQL metadata store
       * `<postgres-db-username>` and `<postgres-db-password>` are the user name and password required to access the Self-Service Analytics PostgreSQL metadata store.

    2. In each instance, run the following command to set up the environment variables for specific enterprise data connector (EDC) packages:

       ```bash theme={null}
       export ZOOMDATA_EDC_PACKAGES='<edc>,<edc>[,<edc>]...'
       ```

       where `<edc>` is the name of the data connector you would like to install. You must install the PostgreSQL connector because it connects to the metadata store. Data connector names are the same as their connector microservice names without the `zoomdata-edc-` prefix. See [Data Connector Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference).

    3. Run the bootstrap installation script after exporting the environment variables in the previous steps.

       ```bash theme={null}
       curl -O https://composer-repo.logianalytics.com/<v.r>/bootstrap-zoomdata.run
       sudo -E /bin/sh bootstrap-zoomdata.run
       ```

       where `<v.r>` is the Self-Service Analytics version and release.

    4. After the installation, ensure that the following property files are correctly set up on each node. Add or update the properties as necessary. In each, the IP address, port, user name, and password of the PostgreSQL metadata store should be specified.

       **In the** `zoomdata.properties` **file:**

       ```properties theme={null}
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

       **In the** `query-engine.properties` **file:**

       ```properties theme={null}
       spring.qe.datasource.jdbcUrl=jdbc:postgresql://<IP-address>:<port>/zoomdata-qe
       spring.qe.datasource.username=<db-username>
       spring.qe.datasource.password=<db-password>
       ```

    5. Ensure that port 8080 is open on all your back-end servers to support load balancing. If not, run the following command:

       ```bash theme={null}
       sudo iptables -I INPUT 1 -p tcp --dport 8080 -j ACCEPT
       sudo service iptables save
       ```

    6. Repeat these steps for every Self-Service Analytics instance (node) in your Self-Service Analytics cluster.
  </Accordion>

  <Accordion title="Step 3. Set Up a Load Balancer">
    Set up one or more load balancers in your environment. For a simple load balanced configuration, only one is needed. In a high availability configuration, however, more than one load balancer is recommended; if only a single load balancer is deployed in a high availability environment, you will not be able to access any of the Self-Service Analytics nodes behind it if the load balancer should fail.

    The following steps provide an example of setting up HAProxy as a load balancer. Regardless of what kind of load balancer you use, ensure that port 443 is open on it.

    **Set up an HAProxy load balancer**

    1. On your machine, run the following command to install HAProxy:

       ```bash theme={null}
       sudo yum install haproxy
       ```

    2. Navigate to the HAProxy folder.

       ```bash theme={null}
       cd /etc/haproxy
       ```

    3. Create a certificate or copy an existing certificate to the `/etc/haproxy` folder. If you need to create a certificate, run the following commands:

       ```bash theme={null}
       sudo openssl genrsa -out ca.key 1024
       sudo openssl req -new -key ca.key -out ca.csr
       sudo openssl x509 -req -days 365 -in ca.csr -signkey ca.key -out ca.crt
       sudo vi cert.pem #Create and save an empty file
       sudo chmod a+w cert.pem
       sudo cat ca.key ca.crt > cert.pem
       ```

    4. In the same folder, replace the contents of the `haproxy.cfg` file with the contents of the [Self-Service Analytics haproxy configuration file](/simba-embedded-analytics/docs/self-service-analytics/26.3/images/files/haproxy.txt). In the file, replace the `<node1-ip>` and `<node2-ip>` with the IP addresses of your servers. If you have more than two servers, add additional lines for each server.

    5. Save your changes and exit the file.

    6. Start the HAProxy microservice

       ```bash theme={null}
       sudo service haproxy restart
       ```

    7. Use the following command to configure the HAProxy microservice to start automatically in CentOS environments:

       ```bash theme={null}
       sudo systemctl enable haproxy
       ```

    8. Ensure that port 443 is open on your load balancer. If not, run the following command:

       ```bash theme={null}
       sudo iptables -I INPUT 1 -p tcp --dport 443 -j ACCEPT
       sudo service iptables save
       ```

    For assistance with configuring SAML for use with HAProxy, contact insightsoftware Technical Support.
  </Accordion>

  <Accordion title="Step 4. Copy Specialized Files">
    If you have any specialized files for Self-Service Analytics, such as vocabulary files, manually copy them to each instance of Self-Service Analytics in your distributed environment.
  </Accordion>
</AccordionGroup>
