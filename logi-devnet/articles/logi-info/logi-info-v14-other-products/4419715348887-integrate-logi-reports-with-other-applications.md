---
title: "Integrate Logi Reports with Other Applications"
id: 4419715348887
section: "Logi Info v14 & Other Products"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715348887-Integrate-Logi-Reports-with-Other-Applications
updated_at: 2022-07-17T02:07:25Z
---

# Integrate Logi Reports with Other Applications

# Integrate Logi Reports with Other Applications

Developers frequently ask how Logi applications can be **integrated** with their other applications and this topic provides an overview.

Topics related to integrating Logi reports with other applications include:

* [Embedding in Desktop Applications](https://devnet.logianalytics.com/hc/en-us/articles/4419715347735-Embedding-in-Desktop-Applications)
* [Including in Main Applications](https://devnet.logianalytics.com/hc/en-us/articles/4419722986263-Including-in-Main-Applications)
* [Integrating Security](https://devnet.logianalytics.com/hc/en-us/articles/4419707651607-Integrating-Security)
* [Logi Plug-ins](https://devnet.logianalytics.com/hc/en-us/articles/4419707654167-Logi-Plug-ins)
* [Scripting and Embedded Reports API](https://devnet.logianalytics.com/hc/en-us/articles/4419707655063-Scripting-and-Embedded-Reports-API)

## About Logi's Zero Footprint

A major consideration when discussing the integration of two applications is what kind of **impact** a second application will have on the performance and operation of the main application. As free-standing web applications, Logi applications are designed to have a "zero footprint", which is to say *no impact at all*. Just think of a Logi applicationas a separate web site your main application connects to.
Logi reports can be run in a way that entirely **isolates** them from the main application: no shared code, no supporting library dependencies, and no mutual versioning considerations.
As free-standing web applications, Logi reports can also be run on **separate servers** so that there need be no performance or storage impacts on the main application.

### No Common Code Required

From a development perspective, Logi reports do not need to be combined with the **code** of the main application. There are no function or object libraries**,** no compiled **API** that developers must add to their main application code in order to access the power and flexibility of Logi reporting. Logi .NET applications are typical ASP.NET apps but none of their code is placed in the Global Assembly Cache. Logi Java applications use their own .jar/.java files.

### Direct Datasource Connection

Logi applications connect directly to a wide variety of datasources, so they do not need to rely on, or go through, the data connectivity of the main application. So main application performance is not affected by data retrieval and processing activities in the reporting application.
