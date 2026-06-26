---
title: "Installation Scenarios"
id: 4406817559575
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817559575-Installation-Scenarios
updated_at: 2022-04-06T06:06:51Z
---

# Installation Scenarios

# Installation Scenarios

The installation file you received contains everything you need to create both .NET and Java web applications. The distinction between the two is made when you start to build an application. There are two major parts to the product in the installation file: **Studio** (the development tool) and the **Server Engine**.

**Studio** is a Windows application that's installed on a Windows platform and the **Server Engine** is a set of files that's added to each Logi application and is processed by the web server. When you build an application, Studio adds the engine files to the application folder.

A typical installation scenario for developers who wish to create Logi applications for Java is to install Studio on a Windows **development** machine, equipped with the Oracle JDK or OpenJDK 8, 11, 12, 13, or 14 (Info v12.6 SP2+ required for version 11, 12, 13, and 14) and one of the approved web servers. In this way, development and testing can be done on a single non-production machine.   
  
![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Oracle has changed its Java usage policies. See [Java Usage Policy](https://devnet.logianalytics.com/hc/en-us/articles/4406817692055-Java-Usage-Policy) for important information.

However, for deployment to production, only the **Server Engine** files (and your application) need to be copied to the production web server, which can be a Linux/UNIX or Windows platform.

## 32- or 64-bit?

Logi Info Java applications will run on 32-bit and 64-bit Linux/UNIX platforms.

## Java Server Configurations

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Important configuration information for each Java web server we support can be found in [Java Server Configurations](https://devnet.logianalytics.com/hc/en-us/articles/4406822432791-Java-Server-Configurations-).
