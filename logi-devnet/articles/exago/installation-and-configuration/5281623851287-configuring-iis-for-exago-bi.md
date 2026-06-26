---
title: "Configuring IIS for Exago BI"
id: 5281623851287
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281623851287-Configuring-IIS-for-Exago-BI
updated_at: 2023-04-03T17:52:19Z
---

# Configuring IIS for Exago BI

# Configuring IIS for Exago BI

This guide covers the IIS configuration details necessary in order to install Exago BI. First-time users are highly encouraged to use this guide during their installation process. Following these steps in order will reduce the amount of troubleshooting necessary to get Exago running.

1. [Install Prerequisites](#1.)
2. [Install Exago](#2.)
3. [Set the Application Pool](#3.)
4. [Set Folder Paths and Permissions](#4.)
5. [Check that the Web Site is Running](#5.)
6. [Open the Admin Console](#6.)

---

This accompanying video is from the Technical Training Series. To see the other videos in this series, start with the [Introduction to Technical Training Series](https://devnet.logianalytics.com/hc/en-us/articles/5281571861783-Introduction-to-Technical-Training-Series).

---

## 1. Install Prerequisites

Exago BI requires the following Windows Features to be installed:

* Internet Information Services
  + Web Management Tools
    - IIS Management Console
  + World Wide Web Services
    - Application Development Features
      * .NET Extensibility
      * ASP.NET
      * ISAPI Extensions
      * ISAPI Filters
    - Common HTTP Features
      * *Optional:* WebDAV Publishing

Before installing Exago BI, ensure that these features are present on the system. To verify, access the Windows Features panel via **Control Panel** > **Programs** > **Programs and Features**, and click **Turn Windows features on or off**.

![programs_dialog.png](https://devnet.logianalytics.com/hc/article_attachments/5432247011607/programs_dialog.png)

In the Windows Features dialog, expand **Internet Information Services** and ensure that the prerequisite features are selected. If any are not installed, check the relevant boxes, press OK, then restart the server.

![Windows_Features_2017-09-08_09.17.38.png](https://devnet.logianalytics.com/hc/article_attachments/5432126656407/windows_features_2017-09-08_09.17.38.png)

These features are necessary in order for the proper Application Pools to be available.

## 2. Install Exago BI

At this point, install Exago BI on the server. See **[Installing Exago on Windows](https://devnet.logianalytics.com/hc/en-us/articles/5281601433239-Installing-Exago-on-Windows)**.

## 3. Set the Application Pool

Verify that Exago BI is using a valid application pool.

Open IIS Manager via **Control Panel**> **Administrative Tools** > **Internet Information Services (IIS) Manager**.

In the Connections pane, select the Exago BI application.

![](https://devnet.logianalytics.com/hc/article_attachments/5432218094103/iis_exago.png)

In the right-most Actions pane, click on **Advanced Settings…**

![](https://devnet.logianalytics.com/hc/article_attachments/5432247066519/advanced_settings.png)

In this menu, click on the **[…]** button to the right of the **Application Pool**.

![mceclip3.png](https://devnet.logianalytics.com/hc/article_attachments/5432262542615/mceclip3.png)

In the **Select Application Pool** menu, determine which of the app pools has the properties:

* .Net Framework Version: 4.5
* Pipeline mode: Integrated

![mceclip0.png](https://devnet.logianalytics.com/hc/article_attachments/5432126733207/mceclip0.png)

Select this app pool, then press **OK** to close the App Pool menu, and then **OK** to close the Settings menu.

Next, ensure that the app pool is running. In the left-most Connections pane, select **Application Pools**.

![](https://devnet.logianalytics.com/hc/article_attachments/5432247154839/iis_app_pools.png)

Check the **Status** column for the selected app pool.

![mceclip2.png](https://devnet.logianalytics.com/hc/article_attachments/5432280584727/mceclip2.png)

If it does not say ***Started***, select the app pool and in the right-most Actions pane, press **Start**.

![](https://devnet.logianalytics.com/hc/article_attachments/5432126784407/start_app_pool.png)

## 4. Set Folder Paths and Permissions

Exago BI uses a Temp and Report (*pre-v2020.1*) folders to store working data and the reports file system, respectively. Create folders in locations suitable for the environment.

The **Reports** folder should not be within the Exago application directory. This could cause timeout errors while using the application.

The **Temp** folder may contain sensitive report and database information. It should be in a secure location, inaccessible to web users.

Several Exago folders require you to set additional permissions for the application pool user. First, determine the user: Open IIS to the Application Pools pane, and look at the app pool which is running Exago. The Identity property indicates the application user:

![mceclip5.png](https://devnet.logianalytics.com/hc/article_attachments/5432247217175/mceclip5.png)

By default, this is set to *ApplicationPoolIdentity*. This corresponds with the built-in user *IIS\_IUSRS*. If this is a different user, then set permissions for that user account instead.

The following folders require the app pool user to have read/write permissions:

* Config
* Temp
* MapCache
* Reports (*pre-v2020.1*)
* ApplicationThemes (*v2020.1.3+*)

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This process may differ slightly depending on the version of Windows. For a list of supported operating systems, see [Technical Specifications](https://devnet.logianalytics.com/hc/en-us/articles/5281616408727-Technical-Specifications)

First, right-click on the folder and select **Properties**.

![](https://devnet.logianalytics.com/hc/article_attachments/5432242520727/folder_properties.png)

Open the **Security** tab. Then click the **Edit…** button.

![](https://devnet.logianalytics.com/hc/article_attachments/5432262762647/security.png)

If the application pool user is not available to select, you need to add it. Press the **Add…** button.

![](https://devnet.logianalytics.com/hc/article_attachments/5432126874391/add_security.png)

Then enter the user name in the dialog box, and press OK (the default app pool user is *IIS\_IUSRS*).

![](https://devnet.logianalytics.com/hc/article_attachments/5432126885143/iis_iusrs.png)

With the user selected, check the box for Allow **Full control**. Then press OK.

![](https://devnet.logianalytics.com/hc/article_attachments/5432126895127/full_control.png)

Repeat this process for every folder listed above.

## 5. Check that the Web Site is Running

Before starting Exago BI, ensure that the Web Site is running. Open IIS, and in the Connections pane, locate and select the web server under which Exago BI was installed

![](https://devnet.logianalytics.com/hc/article_attachments/5432247352727/iis_server.png)

Verify in the right-most Actions pane that the **Start** button is unavailable, and the **Restart** and **Stop** buttons are available. If the **Start** button is not grayed out, press it to start the web server.

![](https://devnet.logianalytics.com/hc/article_attachments/5432262882455/server_running.png)

Next, in the left-most Connections pane, locate and select the web site under which Exago BI was installed.

![](https://devnet.logianalytics.com/hc/article_attachments/5432126931607/iis_web_site.png)

Verify in the right-most Actions pane that the **Start** button is grayed out, and the **Restart** and **Stop** buttons are available. If the **Start** button is not grayed out, press it to start the web site.

![](https://devnet.logianalytics.com/hc/article_attachments/5432262953751/web_site_running.png)

## 6. Open the Admin Console

You’re almost done! To verify that Exago BI was installed correctly, open a web browser and navigate to `http://[ServerAddress]/[ExagoVirtualPath]/Admin.aspx`. If you see the **Admin Console**, then the installation was successful.

In the **Admin Console** > **General Settings**, set your Temp and Reports paths to the folders you previously created. Then click **Okay**.

For versions *v2020.1+*:

Setup the **Storage Management** for storing reports, templates and themes.

* [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction)
* [Storage Management: Getting Started](https://devnet.logianalytics.com/hc/en-us/articles/5281653081111-Storage-Management-Getting-Started)
* [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management)

Finally, navigate to `http://[YourServerAddress]/[YourExagoVirtualPath]/ExagoHome.aspx`. If you can see the Exago BI Web Application user interface, depending on version the Report Tree should be:

* empty for versions *pre-v2020.1*
* empty except for a **My Reports** and **Public** folder for versions *v2020.1+*

Congratulations! The Exago BI installation is complete!

## Additional Notes

We highly recommend [Setting up a State Server](https://devnet.logianalytics.com/hc/en-us/articles/5281581463959-Setting-up-a-State-Server) to handle Exago BI sessions.

If you need more information, contact [Exago Support](https://help.insightsoftware.com/s/contactsupport?language=en_US "Exago support").
