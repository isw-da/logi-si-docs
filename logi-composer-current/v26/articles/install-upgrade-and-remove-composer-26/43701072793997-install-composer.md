---
title: "Install Composer"
id: 43701072793997
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072793997-Install-Composer
updated_at: 2026-05-29T14:08:44Z
---

# Install Composer

# Install Composer

This section provides instructions for performing a clean installation of Composer in your operating environment and is applicable to for both RPM (CentOS, REHL) and Ubuntu environments.

For information about the difference between a clean installation of Composer and an upgrade to the latest GA release, see [Clean Installation and Upgrade Differences](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701134472973-Clean-Installation-and-Upgrade-Differences).

#### Upgrade and Migration Considerations

* Windows Server 2012R2 is not compatible with both Java17 binaries and the latest releases of Composer (23.2 and later). We recommend you use Windows 2016 or later to run Composer 23.2 and later.
* In general, you can upgrade directly to the latest version of Composer from a prior version.
* If you are upgrading to a newer version of Composer and you also want to change your encryption mode, perform the upgrade first and then complete the steps described in [Change the Encryption Mode](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701175423245-Change-the-Encryption-Mode).

**Note:** New installations of Logi Composer (v24.3 and later) use PostgreSQL 16. If you are upgrading your environment to v24.3 or later, you can retain your existing PostgreSQL version.

**Important:** If you are upgrading to a newer version of Composer and have created an attribute named `User.timeZone`, this may be overwritten on upgrade. See [Upgrade Workflow](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701068707725-Timezone-Conversion-for-Users#Upgrade) for more information about preparing your environment for the upgrade process.

In general, the installation process is automated and you only need to run an installation script. The installation script is implemented using Bootstrap. This script accesses a dedicated Composer repository and automatically downloads all the necessary components to install your Composer microservice.

You can install Composer without using the automated installation script. This lets you install and enable each Composer microservices manually in your target server. If you need an alternative option, read [Alternative Installation Options](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072353933-Alternative-Installation-Options).

**Note:** 
To install Composer in other environments, see [Install Composer in a Windows Environment](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072833421-Install-Composer-in-a-Windows-Environment). To install an orchestrated Composer solution, see [Running Composer in Kubernetes](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701110924173-Running-Composer-in-Kubernetes).

After the installation has completed, you need to activate the Composer microservices, download and configure a JDBC driver if you are using specific data sources (see [Post-Installation Options](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072984717-Post-Installation-Options) for a list), and open a browser window and enter the specific IP address to access the Composer client.

Review and complete (as appropriate for your installation) the following installation information:

* [Installation Prerequisites](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701135037709-Installation-Prerequisites)
* [Installation Steps](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701120422797-Installation-Steps)
* [Alternative Installation Options](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072353933-Alternative-Installation-Options)
* [Post-Installation Options](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072984717-Post-Installation-Options)
* [Access Logi Composer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701052048397-Access-Logi-Composer)
