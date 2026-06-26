---
title: "System Requirements - Logi Info"
id: 4419715478551
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715478551-System-Requirements-Logi-Info
updated_at: 2022-10-31T14:41:53Z
---

# System Requirements - Logi Info

# System Requirements - Logi Info

This topic presents the general hardware and software requirements use of Logi Info and the products and data sources it supports.

The following topics discuss requirements and recommendations for installing Logi Info v14:

* [Sample Architecture](https://devnet.logianalytics.com/hc/en-us/articles/4419707831447-Sample-Architecture)
* [Sizing for Performance](https://devnet.logianalytics.com/hc/en-us/articles/4419723163287-Sizing-for-Performance#Performance)
* [Scaling Logi Info Applications](https://devnet.logianalytics.com/hc/en-us/articles/4419707832343-Scaling-Logi-Info-Applications)
* [Server Virtualization](https://devnet.logianalytics.com/hc/en-us/articles/4419707833367-Server-Virtualization#Virtualization)
* [Container Deployments](https://devnet.logianalytics.com/hc/en-us/articles/4419707830551-Container-Deployments#Containers)
* [Cloud Deployments](https://devnet.logianalytics.com/hc/en-us/articles/4419715477399-Cloud-Deployments#Cloud)

## General Requirements

The following general hardware and software components are supported by the latest releases of Logi Info.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Logi add-on modules and related products may not support all data sources and supporting software listed below; refer to their introductory documentation for details.

|  |  |
| --- | --- |
| Browsers | - Chrome, Firefox: all current public versions (Certified) - Microsoft Edge: all current public versions (Certified) - Microsoft Internet Explorer: 11 (Certified); see notes below about earlier versions - Safari, Opera: all current public versions (Supported) |

---

|  |  |
| --- | --- |
| Hardware | Development, QA/Test, Production, and Disaster Recovery servers: - Modern, high-speed CPU, with 4 cores, minimum - 8 GB RAM, minimum - 100GB storage device - 2 GB free disk space minimum (with .NET or JDK already installed) See [Sizing for Performance](https://devnet.logianalytics.com/hc/en-us/articles/4419723163287-Sizing-for-Performance) for more information. |

---

|  |  |
| --- | --- |
| Operating Systems | 64-bit versions of the following are supported:  - Windows Server 2019 (v12.7 + only), 2016 (v12+ only), 2012 R2, 2008, 2003 - Windows 10 (Logi Info v12+ only, all editions except RT) - Windows 7-8 (all editions) - Red Hat (7,8) Ubuntu (latest version), CentOS (7, Stream8), SUSE, and most other flavors of Linux |

---

|  |  |
| --- | --- |
| Web Servers | - Internet Information Server (IIS) 6.x, 7.x, 8.x - Internet Information Server (IIS) 10 (Logi Info v12+ only) - Apache-Tomcat 6, 7, 8 (without Tomcat FHS), 9 8.5, 9.0 - JBoss 4, 5, 7, EAP-6.3 - GlassFish (SJSAS) 2.1, 3.0, 3.1, 4.0, 4.1 - WebLogic 10, 12c - Websphere 7, 8.5 - WildFly 8, 9, 10 |

---

|  |  |
| --- | --- |
| Supporting Software | Required for all development work, using Logi Studio: - Microsoft .NET Framework 4.6+ Required for development and execution of Logi .NET applications on Windows servers: - Microsoft .NET Framework 4.6+ Required for development and execution of Logi Java applications on Windows or Linux servers: - OpenJDK 8, 11, 12 (see note below regarding 11+), 13, 14  Oracle has changed its Java usage policies - see [Java Usage Policy](https://devnet.logianalytics.com/hc/en-us/articles/4419723053335-Java-Usage-Policy) for important information. |

---

|  |  |
| --- | --- |
| Data Sources | Logi Info can connect to, use data from, and in most cases write back to the following data sources: - DB2 database server - Files: JSON, XML, Excel, CSV - Google Docs, Google Maps - HP Vertica - HPCC - JDBC-compliant database servers - Microsoft SQL Server database server - Microsoft SQL Server Analysis Services (OLAP) - MongoDB (up to and including v2.6, but *not* later versions) - MySQL database server (excluding v5.5) - ODBC-compliant database servers - OLEDB-compliant database servers - Oracle database server ( New for 14.2 up to and including 19c) - PostgreSQL database server - Progress OpenEdge database server - Salesforce.com - Twitter.com - Web Services (REST and SOAP) With the addition of supporting products such as Logi DataHub, many other online commercial data sources can be accessed. See each product's System Requirements or introductory documents for more information. |

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png)

* IIS must be installed *before* installing Logi products. Logi .NET applications on Windows and Logi Studio require the .NET Framework 4.6+. If not already in place, with your consent, appropriate versions of the .NET Framework are installed when Logi products are installed. They are also available for free from the [Microsoft Download Center](http://www.microsoft.com/en-us/download/developer-tools.aspx?q=developer+tools).
* More information for Linux developers about Logi Java applications is available in [About Logi Apps and Java](https://devnet.logianalytics.com/hc/en-us/articles/4419715039639-About-Logi-Apps-and-Java-).
* While Internet Explorer versions 7-10 are certified for use with Logi Info v12.x, Microsoft has [ended support](https://www.microsoft.com/en-us/WindowsForBusiness/End-of-IE-support) for them. Microsoft has also ended support IE 5 and 6. You should use Microsoft Edge for viewing applications built with Logi Info v12.x and later.
* Microsoft [ended support](https://support.microsoft.com/en-us/lifecycle/search?alpha=Microsoft%20.NET%20Framework%204.5) for .NET Framework 4.5 in January 2016. .NET 4.6 is required for Logi .NET applications 12.6+.
* Use of Java 11+ (supported in Info v12.6 SP2 and later) requires special configuration - see [Java Server Configurations](https://devnet.logianalytics.com/hc/en-us/articles/7522872807447-Java-Server-Configurations) for more information.

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Adobe no longer supports their Flash Player, and has blocked Flash content from running in a Flash player since January 12, 2021. Select this [link](https://www.adobe.com/products/flashplayer/end-of-life.html "Adobe Flash Player") for more information.
