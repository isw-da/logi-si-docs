---
title: "Handle SQL Errors in Tasks"
id: 4419715033367
section: "Developer Tools - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419715033367-Handle-SQL-Errors-in-Tasks
updated_at: 2022-07-17T02:03:28Z
---

# Handle SQL Errors in Tasks

# Handle SQL Errors in Tasks

**Logi Info** developers are able to use Process definition Tasks to
manipulate their database tables. This could generate SQL errors, so it's
good to be able to handle generic and specific errors.
The following example assume that account names must be unique in the
Accounts table.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714623127/sqlerror_01.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419699512087/sqlerror_01a.png)

In the Process definition shown above, a task has been added to add new
accounts. It includes a **Procedure.SQL** element (procInsertRecord)
which will insert the new account records. An **If Error** element has
been added beneath it to handle any errors that occur, and to route
processing back to a report definition.
To handle *generic* SQL errors, you can leave the If Error element's
**Error Filter** attribute value blank and it will "catch"
any error that occurs as a result of the SQL operation.
If you want to handle *specific* SQL errors, you can fill-in the
**Error Filter** attribute with some of the text that the SQL server
will return in an error message caused by a specific type of error. The
example above suggests an error number and partial text from a duplicate
primary key error message. If the text in the attribute value is contained
in the server's error message, processing will be routed to the If Error
element's child elements.
You can stack up more than one If Error element, for example, to first
handle several different specific errors and then finally handle a generic
error.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714623383/sqlerror_02.png)![](https://devnet.logianalytics.com/hc/article_attachments/4419699512343/sqlerror_02a.png)

You can send the actual error message returned from the SQL server to the
target report, as shown above.
A special token is used for the error message. It starts with
"@Procedure.", then includes the ID of the Procedure.SQL element
used, another dot, and finally the words "ErrorMessage". Don't
forget the tilde character ("~") that terminates every token!

@Procedure.procInsertRecord.ErrorMessage~  

This technique allows you to show your own "user friendly" error
messages for specific SQL errors, while sending along the exact SQL error
message for any other SQL errors.
