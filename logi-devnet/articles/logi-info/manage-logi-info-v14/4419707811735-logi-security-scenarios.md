---
title: "Logi Security Scenarios  "
id: 4419707811735
section: "Manage - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707811735-Logi-Security-Scenarios
updated_at: 2022-07-17T02:06:22Z
---

# Logi Security Scenarios  

# Logi Security Scenarios

This topic introduces examples of representative security scenarios, from simple to complex, to assist you in understanding how to configure your web server and Logi applications to take advantage of Logi Security.

The scenarios include:

* [IIS: Basic and Digest Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4419707808535-IIS-Basic-and-Digest-Authentication-#IIS:)
* [IIS: Windows Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4419707809559-IIS-Windows-Authentication-#Integrated)
* [IIS: ASP.NET Impersonation](https://devnet.logianalytics.com/hc/en-us/articles/4419723141399-IIS-ASP-NET-Impersonation-#Impersonation)
* [Logi Security: NT Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4419715456919-Logi-Security-NT-Authentication-#NTAuth)
* [Logi Security: Session Variable Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4419723142551-Logi-Security-Session-Variable-Authentication-#Session)
* [Logi Security: Standard Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4419723143447-Logi-Security-Standard-Authentication-#Standard)
* [Logi Security: SecureKey Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4419707810711-Logi-Security-SecureKey-Authentication-#SecureKey)

For information about Logi Security in general, see [Logi Security](https://devnet.logianalytics.com/hc/en-us/articles/4419715379607-Logi-Security) and [Working with Logi Security](https://devnet.logianalytics.com/hc/en-us/articles/4419715615255-Working-with-Logi-Security).
The examples use Windows IIS server, however, many of them are also relevant when using non-Windows web servers, such as Apache Tomcat.
The availability of different forms of security in the IIS web server are predicated on the installation of related IIS features, accomplished through Control Panel![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)Programs and Features![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)Windows Features.
