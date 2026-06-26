---
title: "Installing Exago BI on Windows"
id: 5281533204119
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281533204119-Installing-Exago-BI-on-Windows
updated_at: 2022-05-03T22:08:30Z
---

# Installing Exago BI on Windows

# Installing Exago BI on Windows

This video explains how to install Exago BI’s Web Application on a Windows server.

[<< Configuring IIS](https://devnet.logianalytics.com/hc/en-us/articles/5281532846743-Configuring-IIS) Previous Video

Next Video [Installing REST [Windows] >>](https://devnet.logianalytics.com/hc/en-us/articles/5281563077271-Installing-REST-Windows-)

## Transcript

Welcome back to the Exago Technical Training Series!  In this video, we’ll demonstrate how to install Exago on a Windows server. The first step is to download the application installer. For information on accessing the installer, see the Introduction video of this series.

Run the installer as Administrator. If Windows Defender prevents this process, it can be bypassed by clicking More Info… and then Run Anyway. The installer contains all three Exago BI components: the Web Application, the REST Web Service API and the Scheduler Service. We will install only the main component, the Exago Web Application.

At this point, we can follow the steps in the wizard to install Exago. To choose the installation location, specify the virtual directory as well as the physical location for the install. Consider versioning or using environment specific nomenclature to keep track of different installs. In this example, since we’re installing version 2021.1, the virtual and physical directory names the version number.

Click Next. Confirm the website, virtual directory and physical directory are correct, then click Next to begin the installation.

Click the X to close the Exago installer. Once installed, we need to insure Exago is using a valid application pool. Open your IIS Manager and select the Exago application. Verify the application pool running Exago has the properties .NET v4.5 and pipeline mode integrated.  Insure the app pool is running.

The last step is to set permissions for some of the directories for the application pool user. The following folders in the Exago install require IIS\_IUSRS to have read and write permissions: Config, Temp, Drivers, MapCache and ApplicationThemes. We will begin with the Config folder. To set these permissions, open the Security properties for the folder and add the user IIS\_IUSRS if it does not exist already. Finally, give the user Full Control. Repeat this process for the Temp, MapCache, Drivers and ApplicationThemes directories.

Before starting Exago, insure the web site and web server under which Exago was installed are running. Finally, browse to the page admin.aspx included in the Exago installation contents. Congratulations! Exago is successfully up and running!
