---
title: "SQL Database Interactions from Tasks"
id: 4406817799575
section: "Use Logi Studio/SSRM - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817799575-SQL-Database-Interactions-from-Tasks
updated_at: 2022-04-06T06:08:15Z
---

# SQL Database Interactions from Tasks

# SQL Database Interactions from Tasks

Tasks also provide the ability to interact with SQL databases, including the so-called "write-back" capability required to update databases. Both SQL Queries and Stored Procedures are supported, with special elements, and all valid SQL commands, including INSERT, UPDATE, and DELETE, can be used.

## Using SQL Statements

Implementing a direct SQL statement in Process task is easy and tokens can be used to "parameterize" the statement:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563114135/workproctask_13.png)

In the example shown above, we see a task that includes the **Procedure.SQL** element. The complete SQL Command in the example is:

UPDATE Products SET UnitsInStock = @Request.inpHidden~ WHERE ProductID = @Request.ProductID~

Any valid SQL statement can be executed. The **Handle Quotes Inside Tokens** attribute handles tokens that might have embedded single quotes, such as the text *Trail's Head*. When set to *True*, token values in the SQL Command will be wrapped in single-quotes, "doubling" them so the syntax will be valid. The default for this attribute is *False*.

Tokens for string values should be wrapped in quotes to conform to your database's SQL syntax. For example, if you'd use quotes in a plain text query with a WHERE clause, like this:

...WHERE user\_lastname = 'Smith'

then with tokens it would be:

...WHERE user\_lastname = '@Request.UserName~'

The **SQL Return Type** attribute specifies the return value type of the SQL operation:

* If *RowsAffected* (the default) is
  selected, the operation will return the number of rows changed by
  any UPDATE, INSERT, or DELETE commands. You can access this value
  later in the task using
  the special token:  
  @Procedure.<*yourProcedureSQL\_ID>*.RowsAffected~.
* If *FirstRow* is selected, the first row of any result set from the SQL operation is returned. You can access the values of the returned row columns later in the task using tokens in this format:  
  @Procedure.<*yourProcedureSQL\_ID>*.*<ColumnName>*~.

The example above shows an UPDATE operation but queries using SELECT statements are, of course, also supported. Values returned by a query using Procedure.SQL are limited to those in the first row, as described above. If you want to return *multiple* rows, use **Procedure.Run DataLayer Rows** and a datalayer, as described in [Running Datalayer and Data Table Rows](https://devnet.logianalytics.com/hc/en-us/articles/4406822481687-Running-Datalayer-and-Data-Table-Rows).

The **If Error** element can be used beneath Procedure.SQL to handle errors that may occur. The actual error message text is available in this token: @Procedure.<*yourProcedureSQL\_ID>*.ErrorMessage

Procedure.SQL elements can also be used beneath Procedure.Run Data Table Rows, Procedure.Run DataLayer Rows, which are discussed in [Running Datalayer and Data Table Rows](https://devnet.logianalytics.com/hc/en-us/articles/4406822481687-Running-Datalayer-and-Data-Table-Rows).

## Using SQL Parameters

The **SQL Parameters** and **SQL Parameter** elements can be used to include tokenized parameters, if you prefer not to embed tokens directly into the SQL statement. This approach also allows you to enforce a data type for the parameter value and also offers protection against SQL Injection attacks.

To use parameters, write your SQL statement using "placeholder" notation. The exact syntax for this depends on your database *and* the Connection element you're using. For example, if you're using **Connection.SQLServer**, you use this notation:

SELECT \* FROM Customers WHERE State=@state AND City=@city

and the **ID** attribute of each SQL Parameter element must match a placeholder *name*. So, in the example, the value of an element with an ID of *state* will replace the @state placeholder at runtime.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) There is no need to surround the placeholder with quotes, even if it represents string data. The Logi Engine sees the parameter data type in the element attributes and handles it appropriately.

Similarly, if you're using **Connection.Oracle**, you use this notation:

SELECT \* FROM Customers WHERE State=:state AND City=:city

and, as before, the **ID** attribute of each SQL Parameter element must match a placeholder *name*.

However, if you're using **Connection.OLEDB**, you use this notation:

SELECT \* FROM Customers WHERE State=? AND City=?

Unlike the previous examples, these are *positional* parameters so, at runtime, placeholders in the statement will be replaced, starting with the first placeholder, by the values specified in the SQL Parameter elements, based on the elements' *top-to-bottom order* in the definition. The element IDs are ignored.

![](https://devnet.logianalytics.com/hc/article_attachments/4417575560983/workproctask_14.png)

The example above illustrates the relationship, in this scenario, between SQL Parameter element order and placeholders in the statement.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) SQL Parameters will not work when using **Connection.ODBC**.

Consult your database documentation for specific placeholder information.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) SQL Parameters are especially useful if you're *writing* string data that includes embedded single quotes to the database. The Logi Engine automatically handles escaping the single quotes in the SQL statement sent to the database server.

