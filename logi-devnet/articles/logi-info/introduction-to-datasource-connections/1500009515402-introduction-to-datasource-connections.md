---
title: "Introduction to Datasource Connections"
id: 1500009515402
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009515402-Introduction-to-Datasource-Connections
updated_at: 2021-06-17T01:58:26Z
---

# Introduction to Datasource Connections

# Introduction to Datasource Connections

A *datasource connection* is the mechanism used by Logi applications to communicate with datasources through a driver or provider for the purpose of retrieving or updating data. Selecting and configuring a connection is the first step in the process of developing Logi applications that work with data; connections are discussed in this topic.

* About Connections
* [Use Vendor-Specific Connections](#Vendor)
* [Use Generic Connections and Connection Strings](#Generic)
* [Use Special-Purpose Connections](#Special)
* [Create Dynamic Connections](#Dynamic)
* Special Considerations:

+ [Oracle 8.1.7 Client Error](#Ora817)
+ [Oracle 32-bit Software on Windows 64-bit OS](#Ora3264)
+ [Database Browser and Query Builder Connections](#DBQBConn)
+ [Connection.JDBC and SQL Server 2008](#JDBC2008)
+ [JDK 1.7 and SQL Server 2005+](#JDK7)
+ [Configuring Connection.LDAP](#LDAP)
+ [About MongoDB](#MongoDB)
+ [About Amazon Redshift](#Redshift)
+ [About HP Vertica](#Vertica)

## About Connections

Logi applications connect to a datasource in order to retrieve and, sometimes update, its data. In most cases, this is done using a **Connection** element, which specifies the nature of the communication with the datasource, including security credentials.

The exceptions are certain kinds of flat files, such as XML, CSV, and Excel files, which your Logi application is able to access directly through the web server file system. These situations employ datalayers but do not need connections.

Connection elements are configured in the \_Settings definition and are therefore available application-wide. One connection can be used for multiple report definitions, and a Logi application can have multiple connections, allowing data from multiple sources to be included in a single report.

There are *vendor-specific* Connection elements, such as **Connection.MySQL**, *generic* Connection elements, such as **Connection.OLEDB**, and *special-purpose* connections, such as **Connection.Web Service,** for your use.

Generic connection elements require you to provide, or use a wizard to construct, a *connection string*. These are text strings that are passed in code to an underlying driver or provider in order to initiate the connection; they're discussed in a later section.

Vendor-specific connection elements do the job of creating a connection string for you in most cases, using the values you enter as attributes, or do not use traditional connection strings.

Special-purpose connections are designed to ease communication with specific web services or Logi services.

### Vendor-Specific Connections

The available vendor-specific Connection elements include:

|  |  |
| --- | --- |
| * Connection.DB2 * Connection.Google Docs * Connection.Google Maps * Connection.MongoDB * Connection.MySQL * Connection.Oracle * Connection.PostgreSQL | * Connection.Redshift * Connection.Salesforce * Connection.SimpleDB * Connection.SQLServer * Connection.Sybase * Connection.Twitter * Connection.Vertica |

Your Logi product, in combination with the .NET framework or Java libraries, contains all of the underlying *drivers* or *providers* necessary to make all of these connections work, except for two:

Due to licensing restrictions, the **DB2** and **Sybase** connections are only usable if you already have the client or provider software that's distributed with the database server. In the case of the Sybase connection, you must have installed the ADO.NET 2.0 data provider from Sybase, which is
typically included on your Sybase CDs or can be downloaded from the Sybase web
site. Logi products *do not* include providers for these two connections.

**Connection.SQLServer** is for use with Microsoft's SQL Server database server. **Connection.Twitter** uses the Twitter API to interact with the popular social networking web site.

If you're using a version of Logi Info or Logi Report earlier than 9.5.46, some or all of the vendor-specific connection elements may not be available to you. You will have to use a generic connection and build a connection string.

### Generic Connections

The available generic Connection elements include:

|  |  |
| --- | --- |
| * Connection.JDBC * Connection.LDAP * Connection.ODBC | * Connection.OLAP * Connection.OLEDB * Connection.SMTP |

**Connection.OLAP** is used for connection to XML/A OLAP databases and **Connection.SMTP** is for connecting to SMTP email servers. The other generic elements are for connection to a variety of databases.

For example, the **Connection.OLEDB** element allows you to use the Microsoft Jet driver to connect to MS Access database files and can also be configured to connect to Microsoft's SQL Server database server. Note that Microsoft elected not to include the MS Jet driver in its 64-bit OS versions, but it is possible to use the "MS Ace" OLEDB driver, distributed with Office 2007, instead.

### Special-Purpose Connections

The available special-purpose Connection elements include:

|  |  |
| --- | --- |
| * Connection.HTTP * Connection.REST | * Connection.Scheduler * Connection.Web Service |

**Connection.HTTP**, added in v11.0.416, allows the following datalayers to use a connection to an HTTP or HTTPS datasource that requires authentication:

|  |  |
| --- | --- |
| * DataLayer. CSV * DataLayer.Excel * DataLayer.Fixed Format File * DataLayer.GPX File * DataLayer JSON File | * DataLayer.KML File * DataLayer.Web Feed * DataLayer.Web Scraper * DataLayer.XML File |

**Connection.REST** and **Connection.Web Service** are similar, in that they both connect to web services. However, Connection.REST works with Representational State Transfer (REST) protocols, such as HTTP, and Connection.Web Service works with the SOAP protocol.

In v11.0.727 the **Request Header** element was added as a child of Connection.HTTP and Connection.REST. This element allows custom information, primarily intended for authentication purposes, to be sent through the connection in the HTTP request header.

**Connection.Scheduler** is used with the Logi Scheduler service provided in Logi Info to manage scheduled reporting. The other connection elements are used with web services.

## Use Vendor-Specific Connections

Vendor-specific Connection elements are designed to make configuring a connection very simple.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778576919/introconn_01.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402778577175/introconn_01a.png)

As shown in the example above, a **Connection.MySQL** element has been added to the \_Settings definition in an application. Its attributes allow the developer to specify the server name, database name, and access credentials. At runtime, whatever connection string may be required will be automatically created behind-the-scenes using this information. The developer does not need to know the specific format of the connection string.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771699735/introconn_02.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771700375/introconn_02a.png)

Optional parameter elements, as shown above, can be added beneath the connection element. These provide the flexibility of including additional connection string parameters, if necessary. For example, the optional parameters for the MySQL connection include Compress, Connection Lifetime, Direct, Embedded, Port, Protocol, and Unicode.

The other attributes for Connection.MySQL and similar connection elements, are:

| Attribute | Description |
| --- | --- |
| ID | (Required) A unique element ID; referred to by datalayer elements that use this connection. |
| Command Timeout | Specifies the amount of time, in seconds, before the request to connect to the datasource is presumed to have failed. For most datasources, the default value is *60* seconds. For MySQL, the default is *30* seconds. In v10.2.224+, specify *0* to disable the timeout. |
| MySql Connection String | A fully-formed connection string for the MySQL database. If a value is defined here, all other attributes will be ignored and this string will be used to connect to the database. Any child parameter elements are processed and added to the connection string. |
| MySql Port | The port address of the MySql database. Default: *3306*. |

In general, vendor-specific connections are much easier to configure than generic connection and developers should look to them first when creating applications.

**Connection.Google Docs -** Google, as of mid-June 2015, added an optional, additional layer of security for its services. The Connection.Google Docs element *does not* make use of this additional security and you may need to configure your Google account to allow that. If you get "invalid account or password" error messages when you run your Logi application, see [this](https://support.google.com/accounts/answer/6010255?hl=en#zippy=%2Cif-less-secure-app-access-is-on-for-your-account) Google Help page. Note that any changes you make affects *all* apps using your account.

## Use Generic Connections and Connection Strings

An alternate method of creating a connection is to use one of the generic Connection elements, which requires that you provide a connection string for it.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771700759/introconn_03.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771701015/introconn_03a.png)

In the example shown above, a **Connection.OLEDB** element has been added to the \_Settings definition. Its **Connection String** attribute has been configured with a connection string, which looks like this in its entirety:

Provider=SQLOLEDB.1;Password=password;Persist Security Info=True;User ID=user;Initial Catalog=Northwind;Data Source=myDBServer

You can see that the connection string has a specific format, which is unique to the connection type. The Connection.OLEDB element can invoke a special wizard to build its connection string; for all other connections, developers will need to provide an appropriate string.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771701271/introconn_04.png)

The **Data Link Properties** wizard, shown above, assists in the creation of connection strings for the Connection.OLEDB element. In Studio, click the little browse button at the end of the element's Connection String attribute value to invoke the wizard.

The **Test Connection** button only ensures network connectivity to the database server - it *does not* guarantee that the User Name and Password entered are valid! The test can be successful and yet you may still not be able to access the data if the credentials are wrong. If providing specific credentials, be sure that you enter them carefully and check *Allow saving password*.

This very useful web site: [http://www.ConnectionStrings.com](http://www.connectionstrings.com/) provides example connection strings for a wide variety of datasources and can assist in providing the proper format for strings for other connection types.

### Notes For Java Developers

When using **Connection.JDBC** element, specifying an IP address instead of a host name in the connection string may significantly increase the connection opening time, due to the underlying Java implementation. Therefore, it is recommended that developers use host names, not IP addresses, in connection strings to minimize the time it takes to open a connection.

Logi Studio includes tools, like the Query Builder and Database Browser, and uses information from the Connection elements to transparently connect these tools to the data. However, as a .NET application, Studio can't use the information from Connection.JDBC for this purpose. So, as of v10.0.189, Studio includes a special element, **Studio Connection**, a child of Connection.JDBC, which lets developers specify separate, non-JDBC connections for Studio's tools.

The **Connection.SMTP** element supports TLS/SSL authentication in Java applications only. This allows connection to Gmail and other similar services that will programmatically send email on your behalf. Set the element's **SMTP Authentication Mode** attribute to *3* to select TLS/SSL.

## Use Special-Purpose Connections

Special-purpose connections are used to connect to specific web services or to the Logi Scheduler service (Logi Info only). All require credentials to authenticate the connection.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771701655/introconn_05.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771701911/introconn_05a.png)

In the example shown above, a **Connection.Web Service** element has been added to the \_Settings definition. The attributes identify specific aspects of the web service. As with all connections, a unique ID is required so that it can be referenced later by datalayer elements.

For developers connecting to their *own* web service, note that the WSDL document specified in this connection element's required WSDL URL attribute must be "valid", meaning that it can contain no errors that would cause it to fail to compile. A document that's readable but that will not compile is invalid and will cause the connection to fail.

Connection.Web Service has an optional child element, **Connector Property Parameters**, which makes it possible to connect to a web service which requires special
authentication and proxy settings.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771702167/introconn_06.png)![](https://logianalytics.zendesk.com/hc/article_attachments/4402771702423/introconn_06a.png)

In the example shown above, a **Connection.REST** element has been added to the \_Settings definition. Its **Url Host** attribute identifies the web service host address, and other attributes are used to provide user credentials, if required. As with all connections, a unique ID is required so that it can be referenced later by datalayer elements.

## Create Dynamic Connections

*Features discussed in this topic are not available in Logi Report.*

You may want to create *dynamic* connections, which connect to a datasource based on external criteria. Connection elements make this possible by accepting tokens in their attributes.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771702679/introconn_10.png)

In the example above, tokens are used in the attributes of the **Connection.SQL Server** element. Another approach is to assign a complete *connection string* to a Session variable and use its token in the **Connection String** attribute, as shown above right. A value in that attribute will cause the "required" attributes to be ignored.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771702935/introconn_11.png)

Finally, you can enter the literal connection string text into that attribute, as shown above, and tokenize parts of it, like this:

`Server=@Session.DBServer;Database=@Session.DBName~;User Id=@Function.UserID~; Password=@Session.DBPassword;`

There are a variety of techniques available for setting the token values prior to the processing of the \_Settings definition. For Logi Info developers, the Startup Process element (see *The \_Settings Definition*), when included in \_Settings, can be used to call a Process task that assigns the Session variables needed. This task will run before the Connection elements are processed.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778580887/introconn_12.png)

The example shown above is simplistic but shows you how to use a Process task to set Session variables, which can be used later as tokens in the Connection element's attributes.

If you're unable to use the Startup Process element for some reason, you can still make the Process task run by calling it directly, rather than calling the default report definition:

http://yourServer/yourLogiApp/rdProcess.aspx?rdProcess=yourProcessDefinition&rdTaskID=taskStartUp

## Special Considerations

The following considerations apply to connections:

### "Oracle 8.1.7 Client Required" Error

Oracle connections may fail, displaying the Inner error message "System.Data.OracleClient requires Oracle client software version 8.1.7 or greater." in the Debugging Trace Page. This may occur even though the Query Builder is able to connect to the database, and even though a later version of the Oracle Client has been installed.

A likely cause of this problem is that the ASPNET account, under which the web server runs, does not have **access permissions** to the folder that contains the Oracle Client. Granting the ASPNET account **Read** and **Execute** permissions for the folder that contains the client will usually resolve this problem.

### Oracle 32-bit Software on Windows 64-bit OS

If you're attempting to connect to an Oracle database from a Windows platform using one of the following programmatic interfaces: ODBC, OLEDB, OO4O, or ODP.NET, after installing 32-bit Oracle client software on a 64-bit Windows operating system (OS) you may receive one of the following errors:

     ORA-12154: TNS:could not resolve the connect identifier specified    
     ORA-6413:  Connection not open.

This is because the 64-bit Windows OS installs 32-bit software by default into a folder beneath C:\Program Files (x86) and the presence of parenthesis in the file path is unacceptable to the Oracle software. This is a known bug that Oracle may fix in the future. Until then, you must install the Oracle 32-bit client software elsewhere than the default location.

### Database Browser and Query Builder Connections

The Database Browser and Query Builder tools *will* work with the databases for which we provide "native" Connection elements, such as Oracle\*, MS SQL Server, and MySQL. They *may* work with other databases that use a connection that mimics that of a database for which we provide a native connection, such as Netezza ![](https://logianalytics.zendesk.com/hc/article_attachments/4402778416151/menuarrow.gif) PostgreSQL. They are not guaranteed to
work with every possible database and, in that case, we recommend that you use tools provided with the database to examine and manipulate data, and create and test queries, outside of Studio.

\* Due to the way in which Oracle configures its software, the Database Browser and Query Builder will *not* connect, using our native Connection.Oracle element, to Oracle databases when Logi Studio is run on a 64-bit platform. In this situation, developers can choose to do without these tools or to use Connection.ODBC to connect.

### Connection.JDBC and SQL Server 2008

Developers creating Logi applications for Java, and using Connection.JDBC to connect to Microsoft SQL Server 2008, may encounter the following errors:

There was a problem running a DataLayer. The error was: Could not open the supplied connection to the data.

The server version is not supported. The target server must be SQL Server 2000 or later.

This occurs when a newer JDBC driver is required for SQL Server 2008. The solution is:

1. [Download a new driver](http://www.microsoft.com/downloads/en/details.aspx?FamilyID=99b21b65-e98f-4a61-b811-19912601fdc9&displaylang=en) and uncompress the download.
2. From the download, copy the file sqljdbc4.jar to your Logi application's WEB-INF/lib folder.
3. Delete the old driver, sqljdbc.jar, from the same folder.
4. Restart the web server.
5. Run the Logi application.

If the following error message is received:

Java Runtime Environment (JRE) version 1.6 is not supported by this driver. Use the sqljdbc4.jar class library, which provides support for JDBC 4.0.

it means you either did not remove the original sqljdbc.jar, replaced it with the sqljdbc.jar file that came with the download instead of adding sqljdbc4.jar to the folder, or did not restart the web server.

### Use JDK 1.7 and SQL Server 2005+

In v11.0.416, our SQL Server JDBC driver was upgraded to work with JDK 1.7 and MS SQL Server 2005+. The previous version of the driver's sqljdbc4.jar file, however, is still provided, as sqljdbc4.old, for users who work with MS SQL Server 2000.

### Configure Connection.LDAP

The Connection.LDAP element has the following attributes:

| Attribute | Description |
| --- | --- |
| Base DN | (Required for Java, ignored for .NET) Specifies the top level of the LDAP structure, its "base Distinguished Name". The attribute value is derived from the company DNS domain name components. For example, to connect to an LDAP server within the domain www.MassiveDynamic.com, the attribute value would be this string:   dc=MassiveDynamic,dc=com |
| ID | (Required) The unique element ID. |
| Server | (Required) Specifies the LDAP server host machine name. |
| Command Timeout | Specifies the amount of time, in seconds, before the request to connect to the data source is presumed to have failed. Default value: *60* |
| Connection String | Specifies a complete connection string to the LDAP server. If a value is provided, it will be used instead of the connection string generated by the element and all other attributes will be overridden. |
| Password | Specifies the password for the the LDAP user Distinguished Name (DN). |
| Port | Specifies the port address of the LDAP server. Default value: *389*. |
| Server Type | Specifies an LDAP server type. Specify *Standard LDAP* for open system servers, such as OpenLDAP, Apache Directory, OpenDS, etc. Specify *MS Active Directory* for Windows Active Directory.  Default value: *Standard LDAP* |
| User DN | Specifies an LDAP user "Distinguished Name" and must represent a user than can query the LDAP server. For example, the attribute value would be this string:  uid=john.smith,ou=Users,dc=MassiveDynamic,dc=com |

## About MongoDB

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778581143/introconn_08.png)**MongoDB** is a cross-platform, document-oriented database system,
classified as a "NoSQL" database. Rather than using a traditional
table-based, relational DB structure, it uses a collection of JSON-like
documents with dynamic schemas. You can download a free, feature-limited copy for local use, or subscribe to their hosted service. For more information, see the [MongoDB website](https://www.mongodb.com/).

The **Connection.MongoDB** element allows you to connect your Logi application to the MongoDB server or service. A special datalayer element, [DataLayer.MongoDB](https://devnet.logianalytics.com/hc/en-us/articles/1500009514682-DataLayer-MongoDB), is used to retrieve data.

Because of the nature of the MongoDB service, Studio's wizards, Query Builder, Database Browser, and the "available columns" list in the Attributes panel, may not work, or work completely, in all cases.

### About Amazon Redshift

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778581399/introconn_07.png)Amazon Redshift is a fast, fully-managed, petabyte-scale data warehouse
service in "the cloud." It's
optimized for datasets ranging from a few hundred gigabytes to a
petabyte, or more. Before using the service, you must sign-up and be licensed by Amazon. For more information, see the [Amazon Redshift website](http://docs.aws.amazon.com/redshift/latest/dg/welcome.html).

The **Connection.Redshift** element allows you to connect your Logi application to the Amazon service. This is an ODBC connection and requires an ODBC connection string that includes the credentials assigned to you by Amazon. You must use
the PostgreSQL 8.x JDBC and ODBC drivers to ensure compatibility. The PostrgreSQL
9.x JDBC and ODBC drivers might not work properly with all applications.

Though you can have success using standard DataLayer.SQL, for best performance with very large datasets, we recommend use of [DataLayer.ActiveSQL](https://devnet.logianalytics.com/hc/en-us/articles/1500009514502-DataLayer-ActiveSQL). Amazon Redshift SQL is based on PostgreSQL 8.0.2. syntax but has a number of very important differences that you must be aware of as you design and develop your data warehouse applications. Please refer to the [Amazon SQL Reference](http://docs.aws.amazon.com/redshift/latest/dg/cm_chap_SQLCommandRef.html) for more information.

Because of the nature of the Amazon Redshift service, Studio's wizards, Query Builder, Database Browser, and the "available columns" list in the Attributes panel, may not work, or work completely, in all cases.

### About HP Vertica

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771703191/introconn_09.png)The column-oriented Vertica RDBMS is designed to manage large, fast-growing volumes of data and provide very fast query performance when used for data warehouses and other query-intensive applications. It claims to drastically improve query performance over traditional relational database systems, provide high-availability, and petabyte scalability on commodity enterprise servers. You can download a free,
feature-limited copy
for local use, or subscribe to their hosted service. For more information, see the [Vertica website](http://www.vertica.com/).

The **Connection.Vertica** element allows you to connect your Logi applications to the database. Special drivers must be downloaded and installed. For more information, see [Working With HP Vertica](https://devnet.logianalytics.com/hc/en-us/articles/1500009532561-Working-With-HP-Vertica).

Though you can have success using standard DataLayer.SQL, for best performance with very large datasets, we recommend use of [DataLayer.ActiveSQL](https://devnet.logianalytics.com/hc/en-us/articles/1500009514502-DataLayer-ActiveSQL). Vertica SQL is based on standard SQL syntax but has a number of very important differences that you must be aware of as you design and develop your data warehouse applications. Please refer to the [Vertica SQL Reference](https://www.vertica.com/docs/9.2.x/HTML/Content/Authoring/SQLReferenceManual/SQLReferenceManual.htm) for more information
