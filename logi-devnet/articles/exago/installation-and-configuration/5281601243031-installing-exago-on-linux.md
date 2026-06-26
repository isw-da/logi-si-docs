---
title: "Installing Exago on Linux"
id: 5281601243031
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281601243031-Installing-Exago-on-Linux
updated_at: 2023-04-03T17:52:19Z
---

# Installing Exago on Linux

# Installing Exago on Linux

The following topic walks through the installation process for Linux systems. Before beginning installation, refer to the [Technical Specifications](https://devnet.logianalytics.com/hc/en-us/articles/5281616408727-Technical-Specifications) topic for a list of supported distributions and a list of minimum requirements.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> The Linux Installer was updated in *v2019.2.1* of the application. This topic covers several versions of the installer. Use the **Viewing content for dropdown** to see only the content relevant to a specific application version. Any previous headless install scripts will start prompting for missing formation and will require editing to account for the new parameters.

This topic is divided into three sections: Apache, NGINX and Common Install Information. Only follow the instructions in the section that corresponds with the web server in the environment, and review Common Install Information for all installations.

[Apache](#Installa2)

[NGINX](#Installa)

## Installation with Apache

Apache must be installed prior to installing Exago.

The Exago Linux Installer can be used to install the Exago Web Application, Web Service API, and Scheduler Service. It can also install mono and mod-mono. Use the following steps to install Exago on Linux with Apache.

---

This accompanying video is from the Technical Training Series. To see the other videos in this series, start with the [Introduction to Technical Training Series](https://devnet.logianalytics.com/hc/en-us/articles/5281571861783-Introduction-to-Technical-Training-Series).

---

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Apache or NGINX must be installed prior to installing Exago. If changing from one or the other, verify the dependencies (mod-mono or mono-fastcgi-server4) are installed.

1. Navigate to the **Downloads** page, select a build, and then use the Linux Download option.
2. Decompress the download:

   ```
   tar zxvf ExagoInstaller_vX.X.X.X.tgz
   ```
3. Change to the newly created `Installer` directory:

   ```
   cd Installer
   ```
4. Run `installExago.sh` as root:

   ```
   sudo ./installExago.sh
   ```
5. The installer can be run in [guided](#Guided) or [silent](#Silent) mode. The Linux distribution and Apache version will be detected automatically.

### Silent Installation with Parameters

Usage:

```
[-d <install path>] [-m <TRUE|FALSE>] [-i <WEBAPP|WEBAPI|SCHEDULER>] [-y] [-h]
```

| Parameter | Description |
| --- | --- |
| -d <Install Path> | Directory to install Exago in Default is `/opt/Exago` |
| -m <TRUE|FALSE> | Whether or not to install Mono framework with Exago |
| -i <WEBAPP|WEBAPI|SCHEDULER> | Which component(s) to install   * *WEBAPP* — Web Application * *WEBAPI* — REST Web Service API * *SCHEDULER* — Scheduler Service |
| -a <Web App URL Alias> | Default is `/Exago` |
| -s <Web Service URL Alias> | Default is `/ExagoWebApi` |
| -r <Scheduler Service Name> | Name to use for the Scheduler Service’s systemd service. Default is *exago-scheduler*. |
| -R | Configure systemd services As of *v2019.2.1*, Exago will automatically install systemd services unless the -N flag is passed to inhibit their installation. This option is not available in Exago versions *pre-v2019.2.1*. |
| -N | As of *v2019.2.1*, do NOT configure systemd services This option is not available in Exago versions *pre-v2019.2.1*. |
| -u <userId> | As of *v2019.2.1*, user ID to create in the operating system that the Exago systemd services and FastCGI listeners will run under.  A group and home directory with the same name will be created.  This option is not available in Exago versions *pre-v2019.2.1*. |
| -w <APACHE|NGINX> | Available in *v2019.1.15+* Select the web server to configure, if both are available. |
| -D | As of *v2019.2.1*, select all default values for installation options. Individual options can be overridden by including the parameter on the command line.  This option is not available in Exago versions *pre-v2019.2.1*.  See [Default Values](#Default) below for further details |
| -y | Do not prompt for final verification before installing |
| -h | Show this help screen |

##### Examples:

1. Install the Exago Web Application and Web Service API into /opt/Exago

   ```
   ./installExago.sh -d /opt/Exago -m TRUE -i WEBAPP -i WEBAPI
   ```
2. Full installation using all default values without prompting before starting the install

   ```
   ./installExago.sh -D -y
   ```
3. Install the Scheduler Service only into /opt/ExagoRemote using defaults for everything else

   ```
   ./installExago.sh -d /opt/ExagoRemote -i SCHEDULER -D
   ```

### Guided Installation v2019.2.1+

```
##############################################
   ___  __  __   __ _    __ _    ___  
  / _   / /  / _` |  / _` |  / _  
 |  __/  >  <  | (_| | | (_| | | (_) |
  ___| /_/_  __,_|  __, |  ___/ 
                         __/ |        
        Linux Installer |___/         
##############################################
```

The Linux Installer will ask a series of questions to setup the environment. Suggested default values for each question are enclosed in [ brackets ]. To choose the default value, simply press the Enter key on the keyboard.[Default Values](#Default) are explained in their own section below.

1. Select base install path. Default value is `/opt/Exago`.
2. Would you like to install the Mono runtime if not already installed? Default is *yes*.
3. Would you like to install the Exago Web App? Default is *yes*.
4. Would you like to install the Exago Web Service API? Default is *no*.
5. Would you like to install the Exago Scheduling and Remote Execution Service? Default is *no*.
6. Multiple web servers appear to be present. Please choose which web server you would like to use. This question will only appear if both Apache and NGINX are installed on the web server. You must choose 1 for Apache or 2 for NGINX.
7. Enter a name for the Exago Scheduling Service. Default is *exago-scheduler*.
8. Select WebServer Alias for Exago Web App. Default is `/Exago`
9. Select WebServer Alias for Exago WebService API. Default is `/ExagoWebApi`
10. Should systemd services be configured? Default is *yes*.
11. Please enter a userId to configure for use with Exago. This user account is used to run the Exago services under (Scheduler Service and Monitoring Service). Default is *exago*.
12. A summary of installation parameters will appear and you will be asked if ready to install.

Continue to [Start and Test Install](#Start).

### Guided Installation pre-v2019.2.1

Specify an install path when prompted. Default is `/opt/Exago`.

If the proper versions of mono (and mod-mono) are not present in the distribution’s package repository then the Exago installer can be used to download and install the correct versions. If so, the mono repositories will be added to the package manager’s repository list so that they can be updated in the future.

Select which components to install:

1. Web Application
2. Web Service API
3. Scheduler Service

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> It is possible to install any components at a later time by running `installExago.sh` again.

The installer will additionally do the following:

* Download and install mod-mono, if it is not already present.
* Generate an Apache configuration file `exago.conf` in the Apache site path.
* Set read/write permissions for the current Apache user on the install path.

### Start and Test Install

Restart Apache.

Point a browser to the **Admin Console** to verify that the installation was successful and to create a default configuration file. By default this is `http://<YourServer>/Exago/Admin.aspx`

If you need more information, contact [Exago Support](https://help.insightsoftware.com/s/contactsupport?language=en_US "Exago support").

[Folder Configuration](#Folder)

### Folder Configuration

Configure storage locations for the **configuration**, **report storage** (either *Storage Management* for v2020.1.0+ or a Report Path *pre-v2020.1.0*) and **temporary file storage.**

#### Config

The **Config** sub-folder of the Exago installation has read and write permissions set by default.

#### Report Storage

For versions *v2020.1+*, setup the **Storage Management** system for storing reports, templates and themes.

#### Upgrade Install

If upgrading from a previous version of Exago, review these topics:

* [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction)
* [Storage Management: Getting Started](https://devnet.logianalytics.com/hc/en-us/articles/5281653081111-Storage-Management-Getting-Started)
* [Moving Files Between Storage Management Databases](https://devnet.logianalytics.com/hc/en-us/articles/5281638646807-Moving-Files-Between-Storage-Management-Databases)
* [Storage Management: Transitioning from Legacy Storage Methods](https://devnet.logianalytics.com/hc/en-us/articles/5281647090839-Storage-Management-Transitioning-from-Legacy-Storage-Methods)

#### New Install

If this is a new installation, review these topics:

* [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction)
* [Storage Management: Getting Started](https://devnet.logianalytics.com/hc/en-us/articles/5281653081111-Storage-Management-Getting-Started)
* [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management)
* [Storage Management: Custom Implementation](https://devnet.logianalytics.com/hc/en-us/articles/5281646850327-Storage-Management-Custom-Implementation)

Setting up the **Storage Management** system in general is as follows:

1. Create and setup the Storage Management database. This can be accomplished using either one of the following methods:
   * *Recommended*: use the **Admin Console** to initialize the database
   * Manually creating database and the tables based on the [Storage Management: Database Schema](https://devnet.logianalytics.com/hc/en-us/articles/5281630919319-Storage-Management-Database-Schema)
2. Configure Exago to connect to the Storage Management database

**For versions *pre-v2020.1*:**

Create a folder for storing reports. This folder needs to be accessible from the web server, but is not required to be on the web server. The report folder can reside on any server accessible by Exago, provided a mount point is accessible on the Exago server.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Do not create the reports folder within the Exago application structure. This can cause sessions to crash when report folders are created or deleted within Exago.

1. Set the **Report** folder’s read and write permissions to **770**.

   ```
   sudo chmod 770 Reports
   ```
2. Set the default ownership to the specific **<apache user>:<apache group>**
3. In the **Admin Console**, specify the location of the report folder in **General** > **Main Settings** > **Report Path**

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The group ownership on the reports directory is not mandatory, and can be changed to have other group ownership as needed for access outside of Exago.

Default UMASK for files written by Exago is 027 and can be changed by updating the MonoUnixUmask option in the generated `exago.conf` Apache configuration file.

#### Temporary File Storage

The recommended path for the **Temp** folder is `/opt/Exago/Temp`.

1. Set the **Temp** folder’s read and write permissions to **775**.

   ```
   sudo chmod 775 /opt/Exago/Temp
   ```
2. Set the default ownership to **<apache user>:**root
3. In the **Admin Console**, specify the location of the temp Folder in **General** > **Main Settings** > **Temp Path**
4. Set the **MonitoringService** folder’s read and write permissions for the Apache user, (of if not using the default Apache user the user ID specified with -u) to **775**, and set the default ownership to **<apache user>**:**root**.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> If using a custom Application Theme, the **ApplicationThemes** folder will also need the same permissions.

Installation is now completed. If the Scheduler Service or Monitoring Service is required, continue to the [Scheduler and Monitoring Services](#Schedule) section at the end of this topic.

If all components are installed, the `Installer` directory may be deleted.

## Installation with NGINX

NGINX must be installed prior to installing Exago. NGINX proxies incoming and outgoing requests to a running instance of Exago using a fastcgi module that is installed during the installation process. **mono-fastcgi-server4** is a prerequisite for Exago to run on NGINX.

The Exago Linux Installer can be used to install the Exago Web Application, Web Service API, and Scheduler Service. It can also install mono and mono-fastcgi-server4. Use the following steps to install Exago on Linux with NGINX.

---

This accompanying video is from the Technical Training Series. To see the other videos in this series, start with the [Introduction to Technical Training Series](https://devnet.logianalytics.com/hc/en-us/articles/5281571861783-Introduction-to-Technical-Training-Series).

---

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Apache or NGINX must be installed prior to installing Exago. If changing from one or the other, verify the dependencies (mod-mono or mono-fastcgi-server4) are installed.

1. Navigate to the [Downloads](https://support.exagoinc.com/hc/en-us/categories/202053837) page, select a build, and then use the Linux Download option.
2. Decompress the download:

   ```
   tar zxvf ExagoInstaller_vX.X.X.X.tgz
   ```
3. Change to the newly created `Installer` directory:

   ```
   cd Installer
   ```
4. Run `installExago.sh` as root:

   ```
   sudo ./installExago.sh
   ```
5. The installer can be run in [guided](#Guided2) or [silent](#Silent) mode. The Linux distribution will be detected automatically.

### Silent Installation with Parameters

Usage:

```
[-d <install path>] [-m <TRUE|FALSE>] [-i <WEBAPP|WEBAPI|SCHEDULER>] [-y] [-h]
```

| Parameter | Description |
| --- | --- |
| -d <Install Path> | Directory to install Exago in Default is `/opt/Exago` |
| -m <TRUE|FALSE> | Whether or not to install Mono framework in Exago |
| -i <WEBAPP|WEBAPI|SCHEDULER> | Which component(s) to install  * *WEBAPP* — Web Application * *WEBAPI* — REST Web Service API * *SCHEDULER* — Scheduler Service |
| -a <Web App URL Alias> | Default is `/Exago` |
| -s <Web Service URL Alias> | Default is `/ExagoWebApi` |
| -r <Scheduler Service Name> | Name to use for the Scheduler Service’s systemd service. Default is *exago-scheduler*. |
| -f <Fastcgi Service Name> | As of *v2019.2.1*, name to use for the FastCGI services used by NGINX. This option is not available in Exago versions *pre-v2019.2.1*. |
| -p WEBAPP:<port>|WEBAPI:<port> | As of *v2019.2.1*, port numbers to use for the FastCGI listeners for the Web Application or Web Service API, respectively. This option is not available in Exago versions *pre-v2019.2.1*. |
| -R | Configure systemd services As of *v2019.2.1*, Exago will automatically install systemd services unless the -N flag is passed to inhibit their installation. This option is not available in Exago versions *pre-v2019.2.1*. |
| -N | As of *v2019.2.1,* do NOT configure systemd services This option is not available in Exago versions *pre-v2019.2.1*. |
| -u <UserID> | As of *v2019.2.21,* User ID to create in the operating system that the Exago systemd services and FastCGI listeners will run under. A group and home directory with the same name will be created.  This option is not available in Exago versions *pre-v2019.2.1*. |
| -w <APACHE|NGINX> | Available in *v2019.1.15+* Select the web server to configure, if both are available. |
| -D | As of *v2019.2.1*, select all default values for installation options. Individual options can be overridden by including the parameter on the command line. See [Default Values](#Default) below for further details  This option is not available in Exago versions *pre-v2019.2.1*. |
| -y | Do not prompt for final verification before installing |
| -h | Show this help screen |

Examples:

1. Install the Exago Web Application and Web Service API into /opt/Exago

   ```
   ./installExago.sh -d /opt/Exago -m TRUE -i WEBAPP -i WEBAPI
   ```
2. Full installation using all default values without prompting before starting the install

   ```
   ./installExago.sh -D -y
   ```
3. Install the Scheduler Service only into /opt/ExagoRemote using defaults for everything else

   ```
   ./installExago.sh -d /opt/ExagoRemote -i SCHEDULER -D
   ```

### Guided Installation v2019.2.1+

```
##############################################
   ___  __  __   __ _    __ _    ___  
  / _   / /  / _` |  / _` |  / _  
 |  __/  >  <  | (_| | | (_| | | (_) |
  ___| /_/_  __,_|  __, |  ___/ 
                         __/ |        
        Linux Installer |___/         
##############################################
```

The Linux Installer will ask a series of questions to setup the environment. Suggested default values for each question are enclosed in [ brackets ]. To choose the default value, simply press the Enter key on the keyboard. [Default values are explained in their own section below](#Default).

1. Select base install path. Default value is `/opt/Exago`.
2. Would you like to install the Mono runtime if not already installed? Default is *yes*.
3. Would you like to install the Exago Web App? Default is *yes*.
4. Would you like to install the Exago Web Service API? Default is *no*.
5. Would you like to install the Exago Scheduling and Remote Execution Service? Default is *no*.
6. Multiple web servers appear to be present. Please choose which web server you would like to use. This question will only appear if both Apache and NGINX are installed on the web server. You must choose 1 for Apache or 2 for NGINX.
7. Enter a name for the Exago Scheduling Service. Default is *exago-scheduler*.
8. Select WebServer Alias for Exago Web App. Default is `/Exago`
9. Select WebServer Alias for Exago WebService API. Default is `/ExagoWebApi`
10. Enter the base fastcgi service name. Default is *exago-fcgi*
11. Enter the port for the web app fastcgi listener. Default is *9000*
12. Enter the port for the web service fastcgi listener. Default is *9001*.
13. Should systemd services be configured? Default is *yes*.
14. Please enter a userId to configure for use with Exago. This user account is used to run the Exago services under (Scheduler Service and Monitoring Service). Default is *exago*.
15. A summary of installation parameters will appear and you will be asked if ready to install.

Continue to [Start and Test Install](#Start) below.

### Guided Installation pre-v2019.2.1

Specify an install path when prompted. Default is `/opt/Exago`.

If the proper versions of mono (and mono-fastcgi-server4) are not present in your distribution’s package repository then the Exago installer can be used to download and install the correct versions. If so, the mono repositories will be added to the package manager’s repository list so that they can be updated in the future.

Select which components to install:

1. Web Application
2. Web Service API
3. Scheduler Service

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> It is possible to install any components at a later time by running `installExago.sh` again.

### Start and Test Install

#### Configure NGINX

The required configuration is created in a separate site file located in the NGINX configuration directory.

For Ubuntu systems this is typically `/etc/nginx/sites-available/exago`. For other systems this may be `/etc/nginx/conf.d/exago`. The exact location of the file will depend on your system and NGINX installation. Consult with the operating system and NGINX official product documentation for more information.

The site file is not enabled by default.

#### Example

```
#Exago conf file for fastcgi-mono-server4
server {
	listen 80;
	listen [::]:80;
	server_name _;
	root /var/www;

  location /Exago/ {
  	include /etc/nginx/fastcgi_params;
  	root /opt/Exago;
  	access_log /var/log/nginx/exago.log;
  	fastcgi_param SERVER_NAME $host;
  	fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
  	fastcgi_param PATH_INFO "";
  	fastcgi_pass 127.0.0.1:9000;
  }

  location /ExagoWebApi/ {
          include /etc/nginx/fastcgi_params;
          root /opt/Exago/WebServiceApi;
          access_log /var/log/nginx/exago_ws.log;
          fastcgi_param SERVER_NAME $host;
          fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
          fastcgi_param PATH_INFO "";
          fastcgi_pass 127.0.0.1:9001;
  }
}
```

For example on Ubuntu, to enable the site file, link it to `/etc/nginx/sites-enabled`:

```
sudo ln /etc/nginx/sites-available/exago /etc/nginx/sites-enabled/exago
```

Or include the configuration in another running site configuration file. This step will depend on your specific environment. Consult the operating system and NGINX official documentation.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
>
> Make sure that the default port does not conflict with another running site. If it does, you will see a warning when reloading NGINX: `nginx: [warn] conflicting server name "Exago" on 0.0.0.0:80`

Then reload NGINX to refresh the configuration:

```
sudo nginx -s reload
```

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic references `<WebApp>/`,
> `<WebSvc>/` and `<Sched>/`as a placeholder
> for the Web Application, Web Service API and Scheduler Service's install
> location respectively. The default install location is
> `C:\Program Files\Exago\ExagoWeb\` (`/opt/Exago/` on Linux),
> `C:\Program Files\Exago\ExagoWebApi\` ( `/opt/Exago/WebServiceApi/` on Linux) or
> `C:\Program Files\Exago\ExagoScheduler\` (`/opt/Exago/Scheduler/` on Linux); however, these directories
> can be changed during installation.

#### Start Listeners

The installer will create two new scripts which can be used either standalone or along with a service manager such as **systemd**.
> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The **exago-fcgi** portion of each service name can be configured from the defaults below with the -f parameter in silent installation or by providing an answer to the **Enter the base fastcgi service name** question during guided installation.

* `<WebApp>/exago-fcgi-webapp.sh`
* `<WebSvc>/exago-fcgi-webservice.sh`

When not using a service manager, each of these scripts can be run with either the **start**, **stop** and **restart** directives. For example, `<WebApp>/bin/exago-fcgi-webapp.sh start` will start the Web Application’s FastCGI listener. `<WebSvc>/bin/exago-fcgi-webservice.sh restart` will restart the Web Service API’s FastCGI listener.

When using systemd, the commands take the following form:

* `service exago-fcgi-webapp start`
* `service exago-fcgi-webservice stop`

**For versions *pre-v2020.1*:**

This script created during installation needs to be started manually or configured to run at startup:

```
<WebApp>/bin/startExago.sh
```

If the Web Service API was installed, this script created during installation needs to be started manually or configured to run at startup:

```
<WebSvc>/bin/startWebService.sh
```

Point a browser to the **Admin Console** to verify that the installation was successful and to generate a default configuration file. By default this is `http://<YourServer>/Exago/Admin.aspx`

If you need more information, contact [Exago Support](https://help.insightsoftware.com/s/contactsupport?language=en_US "Exago support").

Continue to [Content Storage Configuration](#Content) below to continue with the installation.

### Content Storage Configuration

The **Config** sub-folder of the Exago installation has read and write permissions set by default.

For versions *v2020.1+*, setup the **Storage Management** system for storing reports, templates and themes.

#### Upgrade Install

If upgrading from a previous version of Exago, review these topics:

* [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction)
* [Storage Management: Transitioning from Legacy Storage Methods](https://devnet.logianalytics.com/hc/en-us/articles/5281647090839-Storage-Management-Transitioning-from-Legacy-Storage-Methods)
* [Storage Management: Getting Started](https://devnet.logianalytics.com/hc/en-us/articles/5281653081111-Storage-Management-Getting-Started)

#### New Install

If this is a new installation, review these topics:

* [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction)
* [Storage Management: Getting Started](https://devnet.logianalytics.com/hc/en-us/articles/5281653081111-Storage-Management-Getting-Started)
* [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management)

**For versions *pre-v2019.2*:**

Create a folder for storing reports. This folder needs to be accessible from the web server, but is not required to be on the web server. The report folder can reside on any server accessible by Exago, provided a mount point is accessible on the Exago server.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Do not create the reports folder within the Exago application structure. This can cause sessions to crash when report folders are created or deleted within Exago.

1. Set the **Report** folder’s read and write permissions to **770**:

   ```
   sudo chmod 770 Reports
   ```
2. In the **Admin Console**, specify the location of the report storage folder in **General** > **Main Settings** > **Report Path**

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The group ownership on the reports directory is not mandatory, and can be changed to have other group ownership as needed for access outside of Exago.

Default UMASK for files written by Exago is 027.

The recommended path for the **Temp** folder is `/opt/Exago/Temp`.

1. Set the **Temp** folder’s read and write permissions to **775**:

   ```
   sudo chmod 775 /opt/Exago/Temp
   ```
2. In the **Admin Console**, specify the location of the temp Folder in **General** > **Main Settings** > **Temp Path**

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> If using a custom Application Theme, the **ApplicationThemes** folder will also need the same permissions.

Installation of Exago is now completed. If the Scheduler Service or Monitoring Service is required, continue to the [Scheduler and Monitoring Services](#Schedule) section at the end of this topic.

If all components are installed, the `Installer` directory may be deleted.

## Common Install Information

## Scheduler and Monitoring Services

### Scheduler Service

A script named `exago-scheduler.sh` by default is used to manage the Scheduler Service. The name is customizable with the installer’s `-r` parameter.

#### Installed as a systemd Service

When utilizing a systemd service, the Scheduler Service should start automatically when the system boots, and can be managed with the service command in the following ways:

* `service exago-scheduler start`
* `service exago-scheduler stop`
* `service exago-scheduler status`

When a second scheduler is installed on the same server, the default service name will increment: `exago-scheduler2`, `exago-scheduler3`, and so on.

#### Not Installed as a systemd Service

When the Scheduler Service is not installed as a systemd service (without the `-R` parameter), it is not possible to know if another service with the same name exists on the same server. When a service with the same name is installed, only one can be used at a time. This is due to the fact that lock files used by the service are based on the service’s name, and will prevent the second process from starting. In this scenario, the `-r` flag should be used and additional schedulers be given different names.

To start the Scheduler Service, execute the `exago-scheduler.sh` script as the owner of the installation directory (either **root***pre-v2019.2.21* or the user name specified with the `-u` parameter, **exago** by default in *v2019.2.21+*). For example:

In *v2019.2.21+*, assuming the Scheduler Service is installed in `/opt/Exago/Scheduler/`:

```
su exago
/opt/Exago/Scheduler/exago-scheduler.sh start
exit
```

In *pre-v2019.2.21*, assuming the Scheduler Service is installed in `/opt/Exago/Scheduler/`:

```
su root
/opt/Exago/Scheduler/exago-scheduler.sh start
exit
```

If necessary, configure the Scheduler and Monitoring services to run at startup.

### Start Monitoring Service

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic references `<WebApp>/` as a placeholder for the application’s install location. The default install location is `/opt/Exago/`; however, this directory may be changed during installation.

If the Web Application was installed, the Monitoring Service is also installed, but is disabled by default. This script created during installation needs to be started manually or configured to run at startup:

```
<WebApp>/MonitoringService/startService.sh
```

## Default Values

The `-D` parameter was added to the Linux installer in *v2019.2.1*. This parameter will select the default values for each parameter unless already specified on the command line. These values are:

* defined in the **exagoinstall.properties** file in the Exago installation directory if Exago has already been installed, or
* if Exago has never been installed or is being installed in a new directory for the first time, defined below:
  + **Exago Installation Path**: `/opt/Exago`
  + **Components to install**: *Web Application*, *Monitoring Service*, *Web Service API*, *Scheduler Service*
  + **Install Mono runtime**: *Yes*
  + **User ID:***exago*
  + **Scheduler information**
    - **Scheduler install path**: `/opt/Exago/Scheduler`
    - **Scheduler service name**: *exago-scheduler*
    - **Scheduler user ID**: *exago*
    - **Configure systemd service**: *Yes*
  + **Web Server information**
    - **Selected Web Server**: *Apache* (will use Apache if both NGINX and Apache are available; will use NGINX if only NGINX is available)
    - **Web Application install path**: `/opt/Exago`
    - **Web App alias**: `/Exago`
    - **Web App user ID**: *exago* for NGINX. For Apache, the default is system dependent and will be read from either `apache.conf` or `httpd.conf` depending on which one is in use.
    - **(NGINX only) NGINX conf file**: `/etc/nginx/conf.d/exago.conf`
    - **(Apache only) Apache conf file**: `/etc/httpd/conf.d/exago.conf`
    - **Web Service install path**: `/opt/Exago/WebServiceApi`
    - **Web Service alias**: `/ExagoWebApi`
    - **Web Service user ID**: *apache* for Apache, *exago* for NGINX
    - **(NGINX only) Use system for service(s)**: *Yes*
    - **(NGINX only) Web App Service Name/Port**: *exago-fcgi-webapp / 9000*
    - **(NGINX only) Web API Service Name/Port**: *exago-fcgi-webservice / 9001*

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> For a completely headless installation with all of the default values, pass the `-D` and `-y` parameters. `-D` will not start the installation on it’s own, only select the default values for each parameter.

Once Exago is installed, the settings chosen during installation become the defaults and are written in to the aforementioned **exagoinstall.properties** file in the Exago installation directory.

## Upgrading Mono v2019.2.29+v2020.1.13+v2021.1.1

The **upgradeMono** script included with the installer can be used to upgrade from one supported version of mono to another. The script will remove the installed version and then install the new version in its place, along with the apache mod\_mono module and fastcgi module as applicable.

If the system does not meet the minimum requirements for any of the components, it will upgrade only the installed components but will not install anything additional.

1. Download, uncompress the Linux installer and change to the `Installer` directory as described in steps 1–3 of Installation with Apache or Installation with NGINX above.
2. Call the script as root. The command line parameters described below are optional. If no parameters are provided, the script will prompt for answers to certain questions.

Usage:

```
sudo ./upgradeMono.sh [-f] [-s] [-y] [-a] [-h]
```

| Parameter | Description |
| --- | --- |
| -f | Force a reinstall, even if the version currently installed is at the recommended version |
| -s | Skip the reinstall if the version currently installed is already the recommended version |
| -y | Don’t prompt before starting the upgrade, silently install |
| -a | Upgrade everything despite what is currently installed |
| -h | Show command line parameter help screen |

```
***********************************
Upgrade summary:
Upgrade Mono:          TRUE
Upgrade Mod Mono:      TRUE
Upgrade Mono FastCGI:  FALSE
***********************************
Would you like to continue with this upgrade? (Y or N) [Y]
```

An example summary for a system with Apache. Pressing `Y` or `Enter` on the keyboard will start the upgrade process

## Dependencies

The Exago installer handles the installation and configuration of all of its own dependencies. Installing and configuring dependencies ahead of time is not required, and in some cases could lead to unexpected issues with the Exago deployment. This list is provided as a reference only. In most cases, Exago utilizes the most up to date versions available through the operating system’s package manager (that is apt, yum, zypper).

The Exago installer will display error messages if certain dependencies are not, cannot be or are not correctly installed.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Not all of the packages listed below are installed for every operating system and situation.

* **Installer requirements** — for downloading files, adding repositories and installing GPG keys
  + curl
  + unzip
  + wget
  + yum-utils — only required on distributions that utilize the yum package manager
* **Base .NET runtime** — requirements for all Exago components
  + mono-4.0-service
  + mono-complete
* **Datetime function support**
  + mono-vbnc — used on Ubuntu and Debian only
  + mono-basic — used on Red Hat Enterprise Linux, CentOS, Fedora and SUSE Linux Enterprise Server
* **Export support**
  + Any font package such as liberation fonts or croscore fonts (chromium installed fonts will also work)
* **Apache web server support**
  + apache2-mod\_mono (libapache2-mod-mono)
  + mono-apache-server
* **Puppeteer** — support for headless chart rendering in exported files
  + alsa-lib
  + atk
  + chromium
  + cups-libs
  + gconf2
  + gtk3
  + libasound2
  + libatk-bridge2.0-0
  + libgtk-3-0
  + libnss3
  + libx11-xcb1
  + libxcomposite
  + libxcursor
  + libxdamage
  + libxi
  + libxscrnsaver
  + libxrandr
  + libxtst6
  + libxss1
  + nss
  + pango
  + xorg-x11-fonts-75dpi
  + xorg-x11-fonts-100dpi
  + xorg-x11-fonts-cyrillic
  + xorg-x11-fonts-Type1
  + xorg-x11-fonts-misc
  + xorg-x11-utils
* **NGINX web server support**
  + mono-xsp4
  + xsp
  + mono-fastcgi-server4
