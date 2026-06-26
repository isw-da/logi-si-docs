---
title: "Adding a SQL Data Source"
id: 5281562715799
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281562715799-Adding-a-SQL-Data-Source
updated_at: 2022-05-03T22:08:35Z
---

# Adding a SQL Data Source

# Adding a SQL Data Source

This video explains how to add a SQL Data Source to the Exago configuration.

* [<< Configuring the Scheduler [Windows]](https://devnet.logianalytics.com/hc/en-us/articles/5281562919447-Configuring-the-Scheduler-Windows-) Previous Video
* [<< Configuring the Scheduler [Linux]](https://devnet.logianalytics.com/hc/en-us/articles/5281540739351-Configuring-the-Scheduler-Linux-) Previous Video

Next Video [Configuring a Table or View Pt 1 >>](https://devnet.logianalytics.com/hc/en-us/articles/5281548881175-Configuring-a-Table-or-View-Part-1)

## Transcript

Welcome back to the Exago Technical Training Series! In this video, we’ll demonstrate how to add a SQL Data Source to the configuration.

The first step is to open the Exago Admin Console. To open the Admin Console, we’ll use the server IP slash web app virtual path slash Admin.aspx to build our URL. In our environment, that looks like this.

A Data Source refers to a database or similar programmable object that provides data to the application. Exago does not host its clients data, so it requires a connection to the Data Source to be queried each time data is needed. Although typically only one database is used, Exago can join data from different sources into a single report. We will begin by right-clicking on the Data Source menu item on the left, and clicking Add, to configure a new Data Source connection.

Each Data Source must have a unique name that identifies it to the application. A type, SQL Server in this case, and a connection string. Optionally, a schema name may be included, sometimes used for tenancy purposes. Since Data Source connection strings typically contain passwords, they are hidden by default. Click the Show Connection String icon to show the connection string in plain text temporarily. Enter the full connection string to the Data Source. Then, click the Test Connection icon to make sure Exago can connect to the Data Source. Click Apply to save the new Data Source to the configuration. The menu on the left will update with this new connection.

Every Data Source will have one or more Data Objects, such as tables, views, database functions or stored procedures. With the Automatic Database Discovery Wizard, Exago will automatically query for and suggest data objects as well as joins between these data objects to be added to the configuration. Discovery is available for Microsoft SQL Server, Oracle, MySQL, PostgreSQL, DB2 and Informix databases. Click the Data Source name in the left hand menu, and then click Database Metadata. Exago now reads the contents of the Data Source and opens up a new Admin Console tab with the results. In the new discovery tab, we can choose to select All Complete Objects, to select those with unique keys defined. This will limit the objects to tables only. Or, Select All Objects  to select them regardless of unique key definition at the Data Source. Now we can either Add Objects, to add the selections to the configuration file; or Add Objects and Joins to additionally add any join information. Once we’ve added the objects to the configuration, they’ll populate in the appropriate section.

Congratulations! A SQL Data Source and its objects have been added to the Exago configuration!
