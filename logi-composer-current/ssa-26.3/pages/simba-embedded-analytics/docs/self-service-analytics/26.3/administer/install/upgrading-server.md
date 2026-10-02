> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Upgrade Self-Service Analytics

You can generally upgrade your environment to the latest major version of Self-Service Analytics from a prior major version.

<Warning>
  If you are upgrading from a version of Self-Service Analytics more than one major version back, work with Technical Support to plan and coordinate an upgrade of your operating system and other portions of you environment, if needed. See [Operating System Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#operating-system-support) and [Prerequisites to Upgrading Self-Service Analytics](#prerequisites-to-upgrading-self-service-analytics).
</Warning>

For information about the difference between a clean installation of Self-Service Analytics and an upgrade to the latest GA release, see [Clean Installation and Upgrade Differences](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#clean-installation-and-upgrade-differences).

## Upgrade and Migration Considerations

* Windows Server 2012R2 is not compatible with both Java17 binaries and the latest releases of Composer (23.2 and later). We recommend you use Windows 2019 or later to run Composer 26.2 and later.
* In general, you can upgrade directly to the latest version of Self-Service Analytics from a prior version.
* If you are upgrading to a newer version of Self-Service Analytics and you also want to change your encryption mode, perform the upgrade first and then complete the steps described in [Encryption](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/changing-encryption-mode).

<Note>
  New installations of Self-Service Analytics PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

<Warning>
  If you are upgrading to a newer version of Self-Service Analytics and have created an attribute named `User.timeZone`, this may be overwritten on upgrade. See [Upgrade Workflow](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#upgrade-workflow) for more information about preparing your environment for the upgrade process.
</Warning>

To upgrade your installation, read the following sections:

* [Prerequisites to Upgrading Self-Service Analytics](#prerequisites-to-upgrading-self-service-analytics)
* [Upgrade Steps for Self-Service Analytics](#upgrade-steps-for-self-service-analytics)

If you are upgrading a distributed environment, see [Upgrade a Self-Service Analytics Distributed Environment](#upgrade-a-self-service-analytics-distributed-environment).

<h2 id="prerequisites-to-upgrading-self-service-analytics">
  Prerequisites to Upgrading Self-Service Analytics
</h2>

Prior to upgrading your software, we **strongly recommend** that you back up your metadata store. See [Back Up the Metadata Store](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-metadata-store#back-up-the-metadata-store).

Failure to have a proper backup could result in losing data during the upgrade process. For more information, see [Back Up the Metadata Store](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-metadata-store#back-up-the-metadata-store).

### JDK Installation Option

An option to install OpenJDK is included in the installation and upgrade scripts provided by Self-Service Analytics. If you skip this option or if you install or upgrade the product manually, make sure that Java 17 is installed. If you do not, Self-Service Analytics will not start after the upgrade.

### Environment Prerequisites

* RHEL 9 (Red Hat)

* CentOS Stream 9

* Ubuntu 22.04

  <Note>
    Older versions of Ubuntu are nearing end of life (EOL) support. Self-Service Analytics will require an operating system upgrade before you upgrade your Composer instance.
  </Note>

* Windows Server version 2019 or higher.

<Danger>
  If your operating system has reached or will soon reach its EOL date, insightsoftware recommends you schedule an appropriate time to upgrade both the Self-Service Analytics and operating system to a later version. For more information, see [Operating System Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#operating-system-support).
</Danger>

<Warning>
  If you are upgrading from a version of Self-Service Analytics more than one major version back, work with Technical Support to plan and coordinate an upgrade of your operating system and other portions of you environment, if needed. See [Operating System Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#operating-system-support) and Upgrade Self-Service Analytics.
</Warning>

See [System Requirements](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#system-requirements) for recommended settings for deploying Self-Service Analytics on-premise.

The target server for the Self-Service Analytics program should meet the following conditions:

* Server is connected to the Internet
* The user installing Self-Service Analytics is able to use the 'sudo' command in the server

<h2 id="upgrade-steps-for-self-service-analytics">
  Upgrade Steps for Self-Service Analytics
</h2>

To begin the upgrade process, you must receive an email containing upgrade instructions from [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support). This email provides the upgrade script that you need to run on the server where the Self-Service Analytics environment resides.

<Note>
  If you have not received upgrade instructions, open a ticket with insightsoftware Support.
</Note>

<Warning>
  If you are upgrading from a version of Self-Service Analytics more than one major version back, work with Technical Support to plan and coordinate an upgrade of your operating system and other portions of you environment, if needed. See [Operating System Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#operating-system-support) and [Prerequisites to Upgrading Self-Service Analytics](#prerequisites-to-upgrading-self-service-analytics).
</Warning>

1. Make sure you have read and performed the recommendations in [Prerequisites to Upgrading Self-Service Analytics](#prerequisites-to-upgrading-self-service-analytics). Be sure to back up your metadata store before you upgrade (see [Back Up the Metadata Store](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-metadata-store#back-up-the-metadata-store)).

2. When you receive the email, enter the upgrade command on your target server to start the automated upgrade process. The following Self-Service Analytics components are downloaded on your target server:

   * The Self-Service Analytics server
   * Connector microservices
   * Query Engine
   * Data Writer microservice

3. After the upgrade script has completed, it will take a few minutes for Self-Service Analytics to complete its update of the metadata store. We recommend that you wait a few minutes before accessing Self-Service Analytics from your web browser.

   If you receive a message indicating that Self-Service Analytics is not yet accessible, it may not have completed its setup yet. Wait a few more minutes before trying again or opening a Support ticket. If you continue to have issues accessing Self-Service Analytics from your browser, open a ticket with insightsoftware [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support). For information about accessing Self-Service Analytics, see [Access and Use Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access).

   <Note>
     If you notice some unusual behavior in the Self-Service Analytics UI after upgrading the Self-Service Analytics software (for example, if a drop-down menu does not open or the application does not react when you select a button), clear the browser cache and try again. If the problem persists, contact Support.
   </Note>

4. The upgrade script provided by [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) assumes that your Postgres metadata store is running locally on the same machine as the Self-Service Analytics code and automatically adds the new databases required to your local installation. If you have upgraded and your metadata store is installed on a different machine (not locally), you will need to manually create the following databases in your Postgres metadata store after the upgrade.

   * `zoomdata`
   * `zoomdata-keyset`
   * `zoomdata-qe`
   * `zoomdata-upload`

   See [Create the Metadata Store User & Stores](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-metadata-store#create-the-metadata-store-user-stores).

5. The firewall setup you used with earlier versions of Self-Service Analytics should have been retained and your Self-Service Analytics IP address should remain unchanged, but see the following for more information:

   * [Configure the Firewall](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#configure-the-firewall)
   * [Identify the Self-Service Analytics IP Address](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#identify-the-self-service-analytics-ip-address)

6. SQL connectors require a JDBC driver to be configured before you can connect to your data source. You can download the driver from the vendor’s site. Be aware that you need to download and configure JDBC drivers for the following Self-Service Analytics connectors:

   * [Microsoft SQL Server](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sql-server)
   * [MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql)
   * [MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql)
   * [Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle)
   * [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift)
   * [Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata)

   If you are using one of these connectors, you need to download and configure a JDBC driver as soon as your Self-Service Analytics server has finished upgrading. For steps, see [Add a JDBC Driver](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-ov#add-a-jdbc-driver).

7. Reimport any CA certificates to Java 17 for Composer you installed prior to the Self-Service Analytics upgrade if needed. (In [Prerequisites to Upgrading Self-Service Analytics](#prerequisites-to-upgrading-self-service-analytics), we recommended that you store them or back them up before the Self-Service Analytics upgrade.)

<h2 id="upgrade-self-service-analytics-with-custom-applications">
  Upgrade Self-Service Analytics with Custom Applications
</h2>

Because Self-Service Analytics is installed software, your organization must decide whether and when to install any particular upgrade. The following considerations will help you understand what is involved in upgrading to any version of Self-Service Analytics.

<h3 id="did-you-white-label-self-service-analytics-with-a-custom-css">
  Did You White Label Self-Service Analytics with a Custom CSS?
</h3>

The CSS in Self-Service Analytics evolves with the client application. Differences in the CSS should be considered before you upgrade. You should examine all existing CSS and modify it accordingly.

<h3 id="does-your-application-use-rest-apis">
  Does Your Application Use REST APIs?
</h3>

Self-Service Analytics’s REST API offerings change regularly. Be sure you review the [Release Notes](/simba-embedded-analytics/docs/self-service-analytics/26.3/release-notes/cmp-api-cchgs-thru-v26) regularly for changes in API endpoints.

<h3 id="does-your-application-use-an-iframe-embedded-dashboard">
  Does Your Application Use an iFrame-Embedded Dashboard?
</h3>

Any dashboard already embedded in a custom application using an iFrame will continue to work with newer versions of Self-Service Analytics. iFrame-embedded dashboards have additional capabilities that are invoked using parameters included with the embedding code.

<h3 id="does-your-application-use-the-javascript-client-library">
  Does Your Application Use the JavaScript Client Library?
</h3>

The JavaScript client library is used to embed visuals or data directly into a web application without using an iFrame. Before upgrading Self-Service Analytics, consider the following topics.

#### Visual Variables

Visual variables are written in standard JSON and left unstringified.

#### JSON Modifications

Some key-value pairs are now wrapped in objects. Review the documentation for updated JSON samples.

#### Deprecated Objects and Methods

Deprecated objects are methods are mentioned in the Release Notes.

<h3 id="have-you-created-a-custom-connector">
  Have You Created a Custom Connector?
</h3>

Custom connectors built to work with previous versions of Composer should continue to function as expected with newer versions.

<h2 id="upgrade-a-self-service-analytics-distributed-environment">
  Upgrade a Self-Service Analytics Distributed Environment
</h2>

To upgrade a Self-Service Analytics distributed environment from a previous version or from an environment that was not distributed, follow these steps.

<Warning>
  We recommend that you set up a test environment to run through the upgrade process prior to upgrading your production environment. This will ensure that any errors are understood and resolved that could potentially impact your customers running the production environment.
</Warning>

<Note>
  If you are upgrading to Self-Service Analytics from an version of Composer earlier than 24.2, you will also need to upgrade the Java JDK and PostgreSQL. When upgrading in this scenario, we recommend that you use the bootstrap installation script provided by insightsoftware to upgrade to avoid manual upgrades to Java JDK and PostgreSQL. If you use the bootstrap script, these upgrades happen automatically.
</Note>

<Note>
  New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

**Upgrade a Self-Service Analytics** **distributed environment, complete the following steps**

<AccordionGroup>
  <Accordion title="Step 1: Disable and Stop All Microservices">
    Before you can start the upgrade, you must disable and stop all microservices. Run the commands described in this section.

    To disable all microservices, enter the following command:

    ```bash theme={null}
    sudo systemctl disable $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')
    ```

    To stop all microservices, enter the following command:

    ```bash theme={null}
    sudo systemctl stop $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')
    ```
  </Accordion>

  <Accordion title="Step 2: Back Up the Postgres Metadata Store">
    Before upgrading your server, insightsoftware recommends that you back up your PostgreSQL metadata store. The metadata includes refresh schedule data, object information for your environment (such as sources, dashboards, and visual definitions), and aggregated result sets. After the metadata store is backed up, perform the upgrade. If problems arise, you can restore the metadata store from your backup copy, if necessary.

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
  </Accordion>

  <Accordion title="Step 3: Create A New Postgres Metadata Store">
    While you can upgrade in place, using an existing metadata store, we recommend that you set up a new instance of the PostgreSQL metadata store for your upgrades. This will preserve the old metadata store in case you need to roll back. If you prefer to upgrade using your existing metadata store, contact your Technical Support representative.

    The metadata store should be centrally installed, accessible by all Self-Service Analytics nodes. In a high availability environment, it can be clustered. Complete the following steps.

    1.     <Accordion title="Complete PostgreSQL Setup Steps">
             The instructions to set up PostgreSQL as Self-Service Analytics's metadata store differ depending on the Linux operating system used by the target server. Select a topic below:

             * [PostgreSQL Setup for CentOS Environments](#postgresql-setup-for-centos-environments)
             * [PostgreSQL Setup for Ubuntu Environments](#postgresql-setup-for-ubuntu-environments)

             ### PostgreSQL Setup for CentOS Environments

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

             ### PostgreSQL Setup for Ubuntu Environments

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
           </Accordion>
    2.     <Accordion title="Change Metadata Store Authentication to MD5">
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
           </Accordion>
    3.     <Accordion title="Create the Metadata Store User">
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
           </Accordion>
    4.     <Accordion title="Configure the Metadata Store for SSL">
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
    5.     <Accordion title="Configure the Metadata Store for a Distributed Environment">
             The PostgreSQL data store must be configured so it is available to all Self-Service Analytics instances in a distributed environment. For more information about PostgreSQL high availability clustering, see PostgreSQL documentation on high availability environments.

             <Note>
               New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
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

  <Accordion title="Step 4: Restore the Metadata From the Metadata Store Backup">
    Prior to restoring the metadata, ensure that the target PostgreSQL data store is clean.

    **Restore the metadata store**

    1. From your terminal, SSH to your Self-Service Analytics server.

    2. Stop all microservices. For appropriate commands based on your OS, see [Stop Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#stop-microservices).

    3. Navigate to your backup directory and enter the following commands:

       ```bash theme={null}
       sudo -u postgres psql zoomdata < zoomdata
       sudo -u postgres psql zoomdata-upload < zoomdata-upload
       sudo -u postgres psql zoomdata-keyset < zoomdata-keyset
       sudo -u postgres psql zoomdata-qe < zoomdata-qe
       ```

    4. Restart all microservices. For appropriate commands based on your OS, see [Restart Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#restart-microservices).

    For more information on backup and restore processes for PostgreSQL, refer to the PostgreSQL [documentation](https://www.postgresql.org/docs/9.5/backup-dump.html).
  </Accordion>

  <Accordion title="Step 5. Upgrade Your Self-Service Analytics Software On All Servers">
    Intra-service communication must be enabled by making any necessary networking (ports) and firewall changes.

    To deploy multiple Self-Service Analytics nodes (or instances) in a distributed environment, complete the following steps for each instance:

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

    4. Disable the automatic PostgreSQL metadata store upgrade by running the following command:

       ```bash theme={null}
       export ZOOMDATA_POSTGRES_DISABLE_UPGRADE=TRUE'
       ```

    5. Run the bootstrap installation script after exporting the environment variables in the previous steps.

       ```bash theme={null}
       curl -O https://composer-repo.logianalytics.com/<v.r>/bootstrap-zoomdata.run
       sudo -E /bin/sh bootstrap-zoomdata.run
       ```

       where `<v.r>` is the Self-Service Analytics version and release.

    6. After the installation, ensure that the following property files are correctly set up on each node. Add or update the properties as necessary. In each, the IP address, port, user name, and password of the PostgreSQL metadata store should be specified.

       In the `zoomdata.properties` file:

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

       In the `query-engine.properties` file:

       ```properties theme={null}
       spring.qe.datasource.jdbcUrl=jdbc:postgresql://<IP-address>:<port>/zoomdata-qe
       spring.qe.datasource.username=<db-username>
       spring.qe.datasource.password=<db-password>
       ```

    7. Ensure that port 8080 is open on all your back-end servers to support load balancing. If not, run the following command:

       ```bash theme={null}
       sudo iptables -I INPUT 1 -p tcp --dport 8080 -j ACCEPT
       sudo service iptables save
       ```

    8. Repeat these steps for every instance (node) in your cluster. For additional information on how many nodes to deploy in a high availability environment, see [Determine How Many Nodes to Deploy](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/distenv-ov#determine-how-many-nodes-to-deploy).
  </Accordion>

  <Accordion title="Step 6. Set Up a Load Balancer (Optional)">
    If you are upgrading from an existing distributed environment to another distributed environment, you can skip this step. Your load balancers were set up when you first installed the product.

    If you are upgrading from a non-distributed environment to a distributed environment, set up one or more load balancers in your environment. For a simple load balanced configuration, only one is needed. In a high availability configuration, however, more than one load balancer is recommended; if only a single load balancer is deployed in a high availability environment, you will not be able to access any of the Self-Service Analytics nodes behind it if the load balancer should fail.

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

  <Accordion title="Step 7. Configure Consul Services for High Availability (Optional)">
    If you are upgrading from an existing high availability environment to another high availability environment, you can skip this step. Consul services were set up when you first installed the product.

    If you are upgrading from a non-distributed environment to a high availability environment, Consul services must be configured.

    You can install individual Consul instances locally for each Self-Service Analytics node and then configure the Consul instances as a cluster for the Self-Service Analytics high availability environment. Before you do, make sure you are familiar with the general clustering techniques used for Consul. See [https://www.consul.io/docs/install/bootstrapping](https://www.consul.io/docs/install/bootstrapping) for more information.

    The primary advantage of using a Consul cluster in a high availability environment is that it requires fewer configuration changes to Self-Service Analytics components. Each component will look for the Consul on the localhost interface at port 127.0.0.1. The only configuration necessary is to the Consul cluster nodes themselves.

    Another advantage is that each node of the high availability cluster will use several discovered instances of the same component to balance the load and become more tolerant of any component failures.

    **Configure a Consul cluster for a Self-Service Analytics high availability environment**

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
  </Accordion>

  <Accordion title="Step 8: Vacuum the Metadata Store">
    insightsoftware highly recommends that you vacuum the Self-Service Analytics PostgreSQL metadata store after every upgrade. Vacuuming the metadata store optimizes it by maximizing database performance and minimizing the disk space it uses. The following simple procedure recollects metadata store statistics and "vacuums" the unused or dead rows in the database.

    <Note>
      This procedure blocks writing to the database. Consequently, work with the database is impossible until the procedure completes.
    </Note>

    This procedure only works for a PostgreSQL database.

    If you have performance problems with your PostgreSQL metadata store, examine the database settings related to automatic vacuuming, automatic analyzing, and the write-ahead log (WAL). See [Optimize Self-Service Analytics's Metadata Store Performance](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-metadata-store#optimize-self-service-analytics-s-metadata-store-performance).

    **Vacuum your PostgreSQL metadata store**

    1. Upgrade your version of Self-Service Analytics (if you have not already done so). This automatically upgrades the PostgreSQL metadata store.

    2. Stop Self-Service Analytics and any process connecting to its PostgreSQL metadata store. See [Stop Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#stop-microservices).

    3. Back up the PostgreSQL metadata store. See [Back Up the Metadata Store](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-metadata-store#back-up-the-metadata-store).

    4. Connect to the PostgreSQL database.

    5. Run the following command in the console for the PostgreSQL database:

       ```
       VACUUM (FULL, ANALYZE);
       ```

       For more information about VACUUM, see [https://www.postgresql.org/docs/12/sql-vacuum.html](https://www.postgresql.org/docs/12/sql-vacuum.html).

    6. After vacuuming completes, start Self-Service Analytics. See [Start Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#start-microservices).
  </Accordion>

  <Accordion title="Step 9: Enable and Start All Self-Service Analytics Microservices">
    After the upgrade, you must enable and start all microservices. Run the commands described in this section.

    To enable all microservices, enter the following command:

    ```bash theme={null}
    sudo systemctl enable $(systemctl list-unit-files | grep zoomdata | grep edc | awk '{print $1}')
    ```

    To start all microservices, enter the following command:

    ```bash theme={null}
    sudo systemctl start $(systemctl list-unit-files | grep zoomdata | grep edc | awk '{print $1}')
    ```
  </Accordion>
</AccordionGroup>

<h2 id="important-notices">
  Important Notices
</h2>

<Warning>
  The current major release of Symphony is v26.1. The capabilities and features you use in your analytics environment have been restructured. For more information, see [Transitioning for Symphony and Composer Users](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/transition-sym).
</Warning>

This software is offered on a quarterly release schedule. The current major release is Simba Self-Service Analytics 26.3.

<Danger>
  If your operating system has reached or will soon reach its EOL date, insightsoftware recommends you schedule an appropriate time to upgrade both the Self-Service Analytics and operating system to a later version. For more information, see [Operating System Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#operating-system-support).
</Danger>

<h4 id="important-notices-upgrade-and-migration-considerations">
  Upgrade and Migration Considerations
</h4>

* Windows Server 2012R2 is not compatible with both Java17 binaries and the latest releases of Composer (23.2 and later). We recommend you use Windows 2019 or later to run Composer 26.2 and later.
* In general, you can upgrade directly to the latest version of Self-Service Analytics from a prior version.
* If you are upgrading to a newer version of Self-Service Analytics and you also want to change your encryption mode, perform the upgrade first and then complete the steps described in [Encryption](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/changing-encryption-mode).

<Note>
  New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

<Warning>
  If you are upgrading to a newer version of Self-Service Analytics and have created an attribute named `User.timeZone`, this may be overwritten on upgrade. See [Upgrade Workflow](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#upgrade-workflow) for more information about preparing your environment for the upgrade process.
</Warning>

For information about Self-Service Analytics's end-of-life policy for third-party software, see [Self-Service Analytics Release Vehicles and Third Party End of Life Policy](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#self-service-analytics-release-vehicles-and-third-party-end-of).
