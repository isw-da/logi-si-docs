---
title: "General Requirements"
id: 4406817919767
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817919767-General-Requirements
updated_at: 2022-04-06T06:09:04Z
---

# General Requirements

# General Requirements

This topic covers the general requirements for upgrading Logi products:

* Logi products for the Windows environment and Logi Studio require the .NET Framework 4.x. If not already in place, with your consent, appropriate versions of the .NET Framework are installed when Logi products are installed. They are also available for free from the [Microsoft Download Center](http://www.microsoft.com/en-us/download/developer-tools.aspx?q=developer+tools).   
    
  Microsoft ended support for .NET Framework 4.0 and 4.5 in January 2016. We recommend use of .NET 4.6.
* Separate installations of different versions of Logi products and applications can co-exist as long as they are installed in different folders.
* IIS users need to implement separate Application Pools to isolate Logi applications using different .NET Framework versions. Application Pools are a standard feature of IIS 7+ and can be implemented in IIS 6 using the instructions provided later in this topic.
* Logi v12 Java applications require the Oracle JDK or OpenJDK 8 or (Info v12.6 SP2+) 11, 12, 13, 14  
    
  ![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Oracle has changed its Java usage policies. See [Java Usage Policy](https://devnet.logianalytics.com/hc/en-us/articles/4406817692055-Java-Usage-Policy) for important information.
