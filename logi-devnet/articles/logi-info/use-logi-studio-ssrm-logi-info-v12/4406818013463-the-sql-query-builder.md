---
title: "The SQL Query Builder"
id: 4406818013463
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406818013463-The-SQL-Query-Builder
updated_at: 2022-04-06T06:09:39Z
---

# The SQL Query Builder

# The SQL Query Builder

The **SQL Query Builder** tool allows youto examine data, and construct and test yourqueries, from within Studio. It's launched either from the **Database Browser** or...

![](https://devnet.logianalytics.com/hc/article_attachments/4417583660951/usingstudio_55.png)

...as shown above, by clicking the browse button at the end of the **DataLayer.SQL** element's **Source** attribute.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583661079/usingstudio_56.png)

The SQL Query Builder presents **database objects** in a (1) list, from which tables and views can be **dragged** into the (2) center **work area**. Manipulating the visual objects results in a SQL query being generated in the (3) bottom command area, where it can also be manually edited. The query can use **multiple lines** in the command area and can include DECLARE statements and other more complex SQL statement constructions.

Clicking the (4) **Data****tab** at the top of the SQL Query Builder **executes** the SQL statements and displays the results in that tab panel. The **F5** key can also be used to execute statements; portions of statements can be highlighted and selectively executed using F5 as well. SQL statements such as INSERT and UPDATE can be used to modify the data but there is no graphical way to directly make modifications in the Data tab. By default, the SQL Query Builder will only return
10,000
rows of data. You can turn this limit off in Studio in Tools ![](https://devnet.logianalytics.com/hc/article_attachments/4417575446295/menuarrow.gif) Options.

Clicking (5) **OK** will cause the query constructed in the command area to be copied into the datalayer's **Source** attribute, if the SQL Query Builder was called by clicking the attribute's browse button. Otherwise, the query text can be selected, copied, and pasted as needed.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png)

* The SQL Query Builder *will* work with the databases for which we provide "native" Connection elements, such as Oracle, MS SQL Server, and MySQL. It *may* work with other databases that use a connection that mimics that of a database for which we provide a native connection.
* The SQL Query Builder *will not* support all of the functions and views available in **Microsoft Access** databases, nor does it support other non-standard SQL languages, such as *Salesforce Object Query Language*. It is *not**guaranteed* to work with every possible database and, in that case,
  we recommend
  that you use tools provided with the database to create and test queries, and then copy and paste them into Studio.

### When a Query Has Been Entered Manually

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) If you *have already entered a query manually* in the Source attribute and you then open it in SQL Query Builder, the tool will try to "reverse-engineer" the query into its graphical representation. It succeeds at this most of the time but, if the query includes **tokens** or is created using a non-standard SQL language, the SQL Query Builder may fail and display an error message. This is especially likely when Logi tokens have been used outside of a SELECT statement.

### Use with Oracle and Multiple Schemas

When connecting to an Oracle database, SQL Query Builder will retrieve a list of schemas, prompt you to select one, and then retrieve the related objects.
