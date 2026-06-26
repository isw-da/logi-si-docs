---
title: "ExpressView: Sorting (v2021.1+)"
id: 5281589470487
section: "ExpressView"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281589470487-ExpressView-Sorting-v2021-1
updated_at: 2022-05-03T22:09:04Z
---

# ExpressView: Sorting (v2021.1+)

# ExpressView: Sorting (*v2021.1+*)

Data can be ordered by applying **sorts** to the columns. Adding a group will automatically add a sort on the column. Detail fields may optionally be sorted.

Data can be sorted either in *Ascending* or *Descending* order. *Ascending* sorts start from the smallest or earliest value and end at the largest or latest value. *Descending* order is the opposite—starting from the largest value and ending at the smallest.

Sorting is indicated by a sort direction icon in the column header. Sorts on Detail Fields are also displayed on the Sorts tab of the Properties Pane, and can be modified from there as well.

* ![SortDescendingButton.png](https://devnet.logianalytics.com/hc/article_attachments/5432269225111/sortdescendingbutton.png) — this column is sorted in *Ascending* order
* ![SortAscendingButton.png](https://devnet.logianalytics.com/hc/article_attachments/5432306092695/sortascendingbutton.png) — this column is sorted in *Descending* order

![dUuk9tr0ys.png](https://devnet.logianalytics.com/hc/article_attachments/5432290050455/duuk9tr0ys.png)  

*Descending* sorts on the two **Category** and **Manufacturer** Group columns and an *Ascending* sort on the **Model #** detail field column. The **name** column is not sorted.

![60an0GR3SP.png](https://devnet.logianalytics.com/hc/article_attachments/5432251422359/60an0gr3sp.png)  

The **Sorts** tab of the **Properties Pane** for the above ExpressView shows only the *Ascending* sort on `model`

There may be several sorts on detail fields in an ExpressView. When there is more than one sort on ExpressView detail fields, a sort priority is formed. Consider the figure below, with two sorted detail fields: `City` and `Country`.

![9tBTSUgbvc.png](https://devnet.logianalytics.com/hc/article_attachments/5432273898007/9tbtsugbvc.png)

One sort must be the **primary sort** and the others will follow in priority order. Use the Sorts tab of the Properties Pane to view and modify the priority of detail field sorts.

![eoPQPqcGeg.png](https://devnet.logianalytics.com/hc/article_attachments/5432269518359/eopqpqcgeg.png)  

`Employees.Country` is the **primary** sort, and `Employees.City` is the second priority sort. All records will first be sorted in *Ascending* order by country name, and then each city within each country will be sorted in *Ascending* order

Sort priority for groups is determined by the grouping order. See [ExpressView: Grouping (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281603694615-ExpressView-Grouping-v2021-1-).

### Adding Sorts

**Groups** are automatically sorted in *Ascending* order when they are added. If a detail field has a *descending* sort when it is converted to a group, the sort direction will be changed to *Ascending*.

To add a sort on a **Detail Field**:

1. Open the **Column Menu** by either clicking on the **Column Menu** ![MoreOptions_Black.png](https://devnet.logianalytics.com/hc/article_attachments/5432306248471/moreoptions_black.png) icon or right-clicking on the column.
2. Click ![SortDescendingButton.png](https://devnet.logianalytics.com/hc/article_attachments/5432269225111/sortdescendingbutton.png)**Sort Ascending** to sort this column in *Ascending* order or ![SortAscendingButton.png](https://devnet.logianalytics.com/hc/article_attachments/5432306092695/sortascendingbutton.png)**Sort Descending** to sort this column in *Descending* order

As sorts are added to detail fields, they will be added to the bottom of the sort priority list.

### Modifying Sorts

Sort order may be changed with the Column Menu for both groups and detail fields. Sort order and priority may be changed with the Properties Pane for detail fields.

To change sort direction for groups:

1. Open the **Column Menu** by either clicking on the **Column Menu** ![MoreOptions_Black.png](https://devnet.logianalytics.com/hc/article_attachments/5432306248471/moreoptions_black.png) icon or right-clicking on the column.
2. Click ![SortDescendingButton.png](https://devnet.logianalytics.com/hc/article_attachments/5432269225111/sortdescendingbutton.png)**Sort Ascending** to sort this column in *Ascending* order or ![SortAscendingButton.png](https://devnet.logianalytics.com/hc/article_attachments/5432306092695/sortascendingbutton.png)**Sort Descending** to sort this column in *Descending* order.

To change sort order for detail fields, either:

1. Open the **Column Menu** by either clicking on the **Column Menu** ![MoreOptions_Black.png](https://devnet.logianalytics.com/hc/article_attachments/5432306248471/moreoptions_black.png) icon or right-clicking on the column.
2. Click ![SortDescendingButton.png](https://devnet.logianalytics.com/hc/article_attachments/5432269225111/sortdescendingbutton.png)**Sort Ascending** to sort this column in *Ascending* order or ![SortAscendingButton.png](https://devnet.logianalytics.com/hc/article_attachments/5432306092695/sortascendingbutton.png)**Sort Descending** to sort this column in *Descending* order.

or

1. Open the Properties Pane to the ![SortsMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432211886103/sortsmenu.png)**Sorts** tab.
2. Click either *desc* to sort this column in *Descending* order or *asc* to sort it in *Ascending* order. The currently selected direction is highlighted.

To change sort priority for detail fields, either:

1. Open the **Column Menu** by either clicking on the **Column Menu** ![MoreOptions_Black.png](https://devnet.logianalytics.com/hc/article_attachments/5432306248471/moreoptions_black.png) icon or right-clicking on the column.
2. Click ![MenuSorts.png](https://devnet.logianalytics.com/hc/article_attachments/5432290178327/menusorts.png)**Change to Primary Sort** to change this column’s sort to be the primary one.

or

1. Open the Properties Pane to the ![SortsMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432211886103/sortsmenu.png)**Sorts** tab.
2. Click and drag the **Move Grid Row ![AccordionItemDragHandle.png](https://devnet.logianalytics.com/hc/article_attachments/5432290201623/accordionitemdraghandle.png)** icon to move the sort to the desired position  
   ![ZSsKQ3kakO.png](https://devnet.logianalytics.com/hc/article_attachments/5432306402711/zsskq3kako.png)

### Removing Sorts

Groups must be sorted. To stop sorting on a group column, ungroup it.

To remove a sort on a detail field, either:

1. Open the **Column Menu** by either clicking on the **Column Menu** ![MoreOptions_Black.png](https://devnet.logianalytics.com/hc/article_attachments/5432306248471/moreoptions_black.png) icon or right-clicking on the column.
2. Click ![CloseButton.png](https://devnet.logianalytics.com/hc/article_attachments/5432290266263/closebutton.png)**Remove Sort**.

or

1. Open the Properties Pane to the ![SortsMenu.png](https://devnet.logianalytics.com/hc/article_attachments/5432211886103/sortsmenu.png)**Sorts** tab.
2. Click the **Delete** ![Delete.png](https://devnet.logianalytics.com/hc/article_attachments/5432311840791/delete.png) icon in the row of the sort to remove.
