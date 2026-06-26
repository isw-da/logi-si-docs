---
title: "Installation Steps"
id: 43701120422797
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120422797-Installation-Steps
updated_at: 2026-05-29T14:08:45Z
---

# Installation Steps

# Installation Steps

To begin the installation process, you must receive the installation instructions from Composer [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support). This email contains the installation script that you will run on the server where the Composer environment will reside. If you have not received installation instructions, open a ticket with Composer [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support).

**Note:** 
To install Composer in other environments, see [Install Composer in a Windows Environment](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072833421-Install-Composer-in-a-Windows-Environment). To install an orchestrated Composer solution, see [Running Composer in Kubernetes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701110924173-Running-Composer-in-Kubernetes).

## Steps

After you have received installation instructions from [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support), complete the following steps.

* [Step 1: Run the Installation Script](#Step)
* [Step 2: Configure the Firewall](#Step2)
* [Step 3: Identify the IP Address](#Step3)
* [Step 4: Access Composer from a Web Browser](#Step4)

After you have installed Composer, review the post-installation options in [Post-Installation Options](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072984717-Post-Installation-Options). For information about accessing Composer after it is installed, see [Access Logi Composer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701052048397-Access-Logi-Composer).

### Step 1: Run the Installation Script

The email or PDF you receive from Composer [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) describes the command used to obtain the Composer installation bootstrap procedure and the command used to run the bootstrap procedure. Run these commands, in order, on the target server for Composer to start the automated installation process.

Linux environments: The following Composer components are downloaded to your target server:

* Database for metadata store (using PostgreSQL)
* The Composer Server
* Query Engine
* Data Writer microservice
* Connector microservices

**Important:** Composer uses a packaged PostgreSQL database instance to store its metadata. Use the provided instance due to the specific configuration and version combination:

* Logi Composer v24.2 and earlier: PostgreSQL 12
* Composer v24.3 and later: PostgreSQL 16

If you would like to use another PostgreSQL instance, contact [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support) for further guidance.

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

  **Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.
* Corretto JDK17
* Chocolatey

To install other components, adjust bootstrap switches as needed. See [Windows Bootstrap Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120362381-Windows-Bootstrap-Reference), [Composer  Microservice Name Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701144824589-Composer-Microservice-Name-Reference) and [Data Connector Reference](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701113495693-Data-Connector-Reference).

When the installation script has completed, complete the remaining steps in this section.

### Step 2: Configure the Firewall

See [Configure the Firewall](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134548877-Configure-the-Firewall).

### Step 3: Identify the IP Address

See [Identify the Composer IP Address](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072661773-Identify-the-Composer-IP-Address).

### Step 4: Access Composer from a Web Browser

After the installation script has completed, it will take a few minutes for Composer to complete its setup of the metadata store. Please wait a few minutes before accessing Composer from your web browser. When you are ready to access Composer, read [Access Logi Composer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701052048397-Access-Logi-Composer).

**Note:** 
We recommend that you log into Composer for the first time using admin credentials. This allows you to review all the account-level features available. As an admin, you can access functions that let you connect your data sources to Composer. You can also create and activate user accounts, including an admin user account that will allow you to access the admin functions. See
[Supplied Users and User Groups](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701036219149-Supplied-Users-and-User-Groups).

If you receive a message indicating that Composer is not yet accessible, the Composer setup may not yet be complete. Wait a few more minutes before trying again or opening a Support ticket. If you continue to have issues accessing Composer from your browser, open a ticket with Composer [Technical Support](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072313613-Contact-Technical-Support).
