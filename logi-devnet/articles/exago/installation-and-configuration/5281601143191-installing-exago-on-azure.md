---
title: "Installing Exago on Azure"
id: 5281601143191
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281601143191-Installing-Exago-on-Azure
updated_at: 2023-04-03T17:52:19Z
---

# Installing Exago on Azure

# Installing Exago on Azure

Microsoft Azure is a cloud infrastructure for hosting files, databases, virtual machines, and web applications. Exago BI supports various forms of integration with Azure.

* **[Virtual Machine](#Virtual)** — Exago BI can be installed on a Windows virtual machine on Azure.
* **[File Storage](#File)** — Exago BI data can be stored and accessed from Azure storage containers.
* **[Azure App Services](#Azure)** — Although not recommended for production environments, the Exago BI Web Application, REST Web Service API and .NET API host apps can be installed as Azure App Services. An Azure Virtual Machine is also required for remote report execution when utilizing an Azure App Service.

These methods can be implemented independent of each other. However, Web App integration and VM integration are usually redundant with each other, and most Web App solutions should also implement Azure file storage. This guide will walk through how to set up each of these solutions.

### Which solution should I use?

Azure virtual machines are the preferred implementation method for production environments.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
>
> App Services should only be used for testing and demonstration—not in production.

## File Storage

Exago BI can be integrated with Azure cloud storage for storage and live access to reports, templates, config, and other data files.

The following Azure resources are:

* Required
  + ![](https://devnet.logianalytics.com/hc/article_attachments/5432246583319/storage_icon.png) Storage account
  + ![](https://devnet.logianalytics.com/hc/article_attachments/5432279735191/blob.png)Blob storage
* Optional
  + ![](https://devnet.logianalytics.com/hc/article_attachments/5432246640919/files.png) Files storage

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
>
> The Web Application, Scheduler Service, Web Service API and any cloud storage mechanisms must share at least one security protocol in common otherwise they will not be able to communicate with each other. For more information, refer to [Application Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings).

**Blob storage** is a “flat” file system, which stores every file at the root level. To make use of this system, Exago BI emulates a directory structure using file names. Standard and premium blockblobstorage accounts are supported with Exago.

**File storage** is a directory-based system. Files are placed into directories, which can have sub-directories.

For *pre-v2020.1*, reports can be stored in File storage or Blob storage. Config files, templates, themes, and temp files must be stored in blob storage. For *v2020.1+,* only config files and temp files are stored locally. Reports, templates and themes are stored in a Storage Management database.

In the Azure Dashboard, begin by creating a new Storage account or navigating to an existing one.

![](https://devnet.logianalytics.com/hc/article_attachments/5432241866519/storage_resource.png)

This section is divided into three parts: **Config file** storage, **Reports** storage, and **Temporary files** storage (which includes themes and templates). If you are implementing Exago BI as a scalable app, you must set all three to static locations.

### Config File

An Exago BI installation contains a configuration file, usually called **WebReports.xml**, which tells the application where to store Reports and Temp files.

First, in the Storage account, navigate to **Access Keys**. Record the two connection strings.

#### Azure Connection String

An **Azure Connection String** is a formatted string which contains the Azure account name and a unique alphanumeric key. It is used to give applications access to the storage account. The string uses the following format:

```
DefaultEndpointsProtocol=https;AccountName=acctName;AccountKey=encryptedalphanumerickey;
```

Next, there are two places which you need to specify the location of the configuration file:

1. The `appSettings.config` file in the web app install directory.
2. If using the .NET API, an argument in the **API constructor method**.

#### appSettings.config

Exago BI contains a file called **appSettings.config** in the root folder of the install directory. This file is used for custom app settings which are automatically imported into **Web.config** during runtime.

This file may also be used to specify other important environmental conditions, such as security protocols and input sanitation rules. More information about all available settings can be found in [Application Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281615366423-Application-Settings).

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Do not edit `web.config`. It is automatically generated by Exago BI, and any changes will be overridden.

To set the config file location, add the following key to the `appSettings.config` file:

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> The connection strings used for report, configuration file and temporary file storage must be unique.

```
<add key="ExagoConfigPath" value="pathtype=azure;credentials='Azure Connection String';storagekey=config"/>
```

* *credentials*: Azure Credentials Connection String.
* *storagekey*: The prefix of a blob container used to store the config file.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> When both the REST Web Service API and cloud config storage are being used, the `ExagoConfigPath` node must be included in both the REST Web Service API and Web Application **appSettings.config** files.

#### API

.NET API host apps cannot access the **appSettings.config** file. Instead, use one of the following two methods to specify a config file location:

1. Place the **config key** within the host application’s web.config or app.config.
2. Or pass the connection string in the API constructor method:

```
API api = new API("/exago/virtual/path", "configFn.xml", "pathtype=azure;credentials='Azure Connection String';storagekey=config");
```

* *storagekey*: The prefix of the blob container used to store the config file.
* *configFn*: The name of the config file.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> When both the REST Web Service API and cloud config storage are being used, the `ExagoConfigPath` node must be included in both the REST Web Service API and Web Application **appSettings.config** files.

### Reports Storage

For versions *v2020.1+*, setup the **Storage Management** system for storing reports, templates and themes.

### Upgrade Install

If upgrading from a previous version of Exago BI, review these topics:

* [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction)
* [Storage Management: Transitioning from Legacy Storage Methods](https://devnet.logianalytics.com/hc/en-us/articles/5281647090839-Storage-Management-Transitioning-from-Legacy-Storage-Methods)
* [Storage Management: Getting Started](https://devnet.logianalytics.com/hc/en-us/articles/5281653081111-Storage-Management-Getting-Started)

### New Install

If this is a new installation, review these topics:

* [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction)
* [Storage Management: Getting Started](https://devnet.logianalytics.com/hc/en-us/articles/5281653081111-Storage-Management-Getting-Started)
* [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management)

**For Exago BI versions *pre-v2020.1*:**

To use an Azure storage resource for report and folder management, enter a formatted connection string in the *Report Path* field in the config file.

![](https://devnet.logianalytics.com/hc/article_attachments/5432261982615/report_path.png)

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> The connection strings used for report, configuration file and temporary file storage must be unique.

The connection string uses the following format:

```
pathtype=azure;credentials='Azure Connection String';storagekey='reports';usefilestorage=false
```

* *credentials*: The Azure Connection String.
* *storagekey*: The prefix of the container used to store report files. Reports are stored in “*storagekey*-reports”, templates in “*storagekey*-templates”, and themes in “*storagekey*-themes”. This key is optional and defaults to “*wrreports*“.
* *usefilestorage*: If true, Reports are stored in File storage. If false, Blob storage is used. Templates and themes always use blob storage. This key is optional and defaults to false.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Templates are automatically stored in blobs when the template upload button is used in Exago. Themes need to be manually uploaded to blob storage.

### Migrating from local storage to Azure blob storage

Exago BI emulates a directory structure within a “flat” file system like Azure blob storage by placing a “placeholder.dir” block blob in each directory. This directory file serves as a reference to a folder within the blob container and is automatically added to new folders when the Report Path is set to an Azure blob storage container. If this file is not present, Exago will not be able to recognize that the virtual directory exists within a blob.

When migrating from local storage to Azure blob storage, this file will need to be manually added to pre-existing report folders as it will not exist in folders that were created when the report path was set to a local directory. In order to manually add this file to these folders, please follow these steps after the Report Path is set to an Azure blob storage container:

1. In Exago BI, add a new folder to the Report Tree.
2. With the Azure Storage Explorer, navigate to this folder.
3. Copy the “placeholder.dir” blob within this folder and paste it into folders where it does not already exist.

### Temporary Files Storage

Azure allows an App Service to be scaled up to multiple instances on separate servers. When implementing this configuration, take the following safeguards in order to prevent loss of user data.

Each instance of Exago BI has its own local temp directory, whose path can (optionally) be specified in the **Temp Path** setting in the config file (defaults to %INSTALLDIR%Temp).

![](https://devnet.logianalytics.com/hc/article_attachments/5432246736535/temp_path.png)

In a scalable configuration, initial user calls will reach one instance, storing temp files on that server, but subsequent calls may reach a separate instance, which will not have those temp files in its local directory. There are two solutions to resolve this issue:

* [Temp Cloud Service](#Temp)
* [Azure Affinity Cookie](#Azure2)

#### Temp Cloud Service

This is Exago BI’s built-in solution for handling multiple instances. Specifying a **Temp Cloud Service** causes each instance to push its temporary files to a shared Blob container. Then if a subsequent user call reaches a separate instance, that instance will pull the relevant files from the Blob to its local temp directory. Temp files may only be stored in blob storage.

To set up an Azure storage resource for temporary files:

1. Create a container for temporary files with the Azure Storage Explorer. The default container name is `wrtemp` but any container name, except for those used for report or configuration storage may be used by providing a `storagekey` in the connection string in step 2.
2. Set the **Admin Console** > **General** > **Main Settings** > **Temp Cloud Service** to a formatted connection string.  
   > ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
   >
   > The connection strings used for report, configuration file and temporary file storage must be unique.

The connection string uses the following format:

```
pathtype=azure;credentials='Azure Connection String';
```

to save temporary files to the default blob container named `wrtemp` or

```
pathtype=azure;credentials='Azure Connection String';storagekey=tempFileStorageKey
```

to save temporary files to a blob container named `tempFileStorageKey`.

**Examples:**

```
type=azure;credentials='DefaultEndpointsProtocol=https;AccountName=acctName;AccountKey=encryptedalphanumeric';
```

Store temporary files in the default `wrtemp` blob container

```
type=azure;credentials='DefaultEndpointsProtocol=https;AccountName=acctName;AccountKey=encryptedalphanumeric';storagekey=ourExagoTempFiles;
```

Store temporary files in a blob container named `ourExagoTempFiles`

#### Azure Affinity Cookie

Azure supports setting Affinity Cookies, which track which server instance each user is connected to and cause all calls within the session to reach the same instance.

In the app service, navigate to **Application Settings**. Set ARR Affinity to **On**.

![](https://devnet.logianalytics.com/hc/article_attachments/5432262025751/affinity_cookie.png)

## Virtual Machine

Exago BI can be hosted on a Windows-based Azure Virtual Machine. Installing Exago BI on a VM differs only marginally from installing it on a local machine. Therefore, this guide will not go into depth on this method.

You can interact with a VM using either a remote desktop application or a command shell application.

### Remote Desktop

1. Using Remote Desktop Connection or another remote desktop application, view the VM as a desktop environment.
2. Use a Web Browser to [download the Exago BI Installer](https://support.exagoinc.com/hc/en-us/categories/202053837).
3. Run the installer as Administrator and install Exago BI.
4. Configure Exago BI.

### Command Shell

1. On a local machine, use the above steps 2-4 to create a temporary Exago BI installation.
2. Remote into the VM using Windows PowerShell or another command shell application.
3. Copy the Exago BI directory to a directory on the VM.
4. Configure Windows and IIS (see **Manual Application Installation**).

After configuring IIS, open up the Exago BI port using a Windows Firewall inbound exception rule. You can then access Exago BI through the VM’s IP address. Set up DNS and data security as desired.

## Azure App Services

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Deploying the Exago BI Web Application in an Azure App Service also requires a separate Azure Virtual Machine and the Exago Scheduler Service for handling chart and map rendering. Consider using an Azure Virtual Machine for the entire deployment instead. See [Configuring Remote Report Execution Host for Azure App Service Deployments](https://devnet.logianalytics.com/hc/en-us/articles/5281592516375-Configuring-Remote-Report-Execution-Host-for-Azure-App-Service-Deployments).

The following Azure resources are required:

* ![](https://devnet.logianalytics.com/hc/article_attachments/5432217747863/app_service_plan.png) App Service plan
* ![](https://devnet.logianalytics.com/hc/article_attachments/5432279952279/app_service.png) App Service

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> You may require a Storage Account to run Exago BI as a scalable app. See [File Storage](#File) for details.

### Hosting Exago BI in an App Service

1. In the Azure Dashboard, create a new App Service container or navigate to an existing one.  
   ![](https://devnet.logianalytics.com/hc/article_attachments/5432217806103/web_app_container.png)
2. In the App Service, navigate to **Deployment Credentials**. Add a username and password. This will allow FTP access to the app service to transfer files.
3. Next, you’ll need an FTP application. Open a connection using the deployment credentials created in step 2. Copy the local Exago BI web app installation directory to the app service container.  
   ![](https://devnet.logianalytics.com/hc/article_attachments/5432262221079/ftp_copy.png)
4. In the App Service, navigate to **Application Settings**. Set the following:
   * .NET Framework version: *v4.0* or Later
   * Managed Pipeline Version: *Integrated*
5. Under **Virtual applications and directories** create a virtual directory path to the installation directory and check the *Application* check box.  
   ![](https://devnet.logianalytics.com/hc/article_attachments/5432242031895/virtual_path.png)
6. Click **Save** to save settings.
7. Configure the Remote Report Execution Host as a Virtual Machine. See [Configuring Remote Report Execution Host for Azure App Service Deployments](https://devnet.logianalytics.com/hc/en-us/articles/5281592516375-Configuring-Remote-Report-Execution-Host-for-Azure-App-Service-Deployments).
8. Test the installation by navigating to the *WebAppUrl**virtual path to Exago App Service**Admin.aspx* page (Admin Console).

If using Azure Blob Storage to store the config file, follow the **[File Storage](#File)** instructions before setting the base config. We also recommend setting up a state server either with SQL Server or another database when running Exago in an Azure App Service. See [Setting up a State Server](https://devnet.logianalytics.com/hc/en-us/articles/5281581463959-Setting-up-a-State-Server). If you need more information, contact [Exago Support](https://help.insightsoftware.com/s/contactsupport?language=en_US "Exago support").

### Using Exago Web Service API in an App Service

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This walk through requires either a local Web Service API installation, or a downloadable ZIP file containing the WebServiceApi directory.

1. Copy the contents of the local installation’s WebServiceApi folder to the app service container.
2. Under **Virtual applications and directories** create a virtual directory path to the WebServiceApi directory and check the *Application* check box.
3. Click **Save** to save settings.
4. In Azure, edit the **WebServiceApi\Config\WebReportsApi.xml** file as follows:

   ```
   <apppath>
   	virtual path to Exago App Service
   </apppath>
   <webreportsbaseurl>
   	virtual path to Exago App Service
   </webreportsbaseurl>
   ```

   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
   >
   > Include a trailing slash for both the `apppath` and `webreportsbaseurl` elements.
5. In the **WebServiceApiappSettings.config** file, add a new key to enable the REST service.

   ```
   <appSettings>
      <add key="ExagoREST" value="TRUE" />
   </appSettings>
   ```

   The result should be the following:

   ```
   <appSettings>
      <add key="ExagoREST" value="True" />
   </appSettings>
   ```
6. To prevent front end access without authentication outside of the API, in the **Admin Console**, navigate to **General** > **Main Settings** > set **Allow direct access to Exago (bypassing API)** to *False*. Click **OK**. Test the installation by navigating to the *WebAppUrl**Exago**Api.aspx* page. An ‘Unauthorized access. Contact the system administrator if an error appears. If you need more information, contact [Exago Support](https://help.insightsoftware.com/s/contactsupport?language=en_US "Exago support").
7. To test that the path was set correctly, navigate to *WebAppUrl**virtual\_path\_to\_Exago\_App\_Service**Api.aspx*. A test file listing available supported operations in the API should appear.
8. To prevent unauthorized **Admin Console** access to prevent users from inadvertently reaching it, delete *WebAppUrl**Exago**Admin.aspx* and *WebAppUrl**Exago**Bin**admin.aspx.cdcab7d2.compiled*.  
   > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
   >
   > Make a backup of the files before deletion in case **Admin Console** may be needed later.
9. Test that **Admin Console** is no longer accessible by navigating to *WebAppUrl/ExagoAdmin.aspx*. A 404 error page should appear.
10. Test that REST is enabled by utilizing an advanced REST client such as Advanced REST Client. Make a POST request to *WebAppUrl**virtual\_path\_to\_Exago\_App\_Service**rest**rest**sessions*.  

    | Header Name | Header Value |
    | --- | --- |
    | Accept | application/json |
    | Content-Type | application/json |
    | Authorization | The REST authorization key. Review the [REST — Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281660927895-REST-Introduction) topic for more information. |

    Copy the **AppUrl** received in the response and append it to the end of the browser’s URL *WebAppUrl**virtual path to Exago BI App Service* The Exago BI front end should load, proving that the application can only be reached through the API.
11. Configure the remote report execution host as a Virtual Machine. See [Configuring Remote Report Execution Host for Azure App Service Deployments](https://devnet.logianalytics.com/hc/en-us/articles/5281592516375-Configuring-Remote-Report-Execution-Host-for-Azure-App-Service-Deployments).

### Using the .NET API with Azure

Exago BI .NET API based host applications must be compiled locally before being uploaded to the Azure app container. References to the `WebReports.dll` library should be updated manually, and the program recompiled, when upgrading to a new version.

Set the API constructor to use the previously set Exago virtual path:

```
API api = new API(@"/exago/virtual/path");
```

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> .NET host apps can only access virtual paths (and not URL paths). Therefore they must be located in the same App Service container as the Web Application.

Exago BI utilizes the virtual directory passed in the first argument of this constructor to locate the required .dll libraries to load Exago BI. In cases where the virtual directory is not specified within the API constructor (for example, if Exago BI is installed on the root of the .NET host application), then a reference to the `Microsoft.WindowsAzure.Storage.dll` library will need to be added manually to the host application.
