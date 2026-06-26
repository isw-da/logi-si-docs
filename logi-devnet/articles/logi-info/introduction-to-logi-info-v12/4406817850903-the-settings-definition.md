---
title: "The _Settings Definition"
id: 4406817850903
section: "Introduction to Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817850903-The-Settings-Definition
updated_at: 2022-04-06T06:08:37Z
---

# The _Settings Definition

# The \_Settings Definition

The \_Settings definition contains global configuration settings for your Logi application. This topic introduces the \_Settings definition and the elements available for use in the definition.

The following topics describe the purpose of the elements that can be used in this definition and provide links to more detailed information, when available:

* [Application Element](https://devnet.logianalytics.com/hc/en-us/articles/4406822509207-Application-Element#Application)
* [Connections Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817841815-Connections-Element#Connections)
* [Constants Element](https://devnet.logianalytics.com/hc/en-us/articles/4406822510103-Constants-Element#Constants)
* [Event Logging Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817842967-Event-Logging-Element#Logging)
* [External Definitions Element](https://devnet.logianalytics.com/hc/en-us/articles/4406822511255-External-Definitions-Element#External)
* [File To Database Mapping Element](https://devnet.logianalytics.com/hc/en-us/articles/4406822512279-File-To-Database-Mapping-Element#DBMapping)
* [General Element](https://devnet.logianalytics.com/hc/en-us/articles/4406822513175-General-Element#General)
* [Global Chart Export](https://devnet.logianalytics.com/hc/en-us/articles/4406817844887-Global-Chart-Export#ChartExport)
* [Global Style Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817845911-Global-Style-Element#Style)
* [Globalization Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817847191-Globalization-Element#Globalization)
* [Java Session Copying Element](https://devnet.logianalytics.com/hc/en-us/articles/4406822514071-Java-Session-Copying-Element#Java)
* [Path Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817848471-Path-Element#Path)
* [Security Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817849495-Security-Element#Security)
* [Session Timeout Element](https://devnet.logianalytics.com/hc/en-us/articles/4406822514967-Session-Timeout-Element#Timeout)
* [Startup Process Element](https://devnet.logianalytics.com/hc/en-us/articles/4406817852183-Startup-Process-Element#Startup)
* [Team Development Element](https://devnet.logianalytics.com/hc/en-us/articles/4406822516375-Team-Development-Element#Team)
* [The Wait Panel Element](https://devnet.logianalytics.com/hc/en-us/articles/4406822517399-Wait-Panel-Element#WaitPanel)

## About the \_Settings Definition

The \_Settings definition (*yourLogiApp*\\_Definitions\\_Settings.lgx) contains the global configuration settings for your Logi application.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575547415/settingsdef_01.png)

It includes a variety of unique elements, some required, some optional, that provide overall control of the application. The required and most-commonly-used elements are shown above.

The definition includes information like database connection strings and security information that may need to be changed when deploying the application from development to production. For this reason, care should be taken when considering copying or overwriting a \_Settings definition file.

The \_Settings.lgx file of a Logi Info application is expected to be in a nested location under the root folder of the application, specifically in: <application root>/\_Definitions.

Combining \_Settings definition files for multiple applications or "centralizing" them elsewhere is not possible. A \_Settings definition can be obfuscated, using the Obfuscation tool in Logi Studio, a common technique used by developers to protect their software products from theft, tampering, and reverse-engineering. For more information, see [Obfuscating Definitions](https://devnet.logianalytics.com/hc/en-us/articles/4406818012055-Obfuscating-Definitions).
