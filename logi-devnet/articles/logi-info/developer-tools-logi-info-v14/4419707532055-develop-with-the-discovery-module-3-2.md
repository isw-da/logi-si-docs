---
title: "Develop with the Discovery Module 3.2"
id: 4419707532055
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707532055-Develop-with-the-Discovery-Module-3-2
updated_at: 2022-07-17T02:08:04Z
---

# Develop with the Discovery Module 3.2

# Develop with the Discovery Module 3.2

The **Discovery Module** (DM) is an add-on module for Logi Info, that
enables special elements in Logi Info and provides an embedded discovery
experience that works directly with relational data sources.

The following topics are intended for *Logi developers* and discusses how to configure an application after the DM has been installed:

* [Connecting to the Logi Application Service](https://devnet.logianalytics.com/hc/en-us/articles/4419715254423-Connecting-to-the-Logi-Application-Service#AS)
* [Using The Thinkspace Element](https://devnet.logianalytics.com/hc/en-us/articles/4419722871575-Using-the-Thinkspace-Element#Thinkspace)
* [Configuring Thinkspace Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4419722869527-Configuring-Thinkspace-Bookmarks#Bookmarks)
* [Configuring Add-to-Dashboard or -Gallery](https://devnet.logianalytics.com/hc/en-us/articles/4419707531031-Configuring-Add-to-Dashboard-or-Gallery#Dashboard)
* [Embedding Visualizations](https://devnet.logianalytics.com/hc/en-us/articles/4419722870679-Embedding-Visualizations#Embedding)

## About the Discovery Module

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Advanced features discussed here work with Logi Info v12.5 and later. Earlier and later Info versions may not support them; consult the [Release Notes](https://clm.logianalytics.com/rdPage.aspx?rdReport=RelNotesINF) for specific details.

Introductory information about the DM and directions for installing it can be found in our installation topics for [Install the Discovery Module - Windows](https://devnet.logianalytics.com/hc/en-us/articles/4419722963351-Install-the-Discovery-Module-Windows) and [Install the Discovery Module - Linux](https://devnet.logianalytics.com/hc/en-us/articles/4419715326871-Install-the-Discovery-Module-Linux). If you haven't read it already,
we recommend you do so before proceeding.

Once installed, the DM makes special services and elements available in Logi Studio, controlled by various licensing combinations. These include Logi Platform Services and the **Thinkspace** element, which allows end-users to work with its interface to get a rich, highly-interactive analysis experience. Best-fit visualizations are automatically suggested by a built-in "recommendation engine" and data is organized using intelligent technology that clusters
data to make it more easily consumable by
users.

### Important Restrictions

Please note these important restrictions on the use of the DM 3.1+:

* Client browsers: Chrome 26+, IE 11+, Edge 40+, Firefox 20+, and Safari 7+.
* Server OS: 64-bit versions of Windows Server 2012, Windows 7, or Linux (Java 1.8 capable)
* Server: 4GB RAM minimum, 8GB RAM recommended (more if RAM also used for a VM)
* Server: 4GB hard disk space available
* Logi Info: v12.5, 64-bit version (there is no 32-bit DM version available)

The supported databases are:

* AWS Redshift
* Infobright
* JDBC database providers
* MS SQL Server
* MySQL
* Oracle
* PostgreSQL
* Snowflake
* Vertica

Logi Info .NET applications that include the DM must run using an IIS Application Pool configured for *Integrated* pipeline mode. *Classic* pipeline mode Application Pools will *not* work.

### Special Application Services

The DM uses two special application services on the web server:

* An embedded, runtime environment for server-side web applications ([node.js](https://nodejs.org/en/))
* An embedded, Java-based relational database ([H2](http://www.h2database.com/html/main.html))

Node.js and H2 are extremely compact, have a small installation
footprint, and do not install a lot of extra tools or management
utilities. They're provided as transparent services that require little
or no management for use with the DM.

Two Windows Services or Linux daemons are created during the installation: *Logi Application Service* and *Logi Data Service*.
