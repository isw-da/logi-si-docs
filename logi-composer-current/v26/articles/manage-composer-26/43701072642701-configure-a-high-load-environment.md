---
title: "Configure a High Load Environment"
id: 43701072642701
section: "Manage Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072642701-Configure-a-High-Load-Environment
updated_at: 2026-05-29T14:10:41Z
---

# Configure a High Load Environment

# Configure a High Load Environment

A high load environment should be able to handle hundreds of concurrent users. One of the simplest solutions is to dedicate powerful machines to our microservices, but it’s cost-inefficient and hardly scalable. Composer has a microservice architecture and supports client-side load balancing for all microservices except COMPOSER-WEB. It enables you to deploy several instances of the same microservice on smaller machines and get a performance gain. You are also able to scale each microservice independently according to the type of load your system receives.

![Flow of a high load environment.](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242476313869 "High Load Environment diagram.")

**Important:** 
To configure Composer in a distributed environment, you need a multi-node license before you start setting up your distributed environment. Contact Technical Support for assistance.

**Important:** Composer is designed to handle high loads and with an ability to scale. Bottlenecks may not be caused by microservices, but instead in the metastore (PostgreSQL) or other data stores from which you are retrieving data for visualizations.

## Install PostgreSQL

When setting up your distributed environment, you need to determine if a metadata store is already installed in your environment. If you have already installed Composer and are now setting up a distributed environment, your metadata store may be installed with your existing Composer instance or instances.

If this is the first time you're installing Composer, and you want to set up a distributed environment, you must set up a new metadata store.

