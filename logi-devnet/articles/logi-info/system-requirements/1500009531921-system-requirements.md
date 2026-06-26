---
title: "System Requirements"
id: 1500009531921
section: "System Requirements"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531921-System-Requirements
updated_at: 2021-06-17T01:58:39Z
---

# System Requirements

# System Requirements

This topic discusses hardware and software requirements for Logi Analytics managed reporting products.

**IMPORTANT**: If you wish to upgrade to JDK 8 release build 261 (1.8.0\_261), or any later build of JDK 8, you will need to replace the mscorlib.jar file in the application folder with the new one and restart your server. The mscorlib.jar file can be found on our [Product Download](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads "Select to access Product Dowload page") page. Please contact Support for additional assistance.

* General Requirements
* [How Should Your Server Be Configured?](#Configured)
* [How Many Servers Do You Need?](#HowMany)
* [Server Virtualization](#Virtualization)

## General Requirements

The following general hardware and software components are supported by the latest releases Logi Info and Logi Report:

| **Browsers:** | - Internet Explorer: 7, 8, 9, 10, 11 (Certified); see note below about earlier versions. - Firefox, Chrome: all current public versions (Supported). - Opera, Safari: all current public versions (Supported). |
| **Hardware:** | - 1 GHz or higher processor recommended; 400 MHz minimum required. - 1 GB or higher RAM recommended; 512 MB of RAM minimum required. - 1 GB of available disk space (with .NET already installed). |
| **Operating Systems:** | - Windows Server 2012 R2, 2008, 2003 - Windows 8 (all editions except RT) - Windows 7 (all editions) - Windows Vista (Business, Enterprise, and Ultimate editions only)  - SUSE, Red Hat, Ubuntu, CentOS, and most flavors of Linux  - Solaris, HP-UX (Limited support)  - 32-bit and 64-bit Windows OS supported - 32-bit and 64-bit Linux OS supported |
| **Web Servers:** | - Microsoft Internet Information Server (IIS) 6.x, 7.x, 8.x - Apache-Tomcat 6, 7, 8 (without Tomcat FHS) - JBoss 4, 5, 7, EAP-6.3 - Sun GlassFish (SJSAS) 2.1, 3.0, 3.1  - BEA WebLogic 10 - Oracle WebLogic 12c - IBM Websphere 7, 8.5 |
| **Other Software:** | The following components *must* be installed:  For Logi Studio and to develop Windows applications: - For Logi products prior to v11.0.127, Microsoft .NET Framework 2.0 or 3.x  - For Logi products v11.0.127 and later, Microsoft .NET Framework 4.x, or  To develop Java applications: - Official Sun Java Development Kit (JDK) 1.6, or  - Official Sun Java Development Kit (JDK) 1.7, 1.8 (non-Apple platforms)  (The JRE is not sufficient but OpenJDK 1.7 and JRockit 1.6 or 1.7 may be used) |
| **Data Sources:** | Logi Info and Logi Report can use any of the following data sources/services:  - Amazon SimpleDB - DB2 database server - Files: Excel, CSV, XML, JSON - Google Docs - Google Maps - HP Vertica - JDBC-compliant database servers - Microsoft Access - Microsoft SQL Server - Microsoft SQL Server Analysis Services (OLAP) - MongoDB - MySQL database server - ODBC-compliant database servers - OLEDB-compliant database servers - JDBC-compliant database servers - Oracle database server - PostgreSQL database server - Salesforce.com - SMTP email servers - Sybase database server - Twitter.com - Web Services (REST and SOAP) |

**Notes:**

Microsoft Internet Information Server (IIS) must be installed *before* installing Logi products. Logi products for the Windows environment, and Logi Studio, require the .NET Framework. Prior to v11.0.127, .NET v2.0 or 3.x was required; for v11.0.127 and later, .NET 4.x is required. If not already in place, with your consent, appropriate versions of the .NET Framework are installed when Logi products are installed. They are also available for free from the [Microsoft Download Center](http://www.microsoft.com/en-us/download/developer-tools.aspx?q=developer+tools).

**Linux Users**: More information about Java is available in [Introduction to Logi Reporting with Java](https://devnet.logianalytics.com/hc/en-us/articles/1500009531261-Introduction-to-Logi-Reporting-with-Java).

**Internet Explorer 10** is supported in v11.0.519 (14 June 2013), and later.

**Internet Explorer 5** and **6** are no longer considered "modern" browsers, meaning that they have limited support for the current standard browser technologies, including CSS2, Javascript, and AJAX. Without this support, in Logi applications certain style and visual elements will render incorrectly, transparent backgrounds for charts and other image-related content will be impaired, and problems using features such as our Dashboards and interactive pagination controls will occur.
Major websites, including
Amazon, Google Apps, and YouTube no longer support these browsers, and Microsoft has declared their lifecycle ended.

**Browser updates** are being released so rapidly that it's impossible for us to guarantee that all browser versions will work on a day-to-day basis, or that a new browser release won't be incompatible with an older version of Logi products.

## How Should Your Server Be Configured?

In a typical scenario with an average data size per report (less 10MB of data per report), you should be able serve 50-100 concurrent users per multi-core CPU on a production server, assuming a good amount of RAM (2GB+) and a fast hard drive (12K RPM+). Here are three representative configuration levels for the web server.

A low-performance hardware configuration:

1 multi-core CPU, 1-2GB RAM, 12K RPM HD, 32-bit OS

A better performance configuration (for more users or more data):

Quad-Core CPU, 2-4GB+ RAM, 15K RPM HD, 32-bit OS

The best performance configuration begins with the previous configuration and adds:

        Additional CPUs (2 or more Quad-Core CPUs), more RAM (8GB+), 64-bit OS, or move to a clustered environment.

Here are a few general "rules of thumb" when considering server configuration options:

* More Data and Data Complexity = More RAM
* More Reports, Larger Reports, Complex Reports = Faster hard disk, more available hard disk space
* More Traffic and Concurrent Visitors = More CPUs/Cores

## How Many Servers Do You Need?

Your production web server hosts your Logi applications, which run as extensions to the web server. Ideally, this computer should be dedicated to this task alone.

However, other configurations are possible and feasible, including those in which the web server also serves other functions (i.e. is not dedicated to reporting alone) and/or the database server is also on the reporting server computer.

Which configuration should you use? We do not have guidelines based on specific numbers of users or reports to share with you; each deployment situation is different.

Whether you choose to combine functions (web server, Logi application, and database server) on one computer is, ultimately, your decision. Numerous factors can affect this decision, including the amount of web server traffic, the number of concurrent database users, the size of the databases, the complexity of the database queries, the
frequency of
report access, and, not least, cost.

You may care to begin with a combined configuration and, as your report usage grows, change to a dedicated configuration. The nature of Logi products allows you to do this easily and often without additional cost (if per-server CPU counts remain constant).

Recent studies concerning server virtualization suggest that database servers are frequently under-utilized. On the other hand, many database vendors recommend that their products be run on a dedicated server. You may wish to check with your database vendor for their recommendations concerning database servers.

## Server Virtualization

Many organizations are using server virtualization to maximize hardware usage and reduce costs.

Server virtualization products allow the assignment of CPU resources to processes. This may take the form of a maximum percentage of combined CPU utilization, or as specific allocation of logical CPUs, to a virtual machine (VM). The server administrator is responsible for making these configuration decisions. Logi Analytics' product licenses treat a VM just like a regular, non-virtualized server.

In order to ensure good performance in any virtualized server environment, administrators must be careful to allocate appropriate resources to VMs.

It's not uncommon to relocate a VM from one hardware platform to another, for example, for hardware maintenance. The Logi license will "move" with the VM, as long as the machine name remains unchanged.
