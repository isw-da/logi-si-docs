---
title: "Use the Cassini Web Server"
id: 1500009532101
section: "Install Logi Info/Logi Report"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009532101-Use-the-Cassini-Web-Server
updated_at: 2021-06-17T01:58:42Z
---

# Use the Cassini Web Server

# Use the Cassini Web Server

The installer for Logi Info and Logi Report includes a compact .NET-based web server named **Cassini**. Logi Studio will offer to install this web server on your computer if it detects that no other web server exists there. This topic discusses this web server in more detail.

* About the Cassini Web Server
* [Install Cassini](#Installing)
* [Manage Hosted Applications](#Managing)
* [Remove Cassini](#Removing)

## About the Cassini Web Server

The Cassini web server is a compact, re-distributable web server that can host ASP.NET web applications. It was first published by Microsoft as a sample .NET application and Logi Analytics has chosen to distribute an improved version of this server, created by a company called UltiDev.

Cassini is a light-weight web server that's ideal for development purposes. It runs as a Windows service and is compatible with most modern flavors of Windows, including Windows 2000, Windows XP, Windows 2003 Server, Windows Vista, and Windows 7.

Cassini is an ideal solution for developers or evaluators who do not want to, or cannot, install IIS on their development or evaluation computers. However, Cassini is not suitable as a production web server as it has some performance and security limitations.

One difference between Cassini and IIS is that Cassini does not use virtual directories. Instead it assigns individual port numbers to each web application registered with it. A typical URL for a Cassini-hosted web app looks like this:  http://localhost:2741.

## Install Cassini

Please note that, though it's included with the product, Cassini is not automatically installed when Logi Studio is installed. Developers who have no need of Cassini (primarily those who have IIS installed already) will never see it.

The first time Logi Studio is used to create a new application (by selecting File ![](https://logianalytics.zendesk.com/hc/article_attachments/4402778416151/menuarrow.gif) New Application... from Studio's main menu), its New Application wizard will determine whether IIS is installed on the computer where Studio is installed.   
 

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771561495/cassini_01.png)

If Studio can't detect an IIS installation, the dialog box above will be displayed. The user can then decide whether to install Cassini or IIS.

Why would anyone decide to use Cassini instead of IIS?

* Cassini, as installed by Studio, is configured and ready to go immediately and does not need the additional configuration IIS requires.
* Cassini can be installed and administered by users who do not have Admin privileges on their computer.
* Cassini can be easily uninstalled when no longer needed.

If you elect to install Cassini, a separate installer is launched:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778481047/cassini_02.png)

As shown above, you will need to confirm your decision to install Cassini.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771562007/cassini_03.png)

Once the installation starts, progress will be displayed in the dialog box shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771562263/cassini_04.png)

When the installation is complete, click **No** to return to Studio's New Application wizard. The management console mentioned in the dialog box text is also available via the Start Menu and is discussed in the next section of this topic.

Once Cassini is installed, Studio becomes aware that it is dealing with Cassini and not IIS, and it adjusts its prompts, wizards, and activities to be compatible with Cassini.

## Manage Hosted Applications

Cassini is distributed with a browser-based management tool, and it's installed along with Cassini by default.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771562519/cassini_05.png)

The management tool, called the Cassini Web Server Explorer, can be launched from your Start Menu, as shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778481303/cassini_06.png)

The main page of the Cassini Explorer, shown above, lists each web application registered with it, along with some details. This is a great place to discover the port number used for each application, for use in a URL, if that information is lost.

Applications can be registered and unregistered here, and their details can be edited by clicking Edit.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771562775/cassini_07.png)

The Edit page looks like the example shown above. Typically, Studio will handle seeding all the necessary detail information into Cassini, but you can edit it manually here if necessary.

## Remove Cassini

Cassini can be removed from your computer using the standard Windows Control Panel **Add or Remove Programs** feature:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771563031/cassini_08.png)

As shown above, Add or Remove Programs will show two UltiDev entries: one for the management tool app and one for the Cassini server itself. Click **Remove** to uninstall them. Removing the software will not affect your Logi application files.

If you subsequently wish to use your Logi applications with IIS, be sure to check that your Application Path, in the \_settings definition, is correct after registering the application with IIS through Studio.
