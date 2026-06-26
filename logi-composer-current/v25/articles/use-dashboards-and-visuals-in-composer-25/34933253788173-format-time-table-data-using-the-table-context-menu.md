---
title: "Format Time Table Data Using the Table Context Menu"
id: 34933253788173
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933253788173-Format-Time-Table-Data-Using-the-Table-Context-Menu
updated_at: 2026-05-26T22:08:58Z
---

# Format Time Table Data Using the Table Context Menu

# Format Time Table Data Using the Table Context Menu

Numeric data and time formats [are set at the source](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932906721933-Manage-Fields#Settings). You can change them directly in a table using the table context menu. Your format changes apply directly to that visual, and affects every instance of that visual in your dashboards, without affecting the underlying source formatting. See [Format Numeric Table Data Using the Table Context Menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933268999949-Format-Numeric-Table-Data-Using-the-Table-Context-Menu). To edit date and time formatting for other visuals, see [Configure Date and Time Formatting for Visuals](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933263048077-Configure-Date-and-Time-Formatting-for-Visuals).

**Format time table data using the table context menu**

1. Select a table visual in a dashboard or in the Visual Gallery.
2. Locate the field in the table and select ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167839605133) next to its column heading to access the table context menu.

   ![select to format date time in a table column](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46166972733069 "table context menu with date time formatting")
3. Select **Format <field>** on the context menu. A Format work area opens.

   ![select formatting options in the format work area](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46166943970445 "Date Time Format Work area plain")
4. Select the appropriate date formats from available options. Options vary based on the [granularity you define](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932821901965-Configure-Date-and-Time-Formatting-Data-Sources) at the source level. See [Date Time Format Options](#DateTime). Select **Apply** to apply your changes to the data in the table column, or **Reset** reapply the source formatting.
5. Optionally, repeat for other fields in the table.
6. Save the visual, or the dashboard and visual.

**Format aggregated data using the table context menu**

1. Select a table visual in a dashboard or in the Visual Gallery.
2. Locate the field that includes aggregated in the table and select ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167839605133) next to its column heading to access the table context menu.

   ![select to format aggregated date in a table column](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46166957692941 "table context menu with date formatting aggregated")
3. Select **Format <field>** on the context menu. A Format work area opens.

   ![select formatting options in the format work area](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46166943970445 "Date Time Format Work area plain")
4. Select the appropriate date formats from available options. Options vary based on the [granularity you define](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932821901965-Configure-Date-and-Time-Formatting-Data-Sources) at the source level. See [Date Time Format Options](#DateTime). Select **Apply** to apply your changes to the data in the table column, or **Reset** reapply the source formatting.
5. Optionally, repeat for other fields in the table. You can also show or hide the time zone label using the show and hide table context menu options.
6. Save the visual, or the dashboard and visual.

## Date Time Format Options

The available fields vary based on the data available in the field.

Not all fields may be available for all time formats.

| Format Option | Description |
| --- | --- |
| Year | Select **None**, **Numeric** (2024), **2-Digit** (24), **Narrow**, or **Short**. |
| Day Of Year | Select **None** or **Short**. |
| Quarter | Select **None**, **Range**, **Narrow**, **Numeric** (1-4), or **2-Digit** (01-04). Selections for Quarter are applied only if the time granularity is set to Quarter. Not all options may be available for all time fields. |
| Month | Select **None**, **Numeric** (1-12), **2-Digit** (01-12), **Long** (January, March), **Short** (Jan, Mar), or **Narrow** (J, M). |
| Week | Select **None**, **WeekStart**, **WeekEnd**, **Range**, **Narrow** (w1-w53), **Numeric** (1-53), or **2-Digit** (01-53). |
| Weekday | Select **Long** (Friday, Sunday), **Short** (Fri, Sun), **Narrow** (F, S), or **None**. The default is **None**, to show no day of the week. |
| Day | Select **None**, **Numeric** (1-7), **2-Digit** (01-07), **Narrow**, or **Short**. |
| Hour | Select **Numeric** (1-24) or **2-Digit** (01-24). |
| Hour12 | Select a 12 or 24 hour format option for Hour12.   * **Auto** displays the hour format defined in the source data. * **True** overrides the source format, displaying the hours in 12 hour format, with an appended **AM** or **PM**. * **False** overrides the source format, displaying the hours in 24 hour format. |
| Minute | Select **Numeric** (0-59) or **2-Digit** (00-59). |
| Second | Select **Numeric** (0-59) or **2-Digit** (00-59). |
