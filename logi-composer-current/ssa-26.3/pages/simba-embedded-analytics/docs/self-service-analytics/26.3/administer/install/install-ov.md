> ## Documentation Index
> Fetch the complete documentation index at: https://insightsoftware.mintlify.site/llms.txt
> Use this file to discover all available pages before exploring further.

# Install Self-Service Analytics - Linux

<h2 id="linux-clean-installation">
  Linux (Clean Installation)
</h2>

This section provides instructions for performing a clean installation of Self-Service Analytics in your operating environment and is applicable to for both RPM (CentOS, REHL) and Ubuntu environments.

For information about the difference between a clean installation of Self-Service Analytics and an upgrade to the latest GA release, see [Clean Installation and Upgrade Differences](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#clean-installation-and-upgrade-differences).

### Upgrade and Migration Considerations

* Windows Server 2012R2 is not compatible with both Java17 binaries and the latest releases of Self-Service Analytics. We recommend you use Windows 2019 or later.
* In general, you can upgrade directly to the latest version of Self-Service Analytics from a prior version.
* If you are upgrading to a newer version of Self-Service Analytics and you also want to change your encryption mode, perform the upgrade first and then complete the steps described in [Encryption](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/changing-encryption-mode).

<Note>
  New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

<Warning>
  If you are upgrading to a newer version of Self-Service Analytics and have created an attribute named `User.timeZone`, this may be overwritten on upgrade. See [Upgrade Workflow](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/data/data-number-formatting#upgrade-workflow) for more information about preparing your environment for the upgrade process.
</Warning>

In general, the installation process is automated and you only need to run an installation script. The installation script is implemented using Bootstrap. This script accesses a dedicated Self-Service Analytics repository and automatically downloads all the necessary components to install your Self-Service Analytics microservice.

You can install Self-Service Analytics without using the automated installation script. This lets you install and enable each Self-Service Analytics microservices manually in your target server. If you need an alternative option, read [Alternative Installation Options](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#alternative-installation-options).

<Note>
  To install Self-Service Analytics in other environments, see [Install Self-Service Analytics - Windows](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-windows). To install an orchestrated Self-Service Analytics solution, see [Run Self-Service Analytics in Kubernetes](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/kubernetes-ov).
</Note>

After the installation has completed, you need to activate the Self-Service Analytics microservices, download and configure a JDBC driver if you are using specific data sources (see [Post-Installation Options](#post-installation-options) for a list), and open a browser window and enter the specific IP address to access the Self-Service Analytics client.

Review and complete (as appropriate for your installation) the following installation information:

* [Plan Your Installation](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites)
* [Installation Steps](#installation-steps)
* [Alternative Installation Options](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#alternative-installation-options)
* [Post-Installation Options](#post-installation-options)
* [Access and Use Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access)

space

<h2 id="installation-steps">
  Installation Steps
</h2>

To begin the installation process, you must receive the installation instructions from insightsoftware [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support). This email contains the installation script that you will run on the server where the environment will reside. If you have not received installation instructions, open a ticket with insightsoftware [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support).

<Note>
  To install Self-Service Analytics in other environments, see [Install Self-Service Analytics - Windows](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-windows). To install an orchestrated Self-Service Analytics solution, see [Run Self-Service Analytics in Kubernetes](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/kubernetes-ov).
</Note>

### Steps

After you have received installation instructions from [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support), complete the following steps.

* [Step 1: Run the Installation Script](#step-1-run-the-installation-script)
* [Step 2: Configure the Firewall](#step-2-configure-the-firewall)
* [Step 3: Identify the IP Address](#step-3-identify-the-ip-address)
* [Step 4: Access Self-Service Analytics from a Web Browser](#step-4-access-self-service-analytics-from-a-web-browser)

After you have installed Self-Service Analytics, review the post-installation options in [Post-Installation Options](#post-installation-options). For information about accessing after it is installed, see [Access and Use Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access).

<h4 id="step-1-run-the-installation-script">
  Step 1: Run the Installation Script
</h4>

The email or PDF you receive from insightsoftware [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) describes the command used to obtain the installation bootstrap procedure and the command used to run the bootstrap procedure. Run these commands, in order, on the target server for to start the automated installation process.

**Linux environments:** The following components are downloaded to your target server:

* Database for metadata store (using PostgreSQL)
* The Server
* Query Engine
* Data Writer microservice
* Connector microservices

<Warning>
  Self-Service Analytics uses a packaged PostgreSQL database instance to store its metadata. Use the provided instance due to the specific configuration and version combination:
</Warning>

* Self-Service Analytics 26.3 and later: PostgreSQL 16

If you would like to use another PostgreSQL instance, contact [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) for further guidance.

<Warning>
  On Linux platforms, the Self Service Report microservice is not included in the installation bundle. Install it manually after the installation script completes, or self service reports and expanded export options are unavailable.
</Warning>

In an Ubuntu environment, run the following commands:

```bash theme={null}
sudo apt-get update
sudo apt-get install -y zoomdata-report-service
sudo systemctl start zoomdata-report-service
sudo systemctl enable zoomdata-report-service
sudo systemctl status zoomdata-report-service
```

In a RHEL or CentOS environment, run the following commands:

```bash theme={null}
sudo yum makecache
sudo yum install -y zoomdata-report-service
sudo systemctl start zoomdata-report-service
sudo systemctl enable zoomdata-report-service
sudo systemctl status zoomdata-report-service
```

In the `systemctl status` output, confirm that the service is both active and enabled. Enabling the service is what keeps it running after a reboot. To confirm the service is functional, export a dashboard or visual. A running status alone does not confirm that exports work.

See [Self Service Report Microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-report-microservice).

**Windows Environments**

By default, the bootstrap script installs these core components, connectors, and required dependencies:

* Zoomdata web application

* Query Engine

* MSSQL

* Mongo DB

* Elastic 7

* Solr

* Cloudera Search

* Consul

* PostgreSQL

  <Note>
    New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
  </Note>

* Corretto JDK17

* Chocolatey

To install other components, adjust bootstrap switches as needed. See [Windows Bootstrap Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-windows#windows-bootstrap-reference), [Self-Service Analytics Microservice Name Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-analytics-microservice-name-reference) and [Data Connector Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/reference/data-connector-reference).

When the installation script has completed, complete the remaining steps in this section.

<h4 id="step-2-configure-the-firewall">
  Step 2: Configure the Firewall
</h4>

See [Configure the Firewall](#configure-the-firewall).

<h4 id="step-3-identify-the-ip-address">
  Step 3: Identify the IP Address
</h4>

See [Identify the Self-Service Analytics IP Address](#identify-the-self-service-analytics-ip-address).

<h4 id="step-4-access-self-service-analytics-from-a-web-browser">
  Step 4: Access Self-Service Analytics from a Web Browser
</h4>

After the installation script has completed, it will take a few minutes for Self-Service Analytics to complete its setup of the metadata store. Please wait a few minutes before accessing Self-Service Analytics from your web browser. When you are ready to access Self-Service Analytics, read [Access and Use Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access).

<Note>
  We recommend that you log into for the first time using admin credentials. This allows you to review all the account-level features available. As an admin, you can access functions that let you connect your data sources to Self-Service Analytics. You can also create and activate user accounts, including an admin user account that will allow you to access the admin functions. See [Supplied Users and User Groups](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/users/users-manage#supplied-users-and-user-groups).
</Note>

If you receive a message indicating that is not yet accessible, the setup may not yet be complete. Wait a few more minutes before trying again or opening a Support ticket. If you continue to have issues accessing from your browser, open a ticket with Self-Service Analytics [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support).

<h2 id="install-self-service-analytics-manually">
  Install Self-Service Analytics Manually
</h2>

If running the installer script is not a viable option for you, you can install Self-Service Analytics manually.

<Note>
  Manual install of Self-Service Analytics is not currently supported for Windows environments.
</Note>

To install Self-Service Analytics manually, complete the following steps:

* [Step 1. Review the Prerequisites](#step-1-review-the-prerequisites)
* [Step 2. Set Up Self-Service Analytics's Metadata Store](#step-2-set-up-self-service-analytics-s-metadata-store)
* [Step 3. Configure a Dedicated Directory](#step-3-configure-a-dedicated-directory)
* [Step 4. Download Dependencies and the Self-Service Analytics Installation Packages](#step-4-download-dependencies-and-the-self-service-analytics)
* [Step 5. Obtain Download Instructions and Installation Packages](#step-5-obtain-download-instructions-and-installation-packages)
* [Step 6. Install the Self-Service Analytics Server](#step-6-install-the-self-service-analytics-server)
* [Step 7: Set Self-Service Analytics Microservices to Start Whenever the Server Boots](#step-7-set-self-service-analytics-microservices-to-start)
* [Step 8: Start the Microservices](#step-8-start-the-microservices)
* [Step 9. Configure the Firewall](#step-9-configure-the-firewall)
* [Step 10. Identify the Self-Service Analytics IP Address](#step-10-identify-the-self-service-analytics-ip-address)
* [Step 11. Access Self-Service Analytics](#step-11-access-self-service-analytics)
* [Step 12. Complete Post-Installation Steps](#step-12-complete-post-installation-steps)

<h3 id="step-1-review-the-prerequisites">
  Step 1. Review the Prerequisites
</h3>

Refer to [System Requirements](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#system-requirements) and [Server Size Guidelines](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#server-size-guidelines) for information on the recommended settings for deploying your software on-premises.

The target server for your software should meet the following conditions:

* The server does not have PostgreSQL already installed
* The server does not contain any Self-Service Analytics property files, meaning if a previous version of was installed in this server, ensure that all property files have been deleted.
* The user installing Self-Service Analytics is able to use the `sudo` command in the server

#### CentOS Requirements

<Note>
  CentOS 7 & 8 are end of life (EOL) support. CentOS Stream 9 is supported for new instances of Self-Service Analytics. Upgrade your operating system to CentOS Stream 9 before upgrading your instance. For more information, see [Operating System Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#operating-system-support).
</Note>

#### Time Synchronization Requirements

Self-Service Analytics benefits from time synchronization in your network. Specifically, it leverages Network Time Protocol (NTP), which performs time synchronization of networked servers to Coordinated Universal Time (UTC). If needed, read [Use the Network Time Protocol to Synchronize Time](#use-the-network-time-protocol-to-synchronize-time) for instructions on setting this up.

#### Java Requirements

You must have Java 21 installed to run and use Self-Service Analytics. Without it, your software will not start.

After you have made any needed adjustments to your network configurations, return to this topic to continue the installation process. See [How Self-Service Analytics Validates an Environment's Java Version](#how-self-service-analytics-validates-an-environment-s-java).

<h3 id="step-2-set-up-self-service-analytics-s-metadata-store">
  Step 2. Set Up Self-Service Analytics's Metadata Store
</h3>

Self-Service Analytics uses a standard PostgreSQL database instance to store its metadata. We strongly recommend using this instance as it is configured with the appropriate settings.

<Note>
  New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

To use your own or alternative PostgreSQL instance, contact insightsoftware [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) for further guidance.

Read [Install and Set Up Self-Service Analytics's Metadata Store](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/install-metadata-store). Complete the setup instructions and then return to this topic to continue the manual installation of Self-Service Analytics on your server.

<h3 id="step-3-configure-a-dedicated-directory">
  Step 3. Configure a Dedicated Directory
</h3>

Before you can download the Self-Service Analytics installation packages onto your server, you need to create the Self-Service Analytics directory where the installation and property files are stored. After the directory is created, you need to create property files in that directory.

<h4 id="create-the-self-service-analytics-directory">
  Create the Self-Service Analytics Directory
</h4>

Create the following directory to store all Self-Service Analytics-related files:

```bash theme={null}
sudo install -o root -g root -m 0755 -d /etc/zoomdata
```

<h4 id="create-the-default-self-service-analytics-properties-file">
  Create the Default Self-Service Analytics Properties File
</h4>

Create the default Self-Service Analytics properties file that contains the available variables and parameters related to Self-Service Analytics operation:

```bash theme={null}
sudo touch /etc/zoomdata/zoomdata.properties
sudo chmod 0644 /etc/zoomdata/zoomdata.properties
sudo vi /etc/zoomdata/zoomdata.properties
```

#### Create the Query Engine Properties File

Create the Self-Service Analytics query engine properties file that contains the available variables and parameters related to query engine operation:

```bash theme={null}
sudo touch /etc/zoomdata/query-engine.properties
sudo chmod 0644 /etc/zoomdata/query-engine.properties
sudo vi /etc/zoomdata/query-engine.properties
```

<h4 id="add-the-default-metadata-parameters-to-the-appropriate-self">
  Add the Default Metadata Parameters to the Appropriate Self-Service Analytics Properties File
</h4>

1. Add the following metadata store-related parameters in the newly-created `zoomdata.properties` file. Essentially, you are storing the username and password details for the metadata store in this property file.

   ```properties theme={null}
   spring.datasource.url=jdbc:postgresql://<ip of host>:<port>/zoomdata
   spring.datasource.username=<db_username>
   spring.datasource.password=<db_password>
   keyset.destination.params.jdbc_url=jdbc:postgresql://<ip of host>:<port>/zoomdata-keyset
   keyset.destination.params.user_name=<db_username>
   keyset.destination.params.password=<db_password>
   keyset.destination.schema=public
   upload.destination.params.jdbc_url=jdbc:postgresql://<ip of host>:<port>/zoomdata-upload
   upload.destination.params.user_name=<db_username>
   upload.destination.params.password=<db_password>
   upload.destination.schema=public
   upload.batch-size=1000
   ```

2. Add the following `zoomdata-qe` database metadata store-related parameters in the newly-created `query-engine.properties` file.

   ```properties theme={null}
   spring.qe.datasource.jdbcUrl=jdbc:postgresql://<ip of host>:<port>/zoomdata-qe
   spring.qe.datasource.username=<db_username>
   spring.qe.datasource.password=<db_password>
   ```

In each case, remember to save the files before exiting the editor.

<h3 id="step-4-download-dependencies-and-the-self-service-analytics">
  Step 4. Download Dependencies and the Self-Service Analytics Installation Packages
</h3>

Self-Service Analytics requires the following external dependencies for a successful installation:

* [EPEL](https://fedoraproject.org/wiki/EPEL) (for CentOS environments)
* [Socat](https://pkgs.org/download/socat)
* [OpenSSL](https://www.openssl.org/source/)

If you have not already received the Self-Service Analytics installation package, contact insightsoftware [Technical Support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) to request it. In the request, be sure to include the Linux operating system version you are using (for example, CentOS).

<Note>
  If your server does not have internet access, you will need an internet-enabled computer to download the packages and then move them to the intended server.
</Note>

<h3 id="step-5-obtain-download-instructions-and-installation-packages">
  Step 5. Obtain Download Instructions and Installation Packages
</h3>

Contact your insightsoftware [technical support](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/tech-support) representative and obtain download instructions for the Self-Service Analytics installation packages. Follow the instructions and download the installation packages, remembering to place them in the Self-Service Analytics directory on the target server. The following Self-Service Analytics components are included in your installation packages:

* The Self-Service Analytics server
* Connector microservices
* Query Engine

For more information, see [Supported Technologies Reference](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/installation-prerequisites#supported-technologies-reference)

<h3 id="step-6-install-the-self-service-analytics-server">
  Step 6. Install the Self-Service Analytics Server
</h3>

Use the following command to install Self-Service Analytics in a CentOS environment:

```bash theme={null}
sudo yum install zoomdata* -y
```

Use the following command to install Self-Service Analytics in an Ubuntu environment:

```bash theme={null}
sudo dpkg -i zoomdata*
```

<Note>
  Install this package before you complete Step 7 and Step 8. The commands in those steps enable and start every `zoomdata` service found on the server, including this one.
</Note>

<h3 id="step-7-set-self-service-analytics-microservices-to-start">
  Step 7: Set Self-Service Analytics Microservices to Start Whenever the Server Boots
</h3>

Microservices need to be set to automatically start whenever the server is started or rebooted.

In a CentOS or an Ubuntu environment, run the following command:

```bash theme={null}
sudo systemctl enable $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')
```

Optionally, you can manually set up each microservice by running the following commands in CentOS and Ubuntu:

```bash theme={null}
sudo systemctl enable zoomdata-edc-<connector-name>
sudo systemctl enable zoomdata-screenshot-service
sudo systemctl enable zoomdata-consul
sudo systemctl enable zoomdata
sudo systemctl enable zoomdata-query-engine
```

<h3 id="step-8-start-the-microservices">
  Step 8: Start the Microservices
</h3>

The Self-Service Analytics microservices must be enabled.

In a CentOS or an Ubuntu environment, run the following command:

```bash theme={null}
sudo systemctl start $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')
```

Optionally, you can manually enable each microservice by running the following commands in CentOS and Ubuntu:

```bash theme={null}
sudo systemctl start zoomdata-edc-<connector-name>
sudo systemctl start zoomdata-edc-rts
sudo systemctl start zoomdata-screenshot-service
sudo systemctl start zoomdata-query-engine
sudo systemctl start zoomdata
```

<h3 id="step-9-configure-the-firewall">
  Step 9. Configure the Firewall
</h3>

See [Configure the Firewall](#configure-the-firewall) for complete information.

<h3 id="step-10-identify-the-self-service-analytics-ip-address">
  Step 10. Identify the Self-Service Analytics IP Address
</h3>

Read [Identify the Self-Service Analytics IP Address](#identify-the-self-service-analytics-ip-address) for complete information.

<h3 id="step-11-access-self-service-analytics">
  Step 11. Access Self-Service Analytics
</h3>

Read [Access and Use Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access) for more information.

<h3 id="step-12-complete-post-installation-steps">
  Step 12. Complete Post-Installation Steps
</h3>

Complete any post-installation actions needed for your environment. These include, but are not limited to:

1. Enabling the Real-Time Sales demo data source
2. Setting up the Screenshot microservice

See [Post-Installation Options](#post-installation-options) for more information and links to instructions.

<h2 id="obtain-the-installation-package-without-internet-access">
  Obtain the Installation Package Without Internet Access
</h2>

<Note>
  New installations of Self-Service Analytics use PostgreSQL 16. If you are upgrading your environment to Self-Service Analytics, you can retain your existing PostgreSQL version.
</Note>

If the target server for your Self-Service Analytics installation does not have Internet access, you can download the PostgreSQL repo package from another source and then transfer the files to the target server. Take the following steps to obtain the PostgreSQL repo package:

1. Access the PostgreSQL website, navigate to the appropriate version of PostgreSQL section, and locate the correct repo package for your target server.

   ```
   https://yum.postgresql.org/repopackages.php#pg12
   ```

2. Copy the link address of the PostgreSQL repo package. For example, right-click on the link and select the **Copy Link Address** option.

3. Paste the copied link address into the following command line and execute it:

   ```bash theme={null}
   yum install -y <copied_link_URL>
   ```

   This command needs to be run from a server containing the same OS version as the target server for the Self-Service Analytics installation.

4. Run the following command line to download the dependencies for your selected PostgreSQL repo package:

   ```bash theme={null}
   yum install --enablerepo=pgdg12 -y postgresql12-server --downloadonly --downloaddir=/<your_target_directory>
   ```

5. Transfer the PostgreSQL repo package to the target server.

6. Run the PostgreSQL repo package from the target server.

## Manually Install OpenJDK

Self-Service Analytics 26.3 and later runs on Java 21. When you perform a straightforward upgrade to this release, Java is updated automatically.

**Manually install OpenJDK**

1. Stop all Self-Service Analytics components (if any are running) before you install OpenJDK. See [Stop Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#stop-microservices).

2. Run the following command on the installation machine.

   For JDK 21:

   ```bash theme={null}
   sudo mkdir -p /opt/zoomdata/jre && curl -sL https://corretto.aws/downloads/latest/amazon-corretto-21-x64-linux-jdk.tar.gz | sudo tar zx -C /opt/zoomdata/jre --strip-components=1
   ```

3. Restart all Self-Service Analytics components. See [Start Microservices](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/install/about-microsvcs#start-microservices).

<Note>
  In Windows environments, Self-Service Analytics installs a compatible JDK as part of the bootstrap installation. To install a system wide Java distribution, see [https://www.java.com/en/download/help/windows\_manual\_download.html](https://www.java.com/en/download/help/windows_manual_download.html).
</Note>

For information on how Self-Service Analytics validates the version of Java used in an environment, see [How Self-Service Analytics Validates an Environment's Java Version](#how-self-service-analytics-validates-an-environment-s-java).

<h2 id="how-self-service-analytics-validates-an-environment-s-java">
  How Self-Service Analytics Validates an Environment's Java Version
</h2>

Self-Service Analytics determines which Java is being used in your environment while the microservices are starting. It evaluates your environment in the following sequence. The first Java executable in this sequence that meets minimum requirements is used and validation stops.

1. The directory in the \$JAVA\_HOME environment variable path is evaluated to verify that it points to JRE/JDK and its `$JAVA_HOME/bin/java` path contains a valid Java executable that meets the minimum requirements.
2. The `/etc/environment` file is parsed for its JAVA\_HOME variable identifying the Java installation directory. This Java installation directory is then evaluated for a valid Java executable that meets the minimum requirements.
3. The `<install-path>/jre` folder is evaluated for a valid Java executable that meets the minimum requirements.
4. The directories listed in the \$PATH environment variable are evaluated for a valid Java executable that meets the minimum requirements.

If a Java executable that meets the minimum requirements is not found in this process, an exception occurs and Self-Service Analytics is not started.

<h2 id="use-the-network-time-protocol-to-synchronize-time">
  Use the Network Time Protocol to Synchronize Time
</h2>

The Network Time Protocol daemon (NTPD) is a service that performs time synchronization of networked servers to Coordinated Universal Time (UTC). Using NTP helps mitigate the effects of network latency by synchronizing your network with accurate time servers. In addition, certain Self-Service Analytics functionalities benefit from having NTP in your network, including:

* The connection between Self-Service Analytics server and the data sources (so that monitoring of data source performance and possible network latency issues can be done).
* Authentication protocols (for example, [Kerberos](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/kerberos-sso)), which require precise time correspondence on all instances to work properly.
* Scaled out deployments so that all nodes can have synchronized time.
* [Single Sign-On (via SAML)](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/authorization-tools#implement-single-sign-on-sso-via-saml), to avoid potential failure by the identity provider to authenticate SAML users.

Ideally, NTP should be installed prior to installing the Self-Service Analytics server. The steps below help you install the NTP service in your network. However, be sure to work with your network administrator to use the most appropriate time protocol service for your network environment.

<h3 id="install-ntp-on-rpm-based-distributions">
  Install NTP on RPM-Based Distributions
</h3>

To install NTP on CentOS or RHEL, perform the following steps:

1. Run the following command:

   ```bash theme={null}
   sudo yum install -y ntp
   ```

2. Check that the service is up and running:

   ```bash theme={null}
   sudo service ntpd status
   ```

### Install NTP on Ubuntu

To install NTP on Ubuntu, perform the following steps:

1. Run the following commands:

   ```bash theme={null}
   sudo apt-get update
   sudo apt-get install -y ntp
   ```

2. Check that the service is up and running:

   ```bash theme={null}
   sudo service ntp status
   ```

<h3 id="post-installation-steps">
  Post-Installation Steps
</h3>

If you install the NTP service after Self-Service Analytics has already been installed in your network, you should restart Self-Service Analytics service after NTP has been successfully installed:

```bash theme={null}
sudo service zoomdata restart
```

<h2 id="configure-the-firewall">
  Configure the Firewall
</h2>

After you have successfully installed the Self-Service Analytics components onto your server, you need to configure the firewall. Configure `iptables` to accept port 8443 and to forward incoming HTTPS requests on port 443 to the Self-Service Analytics server port 8443. Note that the command lines may differ slightly depending on the Linux environment. Select the appropriate Linux environment below.

* [CentOS Commands](#centos-commands)
* [Ubuntu Commands](#ubuntu-commands)
* [Windows Defender Firewall](#windows-defender-firewall)

These commands set up the firewall rules to the default `eth0` network interface. If you want to apply them to another network interface, replace it in the commands below. If you want to apply the rules to all the interfaces, remove '`-i eth0`' from the command line.

<h3 id="centos-commands">
  CentOS Commands
</h3>

```bash theme={null}
sudo yum install iptables-services
sudo systemctl enable iptables
sudo systemctl start iptables
sudo iptables -I INPUT 1 -i eth0 -p tcp --dport 8443 -j ACCEPT
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j DNAT --to-destination :8443
sudo iptables -I INPUT 1 -i eth0 -p tcp --dport 80 -j ACCEPT
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination :8080
sudo /usr/libexec/iptables/iptables.init save
```

<h3 id="ubuntu-commands">
  Ubuntu Commands
</h3>

```bash theme={null}
sudo apt-get install iptables-persistent
sudo iptables -I INPUT 1 -i eth0 -p tcp --dport 8443 -j ACCEPT
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 443 -j DNAT --to-destination :8443
sudo iptables -I INPUT 1 -i eth0 -p tcp --dport 80 -j ACCEPT
sudo iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j DNAT --to-destination :8080
sudo netfilter-persistent save
sudo netfilter-persistent reload
```

When prompted for input for the question of `iptables-persistent`, enter `yes`.

<h3 id="windows-defender-firewall">
  Windows Defender Firewall
</h3>

See this best practices article: [Best practices for configuring Windows Defender - Windows Security](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/best-practices-configuring).

<h2 id="configure-the-maximum-number-of-open-processes-and-files">
  Configure the Maximum Number of Open Processes and Files
</h2>

Configuring the maximum number of open processes and open files that can run in your operating environment keeps Self-Service Analytics processes from hitting or exceeding the resource limits that may be imposed by your operating system.

Instructions are provided here for the following operating environments:

### CentOS Instructions

If you are installing via RPM using CentOS or Red Hat, the recommended settings differ slightly. Because `systemd` is responsible for starting the various microservices, you need to amend the files and microservices that are launched so the `limits.conf` file is not ignored.

<Warning>
  Create an override directory specifically for the microservices you want to override.
</Warning>

1. Create a new `systemd` directory:

   ```bash theme={null}
   mkdir /etc/systemd/system/<servicename>.service.d/
   ```

   Replace \<servicename> with the microservice you need to override.

2. The file name for the microservice you want to override needs to be in `.conf`, so use the following command:

   ```
   touch /etc/systemd/system/<servicename>.service.d/<servicename>.conf
   ```

For more information about managing microservices for Red Hat, see the [Red Hat documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/chap-managing_services_with_systemd).

If Self-Service Analytics stops operating and you receive the error message `too many files, cannot operate`, you may need to increase the system limits in your CentOS or supported Ubuntu environments. Make the following changes:

1. In the `service.d` folder for each microservice, open the `limits.conf` file. If the configuration file does not exist, this command creates it.

   ```bash theme={null}
   vi /etc/systemd/system/<servicename>.service.d/limits.conf
   ```

2. Add the following to the file:

   ```
   [Service]
   LimitNOFILE=10000
   ```

3. Restart the init service:

   ```bash theme={null}
   systemctl daemon-reload
   ```

4. Restart the `zoomdata` microservice:

   ```bash theme={null}
   systemctl restart zoomdata.service
   ```

5. Verify your changes were applied:

   ```
   ps -ef | grep zoomdata-web | grep -v grep | awk '{system("cat /proc/"$2"/limits")}' | grep -i "Max open files"
   ```

6. In the output, you should see the following, indicating that your changes were applied:

   ```
   Max open files 10000 10000 files
   ```

<h2 id="identify-the-self-service-analytics-ip-address">
  Identify the Self-Service Analytics IP Address
</h2>

After you have installed Self-Service Analytics and configured the [firewall](#configure-the-firewall), you need to identify the Self-Service Analytics IP address so you can access Self-Service Analytics on your web browser. Record the IP address of the host where Self-Service Analytics is installed.

To obtain the Self-Service Analytics IP address, enter the following command in a terminal window on the Self-Service Analytics server:

```
[zoomdata@localhost ~]$ hostname -I
```

Make a note of this IP address. You will need it when you [access Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/access) from a web browser.

<h2 id="post-installation-options">
  Post-Installation Options
</h2>

After the Self-Service Analytics environment has been installed in your server, the following configuration options are available to you:

<table>
  <thead>
    <tr>
      <th>To</th>
      <th>Read</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Add an SSL Certificate.

        <br />

        By default, Self-Service Analytics enables an *http* port. To enable *https*, you must add an SSL certificate to the Self-Service Analytics server.
      </td>

      <td>[Add an SSL Certificate](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/kerberos-sso#add-an-ssl-certificate)</td>
    </tr>

    <tr>
      <td>Disable SSL.</td>
      <td>[Disable the SSL Certificate in Self-Service Analytics](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/security/kerberos-sso#disable-the-ssl-certificate-in-self-service-analytics)</td>
    </tr>

    <tr>
      <td>
        Use SQL-based connectors.

        <br />

        Some SQL connectors require a JDBC driver to be configured before you can connect to your data source. You can download the driver from the vendor’s site. Be aware that you need to download and configure JDBC drivers for the following Self-Service Analytics connectors as soon as you complete the Self-Service Analytics installation:

        <br />

        * [MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql)
        * [MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql)
        * [Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle)
        * [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift)
        * [Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata)
      </td>

      <td>[Add a JDBC Driver](#add-a-jdbc-driver)</td>
    </tr>

    <tr>
      <td>Configure Self-Service Analytics memory settings.</td>
      <td>[Configure Memory Settings](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#configure-memory-settings)</td>
    </tr>

    <tr>
      <td>
        Enable Self Service Reports and expand data export options.

        <br />

        Self service reports and expanded data export options are controlled by the Self Service Report microservice, and must be [enabled in your environment](/simba-embedded-analytics/docs/self-service-analytics/26.3/administer/configure/config-mgmt-ov#server-level-variables) if you want your users access these features.
      </td>

      <td>[Self Service Report Microservice](/simba-embedded-analytics/docs/self-service-analytics/26.3/get-started/arch-microservice#self-service-report-microservice)</td>
    </tr>

    <tr>
      <td>Use Self-Service Analytics's sample data generator.</td>
      <td>[Manage the Real Time Sales Demo Source](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/enabling-real-time-sales-demo-source)</td>
    </tr>
  </tbody>
</table>

<h2 id="add-a-jdbc-driver">
  Add a JDBC Driver
</h2>

For certain data sources, the JDBC drivers needed are no longer included in the installation package of Self-Service Analytics. You need to provide your own JDBC driver for the following data sources:

* [Amazon Redshift](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-amazon-redshift)
* [Dremio](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-dremio)
* [Jira](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-jira)
* [MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql)
* [MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql)
* [Oracle](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-oracle)
* [SAP Hana](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-hana)
* [SAP S/4HANA](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-saps-4hana)
* [SAP IQ](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-sap-iqsql)
* [Salesforce](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-salesforce)
* [Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake)
* [Teradata](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-teradata)
* [Vertica](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-vertica)

The following Self-Service Analytics connectors are distributed with a JDBC driver, but you can download and install newer versions using the information in this topic: [Snowflake](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-snowflake).

This approach allows you the flexibility to add a specific JDBC driver that meets your licensing, support policies or operational needs. As a result, in order to connect to and visualize data from Self-Service Analytics, you first need to download and install a JDBC driver.

### Caveats

If the JDBC driver for the Self-Service Analytics connector is not configured, the connector server will not start and the connector cannot be enabled within Self-Service Analytics. See [Manage Connectors and Connector Servers](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connectors-ov#manage-connectors-and-connector-servers).

### Install a JDBC Driver

To use any of the connectors listed above, perform the following steps to install the required JDBC driver after successful installation of Self-Service Analytics microservices:

1. Download the required driver from the vendor’s site to the corresponding Self-Service Analytics instance. Place the required driver in the following folder:

   * Linux platforms: `/opt/zoomdata/lib/edc-<connector_name>/`.

   * Windows platforms: `<install_path>\lib\edc-<connector_name>/`. For example, place MySQL libraries for the default Self-Service Analytics path install in this folder: `c:\logi-composer\lib\edc-mysql\` if Self-Service Analytics is installed in `c:\logi-composer\`.

     <Warning>
       The truststore path passed as part of the JDBC url must only contain forward (/) slashes in Windows environments.
     </Warning>

   If the folder does not exist, you need to create it in the location mentioned above. See the following table for resources for vendor’s JDBC drivers. Make sure that the Self-Service Analytics administrator has read-level access rights to the JDBC driver (JAR) file.

   | Connector | Link to JDBC Driver | License Type | Supported Version |
   | - | - | - | - |
   | Amazon Redshift | [http://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html#download-jdbc-driver](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html#download-jdbc-driver) | Commercial | 1.2.16.1027 |
   | Dremio | [https://www.dremio.com/drivers/](https://www.dremio.com/drivers/) | LGPL | 4.1 |
   | MemSQL | [https://dev.mysql.com/downloads/connector/j/](https://dev.mysql.com/downloads/connector/j/) | LGPL | 8.0.13 |
   | MySQL | [https://dev.mysql.com/downloads/connector/j/](https://dev.mysql.com/downloads/connector/j/) | LGPL | 8.0.13 |
   | Oracle | [https://www.oracle.com/database/technologies/appdev/jdbc-ucp-183-downloads.html](https://www.oracle.com/database/technologies/appdev/jdbc-ucp-183-downloads.html) | Commercial | 18.3.0.0 |
   | SAP Hana | [https://developers.sap.com/trials-downloads.html](https://developers.sap.com/trials-downloads.html) | Commercial | 2.0 |
   | SAP IQ | [https://www.sap.com/index.html](https://www.sap.com/index.html) | Commercial | 16 |
   | Snowflake | [https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc/](https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc/) | LGPL | |
   | Teradata | [https://downloads.teradata.com/download/connectivity/jdbc-driver](https://downloads.teradata.com/download/connectivity/jdbc-driver) | Commercial | 15.00.00.30 |
   | Vertica | [https://www.vertica.com/client-drivers/](https://www.vertica.com/client-drivers/) | Commercial | All |

2. Use the following command to access and open the property file:

   * Linux platforms: `vi /etc/zoomdata/edc-<connector_name>.properties`. If you are not logged in as a root user, enter `sudo vi /etc/zoomdata/edc-<connector_name>.properties` to create the desired file. If the properties file does not exist, this command creates it.
   * Windows platforms, using a text editor that can edit Windows property files: `<install-path>\conf-modified\edc-<connector_name>.properties`.

   Replace `<connector_name>` with the name of the connector you are configuring:

   | Connector | Connector Property File Name |
   | - | - |
   | Amazon Redshift | edc-redshift.properties |
   | MemSQL | edc-memsql.properties |
   | Microsoft SQL Server | edc-mssql.properties |
   | MySQL | edc-mysql.properties |
   | Oracle | edc-oracle.properties |
   | SAP Hana | edc-saphana.properties |
   | SAP S/4HANA | |
   | SAP IQ | edc-sapiq.properties |
   | Snowflake | edc-snowflake.properties |
   | Teradata | edc-teradata.properties |
   | Vertica | edc-vertica.properties |

3. In the `edc-<connector_name>.properties` file, add the following property:

   ```properties theme={null}
   loader.path=<JDBC_driver_filepath>
   ```

   If you need to add multiple paths, use a comma-separated list:

   ```properties theme={null}
   loader.path=<JDBC_driver_filepath1>,<JDBC_driver_filepath2>
   ```

4. For [MemSQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-memsql) and [MySQL](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/connectors/connecting-to-mysql) connectors, add the following property to the property files:

   ```properties theme={null}
   datasource.driver-config.class-name=com.mysql.cj.jdbc.Driver
   ```

5. Save your changes to the properties file.

6. Restart the corresponding connector by running the appropriate command:

   * For CentOS and Ubuntu: `systemctl restart zoomdata-edc-<connector_name>`
   * For Windows: `PS C:\> Restart-Service -Name zoomdata-edc-<connector_name>`

7. Log in as the a member of the Supervisors group, access the Connectors page, and verify that the connector is enabled so it appears in the data source list. After the JDBC driver has been configured and the connector has been enabled, users with the correct access privileges can use the connector to connect to the data store in a [data source configuration](/simba-embedded-analytics/docs/self-service-analytics/26.3/connect-to-data/sources/data-source-config-overview).
