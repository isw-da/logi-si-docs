---
title: "Apply Even Time Intervals on Pivot Tables"
id: 4402955516311
section: "Use Dashboards and Visuals in Composer v6"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402955516311-Apply-Even-Time-Intervals-on-Pivot-Tables
updated_at: 2021-08-07T17:32:46Z
---

# Apply Even Time Intervals on Pivot Tables

# Apply Even Time Intervals on Pivot Tables

For more information about even time intervals, see [*Even Time Intervals*](https://devnet.logianalytics.com/hc/en-us/articles/4402962950551-Even-Time-Intervals).

To apply even time intervals to data on pivot tables:

1. [Edit](https://devnet.logianalytics.com/hc/en-us/articles/4402955510551-Edit-a-Dashboard) a dashboard with a pivot table that uses a data source containing date or time fields.
2. If you are editing the visual in a dashboard, select **Edit Visual** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402955730967-Use-the-Visual-Menu). The [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402955735319-Use-the-Visual-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959476119/sidebar-chtsettings.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402955735319-Use-the-Visual-Sidebar-Menu). The Pivot Table Settings sidebar for the visual appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404952801175/pivot-settings_192x354.png)
4. On the sidebar, select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959554583/edit.png) in **Rows** or **Columns** and select a time field for the row or column. Select **OK**.

   The time field is selected and expands so you can select its granularity and even time intervals setting.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4404952888599/pivot-table-timeflds_192x80.png)
5. Select the granularity for the time field.
6. Slide **Include Blanks** on to request even time intervals. By default, the ability to show all values is disabled and only attributes with a value greater than NULL are displayed.
7. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4404959554839/apply-btn_106x35.png) to apply the changes to the pivot table.
