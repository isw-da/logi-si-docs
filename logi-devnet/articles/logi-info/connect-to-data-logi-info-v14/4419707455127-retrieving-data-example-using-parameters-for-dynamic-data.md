---
title: "Retrieving Data Example: Using Parameters for Dynamic Data"
id: 4419707455127
section: "Connect to Data - Logi Info v14"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4419707455127-Retrieving-Data-Example-Using-Parameters-for-Dynamic-Data
updated_at: 2022-07-17T01:54:55Z
---

# Retrieving Data Example: Using Parameters for Dynamic Data

# Retrieving Data Example: Using Parameters for Dynamic Data

This example is similar to the previous one, but introduces the ability to condition the data using Query String parameters.

![](https://devnet.logianalytics.com/hc/article_attachments/4419714703383/usingdatadefs_09.png)

A new data definition, shown above, includes both a **Default Request Parameters** element and a **DataLayer.SQL** element. The Default Request Params ensures that the SQL query, which uses a Request token, will always have a valid WHERE clause value.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699630743/usingdatadefs_10.png)

We'll start our example report definition, shown above, by adding an **Input Select List**, with a datalayer and event handler, to allow the user to select an Employee ID. A Default Request Params element will ensure that the select list always has a default value and the event handler just refreshes the report (and updates the select list Request variable) when a new Employee ID selection is made.

![](https://devnet.logianalytics.com/hc/article_attachments/4419699630999/usingdatadefs_11.png)

We'll finish our report definition with the same set of elements we used previously: Data Table, DataLayer.Json File, Flattener, and Auto Columns. The datalayer's Json File attribute is set to:

https://localhost/v12test/rdTemplate/rdData.aspx?rdData=myDataDefSQL&inpEmployeeID=@Request.empID~

Note the use of an extra Query String parameter, with a value set from a Request token.

![](https://devnet.logianalytics.com/hc/article_attachments/4419706725399/usingdatadefs_12.png)

And the resulting report looks like this when previewed. Changing the Employee ID selection causes the data to refresh.
