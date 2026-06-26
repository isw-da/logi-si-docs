---
title: "Group Table Data Using the Table Context Menu"
id: 4405851236759
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4405851236759-Group-Table-Data-Using-the-Table-Context-Menu
updated_at: 2021-09-21T01:30:16Z
---

# Group Table Data Using the Table Context Menu

# Group Table Data Using the Table Context Menu

If a field is selected for grouping, it is automatically selected for the table and cannot be specifically selected as a table column.

When you group table data, summarized totals are provided for numeric fields in each group. The fields used for grouping are automatically moved to the leftmost columns of the table.

To group table data using the table context menu:

1. View the table visual in a dashboard or from the Visual Gallery. Determine which field you want to use to group the data. For example, you might want to group sales data by state.
2. Locate the field in the table and select ![](https://devnet.logianalytics.com/hc/article_attachments/4406743722135/three-dots-menu.png) next to its column heading to access the table context menu.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406743729303/rdt-contextmenu.png)
3. Select **Group by <field>** on the context menu.

   The table is grouped by that field.
4. Optionally, select an aggregation level for the group field from the **Aggregation** list. The **Aggregation** list is only available for fields that have aggregation enabled in the data source and if the group field is not the first group field for the table.
5. You might want to group the table data by more than one field. For example you might want the sales data that has already been grouped by state to also be grouped by city.

   If you want to group by an additional field, locate the field in the table and select **Group by <field>** on its context menu.

   The table is grouped by that field within the grouping of any previously selected groups.
6. Save the dashboard and visual.
