---
title: "System Requirements, Installation, and Licensing"
id: 4419707583511
section: "Introduction to Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707583511-System-Requirements-Installation-and-Licensing
updated_at: 2022-07-17T02:07:47Z
---

# System Requirements, Installation, and Licensing

# System Requirements, Installation, and Licensing

This topic provides answers to frequently-asked questions about system requirements, installation, and licensing:

1. [What Operating System versions are supported?](#OS)
2. [Are there 64-bit versions of your products?](#64Bit)
3. [What are the licensing ramifications of using server
   virtualization?](#VirtualLic)
4. [Will a Logi application run in a shared hosting environment?](#SharedHosting)
5. [Do you have versions of your products that will run on Linux with the
   Apache-Tomcat web server?](#JavaVersion)
6. [When I register my application, its virtual directory is created on
   IIS under an "OWA" web site. Why is this?](#OWA)
7. [Should I install Logi Server on the same web server I use for Outlook
   Web Access (OWA)?](#OWAServer)
8. [How are your products delivered after someone purchases them?](#NoCDs)
9. [Will your products work via a Citrix server?](#Citrix)
10. [Will your products work with Microsoft SQL Server?](#SQL2008)
11. [I received this error message: Thread was being aborted](#Aborted)
12. [It appears I need a copy of the Logi license file in
    *every* Logi app folder. Is a centralized file possible
    instead?](#CentralLic)

## 1. What Operating System versions are supported?

Supported OS versions include:

* Windows Server 2019 (v12.7 + only), 2016 (v12+ only), 2012 R2, 2008, 2003
* Windows 10 (with Logi Info v12+ only)
* (all editions except *RT*)
* Windows 7-8 (all editions)
* SUSE, Red Hat, Ubuntu, CentOS, and most other flavors of Linux

## 2. Are there 64-bit versions of your products?

Yes. Starting with v12.2, only 64-bit
versions are available. Hardware manufacturers have started focusing
almost exclusively on 64-bit server platform architectures and major OS
manufacturers have transitioned their products to 64-bit only versions,
making it difficult for us to comprehensively test 32-bit versions of our
products against them. A 64-bit environment and software offer numerous
benefits relating to improved performance.

## 3. What are the licensing ramifications of using server virtualization?

Please see [Server Virtualization](https://devnet.logianalytics.com/hc/en-us/articles/4419707793559-Server-Virtualization).

## 4. Will a Logi application run in a shared hosting environment?

Logi applications require a High Trust Level to run. Most hosting centers
insist on Low or Medium Trust levels on shared web servers for security
purposes. However, if the hosting center offers a dedicated server or
virtualized server, they may allow a High Trust Level and Logi
applications can then be used.

## 5. Do you have a version of your products that will run on Linux with the Apache-Tomcat web server?

Yes, Logi Info can create web applications that use OracleJDK or
OpenJDK 8, 11, 12, 13, or 14 instead of .NET and run under Linux or other
UNIX derivatives, on Apache-Tomcat and other open source web servers. Fore more information, see [About Logi Apps and Java](https://devnet.logianalytics.com/hc/en-us/articles/4419715039639-About-Logi-Apps-and-Java-) and [Java Usage Policy](https://devnet.logianalytics.com/hc/en-us/articles/4419723053335-Java-Usage-Policy).

## 6. When I register my application, its virtual directory is created on IIS under an "OWA" web site. Why is this?

By default, IIS is installed with a "Default Web Site"
configured, which has an ID of #1. The Logi tools register applications
(create their virtual directories) under the web site with ID #1. If your
Default Web Site is missing and virtual directories are being created
under "OWA" (which stands for Outlook Web Access and is used for
remote email access) your IIS configuration has been highly customized.
You need to get a trained IIS administrator involved in order to configure
this server for use with Logi apps.

## 7. Should I install Logi Server on the same web server I use for Outlook Web Access (OWA)?

No. Microsoft recommends that, for reasons of security, performance, and
scalability, you do not run other web sites or web applications on your
OWA web server platform.

## 8. How are your products delivered after someone purchases them?

Product delivery is via download from our web site; documentation is
available on this web site. We do not distribute our products on CDs or
DVDs.

## 9. Will your products work via a Citrix server?

Yes. Logi applications, as web applications, can be served and browsed in
a Citrix environment without any problem. Our Studio development tool, as
a standard Windows client application, needs to be installed and published
as a Citrix application. As is the case with many apps published this way,
its performance will be a little less snappy than it would be if it was
installed and run from a user's local machine.

## 10. Will your products work with Microsoft SQL Server?

Yes. Our products have been tested with and work with all versions of MS
SQL Server, starting with SQL Server 2000.

## 11. I received this error message: Thread was being aborted

Depending on the availability of system resources, the IIS worker process
may not have been able to acquire enough memory to process the request and
recycled. If your web server is IIS 6, you may want to investigate how its
Application Pools are being used. If you have a large number of web
applications all using the Default Application Pool, you may want to
isolate some, or all of them, in separate app pools.

## 12. It appears I need a copy of the Logi license file in *every* Logi app folder. Is a centralized file possible instead?

Yes, instead of distributing and maintaining many license files on a
single computer, you place a one copy of the license file in a central
location. In each Logi application, you modify the \_Settings definition,
configuring the General element's License File Location attribute to point
the folder containing the license file. The account the web server uses to
run your apps must have access permissions to that license file folder.
