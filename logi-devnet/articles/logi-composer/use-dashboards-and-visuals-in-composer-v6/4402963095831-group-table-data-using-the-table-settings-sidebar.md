---
title: "Group Table Data Using the Table Settings Sidebar"
id: 4402963095831
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402963095831-Group-Table-Data-Using-the-Table-Settings-Sidebar
updated_at: 2021-08-07T17:32:25Z
---

# Group Table Data Using the Table Settings Sidebar

# Group Table Data Using the Table Settings Sidebar

If a field is selected for grouping, it is automatically selected for the table and cannot be specifically selected as a table column.

When you group table data, summarized totals are provided for numeric fields in each group. The fields used for grouping are automatically moved to the leftmost columns of the table.

To group table data using the Table Settings sidebar:

1. If you are editing the visual in a dashboard, select **Edit Visual** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402955730967-Use-the-Visual-Menu). The [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402955735319-Use-the-Visual-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
2. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959476119/sidebar-chtsettings.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402955735319-Use-the-Visual-Sidebar-Menu). The Table Settings sidebar for the visual appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404952797463/rdt-settings_240x556.png)
3. Select and drag the field by which you want the table grouped from the **Columns** section of the Table Settings sidebar to the **Groups** section.

   The **Groups** section of the Table Settings sidebar lists the columns by which the table is grouped, in order of that grouping. In the following example, the sales data is grouped first by state, then by city within the state, and then by product category.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404959489943/rdt-group_192x533.png)
4. Optionally, select an aggregation level for the group field from the **Aggregation** list. The **Aggregation** list is only available for fields that have aggregation enabled in the data source and only if the group field is not the first group field for the table.
5. Select **Apply** to apply your changes to the table. The grouping selections are applied to the table.
6. Save the dashboard and visual.
