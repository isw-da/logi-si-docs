---
title: "Table-Valued Functions"
id: 5281624804759
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281624804759-Table-Valued-Functions
updated_at: 2023-04-03T17:52:19Z
---

# Table-Valued Functions

# Table-Valued Functions

Table-valued functions (TVF) are user-defined functions that return a table data type as output. Unlike views, table-valued functions allow for more than one SELECT statement.

Below is the TVF we’ll be referencing in this guide. Note that the function RETURNS TABLE and takes the parameter startDate with the data type DATETIME.

```
ALTER FUNCTION "dbo"."OrderFunction" (@startDate@ DATETIME)
RETURNS TABLE
AS
RETURN (SELECT o.OrderId, o.CustomerId, o.EmployeeId, o.OrderDate
		FROM Orders o
		WHERE o.OrderDate >= @startDate@)
```

## Adding Table-Valued Function Data Objects

Before adding the TVF as a Data Object, prepare the configuration by creating all parameters necessary for the function. In this example, the `@startDate@` parameter. Make sure the parameter data type matches that specified in the function.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Selecting the TVF containing this parameter as the Parameter Dropdown Object will cause an error.

![](https://devnet.logianalytics.com/hc/article_attachments/5432261401367/param.png)

With the parameter applied, continue by locating the TVF in the admin console as you would a standard table. Use either the [Automatic Database Discovery](https://devnet.logianalytics.com/hc/en-us/articles/5281636352791-Automatic-Database-Discovery) tool or select the function from the New Data Object name dropdown menu.

After selecting the TVF, give it an Alias, then add the Parameters.

Complete the rest of the New Data Object form as if it were standard database table. Click **Apply** to save the Data Object.

It is possible to join a TVF object to other Data Objects. See [Join Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281644535703-Join-Configuration)
