---
title: "Table Context Menu"
id: 4402955715223
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955715223-Table-Context-Menu
updated_at: 2021-08-07T17:33:28Z
---

# Table Context Menu

# Table Context Menu

The column headings of a table now include a context menu you can use to perform various functions on the table, as described below. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404952786071/three-dots-menu.png) next to the column heading name to access the table context menu. The context menu has two tabs:

* The ![](https://devnet.logianalytics.com/hc/article_attachments/4404952786071/three-dots-menu.png) tab lists the functions you can perform.
* the ![](https://devnet.logianalytics.com/hc/article_attachments/4404952799383/rdt-fieldlist.png) tab lists all the available fields in the data source.

![](https://devnet.logianalytics.com/hc/article_attachments/4404952797847/rdt-contextmenu.png) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404952800151/rdt-contextmenu-time_288x284.png) or ![](https://devnet.logianalytics.com/hc/article_attachments/4404952800407/rdt-contextmenu-num_288x241.png)

Each possible menu option on the ![](https://devnet.logianalytics.com/hc/article_attachments/4404952786071/three-dots-menu.png) tab is described below.

| Menu Option | Description |
| --- | --- |
| Aggregation | Shown only for numeric fields or metrics, this option allows you to change the aggregation method for the field. Valid options are AVG, MIN, MAX, SUM, NONE, or LAST VALUE. See [*Change Metric Aggregation in Tables*](https://devnet.logianalytics.com/hc/en-us/articles/4402963091863-Change-Metric-Aggregation-in-Tables). |
| Autosize all columns | This option causes Composer to autosize all the column widths in the table. See [*Change Column Widths*](https://devnet.logianalytics.com/hc/en-us/articles/4402955713943-Change-Column-Widths). |
| Group by <field> | This option allows you to group the table by the field represented by the table column. See [*Group and Ungroup Table Data*](https://devnet.logianalytics.com/hc/en-us/articles/4402955718551-Group-and-Ungroup-Table-Data). |
| Granularity | Shown only for time fields used to group the table, this option allows you to change the granularity of the grouped time field. Valid options are **Millisecond**, **Second**, **Minute**, **Hour**, **Day**, **Week**, **Month**, and **Year**. See [*Change Time Field Granularity in Tables*](https://devnet.logianalytics.com/hc/en-us/articles/4402963098391-Change-Time-Field-Granularity-in-Tables). |
| Include Blanks | Shown only for time fields used to group the table, this option allows you apply even time intervals for the grouped time field. Select this option once to apply even time intervals. Select it a second time to remove even time intervals. See [*Even Time Intervals*](https://devnet.logianalytics.com/hc/en-us/articles/4402962950551-Even-Time-Intervals). |
| Ungroup <field> | This option removes grouping by the table column. See [*Group and Ungroup Table Data*](https://devnet.logianalytics.com/hc/en-us/articles/4402955718551-Group-and-Ungroup-Table-Data). |

You can also select and hide a column from a table using the ![](https://devnet.logianalytics.com/hc/article_attachments/4404952799383/rdt-fieldlist.png) tab on the table context menu. See [*Select Columns Using the Table Context Menu*](https://devnet.logianalytics.com/hc/en-us/articles/4402955716503-Select-Columns-Using-the-Table-Context-Menu) and [Hide Columns Using the Table Context Menu](https://devnet.logianalytics.com/hc/en-us/articles/4402963093783-Hide-Columns-Using-the-Table-Context-Menu).
