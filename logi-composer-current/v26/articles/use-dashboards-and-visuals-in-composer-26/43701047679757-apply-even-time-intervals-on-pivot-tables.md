---
title: "Apply Even Time Intervals on Pivot Tables"
id: 43701047679757
section: "Use Dashboards and Visuals in Composer 26"
product: "Logi Composer v26"
url: https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701047679757-Apply-Even-Time-Intervals-on-Pivot-Tables
updated_at: 2026-05-29T14:11:14Z
---

# Apply Even Time Intervals on Pivot Tables

# Apply Even Time Intervals on Pivot Tables

For more information about even time intervals, see [Even Time Intervals](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701077393293-Even-Time-Intervals).

**Apply even time intervals to data on pivot tables**

1. [Edit](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701014144397-Edit-a-Dashboard) a dashboard with a pivot table that uses a data source containing date or time fields.
2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701184743565-Use-the-Visual-Menu). The [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
3. Select settings ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243288000781) on the [sidebar menu](https://logi-composer-v26.insightsoftware.com/hc/en-us/articles/43701215106445-Use-the-Visual-Sidebar-Menu). The Pivot Table Settings sidebar for the visual appears.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243273270925)
4. On the sidebar, select edit ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46243288001549) in **Rows** or **Columns** and select a time field for the row or column. Select **OK**.

   The time field is selected and expands so you can select its granularity and even time intervals setting.

   ![](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242689662861)
5. Select the granularity for the time field.
6. Slide **Include Blanks** on to request even time intervals. By default, the ability to show all values is disabled and only attributes with a value greater than NULL are displayed.
7. Select **Apply** to apply the changes to the pivot table.
8. Optionally, select Filter to include a Null filter on the Range tab as needed:

   * Apply `Is not NULL` to hide null values
   * Apply `Is NULL` to include only null values

   ![set a time range, or apply appropriate NULL filter](https://logi-composer-v26.insightsoftware.com/hc/article_attachments/46242673740557 "Filter Time Range")

   Select **Continue** to add the filter, then **Apply** to apply your changes to the pivot table.
