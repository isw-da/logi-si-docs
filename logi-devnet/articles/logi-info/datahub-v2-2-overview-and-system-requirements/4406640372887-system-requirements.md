---
title: "System Requirements"
id: 4406640372887
section: "DataHub v2.2 Overview and System Requirements"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406640372887-System-Requirements
updated_at: 2022-04-01T03:13:25Z
---

# System Requirements

# System Requirements

This topic presents the hardware and software requirements for Logi DataHub.

* [General Requirements](#General)
* [Installation Scenarios](#Scenarios)

## General Requirements

DataHub is a web-based application that includes a columnar data repository. While
DataHub can be installed on a desktop or laptop machine, we recommend that you install it on a fixed server with appropriate resources. The general requirements are:

| Category | Requirements |
| --- | --- |
| Server Memory | 16GB RAM minimum, for testing and evaluation.  32GB RAM minimum, for production environments (more recommended). |
| Server Storage | 4GB hard drive (minimum), for software installation, + 1GB (minimum) for data, Additional GB storage for data as necessary, secondary drive recommended for data loads. |
| Supported Operating Systems | Logi DataHub is only available in a 64-bit version, for:   * Windows Server 2012, Windows Server 2012 R2 * Windows Server 2008 R2 * Windows 10 * Windows 8.1, Windows 8 * Windows 7   *Not supported:*   * Windows 10 Anniversary Update version 1607 (OS Build 14393.10) * Windows Server 2016 |
| Supported System Software | Logi DataHub works with IIS 7+. If IIS is not already installed, or if you prefer, the DataHub installer can also install IIS Express.  The DataHub installer will also install .NET Framework 4.5 and configure required sharing permissions. |
| Data Sources | The following data sources are supported:   | * Microsoft SQL Server * MySQL * ODBC database providers * OLEDB database provers * Oracle * PervasiveDB * PostgresSQL * Vertica  * Microsoft Excel file * CSV data file | * Amazon Dynamo DB\* * Eloqua * Facebook * Financial Accounts (OFX)\* * Freshbooks\* * Google Analytics * Google Spreadsheets\* * HubSpot * Marketo * Microsoft Dynamics CRM Online * Microsoft Dynamics CRM On Premise\* * Microsoft Dynamics GP\* * Netsuite\* * OData\* * Quickbooks Online * Quickbooks On Premise\* * Quickbooks POS\* * Salesforce * SAP Netweaver\* * Twitter |   *\* These applications use a generic ADO.NET connector; please contact Logi Support if you need configuration assistance.* |
| Supported Browsers | Logi DataHub is a web-based application that takes advantage of the latest HTML5 technologies. It is currently compatible with the following web browsers.   * Google Chrome - v26+ * Firefox - v20+ * Internet Explorer - v10+ * Safari - v6+ |

## Installation Scenarios

Logi DataHub allows for several installation modes:

**Standalone -**Installs a single-user, standalone instance of
DataHub. In addition to DataHub, the installer will also install an IIS Express service to deliver the web content.

**Workgroup  -** Installs an instance intended to be accessed by multiple users. The installer will configure a web site under IIS to deliver the web content.

**Two-Tier** - You can also choose to install a two-tier application, wherein the
DataHub Data Repository is installed on a separate database server machine.
In this scenario, the repository must be installed on the database
server *before* the DataHub Web Application is installated on the web server.
