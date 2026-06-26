---
title: "Advanced Reports: Data Objects (v2021.1+)"
id: 5281533535767
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281533535767-Advanced-Reports-Data-Objects-v2021-1
updated_at: 2022-05-03T22:09:25Z
---

# Advanced Reports: Data Objects (v2021.1+)

# Advanced Reports: Data Objects (*v2021.1+*)

A **data object** is a container for reportable information from a source of data. For example, a payroll report may include an *Employees* data object with census data such as names, addresses and hire dates as well as a *Time* data object with clock-in and clock-out times for each employee’s shift start and end.

When creating a new Advanced Report, data objects are added to the report with the **Add Data Objects** dialog.

![8FxvMmq3rt.png](https://devnet.logianalytics.com/hc/article_attachments/5432431331607/8fxvmmq3rt.png)

The Add Data Objects dialog can be recalled at any time by clicking the ![Vector.png](https://devnet.logianalytics.com/hc/article_attachments/5432326620311/vector.png)**Manage Data Objects** button in the Data Objects Pane.

## Data Objects Dialog

The **Data Objects Dialog** consists of two main parts:

* the [available data objects tree](#Availabl) on the left side
* the [selected data objects panel](#Selected) on the right side

### Available Data Objects Tree

The data objects tree on the left side of the dialog shows all of the available data objects that can be added to a report. A **Search…** field at the top of the tree allows searching for data objects by name.

![huUUJd3fPq.png](https://devnet.logianalytics.com/hc/article_attachments/5432326627991/huuujd3fpq.png)

There are two data objects in the Northwind folder of this data objects tree: `Categories` and `Products`

If the system administrator has enabled it, custom SQL statements may be added as a data object in lieu of selecting one of the existing objects. For more information, refer to the [Custom SQL Objects](#Custom) section of this topic.

Selecting a Data Object from the list and clicking on the **View Data Object Details** ![Information.png](https://devnet.logianalytics.com/hc/article_attachments/5432321848855/information.png) icon will display the names of the **fields** that are available in that object.

![w7pc9HG2YU.png](https://devnet.logianalytics.com/hc/article_attachments/5432326657047/w7pc9hg2yu.png)

CompanyName, Phone and ShipperID are fields available in the Shippers data object

### Selected Data Objects Panel

The selected data objects panel on the right side of the dialog is where the added data objects appear and is divided into three or four columns depending on system configuration.

![8FxvMmq3rt2.png](https://devnet.logianalytics.com/hc/article_attachments/5432440826007/8fxvmmq3rt2.png)

Three data objects have been added to this report: Categories, Products and Orders

* **Suppress Duplicates** (*pre-v2021.1.1*)/**Hide Repeated Values** (*v2021.1.1+*) — check this checkbox to hide repeating values on the report. For more information, review the [Dealing with Duplicate Values](https://devnet.logianalytics.com/hc/en-us/articles/5281549620503-Dealing-with-Duplicate-Values) topic.
* **Data Object Name** — the name of the data object as it appears in the available data objects tree and the system configuration
* **Alias** — this column is only available if the system administrator has enabled it. When this column is present data objects can be added more than once. This allows, for example, joining the fields on the duplicate data object to other objects, or to itself in ways other than what the system administrator has defined. For more information, refer to the [Advanced Reports: Joins](https://devnet.logianalytics.com/hc/en-us/articles/5281549160087-Advanced-Reports-Joins) topic. Each data object must be referenced by a unique alias. The alias can also be used to provide a different name for the data object.
* **![X](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png) icons** — click the **Delete**![X](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png) icon on the corresponding row to remove the data object from the report.

## Add, Edit or Delete Data Objects to/from a Report

The instructions below assume that the Add Data Objects dialog is already open on screen.

* To **add** a data object to a report, first choose the data object from the available data objects tree and then either:
  + click the arrow icon to the right of the object’s name
  + click the ![Add2.png](https://devnet.logianalytics.com/hc/article_attachments/5432238606103/add2.png)**Add** button at the bottom of the tree
  + double-click on the data object’s name
  + drag-and-drop the data object from the tree to the selected data objects panel
  + click the ![Add2.png](https://devnet.logianalytics.com/hc/article_attachments/5432238606103/add2.png)**Add SQL** button to add a custom SQL object to the report. There may not be any other data objects in the selected data objects panel for this button to have an effect. For more information, refer to the [Custom SQL Objects](#Custom) section of this topic.
* Click the **Custom SQL Object** ![SQL.png](https://devnet.logianalytics.com/hc/article_attachments/5432234099351/sql.png) icon in the Data Object Name column to **edit** it. Only **Custom SQL Objects** can be edited from the Add Data Objects dialog.
* Click the **Delete**![X](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png) icon on the corresponding row to **delete** a data object,. This removes the data object from the report, but not from the system configuration.

## Custom SQL Objects

This is an advanced feature, and the system administrator must enable it for it to be available.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> If a **Custom SQL Object** is added as a data object to a report, it may be the *only* data object on that report.

Custom SQL Objects may only be added to new report, not an existing report.

![5HG87d9rVS.png](https://devnet.logianalytics.com/hc/article_attachments/5432464530199/ykbjhavbjh.png)

Custom SQL Object dialog in *v2021.1.15+*

Writing Custom SQL Objects requires underlying knowledge of the data source architecture and its relevant SQL language.

To add a **Custom SQL Object** to a report:

1. Click the ![Add2.png](https://devnet.logianalytics.com/hc/article_attachments/5432238606103/add2.png)**Add SQL** button in the Add Data Objects dialog to open the **Custom SQL Object** dialog.
2. Provide a unique **Object Name** for the new data object. It cannot match any existing data object in the system configuration nor contain any of the following characters, including spaces: `[ ] { } . , @`
3. Choose the **Data Source** that this Custom SQL Object will retrieve data from. Not all data sources in the system may support Custom SQL objects.
4. In the large **code window** (shown with a line number 1 in the figure above), enter the full SQL statement. This statement will be inserted as a subquery when it is sent to the data source for processing.  
   > ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
   >
   > `ORDER BY` clauses and **Common Table Expressions** are not supported in subqueries. To sort a report with a Custom SQL Data Object, use the **Sorts** dialog in the Report Designer.
5. System variables called **parameters**, that change based on certain environmental situations (for example who is running the report) may optionally be added to the SQL statement by selecting the name from the dropdown and clicking the ![Add2.png](https://devnet.logianalytics.com/hc/article_attachments/5432238606103/add2.png)**Insert Parameter** button.To add a new report-level parameter to the report, and the system administrator has enabled it, first click the **New Parameter** button to open the Report Parameters dialog (*v2021.1.15+*)
6. Click the **Test**![Checkmark.png](https://devnet.logianalytics.com/hc/article_attachments/5432216091799/checkmark.png) icon to check the SQL statement for validity.
7. Click the **Unique Key Fields** list to select unique keys for the custom SQL object. Select the columns that uniquely identity a record in this object.![QXpD7SSqsy.png](https://devnet.logianalytics.com/hc/article_attachments/5432447982615/qxpd7ssqsy.png)
   1. Click the ![Add2.png](https://devnet.logianalytics.com/hc/article_attachments/5432238606103/add2.png)**Add** button to add a unique key field to the list.
   2. Select the name of the field from the dropdown, or click the **Delete**![X](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png) icon to remove it.
   3. Once all unique key fields are defined, click **Okay.**
8. Click **Okay** to close the Custom SQL Object dialog and save the object to the Add Data Objects dialog.

To edit a Custom SQL Object:

1. Click the ![Vector.png](https://devnet.logianalytics.com/hc/article_attachments/5432326620311/vector.png)**Manage Data Objects** button in the Data Objects Pane to open the Add Data Object dialog.
2. Click the **Custom SQL Object** ![SQL.png](https://devnet.logianalytics.com/hc/article_attachments/5432234099351/sql.png) icon in the Data Object Name column to open the Custom SQL Object dialog.
3. Follow the instructions in the add a **Custom SQL Object** section above to edit the object.

### Example

The following Custom SQL Object could be used to generate the basic report shown below with order IDs and dates of each order placed by each salesperson in the company in a certain month.

```
SELECT
	dbo.[Orders].[OrderID] AS c0,
	dbo.[Orders].[OrderDate] AS c1,
	dbo.[Employees].[FirstName] AS c2,
	dbo.[Employees].[LastName] AS c3,
	dbo.[Employees].[EmployeeID] AS c4,
	dbo.[Orders].[EmployeeID] AS c5
FROM dbo.[Employees]
INNER JOIN dbo.[Orders] ON (
	dbo.[Employees].[EmployeeID] = dbo.[Orders].[EmployeeID]
)
WHERE 
	Month(dbo.[Orders].[OrderDate]) = 7
```

![Employee Sales report](https://devnet.logianalytics.com/hc/article_attachments/5432472366743/656babkycz.png)

Output of the report
