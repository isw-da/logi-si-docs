---
title: "Report Wizard: Sorts"
id: 5281573193111
section: "Advanced Reports"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281573193111-Report-Wizard-Sorts
updated_at: 2022-05-03T22:09:17Z
---

# Report Wizard: Sorts

# Report Wizard: Sorts

Sorting is the process of ordering data rows by a certain sequence. For each available data category, you can choose which data field should be used to sort the rows. Fields can be sorted in ascending or descending direction. The way in which rows are sorted depends on the type of value in the field:

**Numeric**  
![custom.arrow_fore.png](https://devnet.logianalytics.com/hc/article_attachments/5432364512151/custom.arrow_fore.png)

*Lower values     Higher values*![custom.arrow_back.png](https://devnet.logianalytics.com/hc/article_attachments/5432321688983/custom.arrow_back.png)

**Date**  
![custom.arrow_fore.png](https://devnet.logianalytics.com/hc/article_attachments/5432364512151/custom.arrow_fore.png)

*Past     Future* ![custom.arrow_back.png](https://devnet.logianalytics.com/hc/article_attachments/5432321688983/custom.arrow_back.png)

**Text**  
![custom.arrow_fore.png](https://devnet.logianalytics.com/hc/article_attachments/5432364512151/custom.arrow_fore.png)

*A     Z* ![custom.arrow_back.png](https://devnet.logianalytics.com/hc/article_attachments/5432321688983/custom.arrow_back.png)![custom.DepartmentsUnsorted.png](https://devnet.logianalytics.com/hc/article_attachments/5432394095511/custom.departmentsunsorted.png)

A list of employees, sorted by their last name in Ascending order

![custom.DepartmentsSorted.png](https://devnet.logianalytics.com/hc/article_attachments/5432364560535/custom.departmentssorted.png)

The same list of employees, sorted by their department name in Ascending order

A report can have multiple sorts. This can be useful when the highest precedence sort to affect a data field where the values for multiple rows may be the same.

For example, imagine a large company with many employees. There could be multiple people with the last name *Buchanan*. With only a sort on `LastName`, you do not know how all the people with the last name Buchanan will be ordered amongst themselves. If this matters, then you can add a second sort on, say, the `FirstName` field, so that people with the same last names will be ordered by their first names.

## Adding sorts

On the Sorts page, add data fields to sort. The precedence of the sorts starts with the highest row and moves down the list. Drag the rows up or down to change the precedence.

![screen.reportwizard_drag_sort_field.png](https://devnet.logianalytics.com/hc/article_attachments/5432406746903/screen.reportwizard_drag_sort_field.png)

Dragging a field to the Sort By pane

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Tip")
>
> Sorts apply to all report types except **CrossTab Reports**.
