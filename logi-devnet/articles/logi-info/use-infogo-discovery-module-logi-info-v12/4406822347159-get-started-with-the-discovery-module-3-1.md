---
title: "Get Started with the Discovery Module 3.1"
id: 4406822347159
section: "Use InfoGo/Discovery Module - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406822347159-Get-Started-with-the-Discovery-Module-3-1
updated_at: 2022-04-06T06:06:22Z
---

# Get Started with the Discovery Module 3.1

# Get Started with the Discovery Module 3.1

The Discovery Module is an add-on module for Logi Info that
enables special elements in Logi Info and provides an embedded discovery
experience that works directly with data sources.

The following topics discuss getting started with Discovery Module 3.1:

* [Configure a Connection](https://devnet.logianalytics.com/hc/en-us/articles/4406817481111-Configure-a-Connection#Connection)
* [Create a Dataview](https://devnet.logianalytics.com/hc/en-us/articles/4406822346135-Create-a-Dataview#Dataview)
* [Create a SuperWidget](https://devnet.logianalytics.com/hc/en-us/articles/4406817482519-Create-a-SuperWidget#SuperWidget)
* [Use the SuperWidget in Your Application](https://devnet.logianalytics.com/hc/en-us/articles/4406822348055-Use-the-SuperWidget-in-Your-Application#Application)

## About the Discovery Module

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Advanced features discussed here work with Logi Info v12.5. Earlier and later Info versions may not support them; consult the [Release Notes](https://clm.logianalytics.com/rdPage.aspx?rdReport=RelNotesINF) for specific details. SuperWidgets, for example,have been deprecated in Logi Info v12.6.

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
queries to get the data. For more information, see [Web Metadata Builder](https://devnet.logianalytics.com/hc/en-us/articles/4406817979799-Web-Metadata-Builder).

### Logi Services in Your Custom Info Application

A more advanced approach, using the new Logi services technology, is also available and we encourage you to use it.
