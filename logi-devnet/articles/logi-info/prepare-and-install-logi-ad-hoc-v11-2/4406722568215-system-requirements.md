---
title: "System Requirements"
id: 4406722568215
section: "Prepare and Install Logi Ad Hoc v11.2"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406722568215-System-Requirements
updated_at: 2024-05-09T12:13:37Z
---

# System Requirements

# System Requirements

![criticalicon.gif](https://devnet.logianalytics.com/hc/article_attachments/6074426060567)Ad Hoc has reached End of Life and we no longer update or support this product.

This topic discusses hardware and software requirements for Logi Ad Hoc v11. Sections include:

* [General Requirements](#General)
* [How Should Your Server Be Configured?](#Configured)
* [How Many Servers Do You Need?](#HowMany)
* [Server Virtualization](#Virtualization)
* [Product Expiration Information](#Expiration)

![](https://devnet.logianalytics.com/hc/article_attachments/6074426060567) Do not upgrade to JDK 8 release build 261 (1.8.0\_261), or any later build of JDK 8. Doing so affects Logi Info and Logi Ad Hoc running the Java engine. If you perform this upgrade, your web server will stop responding indefinitely the first time it has to process a web request. This issue affects both Oracle JDK 8 and OpenJDK 8. This note will be updated when we have found a resolution.

## General Requirements

Here are the general requirements for Logi Ad Hoc v11:

| Area | Requirement |
| --- | --- |
| **Browsers:** | - Internet Explorer: 7, 8, 9, 10, 11 (Certified); see note below about earlier versions. - Firefox, Chrome: all current public versions (Supported) - Opera, Safari: all current public versions (Supported) |
| **Hardware:** | - 1 GHz or higher processor recommended; 400 MHz minimum required. - 1 GB or higher RAM recommended; 512 MB of RAM minimum required. - 450 MB of available disk space (with .NET already installed). - 800 MB of available disk space (without .NET installed). |
| **Operating Systems:** | - Windows Server 2012 R2, 2008, 2003 - Windows 8 (all editions except RT) - Windows 7 (all editions) - Windows Vista (Business, Enterprise, and Ultimate editions only) - SUSE, Red Hat, Ubuntu, CentOS, and just about any other flavor of Linux  - Solaris, HP-UX (Limited support)  - 32-bit and 64-bit Windows OS supported - 32-bit and 64-bit Linux OS supported |
| **Web Servers:** | - Microsoft Internet Information Server (IIS) - Apache-Tomcat 5.5, 6.0, 7.0 (without Tomcat FHS) - JBoss 4, 5, 7 - Sun GlassFish (SJSAS) 2.1, 3.0, 3.1  - BEA WebLogic 10 - Oracle WebLogic 12c - IBM Websphere 7, 8.5 |
| **Metadata Servers:** | Logi Ad Hoc v11 builds a metadata repository which can be created on any of the following database servers. All are available for .NET, only those with an asterisk (\*) are also available for Java:  - Microsoft SQL Server CE (installed automatically during Logi Ad Hoc v11 installation) - Microsoft SQL Server - MySQL \* - Oracle \* |
| **Other Software:** | The following components *must* be installed:  - Microsoft .NET 2.0, 3.x, or 4.x Framework (.NET 4.x required for v11+), or   - Official Sun Java Development Kit (JDK) 1.6, 1.7, or 1.8  (The JRE is not sufficient but OpenJDK 1.7 and JRockit 1.6 or 1.7 may be used) |
| **Data Sources:** | Logi Ad Hoc v11 can retrieve data for reporting from any of the following database servers. All are available for .NET, only those with an asterisk (\*) are also available for Java:  - DB2 - Informix - Microsoft SQL Server - MySQL \* - Oracle \* - PostgreSQL \* - Sybase |

**Notes:**

Microsoft Internet Information Server (IIS) must be installed *before* installing Logi products. The installation program for Logi reporting tools will, if it doesn't find it, install the .NET 2.0 Framework automatically. There is no need to upgrade to .NET 3.x in order to use Logi products.

**Browser updates** are being released so rapidly that it's impossible for us to guarantee that all versions will work on a day-to-day basis, or that a new browser release won't be incompatible with an older version of Logi Ad Hoc v11.

**Internet Explorer 10** is only supported in v11+.

**Internet Explorer 5** and **6** are no longer considered "modern" browsers, meaning that they have limited support for the current standard browser technologies, including CSS2, Javascript, and AJAX. Without this support, in Logi applications certain style and visual elements will render incorrectly, transparent backgrounds for charts and other image-related content will be impaired, and problems using features such as our Dashboards and interactive pagination controls will occur. Major websites, including Amazon, Google Apps, and YouTube no longer support these browsers, and Microsoft has declared their lifecycle ended.

## How Should Your Server Be Configured?

In a typical scenario with an average data size per report (less 10MB of data per report), you should be able serve 50-100 concurrent users per multi-core CPU on a production server, assuming a good amount of RAM (2GB+) and a fast hard drive (12K RPM+). Here are three representative configuration levels for the web server.

1. A low-performance hardware configuration: 1 multi-core CPU, 1-2GB RAM, 12K RPM HD, 32-bit OS
2. A better performance configuration (for more users or more data): Quad-Core CPU, 2-4GB+ RAM, 15K RPM HD, 32-bit OS
3. The best performance configuration begins with the previous configuration and adds:  Additional CPUs (2 or more Quad-Core CPUs), more RAM (8GB+), 64-bit OS, or move to a clustered environment.

Here are a few general "rules of thumb" when considering server configuration options:

* More Data and Data Complexity = More RAM
* More Reports, Larger Reports, Complex Reports = Faster hard disk, more available hard disk space
* More Traffic and Concurrent Visitors = More CPUs/Cores

## How Many Servers Do You Need?

Your production web server hosts your Logi applications, which run as extensions to the web server. Ideally, this computer should be dedicated to this task alone.

However, other configurations are possible and feasible, including those in which the web server also serves other functions (i.e. is not dedicated to reporting alone) or the database server is also on the reporting server computer.

Which configuration should you use? We do not have guidelines based on specific numbers of users or reports to share with you; each deployment situation is different.

Whether you choose to combine functions (web server, Logi Ad Hoc v11 instance, and database servers) on one computer is, ultimately, your decision. Numerous factors can affect this decision, including the amount of web server traffic, the number of concurrent database users, the size of the databases, the complexity of the database queries, the frequency of report access, and, not least, cost.

You may care to begin with a combined configuration and, as your report usage grows, change to a dedicated configuration. The nature of Logi products allows you to do this easily and often without additional cost (if per-server CPU counts remain constant).

Recent studies concerning server virtualization suggest that database servers are frequently under-utilized. On the other hand, many database vendors recommend that their products be run on a dedicated server. You may wish to check with your database vendor for their recommendations concerning database servers.

## Server Virtualization

Many organizations are using server virtualization to maximize hardware usage and reduce costs. Server virtualization products allow the assignment of CPU resources to processes. This may take the form of a maximum percentage of combined CPU utilization, or as specific allocation of logical CPUs, to a virtual machine (VM). The server administrator is responsible for making these configuration decisions. Logi Analytics product licenses treat a VM just like a regular, non-virtualized server. In order to ensure good performance in any virtualized server environment, administrators must be careful to allocate appropriate resources to VMs. It's not uncommon to relocate a VM from one hardware platform to another, for example, for hardware maintenance. The Logi license will "move" with the VM, as long as the machine name remains unchanged.

## Product Expiration Information

Information about Logi products and versions that have reached the end of their life cycle can be found in *[Product Lifecycle Expiration](https://devnet.logianalytics.com/hc/en-us/articles/4419715037335-Product-Life-Cycle-Expiration)*.
