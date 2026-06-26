---
title: "Install Composer Manually"
id: 43701105134605
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105134605-Install-Composer-Manually
updated_at: 2026-05-29T14:08:42Z
---

# Install Composer Manually

# Install Composer Manually

If running the installer script is not a viable option for you, you can install Composer manually.

**Note:** 
Manual install of Composer is not currently supported for Windows environments.

To install Composer manually, complete the following steps:

* [Step 1. Review the Prerequisites](#Step)
* [Step 2. Set Up Composer's Metadata Store](#Step2)
* [Step 3. Configure a Dedicated Directory](#Step3)
* [Step 4. Download Dependencies and the Composer Installation Packages](#Step4)
* [Step 5. Obtain Download Instructions and Installation Packages](#Step5)
* [Step 6. Install the Composer Server](#Step6)
* [Step 7: Set Composer Microservices to Start Whenever the Server Boots](#Step7)
* [Step 8: Start the Microservices](#Step8)
* [Step 9. Configure the Firewall](#Step9)
* [Step 10. Identify the Composer IP Address](#Step10)
* [Step 11. Access Composer](#Step11)
* [Step 12. Complete Post-Installation Steps](#Step12)

## Step 1. Review the Prerequisites

Refer to [System Requirements](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105740685-System-Requirements) and [Server Size Guidelines](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073249037-Server-Size-Guidelines) for information on the recommended settings for deploying your software on-premises.

The target server for your software should meet the following conditions:

* The server does not have PostgreSQL already installed
* The server does not contain any Composer property files, meaning if a previous version of Composer was installed in this server, ensure that all property files have been deleted.
* The user installing Composer is able to use the `sudo` command in the server

### CentOS Requirements

**Note:** CentOS 7 & 8 are end of life (EOL) support. CentOS Stream 9 is supported for new instances of Logi Composer 25.4 and higher. Upgrade your operating system to CentOS Stream 9 before upgrading your Composer instance. For more information, see [Operating System Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701136004365-Operating-System-Support).

### Time Synchronization Requirements

Composer benefits from time synchronization in your network. Specifically, it leverages Network Time Protocol (NTP), which performs time synchronization of networked servers to Coordinated Universal Time (UTC). If needed, read [Use the Network Time Protocol to Synchronize Time](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073403021-Use-the-Network-Time-Protocol-to-Synchronize-Time) for instructions on setting this up.

### Java Requirements

You must have Java 11.0.5 installed for Composer 23.1 and Java 17 installed for Composer 23.2 and later to use Composer. Without it, your software will not start.

After you have made any needed adjustments to your network configurations, return to this topic to continue the installation process.
See also [How Composer Validates an Environment's Java Version](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701135097613-How-Composer-Validates-an-Environment-s-Java-Version).

## Step 2. Set Up Composer's Metadata Store

Composer uses a standard PostgreSQL database instance to store its metadata. Composer strongly recommends using this instance as it is configured with the appropriate settings.

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

To use your own or alternative PostgreSQL instance, contact Composer [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) for further guidance.

Read [Install and Set Up Composer's Metadata Store](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134943757-Install-and-Set-Up-Composer-s-Metadata-Store). Complete the setup instructions and then return to this topic to continue the manual installation of Composer on your server.

## Step 3. Configure a Dedicated Directory

Before you can download the Composer installation packages onto your server, you need to create the Composer directory where the installation and property files are stored. After the directory is created, you need to create property files in that directory.

### Create the Composer Directory

Create the following directory to store all Composer-related files:

sudo install -o root -g root -m 0755 -d /etc/zoomdata

### Create the Default Composer Properties File

Create the default Composer properties file that contains the available variables and parameters related to Composer operation:

sudo touch /etc/zoomdata/zoomdata.properties  
sudo chmod 0644 /etc/zoomdata/zoomdata.properties  
sudo vi /etc/zoomdata/zoomdata.properties

### Create the Query Engine Properties File

Create the Composer query engine properties file that contains the available variables and parameters related to query engine operation:

sudo touch /etc/zoomdata/query-engine.properties  
sudo chmod 0644 /etc/zoomdata/query-engine.properties  
sudo vi /etc/zoomdata/query-engine.properties

### Add the Default Metadata Parameters to the Appropriate Composer Properties File

1. Add the following metadata store-related parameters in the newly-created `zoomdata.properties` file. Essentially, you are storing the username and password details for the metadata store in this property file.

   spring.datasource.url=jdbc:postgresql://<ip of host>:<port>/zoomdata  
   spring.datasource.username=<db\_username>  
   spring.datasource.password=<db\_password>  
   keyset.destination.params.jdbc\_url=jdbc:postgresql://<ip of host>:<port>/zoomdata-keyset  
   keyset.destination.params.user\_name=<db\_username>  
   keyset.destination.params.password=<db\_password>  
   keyset.destination.schema=public  
   upload.destination.params.jdbc\_url=jdbc:postgresql://<ip of host>:<port>/zoomdata-upload  
   upload.destination.params.user\_name=<db\_username>  
   upload.destination.params.password=<db\_password>  
   upload.destination.schema=public  
   upload.batch-size=1000
2. Add the following `zoomdata-qe` database metadata store-related parameters in the newly-created `query-engine.properties` file.

   spring.qe.datasource.jdbcUrl=jdbc:postgresql://<ip of host>:<port>/zoomdata-qe  
   spring.qe.datasource.username=<db\_username>  
   spring.qe.datasource.password=<db\_password>

In each case, remember to save the files before exiting the editor.

## Step 4. Download Dependencies and the Composer Installation Packages

Composer requires the following external dependencies for a successful installation:

* [EPEL](https://fedoraproject.org/wiki/EPEL) (for CentOS environments)
* [Socat](https://pkgs.org/download/socat)
* [OpenSSL](https://www.openssl.org/source/)

If you have not already received the Composer installation package, contact Composer [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) to request it. In the request, be sure to include the Linux operating system version you are using (for example, CentOS). You can select the Support button on this page to create your request.

**Note:** 
If your server does not have internet access, you will need an internet-enabled computer to download the packages and then move them to the intended server.

## Step 5. Obtain Download Instructions and Installation Packages

Contact your
Composer [technical support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) representative and obtain download instructions for the Composer installation packages. Follow the instructions and download the installation packages, remembering to place them in the Composer directory on the target server. The following Composer components are included in your installation packages:

* The Composer server
* Connector microservices
* Query Engine

## Step 6. Install the ComposerServer

Use the following command to install Composer in a CentOS environment:

sudo yum install zoomdata\* -y

Use the following command to install Composer in an Ubuntu environment:

sudo dpkg -i zoomdata\*

## Step 7: Set ComposerMicroservices to Start Whenever the Server Boots

Microservices need to be set to automatically start whenever the server is started or rebooted.

In a CentOS or an Ubuntu environment, run the following command:

sudo systemctl enable $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')

Optionally, you can manually set up each microservice by running the following commands in CentOS and Ubuntu:

sudo systemctl enable zoomdata-edc-<connector-name>  
sudo systemctl enable zoomdata-screenshot-service  
sudo systemctl enable zoomdata-consul  
sudo systemctl enable zoomdata  
sudo systemctl enable zoomdata-query-engine

## Step 8: Start the Microservices

The Composer microservices must be enabled.

In a CentOS or an Ubuntu environment, run the following command:

sudo systemctl start $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')

Optionally, you can manually enable each microservice by running the following commands in CentOS and Ubuntu:

sudo systemctl start zoomdata-edc-<connector-name>  
sudo systemctl start zoomdata-edc-rts  
sudo systemctl start zoomdata-screenshot-service  
sudo systemctl start zoomdata-query-engine  
sudo systemctl start zoomdata

## Step 9. Configure the Firewall

Read [Configure the Firewall](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134548877-Configure-the-Firewall) for complete information.

## Step 10. Identify the ComposerIP Address

Read [Identify the Composer IP Address](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072661773-Identify-the-Composer-IP-Address) for complete information.

## Step 11. Access Composer

Read [Access Logi Composer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701052048397-Access-Logi-Composer) for more information.

## Step 12. Complete Post-Installation Steps

Complete any post-installation actions needed for your environment. These include, but are not limited to:

1. Enabling the Real-Time Sales demo data source
2. Setting up the Screenshot microservice.

See
[Post-Installation Options](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072984717-Post-Installation-Options) for more information and links to instructions.
