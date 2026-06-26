---
title: "Combining Data in a SQL Query"
id: 4406817179415
section: "Reports - Logi Info v12"
category: "Logi Info"
url: https://devnet.logianalytics.com/hc/en-us/articles/4406817179415-Combining-Data-in-a-SQL-Query
updated_at: 2022-04-06T06:04:28Z
---

# Combining Data in a SQL Query

# Combining Data in a SQL Query

In all of the following examples, the goal is to retrieve FirstName and LastName text data and combine it into a full name.
One of the easiest ways to this is to let the database server do it for you. This SQL query:

SELECT FirstName + ' ' + LastName AS Name FROM Employees

returns a single column, **Name**, which will contain the FirstName and LastName data, separated by a space. Like any other column in the datalayer, the Name column value is accessible using an @Data token:

![](https://devnet.logianalytics.com/hc/article_attachments/4417575832599/combinetext_01.png)

After using the SQL query shown earlier, we can display the Name data in a Data Table column using **Label** element whose **Caption** attribute is set to @Data.Name~, as shown above.
