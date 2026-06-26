---
title: "Running Datalayer and Data Table Rows"
id: 4419707789335
section: "Use Logi Studio/SSRM - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707789335-Running-Datalayer-and-Data-Table-Rows
updated_at: 2022-07-17T02:23:44Z
---

# Running Datalayer and Data Table Rows

# Running Datalayer and Data Table Rows

Tasks offer you the ability to retrieve just one row of data, or to iterate through all of the rows in either a datalayer or a Data Table in a Report definition, processing the data in each row individually.

In a manner similar to the Local Data element, the **Procedure.Data** element can be used to run a datalayer; the column values from the first datalayer row (only) can then be accessed in the task using this token: @Procedure.*<Procedure.Data element ID>*.*<column name>*~.

The examples below show you how to *iterate* through multiple datalayer or Data Table rows :

![](https://devnet.logianalytics.com/hc/article_attachments/7522806567319/workproctask_19.png)

In this example task, we'd like to look through a contact database table and send out an email newsletter for every record that has an email address. Here's a description of the purpose of each element used:

1. The **Procedure.Run Data Layer Rows** element is the parent container that causes the iteration through each row in the datalayer once data has been retrieved.
2. A **DataLayer.SQL** element is used to query the database table, returning all of the records into the datalayer. Other elements beneath the Procedure.Run Data Layer Rows element can access data values in the datalayer using standard @Data tokens.
3. The Procedure.If element is configured so that its child element, Procedure.Send Mail, will run *only* if the email address column in the current datalayer row is not Null.
4. The **Procedure.Send Mail** element uses the token @Data.EmailAddress~ in its **To Email Address** attribute to send out an email for the current datalayer row.
5. The **Response.Report** element, of course, redirects processing somewhere else when the task completes.

Let's look at another example: imagine a report definition that includes a Data Table and one of its columns has an **Input Text** element displayed in every row, like this:

![](https://devnet.logianalytics.com/hc/article_attachments/7522760131863/workproctask_20.png)

At runtime, the user can enter numbers to adjust the table values. But, how would you update the database after multiple changes have been made and the page is submitted? That's right - you can do it with a task.

![](https://devnet.logianalytics.com/hc/article_attachments/7522806584471/workproctask_21.png)

Here's a description of the elements needed:

1. The **Procedure.Run Data Table Rows** element is the parent container that causes the iteration through each row in the Data Table named in its **Data Table ID** attribute. If the attribute is left blank, the first table found in the application that includes user input elements will be used.
2. The **Procedure.SQL** element is used to issue an UPDATE command to the database, using an @Request token to access the value of the Input Text element for each table row.
3. The **Response.Report** element, of course, redirects processing somewhere else when the task completes.

## Important Limitations

![](https://devnet.logianalytics.com/hc/article_attachments/7522725232151/criticalicon.png) Please note these two important limitations:

* **Interactive Paging** should *not* be used with Data Tables being processed using Procedure.Run Data Table Rows. If possible, use input elements and datalayer filtering elements instead to limit the amount of data in the table.
* **Input check boxes** should *not* be the sole Input
  element within a Data Table row when using Procedure.Run Data Table Rows. This Input element is unusual in that
  it does not submit a Request variable value at all if
  the box is not checked and, when this is the only Input element in the
  table, it will cause Procedure.Run Data Table Rows to only "see"
  the rows that are selected, creating an incorrect listing of the rows.
  To avoid this, you can include an **Input Hidden** element within the table that stores a unique ID for each row. This will ensure that each
  row is represented by a Request variable and gets processed by Procedure.Run Data Table Rows.
