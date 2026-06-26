---
title: "Use the Network Time Protocol to Synchronize Time"
id: 4402955612311
section: "Install, Upgrade, and Remove Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955612311-Use-the-Network-Time-Protocol-to-Synchronize-Time
updated_at: 2021-08-07T17:31:23Z
---

# Use the Network Time Protocol to Synchronize Time

# Use the Network Time Protocol to Synchronize Time

The Network Time Protocol daemon (NTPD) is a service that performs time synchronization of networked servers to Coordinated Universal Time (UTC). Using NTP helps mitigate the effects of network latency by synchronizing your network with accurate time servers. In addition, certain Composer functionalities benefit from having NTP in your network, including:

* The connection between Composer server and the data sources (so that monitoring of data source performance and possible network latency issues can be done).
* Authentication protocols (for example,
  [Kerberos](https://devnet.logianalytics.com/hc/en-us/articles/4402955664023-Configure-Kerberos-Single-Sign-On-SSO-Settings)
  ), which require precise time correspondence on all instances to work properly.
* Scaled out deployments so that all nodes can have synchronized time.
* [Single Sign-On
  (via SAML)](https://devnet.logianalytics.com/hc/en-us/articles/4402963050775-Implement-Single-Sign-On-SSO-via-SAML), to avoid potential failure by the identity provider to authenticate SAML users.

Ideally, NTP should be installed prior to installing the Composer server. The steps below help you install the NTP service in your network. However, be sure to work with your network administrator to use the most appropriate time protocol service for your network environment.

## Install NTP on RPM-Based Distributions

To install NTP on CentOS or RHEL, perform the following steps:

1. Run the following command:

   ```
   sudo yum install -y ntp
   ```
2. Check that the service is up and running:

   ```
   sudo service ntpd status
   ```

## Install NTP on Ubuntu

To install NTP on Ubuntu, perform the following steps:

1. Run the following commands:

   ```
   sudo apt-get update     
   sudo apt-get install -y ntp
   ```
2. Check that the service is up and running:

   ```
   sudo service ntp status
   ```

## Post-Installation Steps

If you install the NTP service after Composer has already been installed in your network, you should restart Composer service after NTP has been successfully installed:

```
sudo service zoomdata restart
```

### Related Topics:

* [*Install Composer*](https://devnet.logianalytics.com/hc/en-us/articles/4402955601175-Install-Composer)
* [*Install Composer Manually*](https://devnet.logianalytics.com/hc/en-us/articles/4402955598487-Install-Composer-Manually)
