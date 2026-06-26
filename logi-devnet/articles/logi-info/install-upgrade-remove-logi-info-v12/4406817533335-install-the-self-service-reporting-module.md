---
title: "Install the Self-Service Reporting Module"
id: 4406817533335
section: "Install, Upgrade, & Remove - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817533335-Install-the-Self-Service-Reporting-Module
updated_at: 2022-04-06T06:06:42Z
---

# Install the Self-Service Reporting Module

# Install the Self-Service Reporting Module

The Logi Self-Service Reporting Module (SSRM) is an add-on module that
enables special elements in Logi Info and adds a complete, pre-built Logi
application to your computer.

The following topics guide you through installing the
Self-Service Reporting Module on a single computer under the
Windows operating system:

* [Preparing to Install](https://devnet.logianalytics.com/hc/en-us/articles/4406817534487-Install-the-Self-Service-Reporting-Module-Preparing-to-Install#Preparing)
* [Installing the Software](https://devnet.logianalytics.com/hc/en-us/articles/4406822368663-Install-the-Self-Service-Reporting-Module-Installing-the-Software#StartInstall)
* [Removing or Repairing the Installation](https://devnet.logianalytics.com/hc/en-us/articles/4406822369559-Install-the-Self-Service-Reporting-Module-Removing-or-Repairing-the-Installation#Removing)

We have a separate topic,
[Upgrade the Self-Service Reporting Module](https://devnet.logianalytics.com/hc/en-us/articles/4406817916311-Upgrade-the-Self-Service-Reporting-Module), that provides guidance for installing an upgrade. Information about which Logi Info and Self-Service Reporting Module
versions we recommend using together is available in
[Release Pairings](https://devnet.logianalytics.com/hc/en-us/articles/4417584258327-Release-Pairings). For more information, see the [Release Notes](https://clm.logianalytics.com/rdPage.aspx?rdReport=RelNotesINF) for each Logi
Info version.

## About the Self-Service Reporting Module

The special SSRM elements installed can be used with the Analysis Grid in
your applications and make it easy for users to configure data queries at
runtime, as described in
[The Analysis Grid for Developers](https://devnet.logianalytics.com/hc/en-us/articles/4406816977175-The-Analysis-Grid-for-Developers).

The included application, **InfoGo**, uses the special SSRM elements
and allows users to create and share visualizations, dashboards, and
reports at runtime. We've provided a guide for end-users,
[InfoGo - Use InfoGo](https://devnet.logianalytics.com/hc/en-us/articles/4406822566807-InfoGo-Use-InfoGo). Developers can examine InfoGo for educational purposes and can also
customize its branding and other features, if desired. InfoGo can be
deployed to .NET and Java servers.

After the SSRM installer finishes, there are several things you need to do
to complete the installation. These are explained in
[Configure InfoGo for Developers](https://devnet.logianalytics.com/hc/en-us/articles/4406822193431-Configure-InfoGo-for-Developers).

### Important Restrictions

Please note these important restrictions on the use of the SSRM:

* Requires Logi Info v12 or later, 64-bit version (there is no 32-bit SSRM
  version available).
* Works with Chrome, Firefox, and other major browsers, but
  *does not* work with Internet Explorer 7 or 8.

The **Active Query Builder** and **Metadata** elements and InfoGo
application installed with the SSRM only work with these database
sources:

* 1010data
* DB2
* Microsoft SQL Server 2005+
* MySQL
* Oracle
* PostgreSQL
* Redshift (Amazon)
* Vertica (HP)
* ODBC- and JDBC-accessible databases that use the same SQL syntax as one
  of the databases listed above

Ensure that your environment meets these restrictions prior to
installation!
