---
title: "DataLayer.ActiveSQL"
id: 4419722806807
section: "Datalayers - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419722806807-DataLayer-ActiveSQL
updated_at: 2022-07-17T02:08:17Z
---

# DataLayer.ActiveSQL

# DataLayer.ActiveSQL

The **DataLayer.ActiveSQL** element is a special type of datalayer designed for use with the Analysis Grid and Analysis Chart super-elements, and the Data Table.

The following topics introduce the DataLayer.ActiveSQL element:

* [DataLayer.ActiveSQL Attributes](https://devnet.logianalytics.com/hc/en-us/articles/4419715211287-DataLayer-ActiveSQL-Attributes#Attributes)
* [Retrieving Data with DataLayer.ActiveSQL](https://devnet.logianalytics.com/hc/en-us/articles/4419715212311-DataLayer-ActiveSQL-Retrieving-Data-with-DataLayer-ActiveSQL#Retrieving)
* [Using Studio's DataLayer Wizard](https://devnet.logianalytics.com/hc/en-us/articles/4419707474455-DataLayer-ActiveSQL-Using-Studio-s-DataLayer-Wizard#Wizard)

## About DataLayer.ActiveSQL

The primary model for data retrieval in Logi applications involves retrieving *all* of the requested data from a datasource and caching it, either in memory or to disk, for use by elements that will display the data. This generally works well and provides good performance across a broad spectrum of use cases.

However, there are situations when a different approach is required: when SQL queries that return a large amount of data take a long time to process before the first page of data is returned and shown. In these situations, retrieval of large data sets is usually only the first step in an analysis process, because users are not likely to want to page through thousands of pages of results. Instead they're going to manipulate and reduce the data in order to identify trends or opportunities.

**DataLayer.ActiveSQL** is a special type of datalayer designed for just such a situation. It differs from conventional datalayers in that it does *not* retrieve all of the rows in the initial request and, in response to runtime manipulations of the interface by users, it dynamically modifies and resends its initial SQL query. This helps the parent element work with much larger data sets and still provide good performance. It also increases the number and frequency of SQL queries the database
server must handle (which, generally, does not prove to be a burden on the database server) but dramatically improves performance for the user.

DataLayer.ActiveSQL understands different SQL dialects and automatically adjusts for different database servers.

**Data Tables** can also take advantage of DataLayer.ActiveSQL. The datalayer generates SQL queries that limit the number of rows returned, helping with paging and sorting. With Interactive Paging in use, the query requests a number of pages of records, instead of all of the data, improving performance. As the user moves beyond the first set of pages, the database is queried again to get the next set of pages.

### Usage Restrictions

There are some important restrictions to be observed when using this datalayer:

* DataLayer.ActiveSQL is only available for use with the Analysis Grid, Analysis Chart, Data Table, Sharing List, and AutoComplete elements.
* DataLayer.ActiveSQL *only**works* with these database servers and others that use the same SQL syntax:
  + DB2
  + Microsoft SQL Server 2005+
  + MySQL (except v5.5)
  + Oracle
  + PostgreSQL
  + Progress OpenEdge
  + Redshift (Amazon)
  + Vertica (HP)

It will also work with databases accessible through ODBC and JDBC connections, as long as the database supports the SQL syntax of one of the databases listed above. When you configure Connection.ODBC or Connection.JDBC elements for this purpose, you must specify the appropriate SQL syntax.

ActiveSQL support for 1010data sources is available.  
  
Note, when creating queries, that database servers may support data object names that are *case-sensitive.*

* Do not include *comments* in SQL queries used with this datalayer.
* If the report definition includes interactive features allowing the user to affect the data, such as a super-element or UI elements, SQL queries used with this datalayer *should not* include **ORDER BY** clauses. Use a SQL Sort element instead for ordering the data.
* SQL queries that include a form of the **JOIN** clause should individually list all of the desired field names in the SELECT clause. Queries that don't include a JOIN clause can use the wild card asterisk (\*), if desired.
* When using aggregations, the database server controls whether or not Null values will be included in the calculations. Typically, databases are configured to *exclude* Null values from aggregations, except for COUNT(\*) operations.
* DataLayer.ActiveSQL will not work with Stored Procedures, nor with Common Table Expressions.
