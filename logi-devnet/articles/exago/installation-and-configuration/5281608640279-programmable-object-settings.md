---
title: "Programmable Object Settings"
id: 5281608640279
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281608640279-Programmable-Object-Settings
updated_at: 2023-04-03T17:52:19Z
---

# Programmable Object Settings

# Programmable Object Settings

This topic applies to the **Admin Console** > ![TreeGeneral.png](https://devnet.logianalytics.com/hc/article_attachments/5432174178839/treegeneral.png)**General** > ![TreeGeneralNode.png](https://devnet.logianalytics.com/hc/article_attachments/5432159353239/treegeneralnode.png)**Programmable Object Settings**.

---

The **Programmable Object Settings** enable you to specify names for parameters that will be passed from Exago to stored procedures, web services, or .NET Assemblies. Using these parameters will allow filtering to be done before the data is sent to Exago. This can increase performance and reduce server resources when using Programmable Objects. For more information on these types of Data Objects see [Assembly Data Sources](https://devnet.logianalytics.com/hc/en-us/articles/5281582189591-Assembly-Data-Sources)..

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> If performance is a concern, especially for large data sets, database-joinable objects, such as tables, views, and **[table-valued functions](https://devnet.logianalytics.com/hc/en-us/articles/5281624804759-Table-Valued-Functions)**, are preferable to programmable objects.

Names for the following Parameters can be set:

#### Call Type Parameter Name

Integer that specifies what Exago needs at time of the call. There are three possible values.

* **0 : Schema** — return a data set with no rows (only the schema information).
* **1 : Data** — return a full data set.
* **2 : Filter Dropdown Values** — return data for the filter dropdown list. The Data Field requested is passed in the **Column** parameter and the filter value is passed in the **Filter** parameter (see below). The direction the user is scrolling the dropdown is passed in the **Sort** parameter as either ASC (scrolling down) or DESC (scrolling up).

#### Column Parameter Name

* **Call Type = 1:** List of columns required to execute the report, separated by commas.
* When **Call Type = 2:** Column being requested by the filter dropdown.

#### Filter Parameter Name

* When **Call Type = 1:** The filter string specific to the Data Object being called passed as standard SQL.
* When **Call Type = 2:** The current value of the filter whose dropdown is being requested.

#### Full Filter Parameter Name

* When **Call Type = 1:** The filter string for the entire report passed as standard SQL.
* When **Call Type = 2:** The Tenant and Row Level filters passed as standard SQL.

#### Sort Parameter Name

The sort string for the report.

If using call type 2, it can indicate which direction the user is scrolling a filter dropdown. ASC indicates scrolling down or DESC indicates scrolling up.

### Data Category Parameter Name pre-v2021.1

### Data Object Parameter Name v2021.1+

The Data Object’s name. Can be used in conjunction with the Data Object ID Parameter.

#### Data Object ID Parameter Name

Id of Data Object being called.
