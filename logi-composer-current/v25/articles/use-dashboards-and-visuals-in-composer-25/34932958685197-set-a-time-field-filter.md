---
title: "Set a Time Field Filter"
id: 34932958685197
section: "Use Dashboards and Visuals in Composer 25"
product: "Logi Composer v25"
url: https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932958685197-Set-a-Time-Field-Filter
updated_at: 2026-05-26T22:09:41Z
---

# Set a Time Field Filter

# Set a Time Field Filter

When you select a time attribute for a visual or filter snippet, you can filter the time range you display.

**Note:** If you are using a field that has time zone information disabled (select **[Not Specified](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932879958669-Configure-Time-Bar-Defaults#Default_Time_Attribute)**), only the time-related information is shown in the user interface and exported with your data. Time zone labels are not included.

## Set a Time Range for a Time Field Filter in a Visual or Dashboard

1. Select the filter icon on the [visual](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932931145741-Apply-a-Row-Level-Filter-to-a-Visual-or-Filter-Snippet) or [dashboard](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932922987533-Apply-a-Row-Level-Filter-to-a-Dashboard) to access the appropriate filter sidebar.

   * To access the filter sidebar, select its filter icon ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167902695949) or select**Settings** from the Show More [menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933290868621-Use-the-Visual-Menu)![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167891311501) and then select the filter icon ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167891315469) on the [sidebar menu](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933295031181-Use-the-Visual-Sidebar-Menu).
   * To access the dashboard filter sidebar, select its filter icon ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167902699149). The dashboard-level filter icon is available only when all the visuals are from the same data source.

   The Filters sidebar opens, showing currently applied filters, if any.
2. Select**Add Filter**. An Add Filter work area opens to the Row tab, and includes Group and Saved tabs.
3. Select the Row tab. If the style of your visual is an arc gauge, KPI chart, table (raw data), histogram, or map markers chart, the Group tab is available, but you cannot create a group filter because all filters for these visual styles are row-level filters. If you are using the dashboard filters sidebar, the Group tab is not available.

   The Saved tab shows saved filters that you can apply to a dashboard or visual. See [Maintain Saved Filters](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932976956941-Maintain-Saved-Filters).
4. On the Row tab, select a time field you want to use from the list of available time fields. A Select Values work area opens that you can use to select values and define this filter's specifics on Range and Keysets tabs.
5. On the Range tab, you can optionally apply a null filter to the full time range. Select an **Operator** option as needed:

   * Apply `Between` to specify a time range
   * Apply `Not Between` to exclude a specified time range
   * Apply `Is NULL` to include only null values
   * Apply `Is not NULL` to hide null values

   ![set a time range, or apply appropriate NULL filter](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167198157197 "Filter Time Range")
6. If you did not apply a `Null` filter, you can use the**From** and**To** boxes to specify the time range for the filter. You can set the range in static time, dynamic time, use variables, or use preset ranges provided.

   * Select**Static Time**,**Dynamic Time**, or**Variables** in the drop-down menu.

     ![select a time range value](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167202522893 "Select time values options")

     If you select**Static Time**, the**From** and**To** boxes are filled with default dates and times. Use the boxes to select specific from and to times

     If you select**Dynamic Time**, the**From** and**To** boxes are filled with**Start of Data Set** and**End of Data Set** automatically. Use the**Condition** boxes to select different dynamic from and to times:

     ![Define condtions and offset of dynamic time ranges here](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167170724365 "Dynamic time work area")

     If you select**Variables**, define a variable for use in filtering.
   * Alternatively, select**Presets** to fill the**From** and**To** boxes with predefined time ranges provided.

     ![](https://logi-composer-v25.insightsoftware.com/hc/article_attachments/46167187212301)

     Use the filter box at the top of the presets list to locate the preset setting you want. Descriptions of each of the preset options are provided in [Preset Time Ranges](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933142584973-Preset-Time-Ranges).
7. Alternatively, select a keyset on the **Keysets** tab to use for the filter. See [Use Keysets](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933047406605-Use-Keysets).
8. After you have defined the filter specifics, select**Continue**. After confirming your changes, select**Apply**.

   * Filters you create at the dashboard level are applied to all the visuals in the dashboard that use that source.
   * Filters you create at the visual level apply only to the selected (active) visual.

**Note:** Optionally, nest multiple filters for more targeted filtering results. Select **Nest Filters**, then link multiple filters using `AND` and `OR` filtering.

## Additional Time Field Filters in a Filter Snippet

When you create a [new filter snippet](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34933003207309-Add-Filter-Snippets-to-a-Dashboard), you define the initial data type, operator, data source, and value column to use in [Data Settings](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932987838349-Use-The-Filter-Snippet-Sidebar-Menu#Data "Data settings"). You can add additional filters, including nested filters, as needed.

1. Open your existing filter snippet.
2. Select the Filters option from the [Filter Snippet sidebar](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932987838349-Use-The-Filter-Snippet-Sidebar-Menu#Filters "Filter Snippet sidebar").
3. Select **Add Filter**. An Add Filter work area opens to the Row tab, and includes Group and Saved tabs.
4. Select or create a field to filter from available options on the Row or Group tab.

   * Select an existing available field from [Attribute](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932939064717-Set-an-Attribute-Filter), [Number](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932957895565-Set-a-Numeric-Field-Filter), [Time](#), or [Hierarchy](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932931841549-Filter-by-Hierarchy-Field) and define appropriate options to use.
   * Alternatively, elect the add icon to add a [derived field](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932882620813-Derived-Field-Editor) or [custom metric](https://logi-composer-v25.insightsoftware.com/hc/en-us/articles/34932820475405-Custom-Metrics-Editor), and define appropriate options to use.
5. After you have defined the filter specifics, select **Continue**. After confirming your changes, select **Apply**.

**Note:** Optionally, nest multiple filters for more targeted filtering results. Select Nest Filters, then link multiple filters using `AND` and `OR` filtering.
