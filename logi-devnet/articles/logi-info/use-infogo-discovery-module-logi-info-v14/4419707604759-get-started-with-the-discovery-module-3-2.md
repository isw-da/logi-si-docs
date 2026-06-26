---
title: "Get Started with the Discovery Module 3.2"
id: 4419707604759
section: "Use InfoGo/Discovery Module - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707604759-Get-Started-with-the-Discovery-Module-3-2
updated_at: 2022-07-17T01:48:19Z
---

# Get Started with the Discovery Module 3.2

# Get Started with the Discovery Module 3.2

The Discovery Module is an add-on module for Logi Info that
enables special elements in Logi Info and provides an embedded discovery
experience that works directly with data sources.

The following topics discuss getting started with Discovery Module 3.2:

* [Configure a Connection](https://devnet.logianalytics.com/hc/en-us/articles/4419722932247-Configure-a-Connection#Connection)
* [Create a Dataview](https://devnet.logianalytics.com/hc/en-us/articles/4419707603607-Create-a-Dataview#Dataview)
* [Create a SuperWidget](https://devnet.logianalytics.com/hc/en-us/articles/4419722933143-Create-a-SuperWidget#SuperWidget)
* [Use the SuperWidget in Your Application](https://devnet.logianalytics.com/hc/en-us/articles/4419707605783-Use-the-SuperWidget-in-Your-Application#Application)

## About the Discovery Module

![](https://devnet.logianalytics.com/hc/article_attachments/4419706599575/noteicon.png) Advanced features discussed here work with Logi Info v12.5 and later. Earlier and later Info versions may not support them; consult the [Release Notes](https://documentation.logianalytics.com/inf/content/release-notes.htm) for specific details. SuperWidgets, for example, have been deprecated in Logi Info v12.6.

The purpose of this topic is to help new Logi Info + Discovery
Module users understand how the products can be used. It assumes that
Logi Info and the Discovery Module have already been installed and
licensed. There are three ways that you can approach using the products:

### Thinkspace in SSRM - InfoGo Application

If you have both the Discovery Module (DM) and the Self-Service Reporting Module (SSRM) with its ready-made **InfoGo** application installed with Logi Info, then the DM's **Thinkspace**
element is optionally available in InfoGo and can be used by end-users
to create analyses. DevNet provides complete documentation for
configuration and use of the Thinkspace with the SSRM.

### Thinkspace with Metadata in Your Custom Info Application

You can also use the DM's Thinkspace element directly in your own custom Info application, using the **Active Query Builder** and **Metadata** elements, to provide users with access to the desired data. Metadata files are built using the Metadata Builder
tool and they provide a standard approach to enumerating all of the
database objects that will be available to users. Or, you can just use
direct SQL
queries to get the data. For more information, see [Web Metadata Builder](https://devnet.logianalytics.com/hc/en-us/articles/4419723223063-Web-Metadata-Builder).

### Logi Services in Your Custom Info Application

A more advanced approach, using the new Logi services technology, is also available and we encourage you to use it.
