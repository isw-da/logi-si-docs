---
title: "Modifying Pivot Table Columns and Column Widths"
id: 4402552927511
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402552927511-Modifying-Pivot-Table-Columns-and-Column-Widths
updated_at: 2021-09-15T02:23:02Z
---

# Modifying Pivot Table Columns and Column Widths

# Modifying Pivot Table Columns and Column Widths

You can modify the columns used for a pivot table. Instructions for doing this are given below.

To adjust pivot table columns:

1. Edit the pivot table you want to modify. See [*Editing Visuals*](https://devnet.logianalytics.com/hc/en-us/articles/4402537942295-Editing-Visuals).
2. If you are editing the visual in a dashboard, select **Edit Visual** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu). The [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753439511/sidebar-chtsettings.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu). The Pivot Table Settings sidebar for the visual appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763915543/pivot-settings_192x354.png)
4. To modify the columns in the pivot table:

   * Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753443863/edit2_18x17.png) in the Columns area of the Pivot Table Settings sidebar. The sidebar changes to show all the possible rows for the table.
   * Select the rows you want to add and clear the ones you want to remove. If you want to select all of the rows, select **Select All**.

     Use the search bar at the top of the sidebar to search for a field. Use the buttons under the search bar to limit the fields you see in the list.

     ![](https://devnet.logianalytics.com/hc/article_attachments/4406763913111/rdt-settings-search.png)

     | Select | To |
     | --- | --- |
     |  | See all available fields. |
     |  | Limit the field list to the available attributes. |
     |  | Limit the field list to the available numeric metrics. |
     |  | Limit the field list to the available date and time fields. |
   * After all column fields are selected, select **Apply**.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406753437463/noteicon.jpg) If the field you select is a time field, you can modify its granularity and indicate whether or not blanks (even time intervals) should be included in the time field values.
5. Select **Apply** to apply your changes to the pivot table.
6. Optionally enlarge or decrease the size of pivot table columns while the table is open for viewing. After you save the dashboard, your customized column widths are saved when you close the table and when you share or export it. To change the column widths of a pivot table, drag the separator between two columns in the appropriate direction. [Save](https://devnet.logianalytics.com/hc/en-us/articles/4402537747863-Saving-a-Dashboard) the dashboard to save the column widths.
7. You may want to control whether the Totals column appearing in the rightmost column of the table is frozen on the page (not affected by horizontal scrolling) or unfrozen (only visible when you have scrolled all way to the right).

   By default, the Totals column is frozen on the pivot table (it appears regardless of scrolling actions). To unfreeze the Totals column, slide the **Freeze Rows** slider in the Columns section of the Pivot Table Settings sidebar to the left (off The Totals column will no longer be visible unless you scroll the table all the way to the right.
8. [Save](https://devnet.logianalytics.com/hc/en-us/articles/4402537747863-Saving-a-Dashboard) the dashboard.
