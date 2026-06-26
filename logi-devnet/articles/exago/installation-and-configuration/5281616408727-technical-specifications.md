---
title: "Technical Specifications"
id: 5281616408727
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281616408727-Technical-Specifications
updated_at: 2024-08-22T13:08:47Z
---

# Technical Specifications

# Technical Specifications

## Operating Systems

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/25509819710103 "Important")
>
> When using Content Security Policy (CSP) rules in the web server configuration, additional response headers are required for compatibility with Exago. See [Security Checklist](https://devnet.logianalytics.com/hc/en-us/articles/5281588834455-Security-Checklist) for more information.

### Windows

* Windows Server 2012+ / Windows 10
* Internet Information Services (IIS) 7+
* .NET Framework 4.6.1+, version 4.7.2 recommended

### Linux

#### Supported/Recommended Distributions

* Ubuntu 14+

#### Additional Distributions

* Red Hat Enterprise Linux 7
* Oracle Linux 7
* SUSE Linux Enterprise Server 12
* CentOS 7
* Fedora 21-25
* Debian 8-9

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/25509819710103 "Important")
>
> Exago is incompatible with SELinux.

### Requirements

Exago is not compatible with mono versions installed from system repositories. It is highly recommended that only official mono-project repositories are used or that the Exago installer install mono.

#### Mono

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/25509819710103 "Important")
>
> These are the only versions of Mono that are compatible with Exago. In addition, the Exago installer will install a patched version of `System.Web.dll`. This patch  [can also be installed manually](https://devnet.logianalytics.com/hc/article_attachments/25509810021783).

* mono 5.10.1.20, 6.8.0.105 or 6.8.0.123 (*v2020.1+*).
* *Optional*: mono-basic, which provides support for VB.NET

#### Apache 2.4+

* mod-mono

#### NGINX

* mono-fastcgi-server4

The Exago installer can automatically download and install supported versions of mono, mod-mono or mono-fastcgi-server4.

## Data Sources

### Fully Supported

* + Microsoft SQL Server 2000+
  + PostgreSQL 7.1+
  + Oracle Version 9i+
  + MySQL 5.0+
  + Amazon Aurora
  + IBM DB2
  + IBM Informix

* SQLite v2021.1.8+

#### Partially Supported

* MariaDB
* Microsoft OLAP†

#### Not Currently Supported

* Elasticsearch
* MongoDB
* Redshift
* Snowflake

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/25509819710103 "Critical") **Important:**
>
> As of v2024.2.1, CData drivers are no longer available for use in Exago BI products. See **[CData Drivers](https://devnet.logianalytics.com/hc/en-us/articles/5281585000599)**.

† Limited support available, see [OLAP and MDX Queries](https://devnet.logianalytics.com/hc/en-us/articles/5281617045911-Data-Sources#OLAP).

### Database APIs

* ODBC
* .NET Assembly Methods

### Files

* XML
* Excel

## Data Object Types

* Database Tables
* Database Views
* Stored Procedures
* Database Functions
* Parameterized SQL Statements
* .NET Assembly Methods

## Browsers

Exago BI targets the most current stable versions of the following web browsers.

### Desktop

Desktop browsers support the full user interface and Admin Console.

* Mozilla Firefox
* Internet Explorer 11
* Microsoft Edge
* Google Chrome
* Apple Safari (Mac OS)

### Mobile

Mobile browsers support viewing report output in the embedded Report Viewer and Dashboard Viewer.

* Google Chrome
* Apple Safari

## Storage

### Reports

* **Storage Management** (*v2020.1+*) — see [Storage Management: Introduction](https://devnet.logianalytics.com/hc/en-us/articles/5281647019287-Storage-Management-Introduction)
* **File System** (*pre-v2020.1*)
* **Custom Folder Management** (*pre-v2020.1*) — see [Folder Management](https://devnet.logianalytics.com/hc/en-us/articles/5281620756119-Folder-Management).
  + .NET
* **Azure File/Blob Storage** (*pre-v2020.1*)

### Schedules

* **File System**
* Scheduler Queue (custom)
  + .NET

### Configuration

* **File System**
* **Azure Blob Storage**

## Application Integration

AJAX enabled — .NET API and REST Web Service API for communication between Exago and host application

* **Server-side**
  + .NET API
  + REST API
* **Client-side**
  + JavaScript
  + iframe

## Extensibility

* **Custom Functions**
  + .NET
  + JavaScript (server-side)
* **Server Events**
  + .NET
  + JavaScript (server-side)
* **Action Events**
  + .NET (server-side) + JavaScript (client-side)
  + JavaScript (server- & client-side) [*Windows only*]
