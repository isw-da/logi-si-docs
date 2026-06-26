---
title: "Installing Exago on Linux [Apache]"
id: 5281555053207
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281555053207-Installing-Exago-on-Linux-Apache
updated_at: 2022-05-03T22:08:30Z
---

# Installing Exago on Linux [Apache]

# Installing Exago on Linux [Apache]

This video explains how to install Exago BI’s Web Application on a Linux server with Apache.

[<< Introduction to Technical Training Series](https://devnet.logianalytics.com/hc/en-us/articles/5281571861783-Introduction-to-Technical-Training-Series) Previous Video

Next Video [Installing REST [Linux] >>](https://devnet.logianalytics.com/hc/en-us/articles/5281540942103-Installing-REST-Linux-)

## Transcript

Welcome back to the Exago Technical Training Series! In this video we will demonstration how to install Exago on a Linux server in conjunction with Apache. Either Apache or NGINX must be installed prior to installing Exago. If both already exist on the server, the installer will prompt for which to use.

The first step is to download the application installer. For information on accessing the installer, see the Introduction video of this series.

Once the installer has downloaded, decompress it using tar and zxvf options. This will create an Installer directory with all of the required installation files. This installer contains all three Exago BI components: the Web Application, the REST Web Service API and the Scheduler Service. The installation menu includes three downloadable applications. We will install only the first component today: the Exago Web Application. The installer can be run in guided mode with prompts for each option, or silent mode where options are set with command line switches and the installer runs on its own from there. In this video, we’ll demonstrate the silent installation mode since it’s more commonly used.

First, change the Installer directory. Then, call the installer as root. Today, our full command will look like this. Let’s break it down. The -D switch tells the installer the directory in which to install Exago. Consider versioning or using environment specific nomenclature to keep track of different installs. The Exago installer can also install the Mono framework which is necessary to run Exago on Linux. The lower case -m switch followed by the keyword true tells the installer to install Mono along with Exago. Exago is compatible with only certain Mono versions, so it’s a good idea to allow the installer to install the appropriate version. Next, the installer needs to know what components to use. Use the -i switch followed by the name of a component to install. Specify the web application’s URL alias with the lowercase -a switch. Confirm the installation details, and the installation will proceed. There’s an optional lowercase -y switch that can be included on the command line to skip this confirmation step.

The installer will also generate an Apache configuration file named exago.conf in the Apache site path, and set read-write permissions for the current Apache user on the install path. Once the installer is complete, restart Apache. Open a browser and navigate to the URL server IP slash Exago web alias slash Admin.aspx. In our case, this looks like this.

Congratulations! Exago is successfully up and running!
