---
title: "Datasource Connections"
id: 4406817671447
section: "Connect to Data - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817671447-Datasource-Connections
updated_at: 2022-04-06T06:07:30Z
---

# Datasource Connections

# Datasource Connections

A *datasource connection* is the mechanism used by Logi applications to communicate with datasources through a driver or provider for the purpose of reading and writing data. Selecting and configuring a **Connection** element is the first step in the process of developing most Logi applications; connections are discussed in this topic.

The following topics provide more details about the available datasource connections:

* [Using the Connection Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4406817676567-Using-the-Connection-Wizard)
* [Using Vendor-Specific Connections](https://devnet.logianalytics.com/hc/en-us/articles/4406817679639-Using-Vendor-Specific-Connections)
* [Using Generic Connections and Connection Strings](https://devnet.logianalytics.com/hc/en-us/articles/4406817677591-Using-Generic-Connections-and-Connection-Strings)
* [Using Special-Purpose Connections](https://devnet.logianalytics.com/hc/en-us/articles/4406817678615-Using-Special-Purpose-Connections)
* [Creating Dynamic Connections](https://devnet.logianalytics.com/hc/en-us/articles/4406817666199-Creating-Dynamic-Connections)
* [Connecting with Metadata](https://devnet.logianalytics.com/hc/en-us/articles/4406817662743-Connecting-with-Metadata)
  + [1010data](https://devnet.logianalytics.com/hc/en-us/articles/4406817661463-1010data)
  + [Amazon Redshift](https://devnet.logianalytics.com/hc/en-us/articles/4406822426775-Amazon-Redshift)
  + [Connection.ADO Configuration](https://devnet.logianalytics.com/hc/en-us/articles/4406817663767-Connection-ADO)
  + [Connection.JDBC and SQL Server 2008](https://devnet.logianalytics.com/hc/en-us/articles/4406817665047-Connection-JDBC-and-SQL-Server-2008)
  + [Connection.LDAP Configuration](https://devnet.logianalytics.com/hc/en-us/articles/4406822427927-Configuring-Connection-LDAP)
  + [Database Browser and SQL Builder](https://devnet.logianalytics.com/hc/en-us/articles/4406817667351-Database-Browser-and-Query-Builder-Connections)
  + [HP Vertica](https://devnet.logianalytics.com/hc/en-us/articles/4406817668375-HP-Vertica)
  + [DB2 Universal](https://devnet.logianalytics.com/hc/en-us/articles/4406817669399-IBM-DB2-Universal)
  + [DB2 on iSeries](https://devnet.logianalytics.com/hc/en-us/articles/4406817670423-IBM-DB2-on-iSeries)
  + [Microsoft SQL Server](https://devnet.logianalytics.com/hc/en-us/articles/4406817672471-Microsoft-SQL-Server)
  + [MongoDB](https://devnet.logianalytics.com/hc/en-us/articles/4406817673495-MongoDB)
  + [Oracle](https://devnet.logianalytics.com/hc/en-us/articles/4406817674519-Oracle)
  + [SAP Sybase](https://devnet.logianalytics.com/hc/en-us/articles/4406817675543-SAP-Sybase)

## About Datasource Connections

Logi applications connect to a datasource in order to read and write its data. In most cases, this is done using a **Connection** element, which specifies the nature of the communication, including security credentials.

The exceptions are for accessing certain kinds of files, such as XML, CSV, and Excel files, which your Logi application is able to access directly through the web server file system. These sources *do not* use Connection elements.

Connection elements do not work with datasources requiring SSH.

Connection elements are configured in the \_Settings definition and are therefore available application-wide. One connection can be used for multiple report definitions, and a Logi application can have multiple connections, allowing data from multiple sources to be included in a single report. There are three types of connection elements:

### Vendor-Specific Connections

Vendor-specific connection elements, such as **Connection.MySQL**, are the connections we recommend you use. They provide the best performance and easiest configuration. The available vendor-specific Connection elements include:

* Connection.DB2
* Connection.Google Docs
* Connection.Google Maps
* Connection.MongoDB
* Connection.MySQL
* Connection.OpenEdge
* Connection.Oracle
* Connection.PostgreSQL
* Connection.Redshift
* Connection.Salesforce
* Connection.SQLServer (Microsoft)
* Connection.Sybase
* Connection.Twitter
* Connection.Vertica

Your Logi product, in combination with the .NET framework or Java libraries, contains all of the underlying *drivers* or *providers* necessary to make all of these connections work, except for **Oracle**, **DB2**, and **Sybase.** Due to licensing restrictions, these connections are only usable if you have the client driver software that's distributed
with the database server, or that you download. See the *Usage Notes* sections for each of these systems on page two for information about their drivers.

MySQL 5.5 is not supported for use with our [DataLayer.ActiveSQL](https://devnet.logianalytics.com/hc/en-us/articles/4406817277847-DataLayer-ActiveSQL) technology.

The configuration of **Connection.Google Docs** and **Connection.Google Maps** is discussed in [Google Connections](https://devnet.logianalytics.com/hc/en-us/articles/4406817485335-Google-Connections).

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Salesforce.com has discontinued support for the TLS 1.0 protocol. If you're using **Connection.Salesforce**, or REST or SOAP API connections to Salesforce, you must be using Logi Info v12.2-SP4 or later, which supports the TLS 1.1 and 1.2 protocols. In addition, Login Java applications
must use JDK or OpenJDK 8 or later to use the appropriate protocol
version.
For more information about which versions of JDK works with Info, see [Java Usage Policy](https://devnet.logianalytics.com/hc/en-us/articles/4406817692055-Java-Usage-Policy).

The most recent .NET and Java drivers shipped with Logi Info v12.6 only work with **MongoDB** 2.6 and later. If you're using an older version of MongoDB, such as 2.4, you cannot upgrade your Logi application to Info v12.6.

### Generic Connections

Generic connection elements, such as **Connection.OLEDB**, require you to provide, or use a wizard to construct, a "connection string". Connection strings are text strings that are passed in code to an underlying driver or provider in order to initiate the connection. The available generic Connection elements include:

* Connection.ADO
* Connection.JDBC
* Connection.LDAP
* Connection.ODBC
* Connection.OLAP
* Connection.OLEDB
* Connection.SMTP

**Connection.OLAP** is used to connect to Microsoft Analysis Services OLAP databases and **Connection.SMTP** is used to connect to SMTP email servers.

The other generic elements are for connection to a variety of databases. For example, the **Connection.OLEDB** element allows you to use the Microsoft Jet driver to connect to MS Access database files and can also be configured to connect to Microsoft's SQL Server database server.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Microsoft elected not to include the MS Jet driver in its 64-bit OS versions, but it is possible to use the "MS Ace" OLEDB driver, distributed with Office 2007, instead.

### Special-Purpose Connections

*Special-purpose* connection elements, such as **Connection.Web Service,** are designed to connect with specific web services or special Logi services. The available special-purpose Connection elements include:

* Connection.DataHub
* Connection.HTTP
* Connection.Leaflet Map
* Connection.Logi Application Service
* Connection.OData
* Connection.REST
* Connection.Scheduler
* Connection.Web Service (SOAP)

**Connection.DataHub** is used to connect to our Logi DataHub data virtualization product.
**Connection.Logi Application Service** is used to connect to Logi Platform Services, installed with Logi Info 12.5+ or the Discovery Module 3.0.
**Connection.HTTP** allows the following datalayers to use a connection to an HTTP or HTTPS datasource that requires authentication:

* DataLayer. CSV
* DataLayer.Excel
* DataLayer.Fixed Format File
* DataLayer.GPX File
* DataLayer.JSON
* DataLayer.KML File
* DataLayer.Web Feed
* DataLayer.Web Scraper
* DataLayer.XML

The **Request Header** is a child element of Connection.HTTP and Connection.REST. This element allows custom information, primarily intended for authentication purposes, to be sent through the connection in the HTTP request header.

**Connection.Leaflet Map** is used to connect to a Leaflet API-compatible map server. See [Leaflet Maps](https://devnet.logianalytics.com/hc/en-us/articles/4406817701527-Leaflet-Maps) for more information.

The **Connection.Logi Application Service** element is used to connect to a special service installed with the Discovery Module and is only availablein Logi Info if the add-on moduleis installed. Connection configuration details are available in [Develop with the Discovery Module 3.1](https://devnet.logianalytics.com/hc/en-us/articles/4406822291479-Develop-with-the-Discovery-Module-3-1).

**Connection.OData**, and its **OData Parameters** child element, allow connection to REST-style APIs.

**Connection.REST** and **Connection.Web Service** are similar, in that they both connect to web services. However, Connection.REST works with Representational State Transfer (REST) protocols, such as HTTP, and Connection.Web Service works with the SOAP protocol.
**Connection.Scheduler** is used with the Logi Scheduler service provided in Logi Info to manage scheduled reporting.

### The Studio Connection Element

Logi Studio includes tools, like the SQL Query Builder and the Database Browser, that normally use the configured Connection elements to transparently connect to the data during development.
However, for a variety of reasons, the Windows development machine where Studio is installed may not be able to use the configured data connections. For instance, the driver may not be installed on, or may be incompatible with, the Windows machine running Studio. In this case, a special **Studio Connection** element can be added to provide a separate connection for Studio's tools. Studio Connection is available as a child of the following connections:

* Connection.DataHub
* Connection.DB2
* Connection.JDBC
* Connection.MySQL
* Connection.Oracle
* Connection.PostgreSQL
* Connection.Redshift
* Connection.SQLServer
* Connection.Sybase
* Connection.Vertica
