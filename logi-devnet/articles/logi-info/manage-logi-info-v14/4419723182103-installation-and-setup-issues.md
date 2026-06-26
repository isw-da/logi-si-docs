---
title: "Installation and Setup Issues"
id: 4419723182103
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419723182103-Installation-and-Setup-Issues
updated_at: 2022-07-17T01:36:48Z
---

# Installation and Setup Issues

# Installation and Setup Issues

The following issues should be considered if you have problems installing or
upgrading your Logi products:

* **The installation behaves strangely**  
   When installing Logi Analytics products, you must be logged into your
  computer as an Administrator or use the "Run As Administrator"
  option when executing the installation file. Otherwise, files and
  folders may not be installed correctly. If the product was installed
  using a non-administrative account, login as an Administrator, re-run
  the Logi installation file (right-click then "Run As
  Administrator") and uninstall your Logi product, and then reinstall
  it using the same technique.
* **Application can't be found on the web server**  
   Within Logi Studio, "registering" a Logi application on the
  web server creates a "web application" or "virtual
  directory". Some user accounts may not have the appropriate
  permissions to do this. That may be the case if you attempt to register
  your application and nothing happens at the server. There are two
  alternate ways you can register your application and both require that
  you login to the web server: 1) launch the Logi Server Manager tool on
  the server and then use the "Add an Application" button to
  register it; or 2) launch the web server's management application and
  manually create a new virtual directory for your application.
* **Error: "You are not authorized to view this page"**  
   If you receive this error while browsing a report application, make sure
  "Default.aspx" appears in the list of default documents in the
  virtual directory for your application. Also ensure that file system
  permissions are configured properly.
* **Can't run Logi applications on my development computer**  
   Your Logi applications must be registered with the web server and
  (Windows app) .NET 4.x, or the (Java app) Oracle JDK or OpenJDK 8, 11,
  12, 13, 14 must be installed to run reports locally. Use the Server Manager
  tool or run the registration wizard. Ensure that *localhost* is
  specified as the server name.
    
    
  ![](https://devnet.logianalytics.com/hc/article_attachments/4419706599319/criticalicon.png)
  Oracle has changed its Java usage policies -see
  [Java Usage Policy](https://devnet.logianalytics.com/hc/en-us/articles/4419723053335-Java-Usage-Policy) for important information.
* **Applications won't run on my Apache-Tomcat server**  
   Logi applications can be built to use either .NET or Java runtime
  libraries; be sure that you have used the correct version for your
  server OS. On a Windows platform, .NET applications are intended to run
  on a web server that supports ASP.NET extensions so, generally, you must
  use Microsoft's Internet Information Server (IIS) or Cassini web server.
  On both Windows and Linux/UNIX platforms, Logi Java applications can be
  used with a variety of Java-based web servers; see [System Requirements - Logi Info](https://devnet.logianalytics.com/hc/en-us/articles/4419715478551-System-Requirements-Logi-Info-) for more information. Logi Java applications will not run on
  Apache by itself; the Tomcat container is needed to run required
  servers.
* **How do I upgrade Logi applications?**  
   You must install the new version of Logi Info, which will not overwrite
  any files you've edited, by running its installation program. Then, you
  must also change the version of each of Logi Info application you've
  created, using tools found in Logi Studio. When you open an application
  in Logi Studio, you will find a **Change Version** link in its
  Application tab that allows you to upgrade the current application. To
  upgrade multiple applications simultaneously, use a utility called Logi
  Server Manager (see the Studio Tools menu). For more information about
  upgrading products and changing versions see
  [Logi Product Upgrades](https://devnet.logianalytics.com/hc/en-us/articles/4419715502487-Logi-Product-Upgrades).
