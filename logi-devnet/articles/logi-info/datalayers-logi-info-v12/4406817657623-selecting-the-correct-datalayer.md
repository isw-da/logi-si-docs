---
title: "Selecting the Correct Datalayer"
id: 4406817657623
section: "Datalayers - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817657623-Selecting-the-Correct-Datalayer
updated_at: 2022-04-06T06:07:26Z
---

# Selecting the Correct Datalayer

# Selecting the Correct Datalayer

In Logi reporting products, developers use datalayers to **retrieve data** for tables, charts, and input select lists from a **datasource**. A datasource can be one of the following:

* OLEDB-, ODBC-, and JDBC-compliant databases
* XML, CSV, Excel, JSON, and other data files
* LDAP directories
* Web feeds, web services, or web pages
* REST and SOAP APIs
* Hard-coded, static data
* Your Logi application's metadata

A number of different datalayer elements are available and your selection can depend on both the datasource and the retrieval technique.
The following table lists the typical uses for datalayers within Logi reporting products. The links direct you to individual topics that discuss the use of each datalayer.

| Datalayer Type | Description |
| --- | --- |
| [DataLayer.ActiveSQL](https://devnet.logianalytics.com/hc/en-us/articles/4406817277847-DataLayer-ActiveSQL) | A special type of datalayer designed for use with the Analysis Grid super-element, it only retrieves a limited number of rows based on an initial SQL query and, in response to runtime manipulations of the Analysis Grid interface by users, it dynamically modifies and resends its query. |
| [DataLayer.Bookmarks](https://devnet.logianalytics.com/hc/en-us/articles/4406822059159-DataLayer-Bookmarks) | Retrieves data directly from bookmark collection files. |
| [DataLayer.Cached](https://devnet.logianalytics.com/hc/en-us/articles/4406817281687-DataLayer-Cached) | Modifies the normal data retrieval activities of datalayers; when it's used, data is retrieved, cached, and made available for use in Logi reports for a specific time period, after which the data is refreshed (deleted and recreated). |
| [DataLayer.CSV](https://devnet.logianalytics.com/hc/en-us/articles/4406817283863-DataLayer-CSV) | Retrieves data directly from a .CSV text file. |
| DataLayer. Data Services *Deprecated* | Uses Logi Services for data retrieval and is only available in Logi Info if the Discovery Module v3.x has been installed. |
| DataLayer.Dataview | Retrieves the data for the Thinkspace element. |
| [DataLayer.Definition List](https://devnet.logianalytics.com/hc/en-us/articles/4406822249879-DataLayer-Definition-List) | Retrieves a list of definition files used in your application, and their properties, such as author name, timestamp, and engine version. |
| [DataLayer.Directory](https://devnet.logianalytics.com/hc/en-us/articles/4406822060439-DataLayer-Directory) | Retrieves a list of files and/or folders in a specified directory, including their size, timestamps, and other properties. |
| [DataLayer.Excel](https://devnet.logianalytics.com/hc/en-us/articles/4406822061335-DataLayer-Excel) | Retrieves data directly from a Microsoft Excel spreadsheet file. |
| [DataLayer.Fixed File Format](https://devnet.logianalytics.com/hc/en-us/articles/4406822062231-DataLayer-Fixed-File-Format) | Retrieves data directly from text files that use column widths to specify data format. |
| [DataLayer.Google App](https://devnet.logianalytics.com/hc/en-us/articles/4406822253079-DataLayer-Google-App) | Enables connection to the datastore of a published application hosted by the Google App Engine. |
| [DataLayer.Google Spreadsheet](https://devnet.logianalytics.com/hc/en-us/articles/4406822256023-DataLayer-Google-Spreadsheet) | Retrieves data in a Google online spreadsheet. |
| DataLayer.GPX File | Retrieves data directly from a GIS data file in the GPX format. |
| [DataLayer.JSON](https://devnet.logianalytics.com/hc/en-us/articles/4406817301399-DataLayer-JSON) | Retrieves data directly from a JSON data file. *Prior to v12.1, this datalayer was named DataLayer.JSON File.* |
| DataLayer.KML File | Retrieves data directly from a GIS data file in the KML format. |
| [DataLayer.LDAP](https://devnet.logianalytics.com/hc/en-us/articles/4406817304855-DataLayer-LDAP) | Retrieves data from a Lightweight Directory Access Protocol (LDAP) directory. |
| [DataLayer.LDAP Authentication](https://devnet.logianalytics.com/hc/en-us/articles/4406816908439-DataLayer-LDAP-Authentication) | Authenticates user against a Lightweight Directory Access Protocol (LDAP) directory. |
| DataLayer.Linked | Reuses data retrieved in another datalayer. For more information, see [Link Datalayers](https://devnet.logianalytics.com/hc/en-us/articles/4406822443671-Link-Datalayers). |
| [DataLayer.MDX](https://devnet.logianalytics.com/hc/en-us/articles/4406817309591-DataLayer-MDX) | Retrieves cube data and populates Logi OLAP Grid or OLAP Table elements. |
| [DataLayer.Mongo Find](https://devnet.logianalytics.com/hc/en-us/articles/4406822063255-DataLayer-Mongo-Find) | Retrieves documents from a MongoDB collection using the MongoDB Find API. |
| [DataLayer.Mongo Map Reduce](https://devnet.logianalytics.com/hc/en-us/articles/4406816909591-DataLayer-Mongo-Map-Reduce) | Runs a MongoDB map-reduce operation to return one or more documents. |
| [DataLayer.Mongo Run Command](https://devnet.logianalytics.com/hc/en-us/articles/4406816910743-DataLayer-Mongo-Run-Command) | Runs a MongoDB command, suitable for use with the Aggregation Pipeline, a simpler alternative to using map-reduce operations, to return one or more documents. |
| [DataLayer.Plugin](https://devnet.logianalytics.com/hc/en-us/articles/4406816911767-DataLayer-Plugin) | Retrieves data from a custom-written code module, the "plug-in". |
| [DataLayer.REST](https://devnet.logianalytics.com/hc/en-us/articles/4406817313943-DataLayer-REST) | Retrieves data from a REST-style web service. |
| DataLayer.Scheduler | Retrieves data associated with the Logi Scheduler service. For more information, see [Using Logi Scheduler](https://devnet.logianalytics.com/hc/en-us/articles/4406818028311-Using-Logi-Scheduler). |
| DataLayer.SimpleDB *Deprecated* | Retrieves data from Amazon's SimpleDB web service. |
| [DataLayer.SP](https://devnet.logianalytics.com/hc/en-us/articles/4406822267415-DataLayer-SP) | Retrieves data from a SQL database, using a Stored Procedure. |
| [DataLayer.SQL](https://devnet.logianalytics.com/hc/en-us/articles/4406817325591-DataLayer-SQL) | Retrieves data from a SQL database, using a SQL query. |
| [DataLayer.Static](https://devnet.logianalytics.com/hc/en-us/articles/4406817330839-DataLayer-Static) | Uses hard-coded data values. |
| [DataLayer.Twitter](https://devnet.logianalytics.com/hc/en-us/articles/4406822064151-DataLayer-Twitter) | Retrieves tweets and messages from the Twitter web site. |
| [DataLayer.WebFeed](https://devnet.logianalytics.com/hc/en-us/articles/4406817334935-DataLayer-WebFeed) | Retrieves data from an RSS or Atom web feed. |
| [DataLayer.Web Scraper](https://devnet.logianalytics.com/hc/en-us/articles/4406816912919-DataLayer-Web-Scraper) | Retrieves data from within web pages or HTML files. |
| [DataLayer.Web Service](https://devnet.logianalytics.com/hc/en-us/articles/4406822274839-DataLayer-Web-Service) | Retrieves data from a SOAP-style web service. |
| [DataLayer.XML](https://devnet.logianalytics.com/hc/en-us/articles/4406822271127-DataLayer-XML) | Retrieves data directly from an XML data file. *Prior to v12.1, this datalayer was named DataLayer.XML File.* |
| [DataLayer.XOLAP Query](https://devnet.logianalytics.com/hc/en-us/articles/4406816914327-DataLayer-XOLAP-Query) | Pre-defines a data view based on a Logi XOLAP cube. |

The type of datalayer used often matches the type of **Connection** element used in your \_Settings definition. Some datalayers, such as DataLayer.CSV and DataLayer.Excel, directly access the web server file system and may not require a connection.
The **Connection.HTTP** element allows the following datalayers to optionally use a connection to an HTTP or HTTPS datasource that requires authentication:

* DataLayer. CSV
* DataLayer.Excel
* DataLayer.Fixed Format File
* DataLayer.GPX File
* DataLayer.JSON
* DataLayer.KML File
* DataLayer.Web Feed
* DataLayer.Web Scraper
* DataLayer.XML

The following datalayers include the optional **Http Method** attribute, which allows you to select the one of these verbs to be sent with a REST request: DELETE, GET, POST, or PUT, or to enter a custom verb:

* DataLayer.JSON
* DataLayer.REST
* DataLayer.XML

The default is POST.

Many datalayers are run by the Logi Engine in *separate* threads, which means that data retrieval time is limited to the longest running query, rather than the number of queries, resulting in excellent performance. This includes all datalayers except the following: Local Data datalayers, DataLayer.Linked, DataLayer.XML, DataLayer.Cached, DataLayer.Bookmark, DataLayer.Static, and any datalayer whose data is displayed using the Auto Columns element.

Data Engine performance, when processing large numbers of DateTime-type columns in a result set, can be significantly improved by skipping Time Zone processing, if it's not needed in the application. This is done using a special constant in the \_Settings definition:

rdSQLIncludeGMTOffset = False

However, this feature does *not* offer improved performance with small numbers of DateTime columns.
