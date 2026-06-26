---
title: "Installing Exago on Linux [NGINX]"
id: 5281571805847
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281571805847-Installing-Exago-on-Linux-NGINX
updated_at: 2022-05-03T22:08:31Z
---

# Installing Exago on Linux [NGINX]

# Installing Exago on Linux [NGINX]

This video explains how to install Exago BI’s Web Application on a Linux server with NGINX.

[<< Introduction to Technical Training Series](https://devnet.logianalytics.com/hc/en-us/articles/5281571861783-Introduction-to-Technical-Training-Series) Previous Video

Next Video [Installing REST [Linux] >>](https://devnet.logianalytics.com/hc/en-us/articles/5281540942103-Installing-REST-Linux-)

## Transcript

Welcome back to the Exago Technical Training Series! In this video we will demonstrate how to install Exago on a Linux server in conjunction with NGINX. Either Apache of NGINX must be installed prior to installing Exago. If both already exist on the server, the installer will prompt for which to use.

The first step is to download the application installer. For information on accessing the installer, see the Introduction video of this series.

Once the installer has downloaded, decompress the installer using tar and zxvf options. This will create an Installer directory with all of the required installation files. This installer contains all three Exago BI components: the Web Application, the REST Web Service API and the Scheduler Service. We will only install the first component in this video: the Exago Web Application. The installer can be run in guided mode with prompts for each option or silent mode where options are set with command line switches and the installer runs on its own from there. In this video we’ll demonstrate the silent installation mode since it’s more commonly used.

Silent installation uses command line switches to specify what the installer should do. First, change to the installer directory. Then, call the installer as root. Today, our full command will look like this. Let’s break it down. The -d switch tells the installer the directory in which to install Exago. Consider versioning or using environment specific nomenclature to keep track of different installs. The Exago installer can also install the Mono framework which is necessary to run Exago on Linux. Use the lowercase -m switch followed by the keyword true to install Mono. Exago is compatible with only certain Mono versions, so it’s a good idea to allow the installer to install the appropriate version. Next, the installer needs to know what components to include. Use the lowercase -i switch followed by the name of a component to install: WEBAPP in this case to choose only the Web Application. The lowercase -a switch is used to specify the Web Application’s URL alias, if different from the default. Confirm the installation details and the installation will proceed. There is an optional lowercase -y switch that can be included on the command line to skip this confirmation step.

Once the Exago installer finishes, there is some NGINX configuration to do. During installation, the Exago installer places a site configuration into NGINX’s available sites directory. This site configuration file must exist in NGINX’s enabled sites directory. In this Ubuntu demonstration environment, we can create a link to it with this command. These paths may vary with operating systems. Finally, restart NGINX.

And then to test that the Exago installation was successful, open a browser and navigate to the URL comprised of the server IP slash Exago web alias slash Admin.aspx. In our case, that looks like this.

Congratulations! Exago is successfully up and running!
