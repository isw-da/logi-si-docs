---
title: "Configuring a Stored Procedure Part 1"
id: 5281541282711
section: "Admin Video Traning Series"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281541282711-Configuring-a-Stored-Procedure-Part-1
updated_at: 2022-05-03T22:08:27Z
---

# Configuring a Stored Procedure Part 1

# Configuring a Stored Procedure Part 1

This video explains how to add a stored procedure to the Exago configuration. Learn about the various settings available for each data object. Then continue to ‘Programmable Object Settings’ for the next step in your Stored Procedure setup.

[<< Configuring a Table or View Pt 2](https://devnet.logianalytics.com/hc/en-us/articles/5281563495831-Configuring-a-Stored-Procedure-Part-2) Previous Video

Next Video [Programmable Object Settings >>](https://devnet.logianalytics.com/hc/en-us/articles/5281555184023-Programmable-Object-Settings)

## Transcript

Welcome back to the Exago Technical Training Series! In this video, we will demonstrate adding an beginning to configure a Stored Procedure as a Data Object to the Exago configuration.

The first step is to open the Exago Admin Console. To open the Admin Console, we’ll use the server IP slash web app virtual path slash Admin.aspx to build our URL. In our environment, that looks like this.

In a previous video, we configured the SQL Server Northwind Data Source. In this video, we will manually add a stored procedure Data Object to the configuration. First, right-click Objects. Then, Add to add a new Data Object from scratch. Choose the name of the Data Source from this first dropdown. Then, click the second dropdown to choose the table, view, function or stored procedure in the Data Source to add to Exago. Alternatively, to provide custom SQL, click the Custom SQL Object icon. In this example, we’ll select this stored procedure. The object’s Alias displays to the end user in the user interface and is required. Each Data Object is required to have at least one unique key in Exago. In the user interface, Data Objects are organized into folders. We assign the Data Object a folder here. Folders can be nested by separating them with a backslash. The next required input is the ID, an application wide unique identifier for the Data Object. IDs are required when creating multiple Data Objects that have the same name but come from distinct Data Sources. But they are recommended for every Data Object. Since object IDs are stored in the report files, they should never change in order to preserve the integrity of reports. Parameters that are passed to certain Data Objects can be added here. This stored procedure does require parameters. but we’ll have to add the parameters to the Exago configuration first. We’ll come back to this in just a moment. Tenant columns are not generally used with stored procedures, as tenancy more elegantly handled within a procedure. Refer to the video on setting up a table or view for more information on using tenant columns. The Description can be used to provide an optional user friendly description of the Data Object. When the object is hovered in the Data Fields Pane in any report designer, the description text will pop up in a tooltip. Column metadata will be added after the object has been saved, so we will also come back to these two settings in just a moment. Use the Filter Dropdown Object to specify an alternative Data Object or custom SQL to be queried when a user tries to assign a value to a filter. This might be initiated from the Advanced Report Designer Filter dialog or the Filters pane of the Dashboard or ExpressView Designers, for example. Finally, Interactive Filtering in the Database. When this setting is true, Dashboards incorporating interactive filters will filter in the Data Source instead of in-memory. This can reduce execution time and can reduce the number of calls to the Data Source. For stored procedures that take a long time to execute, it can be advantageous to set this setting to false so that we don’t need to wait for the entire procedure to execute each time we need to use an interactive filter. However, when using stored procedures, you’ll want to evaluate the performance with this setting enabled and disabled, to see which will work best with your use cases. Suppress Sort and Filter is generally recommended for stored procedures, when we can architect to use filter and sort parameters via Programmable Object Settings. This will prevent the use of sorts and filters in the Designers, and instead that functionality will be exposed via parameters. Exago’s Programmable Object Settings enable passing parameters from Exago in to stored procedures. Find more information on Programmable Object Settings in the next video.
