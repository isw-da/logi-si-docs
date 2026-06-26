---
title: "Advanced Reports: Sorts"
id: 5281555992343
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281555992343-Advanced-Reports-Sorts
updated_at: 2022-05-03T22:09:21Z
---

# Advanced Reports: Sorts

# Advanced Reports: Sorts

**Sorting** orders data in a certain sequence. For each available data object, you can choose which data field should be used to sort the rows. Fields can be sorted in *ascending* or *descending*order. The way in which rows are sorted depends on the type of value in the field:

**Numeric**  
Ascending ![-->](https://devnet.logianalytics.com/hc/article_attachments/5432364512151/custom.arrow_fore.png)*Lower values*     *Higher values*  ![<--](https://devnet.logianalytics.com/hc/article_attachments/5432321688983/custom.arrow_back.png) Descending

**Date**  
Ascending ![-->](https://devnet.logianalytics.com/hc/article_attachments/5432364512151/custom.arrow_fore.png)*Past*      *Future*![<--](https://devnet.logianalytics.com/hc/article_attachments/5432321688983/custom.arrow_back.png) Descending

**Text**  
Ascending ![-->](https://devnet.logianalytics.com/hc/article_attachments/5432364512151/custom.arrow_fore.png)*A*      *Z*![custom.arrow_back.png](https://devnet.logianalytics.com/hc/article_attachments/5432321688983/custom.arrow_back.png) Descending

![custom.DepartmentsUnsorted.png](https://devnet.logianalytics.com/hc/article_attachments/5432394095511/custom.departmentsunsorted.png)![custom.DepartmentsSorted.png](https://devnet.logianalytics.com/hc/article_attachments/5432364560535/custom.departmentssorted.png)

Sorting a category by Department

A report can have multiple sorts. This can be useful when it is desired for the highest precedence sort to affect a data field where the values for multiple rows may be the same.

For example, imagine a large company with many employees. There could be multiple people with the last name Buchanan. With only a sort on *LastName*, you do not know how all the people with the last name Buchanan will be ordered amongst themselves. If this matters, then you can add a second sort on, say, the *FirstName* field, so that people with the same last names will be ordered by their first names.

## Relationship Between Sorts and Groups

**Sorts** are a prerequisite for making **Groups**. Sorting puts data in order so that data rows which share common values for the sort field are next to each other. This is essentially what grouping does as well. **Grouping** simply takes those common values, pulls them out of the rows, and makes **Sections** for each group of rows which share that value. Sorts tell the report how the data is to be grouped.

![sorted](https://devnet.logianalytics.com/hc/article_attachments/5432364560535/custom.departmentssorted.png)![grouped](https://devnet.logianalytics.com/hc/article_attachments/5432415514775/custom.departmentsgrouped.png)

Grouping a category by the Department sort

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> Set the sort precedence so that nested groups are in order of their grouping level. The outermost group should have the highest precedence, with the next levels following in order. If the precedence is set incorrectly, it could result in inconsistent data groups.

## Add, Edit, Delete Sorts

1. Click the ![SortsMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432211886103/sortsmenu.png)**Sorts** icon in the toolbar to open the **Report Sorts** dialog.  
   ![CzizrINkGB.png](https://devnet.logianalytics.com/hc/article_attachments/5432323236503/czizrinkgb.png)

   The Report Sorts dialog for a report that will first sort by the manufacturer’s name, then by the Product Category name then finally by the Product’s name
2. Add data fields to sort by first selecting a Data Object from the dropdown, and then either:
   * clicking the arrow icon to the right of the data field’s name
   * clicking the ![Add2.png](https://devnet.logianalytics.com/hc/article_attachments/5432238606103/add2.png)**Add** button at the bottom of the data field’s tree
   * double-clicking on the field’s name
   * drag-and-dropping the data object from the tree to the Sort By panel
   * clicking the ![Add2.png](https://devnet.logianalytics.com/hc/article_attachments/5432238606103/add2.png)**Add Formula** button to add a formula sort to the report. For more information, refer to the [Formula Sorts](#Formula) section of this topic.
3. Click the **Formula Editor**![Formula.png](https://devnet.logianalytics.com/hc/article_attachments/5432247626647/formula.png) icon to change this sort to a **Formula Sort**.
4. Set the **Sort Order** to either *Ascending* or *Descending* with the dropdown.
5. If necessary, change the precedence of the sorts by either:
   * clicking the **Move Item Up ![MoveGridRowUp.png](https://devnet.logianalytics.com/hc/article_attachments/5432225168663/movegridrowup.png)**or **Move Item Down**![MoveGridRowDown.png](https://devnet.logianalytics.com/hc/article_attachments/5432338912791/movegridrowdown.png) icons
   * click and drag the **Grip**![DragGrip.png](https://devnet.logianalytics.com/hc/article_attachments/5432389235351/draggrip.png) icon to move the sort to the desired location
6. Repeat steps 2–5 for any additional sorts to be added
7. To delete a sort from the panel, click the **Delete**![DeleteItem.png](https://devnet.logianalytics.com/hc/article_attachments/5432124748951/deleteitem.png) icon at the end of the row.

### Formula Sorts

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> This feature is recommended for advanced users.

It is also possible to sort by formula instead of a plain data field, to gain finer control over [Sections](https://devnet.logianalytics.com/hc/en-us/articles/5281555584663-Advanced-Reports-Design-Grid-v2021-1-#Sections).

If there is no single data field as a unique key to indicate the end of one group and the start of another (called a break), a sort formula with concatenation of two fields may be used instead. For example, *EmployeeId* plus *TerritoryId* fields:

```
={EmployeeTerritories.EmployeeId} & {EmployeeTerritories.TerritoryId}
```

Or if a plain data field would generate too many groups, sorting on a portion of a field may be helpful. For example, group on only the month and year component of a date field.

```
=Date(Year({Employees.HireDate}),Month({Employees.HireDate}),1)
```

To add a sort formula, click ![+](https://devnet.logianalytics.com/hc/article_attachments/5432238606103/add2.png)**Add Formula**, then use the **[Formula Editor](https://devnet.logianalytics.com/hc/en-us/articles/5281623158039-Formula-Editor)** to make a composite field to sort on.
