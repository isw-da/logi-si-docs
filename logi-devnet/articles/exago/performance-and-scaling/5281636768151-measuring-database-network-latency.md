---
title: "Measuring Database Network Latency"
id: 5281636768151
section: "Performance and Scaling"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281636768151-Measuring-Database-Network-Latency
updated_at: 2022-05-03T22:07:54Z
---

# Measuring Database Network Latency

# Measuring Database Network Latency

This topic will discuss how to examine the Exago log file to determine the time it takes to retrieve data from a database. In this way you can isolate the performance of the network connection between the execution engine and the data source.

The first step is to turn on logging at the INFO level, to allow you to view execution information. If you run reports with the Exago Web Application, see **[Application and Performance Logging](https://devnet.logianalytics.com/hc/en-us/articles/5281670339479-Application-and-Performance-Logging)** for details. If you run reports with Remote Execution, see **[Scheduler Service Configuration](https://devnet.logianalytics.com/hc/en-us/articles/5281627554583-Scheduler-Service-Configuration)** for details.

Then run a report that uses the database in question. Wait for the report to finish loading, then consult the relevant log file.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This topic references `<WebApp>/`,
> `<WebSvc>/` and `<Sched>/`as a placeholder
> for the Web Application, Web Service API and Scheduler Service's install
> location respectively. The default install location is
> `C:\Program Files\Exago\ExagoWeb\` (`/opt/Exago/` on Linux),
> `C:\Program Files\Exago\ExagoWebApi\` ( `/opt/Exago/WebServiceApi/` on Linux) or
> `C:\Program Files\Exago\ExagoScheduler\` (`/opt/Exago/Scheduler/` on Linux); however, these directories
> can be changed during installation.

The application log file is located at `<WebApp>/Temp/WebReportsLog.txt`. The scheduler log files are located at `<Sched>/eWebReportsScheduler.log`.

You will likely want to write a script to automate the following processes.

Since the log files are too large and unwieldy to scan by sight, use a text editor that has good search capabilities. Search for the name of the report you just ran, and look for a line similar to the following:

```
2017-09-26 13:55:26,127 INFO  [4xzemyj3rzt4kq4rnevram45] [Api.Execute.ExecuteReport.Process] ReportExecuteStart: Name: ExamplesTest, UserId: , CompanyId: , Filters:
```

*ReportExecuteStart:* indicates the start of the execution. Browse down until you reach *ReportExecuteEnd:*, which indicates the end of the execution. There should be at least five lines between.

```
2017-09-26 13:55:26,127 INFO  [4xzemyj3rzt4kq4rnevram45] [Api.Execute.ExecuteReport.Process] ReportExecuteStart: Name: ExamplesTest, UserId: , CompanyId: , Filters: 
2017-09-26 13:55:26,155 INFO  [4xzemyj3rzt4kq4rnevram45] [Api.Data.DbConnect.Execute] Db DataSource:C:DatabasesNorthwind.sqlite Database: Type:odbc
2017-09-26 13:55:26,155 INFO  [4xzemyj3rzt4kq4rnevram45] [Api.Data.DbConnect.Execute] SQL Stmt: SELECT `Employee`.`LastName` as c0,`Order`.`OrderDate` as c1,`OrderDetail`.`Quantity` as c2,`OrderDetail`.`UnitPrice` as c3,`OrderDetail`.`Discount` as c4,`Order`.`CustomerId` as c5,`OrderDetail`.`OrderId` as c6,`OrderDetail`.`ProductId` as c7,`Order`.`Id` as c8,`Employee`.`Id` as c9,`Order`.`EmployeeId` as c10 FROM `OrderDetail`  inner join `Order`  on (`OrderDetail`.`OrderId` = `Order`.`Id`) inner join `Employee`  on (`Order`.`EmployeeId` = `Employee`.`Id`) ORDER BY `Employee`.`Id` asc, `Order`.`Id` asc
2017-09-26 13:55:26,190 INFO  [4xzemyj3rzt4kq4rnevram45] [Api.Data.DbConnect.Execute] SQL Stmt rows returned: 2155
2017-09-26 13:55:32,417 INFO  [4xzemyj3rzt4kq4rnevram45] [Api.Execute.ExecuteReport.Process] ReportExecuteEnd: Name: ExamplesTestERThemes, UserId: , CompanyId: , ExecuteTime: 00m:06s
```

Note the format of the log entries:

```
TimeStamp INFO [alphanumeric] [Process] Details
```

Use the time stamps to determine how much time each step of the process took to complete. Since we are only concerned about the network performance, isolate the lines with the start and end of the database query:

```
2017-09-26 13:55:26,155 INFO  [4xzemyj3rzt4kq4rnevram45] [Api.Data.DbConnect.Execute] SQL Stmt: SELECT `Employee`.`LastName` as c0,`Order`.`OrderDate` as c1,`OrderDetail`.`Quantity` as c2,`OrderDetail`.`UnitPrice` as c3,`OrderDetail`.`Discount` as c4,`Order`.`CustomerId` as c5,`OrderDetail`.`OrderId` as c6,`OrderDetail`.`ProductId` as c7,`Order`.`Id` as c8,`Employee`.`Id` as c9,`Order`.`EmployeeId` as c10 FROM `OrderDetail`  inner join `Order`  on (`OrderDetail`.`OrderId` = `Order`.`Id`) inner join `Employee`  on (`Order`.`EmployeeId` = `Employee`.`Id`) ORDER BY `Employee`.`Id` asc, `Order`.`Id` asc
2017-09-26 13:55:26,190 INFO  [4xzemyj3rzt4kq4rnevram45] [Api.Data.DbConnect.Execute] SQL Stmt rows returned: 2155
```

You can identify these lines by the following characteristics:

#### Start

```
... [Api.Data.DbConnect.Execute] SQL Stmt: ...
```

#### End

```
... [Api.Data.DbConnect.Execute] SQL Stmt rows returned: ...
```

Then record the time difference between the two lines. The second line also indicates how many rows were returned for this query, which you should also record. As you get more data points, you can plot the time difference and the row count as coordinate points on a scatter chart, to measure the trends in performance.

You could also record the actual times for each execution, to see if there are any differences in performance per day of the week, or time of the day.

Note that reports may query the database multiple times, especially if the reports contain complex data groupings. Each query is a separate data point.
