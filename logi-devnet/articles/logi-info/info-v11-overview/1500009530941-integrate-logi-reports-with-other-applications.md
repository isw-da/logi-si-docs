---
title: " Integrate Logi Reports with Other Applications"
id: 1500009530941
section: "Info v11 Overview"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009530941--Integrate-Logi-Reports-with-Other-Applications
updated_at: 2021-06-17T01:58:25Z
---

#  Integrate Logi Reports with Other Applications

# Integrate Logi Reports with Other Applications

Developers frequently ask how Logi applications can be **integrated** with their other applications and this topic provides an overview.

* About Logi's Zero Footprint
* [Integrate in Web Applications](#WebApps)
* [Embed in Desktop Applications](#DesktopApps)
* [Include in Main Applications](#Including)
* [Integrate Security](#Security)
* [Logi Plug-ins](#Plugins)
* [Scripting and Embedded Reports API](#API)

## About Logi's Zero Footprint

A major consideration when discussing the integration of two applications is what kind of **impact** a second application will have on the performance and operation of the main application. As free-standing web applications, Logi report applications are designed to have a "zero footprint", which is to say *no impact at all*. Just think of a Logi report as a separate web site your main application connects to.

Logi reports can be run in a way that entirely **isolates** them from the main application: no shared code, no supporting library dependencies, and no mutual versioning considerations.

As free-standing web applications, Logi reports can also be run on **separate servers** so that there need be no performance or storage impacts on the main application.

### No Common Code Required

From a development perspective, Logi reports do not need to be combined with the **code** of the main application. There are no function or object libraries**,** no compiled **API** that developers must add to their main application code in order to access the power and flexibility of Logi reporting. Logi .NET applications are typical ASP.NET apps but none of their code is placed in the Global Assembly Cache. Logi Java applications use their own .jar/.java files.

### Direct Datasource Connection

Logi report applications connect directly to a wide variety of datasources, so they do not need to rely on, or go through, the data connectivity of the main application. So main application performance is not affected by data retrieval and processing activities in the reporting application.

## Integrate in Web Applications

The simplest
integration of Logi report output, of course, is for a web-based application to include a **URL link**
to the Logi reporting web application. From a website, this can be done with simple links, and can be viewed in a separate browser window or within an iFrame within the main application, and it can look quite seamless. Variables can be passed as **query string parameters** in order to achieve runtime flexibility; report output is returned as simple HTML and JavaScript.

## Embed in Desktop Applications

If developers want to **embed** Logi application output in their **desktop applications**, this can be easily accomplished.

Their desktop application just needs the ability to make an **HTTP request** and to **render** the **HTTP response**. Many development languages include browser objects that can do this; for example Microsoft Visual Studio includes a Web Browser component. Once again, the formal interaction with a Logi reporting application is a simple URL call rather than actual code integration.

## Include in Main Applications

Developers may want to actually include their Logi report as part of their main ASP.NET or Java web application. It *is* possible to do this, however, it introduces dependencies and complications, so it's not a recommended approach.

For example, the web.config file used by a Logi .NET reporting application is slightly different from that used by a traditional .NET application, and when the Logi app is part of the main app, these differences have to be resolved for both to run correctly.

The flexibility and performance provided by running Logi reporting applications as separate applications usually outweighs the convenience of packaging everything together within the main application.

## Integrate Security

Our "Logi Security" features offer **secure access protection** at the report, object, data row, and even (in Logi Info) down to the data column level.

Logi Security is very flexible and can operate in a stand-alone mode to independently retrieve security credentials for authentication and authorization from OS-based security systems, such as a **Windows Active Directory** domain, from LDAP directories, from custom security databases, and from a variety of other sources. When necessary, a standard login page is available; customized login pages are supported.

For those interested in a "single sign-on" implementation, **Logi****SecureKey Authentication** allows a main application to handle logins and authentication, and to securely pass user security authorization information into a Logi reporting application.

More information about security is available in [Introduction to Logi Security 10](https://devnet.logianalytics.com/hc/en-us/articles/1500009515502-Introduction-to-Logi-Security-10)*.*

## Logi Plug-ins

Logi applications support the use of "Plug-ins", which are compiled .dll or .jar files, written with modern development languages such as Java, Visual Basic.NET, or C#. Plug-ins allows developers to dynamically change the data, the design, and the behavior of Logi reports at runtime, and provide a way to access system resources and other objects in the scope of the web server OS and platform. Plug-ins can also be used to let the Logi application interact directly with the main application.

More information about plug-ins is available in [Logi Plug-ins](https://devnet.logianalytics.com/hc/en-us/articles/1500009531221-Logi-Plug-ins)*.*

## Scripting and Embedded Reports API

Logi applications support the use of both JavaScript and VBScript within them and can reference external scripting libraries, such as JQuery. Logi Info also includes our own [Embedded Reports API](https://devnet.logianalytics.com/hc/en-us/articles/1500009514942-Embedded-Reports-API), with makes it a breeze to embed active Logi reports into other HTML pages.
