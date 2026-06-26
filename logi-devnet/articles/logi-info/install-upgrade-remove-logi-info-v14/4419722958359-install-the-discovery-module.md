---
title: "Install the Discovery Module"
id: 4419722958359
section: "Install, Upgrade, & Remove - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722958359-Install-the-Discovery-Module
updated_at: 2022-07-17T02:07:33Z
---

# Install the Discovery Module

# Install the Discovery Module

The Logi Discovery Module (DM) provides an embedded data discovery
experience that works directly with relational data sources using Logi
data services. It does this by making several special elements available
in Logi Studio. These include the **Thinkspace** element, which
provides a highly-interactive analysis experience. In its interface,
best-fit visualization suggestions are automatically referred to the user
by a built-in "recommendation engine" and data is organized
using intelligent technology that clusters data to make it more easily
consumable by users.

The DM is installed separately, after Logi Info and, if using it, the SSRM
are installed. Please note these important restrictions:

![](https://devnet.logianalytics.com/hc/article_attachments/7522725179159/noteicon.png) Advanced features discussed here work with Logi Info v12.5 and later, 64-bit version (there is no 32-bit version available). Earlier
and later Info versions may not support them; consult the [Release Notes](https://documentation.logianalytics.com/inf/content/release-notes.htm)
for specific details.

Databases supported include:

* AWS Redshift
* Infobright
* JDBC database providers
* MS SQL Server
* MySQL
* Oracle
* PostgreSQL
* Snowflake
* Vertica

Logi Info applications on IIS that utilize DM v3.1+ must run using an
Application Pool configured for *Integrated* pipeline mode.
*Classic* pipeline mode Application Pools will *not* work.

If you're using Internet Explorer 11, the Internet Options![](https://devnet.logianalytics.com/hc/article_attachments/7522803222807/menuarrowrt.png)Security setting for applications using this technology must be set to
*Medium High* or lower.

## Important Java Information

Starting in January 2019, Oracle discontinued its free, long-term support
of the **Oracle Java Development Kit** (JDK) for enterprises. The
impact of this on Logi products is discussed in detail in [Java Usage Policy](https://devnet.logianalytics.com/hc/en-us/articles/4419723053335-Java-Usage-Policy).

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png)
As a result, Logi no longer distributes the Oracle JRE as part of
the Discovery installation.
*Prior to installing Discovery 3.2, you must have OpenJDK 12 installed;
Oracle JRE is not supported.*

When you install OpenJDK, you must configure your Windows
SystemVariables properly. See
[Install the Discovery Module - Windows - Setting Windows SystemVariables for OpenJDK](https://devnet.logianalytics.com/hc/en-us/articles/4419707630487-Install-the-Discovery-Module-Windows-Setting-Windows-SystemVariables-for-OpenJDK) for more information.

## What Gets Installed

The following components will be installed on the web server:

* An embedded, runtime environment for server-side web applications ([node.js](https://nodejs.org/))
* An embedded, Java-based relational database ([H2](http://www.h2database.com/html/main.html))

Node.js and H2 are extremely compact, have a small installation footprint,
and do not install a lot of extra tools or management utilities. They're
provided as transparent services that require little or no management.

Two Windows services are created during the installation:
*Logi Application Service* and *Logi Data Service*.

## Important Upgrade Information

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png)
If you're upgrading from earlier versions of Discovery, please
*uninstall* the earlier version first, using Control Panel, and at
the end of the process be sure to respond "Yes" when prompted to
remove logs and the database. Then run the Discovery 3.1+ installer to
create a fresh installation.

## Release Pairings

Information about which Logi Info and DM versions should be used together
is available in
[Add-on Modules](https://devnet.logianalytics.com/hc/en-us/articles/4419723002647-Add-on-Modules). For more information, see the [Release Notes](https://documentation.logianalytics.com/inf/content/release-notes.htm) for each Logi
Info version.
