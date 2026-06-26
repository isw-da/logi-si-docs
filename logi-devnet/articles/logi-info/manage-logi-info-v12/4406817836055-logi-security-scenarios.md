---
title: "Logi Security Scenarios  "
id: 4406817836055
section: "Manage - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817836055-Logi-Security-Scenarios
updated_at: 2022-04-06T06:08:31Z
---

# Logi Security Scenarios  

# Logi Security Scenarios

This topic introduces examples of representative security scenarios, from simple to complex, to assist you in understanding how to configure your web server and Logi applications to take advantage of Logi Security.

The scenarios include:

* [IIS: Basic and Digest Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4406817830295-IIS-Basic-and-Digest-Authentication-#IIS:)
* [IIS: Windows Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4406817831447-IIS-Windows-Authentication-#Integrated)
* [IIS: ASP.NET Impersonation](https://devnet.logianalytics.com/hc/en-us/articles/4406822503831-IIS-ASP-NET-Impersonation-#Impersonation)
* [Logi Security: NT Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4406822505239-Logi-Security-NT-Authentication-#NTAuth)
* [Logi Security: Session Variable Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4406817834007-Logi-Security-Session-Variable-Authentication-#Session)
* [Logi Security: Standard Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4406817835031-Logi-Security-Standard-Authentication-#Standard)
* [Logi Security: SecureKey Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4406817832727-Logi-Security-SecureKey-Authentication-#SecureKey)

For information about Logi Security in general, see [Logi Security](https://devnet.logianalytics.com/hc/en-us/articles/4406822422295-Logi-Security) and [Working with Logi Security](https://devnet.logianalytics.com/hc/en-us/articles/4406818124567-Working-with-Logi-Security).
The examples use Windows IIS server, however, many of them are also relevant when using non-Windows web servers, such as Apache Tomcat.
The availability of different forms of security in the IIS web server are predicated on the installation of related IIS features, accomplished through Control Panel![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Programs and Features![](https://devnet.logianalytics.com/hc/article_attachments/4417583616279/menuarrowrt.png)Windows Features.
