---
title: "Installation Guide"
id: 12528208069655
section: "Installation and Maintenance Guide"
category: "Izenda"
url: https://devnet.logianalytics.com/hc/en-us/articles/12528208069655-Installation-Guide
updated_at: 2023-02-23T14:36:21Z
---

# Installation Guide

# [Installation Guide](#id12)

## [Standalone Installation Options](#id13)

There are two main options when deploying a “vanilla” instnace of our standalone environment.
:   * Installing Izenda’s front end and back end as two separate sites
    * Installing Izenda’s front end and back end as virtual directories/applications under a host site

The architectural goal, pre-installation preparations, and web server setup are the same for both deployment options.

## [Architectural Goal](#id14)

![../_images/Slide1B.PNG](https://devnet.logianalytics.com/hc/article_attachments/12528163730839/slide1b.png)

## [Install Izenda Standalone on Window OS](#id15)

### [Pre-installation Preparations](#id16)

The setup of Izenda requires a download of the latest version of the stand-alone front-end and the back-end and a proper web server setup. Izenda can be installed on a local machine on a Windows machine for testing purposes and is a best practice for ensuring permissions and performance can be validated locally prior to moving toward more embedded and integrated examples, but it is not recommended for live deployments.

* Izenda installation packages, download them from the Upgrade tab in the [Customer Portal](https://app.izenda.com/).

  + An Izenda Front-end Package (Default name “App”)

    ![../_images/Izenda_App_folder.png](https://devnet.logianalytics.com/hc/article_attachments/12528163738007/izenda_app_folder_482x382.png)
  + An Izenda Back-end Package (Default name “API”)

    ![../_images/Izenda_API_folder.png](https://devnet.logianalytics.com/hc/article_attachments/12528163744663/izenda_api_folder_482x312.png)
* Server

  + Windows Server with Internet Information Services (IIS) Web Server.

Note: All of the information covered in this document can also be found in video from [here](https://www.izenda.com/7-series-installation-videos/#portal-install)

### [Runtime Installation](#id17)

Izenda depends on [ASP.NET](http://asp.net/) Core Runtime 6.0.13 runtime environment to run applications. This step is only required if you are installing **Izenda 5.0.0 and above**.

Install ASP.Net Core 6.0 runtime.

1. Download and install Hosting Bundle from Microsoft’s download page.  
![](https://devnet.logianalytics.com/hc/article_attachments/12528147739287/image-20230206-175345.png)

2. Check the version after installation by running “dotnet –info”.  
![](https://devnet.logianalytics.com/hc/article_attachments/12528147744279/image-20230215-152148.png)

### [Web Server Setup](#id18)

To ensure that Izenda works properly, your Web Server requires additional components that may not be present on your server by default. If you are installing **Izenda 4.0.0 and above**, this step is not required.

#### Add Web Server Role and .NET Framework

1. Open Server Manager.
2. Click Quick Start, then Add roles and features to open Add Roles and Features dialog box.
3. Click Next to accept default selections until Select Server Roles.
4. Tick the Web Server (IIS) check-box.
5. Click Add Features in the next dialog box.
6. Expand .NET Framework 3.5 features and tick .NET Framework 3.5 check-box.
7. Expand .NET Framework 4.5 features and tick .NET Framework 4.5 check-box.

   Note: For Windows Server 2016, also check ASP.NET 4.6 in this step and skip adding “IIS:ASP.NET 4.5” in next step.

   ![../_images/Server_Role_Web_Server_ASP.NET_4.6.png](https://devnet.logianalytics.com/hc/article_attachments/12528163755031/server_role_web_server_asp.net_4.6_524x414.png)
8. Accept other default options then click Install.

#### Install ASP.NET 4.5 Components

If you are installing **Izenda 4.0.0 and above**, this step is not required.

1. Open Microsoft Web Platform Installer’s [download page](https://www.microsoft.com/web/downloads/platform.aspx).

   > This can also be opened from IIS Manager Actions panel, “Get New Web Platform Components” link.
2. Download and run the installer.
3. Open Microsoft Web Platform Installer.
4. Click Install.

> ![../_images/IIS_ASP.NET_install.png](https://devnet.logianalytics.com/hc/article_attachments/12528147791511/iis_asp.net_install_667x455.png)

#### Install URL Rewrite Components

1. Open Microsoft Web Platform Installer’s [download page](https://www.microsoft.com/web/downloads/platform.aspx).

   > This can also be opened from IIS Manager Actions panel, “Get New Web Platform Components” link.
2. Download and run the installer.
3. Open Microsoft Web Platform Installer.
4. Click Install.

> ![../_images/IIS_URL_REWRITE_install.png](https://devnet.logianalytics.com/hc/article_attachments/12528147797399/iis_url_rewrite_install_667x456.png)

#### Application Pool Requirements

When creating your Izenda Sites please ensure you set the Managed pipeline mode to Integrated. Classic is not supported.

### [Izenda Installation As Two Separate Sites](#id19)

The most common testing scenario places the front-end and the back-end on two separate sites. Virtual Directories and Virtual Applications deployments are possible with additional configuration and are outlined in another section below.

1. Extract the Izenda Front-end and Back-end packages to 2 separate folders, preferably at C:\inetpub\wwwroot\Izenda\App and C:\inetpub\wwwroot\Izenda\API.
2. Izenda can be installed in multiple configurations: new website, new application to an existing website, or new virtual application under an existing website:

   * New website

     1. Right-click the local connection and select Add Website…
     2. Name the website IzendaApp and accept the Application pool with the same name.
     3. Click the ellipsis (…) button to select the location of the extracted Izenda Front-end package (C:\inetpub\wwwroot\Izenda\App).
     4. Skip the Connect as… and Test Settings… buttons for now, since permissions have not been set for Izenda package folders.
     5. Keep the port as 80 by default or change to any available port.
     6. Optionally enter the website address into host name box, but you will have to bind that address with the correct ip in “C:\WINDOWS\System32\drivers\etc\hosts” file.

        > e.g. with website address www.acme.com and the ip 127.0.0.1, the following line needs to be added in hosts file: `127.0.0.1    www.acme.com`
     7. Click OK to create the website.

     ![../_images/IIS_Add_Website.png](https://devnet.logianalytics.com/hc/article_attachments/12528147804567/iis_add_website_439x427.png)
3. Add new website for Back-end package:

   * Follow above steps and add another site for Izenda back-end with different port.

1. Set folder permissions

   1. Right-click the newly-created website, application or virtual application and select Edit Permissions to open the folder properties.
   2. In Security tab, click Edit to open Permissions dialog box.
   3. Click Add then enter `IUSR` then click OK (for IIS 7 and above).

      > For older IIS versions, use `NTAUTHORITY\\NETWORKSERVICE`.
   4. Back in Permissions dialog box, tick the Modify check-box for IUSR.
   5. Click OK to close all dialogs.

      ![../_images/IIS_Folder_Permissions.png](https://devnet.logianalytics.com/hc/article_attachments/12528147817367/iis_folder_permissions_239x336.png)
   6. Set similar permissions for the other package.

1. Update the Back-end API url in Front-end package:

   > Edit the file `App\izenda_config.js`, replace the default value “WebApiUrl” with the correct ip and port: `"WebApiUrl":"http://127.0.0.1:8888/api/",`

> This concludes the steps necessary to install Izenda using two separate websites. Please refer to the following guides below: - Troubleshooting & Verifying the Installation - Common Izenda Stand-alone Installation Issues - Editing the Configuration Files

### [Deploying Izenda as a Virtual Directory or Application](#id20)

> Installing Izenda as a virtual directorys will mirror the steps taken required to deploy Izenda using two separate websites but additional modifications are necessary for the front end and back end to interact correctly together.

#### Initial Set Up

* Add your Front-end package to IIS as a virtual directory. (For the purpose of this tutorial we have given it the alias of IzendaFront)
* Add your Back-end package but then convert it to an application. (For the purpose of this tutorial we have given it the alias of IzendaBack)

#### Within the UI Folder of your Deployment

1. Edit the izenda\_config.js, point the BaseURL and the WebApiUrl to the virtual directory for your front/back-end respectively

   * Target code:

     ```
     BaseUrl:"/<your Url here>/"
     												WebApiUrl:"http://<Your API URL here>/api/"
     											
     ```
   * Example change:

     ```
     BaseUrl:"/IzendaFront/"
     												WebApiUrl:"http://localhost:80/IzendaBack/api/"
     											
     ```
2. Edit the index.html file and add the URL for the Virtual Directory as below, this should follow the ending </style> tag

   * Target code:

     ```
     <script>window.IzendaPublicPath='/<your Url here>/';</script>
     ```
   * Example change:

     ```
     <script>window.IzendaPublicPath='/IzendaFront/';</script>
     ```
3. Alter the location of the files in the index.html file to point to the new location:

   * Target code:

     ```
     <linkrel="shortcut icon"href="/<your Url here>/favicon.png"><linkhref="/<your Url here>/izenda-app.css?   4676ff4fe0cdf3cd2bab"rel="stylesheet"></head><body><divclass="container"id="izenda-root"></div><scripttype="text/javascript"src="/<your Url here>/izenda-vendors.js?4676ff4fe0cdf3cd2bab"></script><scripttype="text/javascript"src="/<your Url here>/izenda_app.js?4676ff4fe0cdf3cd2bab"></script></body>
     ```
   * Example change:

     ```
     <linkrel="shortcut icon"href="/IzendaFront/favicon.png"><linkhref="/IzendaFront/izenda-app.css?4676ff4fe0cdf3cd2bab"rel="stylesheet"></head><body><divclass="container"id="izenda-root"></div><scripttype="text/javascript"src="/IzendaFront/izenda-vendors.js?4676ff4fe0cdf3cd2bab"></script><scripttype="text/javascript"src="/IzendaFront/izenda_app.js?4676ff4fe0cdf3cd2bab"></script></body>
     ```
4. Update the web.config file in the UI folder

   * Target code:

     ```
     <actiontype="Rewrite"url="/<your Url here>/"/>
     ```
   * Example change:

     ```
     <actiontype="Rewrite"url="/IzendaFront/"/>
     ```

#### Within the API Folder of your Deployment

* Update the Web.config file

  + Target code:

    ```
    <httpHandlers><addverb="*"type="Nancy.Hosting.Aspnet.NancyHttpRequestHandler"path="/<Your API URL here>/api/*"/></httpHandlers><handlers><addname="Nancy"verb="*"type="Nancy.Hosting.Aspnet.NancyHttpRequestHandler"path="/<Your API URL here>/api/*"/></handlers>
    ```
  + Example change:

    ```
    <httpHandlers><addverb="*"type="Nancy.Hosting.Aspnet.NancyHttpRequestHandler"path="/IzendaBack/api/*"/></httpHandlers><handlers><addname="Nancy"verb="*"type="Nancy.Hosting.Aspnet.NancyHttpRequestHandler"path="/IzendaBack/api/*"/></handlers>
    ```

> This concludes the steps necessary to install Izenda using virtual directories/applications. Please refer to the following guides below: - Troubleshooting & Verifying the Installation - Common Izenda Stand-alone Installation Issues - Editing the Configuration Files

### [Troubleshooting & Verifying the Installation](#id21)

* To ensure that your API site is running correctly, navigate to [http://YOUR\_API\_URL/api/404](http://your_api_url/api/404) (e.g. <http://localhost:8080/api/404>)

  If your API is installed correctly, you should see the graphic below:

  ![../_images/SuccessfulAPI.png](https://devnet.logianalytics.com/hc/article_attachments/12528163808023/successfulapi.png)
* Navigate to the API folder, you should see a ‘logs’ folder with with at least one log file. If you do not see the folder and/or files, verify that the application pool and/or web site user have write permissions to the API folder.

### [Common Izenda Standalone Installation Issues](#id22)

**IIS Issues**:

* ASP.NET
  :   Izenda’s API is a .NET web application compatible with .NET 4.0 and higher.

      For .NET web applications to run through IIS you need to install IIS ASP.NET through your server’s Add Roles and Feature Wizard, or through the [IIS Web Platform Installer](https://www.microsoft.com/web/downloads/platform.aspx).

      + Add Web Server Role and .NET Framework
      + Install ASP.NET 4.5 Components

      Without these features installed you may encounter errors like the following:

      HTTP Error 500.xx – Internal Server Error

      The requested page cannot be accessed because the related configuration data for the page is invalid.
* URL Rewrite Module
  :   Izenda’s Stand-alone UI web.config makes use of the IIS URL Rewrite Module for routing.

      You’ll install this module through the [IIS Web Platform Installer](https://www.microsoft.com/web/downloads/platform.aspx).

      + Install ASP.NET 4.5 Components

      Without this feature installed you may encounter errors like the following navigating to the UI.

      Configuration Error

      An error occurred during the processing of a configuration file required to service this request.
* API Permissions
  :   If you can get Izenda running and see the UI, but get an error after setting your Izenda Configuration Database Connection String, you may be encountering permission issues at the API level.

      Izenda’s API needs proper write permissions to its own directory to create the izendadb.config file and generate log files.

      Often there are issues using just the default IUSR or NT AUTHORITY\NETWORKSERVICE roles to provide these permissions.

      Try the following to get past the issue:

      + Give the IIS Application Pool Full Access to the API directory.

        > You can see the API’s Application Pool name just by looking at the application’s basic settings in IIS.
        >
        > ![../_images/install_IIS_basic_settings.png](https://devnet.logianalytics.com/hc/article_attachments/12528163813399/install_iis_basic_settings_395x222.png)
        >
        > You can then use that name in setting your folder permissions as you see below.   
        > `IISAppPool\YouApplicationPoolName`
        >
        > ![../_images/install_IIS_AppPool_name.png](https://devnet.logianalytics.com/hc/article_attachments/12528147841303/install_iis_apppool_name_344x190.png)
        >
        > After giving this IIS Application Pool Full Access rights, you can restart the API, and try using the UI again.

**Oracle Issues**:

* Microsoft Visual C++ 2010 Redistributable for Izenda’s Oracle Drivers

  > Izenda’s Oracle Drivers utilize the Microsoft Visual C++ 2010 Redistributable.
  >
  > These can be installed by downloading the installer from Microsoft:   
  > [Microsoft Visual C++ 2010 Redistributable Package (x64)](https://www.microsoft.com/en-us/download/details.aspx?id=14632)
  >
  > Without this dependency installed you may encounter errors like the following.
  >
  > Could load file or assembly ‘Oracle.ManagedDataAccess’ or one of its dependencies. An attempt was made to load a program with an incorrect format.
  >
  > An unhandled exception occurred during the execution of the current web request.

**Resource Configuration**:

* Virtual Directory vs Individual Sites
  :   There are two different ways to install Izenda Stand-alone, as two separate applications with distinct ports or domains or as one application with a virtual directory.

      Concepts from these two separate installation options cannot be mixed together without creating issues. Make sure to follow just one guide or the other:

      + Izenda Installation as Two Separate Sites
      + Deploying Izenda as a Virtual Directory or Application

      Once you have followed one set of instructions to completion, you can move on to Troubleshooting & Verifying the Installation guides, and [Install Izenda System Database and Apply License](https://devnet.logianalytics.com/hc/en-us/articles/12528284579991-System-DB-and-License) guides.
* The izenda.config.js File
  :   You’ll need to edit the izenda\_config.js file during installation and it’s important to use fully qualified URLs for the WebApiURL.

      For example, a fully qualified URL to the API should include `http://` at the beginning and `/api/` at the end. It should look something like what you see below. For Izenda Installation as Two Separate Sites this is all you need to edit.   
      `WebApiUrl:"http://192.168.45.37:8200/api/"`

      For Deploying Izenda as a Virtual Directory or Application you need to edit the BaseUrl. This should look like the following, per the instructions with the trailing slash.   
      `BaseUrl:”/IzendaDirectory/”`

      If you don’t properly configure this file you may be able to see the Izenda login UI, but not get directed to the setup UI, or you may see many console errors in your browser’s dev tools.

**Connection Strings**:

* Misconfigured Connection Strings and Difficulty Connecting
  :   Izenda supports many different database types, and has specific drivers for these specific database types.

      + Make sure you’ve selected the right Data Server Type in the dropdowns near Connection String UIs.

        > ![../_images/install_select_data_server_type.png](https://devnet.logianalytics.com/hc/article_attachments/12528147847575/install_select_data_server_type_900x150.png)
      + Make sure you’ve used the proper syntax for your Connection String.
      + Certain characters may cause issues when used in Connection Strings. Avoid using characters such as semicolons, single-quotes, or double-quotes

        > MSSQL, PostgreSQL, Oracle, and MySQL Connection Strings are all formatted a little different, provide different options, and expect different syntaxes. Use resources like [ConnectionStrings.com](https://www.connectionstrings.com/) to make sure you’re including the right details, options, and port numbers:
        >
        > - MSSQL
        > - PostgreSQL
        > - Oracle
        > - MySQL
      + Make sure you’ve allowed the connection through your Network Security.

        > If you use custom ports for your database you’ll need to factor that into both the web server running Izenda as well as your Connection String.
        >
        > If you use Azure or AWS you may need to add the web server running Izenda to your Network Security Groups, or whitelist the IP address so that it can connect to your database.
      + Make sure you’ve given your Connection String user proper permissions.

        > Double check that the connection string user has permissions to the databases and schemas you want to connect to. You’ll need to give read/write permissions to the user for the Izenda Configuration Database. Izenda cannot get around your RDBMS security, as you might expect.
      + Try connecting with another tool or application.

        > If you’re continuing to have issues with a Connection String you may want to ensure that it’s an Izenda specific problem before reaching out.
        >
        > Try using your RDBMS management tools to connect to the database with the same user, and preferably from the same server, that you are trying to connect with using Izenda.

## [Install Izenda Standalone on Ubuntu OS](#id23)

### [Pre-install preparations](#id24)

Runtime Installation - Izenda 5.0.0 and above

Izenda depends on ASP.Net Core 3.1 runtime environment to run applications.

1. Create an instance of Ubuntu 18.04
2. Login using ssh as the default user
3. Download and install .NET core 6.0 SDK run time env. [Download here.](https://dotnet.microsoft.com/download/dotnet/6.0)

   `wget https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb`
4. Use dotnet--info to check the installation of .NET Core. You will get a confirmation notice if you performed a successful installation.

### [Install Izenda as two separate sites](#id25)

1. Create **izenda-ui.conf** under /etc/apache2/sites-available: `sudovim/etc/apache2/sites-available/izenda-ui.conf`

   ```
   Listen 8080
   									<VirtualHost *:8080>
   									ServerAdmin webmaster@localhost
   									DocumentRoot /var/www/izenda-ui/StandaloneUI
   									ErrorLog /var/log/apache2/izenda-ui-error.log
   									CustomLog /var/log/apache2/Izenda-ui-access.log common
   									<Directory "/var/www/izenda-ui/StandaloneUI">
   									RewriteEngine on
   									# Don't rewrite files or directories
   									RewriteCond %{REQUEST_FILENAME} -f [OR]
   									RewriteCond %{REQUEST_FILENAME} -d
   									RewriteRule ^ - [L]
   									# Rewrite everything else to index.html to allow html5 state links
   									RewriteRule ^ index.html [L]
   									</Directory>
   									</VirtualHost>
   								
   ```
2. Create **izenda-api.conf** under //etc/apache2//sites-available: `sudovim/etc/apache2/sites-available/izenda-api.conf`

   ```
   Listen 8081
   									<VirtualHost *:8081>
   									ProxyPreserveHost On
   									ProxyRequests Off
   									ProxyPass / http://127.0.0.1:5000/
   									ProxyPassReverse / http://127.0.0.1:5000/
   									ServerName localhost
   									ErrorLog /var/log/apache2/izenda-api-error.log
   									CustomLog /var/log/apache2/Izenda-api-access.log common
   									</VirtualHost>
   								
   ```
3. Active the Front-end and Back-end sites.

   ```
   sudo a2ensite izenda-api.confsudo a2ensite izenda-ui.conf
   ```
4. Verify the configuration: `sudoapachectlconfigtest`. If the configuration is correct, the result will be `SyntaxOk`. If not, there is an issue in the configuration.
5. Update WebURL in **Izenda\_Config.js** file with the proper prt (8081). `WebApiUrl:"http://localhost:8087/api/`
6. Provide write permission to current user

   ```
   sudo gpasswd -a "$USER" www-datasudo chown -R "$USER":www-data /var/wwwfind /var/www -type f -exec chmod 0660 {} \;sudo find /var/www -type d -exec chmod 2770 {} \;
   ```
7. Restart the website: `sudoserviceapache2restart`
8. Start your dotnet application: `sudodotnetIzenda.BI.API.AspNetCore.dll`. If the installation is success, you can browse you website via localhost with the 8080 port

### [Create monitor service](#id26)

1. Install Supervisor, a monitor service app: `sudoapt-getinstallsupervisor`
2. Create supervisor config file: `sudovim/etc/supervisor/conf.d/izenda-api.conf`
3. Add the following content to the above file

   ```
   [program:dotnettest]command=/usr/bin/dotnet /var/www/izenda-api/API_AspNetCore/Izenda.BI.API.AspNetCore.dll  --urls "http://*:5000"directory=/var/www/izenda-api/API_AspNetCoreautostart=trueautorestart=truestderr_logfile=/var/log/izenda-api.err.logstdout_logfile=/var/log/izenda-api.out.logenvironment=ASPNETCORE_ENVIRONMENT=Productionuser=www-datastopsignal=INT
   ```
4. Command to start/stop the service

   * Start Supervisor: `sudoservicesupervisorstart`
   * Stop Supervisor: `sudoservicesupervisorstop`
5. Verifying the service running progress `sudotail-f/var/log/izenda-api.out.log`

### [Configuring Exporting](#id27)

1. Configuring Exporting - Izenda v5.0.0 and above

* Apply file permission to the Export Engine’s executable in the Export folder of Izenda API - Linux example:

  1 sudo chmod 777 /API\_AspNetCore/Export/CEFExporterLinux/Dundas.BI.Export.CEFExporter.exe
* For a Linux server:
* Install the X Virtual Frame Buffer (XVFB) service and support packages.

  1 sudo apt-get update && \

  2 apt-get install libasound2 libatspi2.0-0 libexpat1 libfontconfig1 libnspr4 libpangocairo-1.0-0 libxkbcommon-x11-0 \

  3 libnss3 libcairo2 libpango-1.0-0 libcups2 libxkbcommon0 libxshmfence1 libxcomposite1 libxdamage1 libxrandr2 libgbm1 libatk1.0-0 libatk-bridge2.0-0 xvfb --no-install-recommends -y
* Manually start XVFB service - Optional (Izenda API will start the service if it detects it is not already running)

  1 Xvfb :99 -screen 0 1024x768x24 -nolisten tcp >/dev/null 2>&1 &
* For a Windows server, install the required Visual C++ Redistributable Packages → [https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-17](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)0

Apply file permission to the Exporter Engine’s executable in the Export folder of Izenda API - Linux command example:

1 sudo chmod 777 /API\_AspNetCore/Export/CEFExporterLinux/Dundas.BI.Export.CEFExporter.exe

## [Additional Reference](#id28)

* Understanding Configuration vs. Reporting Connection Strings
  :   The Izenda Configuration Database Connection String and Reporting Data Source Connection Strings are set in two different places, it totally separate UIs or underlying APIs.

      + Izenda Configuration Database Connection String

        > The Izenda Configuration Database Connection String will be set in the Settings page under the System DB & License tab.
        >
        > Be very careful when setting and/or changing this connection string!
        >
        > This connection string will point Izenda to a database where it can create its schema and store report metadata, dashboard metadata, data model metadata, Tenant, Role, and User metadata, and much more.
        >
        > If you set this to an existing database you will end up with Izenda specific tables in your schema, it’s usually best to use a separate empty database for the Izenda Configuration Database unless you’re comfortable with mixing Izenda’s storage schema with your database schema.
      + Reporting Data Source Connection Strings

        > Reporting Data Source Connection Strings will be set in the Settings page under the Data Setup/Connection String tab.
        >
        > After connecting Izenda will query the database to establish the available data source listing, so that you can choose specific objects to move into the visible data sources.
        >
        > These selected objects can then be further modeled upon, aliased, secured, and exposed to end-users within report designers.
        >
        > Do not delete Connection Strings if you simply need to change connection strings to another database with a similar schema, or if you need to add new objects to the available/visible data source lists, you can change/rebuild Connection Strings or press reconnect and refresh the schema.
        >
        > Deleting and recreating Connection Strings will break your reports and dashboards, where just resetting the Connection Strings or reconnecting generally will not.
* Editing Configuration Files
  :   Additional features can be set for a customized deployment experience. For live sites, several of the features below are recommended.

      + Change the Back-end passphrase, which is the key to encrypt and decrypt data in Izenda.

        > Enter a 29-character value into the value of this key: `<appSettings>`, `<addkey="izedapassphrase"value=""/>`

      Warning

      This passphrase cannot be changed afterwards since already encrypted data cannot be decrypted with another passphrase.

      + Recommended: add [security configurations](https://devnet.logianalytics.com/hc/en-us/articles/12528299894551-Security-Recommendations#_bm)
      + Optionally change the default Back-end path `/api/`

        > e.g. change the path to `/rest/`
        >
        > 1. Edit the file `API\Web.config`, replace the default value “api”
        >    :   with the new value at the following places:
        >        - `<appSettings>`, `<addkey="izedaapiprefix"value="api"/>`
        >        - `<system.web>`, `<httpHandlers>`, `<addverb="*"type="Nancy.Hosting.Aspnet.NancyHttpRequestHandler"path="api/*"/>`
        >        - `<system.webServer>`, `<handlers>`, `<addname="Nancy"verb="*"type="Nancy.Hosting.Aspnet.NancyHttpRequestHandler"path="api/*"/>`
        > 2. Also edit the file `App\izenda_config.js`, replace the default
        >    :   value “api” with the new value at the following places:
        >        - `"WebApiUrl":"http://127.0.0.1:8888/api/",`
      + Optionally change Izenda log file settings

        > - Change the default log file location in `<log4net..>`, `<appendername="RollingFileAppender"..>`, `<filevalue="logs\izenda-log.log"/>`, which resolves to C:\inetpub\wwwroot\Izenda\API\logs in a typical installation.
        > - Change how the log files are archived/rotated/rolled in `<log4net..>`, `<appendername="RollingFileAppender"..>`.
        >
        >   > The default setting is to keep maximum 1000 last files of 5MB each every day. See other examples at [log4net document](https://logging.apache.org/log4net/release/config-examples.html#rollingfileappender).
        > - Enable folder compression: log file content is all text and will compress up to 2% of the original size.
        >
        >   > 1. Right-click on the folder (C:\inetpub\wwwroot\Izenda\API\logs) and click Properties.
        >   > 2. Click Advanced button in General tab.
        >   > 3. Tick Compress contents to save disk space check-box, then click OK twice.
        >   > 4. Select either option: this folder only, or this folder, subfolders and files then click OK.
        >   > 5. Confirm the compression status: the folder will have blue name, or have two arrows added at the top right of its icon (from Windows 10).
      + Optionally enter settings for [EVO PDF Azure](http://www.evopdf.com/azure-html-to-pdf-converter.aspx) option, or accept the default values to use the local embedded library.

        > 1. Under `<configuration>`, find or add the following section:
        >
        >    > ```
        >    > <evoPdfSettingscloudEnable="false"><azureCloudServiceserver=""port=""servicePassword=""/></evoPdfSettings>
        >    > ```
        > 2. Set `cloudEnable="true"` to use the Azure option, then enter the server IP, port and password.
      + Optionally change the default quartz thread count settings.

        > 1. In `<configSections>` element, add quartz configure section to create the quartz configuration. For example:
        >
        >    > ```
        >    > <configSections><sectionname="quartz"type="System.Configuration.NameValueSectionHandler, System, Version=1.0.5000.0,Culture=neutral, PublicKeyToken=b77a5c561934e089"/></configSections>
        >    > ```
        > 2. In `<configuration>` element, specify the maximum thread count by an integer. For example:
        >
        >    > ```
        >    > <configuration><quartz><addkey="quartz.threadPool.threadCount"value="20"/></quartz></configuration>
        >    > ```

### Next: [Install Izenda System Database and Apply License](https://devnet.logianalytics.com/hc/en-us/articles/12528284579991-System-DB-and-License)

See also

* [Installing IIS 8.5 on Windows Server 2012 R2](http://www.iis.net/learn/install/installing-iis-85/installing-iis-85-on-windows-server-2012-r2).
* [Install IIS and ASP.NET Modules](http://www.iis.net/learn/application-frameworks/scenario-build-an-aspnet-website-on-iis/configuring-step-1-install-iis-and-asp-net-modules)
* [Understanding built in user and group accounts in IIS](https://www.iis.net/learn/get-started/planning-for-security/understanding-built-in-user-and-group-accounts-in-iis)
