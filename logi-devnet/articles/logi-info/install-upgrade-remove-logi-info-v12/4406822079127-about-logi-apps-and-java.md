---
title: "About Logi Apps and Java "
id: 4406822079127
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822079127-About-Logi-Apps-and-Java
updated_at: 2022-04-06T06:03:00Z
---

# About Logi Apps and Java 

# About Logi Apps and Java

Logi Info v12 produces web applications that use either the .NET Framework or Java libraries. You can run Logi Java applications on web servers under Linux and other UNIX variants, as well as under Windows. This topic describes some of the development options you have for .NET and Java libraries and provides links to related topics.  
  
For information about installing Logi Studio, see [Installing Logi Studio](https://devnet.logianalytics.com/hc/en-us/articles/4406822384151-Installing-Logi-Studio).  
For information about configuring Java servers for use with Logi applications, see [Java Server Configurations](https://devnet.logianalytics.com/hc/en-us/articles/4406822432791-Java-Server-Configurations-).

Logi Info consists of two parts: **Logi****Studio** and the **Logi****Server Engine**. When you select a Java application type during development, Studio generates applications that use JDK libraries rather than the .NET framework. The Server Engine includes special components that allow you to deploy Logi applications as Java applications on Windows or Linux/UNIX platforms.

|  |  |
| --- | --- |
| Development Options Your process for creating Logi applications is identical regardless of which application type you choose, Java or .NET. You can use some specialized elements to support the Java environment, such as **Connection.JDBC**, when developing Java applications.  The **formats** of definition, support, and other files that make up a Logi application **are the same** for all versions of Logi managed reporting products.  **Logi Studio**, though Java-aware, is a Windows application. Developers creating Logi apps use Studio on a Windows PC to develop their Logi applications, regardless of the final deployment environment. Your developers have the option of developing *and* testing their application entirely on a Windows platform before moving it to a production Linux/UNIX server. Deployment Options You can deploy Logi applications on servers running Windows or Linux/UNIX. You can move Logi applications to one of these servers and enable it to use the JDK by adding **special folders** to the application folder (changes in the \_Settings definition, such as the application path and connection attributes, may also be necessary). |  |

The following topics provide additional information about Logi apps and Java:

* [General Requirements](https://devnet.logianalytics.com/hc/en-us/articles/4406816947479-Logi-Apps-General-Requirements#Requirements)
* [Product Licensing](https://devnet.logianalytics.com/hc/en-us/articles/4406816948503-Logi-Info-Product-Licensing#Licensing)
* [Differences from Applications for .NET](https://devnet.logianalytics.com/hc/en-us/articles/4406816946327-Differences-of-Java-from-NET-Logi-Applications#Limitations)
* [Sharing Session Variables with Other Apps](https://devnet.logianalytics.com/hc/en-us/articles/4406816949655-Sharing-Session-Variables-with-Other-Apps#Sharing)
* [Cross-site Scripting (XSS) Protection](https://devnet.logianalytics.com/hc/en-us/articles/4406822080023-Cross-site-Scripting-XSS-Protection#XSS)