## Using Stored Procedures

We highly recommend the use of stored procedures, especially when updating the database. It's the most secure method and usually offers the best performance. A stored procedure is code, possibly pre-compiled, that resides on your database server and is called to perform work. It's usually a collection of standard SQL commands.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563114263/workproctask_15.png)

In the example task above, a **Procedure.SP** element has been added in order to invoke a stored procedure. Its attributes are set as shown to connect to, and run, the stored procedure. The **Command** attribute includes a pull-down list of all of the stored procedures available through the database connection specified.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) Stored procedures are written using the tools that came with your database server; some servers may accept code written in an external text editor such as Notepad. Logi Studio does *not* include an editor for writing stored procedures.

Two other types of elements can be used if the stored procedure requires parameters: the **SP Parameters** element, which is just a container, and one or more **SP Parameter** elements.

![](https://devnet.logianalytics.com/hc/article_attachments/4417563114519/workproctask_16.png)

The first **SP Parameter** element has been configured, as shown above, as an Input parameter. It will pass the First Name value from a Request variable to the stored procedure. Its **Direction** attribute is set to *Input*, and its **Size** attribute value is set to *0*, which causes it to be adjusted to the correct size automatically at runtime. Other SP Parameters will be configured similarly, to pass additional values.

![](https://devnet.logianalytics.com/hc/article_attachments/4417583587863/noteicon.png) The relationship between parameters in the task definition and the parameters in the stored procedure is determined solely by their *order*, not by their IDs.

## SP Return Values

The Procedure.SP return behavior is controlled by its **SP Return Type** attribute, which has two possible values:

When configured as *ReturnValue* (the default) only the value of the first column of the first row of data returned by the stored procedure, if any, is available. Additional columns or rows are ignored. The returned value can be accessed with an @Procedure "rdReturnValue" token, for example: @Procedure.myProcedureId.rdReturnValue~

When configured as *FirstRow*, the entire first row of data returned by the stored procedure is available. Access the values of the first row with @Procedure tokens. For example: @Procedure.myProcedureId.someColumnName~

## Using SP Output Parameters

Another mechanism for returning data is to have the stored procedure return *output parameters* and the task can be configured to receive them:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575561495/workproctask_17.png)

To accomplish this, the example task has now been given an SP Parameter element that's configured as an output parameter. Note that its **Direction** attribute is set to *Output*. The stored procedure will return a value to the task, using this parameter. In this case, the **Size** attribute must be set to the number of bytes for its data type, or the maximum expected to be returned.

![](https://devnet.logianalytics.com/hc/article_attachments/4417562936855/criticalicon.png) Once again, the relationship of parameter elements in the task and the stored procedure's output parameters is determined solely by their *order*, not their IDs.

The value returned in the output parameter is available using a special token, shown below:

![](https://devnet.logianalytics.com/hc/article_attachments/4417563114903/workproctask_18.png)

A **Link Parameters** element has been added to the task so that we can pass the results back to a report. Its **Status** attribute has been configured to use the special token that holds the value passed to the output parameter element. The token format is:

@Procedure.*<Procedure.SP Element ID>*.*<SP Parameter Element ID>*~

DevNet includes a [sample application](https://devnet.logianalytics.com/hc/en-us/articles/360050374433-Update-Table-Sample-Application) that demonstrates the use of a Process task to update a table.
