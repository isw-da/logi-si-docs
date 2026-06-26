---
title: "Studio's Configuration Steps"
id: 4419707945879
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707945879-Studio-s-Configuration-Steps
updated_at: 2022-07-17T01:30:31Z
---

# Studio's Configuration Steps

# Studio's Configuration Steps

Logi Studio attempts to register a Logi application with the IIS web
server when:

* You create a new application using Studio's
  **New Application** wizard, or
* You click the **Register** link in Studio's Workspace Application
  tab, or
* You download a DevNet **Sample** application.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707160215/iisreg_01.png)

Logi applications are registered in IIS as a *web application*. A
web application equates a URL with the physical location of application
files and folders on the file system. Logi applications, like other web
applications registered in IIS, are accessible from a web browser using
their *virtual path*.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png)
The Logi Studio registration wizard only configures Logi
applications under the **Default Web Site** section of IIS. See the
manual instructions in one of the following sections in order to create an
application under other IIS web sites you may have defined, or if you have
renamed the Default web site.

You must be logged-in with an account that has administrator privileges at
the time Studio attempts the registration; admin privileges are required
in order to create and configure an IIS application.

![](https://devnet.logianalytics.com/hc/article_attachments/4419707160471/iisreg_02.png)

As shown above, in the **IIS 10 Manager** tool, application pools,
sites, applications, and folders are listed on the left. Removing an
application or virtual directory from the list *does not* remove the
physical application folder and files from your drive.
Studio's registration wizard accomplishes the following:

* If the appropriate version of the .NET framework is not present, it will
  be installed, with your consent, and configured for the web server.
* If it's not already running, the Default Web Site will be started.
* A new web application will be created pointing to the Logi application
  folder.
* The new application will have its .NET version set appropriately.
* The local Windows account "Everyone" will be given Full
  Control file access permissions to the standard Logi application folders
  rdDataCache and rdDownload in the application.
* The application pool's Managed Pipeline Mode will be configured as
  Integrated mode. and Application Pools that use .NET 4.x are required.
  If such an application pool doesn't exist, Studio will generate a
  warning when you upgrade an existing Logi application. When you create a
  new application, Studio will create a new application pool, named
  "Logi Info .Net v4.x", and will assign the application to it.

The following topics provide instruction for accomplishing some of these
tasks manually, in case a situation occurs in which this is necessary, or
in case developers which to ensure that the correct configuration did in
fact occur.
