---
title: "Installing the Scheduler Service"
id: 5281624674327
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281624674327-Installing-the-Scheduler-Service
updated_at: 2023-04-03T17:52:19Z
---

# Installing the Scheduler Service

# Installing the Scheduler Service

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> The version and build number of the **Scheduler Service** must match that of the **Web Application**. Due to this requirement, Scheduler Service’s must run on the same operating system as their corresponding Web Application servers.

You may have different installations of Exago with different versions/builds on separate servers. The Scheduler Service installation wizard allows you to install multiple Schedulers to maintain corresponding version/builds with the Web Application.

Use the following steps to install the Scheduler Service:

1. [Download the latest Windows or Linux installers](https://support.exagoinc.com/hc/en-us/categories/202053837).
2. Make sure any anti virus is software disabled and run the installation wizard as an Administrator.

### For Windows

1. Click the **Scheduler** button.
2. Click **Next** to bring up the ‘Select Installation Location’ menu.
3. Specify if you want to create a new service or if you want to update an existing one.
4. To create a new service set a name and location.
5. Select to who the Exago Scheduler Windows Service will be installed. By default, “Everyone” is selected. Click **Next**.
6. Confirm the location selections by clicking **Next**
7. Monitor the installation and click **Finish** when it is complete.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> As of *v2016.2.12*, schedulers take system resources into account when assigning remote execution jobs. This requires that the services have read access to the system registry. This can be done by adding the services to the **Performance Monitor Users** group. See [How to Read Performance Counters Without Administrator Privileges](https://blogs.msdn.microsoft.com/bclteam/2006/09/08/how-to-read-performance-counters-without-administrator-privileges-ryan-byington/) (MSDN) for details.

### For Linux

If electing to install the Scheduler Service, the installer creates the sub directory **Scheduler** in the previously specified install path.

Follow the instructions in the [Installing Exago on Linux](https://devnet.logianalytics.com/hc/en-us/articles/5281601243031-Installing-Exago-on-Linux) to install the Service. To configure the Service, continue to [Scheduler Service Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281627554583-Scheduler-Service-Configuration)
