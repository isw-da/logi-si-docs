---
title: "Installing the Scheduler [Linux]"
id: 5281548496791
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281548496791-Installing-the-Scheduler-Linux
updated_at: 2022-05-03T22:08:33Z
---

# Installing the Scheduler [Linux]

# Installing the Scheduler [Linux]

This video explains how to install Exago BI’s Scheduler Service on a Linux server with Apache.

[<< Configuring the REST Web Service [Linux]](https://devnet.logianalytics.com/hc/en-us/articles/5281562765719-Configuring-the-REST-Web-Service-Linux-) Previous Video

Next Video [Configuring the Scheduler [Linux] >>](https://devnet.logianalytics.com/hc/en-us/articles/5281540739351-Configuring-the-Scheduler-Linux-)

## Transcript

Welcome back to the Exago Technical Training Series! In this video we’ll demonstrate how to install and configure the Exago Scheduler Service on a Linux server with Apache installed. This video will discuss Apache only, but the installation with NGINX is very similar.

Before we begin, a note about operating systems and version numbers. Although they do not need to reside on the same server, Scheduler Services installed on Windows are only compatible with Web Applications also installed on Windows. Likewise, Linux Scheduler Services are only compatible with Web Applications installed on Linux. Additionally, the version number of the Scheduler Service and Web Application must always match. Therefore, if the Scheduler Service is deployed, it should be updated at the same time and with the same installer application as the Web Application to insure the version numbers are always the same.

The first step its to download the application installer. For information on accessing the installer, see the Introduction video of this series. Navigate to the Installer directory. Then, call the installer as root. The -d switch tells the installer the directory in which to install Exago. Consider versioning or using environment specific nomenclature for your installs to keep track of different versions. The -m switch followed by TRUE tells the installer to install the Mono framework along with Exago. This is Exago for the Scheduler Service to run. Although we’ve previously installed Mono with the Web Application, the installer will check first if Mono is already installed and skip this step if not necessary. Next, the installer what components to include. Use the -i switch followed by the name of a component. In this case, SCHEDULER. Use the small -r switch followed by the desired name of a new service. Since systemd services require a user ID on the system to execute under, we’ll include the lowercase -u switch followed by a user name. Finally, include the capital -R switch to insure the systemd service is configured by the installer. Confirm the installation details, and the installation will proceed. There is an optional lowercase -y switch that can be included in the silent install command to skip this review step.

Restart Apache. Congratulations! The Scheduler Service has been installed! Continue to the next video in this series to configure the service.
