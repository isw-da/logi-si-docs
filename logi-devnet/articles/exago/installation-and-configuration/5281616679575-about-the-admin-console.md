---
title: "About the Admin Console"
id: 5281616679575
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281616679575-About-the-Admin-Console
updated_at: 2023-04-03T17:52:19Z
---

# About the Admin Console

# About the Admin Console

The Exago **Administration Console**, or **Admin Console** for short, serves as a user interface to set up and save administrative preferences. Use the Admin Console to create and modify a base session configuration file, including:

* [Configuration File Options and Optimizations](https://devnet.logianalytics.com/hc/en-us/articles/5281626054679-Configuration-File-Options-and-Optimizations) — Implement a static/dynamic configuration
* [Storage Management](https://devnet.logianalytics.com/hc/en-us/articles/5281661421719-Storage-Management) — Configure report, theme, folder and template file storage
* Data — Establish how to connect to data sources and determine what data should be exposed to users. Configure system-wide variables called **Parameters**. See [Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/5281617045911-Data-Sources), [Data Objects](https://devnet.logianalytics.com/hc/en-us/articles/5281608202519-Data-Objects) and [Parameters](https://devnet.logianalytics.com/hc/en-us/articles/5281625630615-Parameters).
* General — Modify global settings of Exago to enable or disable features.
* [Roles](https://devnet.logianalytics.com/hc/en-us/articles/5281625714967-Roles) — Create and modify security **Roles** for individuals or groups of users.
* Extensions
  + [Custom Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281628193815-Custom-Functions) — Create and modify custom functions to make calculations on reports.
  + [Custom Aggregate Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281616754327-Custom-Aggregate-Functions) — Create and modify custom aggregate functions.
  + [Custom Filter Functions](https://devnet.logianalytics.com/hc/en-us/articles/5281644078487-Custom-Filter-Functions) — Create and modify custom filter functions
  + Server Events — Create and modify custom code that is run when reports execute. See [Introduction to Server Events](https://devnet.logianalytics.com/hc/en-us/articles/5281583100439-Introduction-to-Server-Events).
  + Action Events — Create and modify custom code that activates when a certain condition in the application is met. See [Introduction to Action Events](https://devnet.logianalytics.com/hc/en-us/articles/5281598603671-Introduction-to-Action-Events).
  + [Custom Options](https://devnet.logianalytics.com/hc/en-us/articles/5281625285911-Custom-Options) — Create and modify custom options that can be set on reports.

## Accessing the Admin Console

Once Exago is installed, navigate with a web browser to **`http://<Server>/<Exago Web Alias>/Admin.aspx`**.

It is recommended to protect access to the **Admin Console** by setting values for the **General** > **Other Settings** > **User ID**, **Password** and **Confirm Password** settings. Subsequent access to the Admin Console requires the user name and password be provided to gain access.

![Admin Console login dialog](https://devnet.logianalytics.com/hc/article_attachments/5432216947607/admin-console-login-2.png)

Admin Console login dialog in *v2021.2+*

After making changes in the Admin Console, click the **Logout** button in the top-right corner to lock the Admin Console back out.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> The **Logout** button only appears when either the **General** > **Other Settings** > **User ID** or **General** > **Other Settings** > **Password** (or both) are set. For more information, see the [Other Settings](https://devnet.logianalytics.com/hc/en-us/articles/5281608505879-Other-Settings) topic.

Once Exago is configured and working, access to the Admin Console should be completely disabled. The Admin Console should never be accessible in a production environment. For more information, review the [Security Checklist](https://devnet.logianalytics.com/hc/en-us/articles/5281588834455-Security-Checklist).

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Critical")
>
> Aside from the obvious security concerns by exposing the Admin Console in production, any changes made to the system configuration will invalidate all current user sessions causing an unsatisfactory user experience. For more information, review [Modifying Configs in a Production Environment](https://devnet.logianalytics.com/hc/en-us/articles/5281619727383-Modifying-Configs-in-a-Production-Environment).

## Navigation

The **Admin Console** consists of two sections. On the left is the **Main Menu** and on the right are **Tabs** that can contain menus to create and modify the configuration file.

![firefox_OW56SCWOEJ.png](https://devnet.logianalytics.com/hc/article_attachments/5432241211287/hk0odbdxsk.png)

The Exago Admin Console in *v2021.1*

### Main Menu

Through the main menu you can:

* Configure the **Storage Management** system
* Create **Data Sources**, **Data Objects**, **Joins**, **Parameters**, **Roles**, and **Custom Functions**.
* Edit settings for: **Data**, **Roles**, **Functions**, and **General** features.
* Delete **Data Sources**, **Data Objects**, **Joins**, **Parameters**, **Roles**, and **Functions**.
* Automatically discover data source objects and metadata.

Click the **Collapse ![MainLeftPaneSplitter.png](https://devnet.logianalytics.com/hc/article_attachments/5432236046615/mainleftpanesplitter.png)** icon to hide (or restore) the main menu.

### Tabs

The right section of the **Admin Console** is made up of tabs containing menus to create and modify administrative settings.

To save the changes made in a tab click **Apply** or **Okay.**

Tabs can be closed with or without saving by clicking the **Close**![CloseButtonSmall.png](https://devnet.logianalytics.com/hc/article_attachments/5432241264279/closebuttonsmall.png)

![NmSIdpy2rb.png](https://devnet.logianalytics.com/hc/article_attachments/5432217088663/nmsidpy2rb.png)

The General tab can be closed by clocking the X icon to the right of its name in the tab

Tabs may be arranged by clicking and dragging them as desired.

The **Admin Console** creates two base configuration files: an XML file named `WebReports.xml` and an encrypted XML file named `WebReports.xml.enc`. These files are created and saved in the `/Config` sub-directory of Exago’s installation location. It is recommended to use this as the live version of the config in a production environment. Copy `WebReports.xml` to a secure backup, and then delete it from the `Config` directory.

## Creating Additional Configuration Files

As part of the integration of Exago you may want to create alternative configuration files in addition to `WebReports.xml.` Additional configuration files can be utilized in two ways:

* If entering Exago directly, the configuration file to be used is specified in the **Custom Styling.**
* When entering through the API the configuration file to be used is specified in the **API Constructor Methods**.

To create additional configuration files:

1. Navigate to the **Admin Console** in a web browser.
2. Append “*?configFn=NewConfigFile.xml*” to the URL replacing `NewConfigFile` with the desired configuration file name.
3. Click in the URL bar and press enter.
