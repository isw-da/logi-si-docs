---
title: "Configuring Remote Report Execution Host for Azure App Service Deployments"
id: 5281592516375
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281592516375-Configuring-Remote-Report-Execution-Host-for-Azure-App-Service-Deployments
updated_at: 2023-04-03T17:52:19Z
---

# Configuring Remote Report Execution Host for Azure App Service Deployments

# Configuring Remote Report Execution Host for Azure App Service Deployments

When Exago is deployed as an Azure App Service, some additional configuration is necessary. At a high level, these configuration steps are:

1. The Exago **Scheduler Service** must be installed and properly configured on an Azure Virtual Machine. Exago *v2019.1.5+* must be installed for both the Azure App Service and the Virtual Machine, and the version numbers must be the same.
2. On the Azure App Service installation, enable the Scheduler and Remote Execution.
3. Enable Exago’s **Puppeteer** image rendering libraries on the Azure Virtual Machine (for versions *pre-v2020.1*).

Detailed information about each of these requirements follows.

## 1. Azure Virtual Machine

Exago’s **Puppeteer** image rendering libraries were introduced in *v2019.1.5* of the application. At a minimum, *v2019.1.5* must be installed on the Azure Virtual Machine. The version number of the Scheduler Service must match the version number of the Web Application.

Refer to the topics in the Recommended References section below for complete details on the installation and configuration of the **Scheduler Service** and how to install Exago on a Virtual Machine in Azure.

#### Recommended References

* [Installing Exago on Azure](https://devnet.logianalytics.com/hc/en-us/articles/5281601143191-Installing-Exago-on-Azure)
* [Updating Recommendations](https://devnet.logianalytics.com/hc/en-us/articles/5281618359959-Updating-Recommendations)
* [Installing the Scheduler Service](https://devnet.logianalytics.com/hc/en-us/articles/5281624674327-Installing-the-Scheduler-Service)
* [Scheduler Service Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281627554583-Scheduler-Service-Configuration)

## 2. Settings

The **Scheduler Service** should already be properly installed and configured on the Azure Virtual Machine.

On the Exago installation running as an Azure App Service, there are four parameters in the **Admin Console** which direct it to schedule and execute reports on the Virtual Machine instead of in the App Service:

* **General** > **Scheduler Settings** > **Enable Report Scheduling** must be set to *True*. By default, the value is *False*.
* **General** > **Scheduler Settings** > **Enable Remote Report Execution** must be set to *True*. By default, the value is *False*.
* **General** > **Scheduler Settings** > **Schedule Remoting Host** must be set to the virtual machine Scheduler Service’s protocol, host name/IP address and port. (for example http://a.b.c.d:2000)
* **General** > **Scheduler Settings** > **Remote Execution Remoting Host** must be set the same as **Schedule Remoting Host** above.

#### Recommended References

* [Scheduler Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281608723095-Scheduler-Settings)

## 3. Enable Puppeteer pre-2020.1

By default, Exago will use the older **WkHtmlToImage** libraries for visualization rendering. Therefore, Puppeteer must be manually enabled by adding or changing a key in the virtual machine **Scheduler Service**‘s *eWebReportsScheduler.exe.config* file, as shown below:

```
<appSettings>
	<add key="useWkHtmlToImage" value="false" />
</appSettings>
```

This file is located in the **Scheduler Service**‘s installation directory. For example, `D:\Exago\ExagoScheduler\eWebReportsScheduler.exe.config`.

### Recommended References

* [Application Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings)