1. [Set Up the PostgreSQL Metadata Store](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072738701--Set-Up-the-PostgreSQL-Metadata-Store)
2. [Change Metadata Store Authentication to MD5](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105193613-Change-Metadata-Store-Authentication-to-MD5)
3. [Create the Metadata Store User & Stores](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134856333-Create-the-Metadata-Store-User-Stores)
4. [Configure the Metadata Store for SSL](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072750221-Configure-the-Metadata-Store-for-SSL)
5. [Configure the Metadata Store for a Distributed Environment](#Configur)

### Configure the Metadata Store for a Distributed Environment

**Configure the Metadata Store for a Distributed Environment**

All Composer installations require a Postgres metadata store. If you install Composer on a single server using the supplied bootstrap installation script, this metadata store is installed for you. If you install Composer manually, you must also manually set up the metadata store.

The metadata store should be centrally installed, accessible by all Composer nodes. In a high availability environment, it can be clustered.

When setting up a distributed environment, you need to determine whether the metadata store is installed. If you have already installed Composer and are now trying to set up a distributed environment, there is a good chance that the metadata store was installed with your existing Composer instance or instances.

If this is the first time you have installed Composer, and you want to set up a distributed environment, a new metadata store is required.

* If the metadata store has already been installed, identify its host name and port. Then follow the steps for upgrading a distributed environment. See  [Upgrade a Composer Distributed Environment](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701211428493--Upgrade-a-Composer-Distributed-Environment).
* If the metadata store has not already been installed, manually install it now. Complete the following sub-steps. Then identify its host name and port.

  1. Set up the Metadata Store - Necessary for all installations.

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
  2. **Change Metadata Store Authentication to MD5** -- Not necessary when installing a high availability environment in the cloud.

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
  3. **Configure the Metadata Store for SSL** - Not necessary if installing a high availability environment in the cloud.

     If you have specified SSL connections for the metadata store JDBC connections in `zoomdata.properties` file, the root CA certificate that is used for the PostgreSQL database must be added to the `/opt/zoomdata/.postgresql` directory. This directory does not exist by default and will need to be created. Complete the following steps.

     1. Change to the `/opt/zoomdata` directory as a superuser:

        sudo cd /opt/zoomdata
     2. Create a `.postgresql` subdirectory.

        sudo mkdir .postgresql
     3. Copy the root CA certificate for the PostgreSQL database into the new directory:

        sudo cp root.ca /opt/zoomdata/.postgresql/root.ca
  4. **Configure the Metadata Store for a Distributed Environment** - Not necessary if installing a high availability environment in the cloud.

     The PostgreSQL data store must be configured so it is available to all Composer instances in a distributed environment. For more information about PostgreSQL high availability clustering, see PostgreSQL documentation on high availability environments.

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
  5. **Create user and Database** - Not necessary if installing a high availability environment in the cloud.

     The PostgreSQL data store must be configured so it is available to all instances in a distributed environment. For more information about PostgreSQL high availability clustering, see <https://www.postgresql.org/docs/12/high-availability.html>.

     **Create users and databases in the PostgreSQL data store so they are available to all** Composer **instances**

     CREATE USER zoomdata WITH PASSWORD 'StrongZoomdataPassword';
     CREATE DATABASE "zoomdata" WITH OWNER zoomdata;
     CREATE DATABASE "zoomdata-upload" WITH OWNER zoomdata;
     CREATE DATABASE "zoomdata-keyset" WITH OWNER zoomdata;
     CREATE DATABASE "zoomdata-auth" WITH OWNER zoomdata;
     CREATE DATABASE "zoomdata-qe" WITH OWNER zoomdata;
     CREATE DATABASE "zoomdata-user-auditing" WITH OWNER zoomdata;

## Install Consul Cluster

Composer requires consul 1.2.2 to discover microservices. We recommend using consul reference deployment with 3 dedicated consul servers, and consul agents on each node that contains a Composer microservice. [See the deployment guidelines](https://learn.hashicorp.com/tutorials/consul/deployment-guide?in=consul/production-deploy) for more information on installing consul server nodes.

## Install Microservices

Composer consists of several microservices. In a distributed environment, we recommend installing each microservice on a separate machine with a consul agent. The consul agent should be connected to the consul cluster you installed in a previous step. [See the deployment guidelines](https://learn.hashicorp.com/tutorials/consul/deployment-guide?in=consul/production-deploy) for more information on installing consul server nodes.

We recommend including at least two instances of each microservice except COMPOSER-WEB. Enable intra-service communication by making any necessary networking (ports) and firewall changes. To install a microservice on a machine, see [Add a New Node to Existing Composer Multi-Node Deployments](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072458637-Add-a-New-Node-to-Existing-Composer-Multi-Node-Deployments).

| Microservice | Required |
| --- | --- |
| COMPOSER-WEB | Yes. |
| QUERY ENGINE | Yes. |
| CONNECTOR | Required only for target data sources. |
| SCREENSHOT SERVICE | Required only if you use dashboard reporting. |
| DATA WRITER | Required only if you use upload sources. |
| CONFIG SERVER | No, this is a platform microservice. |
| SERVICE MONITOR | No, this is a platform microservice. |

## Next Steps

* [Scaling Composer Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073088525-Scaling-Composer-Microservices)
* [Install and Configure the Configuration Microservice on Each Node](#Install)
* [Install and Configure the Service Monitor (Optional)](#Install2)

### Install and Configure the Configuration Microservice on Each Node

**Install and Configure the Configuration Microservice On Each Node**

Complete the following steps.

1. **Set Up the Configuration Microservice Metadata Store or Repository**

   Before you can install and start Composer's configuration microservice, you must set up a PostgreSQL metastore or a GitHub repository to store Composer property metadata. A separate PostgreSQL database or a separate GitHub repository must be configured.

   ## PostgreSQL Database Setup Notes

   **If you elect to persist property metadata to a PostgreSQL metastore:**

   1. Configure a separate database and make it accessible to the connection user account:

      CREATE DATABASE <composer-config> WITH OWNER <db\_username>;

      where `<composer-config>` is the name of the PostgreSQL database and `<db_username>` is the connection user account name.
   2. Add the following properties to the Composer`config-server.properties` file, located in the `/etc/zoomdata` directory:

      # metadata storage settings
      spring.datasource.url=jdbc:postgresql://localhost:5432/<composer-config>
      spring.datasource.username=<db\_username>
      spring.datasource.password=<db\_password>

      Substitute the connection user account name and password you set up in Step 1 for `<db_username>` and `<db_password>`. Substitute the name of the PostgreSQL database for `<composer-config>`.
   3. Save the properties file. You will restart the configuration microservice when you configure it. See [Configure and Start the Configuration Microservice](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128284045-Configure-and-Start-the-Configuration-Microservice).

   ## GitHub Repository Setup Notes

   **If you elect to persist property metadata to a GitHub repository:**

   1. Add the following properties to the Composer`config-server.properties` file, located in the `/etc/zoomdata` directory:

      # metadata storage settings
      spring.cloud.config.server.git.uri=<repo\_uri>
      spring.cloud.config.server.git.skipSslValidation=true
      spring.cloud.config.server.git.username=<repo\_username>
      spring.cloud.config.server.git.password=<repo\_password>

      Substitute the repository user account name and password for `<repo_username>` and `<repo_password>`. Substitute the URI of the repository for `<repo_uri>` (for example, `https://example.com/my/repo`).

      Additional and advanced configuration information can be found in [Spring.io's documentation](https://cloud.spring.io/spring-cloud-config/multi/multi__spring_cloud_config_server.html#_git_backend).
   2. Save the properties file. You will restart the configuration microservice when you configure it. See [Configure and Start the Configuration Microservice](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701128284045-Configure-and-Start-the-Configuration-Microservice).
2. **Install, Configure, and Start the Configuration Microservice**

   **Install, configure, and start the** Composer **configuration microservice**

   1. Verify that you have set up a PostgreSQL metastore or a GitHub repository to store the property metadata. See [Set Up the Configuration Microservice Metadata Store or Repository](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701175948429-Set-Up-the-Configuration-Microservice-Metadata-Store-or-Repository).
   2. Open the SSH client associated with your instance.
   3. Configure all installed and enabled microservices to use the configuration microservice. Run the following script:

      for i in $(systemctl list-unit-files | grep zoomdata | grep enabled | awk '{print $1}'|sed -e 's/\.service/.properties/g' -e 's/zoomdata\-//g');  
      do  
      echo "config-server.enabled=true">>/etc/zoomdata/$i;  
      done
   4. Each microservice supports two configuration properties related to the configuration microservice:

      * `config-server.enabled`: Enables or disables integration with the configuration microservice. Valid values are `true` (enable integration) and `false` (disable integration). The default is `true`.
      * `config-client.retry.max-attempts`: Sets the maximum number of attempts that should be made to connect to the configuration microservice. The default is 20. The microservice will fail if the number of attempts to connect to the configuration microservice exceeds this value. This property is useful in situations where the configuration microservice starts with a delay. If your microservice fails while waiting for the configuration microservice and you want to give it more time, increase this value.

      Update these properties, as appropriate, for each microservice.
   5. Install, enable and start the configuration microservice. Enter the following commands:

      sudo yum install zoomdata-config-server \  
      && systemctl enable zoomdata-config-server \  
      && systemctl start zoomdata-config-server

      **Note:** 
      After starting the configuration microservice with a valid database configuration, the microservice should connect to the database and create a properties table.
   6. Restart all the other microservices. Enter the following command:

      sudo systemctl restart $(systemctl list-unit-files | grep zoomdata | grep enabled | awk '{print $1}')

      See also  [Restart Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Restart).

### Install and Configure the Service Monitor (Optional)

**Install and Configure the Service Monitor (Optional)**

The Composer Service Monitor microservice is not installed as part of a default Composer installation. The microservice name is `zoomdata-admin-server`.

**Note:** 
If you are installing Composer in a Windows environment, you can install the Service Monitor as part of running the initial bootstrap script. See [Install Composer in a Windows Environment](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072833421-Install-Composer-in-a-Windows-Environment) and [Windows Bootstrap Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120362381-Windows-Bootstrap-Reference).

**Install, configure, and start the Service Monitor**

1. Open your SSH client.
2. Use the following command to install the Composer Service Monitor in a CentOS environment:

   sudo yum install zoomdata-admin-server -y

   Use the following command to install the Composer Service Monitor in an Ubuntu environment:

   sudo apt-get install zoomdata-admin-server
3. After the Service Monitor is installed, you must specify a user name and password in its properties file. The properties file is called `admin-server.properties` and can be found in the `/etc/zoomdata/` directory (Linux) or the `<install-path>/conf-modify/` directory (Windows). If the properties file is not there, create it. The properties that must be defined are:

   * `monitor.user.name=<username>`
   * `monitor.user.password=<password>`

   Edit the properties file with a text editor and substitute a Service Monitor user name for `<username>` and its associated password for `<password>`. The user name and password can be any user name and password you want.

   When you have finished, save the file.
4. Add the following properties to the `zoomdata.properties` file, located in the `/etc/zoomdata` directory (Linux) or the `<install-path>/conf-modify/` (Windows). These properties ensure that the Service Monitor has access to the Composer server actuator endpoints.

   * `actuator.user.name=<composer-admin-username>`
   * `actuator.user.password=<composer-pswd>`
   * `actuator.logging.external-file=<log-file-path>`

   Edit the properties file and substitute the valid user name and password of a Composer administrator for `<Composer-admin-username>` and `<Composer-pswd>`. If the default Composer log file path is not used for your installation, substitute your custom log file path for `<log-file-path>`. The default log file path is `/opt/zoomdata/logs/zoomdata.log` for Linux and `<install-path>/logs/zoomdata.log` for Windows.

   **Note:** 
   Setting these properties exposes valid Composer credentials as plain text in both the properties file and as tags in the Composer Consul. Anyone in your network with the ability to communicate directly with the Consul API or view the Consul UI will be able to see these values.

   When finished, save the file.
5. Start the microservice. For example, use the following command to start the Composer Service Monitor using `systemd` in a CentOS or Ubuntu environment:

   sudo systemctl start zoomdata-admin-server

   See also  [Start Microservices](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701119873037-About-Microservices#Start).
