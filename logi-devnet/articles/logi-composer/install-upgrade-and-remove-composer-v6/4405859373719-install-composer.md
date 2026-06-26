---
title: "Install Composer"
id: 4405859373719
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405859373719-Install-Composer
updated_at: 2021-09-21T01:28:50Z
---

# Install Composer

# Install Composer

This section provides instructions for performing a clean installation of Composer in your operating environment and is applicable for both RPM (CentOS, RHEL) and Ubuntu environments.

For information about the difference between a clean installation of Composer and an upgrade to the latest GA release, see [*Clean Installation and Upgrade Differences*](https://devnet.logianalytics.com/hc/en-us/articles/4405851077783-Clean-Installation-and-Upgrade-Differences).

#### Upgrade and Migration Considerations

* In general, you can upgrade directly to the latest version of Composer from a prior version.
* If you are upgrading to a newer version of Composer and you also want to change your encryption mode, perform the upgrade first and then complete the steps described in [*Change the Encryption Mode*](https://devnet.logianalytics.com/hc/en-us/articles/4405859459351-Change-the-Encryption-Mode).
* Manually upgrading Composer no longer provides the Java Runtime Environment (JRE) needed for Composer to start. Make sure you have Java 11.0.5 or later installed before you manually install or manually upgrade to Composer 5.8 or later. If you do not, Composer will not start.

In generally, the installation process is automated and you only need to run an installation script. The installation script is implemented using Bootstrap. This script accesses a dedicated Composer repository and automatically downloads all the necessary components to install your Composer microservice.

You can install Composer without using the automated installation script. This lets you install and enable each Composer microservices manually in your target server. If you need an alternative option, read [*Alternative Installation Options*](https://devnet.logianalytics.com/hc/en-us/articles/4405851076887-Alternative-Installation-Options).

After the installation has completed, you need to activate the Composer microservices, download and configure a JDBC driver if you are using specific data sources (see [*Post-Installation Options*](https://devnet.logianalytics.com/hc/en-us/articles/4405851092631-Post-Installation-Options) for a list), and open a browser window and enter the specific IP address to access the Composer client.

Review and complete (as appropriate for your installation) the following installation information:

* [*Installation Prerequisites*](https://devnet.logianalytics.com/hc/en-us/articles/4405851087895-Installation-Prerequisites)
* [*Installation Steps*](https://devnet.logianalytics.com/hc/en-us/articles/4405851088791-Installation-Steps)
* [*Alternative Installation Options*](https://devnet.logianalytics.com/hc/en-us/articles/4405851076887-Alternative-Installation-Options)
* [*Post-Installation Options*](https://devnet.logianalytics.com/hc/en-us/articles/4405851092631-Post-Installation-Options)
* [*Access Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4405850867223-Access-Composer)
