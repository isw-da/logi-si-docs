---
title: "Use the IIS Express Web Server"
id: 1500009532161
section: "Install Logi Info/Logi Report"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009532161-Use-the-IIS-Express-Web-Server
updated_at: 2021-06-17T01:58:42Z
---

# Use the IIS Express Web Server

# Use the IIS Express Web Server

Beginning with v11.0.519, Logi Info and Logi Report include the compact, .NET-based web server **IIS Express**. When you run its New Application wizard to create a new .NET Logi application, Logi Studio will offer to install this web server on your computer if it detects that no other web server has been installed. This topic discusses this web server in more detail.

* About the IIS Express Web Server
* [Instal IIS Express](#Installing)
* [Manage Applications](#Managing)
* [Remove IIS Express](#Removing)

Prior to v11.0.519, the Cassini .NET web server was included. For more information, see [Use the Cassini Web Server](https://devnet.logianalytics.com/hc/en-us/articles/1500009532101-Use-the-Cassini-Web-Server).

## About the IIS Express Web Server

The IIS Express web server is a compact version of Microsoft IIS. It's available for free from Microsoft and Logi Analytics has chosen to distribute it with Logi Info and Logi Report, v11.0.519 and later.

IIS Express is a light-weight web server that's ideal for development purposes. It runs as a Windows application (not a service) and is compatible with most modern flavors of Windows, including all editions of Windows XP, Vista, Windows 7, Server 2003 SP2, Server 2008, and Server 2008 R2. It requires .NET 4.0 and does not require Administrator privileges to perform most tasks.

IIS Express is an ideal solution for developers or evaluators who do not want to, or cannot, install IIS on their development or evaluation computers. However, IIS Express is not suitable as a production web server as it has some performance and security limitations.

Complete information about [IIS Express](http://www.iis.net/learn/extensions/introduction-to-iis-express) is available from Microsoft.

## Install IIS Express

Please note that, although it's included with the product, IIS Express is *not* automatically installed when Logi Studio is installed. Developers who have no need of IIS Express (i.e. those who have IIS installed already) will never see it.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif) If you have regular IIS installed and decide to "turn it off" in Control Panel in order to see how IIS Express works, when you turn it back on later you may not have all of your IIS custom Application Pools and Virtual Directories restored! If that happens, they can be restored as part of a general System Restore Point restore operation (assuming you have a recent Restore Point saved). This is not
something
we recommend, in general, so if you must do it, do it on a dedicated test machine, not your development or production machine.

The first time Logi Studio is used to create a new application (by selecting File ![](https://logianalytics.zendesk.com/hc/article_attachments/4402778416151/menuarrow.gif) New Application... from Studio's main menu), its New Application wizard will determine whether IIS is installed on the computer where Studio is installed.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771559191/iisexpress_01.png)

If Studio can't detect an IIS installation, the dialog box above will be displayed. The user can then decide whether to install IIS Express or IIS.

Why would anyone decide to use IIS Express instead of IIS?

* IIS Express, as installed by Studio, is configured and ready to go immediately and does not need the additional configuration IIS requires.
* IIS Express can be installed and administered by users who do not have Admin privileges on their computer.
* IIS Express can be easily uninstalled when no longer needed.

If you decide to install IIS Express, click **Install IIS Express**, as shown above, and a separate installer is launched:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778478999/iisexpress_02.png)

As shown above, you'll need to accept the License Agreement and click **Install**.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771559447/iisexpress_03.png)

Once the installation starts, progress will be displayed in the dialog box shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778479255/iisexpress_04.png)

When the installation is complete, click **Finish** to return to Studio's New Application wizard.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771559703/iisexpress_05.png)

Once IIS Express is installed, Studio becomes aware that it's dealing with IIS Express and not IIS, and it adjusts its prompts, wizards, and activities to be compatible with IIS Express, as shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771559959/iisexpress_06.png)

Once the wizard finishes, the only difference you can see in your report will be in its \_Settings definition. The **Path** element's **Application Path** attribute will have a an address value similar to the one shown above. The high-lighted part is a port number, which will be different for each Logi app you create.

Your Logi applications will be displayed just as they would if you had regular IIS installed: you can preview them in Studio and browse them by using the Studio browse button and link or by entering their URL in an independent browser window.

## Manage Applications

You can see what applications are running on IIS Express using a tool that's available in the System Tray:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771560215/iisexpress_07.png)

The IIS Express icon is shown above. If you don't see the icon in your System Tray, click the Hidden Icons button. Right-click this icon to see the context menus shown below:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778479511/iisexpress_07a.png)

These menus allow you to view applications (web sites) that are running and stop them. This is a great way to re-discover the port number used for each application, for use in a URL, if you forget it.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771560471/iisexpress_08.png)

If you click Show All Applications in the context menu, the dialog box shown above is displayed. It lists the Logi applications running in IIS Express and their details.

## Remove IIS Express

IIS Express can be removed from your computer using the standard Windows Control Panel **Programs and Features** applet:

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778479767/iisexpress_10.png)

If you subsequently wish to use your Logi applications with IIS, be sure to check that your Application Path, in the \_Settings definition, is correct after registering the application with IIS through Studio.
