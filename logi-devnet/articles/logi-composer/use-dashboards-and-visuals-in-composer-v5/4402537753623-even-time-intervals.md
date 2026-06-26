---
title: "Even Time Intervals"
id: 4402537753623
section: "Use Dashboards and Visuals in Composer v5"
category: "Logi Composer"
url: https://devnet.logianalytics.com/hc/en-us/articles/4402537753623-Even-Time-Intervals
updated_at: 2021-09-15T02:21:02Z
---

# Even Time Intervals

# Even Time Intervals

Even time intervals allow you to include all time groupings from your data source on a dashboard that have date or time data. You can select whether you want to display all time data, or just the data that returns a value. By default, time groups with a value of NULL (groups without any data) are not displayed.

Even time interval grouping is only available on dashboards that use a data source with date and time fields.
It is also not available for raw data tables, KPI charts, or maps.

Even time intervals can be displayed in live mode and historical playback using the time bar. See [*Live Mode and Historical Playback*](https://devnet.logianalytics.com/hc/en-us/articles/4402552905879-Live-Mode-and-Historical-Playback).

## Applying Even Time Intervals

To apply even time intervals to data on bar, box plot, donut, floating bubble, heat map, line, packed bubble, pie, scatter, tree map, and word cloud visuals:

1. [Edit](https://devnet.logianalytics.com/hc/en-us/articles/4402537743383-Editing-a-Dashboard) a dashboard with one of these visual styles that uses a data source containing date or time fields.
2. Select a time attribute for the visual Group (x-axis).
3. Select the Time Granularity box on the x-axis.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406764017303/even-time-intervals_192x237.png)
4. Slide **Include Blanks** on to request even time intervals. By default, the ability to show all values is disabled and only attributes with a value greater than NULL are displayed.

   If this is a line chart, you can also select the **Display null as zero** check box to request that null values display as zeros on the chart:

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406753491607/even-time-intervals-linecht_192x279.png)

The dashboard updates to include all values from the data source.

To apply even time intervals to data on pivot tables:

1. [Edit](https://devnet.logianalytics.com/hc/en-us/articles/4402537743383-Editing-a-Dashboard) a dashboard with a pivot table that uses a data source containing date or time fields.
2. If you are editing the visual in a dashboard, select **Edit Visual** from the [visual drop-down menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537941655-Using-the-Visual-Menu). The [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu) for the visual appears.

   If you are editing the visual from the Visual Gallery, the sidebar appears to the right of the visual.
3. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406753439511/sidebar-chtsettings.png) on the [sidebar menu](https://devnet.logianalytics.com/hc/en-us/articles/4402537948311-Using-the-Sidebar-Menu). The Pivot Table Settings sidebar for the visual appears.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406763915543/pivot-settings_192x354.png)
4. On the sidebar, select ![](https://devnet.logianalytics.com/hc/article_attachments/4406764017559/edit.png) in **Rows** or **Columns** and select a time field for the row or column. Select **OK**.

   The time field is selected and expands so you can select its granularity and even time intervals setting.

   ![](https://devnet.logianalytics.com/hc/article_attachments/4406764017815/pivot-table-timeflds_192x80.png)
5. Select the granularity for the time field.
6. Slide **Include Blanks** on to request even time intervals. By default, the ability to show all values is disabled and only attributes with a value greater than NULL are displayed.
7. Select ![](https://devnet.logianalytics.com/hc/article_attachments/4406764018199/apply-btn_106x19.png) to apply the changes to the pivot table.
