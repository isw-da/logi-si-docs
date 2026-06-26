---
title: "Apply Even Time Intervals on Tables"
id: 34932833379341
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932833379341-Apply-Even-Time-Intervals-on-Tables
updated_at: 2026-05-26T22:09:56Z
---

# Apply Even Time Intervals on Tables

# Apply Even Time Intervals on Tables

If you group a table by a time field, you can select even time intervals for that time field. For more information about even time intervals, see [Even Time Intervals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932833532429-Even-Time-Intervals).

**Apply even time intervals to a time field on a table from the table context menu**

1. [Edit](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763603597-Edit-a-Dashboard) a dashboard with a table that uses a data source containing date or time fields.
2. Group the table by a time field in the data. See [Group and Ungroup Table Data](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933242142605-Group-and-Ungroup-Table-Data).
3. Select ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167931742349) next to the time field column heading to access the table context menu.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167941822861)
4. Select **Include Blanks** on the context menu. A check mark appears next to it.

   Even time intervals are applied for the time field.
5. [Save](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932815496845-Save-a-Dashboard) the dashboard.

**Apply even time intervals to a time field using the sidebar menus**

1. [Edit](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763603597-Edit-a-Dashboard) a dashboard with a table that uses a data source containing date or time fields. At least one field must be grouped.
2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). The [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
3. Select settings ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167941829005) on the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu). The Table Settings sidebar for the visual appears.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167339155469)
4. On the sidebar, select a time field in **Groups**.

   The time field is selected and expands so you can select its granularity and even time intervals setting.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167328975373)
5. Select the granularity for the time field.
6. Slide **Include Blanks** on to request even time intervals. By default, the ability to show all values is disabled and only attributes with a value greater than NULL are displayed.
7. Select **Apply** to apply the changes to the table.
8. Optionally, select Filter to include a Null filter for this field on the Range tab as needed:

   * Apply `Is not NULL` to hide null values
   * Apply `Is NULL` to include only null values

   ![set a time range, or apply appropriate NULL filter](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167363144589 "Filter Time Range")

   Select **Continue** to add the filter, then **Apply** to apply your changes to the table.
