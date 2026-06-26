---
title: "Integrate Logi Reports with Other Applications"
id: 4406817570711
section: "Logi Info v12 & Other Products"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817570711-Integrate-Logi-Reports-with-Other-Applications
updated_at: 2022-04-06T06:06:55Z
---

# Integrate Logi Reports with Other Applications

# Integrate Logi Reports with Other Applications

Developers frequently ask how Logi applications can be **integrated** with their other applications and this topic provides an overview.

Topics related to integrating Logi reports with other applications include:

* [Embedding in Desktop Applications](https://devnet.logianalytics.com/hc/en-us/articles/4406817569175-Embedding-in-Desktop-Applications)
* [Including in Main Applications](https://devnet.logianalytics.com/hc/en-us/articles/4406822388375-Including-in-Main-Applications)
* [Integrating Security](https://devnet.logianalytics.com/hc/en-us/articles/4406817571991-Integrating-Security)
* [Scripting and Embedded Reports API](https://devnet.logianalytics.com/hc/en-us/articles/4406817573015-Scripting-and-Embedded-Reports-API)

For information about Logi Plug-ins, see [Logi Plug-ins](https://devnet.logianalytics.com/hc/en-us/articles/4406817734295-Logi-Plug-ins).

## About Logi's Zero Footprint

A major consideration when discussing the integration of two applications is what kind of **impact** a second application will have on the performance and operation of the main application. As free-standing web applications, Logi applications are designed to have a "zero footprint", which is to say *no impact at all*. Just think of a Logi application as a separate web site your main application connects to.
Logi reports can be run in a way that entirely **isolates** them from the main application: no shared code, no supporting library dependencies, and no mutual version considerations.
As free-standing web applications, Logi reports can also be run on **separate servers** so that there need be no performance or storage impacts on the main application.

### No Common Code Required

From a development perspective, Logi reports do not need to be combined with the **code** of the main application. There are no function or object libraries**,** non-compiled **API** that developers must add to their main application code in order to access the power and flexibility of Logi reporting. Logi .NET applications are typical ASP.NET apps but none of their code is placed in the Global Assembly Cache. Logi Java applications use their own .jar/.java files.

### Direct Datasource Connection

Logi applications connect directly to a wide variety of datasources, so they do not need to rely on, or go through, the data connectivity of the main application. So main application performance is not affected by data retrieval and processing activities in the reporting application.
