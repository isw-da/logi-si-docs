---
title: "Logi Apps General Requirements"
id: 4406816947479
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406816947479-Logi-Apps-General-Requirements
updated_at: 2022-04-06T06:03:04Z
---

# Logi Apps General Requirements

# Logi Apps General Requirements

There are specific hardware and software requirements that you must match to use Logi apps. This topic describes the requirements.

Please review the following requirements carefully to ensure that your hardware and software are suitable.

## Hardware

We do not have specific hardware configurations to recommend for use with the product. Logi Studio can only be installed on 64-bit Windows platforms. Logi Info is only available in a 64-bit version. ![](https://devnet.logianalytics.com/hc/article_attachments/4417575410199/__new12.8.png) Logi Info v12 can be installed on a single computer under Windows Server 7, 8, 10, 2012 r2, 2016, and 2019 for use with the IIS web server. Logi Java applications must also be run 64-bit Linux/UNIX platforms.

## Software

Review [System Requirements - Logi Info](https://devnet.logianalytics.com/hc/en-us/articles/4406822529559-System-Requirements-Logi-Info) to ensure that your web server and other software are supported.

## Oracle JDK or OpenJDK

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)Oracle has changed its Java usage policies - please read our [Java Usage Policy](https://devnet.logianalytics.com/hc/en-us/articles/4406817692055-Java-Usage-Policy) for important information.

The official Oracle Java Development Kit or OpenJDK 8, 11, 12, 13, or 14 (Info v12.6 SP2+ required for 11+) is required for Logi Java applications, as it includes the Server JVM and will provide faster performance. You must install the JDK on the web server, the JRE is not sufficient.

## Database Connectivity and Tools

Connectivity to databases such as **Oracle**, **MySQL**, and **MS SQL Server** is supported via native connections. Connections using **JDBC** are also available. Connections to a variety of non-database datasources are also supported, including XML, CSV, Excel data files, and web services.

We provide specific MySQL and MS SQL Server database drivers with the Logi Server Engine, so developers do not need to separately download and install them. However, these may not be the correct version for all circumstances and developers may need to update or replace them.

Our SQL Server JDBC driver works with JDK or OpenJDK 8, (Info v12.6 SP2+) 11, 12, 13, or 14 and MS SQL Server 2005+. The previous version of the driver's sqljdbc4.jar file, however, is still provided, as sqljdbc4.old, for users who work with MS SQL Server 2000.

If you are working with **Oracle**, and wish to use the **Database Browser** and **Query Builder** tools within Studio, you may need to install and configure the **Oracle Client (OLEDB)** on the Windows platform where Logi Studio is installed.

## Required Platform Knowledge

If you or your developers are creating Logi Java applications for Linux/UNIX servers, you should ensure that you have a **good working understanding** of the OS, the JDK, the web server, and the admin/management tools on their server. The detailed knowledge required to successfully administer the servers can be **extensive** and **complex** and is well beyond the scope of Logi documentation.
