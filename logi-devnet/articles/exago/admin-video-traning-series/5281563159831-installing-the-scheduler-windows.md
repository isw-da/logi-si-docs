---
title: "Installing the Scheduler [Windows]"
id: 5281563159831
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281563159831-Installing-the-Scheduler-Windows
updated_at: 2022-05-03T22:08:30Z
---

# Installing the Scheduler [Windows]

# Installing the Scheduler [Windows]

This video explains how to install Exago BI’s Scheduler Service on a Windows server.

[<< Configuring the REST Web Service [Windows]](https://devnet.logianalytics.com/hc/en-us/articles/5281540715927-Configuring-the-REST-Web-Service-Windows-) Previous Video

Next Video [Configuring the Scheduler [Windows] >>](https://devnet.logianalytics.com/hc/en-us/articles/5281562919447-Configuring-the-Scheduler-Windows-)

## Transcript

Welcome back to the Exago Technical Training Series! In this video, we’ll demonstrate how to install the Exago Scheduler Service on a Windows server.

Before we begin, a note about operating systems and version numbers. Although they do not need to reside on the same server, Scheduler Services installed on Windows are only compatible with Web Applications installed on Windows. Likewise, Linux Scheduler Services are only compatible with Web Applications on Linux. Additionally, the version number of the Scheduler Service and the Web Application must always match. Therefore, if the Scheduler Service is deployed, it must be updated at the same time and with same installer application that the Web Application is to insure that the version numbers are always the same.

The first step is to download the application installer. For information on accessing the installer, see the Introduction video of this series. This installer contains all three Exago BI Components: the Web Application, the REST Web Service API and the Scheduler Service. Click the bottom button to install the Exago Scheduler Service. At this point, we can follow the steps in the wizard to install the Scheduler. The Service Name is the name of the Windows Service Exago will install, and how it appears in the Services Control Panel. Choose the installation location, consider versioning or using environment specific nomenclature that matches your Web App installs to keep track of different versions. Select if the service will be available all user accounts on this server, or just the currently logged in user account, then click Next. Click Next again, confirm the details are correct then click Next again to begin the installation.

At this point, the Scheduler Service has been installed. Continue to the next video in this series to configure the service.
