---
title: "Use the Network Time Protocol to Synchronize Time"
id: 43701073403021
section: "Install, Upgrade, and Remove Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701073403021-Use-the-Network-Time-Protocol-to-Synchronize-Time
updated_at: 2026-05-29T14:08:50Z
---

# Use the Network Time Protocol to Synchronize Time

# Use the Network Time Protocol to Synchronize Time

The Network Time Protocol daemon (NTPD) is a service that performs time synchronization of networked servers to Coordinated Universal Time (UTC). Using NTP helps mitigate the effects of network latency by synchronizing your network with accurate time servers. In addition, certain Composer functionalities benefit from having NTP in your network, including:

* The connection between Composer server and the data sources (so that monitoring of data source performance and possible network latency issues can be done).
* Authentication protocols (for example, [Kerberos](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701208766477-Configure-Kerberos-Single-Sign-On-SSO-Settings)), which require precise time correspondence on all instances to work properly.
* Scaled out deployments so that all nodes can have synchronized time.
* [Single Sign-On
  (via SAML)](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701194343565-Implement-Single-Sign-On-SSO-via-SAML), to avoid potential failure by the identity provider to authenticate SAML users.

Ideally, NTP should be installed prior to installing the Composer server. The steps below help you install the NTP service in your network. However, be sure to work with your network administrator to use the most appropriate time protocol service for your network environment.

## Install NTP on RPM-Based Distributions

To install NTP on CentOS or RHEL, perform the following steps:

1. Run the following command:

   sudo yum install -y ntp
2. Check that the service is up and running:

   sudo service ntpd status

## Install NTP on Ubuntu

To install NTP on Ubuntu, perform the following steps:

1. Run the following commands:

   sudo apt-get update   
   sudo apt-get install -y ntp
2. Check that the service is up and running:

   sudo service ntp status

## Post-Installation Steps

If you install the NTP service after Composer has already been installed in your network, you should restart Composer service after NTP has been successfully installed:

sudo service zoomdata restart

### Related Topics:

* [Install Composer](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701072793997-Install-Composer)
* [Install Composer Manually](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701105134605-Install-Composer-Manually)
