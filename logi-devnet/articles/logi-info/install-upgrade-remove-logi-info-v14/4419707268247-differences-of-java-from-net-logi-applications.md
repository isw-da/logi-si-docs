---
title: "Differences of Java from .NET Logi Applications"
id: 4419707268247
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707268247-Differences-of-Java-from-NET-Logi-Applications
updated_at: 2022-07-17T02:09:34Z
---

# Differences of Java from .NET Logi Applications

# Differences of Java from .NET Logi Applications

Logi Java applications provide all of the features and functionality found in Logi .NET applications. This topic describes some of the differences between .NET and Java implementations.

Naturally, Logi Java apps do not support Windows-specific technologies such as OLEDB. Instead, Logi Info supports Analogous Java technologies, such as **JDBC**. However, for the best results, you should try to use *native* connections, such as Connection.MySQL, before using *generic* connections like Connection.JDBC.

**JavaScript** is the only scripting language you can use when building Java applications. However, you can use a built-in "VBScript emulator" for intrinsic functions, such as IIF(), which are modeled on VBScript. They're translated into JavaScript behind-the-scenes.
Currently, Logi applications for Java *do not* have support for the following elements*:*

* Any OLAP elements (![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) XOLAP elements, however, *are* supported)
* DataLayer.Web Scraper

For information about installing Logi Studio, see [Installing Logi Studio](https://devnet.logianalytics.com/hc/en-us/articles/4419707645207-Installing-Logi-Studio).  
For information about deploying Logi Java applications, see [Java Server Configurations](https://devnet.logianalytics.com/hc/en-us/articles/7522872807447-Java-Server-Configurations).
