---
title: "Version, Connections, and Permissions"
id: 5281662050199
section: "Troubleshooting"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281662050199-Version-Connections-and-Permissions
updated_at: 2022-05-03T22:08:44Z
---

# Version, Connections, and Permissions

# Version, Connections, and Permissions

This topic details a few useful things to check when troubleshooting an issue within Exago.

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

## Verifying Folder Permissions

A common issue when installing or updating Exago is to not set read/write permissions on various folders the application uses. For these folders the user accessing them via the IIS app pool must have read write permissions. For the default app pool this is the IIS user. The folders that require read/write permissions are listed below.

* **<WebApp>/Config** – this folder contains the configuration settings loaded and modified by the Admin Console.
* **<WebApp>/Temp** – this folder is used to store some temporary files.
* The folder specified in the **Report Path** of the **Main Settings**.
* The folder specified in the **Temp Path** of the **Main Settings**.

![](https://devnet.logianalytics.com/hc/article_attachments/5432191514775/image117.png)

Security tab of the Properties dialog for the Reports folder

## Verifying Administration Settings

Some settings in the **Admin Console** are used to connect to other programs such as databases, Web Services, .NET Assemblies or the External Interface module. Each of these items will have a **Test Connection** ![CheckmarkAdmin.png](https://devnet.logianalytics.com/hc/article_attachments/5432158412439/checkmarkadmin.png) icon next to them. Click **Test Connection** to verify the connection.

The following settings can be checked:

* The **Data Source**(s) being utilized by the report you are investigating.  
  ![eaeH5B8BVm.png](https://devnet.logianalytics.com/hc/article_attachments/5432121751831/eaeh5b8bvm.png)
* **General** > **Scheduler Settings** > **Schedule Remoting Host** and **Remote Execution Remoting Host**  
  ![cycukwULlW.png](https://devnet.logianalytics.com/hc/article_attachments/5432179514647/cycukwullw.png)
* **General** > **Other Settings** > **External Interface**
* **Storage Management** > **Class Name**
* **Storage Management** > **Check Database Settings**

## Verifying Versions

When updating Exago occasionally issues arise because the Storage Management database schema,Scheduler Service or Web Service API have not also been updated. For the Scheduler Service and Web Service API to function properly they must be running the same version and build as the Web Application.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> When using the .NET API you will need to copy the DLLs from the updated Exago application to the bin directory of the host application.

### Exago Web Application

To check the version of the Web Application:

1. Navigate to the home page.
2. Press **Ctrl + Shift + V**.  
   ![oZeVxP9QNx.png](https://devnet.logianalytics.com/hc/article_attachments/5432179542295/ozevxp9qnx.png)

### Scheduler Service

To check the version of the Scheduler Service on Windows:

1. Locate the file `<Sched>/eWebReportsScheduler.exe`.
2. Right click on this file and select **Properties**.
3. Navigate to the **Details** tab.![](https://devnet.logianalytics.com/hc/article_attachments/5432179586711/image120.png)

   Checking the version number of the Scheduler Service, this one is *v2015.1.3.0*

To check the version of the Scheduler Service on Linux:

1. Open a terminal.
2. Issue the following command

   ```
   ikdasm -assembly <Sched>/eWebReportsScheduler.exe | grep Version
   ```

The result will resemble the following:

```
Version:		2020.1.0.108
```

### Web Service API

To check the version of Web Service API on Windows:

1. Locate the file `<WebSvc>/bin/WebReportsApi.dll`.
2. Right click on this file and select **Properties**
3. Navigate to the **Details** tab.![](https://devnet.logianalytics.com/hc/article_attachments/5432206337559/image121.png)

   Checking the version number of the Web Service API DLL, this one is *v2015.1.3.0*

To check the version of the **Web Service API** on Linux:

1. Open a terminal.
2. Issue the following command

   ```
   ikdasm -assembly <WebSvc>/WebReportsApi.dll | grep Version
   ```

The result will resemble the following:

```
Version:		2020.1.0.108
```

## Storage Management Database Schema v2020.1+

To check the version/update the **Storage Management database schema**:

1. Navigate to **Admin Console** > **Storage Management**.
2. Click **Check Database Settings**.

To update the database schema:

1. Click **Prepare Database** or **Show Prepare Database SQL**.

An explanation of these two different buttons can be found in the [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management) topic.
