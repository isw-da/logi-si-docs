---
title: "Installation Steps"
id: 4405851088791
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851088791-Installation-Steps
updated_at: 2021-12-21T15:39:15Z
---

# Installation Steps

# Installation Steps

To begin the installation process, you must receive the installation instructions from Composer [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support). This email contains the installation script that you will run on the server where the Composer environment will reside. If you have not received installation instructions, open a ticket with Composer[Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support).

#### Important CentOS 6 Information

CentOS 6 is no longer supported and the special installation Bootstrap procedure (`bootstrap-zoomdata-centos6.run`) is no longer provided with this product. CentOS 6 is no longer supported by Red Hat Linux (RHEL). Use CentOS 7 or 8 instead.

#### Important Ubuntu Information

Ubuntu users who have Composer or Zoomdata versions earlier than 5.8 installed must first remove the legacy repository before upgrading Composer 5.8 or later. Use this command:

```
sudo rm -f /etc/apt/sources.list.d/saltstack.list
```

## Steps

After you have received installation instructions from [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support), complete the following steps.

* [*Step 1: Run the Installation Script*](#Step)
* [*Step 2: Configure the Firewall*](#Step2)
* [*Step 3: Identify the IP Address*](#Step3)
* [*Step 4: Access Composer from a Web Browser*](#Step4)

After you have installed Composer, review the post-installation options in [*Post-Installation Options*](https://devnet.logianalytics.com/hc/en-us/articles/4405851092631-Post-Installation-Options). For information about accessing Composer after it is installed, see [*Access Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405850867223-Access-Composer).

### Step 1: Run the Installation Script

The email or PDF you receive from Composer [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support) describes the command used to obtain the Composer installation bootstrap procedure and the command used to run the bootstrap procedure. Run these commands, in order, on the target server for Composer to start the automated installation process. The following Composer components are downloaded to your target server:

* Database for metadata store (using PostgreSQL v12)
* The Composer Server
* Query Engine
* Data Writer microservice
* Connector microservices

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg)Composer uses a packaged PostgreSQL v12 database instance to store its metadata and strongly recommends using this instance due to the specific configuration and version employed. If you would like to use another PostgreSQL instance, contact [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support) for further guidance.

When the installation script has completed, complete the remaining steps in this section.

### Step 2: Configure the Firewall

See [*Configure the Firewall*](https://devnet.logianalytics.com/hc/en-us/articles/4405859364759-Configure-the-Firewall).

### Step 3: Identify the IP Address

See [*Identify the Composer IP Address*](https://devnet.logianalytics.com/hc/en-us/articles/4405851084311-Identify-the-Composer-IP-Address).

### Step 4: Access Composer from a Web Browser

After the installation script has completed, it will take a few minutes for Composer to complete its setup of the metadata store. Please wait a few minutes before accessing Composer from your web browser. When you are ready to access Composer, read [*Access Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405850867223-Access-Composer).

![](https://devnet.logianalytics.com/hc/article_attachments/4406747382295/noteicon.jpg) We recommend that you log into Composer for the first time using supervisor credentials. This allows you to review all the account-level features available. As a supervisor, you can access functions that let you connect your data sources to Composer. You can also create and activate user accounts, including an admin user account that will allow you to access the admin functions. See
[*Supplied User Definitions*](https://devnet.logianalytics.com/hc/en-us/articles/4405859125911-Supplied-User-Definitions).

If you receive a message indicating that Composer is not yet accessible, the Composer setup may not yet be complete. Wait a few more minutes before trying again or opening a Support ticket. If you continue to have issues accessing Composer from your browser, open a ticket with Composer [Technical Support](https://devnet.logianalytics.com/hc/en-us/articles/4405859363351-Contact-Technical-Support).
