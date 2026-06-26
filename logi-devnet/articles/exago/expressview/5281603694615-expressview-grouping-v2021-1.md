---
title: "ExpressView: Grouping (v2021.1+)"
id: 5281603694615
section: "ExpressView"
category: "Exago"
url: https://devnet.logianalytics.com/hc/en-us/articles/5281603694615-ExpressView-Grouping-v2021-1
updated_at: 2022-05-03T22:09:05Z
---

# ExpressView: Grouping (v2021.1+)

# ExpressView: Grouping (*v2021.1+*)

Data may be organized in up to seven hierarchical groups. In addition to dragging-and-dropping fields to the canvas as described in the [ExpressView: Introduction (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281589443095-ExpressView-Introduction-v2021-1-) topic, groups can be manipulated with the column menu.

**Groups** nest inside of each other and establish a “for each” hierarchy. In the example below, *for each* product category, all of the products will be listed.

![AYBotH1v5j.png](https://devnet.logianalytics.com/hc/article_attachments/5432291992087/ayboth1v5j.png)![PH3fN48dtA.png](https://devnet.logianalytics.com/hc/article_attachments/5432251747607/ph3fn48dta.png)  

ExpressView with two detail fields (left) and after adding `CategoryName` as a group (right). Note the two products grouped under the Beverages and Produce categories.

Groups may be nested or layered together. In the example below, to see all of the model numbers *for each* manufacturer *for each* product category, two groups are needed: one on the category and one on the manufacturer. Since each manufacturer may have products in many categories, manufacturer should be the left-most or least-specific group. The product category will be nested inside of the manufacturer group so that *for each* manufacturer, all of the applicable categories and products in those categories are listed.

![XmE7MJOsNd.png](https://devnet.logianalytics.com/hc/article_attachments/5432222452247/xme7mjosnd.png)![kbf7weC4Uf.png](https://devnet.logianalytics.com/hc/article_attachments/5432315062039/kbf7wec4uf.png)  

An ExpressView with all columns as data fields (top) then with three data fields and two nested groups (bottom)

## Adding Groups

To create the first group on an ExpressView, drag a field from the Data Objects pane to the “Add Group” drop zone on the canvas.

![firefox_puw4rYiOiJ.png](https://devnet.logianalytics.com/hc/article_attachments/5432315121175/firefox_puw4ryioij.png)

To change a detail field to a group, either drag-and-drop the detail field column to a Group drop zone (that is the **Add Group** zone or one of the drop zones on an existing Group column) or use the **Column Menu**:

1. Open the **Column Menu** by either clicking on the **Column Menu** ![MoreOptions_Black.png](https://devnet.logianalytics.com/hc/article_attachments/5432306248471/moreoptions_black.png) icon or right-clicking on the column.
2. Click ![MenuGroup.png](https://devnet.logianalytics.com/hc/article_attachments/5432307085335/menugroup.png)**Group By This**. The column will be added as the right-most (most-specific) group.

Adding a Group will automatically add an *Ascending* **Sort** on that column. See the [ExpressView: Sorting (v2021.1+)](https://devnet.logianalytics.com/hc/en-us/articles/5281589470487-ExpressView-Sorting-v2021-1-) topic for more information.

## Changing Group Order

As the order of Groups is changed, they will be promoted (less specific) as they move left or be demoted (more specific) as they move right.

Groups may be re-ordered by simply dragging-and-dropping them from one Group drop zone to another, or by using the **Column Menu**:

1. Open the **Column Menu** by either clicking on the **Column Menu** ![MoreOptions_Black.png](https://devnet.logianalytics.com/hc/article_attachments/5432306248471/moreoptions_black.png) icon or right-clicking on the column.
2. Click ![PageUp.png](https://devnet.logianalytics.com/hc/article_attachments/5432251989783/pageup.png)**Promote Group** to promote a group to the left or ![PageDown.png](https://devnet.logianalytics.com/hc/article_attachments/5432307056279/pagedown.png)**Demote Group** to demote a group to the right.

> ![light bulb](https://devnet.logianalytics.com/hc/article_attachments/5432173099031/noteicon.jpg "Note")
>
> Dragging a group to a drop zone on a detail field column will ungroup the column and change it back to a detail field.

## Removing Groups

To ungroup a column, either:

* drag-and drop it off of the canvas,
* drag-and-drop it over a detail field column’s drop zone (to change the group to a detail field),
* or use the **Column Menu**:
  1. Open the **Column Menu** by either clicking on the **Column Menu** ![MoreOptions_Black.png](https://devnet.logianalytics.com/hc/article_attachments/5432306248471/moreoptions_black.png) icon or right-clicking on the column.
  2. Do one of the following:
     + Click ![MenuGroup.png](https://devnet.logianalytics.com/hc/article_attachments/5432307085335/menugroup.png)**Ungroup**. The column will be converted to the left-most detail field column on the report.
     + Click ![CloseButton.png](https://devnet.logianalytics.com/hc/article_attachments/5432290266263/closebutton.png)**Remove Field** to remove the column entirely.
