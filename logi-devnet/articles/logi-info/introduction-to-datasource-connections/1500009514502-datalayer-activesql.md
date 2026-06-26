---
title: "DataLayer.ActiveSQL"
id: 1500009514502
section: "Introduction to Datasource Connections"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/1500009514502-DataLayer-ActiveSQL
updated_at: 2021-06-17T01:58:08Z
---

# DataLayer.ActiveSQL

# DataLayer.ActiveSQL

The **DataLayer.ActiveSQL** element is a special type of datalayer designed for use with the Analysis Grid and Analysis Chart super-elements, and the Data Table. This topic discusses its use.

* About DataLayer.ActiveSQL
* [Attributes](#Attributes)
* [Work with DataLayer.ActiveSQL](#sec1)
* [Use Studio's DataLayer Wizard](#Wizard)

## About DataLayer.ActiveSQL

The primary model for data retrieval in Logi applications involves retrieving *all* of the requested data from a datasource and caching it, either in memory or to disk, for use by elements that will display the data. This generally works well and provides good performance across a broad spectrum of use cases.

However, there are situations when a different approach is required: when SQL queries that return a large amount of data take a long time to process before the first page of data is returned and shown. In these situations, retrieval of large data sets is usually only the first step in an analysis process, because users are not likely to want to page through thousands of pages of results. Instead they're going to manipulate and reduce the data in order to identify trends or opportunities.

**DataLayer.ActiveSQL** is a special type of datalayer designed for just such a situation. It differs from conventional datalayers in that it does *not* retrieve all of the rows in the initial request and, in response to runtime manipulations of the interface by users, it dynamically modifies and resends its initial SQL query. This helps the parent element work with much larger data sets and still provide good performance. It also increases the number and frequency of SQL queries the database
server must handle (which, generally, does not prove to be a burden on the database server) but dramatically improves performance for the user.

DataLayer.ActiveSQL understands different SQL dialects and automatically adjusts for different database servers.

Starting with v11.1.033, **Data Tables** can also take advantage of DataLayer.ActiveSQL. The datalayer generates SQL queries that limit the number of rows returned, helping with paging and sorting. With Interactive Paging in use, the query requests a number of pages of records, instead of all of the data, improving performance. As the user moves beyond the first set of pages, the database is queried again to get the next set of pages.

## Usage Restrictions

There are some important restrictions to be observed when using this datalayer:

* DataLayer.ActiveSQL is only available for use with the Analysis Grid (v11.0.43+), the Analysis Chart (v11.1.033+), and the Data Table (v11.1.033+).
* DataLayer.ActiveSQL *only**works* with **Oracle**, **MySQL**, **Microsoft SQL Server 2005+** and, if using v11.0.519+, **PostgreSQL** database servers. Note that these database servers may support data object names that are *case-sensitive*, so the spelling of things such as table names in queries may be case-sensitive.
* Do not include comments in SQL queries used with this datalayer.
* If the report definition includes interactive features allowing the user to affect the data, such as a super-element or UI elements, SQL queries used with this datalayer *should not* include **ORDER BY** clauses. Use a SQL Sort element instead for ordering the data.
* SQL queries that include a form of the **JOIN** clause should individually list all of the desired field names in the SELECT clause. Queries that don't include a JOIN clause can use the wild card asterisk (\*), if desired.
* When using aggregations, the database server controls whether or not Null values will be included in the calculations. Typically, databases are configured to *exclude* Null values from aggregations, except for COUNT(\*) operations.
* DataLayer.ActiveSQL will not work with Stored Procedures, nor with Common Table Expressions.

## Attributes

The DataLayer.ActiveSQL element has the following attributes:

| Attribute | Description |
| --- | --- |
| Connection ID | The ID of a **Connection.Oracle**, **Connection.MySQL**, or **Connection.SqlServer** (to a MS SQL Server 2005 or later) element defined in the \_Settings definition. If using v11.0.519+, may also be the ID of a **Connection.PostgreSQL** element. Other connection types will not work. If left blank, the top-most Connection element defined will be used by default. |
| HandleQuotesInTokens | When *True*, ensures SQL syntax validity by **doubling** any single-quotes that may be included in tokens used to form part of the SQL statement in the Source attribute.  For example, imagine the SQL statement "SELECT \* FROM Customers WHERE CompanyName LIKE '%@Request.Name~%' ". If the value of the Request token is "Trail's Head", the embedded single-quote could be problematic. With the HandlesQuotesInTokens attribute set to *True*, the SQL statement sent to the database server will become "SELECT \* FROM Customers WHERE CompanyName LIKE '%Trail''s Head%' ".  Default: *False* |
| ID | A unique element ID. |
| Maximum Rows | The maximum number of rows to retrieve from the data source, per request. |
| Source | (Required) The initial SQL query to be executed, for example SELECT \* FROM *MyTable*. This query will be modified dynamically by the datalayer as its parent element's user interface is manipulated.  If other elements allow the user to dynamically affect the data, queries should *not* include an **ORDER BY** clause. Use a SQL Sort element instead. Also, SQL queries that include a form of the **JOIN** clause should individually list all of the desired field names in the SELECT clause. Queries that don't include a JOIN clause can use the asterisk (\*), if desired.  **Tokens** can be used, for example, in WHERE clauses, to create dynamic queries.  The Browse button for this attribute can be used to launch the **Query Builder** wizard. |

## Work with DataLayer.ActiveSQL

Like other datalayers, DataLayer.ActiveSQL has some special child elements (discussed below) that developers can use to shape the retrieved data. However, with the exception of **Formatted Column**, other child elements for linking datalayers and formatting or transforming the data are not unavailable.

The data retrieved is available using @Data **tokens**, in the format @Data.*ColumnName*~. The spelling of the column name is **case-sensitive**. The data is only available within the **scope** of the **parent** element of the datalayer, not throughout the entire report definition.

The data retrieved into the datalayer can be viewed by turning on the **Debugging Link** in your \_Settings definition (General element) and using the resulting link at the bottom of your report page to view the **Application Trace** page. You'll be able to see the generated SQL query, and a link on the page will display the data it retrieved.

## The Datalayer to Retrieve SQL Data

DataLayer.ActiveSQL runs a SQL query to retrieve data from a SQL datasource. The element's **Source** attribute value is the actual SQL statement, which must be composed using valid syntax to be run.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402771871383/dlactivesql_01.png)

Use of the DataLayer.ActiveSQL element with an Analysis Grid is shown above.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778705943/dlactivesql_02.png)

For easier editing, double-click the Source attribute name and the attribute value can be entered in the **Attribute Zoom Window**, as shown above.

## Special ActiveSQL Child Elements

As mentioned earlier, DataLayer.ActiveSQL has some unique child elements that can be used to shape the SQL query that's generated and the retrieved data.

|  |  |
| --- | --- |
| **Element** | **Description** |
| SQL Aggregate Column | Adds a new column in the datalayer that represents an aggregate value of all rows of the datalayer. The value is populated in every row so that it can be used in further calculations, such as Summary Rows, Link Params, etc. It is also populated in the top-level row, allowing reference to the value anywhere in the report outside of a Data Table.  Available aggregate functions include *Sum*, *Count*, *Average*, *Min*, or *Max*. The column's data type must be numeric for the Sum, Count, and Average functions. |
| SQL Calculated Column | Adds a new column in the datalayer created from other values in the same row, or from token values. |
| SQL Condition Filter | Applies a WHERE-clause like functionality to the datalayer. Its Condition attribute (an expression) is evaluated for each row, and the row is removed when the result is *False*. The expression must written in the SQL query language of the data provider. Expressions usually contain tokens such as @Data to access specific values of each data row. Expressions can include almost any combination of tokens available in Info. |
| SQL Group | Groups rows in the datalayer and allows grouped aggregate values to be created. Rows are grouped by values in one or more datalayer columns. Grouped data can consist of just the first row of each group, or all grouped rows. Grouping elements can be nested. |
| SQL Parameters | Specifies the parameters for the SQL command. Parameters are listed in the SQL command using question marks as placeholders. For example, this command requires two parameters:  SELECT \* FROM Customers WHERE State=? AND City=?  Specified parameters are supplied to the command based on their *order*, and their ID is ignored. |
| SQL Sort | Sorts the rows of the datalayer. You may specify more than one column, using a comma-separated list of column names. Multiple Sort Sequences may also be entered in the same way. |
| SQL Time Period Column | Adds a new column in the datalayer that represents a time period, such as year, quarter, month, etc., derived by parsing the value in another date-time type column. |

## Studio's DataLayer Wizard

Studio includes a wizard that can assist you in configuring DataLayer.ActiveSQL. The wizard assumes that you have already added an appropriate database **Connection** element in the \_Settings definition and configured it.

![](https://logianalytics.zendesk.com/hc/article_attachments/4402778706199/dlactivesql_03.png)

As shown above, the wizard can be started by selecting and right-clicking the parent element under which you want to add the datalayer, and using the context menus to select "Add an ActiveSQL DataLayer". The wizard will open and ask you to select a connection from the list of those defined in the \_Settings definition, and to provide a SQL query. It will then insert the configured datalayer element into your definition.
