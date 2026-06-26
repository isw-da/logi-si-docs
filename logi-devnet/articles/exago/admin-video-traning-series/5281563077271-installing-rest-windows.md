---
title: "Installing REST [Windows]"
id: 5281563077271
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281563077271-Installing-REST-Windows
updated_at: 2022-05-03T22:08:32Z
---

# Installing REST [Windows]

# Installing REST [Windows]

This video explains how to install Exago BI’s Web Service API on a Windows server.

[<< Installing Exago on Windows](https://devnet.logianalytics.com/hc/en-us/articles/5281533204119-Installing-Exago-BI-on-Windows) Previous Video

Next Video [Configuring the REST Web Service [Windows] >>](https://devnet.logianalytics.com/hc/en-us/articles/5281540715927-Configuring-the-REST-Web-Service-Windows-)

## Transcript

Welcome back to the Exago Technical Training Series! In this video we’ll demonstrate how to install the REST Web Service API on Windows.

The first step is to download the application installer. For information on accessing the installer, see the Introduction video of this series.

Once the installer has downloaded, run it as Administrator. This installer contains all three Exago BI components: the Web Application, the REST Web Service API, and the Scheduler Service. Click the middle button to install the Web Service API. Choose the installation location. Specify the virtual directory for the web service as well as the physical location for the install. Consider versioning or using environment specific nomenclature that is similar to the Web Application’s install to keep track of different versions. Note that these paths must be different than the paths used for the Web Application installation. In this example, since we’re installing version 2021.1, the virtual and physical directory names include the version number.

Click Next. Confirm that the web site, virtual directory and physical directory are correct, then click Next again to begin the installation.

Now that the Web Service API has been installed on the server, restart the web server and then proceed to the next video for configuration.
