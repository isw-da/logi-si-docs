---
title: "Join Configuration"
id: 5281644535703
section: "Installation and Configuration"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281644535703-Join-Configuration
updated_at: 2023-04-03T17:52:19Z
---

# Join Configuration

# Join Configuration

This topic applies to the **Admin Console** > ![TreeData.png](https://devnet.logianalytics.com/hc/article_attachments/5432184487703/treedata.png)**Data** > ![TreeJoin.png](https://devnet.logianalytics.com/hc/article_attachments/5432257357847/treejoin.png)**Joins** settings.

---

Joins specify to Exago the relationship between Data Objects.

## Create, Edit, Delete Joins

* To **add** a new join click ![><noscript><img src=](https://devnet.logianalytics.com/hc/article_attachments/5432257357847/treejoin.png) icon at the top of the main menu
* right-click and select ![+](https://devnet.logianalytics.com/hc/article_attachments/5432231941911/addnew.png)**Add** from the context menu
* or to quickly add data joins, use the [**Automatic Database Discovery**](https://devnet.logianalytics.com/hc/en-us/articles/5281636352791-Automatic-Database-Discovery)![magnifying glass](https://devnet.logianalytics.com/hc/article_attachments/5432184643735/admindiscoverylarge.png) tool

- To **edit** a join either:
  * double click it
  * select it and click the **Edit** ![pencil](https://devnet.logianalytics.com/hc/article_attachments/5432227755287/adminopen.png) icon at the top of the main menu
  * right-click it and select ![pencil](https://devnet.logianalytics.com/hc/article_attachments/5432185311127/edit.png)**Edit** from the context menu
  > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
  >
  > Review the [Modifying Joins](#Modifyin) section below when making changes to joins in the Admin Console.
- To **delete** a join either:
  * select it and click the **Delete** ![AdminDelete.png](https://devnet.logianalytics.com/hc/article_attachments/5432232296599/admindelete.png) icon at the top of the main menu
  * right-click it and select ![X](https://devnet.logianalytics.com/hc/article_attachments/5432232340503/deletereportsmall.png)**Delete** from the context menu
- To **save** changes and new joins click the **Apply** or **Okay** buttons.

## Join Properties

Every join has the following properties:

#### From Object

The first Data Object you would like to join.

#### To Object

The other Data Object you would like to join.

* The order of the Data Objects is important if you have a one-to-many relation type or a Left/Right Outer Join type. See below for details.

#### Join Column(s)

Specify the field(s) of each Data Object that must match to join an entity in the From Object to an entity(s) in the To Object.

#### Join Type

Specify whether rows from either Data Object that do not have a match should or should not be included.

* **Inner** — include only rows of the *From* Object that have a match in the *To* Object and vice versa.
* **Left Outer** — include rows of the *From* Object that do not have a match in the *To* Object but not vice versa.
* **Right Outer** — include rows of the *To* Object that do not have a match in the *From* Object but not vice versa.
  > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
  >
  > SQLite Data Sources do not support right outer joins.
* **Full Outer** — include rows in either Data Object that do not have a match.
  > ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
  >
  > MySQL Data Sources and SQLite Data Sources do not support full outer joins.

#### Relationship Type

Specify if the join type is one-to-one or one-to-many.

* **One-to-One** — each row in the *From* Object can join to at most one row from the *To* Object.
* **One-to-Many** — each row in the *From* Object can join to any number of rows from the *To* Object.

#### Weight

Give a join weight in order to set its precedence when multiple join paths exist between Data Objects. The path with the higher weight will be utilized.

* A report contains three Data Objects ‘Students’, ‘Professors’ and ‘Comp Sci 101.’ Students is joined to ‘Professors’ and ‘Comp Sci 101.’ Additionally ‘Professors’ is joined to ‘Comp Sci 101.’ There are two available join paths between ‘Students’ and ‘Comp Sci 101.’ Adding weight to a join will clarify which of the two paths Exago should use.  
  ![](https://devnet.logianalytics.com/hc/article_attachments/5432238885783/image41.png)

## Modifying Joins

Although joins are created in the Admin Console, they are also saved within each individual report. If changes are made in the Admin Console, the affected reports need to refresh their joins. To do so:

1. Open the report for editing in the Report Designer.
2. From the Advanced Options > Joins menu, click the ![Refresh.png](https://devnet.logianalytics.com/hc/article_attachments/5432258806679/refresh.png)**Recreate** button.
3. Click **Okay** on the confirmation dialog.

For more information, see [Advanced Joins](https://devnet.logianalytics.com/hc/en-us/articles/5281600746903-Advanced-Joins) and [Advanced Reports: Joins](https://devnet.logianalytics.com/hc/en-us/articles/5281549160087-Advanced-Reports-Joins).

## Cross Source Joins

Data Objects from different Data Sources can be joined together.

### Caveats

* [Filter Dependency](https://devnet.logianalytics.com/hc/en-us/articles/5281549708439-Filters#Filter) only works when all data objects originate from the same Data Source.
* The data types and size of the joined columns must match exactly. For example, an `Unsigned Int` column may only be joined with another `Unsigned Int` column.

> ![red exclamation point](https://devnet.logianalytics.com/hc/article_attachments/5432173635607/criticalicon.gif "Important")
>
> Cross Source Joins are done in-memory, so this process may be memory intensive for very large data sets.
