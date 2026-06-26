---
title: "Configure InfoGo for Developers"
id: 4419722760343
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722760343-Configure-InfoGo-for-Developers
updated_at: 2022-07-17T02:08:39Z
---

# Configure InfoGo for Developers

# Configure InfoGo for Developers

InfoGo is a complete Logi application distributed with the Self-Service Reporting Module. It provides a complete self-service reporting experience for users.

The following topics discuss how to configure the application after it's been installed:

* [Upgrade Considerations](https://devnet.logianalytics.com/hc/en-us/articles/4419715174167-Upgrade-Considerations#Considerations)
* [Completing the Installation](https://devnet.logianalytics.com/hc/en-us/articles/4419722758423-Completing-the-Installation#Installation)
* [Integrating the Discovery Module](https://devnet.logianalytics.com/hc/en-us/articles/4419715171223-Integrating-the-Discovery-Module#Discovery)
* [Specifying Application Metadata](https://devnet.logianalytics.com/hc/en-us/articles/4419715173143-Specifying-the-Application-Metadata#Metadata)
* [Configuring Scheduler and SMTP Services](https://devnet.logianalytics.com/hc/en-us/articles/4419722761239-Configuring-Scheduler-and-SMTP-Services#Scheduler)
* [Managing Scheduled Reports](https://devnet.logianalytics.com/hc/en-us/articles/4419707422743-Managing-Scheduled-Reports#ManagingScheduled)
* [Configuring Security](https://devnet.logianalytics.com/hc/en-us/articles/4419722762263-Configuring-Security#Security)
* [Configuring InfoGo Constants](https://devnet.logianalytics.com/hc/en-us/articles/4419722759447-Configuring-InfoGo-Constants#Constants)
* [Enabling Panel Content Editing](https://devnet.logianalytics.com/hc/en-us/articles/4419722769431-Enabling-Panel-Content-Editing)
* [Setting Up Sharing](https://devnet.logianalytics.com/hc/en-us/articles/4419715172247-Setting-Up-Sharing-#Sharing)
* [Designating a Global Main Page](https://devnet.logianalytics.com/hc/en-us/articles/4419722765207-Designating-a-Global-Main-Page#MainPage)
* [Creating a Global Menu](https://devnet.logianalytics.com/hc/en-us/articles/4419722763159-Creating-a-Global-Menu#GlobalMenu)
* [Working with Gallery Files](https://devnet.logianalytics.com/hc/en-us/articles/4419707423895-Working-with-Gallery-Files#Gallery)
* [Customizing Appearance](https://devnet.logianalytics.com/hc/en-us/articles/4419707420567-Customizing-Appearance#Appearance)
* [Customizing InfoGo Files](https://devnet.logianalytics.com/hc/en-us/articles/4419722764311-Customizing-InfoGo-Files#Files)
* [Embedding InfoGo](https://devnet.logianalytics.com/hc/en-us/articles/4419707421719-Embedding-InfoGo#Embedding)

## About the InfoGo Application

Introductory information about the **Self-Service Reporting Module** (SSRM) and directions for installing it can be found in [Install the Self-Service Reporting Module](https://devnet.logianalytics.com/hc/en-us/articles/4419707632407-Install-the-Self-Service-Reporting-Module). If you haven't read it already, we recommend you do so before proceeding.

The SSRM includes a complete Logi application, **InfoGo**. It allows users to create and share visualizations, Dashboards, and reports at runtime, and can be used as is or as a template for your own applications.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png)

* Unlike the Sample Applications on DevNet, InfoGo is distributed complete with Logi Engine files - these include required code and you should *not* downgrade this application to an earlier engine version or it may cease to work.
* InfoGo is an extremely advanced example of Logi Info programming. It uses highly customized code and specialized techniques that may not work if copied into other Logi applications. While you can customize some portions of it, pulling it apart and reusing code in other applications, as you might with a regular Logi Sample Application, may not work well.

### Deployment Strategies

You *can* use the InfoGo application right where it was installed, configuring and modifying it right in its installation location. The default installation location is C:\Program Files\Logi Analytics\InfoGo. However, this approach requires extreme vigilance when applying Logi upgrades and is therefore dangerous.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Our Best Practices recommendation is that you *not* run the program from there. Instead, leave those files *untouched* and use them as your "reference model", a pristine set of files that can be copied whenever needed to new applications in other locations (such as C:\inetpub\wwwroot) for customization,
registration, and use
with your web server. As with any Logi app, you can deploy instances using the Application Deployment tool in Logi Studio.

#### Java Application

For example, if you want to deploy InfoGo as a Java-based application:

1. Install the SSRM, including the InfoGo application, as usual.
2. Use Logi Studio to create a new Java application.
3. Copy all the folders and their contents from the installed InfoGo application root folder to the new Java application root folder, except bin and rdTemplate.
4. Copy InfoGoReportManagementPlugin.jar from the applications \_SupportFile folder to the new Java application's WEB-INF\lib folder.
5. Ensure that the copied folders have inherited the file access permissions of the Java application root folder.

Configure the Java application as described in this topic, and make any customizations you desire.

#### .NET Application

If you want to deploy InfoGo as a .NET-based application:

1. Install the SSRM, including the InfoGo application, as usual.
2. Use Logi Studio to create a new .NET application.
3. Copy all the folders and their contents from the installed InfoGo application root folder to the new .NET application root folder, except bin and rdTemplate.
4. Give full control to IIS\_IUSRS on the .NET application root web folder (and its subfolders).
5. Ensure that the copied folders have inherited the file access permissions of the .NET application root folder.

Configure the .NET application as described in this topic, and make any customizations you desire.
