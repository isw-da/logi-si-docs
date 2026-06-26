---
title: "Installing REST [Linux]"
id: 5281540942103
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281540942103-Installing-REST-Linux
updated_at: 2022-05-03T22:08:31Z
---

# Installing REST [Linux]

# Installing REST [Linux]

This video explains how to install Exago BI’s Web Service API on a Linux server with Apache

* [<< Installing Exago on Linux [Apache]](https://devnet.logianalytics.com/hc/en-us/articles/5281555053207-Installing-Exago-on-Linux-Apache-) Previous Video
* [<< Installing Exago on Linux [NGINX]](https://devnet.logianalytics.com/hc/en-us/articles/5281571805847-Installing-Exago-on-Linux-NGINX-) Previous Video

Next Video [Configuring the REST Web Service [Linux] >>](https://devnet.logianalytics.com/hc/en-us/articles/5281562765719-Configuring-the-REST-Web-Service-Linux-)

## Transcript

Welcome back to the Exago Technical Training Series! In this video, we’ll demonstrate how to install and configure the REST Web Service API on a Linux server with Apache installed.

Installing the Web Service API on Linux is the same process as installing the Web Application. Review either Installing Exago on Linux with Apache or Installing Exago on Linux with NGINX for full details. The first step is download the application installer. For information on accessing the installer, see the Introduction video of this series. The only difference is that the installer’s silent mode command line, supply the -i switch with the WEBAPI keyword. In practice, the command line supports multiple -i commands, such as -i WEBAPP -i WEBAPI to install multiple components in one call.

Now that the Web Service API has been installed on the server, restart the web server and then proceed to the next video for configuration.
