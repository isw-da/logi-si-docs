---
title: "Install Composer Manually"
id: 4405851085207
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851085207-Install-Composer-Manually
updated_at: 2021-09-21T01:28:49Z
---

# Install Composer Manually

# Install Composer Manually

If running the installer script is not a viable options for you, you can install Composer manually.

To install Composer manually, complete the following steps:

* [*Step 1. Review the Prerequisites*](#Step)
* [*Step 2. Set Up Composer's Metadata Store*](#Step2)
* [*Step 3. Configure a Dedicated Directory*](#Step3)
* [*Step 4. Download Dependencies and the Composer Installation Packages*](#Step4)
* [*Step 5. Obtain Download Instructions and Installation Packages*](#Step5)
* [*Step 6. Install the Composer Server*](#Step6)
* [*Step 7: Set Composer Microservices to Start Whenever the Server Boots*](#Step7)
* [*Step 8: Start Composer Microservices*](#Step8)
* [*Step 9. Configure the Firewall*](#Step9)
* [*Step 10. Identify the Composer IP Address*](#Step10)
* [*Step 11. Access Composer*](#Step11)
* [*Step 12. Complete Post-Installation Steps*](#Step12)

## Step 1. Review the Prerequisites

Refer to [*System Requirements*](https://devnet.logianalytics.com/hc/en-us/articles/4405859384727-System-Requirements) and [*Server Size Guidelines*](https://devnet.logianalytics.com/hc/en-us/articles/4405851099543-Server-Size-Guidelines) for information on the recommended settings for deploying Composer on-premises.

The target server for the Composer software should meet the following conditions:

* The server does not have PostgreSQL already installed
* The server does not contain any Zoomdata or Composer property files, meaning if a previous version of Zoomdata or Composer was installed in this server, ensure that all property files have been deleted.
* The user installing Composer is able to use the `sudo` command in the server

### CentOS Requirements

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) CentOS 6 is no longer supported and the special installation Bootstrap procedure (`bootstrap-zoomdata-centos6.run`) is no longer provided with this product. CentOS 6 is no longer supported by Red Hat Linux (RHEL). Use CentOS 7 or 8 instead.

### Time Synchronization Requirements

Composer benefits from time synchronization in your network. Specifically, Composer leverages Network Time Protocol (NTP), which performs time synchronization of networked servers to Coordinated Universal Time (UTC). If needed, read [*Use the Network Time Protocol to Synchronize Time*](https://devnet.logianalytics.com/hc/en-us/articles/4405859386519-Use-the-Network-Time-Protocol-to-Synchronize-Time) for instructions on setting this up.

### Java Requirements

You must have Java 11.0.5 or later installed to use Composer. Without it, Composer will not start.

#### Important CentOS 6 Information

CentOS 6 is no longer supported and the special installation Bootstrap procedure (`bootstrap-zoomdata-centos6.run`) is no longer provided with this product. CentOS 6 is no longer supported by Red Hat Linux (RHEL). Use CentOS 7 or 8 instead.

After you have made any needed adjustments to your network configurations, return to this topic to continue the installation process.
See also [*How Composer Validates an Environment's Java Version*](https://devnet.logianalytics.com/hc/en-us/articles/4405859375767-How-Composer-Validates-an-Environment-s-Java-Version).

## Step 2. Set Up Composer's Metadata Store

Composer uses a standard PostgreSQL v12 database instance to store its metadata. Composer strongly recommends using this instance as it is configured with the appropriate settings.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If you would like to use your own or alternative PostgreSQL instance, contact Composer [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support) for further guidance.

Read [*Install and Set Up Composer's Metadata Store*](https://devnet.logianalytics.com/hc/en-us/articles/4405859372695-Install-and-Set-Up-Composer-s-Metadata-Store). Complete the setup instructions and then return to this topic to continue the manual installation of Composer on your server.

## Step 3. Configure a Dedicated Directory

Before you can download the Composer installation packages onto your server, you need to create the Composer directory where the installation and property files are stored. After the directory is created, you need to create property files in that directory.

### Create the Composer Directory

Create the following directory to store all Composer-related files:

```
sudo install -o root -g root -m 0755 -d /etc/zoomdata
```

### Create the Default Composer Properties File

Create the default Composer properties file that contains the available variables and parameters related to Composer operation:

```
sudo touch /etc/zoomdata/zoomdata.properties  
sudo chmod 0644 /etc/zoomdata/zoomdata.properties  
sudo vi /etc/zoomdata/zoomdata.properties
```

### Create the Query Engine Properties File

Create the Composer query engine properties file that contains the available variables and parameters related to query engine operation:

```
sudo touch /etc/zoomdata/query-engine.properties  
sudo chmod 0644 /etc/zoomdata/query-engine.properties  
sudo vi /etc/zoomdata/query-engine.properties
```

### Add the Default Metadata Parameters to the Appropriate Composer Properties File

1. Add the following metadata store-related parameters in the newly-created `zoomdata.properties` file. Essentially, you are storing the username and password details for the metadata store in this property file.

   ```
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

   ```
   spring.qe.datasource.jdbcUrl=jdbc:postgresql://<ip of host>:<port>/zoomdata-qe  
   spring.qe.datasource.username=<db_username>  
   spring.qe.datasource.password=<db_password>
   ```

In each case, remember to save the files before exiting the editor.

## Step 4. Download Dependencies and the Composer Installation Packages

Composer requires the following external dependencies for a successful installation:

* [EPEL](https://fedoraproject.org/wiki/EPEL) (for CentOS environments)
* [Socat](https://pkgs.org/download/socat)
* [OpenSSL](https://www.openssl.org/source/)

If you have not already received the Composer installation package, contact Composer [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support) to request it. In the request, be sure to include the Linux operating system version you are using (for example, CentOS 7). You can select the Support button on this page to create your request.

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) If your server does not have internet access, you will need an internet-enabled computer to download the packages and then move them to the intended server.

## Step 5. Obtain Download Instructions and Installation Packages

Contact your
Composer [technical support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support) representative and obtain download instructions for the Composer installation packages. Follow the instructions and download the installation packages, remembering to place them in the Composer directory on the target server. The following Composer components are included in your installation packages:

* The Composer server
* Connector microservices
* Query Engine

![](https://devnet.logianalytics.com/hc/article_attachments/4406743739159/criticalicon.gif) CentOS 6 is no longer supported and the special installation Bootstrap procedure (`bootstrap-zoomdata-centos6.run`) is no longer provided with this product. CentOS 6 is no longer supported by Red Hat Linux (RHEL). Use CentOS 7 or 8 instead.

## Step 6. Install the Composer Server

Use the following command to install Composer in a CentOS environment:

```
sudo yum install zoomdata* -y
```

Use the following command to install Composer in an Ubuntu environment:

```
sudo dpkg -i zoomdata*
```

## Step 7: Set Composer Microservices to Start Whenever the Server Boots

Composer microservices need to be set to automatically start whenever the server is started or rebooted.

In a CentOS 7 or 8 or an Ubuntu 16 or 18 environment, run the following command:

```
sudo systemctl enable $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')
```

Optionally, you can manually set up each Composer microservice by running the following commands in CentOS 7 or 8 and Ubuntu 16 or 18:

```
sudo systemctl enable zoomdata-edc-<connector-name>  
sudo systemctl enable zoomdata-screenshot-service  
sudo systemctl enable zoomdata-consul  
sudo systemctl enable zoomdata  
sudo systemctl enable zoomdata-query-engine
```

## Step 8: Start Composer Microservices

The Composer microservices must be enabled.

In a CentOS 7 or 8 or an Ubuntu 16 or 18 environment, run the following command:

```
sudo systemctl start $(systemctl list-unit-files | grep zoomdata | awk '{print $1}')
```

Optionally, you can manually enable each Composer microservice by running the following commands in CentOS 7 or 8 and Ubuntu 16 or 18:

```
sudo systemctl start zoomdata-edc-<connector-name>  
sudo systemctl start zoomdata-edc-rts  
sudo systemctl start zoomdata-screenshot-service  
sudo systemctl start zoomdata-query-engine  
sudo systemctl start zoomdata
```

## Step 9. Configure the Firewall

Read [*Configure the Firewall*](https://devnet.logianalytics.com/hc/en-us/articles/4405859364759-Configure-the-Firewall) for complete information.

## Step 10. Identify the Composer IP Address

Read [*Identify the Composer IP Address*](https://devnet.logianalytics.com/hc/en-us/articles/4405851084311-Identify-the-Composer-IP-Address) for complete information.

## Step 11. Access Composer

Read [*Access Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405850867223-Access-Composer) for more information.

## Step 12. Complete Post-Installation Steps

Complete any post-installation actions needed for your environment. These include, but are not limited to:

1. Enabling the Real-Time Sales demo data source
2. Setting up the Screenshot microservice.

See
[*Post-Installation Options*](https://devnet.logianalytics.com/hc/en-us/articles/4405851092631-Post-Installation-Options) for more information and links to instructions.
