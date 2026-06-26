---
title: "Configuring a Table or View Part 1"
id: 5281548881175
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281548881175-Configuring-a-Table-or-View-Part-1
updated_at: 2022-05-03T22:08:28Z
---

# Configuring a Table or View Part 1

# Configuring a Table or View Part 1

This video explains how to add a table or view to the Exago configuration. Learn about the various settings available for each data object.

[<< Adding a SQL Data Source](https://devnet.logianalytics.com/hc/en-us/articles/5281562715799-Adding-a-SQL-Data-Source) Previous Video

Next Video [Configuring a Table or View Pt 2 >>](https://devnet.logianalytics.com/hc/en-us/articles/5281541391511-Configuring-a-Table-or-View-Part-2)

## Transcript

Welcome back to the Exago Technical Training Series! In this video, we’ll demonstrate adding and configuring a table or a view to the Exago configuration.

The first step is to open the Exago Admin Console. To open the Admin Console, we’ll use the server IP slash web app virtual path slash Admin.aspx to build our URL. In our environment, that looks like this. In a previous video, we configured the SQL Server Northwind Data Source. In this video, we will manually add a Data Object from this Data Source to our configuration.

First, click Objects. Then, Add. Choose the name of the Data Source from the first dropdown. Then click the second dropdown to choose the table, view, function or stored procedure in the Data Source to add to Exago. Alternatively, to provide SQL, click the Custom SQL Object icon. In this example, we’re going to use choose the Orders table.

The object’s Alias displays to the end user in the Exago user interface, and is required. Each Data Object is required to have at least one unique key in Exago. IN the user interface, Data Objects are organized into folders. We assign the Data Object a folder here. Folders can be nested by separating them with a backslash. The next required input is the ID, an application wide unique identifier for the Data Object. IDs are required when creating multiple Data Objects that have the same name and come from the same Data Sources, but they are recommended for every Data Object regardless. Since object IDs are stored in the report files, they should never change in order to preserve the integrity of your reports. Parameters that are passed to certain Data Objects can be added here. This table does not require any Parameters, but we will revisit this menu in a future video when we set up a Stored Procedure. If multiple users or clients data is held within the same table or view, and a column exists with identifying information, use the Tenant Columns dropdown to specify which columns in the Data Object contain that information, and associate it with an Exago variable called a Tenant Parameter. Exago will then only retrieve the rows where the column value matches the corresponding parameter, which has a value set at runtime matching the current user. The Description can be used to provide an optional user friendly description of the data object. When the object is hovered over in the Data Fields Pane in any report designer, the description text will pop up in a tooltip. Column tablmetadata will be added after the object has been saved. So, we will come back to these two settings in just a moment. Use the Filter Dropdown Object to specify an alternative Data Object or Custom SQL to be queries when a user tries to assign a value to a filter. This might be initiated from the Advanced Report Designer Filter dialog, or the Filters pane of the Dashboard or ExpressView Designer. Interactive filtering in the database: when this setting is true, Dashboards with interactive filters will filter in the Data Source instead of in-memory. For tables or views, it is recommended that this setting remain true. For certain stored procedures or assembly data sources, it can be advantageous to set this to false. Consult the Exago documentation for more information. Suppress Sort and Filter ins not generally recommended for tables or views. Like interactive filtering in the database, is use mainly centers around .NET assemblies or stored procedures.

We will Apply these changes, and then return in the next video to the Column Metadata dialog. Congratulations! You’ve successfully added and partially configured a table or view to the Exago base configuration file!
