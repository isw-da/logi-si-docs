---
title: "Introduction to Logi Scheduler"
id: 1500009515482
section: "Doctype Declarations"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009515482-Introduction-to-Logi-Scheduler
updated_at: 2021-06-17T01:58:29Z
---

# Introduction to Logi Scheduler

# Introduction to Logi Scheduler

Logi Info includes the Logi Scheduler, which allows Logi applications to be run by administrators on a scheduled basis. Scheduling features can also be embedded in reports, allowing runtime scheduling by end users. This topic introduces these features.

* About The Logi Scheduler
* [Terminology](#Terminology)
* [Deployment for Windows](#WindowsOS)
* [Deployment for Java](#Java)
* [Configure Scheduler Communications](#Communications)
* [Schedule Task Databases](#Databases)
* [Quick and Easy Report Scheduling](#QuickEasy)

Using a release earlier than v9.5? For more information, see [Schedule Reports with Server Manager](https://devnet.logianalytics.com/hc/en-us/articles/1500009515862-Schedule-Reports-with-Server-Manager).

## About The Logi Scheduler

In simple terms, the **Logi Scheduler** is a proprietary service that runs "in the background" as either a Windows Service or a Linux/UNIX daemon. It maintains its own database of scheduled events and runs them at the desired times and intervals. The Scheduler service has no user interface of its own, but is instead directed to create, maintain, and delete scheduled events by other applications through an application interface.

This service is configured to start up automatically when its host server is started and therefore runs without user intervention. From a performance perspective, it consumes very few resources on the server and spends most of its time idling.

When the Scheduler "runs" an event from its database, it does so by opening a new web server session and calling a specific task in a Logi Info **Process****definition**. That process task can then run reports, send emails, etc. - any of the usual task-driven activities. Logi Report *does not* support process definitions, therefore the Logi Scheduler is not included with it.

The Scheduler service release and its corresponding Logi Info release are tightly-coupled so, for example, you must use the v11 Scheduler service with Logi Info v11; you cannot use the v10 Scheduler service with it.

### Additional Resources

This topic concerns itself primarily with the preliminaries: understanding the Scheduler service and installing it. A sister topic, [Use Logi Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/1500009532181-Use-Logi-Scheduler), is also available with more detailed information about how to configure the Scheduler and work with it from within a Logi application.

In addition, there are two sample scheduling applications available from DevNet that can be downloaded and examined for a better understanding of the elements that support the Scheduler. One of these, [Scheduler Console,](https://devnet.logianalytics.com/hc/en-us/articles/360050242853-Scheduler-Console-Sample-Application) is designed for administering the Scheduler on your server; this is the primary tool we provide for this purpose. The other sample application is an example of a report that allows end users to
schedule reports at runtime.

### Manage Older Scheduled Events

Prior to v9.5, scheduled reports were managed using the **Logi Server Manager**, a tool that was separately installed with your Logi product. In later releases, this tool is built into Studio and is no longer used for scheduled task management.

## Terminology

For the sake of clarity, the following terms are used in this Scheduler topic:

| Term | Description |
| --- | --- |
| Scheduler | The Windows service or Linux daemon that runs in the background and runs events at the times and intervals detailed in its database. |
| Scheduler Task | An event (one record) in the Scheduler's database. Contains details of time, frequency, interval, and the ID of the target process to run. |
| Process Task | A task within a Logi Info process definition in a Logi application. A Scheduler Task "runs" a Process Task at the desired time/interval. |
| Schedule XML | The XML representation of the scheduling details for a Scheduler Task. May include date, time, frequency, etc. |
| Schedule | An element used in report definitions which includes a user interface with controls, for the purpose of creating or editing a Scheduler Task. |
| Schedule Intervals | The time intervals that can be used in a Scheduler Task: *Once*, *Daily*, *Weekly*, and *Monthly*. In v10.0.366+, *Minutes* and *Hourly* are also available. |

The Scheduler is supported by special elements for both report and process definitions and these are introduced later on.

## Deployment for Windows

In a Windows environment, installation of the **Logi Info Scheduler Service for .NET** is accomplished as part of the Logi Info product installation. However, it's not selected for installation by default - you need to select the **Custom** installation option and indicate that it be installed. You can run the installation program again at any time and modify the installation to include the Scheduler if you need to.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771662743/introstudio_01.png)

As shown above, you must click the icon next to the Scheduler item and select "This feature will be installed on the local hard drive." from the drop-down list of options. Note that there are separate schedulers for .NET and Java applications.

By default, the .NET scheduler files will be installed to: C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service. In the rest of this topic, the installation folder you specified, the default or a custom location, will be abbreviated as <installFolder>.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778551447/introscheduler_02.png)

After installation is complete, you can use your Windows administrative tools to examine your services. The LogiXML Scheduler Service should appear as shown above, its status should be "Started", and it should be configured to start automatically.

Due to the flexible nature of the Scheduler and its interactions with Logi Info applications, you can install the Scheduler on a *different server* than the application web server, separate from Logi Info, if desired.

### With Logi Apps Using Logi Security and AuthNT

If you're planning to use the Scheduler to run secure Logi applications that use the "AuthNT" authentication source, then you need to configure the Scheduler service to log on using an account that can be authenticated *in the domain*. The default installation configuration uses the Local System account, which is only valid on the local machine. This configuration is independent of setting the **Run As** name for Scheduler
tasks or the **Scheduler User Name** in the \_Settings definition.

If the Logi application is using any
Active Directory groups to filter domain users, then the domain account used by the Scheduler must also belong to those groups. The account doesn't have to be an Administrator on the server running Scheduler, but it does need these minimum permissions to access the Scheduler database, log errors, etc.:

| Folder or File | Permissions |
| --- | --- |
| C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service | Read |
| C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service\Schedules.vdb3 | Read, Write |
| C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service\Log | Read, Write, Create |
| C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service\RunNowTasks | Read, Write, Create, Delete |

To change the account being used by the Scheduler:

 ![](https://logianalytics.zendesk.com/hc/article_attachments/4402771667351/introscheduler_03.png)

In the Services administrative tool, double-click the LogiXML Scheduler Service to view its properties, as shown above, then select the **Log On** tab. Check **This account:** and provide valid domain account information and click OK. Then stop and restart the Scheduler service.

## Deployment for Java

The **Logi Info Scheduler Service for Java** runs on the Linux/UNIX or Windows operating systems. It's distributed as part of the Logi Info product and, regardless of the server type that you plan to run it on in the end, in order to access its files it must first be installed on a Windows machine, using the Windows product installer, as shown in the previous section. Naturally, during the process you select the Scheduler Service for Java feature option, *not* the service
for .NET.

The default installation location is: C:\Program Files\LogiXML IES Dev\LogiXML Scheduler Service Java. In the rest of this topic, the installation folder you specified, the default or a custom location, will be abbreviated as <installFolder>.

### On a Windows Server

By default, the Scheduler Service for Java, installed on a Windows server, isn't configured to start automatically. Instead, it's started by running:

<installFolder>\bin\Scheduler.bat.

When running the Scheduler Service for Java on Windows 7 or Windows Vista, the User Account Control (UAC) system can interfere with normal operations of the Scheduler, as the <installFolder>\Log, \RunNowTasks and \Schedules folders require Write file access permissions. There are two options to resolve this: either disable UAC on the server, or use UAC to set the privileges
of these directories to allow Write access. This MSDN article
provides [more
information about UAC](https://docs.microsoft.com/en-us/windows/security/identity-protection/user-account-control/how-user-account-control-works) should you need it.

If you wish to start the Scheduler service automatically, and you feel comfortable directly modifying system-level configurations, use the Registry editor to add a String value in

HK\_Local\_Machine\Software\Microsoft\Windows\CurrentVersion\Run

Set its Value Name to LogiSchedulerJava and its Value Data to <installFolder>\bin\Scheduler.bat.

### On a Linux/UNIX Server

In order to subsequently install the Scheduler Service for Java on a Linux/UNIX server, copy *all* of the subfolders and files from the <installFolder> on the Windows machine to the desired installation folder on your Linux/UNIX server. That folder on your Linux/UNIX server now becomes your <installFolder> for the rest of this discussion.

The Scheduler is started by running <installFolder>/bin/Scheduler.sh. Don't use a symbolic link for this, as it may lead to unstable behavior.

To start the Java scheduler automatically, add a line to /etc/rc.d/rc.local. The invocation should be similar to

/opt/LogiSchedulerJava/Scheduler.sh &

Note that the ampersand (&) at the end *is* significant: it causes the application to load as a background process.

Due to the flexible nature of the Scheduler and its interactions with Logi Info applications, you can install the Scheduler on a *different server* than the application web server, separate from Logi Info, if desired.

## Configure Scheduler Communications

The Logi Scheduler "listens" for requests on a specific port. For security purposes, a key value is set for each instance of the Scheduler. Logi Info applications that wish to communicate with the Scheduler have to be internally configured with the same key value in order to be identified as legitimate clients of the service. By default, the appropriate Logi Info elements and the Scheduler are installed already configured to communicate on the same port and with the same default key value.

However, both of these attributes can be changed by (1) setting the appropriate attribute values in your Logi Info application's \_Settings definition, and (2) editing the text file named \_Settings.lgx in the Scheduler's <installFolder>. For more information about this procedure and the Scheduler in general, see [Use Logi Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/1500009532181-Use-Logi-Scheduler).

## Schedule Task Databases

The Scheduler Service for .NET normally stores its scheduled task data using an embedded instance of **VistaDB,** a text-based database; for the Scheduler Service for Java, an embedded instance of **Apache Derby** is used.

In v11, the option of storing the data instead in a networked **Microsoft SQL Server**, **Oracle**, or **MySQL** database was introduced. In order to use one of these SQL database servers, you must first create the Tasks table in a database of your choice, and then configure the Scheduler's \_Settings.lgx file appropriately, as described in [Use Logi Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/1500009532181-Use-Logi-Scheduler). Example SQL scripts for creating
the Tasks table on each of the supported database servers are installed with the Scheduler in its <installFolder> for your use.

## Multiple Scheduler Instances

Support for storing task data in networked databases, available beginning in v11, allows **multiple instances** of the Scheduler service to run at the same time, on multiple servers, creating a fault-tolerant configuration. If one of the Scheduler instances goes down, the remaining instances will continue to function. Having multiple Scheduler service instances will *not* result in a task being run more often than its designated frequency. The Scheduler service can be installed independently
of the full Logi Info product.

A multi-instance configuration is *not* supported when using the standard embedded VistaDB (.NET) or Derby (Java) databases.

For the purposes of interacting with multiple Scheduler service instances from a Logi application, the application's \_Settings definition must be properly configured to address all of the instances. This is discussed in [Use Logi Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/1500009532181-Use-Logi-Scheduler).

## Quick and Easy Report Scheduling

Developers or administrators who just want to run Logi applications on a scheduled basis can do so by:

1. Installing the Logi Scheduler
2. Downloading the [Scheduler Console Sample Application](https://devnet.logianalytics.com/hc/en-us/articles/360050242853-Scheduler-Console-Sample-Application) from DevNet
3. Registering the sample application with your web server via Logi Studio
4. And running it to create and manage Scheduler tasks.
