---
title: "Introduction to Logi Reporting with Java"
id: 1500009531261
section: "Introduction to Logi Reporting with Java"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009531261-Introduction-to-Logi-Reporting-with-Java
updated_at: 2021-06-17T01:58:29Z
---

# Introduction to Logi Reporting with Java

# Introduction to Logi Reporting with Java

Logi Info and Logi Report, versions 10 and 11, can produce reports and web applications that use either the .NET Framework or Java libraries.

**IMPORTANT**: If you wish to upgrade to JDK 8 release build 261 (1.8.0\_261), or any later build of JDK 8, you will need to replace the mscorlib.jar file in the application folder with the new one and restart your server. The mscorlib.jar file can be found on our [Product Download](https://clm.logianalytics.com/rdPage.aspx?rdReport=ProductDownloads "Select to access Product Dowload page") page. Please contact Support for additional assistance.

Logi Java applications can be run on web servers under Linux and other UNIX variants, as well as under Windows, and this topic provides introductory information about them.

* About Logi Reporting with Java
* [System Requirements](#Requirements)
* [Product Licensing](#Licensing)
* [Differences from Applications for .NET](#Limitations)
* [Share Session Variables with Other Apps](#Sharing)

For information about installing Logi Studio, see [Install Logi Studio](https://devnet.logianalytics.com/hc/en-us/articles/4402771959063-Install-Logi-Studio).  
For information about configuring Java servers for use with Logi applications, see [Java Server Configurations](https://devnet.logianalytics.com/hc/en-us/articles/1500009515622-Java-Server-Configurations).

## About Logi Reporting with Java

Logi Info and Logi Report consist of two parts: **Logi****Studio** and the **Logi****Server Engine**. When a Java application type is selected during development, Studio generates applications that use the JDK libraries rather than the .NET framework. The Server Engine includes special components that allow Logi applications to be deployed as Java applications on Windows or Linux/UNIX platforms.

### Development Options

The process of creating Logi applications is identical regardless of which application type, Java or .NET, is desired. Some specialized elements that are included to support the Java environment are available, such as **Connection.JDBC**, when developing Java applications.

The **formats** of definition, support, and other files that make up a Logi application and are created by developers **are the same** for all versions of Logi managed reporting products.

**Logi Studio**, though Java-aware, is a Windows application. Developers creating Logi apps use Studio on a Windows PC to develop their Logi applications, regardless of the final deployment environment.
Developers
have the option of developing *and* testing their application entirely on a Windows platform before
moving it to a production Linux/UNIX server.

### Deployment Options

Logi applications can be deployed on servers running Windows or Linux/UNIX. A Logi application can be moved to one of these servers and enabled to use the JDK by adding **special folders** to the application folder (changes in the \_Settings definition, such as the application path and connection attributes, may also be necessary).

## System Requirements

Please review the following requirements carefully to ensure that your hardware and software are suitable:

### Hardware

We do not have specific hardware configurations to recommend for use with the product. Logi Studio can be installed on 32-bit or 64-bit Windows platforms. Logi Java applications can be run on 32-bit and 64-bit Linux/UNIX platforms.

### Software

Check [System Requirements](https://devnet.logianalytics.com/hc/en-us/articles/1500009531921-System-Requirements) to ensure that your web server and other software are supported.

### Sun JDK 1.6, 1.7, or 1.8 (or equivalent Server JVM)

The official Sun Java Development Kit (JDK) v1.6, 1.7, or 1.8 is *required* for Logi Java applications, as it includes the Server JVM and will provide faster performance. You must install the JDK on the web server. The JRE is not sufficient, but **OpenJDK** 1.7 and Oracle **JRockit** 1.6 or 1.7 may be used.

### Database Connectivity and Tools

Connectivity to databases such as **Oracle**, **MySQL**, and **MS SQL Server** is supported via native connections. Connections using **JDBC** are also available. Connections to a variety of non-database datasources are also supported, including XML, CSV, Excel data files, and web services.

Specific MySQL and MS SQL Server database drivers are provided with the Logi Server Engine, so developers do not need to separately download and install them. However, these may not be the correct version for all circumstances and developers may need to update or replace them.

In v11.0.416, our SQL Server JDBC driver was upgraded to work with JDK 1.7 and MS SQL Server 2005+. The previous version of the driver's sqljdbc4.jar file, however, is still provided, as sqljdbc4.old, for users who work with MS SQL Server 2000.

Developers working with **Oracle**, who wish to use the **Database Browser** and **Query Builder** tools within Studio, may need to install and configure the **Oracle Client (OLEDB)** on the Windows platform where Logi Studio is installed.

### Required Platform Knowledge

Developers creating Logi Java applications for Linux/UNIX servers should ensure that they have a **good working understanding** of the OS, the JDK, the web server, and the admin/management tools on their server. The detailed knowledge required to successfully administer the servers can be **extensive** and **complex** and is well beyond the scope of Logi documentation.

## Product Licensing

All Logi 10+ products come with a built-in, **15-day trial license**. You need
do nothing but install the product and you can begin using it. A clearly-visible
display in Studio's toolbar counts down the days remaining in
the trial period.

Clicking the counter display will take you to a web page that offers
information about **purchasing** a regular Logi license.

After the trial period expires, Studio and any Logi reports you may have
developed will *no longer run* without a valid license.

You *may not* use our products for redistribution with, or embed them in,
other products without an **OEM license**; contact our Sales group for more
information if you need an OEM license.

For more detailed information about licenses, see [Product Licensing](https://devnet.logianalytics.com/hc/en-us/articles/1500009531601-Product-Licensing).

## Differences from Logi Applications for .NET

Logi Java applications provide all of the features and functionality found in Logi .NET applications.

Naturally, Logi Java apps do not support Windows-specific technologies such as OLEDB. Analogous Java technologies, such as JDBC, are supported instead. However, for the best results, developers should try to use *native* connections, such as Connection.MySQL, before using *generic* connections like Connection.JDBC.

**JavaScript** is the only scripting language available when building Java applications. However, a built-in "VBScript emulator" allows our intrinsic functions, such as IIF(), which are modeled on VBScript, to be available for use in a Java application.

Currently, Logi applications for Java *do not* have support for the following elements*:*

* Any OLAP elements (note that XOLAP elements, however, *are* supported)
* Connector.Salesforce (prior to v11.0.416)
* DataLayer.Web Scraper

Prior to v10.0.428, when exporting reports to PDF from a Java application, data table column headers would not be repeated after page breaks.

For information about installing Logi Studio, see [Install Logi Studio](https://devnet.logianalytics.com/hc/en-us/articles/4402771959063-Install-Logi-Studio).  
For information about deploying Logi Java applications, see [Java Server Configurations](https://devnet.logianalytics.com/hc/en-us/articles/1500009515622-Java-Server-Configurations).

## Share Session Variables with Other Apps

On a web server, Logi applications for Java and regular (non-Logi) Java applications
maintain their session variables in different ways. And, typically, Logi application session variables are accessed using @Session tokens, while Java application session variables are accessed via JSP or by using the javax.servlet.http.HttpSession object.

If a Logi application for Java is to be integrated with a Java application, then how can their session variables be shared?

Prior to v11.0.127, almost all session variables were *automatically* copied between two integrated applications. However, this behavior did not always produce the best performance and has been discontinued. The **Java Session Copying** element, introduced in v11.0.127 and available in the \_Settings definition, provides a more selective method for session variable copying between the two applications.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778385687/attnicon.gif)  In order to use this feature, you must not use session variable names that contain *spaces* in your Logi application, and there's a small performance penalty for this process, so it's best to minimize the number of variables copied. It may be necessary to restart your web server if you edit the lists in the attributes described below.

The element has four attributes, consisting of Regular Expressions, which control which session variables are copied. As it can be difficult to write Regular Expressions which both include *and* exclude strings, we've provided two attributes ("include") which are processed first, followed by two other attributes ("exclude") which are processed second, making it easier to accomplish both types of operations.

| Attribute | Description |
| --- | --- |
| Copy From Java Exclude | Specifies, as a comma-separated list of Regular Expressions, the Java application session variables that will *not* be copied to the Logi application session variable space. This attribute is processed *after* Copy From Java Include, removing variables from that list. |
| Copy From Java Include | Specifies, as a comma-separated list of Regular Expressions, the Java application session variables that *will* be copied to the Logi application session variable space. |
| Copy To Java Exclude | Specifies, as a comma-separated list of Regular Expressions, the Logi application session variables that will *not* be copied to the Java application session variable space. This attribute is processed *after* Copy To Java Include, removing variables from that list. |
| Copy To Java Include | Specifies, as a comma-separated list of Regular Expressions, the Logi application session variables that *will* be copied to the Java application session variable space. |

Once copied, session variables are identified, in the Java app, using its session object's attribute ID and, in the Logi app, as the name used with a @ Session token. For example:

Java JSP: session.getAttribute("userEmail")    
Logi app: @Session.userEmail~

It is possible to return to the pre-v11.0.127 "copy all" behavior by manually adding the following XML to your \_Settings definition source code, as a child of the <Setting> tag:

<JavaSessionCopying
CopyToJavaInclude="^" CopyToJavaExclude="DebugFile,-bUsesSort$,-tra$,-xmlDef$,  
    -Xsl$,-rdDef$" CopyFromJavaInclude="^" CopyFromJavaExclude="^rd,^dt" />
