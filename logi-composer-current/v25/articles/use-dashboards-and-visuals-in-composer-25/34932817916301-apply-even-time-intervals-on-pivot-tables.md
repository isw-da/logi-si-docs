---
title: "Apply Even Time Intervals on Pivot Tables"
id: 34932817916301
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932817916301-Apply-Even-Time-Intervals-on-Pivot-Tables
updated_at: 2026-08-24T20:33:05Z
---

# Apply Even Time Intervals on Pivot Tables

# Apply Even Time Intervals on Pivot Tables

For more information about even time intervals, see [Even Time Intervals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932833532429-Even-Time-Intervals).

**Apply even time intervals to data on pivot tables**

1. [Edit](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932763603597-Edit-a-Dashboard) a dashboard with a pivot table that uses a data source containing date or time fields.
2. If you are editing the visual in a dashboard, select **Settings** from the [visual drop-down menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu). The [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
3. Select settings ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/48374841540493) on the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu). The Pivot Table Settings sidebar for the visual appears.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/48374841543437)
4. On the sidebar, select edit ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/48374825401869) in **Rows** or **Columns** and select a time field for the row or column. Select **OK**.

   The time field is selected and expands so you can select its granularity and even time intervals setting.

   ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/48373734014349)
5. Select the granularity for the time field.
6. Slide **Include Blanks** on to request even time intervals. By default, the ability to show all values is disabled and only attributes with a value greater than NULL are displayed.
7. Select **Apply** to apply the changes to the pivot table.
8. Optionally, select Filter to include a Null filter on the Range tab as needed:

   * Apply `Is not NULL` to hide null values
   * Apply `Is NULL` to include only null values

   ![set a time range, or apply appropriate NULL filter](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/48373725763085 "Filter Time Range")

   Select **Continue** to add the filter, then **Apply** to apply your changes to the pivot table.
